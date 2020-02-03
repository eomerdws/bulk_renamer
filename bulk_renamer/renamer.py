import os
import glob
import argparse
from audio_file import AudioFile


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dat=", metavar='filename', dest="data_file", nargs='*')
    parser.add_argument('--loc=', metavar='filename', dest="location", nargs='*')

    args = parser.parse_args()
    print(args.location)
    print(args.data_file)



