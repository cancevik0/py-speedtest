# Internet Speed Test

This script performs an internet speed test using the `speedtest` module and provides real-time progress bars for both download and upload speeds.

## Features

- Measures **download speed**, **upload speed**, and **ping**.
- Displays real-time progress bars using `colorama`.
- Calculates **maximum**, **average**, and **minimum** speeds.

## Requirements

Ensure you have Python installed along with the following dependencies:

```
pip install speedtest-cli colorama
```

## Usage

Run the script using:

```
python speedtester.py
```

## Output Example

![Speed Test Result](https://i.imgur.com/wFOAdjH.png) 

```
⚡ Ping: 20.15 ms
⬇️ Download Speed: 150.32 Mbps (Max.)
⬇️ Download Speed: 120.45 Mbps (Average)
⬇️ Download Speed: 95.12 Mbps (Min.)
⬆️ Upload Speed: 50.78 Mbps (Max.)
⬆️ Upload Speed: 45.34 Mbps (Average)
⬆️ Upload Speed: 39.89 Mbps (Min.)
```

