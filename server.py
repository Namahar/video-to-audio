from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/formData', methods=['POST'])
def formData():

   # get form data in dictionary
   # index with url key
   url = request.form['url']
   print(url)

   # make youtube-dl command
   command = 'python3 youtube_dl/__main__.py -x --audio-format "mp3" --audio-quality 0 --ffmpeg-location ffmpeg-4.2.1/ffmpeg ' + url

   os.system(command)

   # return to index page with proper url route
   return redirect('/', code=302)

# render html
@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   # run flask
   app.run(debug=True, port=8000)