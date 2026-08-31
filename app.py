from flask import Flask, render_template

app = Flask(__name__)


# ==================================================
# TEAM
# ==================================================

teams = [
    {
        "name": "TEAM ALPHA",
        "win": 5,
        "loss": 1
    },
    {
        "name": "TEAM BETA",
        "win": 4,
        "loss": 2
    },
    {
        "name": "TEAM GAMMA",
        "win": 4,
        "loss": 2
    },
    {
        "name": "TEAM DELTA",
        "win": 3,
        "loss": 3
    },
    {
        "name": "TEAM OMEGA",
        "win": 2,
        "loss": 4
    },
    {
        "name": "TEAM SIGMA",
        "win": 0,
        "loss": 6
    }
]


# ==================================================
# PLAYER
# ==================================================

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
        "pts": 85
    },
    {
        "name": "PLAYER FOUR",
        "pts": 80
    },
    {
        "name": "PLAYER FIVE",
        "pts": 75
    },
    {
        "name": "PLAYER SIX",
        "pts": 70
    }
]


# ==================================================
# PLAYOFF TEAMS
# 6 TEAM -> 4 TEAM PLAYOFF
# ==================================================

playoff_teams = [
    "TEAM ALPHA",
    "TEAM BETA",
    "TEAM GAMMA",
    "TEAM DELTA"
]


# ==================================================
# SEMI FINALS
# ==================================================

semi_finals = [

    {
        "team1": "TEAM ALPHA",
        "score1": 2,
        "team2": "TEAM DELTA",
        "score2": 0
    },

    {
        "team1": "TEAM BETA",
        "score1": 2,
        "team2": "TEAM GAMMA",
        "score2": 1
    }

]


# ==================================================
# GRAND FINAL
# ==================================================

grand_final = {

    "team1": "TEAM ALPHA",
    "score1": 0,

    "team2": "TEAM BETA",
    "score2": 0
}


# ==================================================
# THIRD PLACE
# ==================================================

third_place = {

    "team1": "TEAM DELTA",
    "score1": 0,

    "team2": "TEAM GAMMA",
    "score2": 0
}


# ==================================================
# MOMENTS
#
# Kalau belum ada video, biarkan kosong.
#
# Contoh:
#
# moments = [
#     {
#         "title": "SEMIFINAL MOMENT",
#         "video": "semifinal.mp4"
#     }
# ]
# ==================================================

moments = []


# ==================================================
# HOME
# ==================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==================================================
# LEADERBOARD
# ==================================================

@app.route("/leaderboard")
def leaderboard():

    return render_template(
        "leaderboard.html",
        players=players,
        teams=teams
    )


# ==================================================
# PLAYOFF
# ==================================================

@app.route("/playoff")
def playoff():

    return render_template(
        "playoff.html",
        playoff_teams=playoff_teams,
        semi_finals=semi_finals,
        grand_final=grand_final,
        third_place=third_place
    )


# ==================================================
# MOMENTS
# ==================================================

@app.route("/moments")
def moments_page():

    return render_template(
        "moments.html",
        moments=moments
    )


# ==================================================
# RUN SERVER
# ==================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
