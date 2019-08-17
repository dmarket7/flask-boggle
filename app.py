from flask import Flask, request, render_template, redirect, flash, jsonify, session
from unittest import TestCase
from boggle import Boggle

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'anything'

BOARD_KEY = 'board'
SCORE_KEY = 'score'
HIGH_SCORE = 'high'
GAMES_PLAYED = 'games'
boggle_game = Boggle()


# def display_board()

@app.route('/')
def create_game():
    # new_game = boggle_game.make_board()
    session[BOARD_KEY] = boggle_game.make_board()
    session[SCORE_KEY] = 0

    if not session.get(HIGH_SCORE):
        session[HIGH_SCORE] = session[SCORE_KEY]
    
    if session.get(GAMES_PLAYED):
        games_played = session[GAMES_PLAYED]
        session[GAMES_PLAYED] = games_played + 1 
    else:
        session[GAMES_PLAYED] = 1
    
    return render_template('base.html', game_board=session[BOARD_KEY])


@app.route('/guess', methods=["POST"])
def check_guess():
    form_data = request.json['userGuess']
    current_board = session[BOARD_KEY]
    current_score = session[SCORE_KEY]
    print("current board: ", current_board)
    print("form data: ", form_data)
    guess_response = boggle_game.check_valid_word(current_board, form_data.lower())

    high_score = session[HIGH_SCORE] 
    print("RIGHT HERE!!!!!", session)
    if guess_response == "ok":
        session[SCORE_KEY] = len(form_data) + current_score
        if session[SCORE_KEY] > high_score:
            session[HIGH_SCORE] = session[SCORE_KEY]
    
    return jsonify(response=guess_response, score=session[SCORE_KEY], highscore=session[HIGH_SCORE])


@app.route('/finished')
def checking_stats():
    highest_score = session[HIGH_SCORE]
    current_score = session[SCORE_KEY]
    if current_score > highest_score:
        session[HIGH_SCORE] = current_score
    return jsonify(highscore=session[HIGH_SCORE])
