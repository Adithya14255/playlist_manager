from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask import json
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
import random
from time import *



app = Flask(__name__)

app.secret_key='dev'

songs = [
    { 'id':'1','title': 'leo song','path':'song.mp3'},
    { 'id':'2','title': '80\'s Music','path':'song2.mp3' },
    { 'id':'3','title': 'song','path':'song3.mp3' }
]

current_playlists=[]

@app.route('/',methods=['GET', 'POST'])
def index():
    """Return homepage."""
    print("current",current_playlists)
    print("original",songs)
    # change the original return statement you wrote to the one below
    return render_template('home.html', msg="hello",playlists=songs,current_playlists=current_playlists)


@app.route('/addplaylist/<string:id>',methods=['GET', 'POST'])
def addplaylist(id):
    if request.method=='POST':
        for i in songs:
            if(id==i['id']):
                current_playlists.append(i)
                songs.remove(i)

        # change the original return statement you wrote to the one below
        return redirect(url_for('index'))

@app.route('/removeplaylist/<string:id>',methods=['GET', 'POST'])
def removeplaylist(id):
    if request.method=='POST':
        for i in current_playlists:
            if(id==i['id']):
                songs.append(i)
                current_playlists.remove(i)
        # change the original return statement you wrote to the one below
        return redirect(url_for('index'))

@app.route('/play/<int:id>',methods=['GET', 'POST'])
def play(id):
        if id==1:
            copy_playlist = random.sample(current_playlists, len(current_playlists))
            return render_template('play.html',songs=copy_playlist)
        return render_template('play.html',songs=current_playlists)

@app.route('/trial',methods=['GET', 'POST'])
def trial():
       print("hello",gmtime(time()))
       return "hello"
    

if __name__ == '__main__':
    app.run(debug=True)

