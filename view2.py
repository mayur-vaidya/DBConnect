from flask import Flask, render_template, request
from DBConnect import app
import sqlite3

@app.route('/user/', methods =['GET', 'POST'])
def insertion():
    if request.method=='POST':
        try:
            nm = request.form['fn']
            ln = request.form['ln']
            ad = request.form['ad']
            cn = request.form['cn']

            #with sql.connect("database.db") as con:
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            print "First"
            cur.execute("INSERT INTO students VALUES(?, ?, ?, ?)",(nm, ln, ad, cn))
            con.commit()
            print "Second"
            msg = "Insertion Successful!!!"
        except:
            con.rollback()
            msg= "Error in insertion!!!"
        finally:
            print "Third"
            con.close()
            return render_template('search.html', msg = msg)

@app.route('/find3/', methods=['GET', 'POST'])
def list():
    if request.method=='POST':
        name=request.form['first']
        mobile=request.form['mobile']
        print "1"
        con = sqlite3.connect("database.db")
        print "2"
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        print "3"
        cur.execute("select * from students where firstname='"+name+"' and mobile='"+mobile+"'")
        print "4"
        rows = cur.fetchall()
        con.close()
        print "5"
        return render_template("list.html", rows=rows)


""""@app.route('/update1/', methods=['GET', 'POST'])
def update1():
    if request.method=='POST':
        name=request.form['first']
        mobile=request.form['mobile']
        fn = request.form['fn']
        ln = request.form['ln']
        add=request.form['add']
        cn=request.form['cn']
        print "1"
        con = sqlite3.connect("database.db")
        print "2"
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        print "3"
        cur.execute("UPDATE students SET firstname='"+fn+"', lastname='"+ln+"', address='"+add+"', mobile='"+cn+"' where firstname='"+name+"' and mobile='"+mobile+"'")
        print "4"
        con.close()
        print "5"
        return render_template("update1.html")"""
