import psycopg2

db_name = "TaskListDB"
db_user = "kushal"
db_pass = "Kushal098"
db_host = "localhost"

def getTaskList():
    conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pass, host = db_host)
    cur = conn.cursor()
    cur.execute('SELECT task_name, is_complete FROM TaskList')
    tasklist = cur.fetchall()
    cur.close()
    conn.close()
    return tasklist