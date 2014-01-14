#!/usr/bin/env python
# See http://stackoverflow.com/a/18599427/380587

import argparse
import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def repo_root_dir(file):
    return file

def commit(directory):
    # TODO: call hg commands directly from python
    retcode = subprocess.call(['hg', 'commit', '-q', '-m', 'WIP'])
    if retcode:
        print 'Error commiting'

class MyHandler(PatternMatchingEventHandler):

    def on_any_event(self, event):
        directory = repo_root_dir(event.src_path)
        commit(directory)


def init():
    pass

def monitor(directories):
    # TODO: read .gitignore (~/.gitignore too)
    ignore_patterns = ['*/.git', '*/.git/*', '*/.hg', '*/.hg/*']
    event_handler = MyHandler(ignore_patterns=ignore_patterns)
    observer = Observer()
    for d in directories:
        observer.schedule(event_handler, path=d, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def readable_dir(prospective_dir):
  if not os.path.isdir(prospective_dir):
    raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
  if os.access(prospective_dir, os.R_OK):
    return prospective_dir
  else:
    raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gimme a directory to monitor')
    parser.add_argument('directories', type=readable_dir, nargs='+', metavar='dir')
    args = parser.parse_args()
    monitor(args.directories)
