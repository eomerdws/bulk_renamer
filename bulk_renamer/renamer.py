import os
import glob
import argparse
from audio_file import AudioFile

if __name__ == '__main__':
    audio_files = []
    parser = argparse.ArgumentParser()
    parser.add_argument("--dat=", metavar='filename', dest="data_file", nargs='*')
    parser.add_argument('--loc=', metavar='filename', dest="location", nargs='*')

    args = parser.parse_args()
    print(args.location[0])
    print(args.data_file[0])

    os.chdir(args.location[0])

    print(f"Open : {args.data_file[0]}")
    data = ""
    loc = args.location[0]

    with open(args.data_file[0], 'r') as fp:
        data = fp.read().split("\n")

    for d in data:
        if not d:  # empty line
            continue
        a = d.strip()
        # print(a[10:43])
        # print(a[43:68])

        audio: AudioFile = AudioFile(a[0:10], loc, a[10:43], a[43:68])
        audio.rename()



