#----------------------------------------------------------------------------
# Created By  Aaron Pacanowski 
# Created Date: 18/7/2022
# version ='1.0'
# ---------------------------------------------------------------------------
"Web Scraping Challenge"
# ---------------------------------------------------------------------------


from NewsScraper import NewsScraper

#ABC

def main():
    #ABC

    # TODO: These variables need to go into a YAML file for future extendabillity.
    # TODO: A method needs to be created to retrieve all these values to memory so they can then be input into the NewsScraper class. 
    # TODO: 
    sites=['https://www.abc.net.au/news/story-streams/coronavirus','https://www.abc.net.au/news/politics/','https://www.abc.net.au/news/world/','https://www.abc.net.au/news/business/','https://www.abc.net.au/news/analysis-and-opinion/','https://www.abc.net.au/news/sport/','https://www.abc.net.au/news/science/','https://www.abc.net.au/news/health/','https://www.abc.net.au/news/arts-culture/','https://www.abc.net.au/news/arts-culture/','https://www.abc.net.au/news/factcheck/','https://www.abc.net.au/news/more/']
    for site in sites:
        conn_url=site
        header_tag='h3'
        header_class='_1EAJU hMmqO MaLKt _2i9Xe _316gH _1SwKP _1BqKa _2YWka _3HiTE x9R1x pDrMR hmFfs _390V1'
        body_tag='p'
        body_class='_1HzXw'
        by_tag='span'
        by_class='_1EAJU _1gyp6 _2L258 _1BqKa _3pVeq hmFfs _2F43D'
        root_url='https://www.abc.net.au'
        full_url_bool=False
        try:
            newsScraper=NewsScraper(conn_url,header_tag,header_class,body_tag,body_class,by_tag,by_class,full_url_bool,root_url)
        except:
            print("Something went wrong reading this site.")

    # #9News
    # sites=['https://www.9news.com.au/national/4','https://www.9news.com.au/just-in/4','https://www.9news.com.au/politics/4','https://www.9news.com.au/world/4']
    # for site in sites:
    #     conn_url=site
    #     header_tag='h3'
    #     header_class='story__headline'
    #     body_tag='div'
    #     body_class='styles__Container-sc-1ylecsg-0 goULFa'
    #     by_tag='span'
    #     by_class='text--author'
    #     root_url=''
    #     full_url_bool=True
    #     try:
    #         newsScraper=NewsScraper(conn_url,header_tag,header_class,body_tag,body_class,by_tag,by_class,full_url_bool,root_url)
    #     except:
    #         print("Something went wrong reading this site.")

if __name__ == "__main__":
    main()
