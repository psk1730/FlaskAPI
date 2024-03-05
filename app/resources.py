from flask_restx import Resource, Namespace 
from .api_models import course_model ,  student_model ,course_input_model ,student_input_model
from .model import Course ,Student 
from .extensions import db


ns= Namespace("api") # instatiating namespace that takes argument as an URL 


@ns.route("/hello")
class Hello(Resource): # hello class is going to inherit from Resource 
    def get(self): # in this clas  u define all the HTTP method that u want to support 
        return {"hello": "restx"}  # python dictonary which is jason serializable 
    
@ns.route("/courses")  
class CourseListAPI(Resource):
    @ns.marshal_list_with(course_model) # this line of code takes the return type and convert into dictonary or json serializable
    def get(self):
        return Course.query.all() # class restx does not know how to convert the reslt of query
                                  # that can be pass as api response 
    # method to create/ to add the course to data base
    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def post(self):
        print(ns.payload) # to get the information, payload has the information so it is 
                        # use to create the database 
        course= Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course ,201    
    
@ns.route("/course/<int:id>")  # this route is to handle with single entity
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        course =Course.query.get(id)
        return course 
    
    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def put(self, id):  # method to update the single entity 
        course=Course.query.get(id)
        course.name= ns.payload["name"]
        # student.cousre_id= ns.payload["ousre_id"]
        db.session.commit()
        return course 
    def delete(self,id):
        course= Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return { },204 # returning list of remaining students
    
@ns.route("/student")
class StudentListAPI(Resource):
    @ns.marshal_list_with(student_model) # this line of code takes the return type and convert into dictonary or json serializable
    def get(self):
        return Student.query.all() # class restx does not know how to convert the reslt of query
                                  # that can be pass as api response  
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name= ns.payload["name"], course_id= ns.payload["course_id"])
        db.session.adddb.session.commit()
        return student, 201
    
@ns.route("/student/<int:id>")
class StudentAPI(Resource):
    @ns.marshal_with(student_model)
    def get(self, id):
        student=Student.query.get(id)
        return student 

    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def put(self, id):  # method to update the single entity 
        student=Student.query.get(id)
        student.name= ns.payload["name"]
        # student.cousre_id= ns.payload["ousre_id"]
        db.session.commit()
        return student 
    def delete(self,id):
        student= Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return { },204 # returning list of remaining students