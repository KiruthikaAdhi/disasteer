from flask import Flask, render_template
import sqlite3
import json
app = Flask(__name__)

@app.route("/")
def disasteer():
    return render_template("webapp.html")

@app.route('/getLinkIdArr' , methods = ['GET'])
def getLinkIdArr():
	conn = sqlite3.connect("disasteer.db");
	c = conn.cursor()
	sql = "select link_id from damage_road"
	c.execute(sql)
	rows = c.fetchall()
	print("Rows : ")
	print(rows)
	linkIdArr = json.dumps(rows)	
	print(linkIdArr)
	conn.close()
	return linkIdArr
