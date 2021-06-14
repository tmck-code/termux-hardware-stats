#!/usr/bin/env python3

from dataclasses import dataclass, asdict

from stats import termux_cpu, termux_mem

import argparse

import ujson as json

def run():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('op', type=str, choices=['cpu', 'mem'], help='which hardware stats to grab')

    args = parser.parse_args()

    if args.op == 'cpu':
        print(json.dumps(list(map(asdict, termux_cpu.CPUGlobalStateReader(8).load_all()))))

if __name__ == '__main__':
    run()
