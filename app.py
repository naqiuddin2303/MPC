from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# TEAM LEADERBOARD
# 6 TEAM
# ==========================================

teams = [
    {"name": "TEAM B", "win": 1, "loss": 0},
    {"name": "ZENITH", "win": 0, "loss": 1},
    {"name": "TEAM 3", "win": 3, "loss": 2},
    {"name": "TEAM 4", "win": 2, "loss": 3},
    {"name": "TEAM 5", "win": 1, "loss": 4},
    {"name": "TEAM 6", "win": 0, "loss": 5}
]


# ==========================================
# PLAYER LEADERBOARD
# 30 PLAYER
# ==========================================

players = [
    {"name": "PLAYER 1", "pts": 100},
    {"name": "PLAYER 2", "pts": 95},
    {"name": "PLAYER 3", "pts": 90},
    {"name": "PLAYER 4", "pts": 85},
    {"name": "PLAYER 5", "pts": 80},
    {"name": "PLAYER 6", "pts": 75},
    {"name": "PLAYER 7", "pts": 70},
    {"name": "PLAYER 8", "pts": 65},
    {"name": "PLAYER 9", "pts": 60},
    {"name": "PLAYER 10", "pts": 55},
    {"name": "PLAYER 11", "pts": 50},
    {"name": "PLAYER 12", "pts": 45},
    {"name": "PLAYER 13", "pts": 40},
    {"name": "PLAYER 14", "pts": 35},
    {"name": "PLAYER 15", "pts": 30},
    {"name": "PLAYER 16", "pts": 25},
    {"name": "PLAYER 17", "pts": 20},
    {"name": "PLAYER 18", "pts": 15},
    {"name": "PLAYER 19", "pts": 10},
    {"name": "PLAYER 20", "pts": 5},
    {"name": "PLAYER 21", "pts": 0},
    {"name": "PLAYER 22", "pts": 0},
    {"name": "PLAYER 23", "pts": 0},
    {"name": "PLAYER 24", "pts": 0},
    {"name": "PLAYER 25", "pts": 0},
    {"name": "PLAYER 26", "pts": 0},
    {"name": "PLAYER 27", "pts": 0},
    {"name": "PLAYER 28", "pts": 0},
    {"name": "PLAYER 29", "pts": 0},
    {"name": "PLAYER 30", "pts": 0}
]


# ==========================================
# PLAYOFF
# HANYA 4 TEAM
# ==========================================

playoff_teams = [
    "TEAM 1",
    "TEAM 2",
    "TEAM 3",
    "TEAM 4"
]


# ==========================================
# SEMI FINALS
# ==========================================

semi_finals = [
    {
        "team1": "TEAM 1",
        "score1": 0,
        "team2": "TEAM 4",
        "score2": 0
    },
    {
        "team1": "TEAM 2",
        "score1": 0,
        "team2": "TEAM 3",
        "score2": 0
    }
]


# ==========================================
# GRAND FINAL
# ==========================================

grand_final = {
    "team1": "WINNER SF1",
    "score1": 0,
    "team2": "WINNER SF2",
    "score2": 0
}


# ==========================================
# THIRD PLACE
# ==========================================

third_place = {
    "team1": "LOSER SF1",
    "score1": 0,
    "team2": "LOSER SF2",
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
        teams=teams,
        players=players
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
