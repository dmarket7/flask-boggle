from flask import Flask, request, render_template, redirect, flash, jsonify, session
from unittest import TestCase
from boggle import Boggle

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'anything'

BOARD_KEY = 'board'
RESULTS_KEY = 'response'
boggle_game = Boggle()


# def display_board()

@app.route('/')
def create_game():
    # new_game = boggle_game.make_board()
    session[BOARD_KEY] = boggle_game.make_board()

    return render_template('base.html', game_board=session[BOARD_KEY])

@app.route('/guess', methods=["POST"])
def check_guess():
    form_data = request.json['userGuess']
    
    current_board = session[BOARD_KEY]
    print("current board: ", current_board)
    print("form data: ", form_data)
    guess_response = boggle_game.check_valid_word(current_board, form_data.lower())

    print("Guess Response: ", guess_response)
    
    return jsonify(response=guess_response)
