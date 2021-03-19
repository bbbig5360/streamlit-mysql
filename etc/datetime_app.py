import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():

    if st.button('저장'):
        name = st.text_input('이름을 입력하세요')
        birth_date = st.date_input('생년월일')
        birth_time = st.time_input('시간 입력')

        try:           
            print(type(birth_date))
            print(type(birth_time))

            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'yhdb',
                password = 'yh1234'
            )

            if connection.is_connected():
                db_info = connection.get_server_info()
                print('MySQL server version : ', db_info)
                
                cursor = connection.cursor()
                
                query = '''insert into people (name, birth_date, birth_time, birth_dt)
                            values (%s, %s, %s, %s);'''
                record = (name, birth_date, birth_time, datetime.combine(birth_date, birth_time))

                print(datetime.now())
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
