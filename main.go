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
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
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

