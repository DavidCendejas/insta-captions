# insta-captions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![issues](https://img.shields.io/github/issues/DavidCendejas/insta-captions)

[![Build Status](https://github.com/DavidCendejas/insta-captions/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/DavidCendejas/insta-captions/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/DavidCendejas/insta-captions/branch/main/graph/badge.svg?token=Z2HN4RCJGZ)](https://codecov.io/gh/DavidCendejas/insta-captions)

insta-captions is a tool that will allow for the instant transcription and translation of audio files to and from different languages.

## Overview

`insta-captions` is a library that deals with the conversion of audio into "captions". I have been learning Mandarin, my third language. Part of my learning process, as well as maintenance for Spanish, is to watch videos, shows, and movies in the language I am trying to deepen. Sometimes, however, I need to watch content in English but want to read it in another language, and there is no easy way to do this if captions are not provided by the video maker, which is the crux of this issue.

The main feature that I envision for this project would be for audio to be converted into text of any (supported) language regardless of the language of the input audio. This involves two, albeit involved, steps:

- given an audio file, convert that audio into text of language it is in
- given text of one language, translate into another

## Installation and Running

insta-captions transcriptions are possible with [DeepSpeech](https://github.com/mozilla/DeepSpeech). For installation of DeepSpeech, refer to their [documentation](https://deepspeech.readthedocs.io/en/r0.9/?badge=latest). I use their [pre-trained models](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3) on english and mandarin. These models are not included in this repository due to file size, and must be downloaded separately and placed in the src/language_models folder (both the model and the scorer). The optimal alpha and beta values for each respective language were found here as well.

Additional libraries used are numpy to convert the buffer of the .wav files into int16 numpy arrays as this is what DeepSpeech speech-to-text accepts.

## make commands
- `make format`: autoformat this library using `black`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make test`: run automated tests with `unittest`
- `make coverage`: run automated tests with `unittest` and collect coverage information