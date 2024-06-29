
import os
import sys
import urllib
import urllib.request

def main(args=sys.argv):
  lon_x = float(args[1])
  lat_y = float(args[2])

  print(f'Requesting a chip containing {lon_x},{lat_y}')




if __name__ == '__main__':
  main()

