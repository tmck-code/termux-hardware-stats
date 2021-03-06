# Examples

- [Examples](#examples)
  - [CPU](#cpu)

## CPU

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

<details>
    <summary>All CPU stats</summary>
    I used a find command to find all files under the main CPU stats directory that are
    readable by a non-root termux user

    Command:

    ```bash
    find /sys/devices/system/cpu/ -type f -readable
    ```

    Output:

    ```text
    /sys/devices/system/cpu/core_ctl_isolated
    /sys/devices/system/cpu/cpu0/cache/index0/level
    /sys/devices/system/cpu/cpu0/cache/index0/shared_cpu_list
    /sys/devices/system/cpu/cpu0/cache/index0/shared_cpu_map
    /sys/devices/system/cpu/cpu0/cache/index0/type
    /sys/devices/system/cpu/cpu0/cache/index0/uevent
    /sys/devices/system/cpu/cpu0/cache/index0/waiting_for_supplier
    /sys/devices/system/cpu/cpu0/cache/index1/level
    /sys/devices/system/cpu/cpu0/cache/index1/shared_cpu_list
    /sys/devices/system/cpu/cpu0/cache/index1/shared_cpu_map
    /sys/devices/system/cpu/cpu0/cache/index1/type
    /sys/devices/system/cpu/cpu0/cache/index1/uevent
    /sys/devices/system/cpu/cpu0/cache/index1/waiting_for_supplier
    /sys/devices/system/cpu/cpu0/cache/index2/level
    /sys/devices/system/cpu/cpu0/cache/index2/shared_cpu_list
    /sys/devices/system/cpu/cpu0/cache/index2/shared_cpu_map
    /sys/devices/system/cpu/cpu0/cache/index2/type
    /sys/devices/system/cpu/cpu0/cache/index2/uevent
    /sys/devices/system/cpu/cpu0/cache/index2/waiting_for_supplier
    /sys/devices/system/cpu/cpu0/cache/index3/level
    /sys/devices/system/cpu/cpu0/cache/index3/shared_cpu_list
    /sys/devices/system/cpu/cpu0/cache/index3/shared_cpu_map
    /sys/devices/system/cpu/cpu0/cache/index3/type
    /sys/devices/system/cpu/cpu0/cache/index3/uevent
    /sys/devices/system/cpu/cpu0/cache/index3/waiting_for_supplier
    /sys/devices/system/cpu/cpu0/cache/uevent
    /sys/devices/system/cpu/cpu0/cache/waiting_for_supplier
    /sys/devices/system/cpu/cpu0/core_ctl/active_cpus
    /sys/devices/system/cpu/cpu0/core_ctl/busy_down_thres
    /sys/devices/system/cpu/cpu0/core_ctl/busy_up_thres
    /sys/devices/system/cpu/cpu0/core_ctl/enable
    /sys/devices/system/cpu/cpu0/core_ctl/global_state
    /sys/devices/system/cpu/cpu0/core_ctl/max_cpus
    /sys/devices/system/cpu/cpu0/core_ctl/min_cpus
    /sys/devices/system/cpu/cpu0/core_ctl/need_cpus
    /sys/devices/system/cpu/cpu0/core_ctl/not_preferred
    /sys/devices/system/cpu/cpu0/core_ctl/nr_prev_assist_thresh
    /sys/devices/system/cpu/cpu0/core_ctl/offline_delay_ms
    /sys/devices/system/cpu/cpu0/core_ctl/task_thres
    /sys/devices/system/cpu/cpu0/cpu_capacity
    /sys/devices/system/cpu/cpu0/cpuidle/driver/name
    /sys/devices/system/cpu/cpu0/cpuidle/state0/above
    /sys/devices/system/cpu/cpu0/cpuidle/state0/below
    /sys/devices/system/cpu/cpu0/cpuidle/state0/desc
    /sys/devices/system/cpu/cpu0/cpuidle/state0/disable
    /sys/devices/system/cpu/cpu0/cpuidle/state0/latency
    /sys/devices/system/cpu/cpu0/cpuidle/state0/name
    /sys/devices/system/cpu/cpu0/cpuidle/state0/power
    /sys/devices/system/cpu/cpu0/cpuidle/state0/residency
    /sys/devices/system/cpu/cpu0/cpuidle/state0/time
    /sys/devices/system/cpu/cpu0/cpuidle/state0/usage
    /sys/devices/system/cpu/cpu0/cpuidle/state1/above
    /sys/devices/system/cpu/cpu0/cpuidle/state1/below
    /sys/devices/system/cpu/cpu0/cpuidle/state1/desc
    /sys/devices/system/cpu/cpu0/cpuidle/state1/disable
    /sys/devices/system/cpu/cpu0/cpuidle/state1/latency
    /sys/devices/system/cpu/cpu0/cpuidle/state1/name
    /sys/devices/system/cpu/cpu0/cpuidle/state1/power
    /sys/devices/system/cpu/cpu0/cpuidle/state1/residency
    /sys/devices/system/cpu/cpu0/cpuidle/state1/s2idle/time
    /sys/devices/system/cpu/cpu0/cpuidle/state1/s2idle/usage
    /sys/devices/system/cpu/cpu0/cpuidle/state1/time
    /sys/devices/system/cpu/cpu0/cpuidle/state1/usage
    /sys/devices/system/cpu/cpu0/dcvsh_freq_limit
    /sys/devices/system/cpu/cpu0/hotplug/fail
    /sys/devices/system/cpu/cpu0/hotplug/state
    /sys/devices/system/cpu/cpu0/hotplug/target
    /sys/devices/system/cpu/cpu0/isolate
    /sys/devices/system/cpu/cpu0/online
    /sys/devices/system/cpu/cpu0/power/autosuspend_delay_ms
    /sys/devices/system/cpu/cpu0/power/control
    /sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us
    /sys/devices/system/cpu/cpu0/power/runtime_active_time
    /sys/devices/system/cpu/cpu0/power/runtime_status
    /sys/devices/system/cpu/cpu0/power/runtime_suspended_time
    /sys/devices/system/cpu/cpu0/regs/identification/midr_el1
    /sys/devices/system/cpu/cpu0/regs/identification/revidr_el1
    /sys/devices/system/cpu/cpu0/sched_load_boost
    /sys/devices/system/cpu/cpu0/topology/core_cpus
    /sys/devices/system/cpu/cpu0/topology/core_cpus_list
    /sys/devices/system/cpu/cpu0/topology/core_id
    /sys/devices/system/cpu/cpu0/topology/core_siblings
    /sys/devices/system/cpu/cpu0/topology/core_siblings_list
    /sys/devices/system/cpu/cpu0/topology/die_cpus
    /sys/devices/system/cpu/cpu0/topology/die_cpus_list
    /sys/devices/system/cpu/cpu0/topology/die_id
    /sys/devices/system/cpu/cpu0/topology/package_cpus
    /sys/devices/system/cpu/cpu0/topology/package_cpus_list
    /sys/devices/system/cpu/cpu0/topology/physical_package_id
    /sys/devices/system/cpu/cpu0/topology/thread_siblings
    /sys/devices/system/cpu/cpu0/topology/thread_siblings_list
    /sys/devices/system/cpu/cpu0/uevent
    /sys/devices/system/cpu/cpu0/waiting_for_supplier
    /sys/devices/system/cpu/cpu_boost/input_boost_freq
    /sys/devices/system/cpu/cpu_boost/input_boost_ms
    /sys/devices/system/cpu/cpu_boost/sched_boost_on_input
    /sys/devices/system/cpu/cpufreq/policy0/affected_cpus
    /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_max_freq
    /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_min_freq
    /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_transition_latency
    /sys/devices/system/cpu/cpufreq/policy0/freq_change_info
    /sys/devices/system/cpu/cpufreq/policy0/related_cpus
    /sys/devices/system/cpu/cpufreq/policy0/scaling_available_frequencies
    /sys/devices/system/cpu/cpufreq/policy0/scaling_available_governors
    /sys/devices/system/cpu/cpufreq/policy0/scaling_boost_frequencies
    /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq
    /sys/devices/system/cpu/cpufreq/policy0/scaling_driver
    /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq
    /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq
    /sys/devices/system/cpu/cpufreq/policy0/scaling_setspeed
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/down_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/hispeed_freq
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/hispeed_load
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/pl
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/rtg_boost_freq
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/target_loads
    /sys/devices/system/cpu/cpufreq/policy0/schedutil/up_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy0/stats/time_in_state
    /sys/devices/system/cpu/cpufreq/policy0/stats/total_trans
    /sys/devices/system/cpu/cpufreq/policy0/stats/trans_table
    /sys/devices/system/cpu/cpufreq/policy4/affected_cpus
    /sys/devices/system/cpu/cpufreq/policy4/cpuinfo_max_freq
    /sys/devices/system/cpu/cpufreq/policy4/cpuinfo_min_freq
    /sys/devices/system/cpu/cpufreq/policy4/cpuinfo_transition_latency
    /sys/devices/system/cpu/cpufreq/policy4/freq_change_info
    /sys/devices/system/cpu/cpufreq/policy4/related_cpus
    /sys/devices/system/cpu/cpufreq/policy4/scaling_available_frequencies
    /sys/devices/system/cpu/cpufreq/policy4/scaling_available_governors
    /sys/devices/system/cpu/cpufreq/policy4/scaling_boost_frequencies
    /sys/devices/system/cpu/cpufreq/policy4/scaling_cur_freq
    /sys/devices/system/cpu/cpufreq/policy4/scaling_driver
    /sys/devices/system/cpu/cpufreq/policy4/scaling_max_freq
    /sys/devices/system/cpu/cpufreq/policy4/scaling_min_freq
    /sys/devices/system/cpu/cpufreq/policy4/scaling_setspeed
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/down_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/hispeed_freq
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/hispeed_load
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/pl
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/rtg_boost_freq
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/target_loads
    /sys/devices/system/cpu/cpufreq/policy4/schedutil/up_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy4/stats/time_in_state
    /sys/devices/system/cpu/cpufreq/policy4/stats/total_trans
    /sys/devices/system/cpu/cpufreq/policy4/stats/trans_table
    /sys/devices/system/cpu/cpufreq/policy7/affected_cpus
    /sys/devices/system/cpu/cpufreq/policy7/cpuinfo_max_freq
    /sys/devices/system/cpu/cpufreq/policy7/cpuinfo_min_freq
    /sys/devices/system/cpu/cpufreq/policy7/cpuinfo_transition_latency
    /sys/devices/system/cpu/cpufreq/policy7/freq_change_info
    /sys/devices/system/cpu/cpufreq/policy7/related_cpus
    /sys/devices/system/cpu/cpufreq/policy7/scaling_available_frequencies
    /sys/devices/system/cpu/cpufreq/policy7/scaling_available_governors
    /sys/devices/system/cpu/cpufreq/policy7/scaling_boost_frequencies
    /sys/devices/system/cpu/cpufreq/policy7/scaling_cur_freq
    /sys/devices/system/cpu/cpufreq/policy7/scaling_driver
    /sys/devices/system/cpu/cpufreq/policy7/scaling_max_freq
    /sys/devices/system/cpu/cpufreq/policy7/scaling_min_freq
    /sys/devices/system/cpu/cpufreq/policy7/scaling_setspeed
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/down_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/hispeed_freq
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/hispeed_load
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/pl
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/rtg_boost_freq
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/target_loads
    /sys/devices/system/cpu/cpufreq/policy7/schedutil/up_rate_limit_us
    /sys/devices/system/cpu/cpufreq/policy7/stats/time_in_state
    /sys/devices/system/cpu/cpufreq/policy7/stats/total_trans
    /sys/devices/system/cpu/cpufreq/policy7/stats/trans_table
    /sys/devices/system/cpu/cpuidle/current_driver
    /sys/devices/system/cpu/cpuidle/current_governor_ro
    /sys/devices/system/cpu/hang_detect_core/enable
    /sys/devices/system/cpu/hang_detect_core/pmu_event_sel
    /sys/devices/system/cpu/hang_detect_core/threshold
    /sys/devices/system/cpu/hotplug/states
    /sys/devices/system/cpu/hyp_core_ctl/enable
    /sys/devices/system/cpu/hyp_core_ctl/hcc_min_freq
    /sys/devices/system/cpu/hyp_core_ctl/status
    /sys/devices/system/cpu/isolated
    /sys/devices/system/cpu/kernel_max
    /sys/devices/system/cpu/modalias
    /sys/devices/system/cpu/offline
    /sys/devices/system/cpu/online
    /sys/devices/system/cpu/possible
    /sys/devices/system/cpu/power/autosuspend_delay_ms
    /sys/devices/system/cpu/power/control
    /sys/devices/system/cpu/power/runtime_active_time
    /sys/devices/system/cpu/power/runtime_status
    /sys/devices/system/cpu/power/runtime_suspended_time
    /sys/devices/system/cpu/present
    /sys/devices/system/cpu/smt/active
    /sys/devices/system/cpu/smt/control
    /sys/devices/system/cpu/uevent
    /sys/devices/system/cpu/vulnerabilities/itlb_multihit
    /sys/devices/system/cpu/vulnerabilities/l1tf
    /sys/devices/system/cpu/vulnerabilities/mds
    /sys/devices/system/cpu/vulnerabilities/meltdown
    /sys/devices/system/cpu/vulnerabilities/spec_store_bypass
    /sys/devices/system/cpu/vulnerabilities/spectre_v1
    /sys/devices/system/cpu/vulnerabilities/spectre_v2
    /sys/devices/system/cpu/vulnerabilities/srbds
    /sys/devices/system/cpu/vulnerabilities/tsx_async_abort
    /sys/devices/system/cpu/waiting_for_supplier
    ```
</detail>