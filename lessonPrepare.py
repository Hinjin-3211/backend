from flask import Blueprint, jsonify, request

from ai import createLessonPrepareDocx
import db

lessonPrepare = Blueprint("lessonPrepare", __name__)
host = "/lessonPrepare"


@lessonPrepare.route(host + "/getLessonPlanDataById", methods=["post"])
def getLessonPlanDataById():
    id = request.get_json()["id"]
    sql = "select data from lessonplantable where id=%s"
    sqlData = db.select(sql, (id,))
    return jsonify(sqlData[0])


@lessonPrepare.route(host + "/getNewLessonPrepareDocx", methods=["post"])
def getNewLessonPrepareDocx():
    inputData = request.get_json()
    sql = "select data from lessonplantable where id=%s"
    sqlData = db.select(sql, (id,))
    lessonPlan = sqlData[0]["data"]
    lessonPrepare = createLessonPrepareDocx(
        lessonPlan, inputData["text"], inputData["callWord"]
    )
