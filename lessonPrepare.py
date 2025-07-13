lessonPrepare = Blueprint("lessonPrepare", __name__)
host = "/lessonPrepare"


@lessonPrepare.route(host+"/getLessonPlanDataById",methods=["post"])
def getLessonPlanDataById():
  
