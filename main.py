import requests
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Download assets from Modpacks.ch')
parser.add_argument( '-u', '--url', type=str,
                    help='Download files from URL.')
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

def download_manifest(url):
  r = requests.get(url)
  json = r.json()
  for file in json['files']:
    if not file['path'] == './':
      if not os.path.isdir(file['path'][2:]):
        os.makedirs(file['path'][2:])
    file_content = requests.get(file['url']).content
    with open(file['path'][2:] + file['name'], 'wb') as f:
      f.write(file_content)
    print('Downloaded: {}!'.format(file['path'][2:] + file['name']))

download_manifest(args.url)