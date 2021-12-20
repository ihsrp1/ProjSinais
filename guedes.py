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



file = os.listdir(MP3_FOLDER)[0]
file = file[:-4]
file_wav_path = os.path.join(WAV_FOLDER, file+'.wav')
file_mp3_path = os.path.join(MP3_FOLDER, file+'.mp3')
file_mono_path = os.path.join(MONO_FOLDER, file+'.wav')
sound = AudioSegment.from_mp3(file_mp3_path)
sound.export(file_wav_path, format='WAV')
s, ifile = wavfile.read(file_wav_path)

for i in ifile:
  print(ifile)

# arr = np.array(s[1])

print(s)
  # frequencies, times, spectrogram = signal.spectrogram(data, samplerate)
  # print(samplerate, data)

  # plt.pcolormesh(times, frequencies, spectrogram)
  # # plt.imshow(spectrogram)
  # plt.ylabel('Frequency [Hz]')
  # plt.xlabel('Time [sec]')
  # plt.savefig(os.path.join(SPECTROGRAM_FOLDER, file+'.png'))