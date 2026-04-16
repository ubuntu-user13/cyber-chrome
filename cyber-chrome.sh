#!/usr/bin/env bash
 HEAD
chromium-browser --new-window --disable-features=ChromeWhatsNewUI,MediaRouter


MODE=${1:-normal}

BASE_FLAGS="--new-window --no-first-run --no-pings --dns-prefetch-disable"

NORMAL_FLAGS="$BASE_FLAGS"
SECURE_FLAGS="$BASE_FLAGS --disable-sync --disable-background-networking --disable-extensions --js-flags=--jitless"
STEALTH_FLAGS="$SECURE_FLAGS --incognito"

case "$MODE" in
  normal) FLAGS="$NORMAL_FLAGS" ;;
  secure) FLAGS="$SECURE_FLAGS" ;;
  stealth) FLAGS="$STEALTH_FLAGS" ;;
  *) FLAGS="$NORMAL_FLAGS" ;;
esac

chromium-browser $FLAGS file://$HOME/cyber-chrome/ui/index.html
 878e253 (full cyber chrome toolkit)
