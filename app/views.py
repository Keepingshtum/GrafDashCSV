from app import app

from flask import Flask,render_template, redirect,url_for,session,request

from sqlalchemy.ext.declarative import declarative_base

import pandas as pd

from sqlalchemy import create_engine, types

from sqlalchemy.types import Integer

Base = declarative_base()

@app.route("/",methods=["GET", "POST"])

def index():

    if request.method == "POST":
        csv_file = request.files["file"]
        
        # create sql engine, connect to mysql
        #not exactly the best dev practice but if it works, it works!

        engine = create_engine('mysql://newuser:password@localhost/mydb')
        #read csv lines into dataframe
        df = pd.read_csv(csv_file,error_bad_lines=False, dtype=object)

        #csv formatting starts here
        column_list = list(df)
        df['Date']=pd.to_datetime(df['Date'])


        #make sure everything is in an acceptable data format
        for j in column_list[4:]:

            df[j] =df[j].replace(regex=True,to_replace=r'\D',value=r'')

            

            df[j]=pd.to_numeric(df[j], errors ='coerce',downcast ='integer')


        #export data to sql table
        df.to_sql('mytable',con=engine,if_exists='replace')

        return redirect(url_for("templates/public/grafdash"))    
    return render_template("public/index.html")

#route to render grafana dashboard via localhost dashboard embed
@app.route("/grafdash")

def grafdash():

    return render_template('public/grafdash.html')
    
#obsolete routes, ignore
@app.route("/about",methods=["GET", "POST"])
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """
@app.route("/jinja")
def jinja():
    my_name = "Anant"
    return render_template("public/jinja.html", my_name=my_name)