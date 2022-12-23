import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument("-e", "--encode", nargs=2, type=str, default=False)
    p.add_argument("-d", "--decode", nargs=2, type=str, default=False)
    return p

