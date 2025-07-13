from flask import Flask, jsonify, request
from flask_cors import CORS
from lessonPlan import lessonPlan
from login import login
from teachingProgram import teachingProgram
from lessonPrepare import lessonPrepare
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
app.register_blueprint(lessonPlan)
app.register_blueprint(login)
app.register_blueprint(teachingProgram)
app.register_blueprint(lessonPrepare)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
