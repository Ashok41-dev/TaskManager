from flask import Flask, jsonify, redirect, render_template, request, jsonify
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('taskmanager.db')
    conn.row_factory = sqlite3.Row  
    return conn

# def create_table():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE tasks (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             taskname TEXT NOT NULL,
#             description TEXT,
#             date TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# create_table()


app=Flask(__name__)



@app.route('/')
def Default():
    return render_template('index.html')

@app.route('/<string:id>')
def HomePage(id):
    if id=='addtask':
        return render_template('index.html', id='addtask')
    elif id=='tasklist':
        redirect('/tasklist')
    elif id=='deletetask':
        redirect('/deletetask')
    elif id=='updatetask':
        redirect('/updatetask')    
    return render_template('index.html')

@app.route('/tasklist')
def FetchDetails():
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        task_list = [dict(task) for task in tasks]
        return render_template('index.html',id='tasklist',task=task_list)

@app.route('/updatetask',methods=['GET'])
def UpdateTask():
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        task_list = [dict(task) for task in tasks]
        return render_template('index.html',id='updatetask',task=task_list)
      

@app.route('/deletetask/<string:ID>', methods=['GET'])
@app.route('/deletetask', methods=['GET'])
def DeleteTask(ID=None):
        if ID:
            date=request.args.get('date')
            print('work',ID,date)
            conn = get_db_connection()
            tasks = conn.execute('delete FROM tasks where taskname=? AND date=?',(ID,date))
            conn.commit()
            tasks = conn.execute('SELECT * FROM tasks').fetchall()
            task_list = [dict(task) for task in tasks]
            return render_template('index.html',id='deletetask',task=task_list)
        else:     
            conn = get_db_connection()
            tasks = conn.execute('SELECT * FROM tasks').fetchall()
            task_list = [dict(task) for task in tasks]
            return render_template('index.html',id='deletetask',task=task_list)

# @app.route('/deletetask')
# def DeleteTask():
#         conn = get_db_connection()
#         tasks = conn.execute('SELECT * FROM tasks').fetchall()
#         task_list = [dict(task) for task in tasks]
#         return render_template('index.html',id='deletetask',task=task_list)

@app.route('/createTask', methods=['POST'])
def CreateTask():
    try:
        data = request.get_json()
        print(f"Received data: {data}")

        if data:
            task_name = data.get('taskname')
            description = data.get('description')
            date = data.get('date')

            print(f"Task Name: {task_name}, Description: {description}, Date: {date}")

            if not task_name or not date:
                raise ValueError("Task name and date are required fields.")

            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert task data into the tasks table
            cursor.execute('''
                INSERT INTO tasks (taskname, description, date)
                VALUES (?, ?, ?)''', (task_name, description, date))

            # Commit changes and close the connection
            conn.commit()
            conn.close()

            return jsonify({
                'success': True,
                'message': "Task created successfully"
            })

        else:
            raise ValueError("No task data received")

    except Exception as e:
        # Log the full exception message
        print(f"Error: {e}")
        return jsonify({
                'success': False,
                'message': "Issue in creating task",
                'error': str(e) 
            })



@app.route('/delete/:ID',methods=['DELETE'])
def Deletetask():
    return render_template('index.html')

# @app.route('/update/:ID',methods=['UPDATE'])
# def Updatetask():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 
