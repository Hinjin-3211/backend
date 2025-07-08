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
    sql = "select data from teachingprogramtable where term=%s and id=%s"
    sqlData = db.select(
        sql,
        (
            term,
            courseId,
        ),
    )
    print(sqlData)
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
    result = createLessonPlan(
        data["course"], data["para"], data["content"], tpData, data["callWord"]
    )
    id = data["id"]
    if id == -1:
        sql = "insert into lessonplantable (name,userId,teachingProgramId,para,createTime,changeTime,data,chapterNum,subChapterNum)values (%s,%s,%s,%s,NOW(),NOW(),%s,%s,%s)"
        sqlData = db.update(
            sql,
            (
                data["name"],
                data["userId"],
                data["teachingProgramId"],
                data["para"],
                result,
                data["index"],
                data["iindex"],
            ),
        )
        print(sqlData)
        sql = "select max(id) as id from lessonplantable"
        id = db.select(sql)[0]["id"]
    else:
        sql = "update lessonplantable set changeTime=NOW() ,data=%s where id=%s"
        sqlData = db.update(
            sql,
            (
                result,
                id,
            ),
        )
        print(sqlData)
    return jsonify({"id": id, "data": result})
