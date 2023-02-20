import sys
import numpy as np
import os
import wave
from deepspeech import Model as dsm

model_path = 'language_models/deepspeech-0.9.3-models.pbmm'
lm_path = 'language_models/deepspeech-0.9.3-models.scorer'
beam_width = 100
lm_alpha = 0.93
lm_beta = 1.18

def read_from_wav(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
    return rate, buffer

def wav_to_text(model, filename):
    rate, buffer = read_from_wav(filename)
    wav_data = np.frombuffer(buffer, dtype=np.int16)
    return model.stt(wav_data) 



def main():
    if len(sys.argv) == 1:
        print('At least 1 file must be inputed.\n\nUsage: "./transcription.py filename1 filename2 ...')
    else:
        model = dsm(model_path)
        model.enableExternalScorer(lm_path)
        model.setScorerAlphaBeta(lm_alpha, lm_beta)
        model.setBeamWidth(beam_width)

        for audiofile in sys.argv[1:]:
            try:
                print(wav_to_text(model, audiofile))
            except:
                print('Invalid File')

if __name__ == '__main__':
    main()