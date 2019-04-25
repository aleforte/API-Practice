# Importing framework
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api
import markdown
import os

# Create an instance of Flask
app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    """Present some documentation"""
    with open(os.path.dirname(app.root_path) + '\\README.md', 'r') as markdown_file:
        # Read contents of file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class StudentList(Resource):
    def get(self):
        con = sqlite3.connect("./registry/database.db")

        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        con.close()
        return { "message": "Success", "data": students}, 200

    def post(self):
        fn = request.form['first_name']
        ln = request.form['last_name']
        age = request.form['age']
        with sqlite3.connect("./registry/database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO students (first_name, last_name, age) VALUES(?, ?, ?)", (fn, ln, age))
            con.commit()
                
        return { "message": "Student successfully added.", "data": [fn, ln, age]}, 201

class Student(Resource):
    def get(self, identifier):
        con = sqlite3.connect("./registry/database.db")

        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", identifier)
    
        student = cur.fetchone()
        con.close()
        if not student:
            return { "message": "Student not found", "data": {}}, 404
        else:
            return { "message": "Student found", "data": student}, 200
        

    def delete(self, identifier):
        con = sqlite3.connect("./registry/database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", identifier)
    
        student = cur.fetchone()
        if not student:
            con.close()
            return { "message": "Student not found", "data": {}}, 404
        else:
            cur.execute("DELETE FROM students WHERE id = ?", identifier)
            con.close()
            return "", 204

api.add_resource(StudentList, "/students")  
api.add_resource(Student, "/students/<string:identifier>")



