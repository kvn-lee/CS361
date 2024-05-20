
import zmq
from tkinter import messagebox

# SOCKET SETUP

# Create context
context = zmq.Context()

#  Connect to "UI" microservice socket (5000)
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")

def BuildScoreboardString(score_list):
    """
    Function that takes a list of FishBowl scores for a given round and returns a string representing
    a scoreboard of the scores of each team for the given round.

    :param score_list:  A list of scores
    :return:            A string representing a scoreboard of all teams' scores
    """

    score_board = ""

    for team, score in enumerate(score_list):
        score_board += f"Team {team+1}'s Score: {score}"
        if team < len(score_list):
            score_board += "\n\n"

    return score_board

while True:
    score_list = socket.recv_json()

    message = BuildScoreboardString(score_list)

    messagebox.showinfo(title="FISHBOWL SCOREBOARD", message=message)

    socket.send_string("Complete")