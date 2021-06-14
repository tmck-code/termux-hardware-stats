from glob import glob
import os
import ujson as json

def parse_temp(value):
    return round(float(value)/1000, 2)

TYPES = [
    'battery',
    'usb',
    'shell_front',
    'shell_back',
    'cpu-1-0-usr',
    'cpu-1-1-usr',
    'cpu-1-2-usr',
    'cpu-1-3-usr',
    'cpu-1-4-usr',
    'cpu-1-5-usr',
    'cpu-1-6-usr',
    'cpu-1-7-usr',
]

def load_temps():
    values = {}
    for d in glob('/sys/class/thermal/thermal_zone*'):
        with open(f'{d}/type') as istream:
            typ = istream.read().strip()
        if typ not in TYPES:
            continue
        with open(f'{d}/temp') as istream:
            values[typ] = parse_temp(istream.read().strip())
    return dict(sorted(values.items()))

