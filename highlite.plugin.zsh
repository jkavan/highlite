SCRIPT_PATH=$0:A:h

function hl {
  if which python3 &>/dev/null; then
    python3 $SCRIPT_PATH/highlite.py "$@"
  else
    echo "Couldn't locate python3"
  fi
}
