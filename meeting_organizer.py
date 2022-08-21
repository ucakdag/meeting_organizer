from flask import Flask, redirect, url_for, render_template, request, jsonify,flash
import flask
import json
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='template')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "ucaKDg.11"
app.config['MYSQL_DB'] = "meets"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/create')
def create():
        return render_template("create.html")
        
            
@app.route('/showmeets', methods=['POST', 'GET'])


def showmeets():


   if request.method == 'POST':
       cursor = mysql.connection.cursor()
       sorgu = "INSERT INTO meets VALUES(%s,%s,%s,%s,%s,%s)"
       subject = request.form.get('subject') 
       date = request.form.get('date')
       starttime = request.form.get('starttime')
       endtime = request.form.get('endtime')
       members = request.form.get('members')
       cursor.execute(sorgu,(None,subject,date,starttime,endtime,members))
       mysql.connection.commit()
       sorgu = "SELECT idmeets,meetingsubject,meetingdate,meetingstarttime,meetingendtime,members FROM meets"
       check = cursor.execute(sorgu)

       if check > 0:
           datas=cursor.fetchall()
       return (render_template("show.html",datas=datas))

   else:
       cursor = mysql.connection.cursor()
       sorgu = "SELECT idmeets,meetingsubject,meetingdate,meetingstarttime,meetingendtime,members FROM meets"
       check = cursor.execute(sorgu)

       if check > 0:
           datas=cursor.fetchall()
       return (render_template("show.html",datas=datas))
    
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    cursor = mysql.connection.cursor()
    sorgu="DELETE FROM meets.meets WHERE idmeets="+'"'+id+'"';

    check = cursor.execute(sorgu)
    sorgu2 = "SELECT idmeets,meetingsubject,meetingdate,meetingstarttime,meetingendtime,members FROM meets"
    check2 = cursor.execute(sorgu2)
  
    mysql.connection.commit()
    if check2 > 0:
           datas=cursor.fetchall()
           
    return (render_template("show.html",datas=datas))
@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        id_data = request.form['id']
        subject = request.form['subject'] 
        date = request.form['date'] 
        starttime = request.form['starttime'] 
        endtime = request.form['endtime'] 
        members = request.form['members'] 

        sorgu = 'UPDATE meets.meets SET meetingsubject = (%s), meetingdate = (%s), meetingstarttime = (%s), meetingendtime=(%s), members= (%s) WHERE idmeets=(%s);'
        cursor.execute(sorgu,(subject,date,starttime,endtime,members,id_data))
        mysql.connection.commit()
        return (redirect("/showmeets"))


  

            



 
app.run(debug=True)