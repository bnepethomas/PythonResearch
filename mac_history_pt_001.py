import sys
import requests
requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth
import json
import base64
import time

import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.image as image
import matplotlib.pyplot as plt

import numpy as np

image_path = "./images/"
image_name = 'FloorPlanCopy.png'
original_image_name = 'FloorPlanOriginal.png'

def main():
  print("********************************************************");
  print("* Cisco CMX MAC History Python 3 Utility               *");
  print("* Please provide the input in the following format     *");
  print("*                                                      *");
  print("* macAddress: 00:00:2a:01:00:06                        *");
  print("*                                                      *");
  print("* Control C to exit                                    *");
  print("********************************************************");

  username = 'learning'
  password = 'learning'
  restURL1 = 'https://cmxlocationsandbox.cisco.com/api/location/v1/historylite/clients/'

  x          = None
  y          = None
  chgOn      = None
  flr        = None
  macAddress = None

  macAddress = input("macAddress: ")
  try:

      Path = mpath.Path
      path_data = [
          ]

      response = requests.get(
      url = restURL1 +"/"+ macAddress,
      auth = HTTPBasicAuth(username,password),
      verify=False)

      json_data = response.json()

      ActCount = json_data["Count"] #actual count could be thousands, ie. 3000
      count = 0
      l = []
      while (count < 100):

          macAddress= json_data["Macaddress"]
          x = json_data["Data"][count]["x"]
          y = json_data["Data"][count]["y"]
          chgOn = json_data["Data"][count]["chgOn"]
          timestamp = time.ctime(int(chgOn)/1000)
          flr = json_data["Data"][count]["flr"]

          s = [timestamp, str(x), str(y), str(flr)]
          l.append(s)

          count = count + 1

          if count == 1:
            path_data.append((Path.MOVETO, (x, y)))
          else:
            path_data.append((Path.LINETO, (x, y)))
          


      print("----------------------------------------------------------------")
      print(" Actual Count: ", ActCount, " (only showing 10 events)")
      print(" Macaddress: ", macAddress)
      print(" List contains timestamp, xCoordinates, yCoordinates , FloorId")
      print("----------------------------------------------------------------")
      for s in l:
          print(list(s))


      im = image.imread(image_path + original_image_name)
      im[1, 1, 1] = 0 # set the alpha channel

      fig, ax = plt.subplots()

      ax.set_alpha(1)




      codes, verts = zip(*path_data)
      path = mpath.Path(verts, codes)



      x, y = zip(*path.vertices)
      line, = ax.plot(x, y, 'go-')



      fig.figimage(im, 10, 10, zorder=-11)


      ax.grid('off')
      ax.axis('off')

      plt.savefig(image_path + image_name, format='png', dpi=200)

      plt.show()


  except requests.exceptions.RequestException as e:
      print(e)


if __name__ == '__main__':
    main()

'''
Response from GET request
https://<cmx_ip>/api/location/v1/historylite/clients/00:00:2a:01:00:06

{
  "Data": [
    {
      "x": 209.99107,
      "y": 38.91461,
      "flr": "723413320329068590",
      "chgOn": "1492780699608",
      "s": "1",
      "ssid": "test",
      "ap": "00:2b:01:00:02:00",
      "un": "",
      "ip": "10.10.20.165",
      "lat": -999,
      "long": -999
    },
'''
