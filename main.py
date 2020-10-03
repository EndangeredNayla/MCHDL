import requests
import os
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description='Download assets from Modpacks.ch')
    parser.add_argument('-u', '--url', type=str, required=True,
                        help='Download files from URL.')
    parser.add_argument('-p', '--path', type=str, default=os.getcwd(),
                        help="Path to place downloads. Defaults to current directory.")
    args = parser.parse_args()
    go_to_path(args, parser)
    return args


def go_to_path(args, parser):
    try:
        os.chdir(args.path)
    except:
        print(f"ERROR: Cannot go to path {args.path}!")
        parser.print_help()
        sys.exit(1)


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


if __name__ == "__main__":
    download_manifest(parse_args().url)
