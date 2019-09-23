import os
import matplotlib.pyplot as plt
from drawnow import *

loadavg = []

plt.ion()
cnt=0

def plotLoadAvg():
    plt.ylim(0,4)
    plt.title('Raspberry Pi load average')
    plt.grid(True)
    plt.ylabel('usage')
    plt.plot(loadavg, 'bo-', label='usage')
    plt.legend(loc='upper right')

#pre-load dummy data
for i in range(0,100):
    loadavg.append(0)

while True:

    usage = os.popen("awk '{print $1}' /proc/loadavg").readline()
    print(usage)
    loadavg.append(usage)
    loadavg.pop(0)
    drawnow(plotLoadAvg)
    plt.pause(1)
