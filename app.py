from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# TEAM DATA
# ==========================================

teams = [
    {"name": "TEAM ALPHA", "win": 5, "loss": 1},
    {"name": "TEAM BRAVO", "win": 4, "loss": 2},
    {"name": "TEAM CHARLIE", "win": 4, "loss": 2},
    {"name": "TEAM DELTA", "win": 3, "loss": 3},
    {"name": "TEAM ECHO", "win": 2, "loss": 4},
    {"name": "TEAM FOXTROT", "win": 0, "loss": 6},
]


# ==========================================
# PLAYER DATA
# ==========================================

players = [
    {"name": "Player 1", "pts": 100},
    {"name": "Player 2", "pts": 90},
    {"name": "Player 3", "pts": 80},
    {"name": "Player 4", "pts": 70},
    {"name": "Player 5", "pts": 60},
    {"name": "Player 6", "pts": 50},
    {"name": "Player 7", "pts": 45},
    {"name": "Player 8", "pts": 40},
    {"name": "Player 9", "pts": 35},
    {"name": "Player 10", "pts": 30},
]


# ==========================================
# PLAYOFF TEAMS
# 4 TEAM TERATAS DARIPADA 6 TEAM
# ==========================================

playoff_teams = [
    teams[0]["name"],
    teams[1]["name"],
    teams[2]["name"],
    teams[3]["name"]
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
    "team1": "LOSER SEMI 1",
    "score1": 0,
    "team2": "LOSER SEMI 2",
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
        semi_finals=semi_finals,
        grand_final=grand_final,
        third_place=third_place,
        playoff_teams=playoff_teams
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
