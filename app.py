from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# TEAM LEADERBOARD
# 6 TEAM
# ==========================================

teams = [
    {"name": "TEAM B", "win": 1, "loss": 0},
    {"name": "Arachnid", "win": 1, "loss": 0},
    {"name": "ZENITH", "win": 0, "loss": 1},
    {"name": "TEAM E", "win": 0, "loss": 1},
    {"name": "KAN ESPORT", "win": 0, "loss": 0},
    {"name": "TEAM C", "win": 0, "loss": 0}
]


# ==========================================
# PLAYER LEADERBOARD
# 30 PLAYER
# ==========================================

players = [
    {"name": "Xylark", "pts": 5},
    {"name": "mimiii", "pts": 5},
    {"name": "ReimuHKRI",  "pts": 4},
    {"name": "Nerff Feeq.", "pts": 4},
    {"name": "Super Frince", "pts": 3},
    {"name": "It's Rezz", "pts": 3},
    {"name": "narcissist", "pts": 3},
    {"name": "FakriDude", "pts": 3},
    {"name": "Dr.moonrox", "pts": 3},
    {"name": "Capt _Kenny", "pts": 3},
    {"name": "Renzi", "pts": 3},
    {"name": "DRayz??", "pts": 2},
    {"name": "nimo1195", "pts": 2},
    {"name": "Dysprosium", "pts": 2},
    {"name": "epiee30.15", "pts": 2},
    {"name": "yookaa", "pts": 2},
    {"name": "BapakOreo", "pts": 2},
    {"name": "Natrium Klorida", "pts": 2},
    {"name": "KuremariousThelll", "pts": 2},
    {"name": "PLAYER 20B o nZ.", "pts": 0},
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
