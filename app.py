from flask import Flask, request, render_template, redirect, flash, jsonify
from unittest import TestCase
from boggle import Boggle

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'anything'

boggle_game = Boggle()

def display_board()

@app.route('/')
def create_game():
    new_game = boggle_game.make_board()

    return render_template('base.html', game_board=new_game)

@app.route('/guess')