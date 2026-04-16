@echo off
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
--new-window ^
--disable-sync ^
--disable-background-networking ^
--disable-default-apps ^
--disable-extensions ^
--disable-component-update ^
--disable-features=Translate,MediaRouter,OptimizationHints,NetworkPrediction ^
--dns-prefetch-disable ^
--no-first-run ^
--no-pings ^
--js-flags="--jitless"

