from flask import Blueprint, jsonify, request
import logging
import db

login = Blueprint("login", __name__)
host = "/login"


@login.route(host + "/check", methods=["post"])
def check():
    """
    根据用户名和密码检查是否登录成功
    成功为0，同时返回用户id
    密码错误为1
    用户不存在为2
    """
    logging.info("执行login中的check函数")
    data = request.get_json()
    name = data["name"]
    password = data["password"]
    sqlData = db.select("select password,id from usertable where name=%s", (name,))
    if sqlData == []:
        return jsonify(
            {
                "id": -1,
                "errorNum": 2,
            }
        )
    elif sqlData[0]["password"] != password:
        return jsonify(
            {
                "id": -1,
                "errorNum": 1,
            }
        )
    else:
        return jsonify(
            {
                "id": sqlData[0]["id"],
                "errorNum": 0,
            }
        )
