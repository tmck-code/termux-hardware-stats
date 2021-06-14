#!/usr/bin/env python3

from dataclasses import dataclass, asdict

from termux_hardware_stats.stats import termux_cpu, termux_mem

import argparse

import ujson as json


def run():
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='Termux Hardware Stats')
    subparsers = parser.add_subparsers(help='Operation help', dest='hardware')

    # create the parser for the 'cpu' command
    parser_a = subparsers.add_parser('cpu', help='CPU help')
    parser_a.add_argument('op', type=str, choices=['state', 'freqs', 'usage'], help='CPU stat')

    # create the parser for the 'mem' command
    parser_b = subparsers.add_parser('mem', help='Mem help')
    parser_b.add_argument('op', type=str, choices=['meminfo', 'meminfo_complete'], help='Mem stat')
    args = parser.parse_args().__dict__

    if args['hardware'] == 'cpu':
        if args['op'] == 'state':
            print(json.dumps(list(map(asdict, termux_cpu.CPUGlobalStateReader(8).load_all()))))
        if args['op'] == 'usage':
            print(json.dumps(list(termux_cpu.CPUGlobalStateReader(8).load_percentages())))
        elif args['op'] == 'freqs':
            print(json.dumps(list(map(asdict, termux_cpu.CPUFrequencyReader(8).load_all()))))
    elif args['hardware'] == 'mem':
        if args['op'] == 'meminfo':
            print(json.dumps(asdict(termux_mem.MemInfoReader().load())))
        if args['op'] == 'meminfo_complete':
            print(json.dumps(asdict(termux_mem.MemInfoReader().load_all())))

if __name__ == '__main__':
    run()

