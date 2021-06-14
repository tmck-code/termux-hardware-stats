#!/usr/bin/env python3

from dataclasses import dataclass
from collections import defaultdict, namedtuple
from itertools import takewhile, repeat
import multiprocessing
from functools import lru_cache

from termux_hardware_stats.stats import termux_cpu, termux_mem
