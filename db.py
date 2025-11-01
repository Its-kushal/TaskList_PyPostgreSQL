import psycopg2

db_name = "TaskListDB"
db_user = "kushal"
db_pass = "Kushal098"
db_host = "localhost"

def getTaskList() -> list:
    conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pass, host = db_host)
    cur = conn.cursor()
    cur.execute('SELECT task_name, due_date, is_complete FROM TaskList ORDER BY due_date ASC')
    tasklist = cur.fetchall()
    cur.close()
    conn.close()
    return tasklist

def addTask(name: str, date: str):
    conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pass, host = db_host)
    cur = conn.cursor()
    cur.execute(f'INSERT INTO TaskList(task_name, due_date) VALUES(\'{name}\', \'{date}\')')
    conn.commit()
    cur.close()
    conn.close()