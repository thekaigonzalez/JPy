import os


def export(filename):
    js = open(filename + ".py.js", 'a')
    return js