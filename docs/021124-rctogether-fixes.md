on February 11th 2024, Greg did some fixes to try to improve the stability of RCTV

the extremely TLDR version is that 1. we now load rctvtogether (as an rctv app) without having to manually log into the recurse.com oauth (using Greg's credentials) and 2. we now use a chrome extension to override the x-frame-options AND (most importantly and incredibly) we use privoxy to override a cookie policy which was making it impossible to iframe rctogether

yes, the raspi now runs a privoxy proxy, and chromium has been configured to accept a self signed ssl authority to let the fake/self-signed ssl certificate for recurse.rctogether.com to be seen as valid

Greg also added a line into the crontab so that the raspi would restart once a day, hopefully helping with instability / weird non-states where chromium couldn't even be started after the raspi had been running for some time (probably because the ram was full? or something was off?). a reboot most always fixes everything...

---

for future hackers:
- the rctv.service described by Jacob in the readme can be edited -- if/when you do that and want to restart the rctv service (which starts chromium), run `sudo systemctl daemon-reload; sudo systemctl restart rctv`
- the privoxy also runs as a service and can be restarted with `sudo systemctl restart privoxy` (start/stop/status also work)
- the once-a-day restarting was done using a cron, so `sudo crontab -e` to edit that
- privoxy files are under /etc/privoxy, be root to do stuff but also `chown privoxy:root` files/dirs to make sure that the privoxy user can read/write them
- privoxy doesn't log anything by default, you can enable logging in /etc/privoxy/config by enabling all of the `debug <NUMBER>` lines
- when privoxy logging is enabled, logs can be found in /var/log/privoxy/logfile
- I'm not sure if the privoxy service needs to be restarted between changes to config and/or user.filter or user.action, but it's always safer to do so using `sudo systemctl restart privoxy`
- the rctogether privoxy header hacks specifically live in /etc/privoxy/user.action and .../user.filter
- there are also hacks for example.com that are just there to check that privoxy https proxying does work