import streamlit as st
import mysql.connector
from mysql.connector import Error

def run_update():

    book_id_list = []

    try:
        connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )
        if connection.is_connected():
            print('DB Connect ')

            cursor = connection.cursor(dictionary=True)

            query = '''select * from books'''

            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                book_id_list.append( row['book_id'] )


    except Error as e:
        print('db관련 에러 발생', e)

    finally :
        cursor.close()
        connection.close()
        print('DB connection END')


    book_id = st.number_input('바꿀 책의 id를 입력해주세요', min_value=book_id_list[0], max_value= book_id_list[-1])
    pages = st.number_input('바꿀 페이지 수를 입력하세요',0)
    stock_quantity = st.number_input('바꿀 판매량을 입력해주세요',0)

    if st.button('데이터 변경'):
        try:           
            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )

            if connection.is_connected():
                print('DB update')
                
                cursor = connection.cursor()
                
                query = """update books set pages = %s, stock_quantity = %s
                           where book_id = %s;
                        """
                param = ( pages, stock_quantity, book_id)

                cursor.execute(query, param)
                connection.commit()
            
        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()
            print('DB connection END')
