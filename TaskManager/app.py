from flask import Flask, jsonify, render_template, request, jsonify
import sqlite3

db = sqlite3.connect('taskmanager.db') 

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
    tasks=db.execute('Select * from tasks').fetchall()
    return jsonify({"tasks":tasks})

@app.route('/createTask',methods=['POST'])
def CreateTask():
    try:
        data=request.get_json()
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
