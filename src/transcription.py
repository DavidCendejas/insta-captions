import sys
import numpy as np
import os
import wave
from deepspeech import Model as dsm

models = {
    'english': 'language_models/deepspeech-0.9.3-models.pbmm',
    'mandarin': 'language_models/deepspeech-0.9.3-models-zh-CN.pbmm'
}

lm = {
    'english': 'language_models/deepspeech-0.9.3-models.scorer',
    'mandarin': 'language_models/deepspeech-0.9.3-models-zh-CN.scorer'
}

alphabeta = {
    'english': {'alpha': 0.931289039105002, 'beta': 1.1834137581510284},
    'mandarin': {'alpha': 0.6940122363709647, 'beta': 4.777924224113021}
}

beam_width = 100

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



# wav_files is a list of .wav files
def transcribe(wav_files, language='english'):
    if len(wav_files) == 0:
        return []
    if language not in models:
        return [] #THIS SHOULD RAISE AN EXCEPTION
    else:
        
        # Eventually when incorporating SpeechRecognition library to be able to detect
        # the language of a file, the model parameters should be set for each distinct
        # .wav file each loop. Language parameter would then be refactored out

        model = dsm(models[language])
        model.enableExternalScorer(lm[language])
        model.setScorerAlphaBeta(alphabeta[language]['alpha'],
            alphabeta[language]['beta'])
        model.setBeamWidth(beam_width)

        for audio in wav_files:
            try:
                filename = os.path.splitext(os.path.basename(audio))[0]
                with open('transcriptions/{}.txt'.format(filename), 'w') as fp:
                    transcription = wav_to_text(model, audio)
                    fp.write(transcription)
            except:
                print('Invalid File')

transcribe(['audio/english_examples/8455-210777-0068.wav'], 'english')