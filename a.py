from acoustid import lookup, fingerprint_file
import chromaprint
import os
import audioread
import wikipedia
import requests


API_KEY = 'NMMRWI3vOJ'
MAX_AUDIO_LENGTH = 120  # Seconds.
LYRICS_URL = 'https://api.lyrics.ovh/v1/'

def generate_fingerprint(samplerate, channels, pcmiter, maxlength=MAX_AUDIO_LENGTH):
  endposition = samplerate * channels * maxlength

  try:
    fper = chromaprint.Fingerprinter()
    fper.start(samplerate, channels)

    position = 0  
    for block in pcmiter:
        fper.feed(block)
        position += len(block) // 2
        if position >= endposition:
            break

    return fper.finish()
  except chromaprint.FingerprintError:
    print('Deu ruim')

def findMusic(musicPath):
  print(musicPath)
  path = os.path.abspath(os.path.expanduser(musicPath))
  print(path)
  with audioread.audio_open(path) as f:
    duration = f.duration
    fp = generate_fingerprint(f.samplerate, f.channels, iter(f))
  # duration, fingerprint = fingerprint_file('./descubra.mp3')
  # print(duration, int.from_bytes(fp, "little"))

  result = lookup(API_KEY, fp, duration)

  found = False
  i = 0
  while not found:
    first_result = result['results'][0]['recordings'][i]
    song_name = first_result['title']
    artist_name = first_result['artists'][0]['name']
    if first_result and song_name and artist_name:
      result = wikipedia.page(artist_name + ' artist')
      wikiContent = result.content
      lyrics_query = LYRICS_URL + '/' + artist_name + '/' + song_name
      res = requests.get(lyrics_query)
      lyrics = res.json()['lyrics']
      found = True
    i+=1
  finalResult = (song_name, artist_name, wikiContent, lyrics)
  return finalResult

    