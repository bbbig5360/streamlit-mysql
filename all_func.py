import streamlit as st
from func_select import run_select
from func_delete import run_delete
from func_insert import run_insert
from func_update import run_update

def main():
    menu = ['원하는 작업을 선택하세요', 'Select', 'Insert', 'Update', 'Delete'] 
    sel_menu = st.sidebar.selectbox("메뉴", menu)
  
    if sel_menu == 'Select':
        run_select()
    if sel_menu == 'Insert':
        run_insert()
    if sel_menu == 'Delete':
        run_delete()
    if sel_menu == 'Update':
        run_update()

if __name__ == '__main__':
    main()