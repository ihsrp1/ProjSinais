from pydub import AudioSegment
from scipy.io import wavfile
import os
from scipy import signal
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WAV_FOLDER = 'wav'
MONO_FOLDER = 'wav-mono'
SPECTROGRAM_FOLDER = 'spectrograms'
MP3_FOLDER = 'mp3'


for file in os.listdir(MP3_FOLDER):
  file = file[:-4]

  file_wav_path = os.path.join(WAV_FOLDER, file+'.wav')
  file_mp3_path = os.path.join(MP3_FOLDER, file+'.mp3')
  file_mono_path = os.path.join(MONO_FOLDER, file+'.wav')

  sound = AudioSegment.from_mp3(file_mp3_path)
  sound.export(file_wav_path, format='WAV')

  sound = AudioSegment.from_wav(file_wav_path)
  sound = sound.set_channels(1)
  sound.export(file_mono_path, format="WAV")