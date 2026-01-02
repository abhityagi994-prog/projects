from flask import Flask, jsonify,request
import ipl
import api_functions

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome To IPL World"


@app.route('/api/teams')
def teams():
    _teams=ipl.api_teams()
    return jsonify(_teams)

@app.route('/api/teamvteam')
def matches():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    return jsonify(ipl.head_to_head(team1,team2))

@app.route('/api/team-record')
def team_record():
    team_name=request.args.get('team')
    return api_functions.teamAPI(team_name)

@app.route('/api/batsman-record')
def batsman_record():
    batsman_name=request.args.get('batsman')
    return api_functions.batsmanAPI(batsman_name)

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name=request.args.get('bowler')
    return api_functions.bowlerAPI(bowler_name)

app.run(debug=True)

