import mysql.connector
conn_obj=mysql.connector.connect(host='localhost',
                        user='root',
                        password='2202',
                        database='mydata')
if conn_obj:
    print("Connection established")
else:
    print("please try again")

#cursor object
cur_object=conn_obj.cursor()
def create_table():
    cur_object.execute("create table if not exists taskstable(task Text,task_status Text,task_due_date Date)")
conn_obj.commit()
def add_data(task,task_status,task_due_date):
    cur_object.execute('INSERT INTO taskstable(task,task_status,task_due_date) values (%s,%s,%s)',(task,task_status,task_due_date))
    conn_obj.commit()

def view_all_data():
    cur_object.execute('select * from taskstable')
    data = cur_object.fetchall()
    return data

def view_unique_task():
    cur_object.execute('select distinct task from taskstable')
    data=cur_object.fetchall()
    return data

def get_task(task):
    cur_object.execute('select * from taskstable where task="{}"'.format(task))
    data=cur_object.fetchall()
    return data

def edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date):
    cur_object.execute('update taskstable set task=%s,task_status=%s,task_due_date=%s where task=%s and task_status=%s and task_due_date=%s',(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date))
    conn_obj.commit()
    data = cur_object.fetchall()

def delete_data(task):
    cur_object.execute('Delete from taskstable where task="{}"'.format(task))
    conn_obj.commit()