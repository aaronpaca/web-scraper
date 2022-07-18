# -*- coding: utf-8 
#----------------------------------------------------------------------------
# Created By  Aaron PAcanowski 
# Created Date: 18/07/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" The DBUtil is used for performing database operations through Python code."""
# ---------------------------------------------------------------------------
import psycopg2
import re
class DBUtil:
        # Inserts an article into the database
        def insert_into_db(self,article):
            
            # TODO: This needs to be put in a yaml file
            try:
                # uncomment and insert db connection variables here
                #host_var="_______________"
                #database_var="_______________"
                #user_var="_________"
                #password_var="________"
                db_conn = psycopg2.connect(
                    host=host_var,
                    database=database_var,
                    user=user_var,
                    password=password_var)
                # create a cursor
                cur = db_conn.cursor()
                cur.execute('INSERT INTO articles."articlesContent" (title,body,authors,url) VALUES ( %s ,  %s, %s, %s )', (article.title,article.body,article.authors,article.full_url))
                

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if db_conn is not None:
                    db_conn.close()
                print('Database connection closed.')    