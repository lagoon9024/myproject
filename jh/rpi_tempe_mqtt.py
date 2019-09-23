import urllib.request
import time

def getCPUTemp():
    with open('/sys/class/thermal/thermal_zone0/temp','r') as ftemp:
        return ftemp.read()

channelID = "880451"

apiKey = "K3H1C108NC6LEBM7"

url = 'https://api.thingspeak.com/update?api_key=%s'%apiKey

while(True):
    cpuTemp = int(getCPUTemp())/1000

    url_addr = url + "&field1=%d"%cpuTemp
    
    try:
        urllib.request.urlopen(url_addr)
        time.sleep(15)
    except (KeyboardInterrupt):
        break
    except:
        print("There was an error while publishing the data.")