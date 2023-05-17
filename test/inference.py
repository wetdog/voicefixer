#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   inference.py    
@Contact :   haoheliu@gmail.com
@License :   (C)Copyright 2020-2100

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
9/6/21 3:08 PM   Haohe Liu      1.0         None
"""



import sys
import os
from os.path import isdir, exists, basename, join
from argparse import ArgumentParser
from os.path import dirname, abspath

upper_level = dirname(dirname(abspath(__file__)))
sys.path.append(upper_level)

from voicefixer import VoiceFixer
from voicefixer import Vocoder
import logging

#Parser
parser = ArgumentParser()

parser.add_argument(
    "-i",
    "--input_file_path",
    default="",
    help="The .wav file or the audio folder to be processed",
)
parser.add_argument(
    "-o", "--output_path", default=".", help="The output dirpath for the results"
)
parser.add_argument("-m", "--models", default="voicefixer_fe")
parser.add_argument(
    "--cuda", type=bool, default=False, help="Whether use GPU acceleration."
)
args = parser.parse_args()


if __name__ == "__main__":

    #Setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('voicefixer_logs.txt')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # instantiate voicefixer
    voicefixer = VoiceFixer()

    if not isdir(args.output_path):
        raise ValueError("Error: output path need to be a directory, not a file name.")
    if not exists(args.output_path):
        os.makedirs(args.output_path, exist_ok=True)

    if not isdir(args.input_file_path):
        assert (
            args.input_file_path[-3:] == "wav" or args.input_file_path[-4:] == "flac"
        ), (
            "Error: invalid file "
            + args.input_file_path
            + ", we only accept .wav and .flac file."
        )
        output_path = join(args.output_path, basename(args.input_file_path))
        print("Start Prediction.")
        voicefixer.restore(
            input=args.input_file_path, output=output_path, cuda=args.cuda
        )
    else:
        files = os.listdir(args.input_file_path)
        logger.info(f"Found {len(files)} files in {args.input_file_path}")
        logger.info("Start Prediction.")
        processed_files = 0
        
        # processing loop 
        for i, file in enumerate(files):
            if not file[-3:] == "wav" and not file[-4:] == "flac":
                print(
                    "Ignore file",
                    file,
                    " unsupported file type. Please use wav or flac format.",
                )
                continue
            output_path = join(args.output_path, basename(file))
            voicefixer.restore(
                input=join(args.input_file_path, file),
                output=output_path,
                cuda=args.cuda,
            )
            processed_files += 1
    logger.info(f"Prediction Completed. {processed_files} restored")
