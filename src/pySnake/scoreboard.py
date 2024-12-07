import pandas
from os.path import exists
from turtle import Turtle

DATA_FILE_NAME = "players_data.csv"
PLAYERS_DATABASE = {
            "players_name": [],
            "players_score": [],
        }

FONT = ("Courier", 20, "normal")


class Database:
    def __init__(self):
        self.players_name = ""

        if not exists(DATA_FILE_NAME):
            new_file = pandas.DataFrame(PLAYERS_DATABASE)
            new_file.to_csv(DATA_FILE_NAME)
        else:
            self.data_read = pandas.read_csv(DATA_FILE_NAME)
            PLAYERS_DATABASE["players_name"] = self.data_read["players_name"].tolist()
            PLAYERS_DATABASE["players_score"] = self.data_read["players_score"].tolist()

    def add_new_player(self):
        PLAYERS_DATABASE["players_name"].append(self.players_name)
        PLAYERS_DATABASE["players_score"].append(0)

    def get_highscore(self, name):
        self.players_name = name

        if self.players_name not in PLAYERS_DATABASE["players_name"]:
            self.add_new_player()

        score_index = PLAYERS_DATABASE["players_name"].index(self.players_name)
        highscore = PLAYERS_DATABASE["players_score"][score_index]
        return highscore

    def save_players_data(self, highscore):
        name_index = PLAYERS_DATABASE["players_name"].index(self.players_name)
        PLAYERS_DATABASE["players_score"][name_index] = highscore

        data_to_save = pandas.DataFrame(PLAYERS_DATABASE)
        data_to_save.to_csv(DATA_FILE_NAME)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.database = Database()

        self.score = 0
        self.highscore = 0

        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def add_point(self, points_modifier):
        self.score += 1 * points_modifier
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_players_highscore()
        self.score = 0
        self.update_score()

    def save_players_highscore(self):
        self.database.save_players_data(self.highscore)

    def get_highscore_from_database(self, players_name):
        self.highscore = self.database.get_highscore(players_name)
        self.update_score()

    def pause_info(self, pause):
        if pause:
            self.home()
            self.write("PAUSE", align="center", font=("Courier", 30, "bold"))
        else:
            self.update_score()
