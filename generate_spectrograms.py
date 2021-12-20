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

for file in os.listdir(MONO_FOLDER):
  file_mono_path = os.path.join(MONO_FOLDER, file)

  samplerate, samples = wavfile.read(file_mono_path)
  frequencies, times, spectrogram = plt.specgram(samples, samplerate)

  # print(len(times), len(frequencies), spectrogram.shape)
  print(spectrogram)

  # plt.pcolormesh(times, frequencies, spectrogram)
  # plt.imshow(spectrogram)
  plt.ylabel('Frequency [Hz]')
  plt.xlabel('Time [sec]')
  plt.savefig(os.path.join(SPECTROGRAM_FOLDER, file+'.png'))