from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db

global_db_con = get_db()
from tools.logging import logger

def handle_request():

    cur = global_db_con.cursor()
    cur.execute("SELECT * FROM employees WHERE uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()
    queryRSP = cur.fetchall()
    return json_response(status_=200, token = create_token( g.jwt_data ), data = queryRSP)
