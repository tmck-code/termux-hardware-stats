# termux-hardware-stats

A utility to fetch available hardware stats in Termux (Android).

Currently, there aren't any easy-to-use (non-root!) tools to grab basic information about your Android's hardware. This information is there for the taking! This package combines all the available methods to grab this info into one place for your convenience (see below if you are interested in the specifics of how anything works)

- [termux-hardware-stats](#termux-hardware-stats)
  - [The TODO list](#the-todo-list)
  - [Available stats](#available-stats)
    - [CPU](#cpu)
      - [Number of CPU cores](#number-of-cpu-cores)
      - [CPU Frequencies](#cpu-frequencies)
      - [CPU Usage per-core](#cpu-usage-per-core)

---

## The TODO list

- [x] CPU
- [x] Memory
- [ ] Temperature
- [ ] Network
- [ ] Processes

---

## Available stats

### CPU

```python
from termux_hardware_stats.termux_hardware_stats import TermuxHardwareStats
```

#### Number of CPU cores

```python
TermuxHardwareStats.cpu_count()
# 8
```

#### CPU Frequencies

```python
TermuxHardwareStats.cpu_freq()
# [{'current': 1401600, 'min': 691200, 'max': 1804800},
#  {'current': 1401600, 'min': 691200, 'max': 1804800},
#  {'current': 1401600, 'min': 691200, 'max': 1804800},
#  {'current': 1401600, 'min': 691200, 'max': 1804800},
#  {'current': 2419200, 'min': 710400, 'max': 2419200},
#  {'current': 2419200, 'min': 710400, 'max': 2419200},
#  {'current': 2419200, 'min': 710400, 'max': 2419200},
#  {'current': 2841600, 'min': 844800, 'max': 2841600}]
```

#### CPU Usage per-core

```python
TermuxHardwareStats.cpu_percent()
# [23.0, 100.0, 84.0, 18.0, 97.0, 10.0, 100.0, 43.0]
```
