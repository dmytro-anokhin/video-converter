#!/usr/bin/python3

from argparse import ArgumentParser
from os import listdir, mkdir
from os.path import isfile, isdir, join, split
import subprocess

if __name__ != '__main__':
    raise SystemExit(f'The script "{__name__}" should not be imported')

class App:
    """Principal class for the app"""

    def __init__(self):
        self.parser = ArgumentParser(
            prog = 'GoPro Converter',
            description = 'Convert GoPro videos to HEVC',
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
            raise ValueError(f'"{path}" not a file or a directory')

    def convert(self, file):
        """Convert single file"""
        print(f'Converting {file}')
        parts = split(file)
        directory = join(parts[0], "out")

        try:
            mkdir(directory)
        except:
            pass

        subprocess.run([
            'avconvert',
            '--source', file,
            '--output', join(directory, parts[1]),
            '--preset', 'PresetHEVCHighestQuality',
            '--progress'
        ])


app = App()
app.run()
