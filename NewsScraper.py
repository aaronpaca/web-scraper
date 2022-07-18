# -*- coding: utf-8 
#----------------------------------------------------------------------------
# Created By  Aaron PAcanowski 
# Created Date: 18/07/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" The NewsScraper class scrapes news websites to subsequently insert into
    the database."""
# ---------------------------------------------------------------------------
# Imports Article
# ---------------------------------------------------------------------------
from bs4 import BeautifulSoup as soup
import spacy
import requests
import psycopg2
import re
from DBUtil import DBUtil
from Article import Article
class NewsScraper:
# -*- coding: utf-8 -*-
    # TODO: Satisfy the Single Responsibility Principle 
    def __init__(self,conn_url,header_tag,header_class,body_tag,body_class,by_tag,by_class,full_url_bool,root_url):
        # URL of the news website including category e.g. 'https://www.abc.net.au/news/story-streams/coronavirus'  
        self.conn_url=conn_url
        # tag used by header
        self.header_tag=header_tag
        # class used by header
        self.header_class=header_class
        # tag used by each paragraph in body
        self.body_tag=body_tag
        # class used by each paragraph in body
        self.body_class=body_class
        # tag used by "by" line such as "By John Smith"
        self.by_tag=body_tag
        # class used by "by" line such as "By John Smith"
        self.by_class=body_class
        # Boolean that says whether the 'href' in the link to
        # each article on site includes the root URL
        # e.g. for href of form 'https://www.abc.net.au/news/story-streams/coronavirus' full_url_bool =True
        # while if href is of form '/news/story-streams/coronavirus' full_url_bool =False
        self.full_url_bool=full_url_bool
        # root url such as https://www.abc.net.au
        self.root_url=root_url
        self.extractArticles(self.conn_url,full_url_bool,root_url)

    def find_author_from_str(self,by_string):
        # Given a string such as 'By John Smith', this method extracts
        # the names and organisations mentioned in the string.
        english_nlp = spacy.load('en_core_web_sm')

        text = by_string
        
        spacy_parser = english_nlp(text)
        authors_found=[]
        for entity in spacy_parser.ents:
            if str(entity.label_)=="PERSON" or str(entity.label_)=="ORG":
                authors_found.append(str(entity.text))
        # The below is required to ensure that if no authors are found,
        # it can still be of suitable form to be inputted into the database.       
        if len(authors_found)>0:
            authors_found_str=str(set(authors_found))
        else:
            authors_found_str=None

        return authors_found_str
    
    

    def extractArticles(self,conn_url,full_url_bool,root_url):
        # This method connects to websites, gets required information for input into the 
        # database.
        bsobj = self.connect_to_website(conn_url)
        headings=self.extract_headings(bsobj)
        for heading in headings:
            try:
                # saves the title to memory
                title="{}".format(heading.text)
                # initialises an Article object
                article=Article(title)
                print("Headline : "+title)
                # gets full URL and saves it to the Article object
                full_url = self.get_full_url(full_url_bool, heading, root_url)
                article.full_url=full_url
                # openes up the article link and saves to bsobj object
                page = requests.get(full_url)
                bsobj = soup(page.content,'lxml')
                # gets body and authors and saves it to the Article object
                article.body=self.get_body(bsobj, article)
                article.authors=self.find_authors(bsobj, article)
                dbUtil=DBUtil()
                dbUtil.insert_into_db(article)
            except:
                print("Error reading article.")
            

    def find_authors(self,bsobj, article):
        # extracts the authors from the article
        #  TODO: still needs to be perfected as doesn't always get all authors
        spans = self.find_by_line(bsobj)
        authors='[]'
        if spans:
            authors=self.find_author_from_str(spans.text)
            print("find_aut",authors)
            
        return authors

    def find_by_line(self, bsobj):
        # finds y line on page such as "By John Smith" 
        spans=bsobj.find(self.by_tag,{'class':self.by_class})
        return spans

    def get_body(self,bsobj, article):
        # finds body text of article 
        body=''
        for body_tag in bsobj.findAll(self.body_tag,{'class': self.body_class}):
            body+=(body_tag.text.strip())
        return body

    def get_full_url(self,full_url_bool, article, root_url):
        # gets full URL of article
        if full_url_bool:
            link=article.a['href']
        else:
            link=root_url+str(article.a['href'])
        return link
    def extract_headings(self,bsobj):
        # extracts headings
        return bsobj.findAll(self.header_tag,{'class':self.header_class})


    def connect_to_website(self,conn_url):
        # connects to website and saves in Beautiful Soup object
        r = requests.get(conn_url)
        bsobj = soup(r.content,'lxml')
        return bsobj

