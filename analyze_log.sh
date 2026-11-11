#!/usr/bin/env bash

log_file="${1:-transit_session.log}"

if [[ ! -f "$log_file" ]]; then
    printf 'Error: log file not found: %s\n' "$log_file" >&2
    exit 1
fi

awk '
    /===== New session started/ { sessions++ }
    /Zebra crossing! Stopping for/ { zebra_stops++ }
    /Changing lane:/ { lane_changes++ }
    /Driver[[:space:]]*:/ {
        sub(/^.*Driver[[:space:]]*:[[:space:]]*/, "")
        driver = $0
    }
    /Top speed[[:space:]]*:/ {
        sub(/^.*Top speed[[:space:]]*:[[:space:]]*/, "")
        top_speed = $0
    }
    END {
        printf "Sessions: %d\n", sessions
        printf "Zebra crossing stops: %d\n", zebra_stops
        printf "Lane changes: %d\n", lane_changes
        if (driver != "" || top_speed != "") {
            printf "Latest driver: %s\n", driver ? driver : "Unknown"
            printf "Latest top speed: %s\n", top_speed ? top_speed : "Unknown"
        } else {
            print "Latest trip: no completed trip report found"
        }
    }
' "$log_file"
