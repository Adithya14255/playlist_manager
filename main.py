from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask import json
from random import randint
from time import gmtime,time
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy



app = Flask(__name__)

app.secret_key='dev'

songs = [
    { 'id':'1','title': 'song.mp3', 'description': 'Cats acting weird' },
    { 'id':'2','title': '80\'s Music', 'description': 'Don\'t stop believing!' },
    { 'id':'3','title': 'song', 'description': 'Don\'t stop believing!' }
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

@app.route('/play',methods=['GET', 'POST'])
def play():
        return render_template('play.html',list=current_playlists)
            
        
    

if __name__ == '__main__':
    app.run(debug=True)

