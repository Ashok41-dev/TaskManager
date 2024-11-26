from flask import Flask, jsonify, render_template
import sqlite3

db = sqlite3.connect('taskmanager.db') 

app=Flask(__name__)


@app.route('/')
def HomePage():

    return render_template('index.html')

@app.route('/fetch')
def FetchDetails():
    tasks=db.execute('Select * from tasks').fetchall()
    return jsonify({"tasks":tasks})

@app.route('/createTask')
def CreateTask():
    return render_template('index.html')

@app.route('/delete/:ID',methods=['DELETE'])
def Deletetask():
    return render_template('index.html')

@app.route('/update/:ID',methods=['UPDATE'])
def Updatetask():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 
