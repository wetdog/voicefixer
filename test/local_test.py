#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py
@Contact :   haoheliu@gmail.com
@License :   (C)Copyright 2020-2100

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
9/14/21 11:02 AM   Haohe Liu      1.0         None
"""

import os
import sys
import librosa
import numpy as np
import torch
from os.path import dirname, abspath

upper_level = dirname(dirname(abspath(__file__)))
sys.path.append(upper_level)

from voicefixer import VoiceFixer, Vocoder

AUDIO_PATH = os.path.join(dirname(abspath(__file__)),"255774__kwahmah_02__v02acuban1.wav")

# TEST VOICEFIXER
## Initialize a voicefixer
print("Initializing VoiceFixer...")
voicefixer = VoiceFixer()
# Mode 0: Original Model (suggested by default)
# Mode 1: Add preprocessing module (remove higher frequency)
# Mode 2: Train mode (might work sometimes on seriously degraded real speech)
for mode in [0]:
    print("Test voicefixer mode", mode, end=", ")
    print("Using CPU:")
    voicefixer.restore(
        input=AUDIO_PATH,  # low quality .wav/.flac file
        output=f"{os.path.basename(AUDIO_PATH)}_{mode}_restored.wav",
        cuda=False,  # GPU acceleration
        mode=mode,
    )

    '''
    if torch.cuda.is_available():
        print("Using GPU:")
        voicefixer.restore(
        input=AUDIO_PATH,  # low quality .wav/.flac file
        output=f"{os.path.basename(AUDIO_PATH)}_{mode}_restored.flac",
        cuda=True,  # GPU acceleration
        mode=mode,
        )
    print("Pass")
    '''

print("Pass")
