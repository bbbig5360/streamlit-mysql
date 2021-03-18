import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():
    try:
        title = st.text_input('책의 제목을 입력하세요')
        author_fname = st.text_input('작가의 이름을 입력하세요')
        author_lname = st.text_input('작가의 성씨를 입력하세요')
        released_year = st.number_input('출판년도를 입력하세요',0)
        stock_quantity = st.number_input('판매 부수를 입력하세요',0)
        pages = st.number_input('페이지 수를 입력하세요',0)
 
        if st.button('저장'):        
        # 커넥터을 가져온다.
            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )

            if connection.is_connected():
                db_info = connection.get_server_info()
                print('MySQL server version : ', db_info)
                
                # 2.커서를 가져온다.
                cursor = connection.cursor()
                
                # 3. 내가 원하는 문장 실행.
                # cursor.execute('select database();')

                
                query = '''insert into books (title, author_fname, author_lname, released_year, stock_quantity, pages)
                            values (%s, %s, %s, %s, %s, %s);'''
                record = (title, author_fname, author_lname, released_year, stock_quantity, pages)

                cursor.execute(query, record)
                connection.commit()

                print( '{}개 저장됨'.format(cursor.rowcount) )

                # 4. 실행 후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone()
                # print( 'Connected to db : ', record )
                

    except Error as e:
        print('db관련 에러 발생', e)
    
    finally :
        # 5. 데이터베이스 실행 명령을 끝냈으면, 
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print('MySQL connection END')

if __name__ == '__main__':
    main()
