# insta-captions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![issues](https://img.shields.io/github/issues/DavidCendejas/insta-captions)

insta-captions is a tool that will allow for the instant transcription and translation of audio files to and from different languages.

## Overview

`insta-captions` is a library that deals with the conversion of audio into "captions". I have been learning Mandarin, my third language. Part of my learning process, as well as maintenance for Spanish, is to watch videos, shows, and movies in the language I am trying to deepen. Sometimes, however, I need to watch content in English but want to read it in another language, and there is no easy way to do this if captions are not provided by the video maker, which is the crux of this issue.

The main feature that I envision for this project would be for audio to be converted into text of any (supported) language regardless of the language of the input audio. This involves two, albeit involved, steps:

- given an audio file, convert that audio into text of language it is in
- given text of one language, translate into another
