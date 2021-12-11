from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db

global_db_con = get_db()
from tools.logging import logger

def handle_request():

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('mon_am')) + " WHERE day = 'mon_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('mon_pm')) + " WHERE day = 'mon_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('tues_am')) + " WHERE day = 'tues_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('tues_pm')) + " WHERE day = 'tues_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('wed_am')) + " WHERE day = 'wed_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('wed_pm')) + " WHERE day = 'wed_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('thurs_am')) + " WHERE day = 'thurs_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('thurs_pm')) + " WHERE day = 'thurs_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('fri_am')) + " WHERE day = 'fri_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = " + str(request.args.get('fri_pm')) + " WHERE day = 'fri_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")

    return json_response(status_=200, data={ })
