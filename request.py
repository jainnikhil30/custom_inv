#!/usr/bin/python

import json
import requests
import time

def main():
  # sleep
  time.sleep(200)
  res=requests.get('https://raw.githubusercontent.com/jainnikhil30/custom_inv/master/custom.json')
  data=res.json()
  print json.dumps(data, sort_keys=True, indent=2)
if __name__ == '__main__':
  main()
