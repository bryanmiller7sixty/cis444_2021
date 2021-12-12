from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import smtplib, ssl

global_db_con = get_db()
from tools.logging import logger

def handle_request():
    monAM = 0
    monPM = 0
    tuesAM = 0
    tuesPM = 0
    wedAM = 0
    wedPM = 0
    thursAM = 0
    thursPM = 0
    friAM = 0
    friPM = 0
    totalHours = 0
    cur = global_db_con.cursor()
    cur.execute("SELECT * FROM employees WHERE uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()
    queryRSP = cur.fetchall()
    empName = queryRSP[0][1]

    cur = global_db_con.cursor()
    cur.execute("SELECT * FROM hours WHERE uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()
    queryRSP = cur.fetchall()
    

    for i in range(len(queryRSP)):
        if(queryRSP[i][1] == "mon_am"):
            monAM = queryRSP[i][2]
        elif(queryRSP[i][1] == "mon_pm"):
            monPM = queryRSP[i][2]
        elif(queryRSP[i][1] == "tues_am"):
            tuesAM = queryRSP[i][2]
        elif(queryRSP[i][1] == "tues_pm"):
            tuesPM = queryRSP[i][2]
        elif(queryRSP[i][1] == "wed_am"):
            wedAM = queryRSP[i][2]
        elif(queryRSP[i][1] == "wed_pm"):
            wedPM = queryRSP[i][2]
        elif(queryRSP[i][1] == "thurs_am"):
            thursAM = queryRSP[i][2]
        elif(queryRSP[i][1] == "tues_pm"):
            thursPM = queryRSP[i][2]
        elif(queryRSP[i][1] == "fri_am"):
            friAM = queryRSP[i][2]
        elif(queryRSP[i][1] == "fri_pm"):
            friPM = queryRSP[i][2]

    if(monAM != 0):
        totalHours += ((12-monAM) + monPM)
    if(tuesAM != 0):
        totalHours += ((12-tuesAM) + tuesPM)
    if(wedAM != 0):
        totalHours += ((12-wedAM) + wedPM)
    if(thursAM != 0):
        totalHours += ((12-thursAM) + thursPM)
    if(friAM != 0):
        totalHours += ((12-friAM) + friPM)
    
    strBuilder = "Employee " + empName + " worked " + str(totalHours) + " hours."

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "mille486@cougars.csusm.edu"  # Enter your address
    receiver_email = "mille486@cougars.csusm.edu"  # Enter receiver address
    password = "password_here"
    message = strBuilder

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0  WHERE day = 'mon_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'mon_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'tues_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0  WHERE day = 'tues_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()
    

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'wed_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'wed_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'thurs_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'thurs_pm' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    cur = global_db_con.cursor()
    cur.execute("UPDATE hours SET hours = 0 WHERE day = 'fri_am' AND uid = " + str(g.jwt_data.get('sub')) + ";")
    global_db_con.commit()

    return json_response( token = create_token(  g.jwt_data ) , data = {})


