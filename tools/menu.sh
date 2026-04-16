#!/usr/bin/env bash

echo "1) Normal"
echo "2) Secure"
echo "3) Stealth"
echo "4) Scan local"
read -p "Select: " opt

case $opt in
  1) ./cyber-chrome.sh normal ;;
  2) ./cyber-chrome.sh secure ;;
  3) ./cyber-chrome.sh stealth ;;
  4) ./tools/scan.sh ;;
esac
