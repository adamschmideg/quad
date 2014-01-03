#!/usr/bin/python
# See http://stackoverflow.com/a/18599427/380587

import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):

    def on_any_event(self, event):
        error_code = subprocess.call(['hg', 'commit', '-q', '-m', 'WIP'])
        print 'Changed, so commited with return code %s' % error_code


if __name__ == "__main__":
    # TODO: read .gitignore (~/.gitignore too)
    ignore_patterns = ['*/.git', '*/.git/*', '*/.hg', '*/.hg/*']
    event_handler = MyHandler(ignore_patterns=ignore_patterns)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
