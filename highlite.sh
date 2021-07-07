SCRIPT_PATH=$(dirname ${BASH_SOURCE[0]})
hl() {
  if which python3 &>/dev/null; then
    python3 $SCRIPT_PATH/highlite.py "$@"
  else
    echo "Couldn't locate python3"
  fi
}

