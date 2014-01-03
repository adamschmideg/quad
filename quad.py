#!/usr/bin/python
# See http://stackoverflow.com/a/18599427/380587

import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):

    def on_any_event(self, event):
        subprocess.call(['git', 'wip'])


if __name__ == "__main__":
    # TODO: read .gitignore (~/.gitignore too)
    event_handler = MyHandler(ignore_patterns=['*/.git', '*/.git/*'])
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
