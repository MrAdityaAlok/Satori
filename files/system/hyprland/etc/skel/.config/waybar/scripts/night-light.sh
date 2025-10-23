#!/bin/bash

CONFIG_FILE="$HOME/.config/waybar/scripts/.night-light"

temp="$(cat "$CONFIG_FILE")"

# Default value:
if test -z "$temp"; then
  temp=4000
fi

is_running() {
  pgrep -x "hyprsunset" >/dev/null
  return $?
}

start_hyprsunset() {
  ! is_running && hyprsunset -t "$temp" &
}

stop_hyprsunset() {
  is_running && pkill "hyprsunset" 2>/dev/null
}

restart_hyprsunset() {
  if is_running; then
    stop_hyprsunset
    start_hyprsunset
  fi
}

mod() {
  local v="$1"
  if ((v > 20000)); then
    v=20000
  elif ((v < 1000)); then
    v=1000
  fi
  echo "$v"
}

case "$1" in
"toggle")
  if is_running; then
    stop_hyprsunset
  else
    start_hyprsunset
  fi
  ;;
"increase")
  temp=$(mod $((temp + 500)))
  echo "$temp" >"$CONFIG_FILE"
  restart_hyprsunset
  ;;
"decrease")
  temp=$(mod $((temp - 500)))
  echo "$temp" >"$CONFIG_FILE"
  restart_hyprsunset
  ;;
"status")
  if is_running; then
    echo "{\"text\": \" 󰖔 \", \"class\": \"on\", \"tooltip\": \"Night Light: ON ($temp K)\"}"
  else
    echo "{\"text\": \" 󰖨 \", \"class\": \"off\", \"tooltip\": \"Night Light: OFF ($temp K)\"}"
  fi
  ;;
esac
