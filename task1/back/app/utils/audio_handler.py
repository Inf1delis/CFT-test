import librosa
import librosa.display
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize'] = 16, 10

import numpy as np

import io


def audio_spectogram(filename, mp3):
    if filename is "":
        wav_src = librosa.util.example_audio_file()
    else:
        wav_src = io_to_wav(mp3)

    y, sr = librosa.load(wav_src)
    D = np.abs(librosa.stft(y, dtype=np.complex64))

    librosa.display.specshow(
                          librosa.amplitude_to_db(D, ref=np.max),
                          y_axis='log',
                          x_axis='time'
                      )

    plt.title(f'Power spectrogram of {filename}')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='jpeg')
    buf.seek(0)
    image = buf.getvalue()
    buf.close()
    plt.close()
    plt.cla()
    return image


def io_to_wav(io_file):
    src = '../tmp/tmp.mp3'
    with open(src, 'wb') as file:
        file.write(io_file)

    return _convert_mp3_to_wav(src)


def _convert_mp3_to_wav(src):
    from pydub import AudioSegment

    dst = "../tmp/tmp.wav"

    try:
        sound = AudioSegment.from_mp3(src)
        # fastest export from mp3 is wav
        sound.export(dst, format="wav")
        return dst
    except Exception as e:
        print(e)
        return None
