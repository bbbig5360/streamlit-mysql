import streamlit as st
import mysql.connector
from mysql.connector import Error

def run_insert():

    title = st.text_input('책의 제목을 입력하세요')
    author_fname = st.text_input('작가의 이름을 입력하세요')
    author_lname = st.text_input('작가의 성씨를 입력하세요')
    released_year = st.number_input('출판년도를 입력하세요',0)
    stock_quantity = st.number_input('판매 부수를 입력하세요',0)
    pages = st.number_input('페이지 수를 입력하세요',0)
            
    if st.button('저장'):
        try:
            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )

            if connection.is_connected():
                print('MySQL start')
                
                cursor = connection.cursor()
                
                query = '''insert into books (title, author_fname, author_lname, released_year, stock_quantity, pages)
                            values (%s, %s, %s, %s, %s, %s);'''
                record = (title, author_fname, author_lname, released_year, stock_quantity, pages)

                cursor.execute(query, record)
                connection.commit()

                print( '{}개 저장됨'.format(cursor.rowcount) )

        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()
            print('MySQL connection END')
