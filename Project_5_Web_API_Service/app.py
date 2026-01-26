import flask
import requests
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    response=requests.get('http://127.0.0.1:5000/api/teams')
    team=response.json()['teams']
    return render_template('home.html',team=sorted(team))

@app.route('/teamvteam')
def teamvsteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    response=requests.get(f"http://127.0.0.1:5000/api/teamvteam?team1={team1}&team2={team2}")
    response=response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    team = response1.json()['teams']
    return render_template('home.html',result=response,team=sorted(team))


app.run(debug=True,port=7000)
