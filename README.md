# Video Converter

Video Converter script batch converts video files to a different format.

Video files produced by modern cameras, mirrorless or action cameras, occupy a lot of space. This is great for editing, but not so much for storing in cloud and viewing on a mobile device.

Using format like [HEVC](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) reduces size dramatically without much quality loss, and makes viewing your footage on mobile a joy.

On macOS you can use `avconvert` to convert individual files. Video Converter script automates this process for multiple files.

## Usage

You need Python 3 to run it.

```
python3 convert.py <path to a file or a directory>
```

Alternatively you can make `convert.py` executable:

```
chmod +x convert.py
./convert.py <path to a file or a directory>
```

To store converted files `convert.py` creates `out` directory next to the source files. Original file names and metadata preserved.

`convert.py` uses `PresetHEVCHighestQuality` preset (a high quality preset with HEVC video and AAC audio). You can pass a different preset using `--preset | -p name` option. See `man avconvert` for the list of presets.
