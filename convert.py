#!/usr/bin/python3
""" Converts videos to HEVC format """

from argparse import ArgumentParser
from os import listdir, mkdir
from os.path import isfile, isdir, join, split
from subprocess import run, CalledProcessError

class App:
    """Principal class for the app"""

    def __init__(self):
        self.parser = ArgumentParser(
            prog = 'Video Converter',
            description = 'Convert videos to HEVC format',
            epilog = '')
        self.parser.add_argument('path')

    def run(self):
        """Run the app"""
        args = self.parser.parse_args()
        path = args.path

        if isfile(path):
            self.convert(path)
        elif isdir(path):
            contents = map(lambda name: join(path, name), listdir(path))
            files = [file for file in contents if isfile(file)]
            for file in files:
                self.convert(file)
        else:
            raise ValueError(f'"{path}" no such file')

    def convert(self, file):
        """Convert single file"""
        print(f'Converting {file}')
        parts = split(file)
        directory = join(parts[0], "out")

        try:
            mkdir(directory)
        except FileExistsError:
            pass

        try:
            run([
                'avconvert',
                '--source', file,
                '--output', join(directory, parts[1]),
                '--preset', 'PresetHEVCHighestQuality',
                '--progress'
            ], check=True)
        except CalledProcessError as ex:
            print(ex)

if __name__ == '__main__':
    app = App()
    app.run()
