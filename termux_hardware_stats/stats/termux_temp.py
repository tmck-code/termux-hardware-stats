from glob import glob
import os

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

for d in glob('/sys/class/thermal/thermal_zone*'):
    values = []
    for typ in ['type', 'temp']:
        fpath = f'{d}/{typ}'
        if not os.path.exists(fpath):
            continue
        try:
            with open(fpath) as istream:
                values.append(istream.read().strip())
        except OSError as e:
            # print(d, typ, values, e.__class__, e)
            values.append(0)
    if values[0] in TYPES:
        print(values[0], parse_temp(values[1]), d)
