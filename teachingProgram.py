import json
from flask import Blueprint, jsonify, request
import db
import logging

teachingProgram = Blueprint("teachingProgram", __name__)
host = "/teachingProgram"


@teachingProgram.route(host + "/getAllData", methods=["get"])
def getAllData():
    """获取所有教学大纲信息"""
    logging.info("执行teachingProgram的getAllData函数")
    sql = "select a.*,b.name as courseName from teachingprogramtable a,course b where a.courseId=b.id"
    sqlData = db.select(sql)
    return jsonify(sqlData)


@teachingProgram.route(host + "/getDataById", methods=["post"])
def getDataById():
    logging.info("执行teachingProgram的getDataById函数")
    data = request.get_json()["id"]
    sql = "select data from teachingprogramtable where id=%s"
    sqlData = db.select(sql, (data,))
    return jsonify(eval(sqlData[0]["data"]))
