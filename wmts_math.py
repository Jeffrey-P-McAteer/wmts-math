
import os
import sys
import urllib
import urllib.request
import pip

pkgs = os.path.join(os.path.dirname(__file__), 'our-site-packages')
sys.path.append(pkgs)

try:
  import xmltodict
except:
  pip.main([
    'install', f'--target={pkgs}', 'xmltodict'
  ])
  import xmltodict

def get(url):
  with urllib.request.urlopen(url) as response:
   return response.read()

def get_xml_as_dict(url):
  with urllib.request.urlopen(url) as response:
   return xmltodict.parse(response.read().decode('utf-8'))



def main(args=sys.argv):
  lon_x = float(args[1])
  lat_y = float(args[2])

  wmts_url = args[3] if len(args) > 3 else 'https://geo.ngu.no/geoserver/gwc/service/wmts?'
  if not wmts_url.endswith('?'):
    wmts_url += '?'

  print(f'Requesting a chip containing {lon_x},{lat_y} from {wmts_url}')

  capabilities = get_xml_as_dict(f'{wmts_url}service=WMTS&request=GetCapabilities')
  print(f'capabilities = {capabilities}')




if __name__ == '__main__':
  main()

