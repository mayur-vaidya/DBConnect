from flask import Flask, render_template, request
from DBConnect import app
import sqlite3


@app.route('/update2/', methods =['GET', 'POST'])
def update2():
    if request.method=='POST':
        try:
            name = request.form['first']
            mobile = request.form['mobile']
            fn = request.form['fn']
            ln = request.form['ln']
            add = request.form['add']
            cn = request.form['cn']

            #with sql.connect("database.db") as con:
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            print "First"
            cur.execute("UPDATE students SET firstname='"+fn+"', lastname='"+ln+"', address='"+add+"', mobile='"+cn+"' where firstname='"+name+"' and mobile='"+mobile+"'")
            con.commit()
            print "Second"
            msg = "Updation Successful!!!"
        except:
            con.rollback()
            msg= "Error in updation!!!"
        finally:
            print "Third"
            con.close()
            return render_template('update1.html', msg = msg)


@app.route('/delete1/', methods=['GET', 'POST'])
def delete1():
    if request.method=='POST':
        name=request.form['first']
        mobile=request.form['mobile']
        print "1"
        con = sqlite3.connect("database.db")
        print "2"
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        print "3"
        cur.execute("delete from students where firstname='"+name+"' and mobile='"+mobile+"'")
        print "4"
        con.commit()
        con.close()
        print "5"
        return render_template("delete2.html")
