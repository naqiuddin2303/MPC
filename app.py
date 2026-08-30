from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# PLAYER LEADERBOARD
# ==========================================

players = [
    {"name": "Player 01", "pts": 1500},
    {"name": "Player 02", "pts": 1450},
    {"name": "Player 03", "pts": 1400},
    {"name": "Player 04", "pts": 1350},
    {"name": "Player 05", "pts": 1300},
    {"name": "Player 06", "pts": 1250},
    {"name": "Player 07", "pts": 1200},
    {"name": "Player 08", "pts": 1150},
    {"name": "Player 09", "pts": 1100},
    {"name": "Player 10", "pts": 1050},
    {"name": "Player 11", "pts": 1000},
    {"name": "Player 12", "pts": 950},
    {"name": "Player 13", "pts": 900},
    {"name": "Player 14", "pts": 850},
    {"name": "Player 15", "pts": 800},
    {"name": "Player 16", "pts": 750},
    {"name": "Player 17", "pts": 700},
    {"name": "Player 18", "pts": 650},
    {"name": "Player 19", "pts": 600},
    {"name": "Player 20", "pts": 550},
    {"name": "Player 21", "pts": 500},
    {"name": "Player 22", "pts": 450},
    {"name": "Player 23", "pts": 400},
    {"name": "Player 24", "pts": 350},
    {"name": "Player 25", "pts": 300},
    {"name": "Player 26", "pts": 250},
    {"name": "Player 27", "pts": 200},
    {"name": "Player 28", "pts": 150},
    {"name": "Player 29", "pts": 100},
    {"name": "Player 30", "pts": 50},
]


# ==========================================
# TEAM STATISTICS
# ==========================================

teams = [
    {"name": "Team Vitality", "win": 3, "loss": 0},
    {"name": "Team Falcons PH", "win": 2, "loss": 1},
    {"name": "True Rippers", "win": 2, "loss": 1},
    {"name": "Guangzhou Gaming", "win": 1, "loss": 2},
    {"name": "Team Spirit", "win": 1, "loss": 2},
    {"name": "ONIC", "win": 0, "loss": 3},
]


# ==========================================
# QUALIFIED PLAYOFF TEAMS
# ==========================================

playoff_teams = [
    "Team Vitality",
    "Team Falcons PH",
    "True Rippers",
    "Guangzhou Gaming",
]


# ==========================================
# SEMI FINALS
# ==========================================

semi_finals = [
    {
        "team1": "Team Vitality",
        "score1": 2,
        "team2": "Guangzhou Gaming",
        "score2": 0,
    },
    {
        "team1": "Team Falcons PH",
        "score1": 2,
        "team2": "True Rippers",
        "score2": 1,
    },
]


# ==========================================
# GRAND FINAL
# ==========================================

grand_final = {
    "team1": "Team Vitality",
    "score1": 3,
    "team2": "Team Falcons PH",
    "score2": 1,
}


# ==========================================
# MOMENTS / VIDEO
# ==========================================

moments = [
    {
        "title": "MOMENT 1",
        "description": "Highlight pertandingan pertama.",
        "video": "moment1.mp4",
    },
    {
        "title": "MOMENT 2",
        "description": "Moment terbaik tournament.",
        "video": "moment2.mp4",
    },
    {
        "title": "MOMENT 3",
        "description": "Highlight playoff stage.",
        "video": "moment3.mp4",
    },
]


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
# RUN SERVER
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)