from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# TEAM
# ==========================================

teams = [
    {
        "name": "TEAM ALPHA",
        "win": 3,
        "loss": 0
    },
    {
        "name": "TEAM BRAVO",
        "win": 2,
        "loss": 1
    },
    {
        "name": "TEAM CHARLIE",
        "win": 2,
        "loss": 1
    },
    {
        "name": "TEAM DELTA",
        "win": 1,
        "loss": 2
    },
    {
        "name": "TEAM ECHO",
        "win": 1,
        "loss": 2
    },
    {
        "name": "TEAM FOXTROT",
        "win": 0,
        "loss": 3
    }
]


# ==========================================
# PLAYER
# ==========================================

players = [
    {
        "name": "PLAYER ONE",
        "pts": 100
    },
    {
        "name": "PLAYER TWO",
        "pts": 90
    },
    {
        "name": "PLAYER THREE",
        "pts": 80
    },
    {
        "name": "PLAYER FOUR",
        "pts": 70
    },
    {
        "name": "PLAYER FIVE",
        "pts": 60
    },
    {
        "name": "PLAYER SIX",
        "pts": 50
    }
]


# ==========================================
# PLAYOFF TEAMS
# 4 TEAM
# ==========================================

playoff_teams = [
    "TEAM ALPHA",
    "TEAM BRAVO",
    "TEAM CHARLIE",
    "TEAM DELTA"
]


# ==========================================
# SEMI FINALS
# ==========================================

semi_finals = [

    {
        "team1": "TEAM ALPHA",
        "score1": 2,
        "team2": "TEAM DELTA",
        "score2": 0
    },

    {
        "team1": "TEAM BRAVO",
        "score1": 2,
        "team2": "TEAM CHARLIE",
        "score2": 1
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
# THIRD PLACE
# ==========================================

third_place = {

    "team1": "LOSER SEMI 1",
    "score1": 0,

    "team2": "LOSER SEMI 2",
    "score2": 0

}


# ==========================================
# MOMENTS
# ==========================================

moments = []


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


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

        semi_finals=semi_finals,

        grand_final=grand_final,

        third_place=third_place,

        playoff_teams=playoff_teams
    )


# ==========================================
# MOMENTS
# ==========================================

@app.route("/moments")
def moments_page():

    return render_template(
        "moments.html",
        moments=moments
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
