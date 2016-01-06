#!/usr/bin/env python3

import signal
from sys import exit
from getpass import getpass

def start():
    pass_to_learn = getpass("password> ")
    input("if ready press [enter] else press C-c ")
    return pass_to_learn

def do_training(pass_to_learn):
    total = 0
    good = 0
    try_pass = True

    while try_pass:
        try_pass = getpass("(good: {} of {}) try password (empty for leave)> ".format(good, total))
        if try_pass:
            if pass_to_learn == try_pass:
                good = good + 1
                print("GOOD!")
            else:
                print("BAD!")
            total = total + 1
    return (total, good, pass_to_learn)

def print_stats(info):
    (total, good, pass_to_learn) = info

    print("statistics:")
    print("===========")
    print("")
    print("original password: {}".format(pass_to_learn))
    print("total answers    : {}".format(total))
    print("good answers     : {}".format(good))
    print("bad answers      : {}".format(total - good))
    print("efectiveness     : {:.2f}%".format((good * 100.0)/total))

def good_bye():
    print("")
    print("Have a nice day.")

def sigint_handler(signal, frame):
    good_bye()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    print_stats(do_training(start()))
    good_bye()
