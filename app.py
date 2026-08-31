from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# TEAM DATA
# ==========================================

teams = [
    {
        "name": "TEAM ALPHA",
        "win": 5,
        "loss": 1
    },
    {
        "name": "TEAM BRAVO",
        "win": 4,
        "loss": 2
    },
    {
        "name": "TEAM CHARLIE",
        "win": 4,
        "loss": 2
    },
    {
        "name": "TEAM DELTA",
        "win": 3,
        "loss": 3
    },
    {
        "name": "TEAM ECHO",
        "win": 2,
        "loss": 4
    },
    {
        "name": "TEAM FOXTROT",
        "win": 1,
        "loss": 5
    }
]


# ==========================================
# PLAYER DATA
# ==========================================

players = [
    {
        "name": "PLAYER 1",
        "pts": 100
    },
    {
        "name": "PLAYER 2",
        "pts": 90
    },
    {
        "name": "PLAYER 3",
        "pts": 80
    },
    {
        "name": "PLAYER 4",
        "pts": 70
    },
    {
        "name": "PLAYER 5",
        "pts": 60
    },
    {
        "name": "PLAYER 6",
        "pts": 50
    }
]


# ==========================================
# PLAYOFF TEAMS
# ==========================================

playoff_teams = [
    "TEAM ALPHA",
    "TEAM BRAVO",
    "TEAM CHARLIE",
    "TEAM DELTA",
    "TEAM ECHO",
    "TEAM FOXTROT"
]


# ==========================================
# SEMI FINALS
# ==========================================

semi_finals = [
    {
        "team1": "TEAM ALPHA",
        "score1": 0,
        "team2": "TEAM DELTA",
        "score2": 0
    },
    {
        "team1": "TEAM BRAVO",
        "score1": 0,
        "team2": "TEAM CHARLIE",
        "score2": 0
    }
]


# ==========================================
# GRAND FINAL
# ==========================================

grand_final = {
    "team1": "TBD",
    "score1": 0,
    "team2": "TBD",
    "score2": 0
}


# ==========================================
# THIRD PLACE MATCH
# ==========================================

third_place = {
    "team1": "LOSER SEMI FINAL 1",
    "score1": 0,
    "team2": "LOSER SEMI FINAL 2",
    "score2": 0
}


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# LEADERBOARD
# ==========================================

@app.route("/leaderboard")
def leaderboard():
    return render_template(
        "leaderboard.html",
        players=players,
        teams=teams
    )


# ==========================================
# PLAYOFF
# ==========================================

@app.route("/playoff")
def playoff():
    return render_template(
        "playoff.html",
        playoff_teams=playoff_teams,
        semi_finals=semi_finals,
        grand_final=grand_final,
        third_place=third_place
    )


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
