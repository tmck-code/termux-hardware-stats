package main

import (
    "fmt"
    "io/ioutil"
    "encoding/json"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

var BASE_DIR = "/sys/devices/system/cpu"

var STATS = map[string]string{
	"curr_freq": "cpufreq/scaling_cur_freq",
	"min_freq":  "cpufreq/scaling_min_freq",
	"max_freq":  "cpufreq/scaling_max_freq",
}

func main() {
    dat, err := ioutil.ReadFile(
		fmt.Sprintf("%s/%s/%s", BASE_DIR, "cpu0", STATS["curr_freq"]),
	)
    check(err)

    json, _ := json.Marshal(
		map[string]string{
			"cpu": "cpu0",
			"key": "curr_freq",
			"value": strings.Trim(string(dat), "\n"),
		},
	)
    fmt.Println(string(json))
}

