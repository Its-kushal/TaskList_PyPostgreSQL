import psycopg2

db_name = "TaskListDB"
db_user = "kushal"
db_pass = "Kushal098"
db_host = "localhost"

def executeQuery(query: str):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def getTaskList() -> list:
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT id, task_name, due_date, is_complete FROM TaskList ORDER BY due_date ASC;')
    tasklist = cur.fetchall()
    cur.close()
    conn.close()
    return tasklist

def addTask(name: str, date: str):
    executeQuery(f'INSERT INTO TaskList(task_name, due_date) VALUES(\'{name}\', \'{date}\');')

def updateTask(id: int, updateTask: str, updateDate: str):
    executeQuery(f'UPDATE TaskList SET task_name = \'{updateTask}\', due_date = \'{updateDate}\' WHERE id = {id};')

def deleteTask(id: int):
    executeQuery(f'DELETE FROM TaskList WHERE id = {id};')

def completeTask(id: int):
    executeQuery(f'UPDATE TaskList SET is_complete = TRUE WHERE id = {id};')