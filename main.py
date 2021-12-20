from generate_fingerprint import fingerprint
from scipy.io import wavfile
import os

MONO_FOLDER = 'wav-mono'
file = 'a-ha - Take On Me.wav'
file_mono_path = os.path.join(MONO_FOLDER, file)

samplerate, samples = wavfile.read(file_mono_path)

cu = fingerprint(samples)
mapper = {}
for hash, offset in cu:
  mapper[hash.upper()] = offset

print(mapper)