import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():
    released_year = st.number_input('기준 년도 입력',min_value = 1500, max_value=2030)
    pages = st.number_input('기준 페이지 수 입력', min_value=0, max_value=1000)

    # option = st.radio('정렬을 선택하세요', ['오름차순','내림차순'])

    # checkbutton = st.checkbox('오름차순을 원하면 체크하세요')

    order = 'desc'
    if st.checkbox('오름차순을 원한다면 체크(아니라면 내림차순)'):
        order = 'asc'

    if st.button('조회'):
        try:           
            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )

            if connection.is_connected():
                db_info = connection.get_server_info()
                print('MySQL server version : ', db_info)
                
                cursor = connection.cursor( dictionary= True)
                # dictionary형태로 만들어서 준다. 왜냐하면 json형식이 dictionary이기 때문.

                # if option == '오름차순' and checkbutton:
                query = '''select title, released_year, pages 
                        from books
                        where released_year > %s and pages > %s
                        order by released_year '''+ order + ';'
                param = (released_year, pages)
                # 하나의 데이터를 넣은  튜플을 만들때는 ( 데이터, ) !!!!

                cursor.execute(query, param)

                result = cursor.fetchall()

                print(result)

                st.success('데이터를 불러왔습니다.')

                for data in result:
                    st.write(data)

        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()
            print('MySQL connection END')

if __name__ == '__main__':
    main()
