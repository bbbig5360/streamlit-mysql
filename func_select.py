import mysql.connector
from mysql.connector import Error
import streamlit as st
import pandas as pd
import json

def run_select():

    column_list = ['book_id', 'title', 'author_fname', 'author_lname',
                    'released_year', 'stock_quantity', 'pages']

    selected_col_list = st.multiselect('컬럼을 선택하세요', column_list)
    print(selected_col_list)
    if selected_col_list :
        column_str = ', '.join(selected_col_list)
        # 리스트를 ,를 넣으며 합쳐서 sql문으로 사용한다.
        query = 'select ' + column_str + ' from books;'
    else:
        query = '''select * from books;'''

    try:           
        connection = mysql.connector.connect(
            host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'yhdb',
            password = 'yh1234'
        )

        if connection.is_connected():
            print('MySQL start')
            
            cursor = connection.cursor(dictionary=True)

            cursor.execute(query)
            
            result = cursor.fetchall()
            
            # 파이썬의 리스트 + 딕셔너리 조합 [{},{}]을 => JSON 형식으로 바꾸는 것.
            # 파이썬에선 '이지만 json에서는 "를 쓴다.
            json_result = json.dumps(result)
            # print(type(json_result))
            # print(json_result)

            # for row in result:
            #     st.write(row)

            # 판다스의 데이터프레임으로 변환하자.
            df = pd.read_json(json_result)
            st.dataframe(df)
            
    except Error as e:
        print('db관련 에러 발생', e)
    
    finally :
        cursor.close()
        connection.close()
        print('MySQL connection END')
