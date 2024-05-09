import streamlit as st
import pandas as pd
from dbfun import *
import plotly.express as px 
ch=st.sidebar.selectbox("Menu",['Create','Read','Update','Delete'])
st.title("welcome to todo application")
create_table()
if ch=='Create':
    st.subheader("Add records into task")
    # layout
    col1,col2 = st.columns(2)
    with col1:
        task = st.text_area("Task To Do")
    with col2:
        task_status = st.selectbox("Status",["ToDo","Doing","Done"])
        task_due_date = st.date_input("Due Date")
    if st.button("Add Task"):
        add_data(task,task_status,task_due_date)
        st.success("Successfully Added Data:{}".format(task))

elif ch=='Read':
    st.subheader("View Items")
    result = view_all_data()  # called a function
    #st.write(result)
    df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
    with st.expander("View All Data"):
        st.dataframe(df)
    with st.expander("Task Status"):
        task_df = df['Task'].value_counts().to_frame()

        task_df=task_df.reset_index()
        st.dataframe(task_df)

        p1 = px.pie(task_df,names='Task',values='count')
        st.plotly_chart(p1)

elif ch=='Update':
    st.subheader("Update records")
    #see previous records
    result=view_all_data()
    #st.write(result)
    df=pd.DataFrame(result,columns=['Task','Status','Due Date'])
    with st.expander("current data"):
        st.dataframe(df)
    #st.write(view_unique_task())
    list_of_task=[i[0] for i in view_unique_task()]
    #st.write(list_of_task)
    selected_task=st.selectbox('Task to edit',list_of_task)
    selected_result=get_task(selected_task)
    #st.write(selected_result)
    if selected_result:
        task=selected_result[0][0]
        task_status=selected_result[0][1]
        task_due_date=selected_result[0][2]
        # layout
        col1,col2 = st.columns(2)
        with col1:
            new_task = st.text_area("Task To Do",task)
        with col2:
            new_task_status = st.selectbox("Status",["ToDo","Doing","Done"])
            new_task_due_date = st.date_input("Due Date")
        if st.button("Update a task"):
            edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
            st.success(f"Taskupdation successfully {task}")
        result2=view_all_data()
        #st.write(result)
        df1=pd.DataFrame(result2,columns=['Task','Status','Due Date'])
        with st.expander("Updated data"):
            st.dataframe(df1)
    
elif ch=='Delete':
    st.subheader("Delete records")
    data=view_all_data()
    df=pd.DataFrame(data,columns=['Task','Status','Due Date'])
    with st.expander("Current available records"):
        st.dataframe(df)
    list_of_task=[i[0] for i in view_unique_task()]
    #st.write(list_of_task)
    selected_task=st.selectbox('Task to delete',list_of_task)
    #selected_result=get_task(selected_task)
    #st.write(selected_result)
    st.warning("Do You Want To Delete ::{}".format(selected_task))
    if st.button('Yes'):
        delete_data(selected_task)
        st.success("Selected task is deleted successsfully {}".format(selected_task))
    updated_data=view_all_data()
    df1=pd.DataFrame(updated_data,columns=['Task','Status','Due Date'])
    with st.expander("After deletion a record"):
        st.dataframe(df1)   