from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask import json
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
import random
from time import *



app = Flask(__name__)

app.secret_key='dev'

songs = [
    { 'id':'1','title': 'Alan Walker, Sabrina Carpenter & Farruko  - On My Way','path':'Alan Walker, Sabrina Carpenter & Farruko  - On My Way.mp3'},
    { 'id':'2','title': 'Hans Zimmer & Alan Walker - Time (Official Remix)','path':'Hans Zimmer & Alan Walker - Time (Official Remix).mp3' },
    { 'id':'3','title': 'Disfigure - Blank _ Melodic Dubstep _ NCS ','path':'Disfigure - Blank _ Melodic Dubstep _ NCS - Copyright Free Music.mp3' },
    { 'id':'4','title': 'Alan Walker - Faded.mp3 ','path':'Alan Walker - Faded.mp3' },
    { 'id':'5','title': 'Alan Walker - The Spectre','path':'Alan Walker - The Spectre.mp3' },
    { 'id':'6','title': 'Alan Walker & K-391 - Ignite (Lyrics) ft. Julie Bergan & Seungri','path':'Alan Walker & K-391 - Ignite (Lyrics) ft. Julie Bergan & Seungri.mp3' },
    { 'id':'7','title': 'Metro Boomin, A$AP Rocky, Roisee - Am I Dreaming (Visualizer)','path':'Metro Boomin, A$AP Rocky, Roisee - Am I Dreaming (Visualizer).mp3' },
    { 'id':'8','title': 'Alok & Alan Walker - Headlight (Fajar Asia Remix)','path':'Alok & Alan Walker - Headlight (Fajar Asia Remix).mp3' },
    { 'id':'9','title': 'Alan Walker & Hernandz - Endless Sea  (Official Music Video)','path':'Alan Walker & Hernandz - Endless Sea  (Official Music Video).mp3' },
    { 'id':'10','title': 'Alan Walker - Alone','path':'Alan Walker - Alone.mp3' }
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


if __name__ == '__main__':
    app.run(debug=True)

