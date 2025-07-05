from flask import Blueprint, jsonify, request

from ai import createLessonPlan
import db

lessonPlan = Blueprint("lessonPlan", __name__)
host = "/lessonPlan"


@lessonPlan.route(host + "/getAllTerm", methods=["get"])
def getAllTerm():
    sqlData = db.select("select distinct term from teachingprogramtable")
    return jsonify(sqlData)


# 这里实际上是教案的id
@lessonPlan.route(host + "/getCourseByTerm", methods=["post"])
def getCourseByTerm():
    data = request.get_json()
    term = data["term"]
    sql = "select a.id,b.name from teachingprogramtable a,course b where a.courseId=b.id and a.term=%s"
    sqlData = db.select(sql, (term,))
    print(sqlData)
    return jsonify(sqlData)


@lessonPlan.route(host + "/getParaByCourse", methods=["post"])
def getParaByCourse():
    data = request.get_json()
    term = data["term"]
    courseId = data["courseId"]
    sql = "select data from teachingprogramtable where term=%s and courseId=%s"
    sqlData = db.select(
        sql,
        (
            term,
            courseId,
        ),
    )
    sqlData = eval(sqlData[0]["data"])
    result = []
    for i in range(len(sqlData)):
        temp = {}
        temp["label"] = sqlData[i]["chapter"]
        temp["value"] = f"{i}"
        temp2 = []
        for j in range(len(sqlData[i]["subChapter"])):
            temp3 = {}
            temp3["label"] = sqlData[i]["subChapter"][j]["title"]
            temp3["value"] = f"{i}-{j}"
            temp2.append(temp3)
        temp["children"] = temp2
        result.append(temp)
    return jsonify(result)


@lessonPlan.route(host + "/createNewText", methods=["post"])
def createNewText():
    data = request.get_json()
    teachingProgramId = data["teachingProgramId"]
    sql = "select data from teachingprogramtable where id=%s"
    sqlData = db.select(sql, (teachingProgramId,))
    sqlData = eval(sqlData[0]["data"])
    print(data["index"])
    tpData = sqlData[data["index"]]["subChapter"][data["iindex"]]["content"]
    createLessonPlan(
        data["course"], data["para"], data["content"], tpData, data["callWord"]
    )
    return jsonify({"id": 0})
