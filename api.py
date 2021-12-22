from flask import Flask, flash, request, redirect, url_for
import os
app = Flask(__name__)
import json
from flask_cors import CORS #include this line
from a import findMusic
import sys
CORS(app) 

@app.route('/sendMusic',methods=['POST'])
def createTask():
    # print('Recebi algo')
    audio = request.files['audio']
    # print(audio)
    path = os.path.join('musics', audio.filename)
    audio.save(path)
    musicInfo = findMusic(path)
    returnString = '{}*{}*{}*{}' .format(musicInfo[0], musicInfo[1],musicInfo[2], musicInfo[3])
    
 
    with open("randomfile.txt", "a") as o:
        o.write(returnString)
    # result = returnString.split("*")
    # print (result[0])
    return returnString


if __name__ == "__main__":
    print('oi')
    app.run()