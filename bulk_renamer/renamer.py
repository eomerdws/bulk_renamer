import os
import glob
import argparse
from audio_file import AudioFile


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dat=", metavar='filename', dest="data_file", nargs='*')
    parser.add_argument('--loc=', metavar='filename', dest="location", nargs='*')

    args = parser.parse_args()
    print(args.location[0])
    print(args.data_file[0])

    os.chdir(args.location[0])
    with open(args.data_file[0], 'r') as fp:
        print(fp.readline(1))



