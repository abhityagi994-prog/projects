import pandas as pd
import numpy as np

ipl=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv")
#print(ipl.head())


def api_teams():
    teams = list(pd.unique(pd.concat((ipl['Team1'], ipl['Team2']))))
    d={
        'teams':teams
    }
    return d

def head_to_head(team1,team2):
    total_matches = ipl[
        ((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))]
    t1_win = total_matches[total_matches['WinningTeam'] == team1].shape[0]
    t2_win = total_matches[total_matches['WinningTeam'] == team2].shape[0]

    draws = total_matches.shape[0] - (t1_win + t2_win)

    response = {
        'total_matches': total_matches.shape[0],
        team1: t1_win,
        team2: t2_win,
        'draws': draws
    }

    return response
