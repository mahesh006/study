import datetime
from flask import Flask, render_template, request
import database
import getYoutubeVideoLinks as getYT


app = Flask(__name__)

database.create_tables()
database.create_table_video()


videos = []

@app.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        entry_content = request.form.get("content")
        entry_content1 = request.form.get("content1")
        database.create_entry_video(entry_content, datetime.datetime.today().strftime("%b %d"))
      
        res = entry_content1.strip('][').split(', ')
        for words in res:
            video = getYT.searchVideoForKeyword(words)
            for indivvideo in video:
                database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"), indivvideo)
                videos.append(f'{indivvideo}')
    return render_template("home.html")



@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():         
    return render_template('index.html', videos=videos, entrie=database.retrieve_entries_video())


@app.route("/recommendations", methods=["GET", "POST"])
def recommendations():         
    return render_template('video.html', videos=videos, entries=database.retrieve_entries() )



