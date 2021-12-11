from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
import bcrypt
from random import randint
from db_con import get_db_instance, get_db

global_db_con = get_db()
from tools.logging import logger

def handle_request():
    logger.debug("Login Handle Request")
    un = str(request.args.get('username2'))
    cur = global_db_con.cursor()
    cur.execute("select * from employees where name = '" + un  + "';")
    global_db_con.commit()
    queryRSP = cur.fetchall()

    if(len(queryRSP) == 0):
        pasw = str(request.args.get('password2'))
        recvdPSS = bcrypt.hashpw( bytes(pasw,  'utf-8' ) , bcrypt.gensalt(10))
        usr = str(randint(1, 1000000))
        
        cur = global_db_con.cursor()
        cur.execute("INSERT INTO employees(admin, name, uid, password) VALUES('f', '" + un  + "', " + usr + ", '" + recvdPSS.decode() + "');")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'mon_am', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'mon_pm', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'tues_am', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'tues_pm', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'wed_am', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'wed_pm', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'thurs_am', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'thurs_pm', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'fri_am', " + "0" + ");")
        global_db_con.commit()

        cur = global_db_con.cursor()
        cur.execute("INSERT INTO hours(uid, day, hours) VALUES('" + usr + "', " +  "'fri_pm', " + "0" + ");")
        global_db_con.commit()
        print("Done inserting")
    return json_response(token = create_token(  g.jwt_data ), da={})
