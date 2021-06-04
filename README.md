# termux-hardware-stats

A utility to fetch available hardware stats in Termux (Android)

## Available stats

CPU stats are available in termux via text files. These files live under:

```
/sys/devices/system/cpu/
```

> _(note: not all of the files under this directory are readable)_

### Working stats

#### CPU Frequencies (current, min & max)

CPU frequency info can be found under per-core directores, e.g. for the first
core:

```bash
$ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
1804800
```

There is a corresponding `core<n>` directory for each core on your phone. For
example, my phone is currently the OnePlus 9, which runs the 8-core Snapdragon
888

If I check inside the cpu stats directory I can see 8 directories, which are
symlinks that point to 3 different policy folders

```
 ☯ ~ ls -alh /sys/devices/system/cpu/cpu*/cpufreq
lrwxrwxrwx 1 root root 0 Jun  4 23:20 /sys/devices/system/cpu/cpu0/cpufreq -> ../cpufreq/policy0
lrwxrwxrwx 1 root root 0 Jun  4 23:25 /sys/devices/system/cpu/cpu1/cpufreq -> ../cpufreq/policy0
lrwxrwxrwx 1 root root 0 Jun  4 23:25 /sys/devices/system/cpu/cpu2/cpufreq -> ../cpufreq/policy0
lrwxrwxrwx 1 root root 0 Jun  4 23:25 /sys/devices/system/cpu/cpu3/cpufreq -> ../cpufreq/policy0
lrwxrwxrwx 1 root root 0 Jun  4 23:20 /sys/devices/system/cpu/cpu4/cpufreq -> ../cpufreq/policy4
lrwxrwxrwx 1 root root 0 Jun  4 23:25 /sys/devices/system/cpu/cpu5/cpufreq -> ../cpufreq/policy4
lrwxrwxrwx 1 root root 0 Jun  4 23:25 /sys/devices/system/cpu/cpu6/cpufreq -> ../cpufreq/policy4
lrwxrwxrwx 1 root root 0 Jun  4 23:20 /sys/devices/system/cpu/cpu7/cpufreq -> ../cpufreq/policy7
```

This matches the configuration of the 8-core Snapdragon 888, which has the
following cores:

- 1x 2.84GHz (Cortex-X1)
- 3x 2.4GHz (Cortex-A78)
- 4x 1.8GHz (Cortex-A55)

Using this information, I'm able to map each cpu directory to its matching Snapdragon
core

