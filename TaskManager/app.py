from flask import Flask, jsonify, render_template, request, jsonify
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('taskmanager.db')
    conn.row_factory = sqlite3.Row  
    return conn


app=Flask(__name__)


@app.route('/')
def Default():
    return render_template('index.html')

@app.route('/<string:id>')
def HomePage(id):
    if id=='addtask':
        return render_template('index.html', id='addtask')
    return render_template('index.html')

@app.route('/fetch')
def FetchDetails():
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        return jsonify({"tasks":tasks})

@app.route('/createTask',methods=['POST'])
def CreateTask():
    try:
        data=request.get_json()
        if data:
            task_name = data.get('taskname')
            description = data.get('description')
            due_date = data.get('due_date')
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO tasks (taskname, description, due_date)
                VALUES (?, ?, ?)
            ''', (task_name, description, due_date))

            conn.commit()

            conn.close()

    except:
        return jsonify({
                'success': False,
                'message': "Issue in creating task"
            })


@app.route('/delete/:ID',methods=['DELETE'])
def Deletetask():
    return render_template('index.html')

@app.route('/update/:ID',methods=['UPDATE'])
def Updatetask():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 
