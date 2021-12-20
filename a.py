from acoustid import lookup, fingerprint_file
import chromaprint
import os
import audioread

API_KEY = 'NMMRWI3vOJ'
MAX_AUDIO_LENGTH = 120  # Seconds.

def generate_fingerprint(samplerate, channels, pcmiter, maxlength=MAX_AUDIO_LENGTH):
  """Fingerprint audio data given its sample rate and number of
  channels.  pcmiter should be an iterable containing blocks of PCM
  data as byte strings. Raises a FingerprintGenerationError if
  anything goes wrong.
  """
  # Maximum number of samples to decode.
  endposition = samplerate * channels * maxlength

  try:
    fper = chromaprint.Fingerprinter()
    fper.start(samplerate, channels)

    position = 0  # Samples of audio fed to the fingerprinter.
    for block in pcmiter:
        fper.feed(block)
        position += len(block) // 2  # 2 bytes/sample.
        if position >= endposition:
            break

    return fper.finish()
  except chromaprint.FingerprintError:
    print('fodeu')

path = os.path.abspath(os.path.expanduser('./descubra.mp3'))

with audioread.audio_open(path) as f:
  duration = f.duration
  fp = generate_fingerprint(f.samplerate, f.channels, iter(f))
# duration, fingerprint = fingerprint_file('./descubra.mp3')
print(duration, int.from_bytes(fp, "little"))

result = lookup(API_KEY, fp, duration)


print(result)
# api key: NMMRWI3vOJ