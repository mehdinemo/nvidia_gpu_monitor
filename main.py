import asciichartpy
import matplotlib.pyplot as plt
import subprocess
import schedule
import re
import os

n = 60
height = 2
sec = 1

# Initialize lists to store values
temp = []
memory = []
power = []
usage = []


# Function to parse nvidia-smi output
def parse_output(output):
    temp_match = re.search(r"(\d+)C", output)
    power_match = re.search(r"(\d+)W", output)
    memory_match = re.search(r"(\d+)MiB", output)
    usage_match = re.search(r"(\d+)%", output)

    if temp_match and power_match and memory_match and usage_match:
        temp.append(int(temp_match.group(1)))
        power.append(int(power_match.group(1)))
        memory.append(int(memory_match.group(1)))
        usage.append(int(usage_match.group(1)))
    else:
        print("Failed to parse nvidia-smi output.")

    while len(temp) > n:
        temp.pop(0)
    while len(memory) > n:
        memory.pop(0)
    while len(power) > n:
        power.pop(0)
    while len(usage) > n:
        usage.pop(0)


# Function to plot graphs
def plot_graphs_mat():
    plt.figure(figsize=(15, 10))

    plt.subplot(221)
    plt.plot(temp)
    plt.title('Temperature')

    plt.subplot(222)
    plt.plot(memory)
    plt.title('Memory')

    plt.subplot(223)
    plt.plot(power)
    plt.title('Power')

    plt.subplot(224)
    plt.plot(usage)
    plt.title('Usage')

    plt.tight_layout()
    plt.draw()
    plt.pause(0.001)
    plt.clf()


# Function to plot graphs
def plot_graphs_ascii():
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Temperature")
    print(asciichartpy.plot(temp, {'height': height}))
    print("\nMemory")
    print(asciichartpy.plot(memory, {'height': height}))
    print("\nPower")
    print(asciichartpy.plot(power, {'height': height}))
    print("\nUsage")
    print(asciichartpy.plot(usage, {'height': height}))


# Function to run nvidia-smi and update graphs
def job():
    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
    parse_output(result.stdout.decode())
    plot_graphs_ascii()


# Schedule the job
schedule.every(sec).seconds.do(job)

# Run the script
while True:
    schedule.run_pending()
