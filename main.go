package main

import (
    "fmt"
    "io/ioutil"
    "encoding/json"
	"strings"
)

var N_CPUS = 8
var BASE_DIR = "/sys/devices/system/cpu"
var STATS = map[string]string{
	"curr_freq": "cpufreq/scaling_cur_freq",
	"min_freq":  "cpufreq/scaling_min_freq",
	"max_freq":  "cpufreq/scaling_max_freq",
	"global_state": "core_ctl/global_state",
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func demo_curr_freq() {
	for i := 0 ; i < N_CPUS; i++ {
		core := fmt.Sprintf("%s%d", "cpu", i)
		dat, err := ioutil.ReadFile(
			fmt.Sprintf("%s/%s/%s", BASE_DIR, core, STATS["curr_freq"]),
		)
		check(err)
		json, _ := json.Marshal(
			map[string]string{
				"core": core,
				"key": "curr_freq",
				"value": strings.Trim(string(dat), "\n"),
			},
		)
		fmt.Println(string(json))
	}
}

func demo_global_state() {
	dat, err := ioutil.ReadFile(
		fmt.Sprintf("%s/%s/%s", BASE_DIR, "cpu0", STATS["global_state"]),
	)
	check(err)
	lines := strings.Split(string(dat), "\n")
	current := ""
	stat := "Busy%"
	stats := make(map[string]map[string]string)
	stats[stat] = make(map[string]string)
	for _, el := range(lines) {
		if len(el) == 0 {
			break
		}
		if el[:3] == "CPU" {
			current = el
			continue
		}
		line := strings.Split(strings.TrimSpace(el), ":")
		if line[0] == "Busy%" {
			stats[stat][current] = strings.TrimSpace(line[1])
		}
	}
	json, _ := json.Marshal(stats)
	fmt.Println(string(json))
}

func main() {
	demo_global_state()
	// demo_curr_freq()
}

