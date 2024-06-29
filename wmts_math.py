
import os
import sys
import urllib
import urllib.request
import pip
import json
import io

pkgs = os.path.join(os.path.dirname(__file__), 'our-site-packages')
sys.path.append(pkgs)

try:
  import xmltodict
except:
  pip.main([
    'install', f'--target={pkgs}', 'xmltodict'
  ])
  import xmltodict


try:
  import PIL
except:
  pip.main([
    'install', f'--target={pkgs}', 'Pillow'
  ])
  import PIL
import PIL.Image

def get(url):
  with urllib.request.urlopen(url) as response:
   return response.read()

def get_xml_as_dict(url):
  with urllib.request.urlopen(url) as response:
   return xmltodict.parse(response.read().decode('utf-8'))

def get_capabilities_dict(url):
  return get_xml_as_dict(f'{url}service=WMTS&request=GetCapabilities')

def get_tile_png_rowcol(url, layer, matrix_num, row, col):
  png_bytes = get(f'{url}SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER={layer}&STYLE=default&FORMAT=image/png&TILEMATRIX={matrix_num}&TILEROW={row}&TILECOL={col}')
  return PIL.Image.open(io.BytesIO(png_bytes))




def main(args=sys.argv):
  lon_x = float(args[1])
  lat_y = float(args[2])

  wmts_url = args[3] if len(args) > 3 else 'https://geo.ngu.no/geoserver/gwc/service/wmts?'
  if not wmts_url.endswith('?'):
    wmts_url += '?'

  print(f'Requesting a chip containing {lon_x},{lat_y} from {wmts_url}')

  capabilities = get_capabilities_dict(wmts_url)
  print(f'capabilities = {json.dumps(capabilities, indent=2)}')






if __name__ == '__main__':
  main()

