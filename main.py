#!/usr/bin/env python
from error import *
import Wang
from argparse import ArgumentParser
from argparse import SUPPRESS

def audio_matcher():
    """Our main control flow."""

    parser = ArgumentParser(
        description="Compare two audio files to determine if one "
                    "was derived from the other.",
        prog="ERROR: p4500", usage=SUPPRESS)
    parser.add_argument("-f", action="append",
                        required=False, dest="files",
                        default=list(),
                        help="A file to examine. "
                        "Must provide two instance of this argument.")
    parser.add_argument("--test",
                  action="store_true", dest="test", default=False,
                  help="Run in test mode (shows stacktraces on error)")

    try:
        args = parser.parse_args()
    except Exception, e:
        if args.test:
            raise
        die(e.message)

    if len(args.files) != 2:
        die("Must provide exactly two input files.")

    # Use our matching system
    try:
        matcher = Wang.Wang(args.files)
        if matcher.match():
            print "MATCH"
        else:
            print "NO MATCH"
    except IOError, e:
        if args.test:
            raise
        die(e)
        return

if __name__ == "__main__":
    audio_matcher()
