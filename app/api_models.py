# these molse are basically creted to define the structure of response of the api
from flask_restx import fields
from .extensions import api



student_model= api.model("Student", {    # now this will be the structure of the Student end Point
    "id": fields.Integer,
    "name": fields.String,
    # "course": fields.Nested(course_model)
})


course_model= api.model("Course", {    # now this will be the structure of the Course end Point
    "id": fields.Integer,
    "name": fields.String, 
    "student": fields.List(fields.Nested(student_model))
})

course_input_model= api.model("CourseInput",{
    "name": fields.String
})  

student_input_model= api.model("StudentInput",{
    "name": fields.String,
    "course_id": fields.Integer 
})

