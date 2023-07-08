# GPU Monitoring Tool

This Python script provides real-time monitoring of NVIDIA GPU parameters like temperature, memory usage, power usage,
and GPU utilization. The script uses the `nvidia-smi` command to retrieve these parameters and presents them as ASCII
line charts in the terminal.

## Dependencies

The script requires the following Python packages:

- asciichartpy
- matplotlib (not used in the current version but kept for possible future use)
- schedule

These can be installed with pip:

```bash
pip install asciichartpy matplotlib schedule
```

## Running the Script

To run the script, simply execute the Python file in your terminal:

```bash
python monitor.py
```

The script will start displaying ASCII line charts of the GPU parameters and will update them every second.

## Configuration

You can modify the following variables in the script to change its behavior:

- n: the number of most recent readings to display (default: 60)
- height: the height of the ASCII charts (default: 2)
- sec: the interval between updates, in seconds (default: 1)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
