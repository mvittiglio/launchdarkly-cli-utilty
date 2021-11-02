#!/usr/bin/env python3
""" LaunchDarkly CLI Utility
General purpose utility to allow for easy adminstration via CLI

Usage:
  LaunchDarkly.py -h
  LaunchDarkly.py -v
  LaunchDarkly.py create-flag (--api-key=<api_key>) (--project-id=<project_id>) (--flag-name=<flag_name>)

Options:
  -h --help                     Show this screen.
  -v --version                  Show version.
  --api-key=<key>               Key to use when accessing LaunchDarkly API.
  --project-id=<project_id>     ID for the project where the flag will be created.
  --flag-name=<flag_name>       Name of the flag being created
"""
import requests
import stringcase

from docopt import docopt


def create_feature_flag(api_key, project_id, flag_name):
  url = "https://app.launchdarkly.com/api/v2/flags/" + project_id

  payload = {
    "name": flag_name,
    "key": stringcase.spinalcase(flag_name)
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
  }

  response = requests.post(url, json=payload, headers=headers)

  data = response.json()
  print(data)


def main():
  args = docopt(__doc__, version='LaunchDarkly CLI Utility v0.1.211102')
  print(args)
  if(args['create-flag']):
    create_feature_flag(args['--api-key'], args['--project-id'], args['--flag-name'])


if __name__ == '__main__':
  main()
