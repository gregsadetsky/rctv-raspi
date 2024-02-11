### Custom RCTV Systemd Service

**Goals**

* On startup, launch `/usr/bin/chromium-browser` in `--kiosk` mode
* Ensure that the Raspberry Pi never puts the display to sleep
* Relaunch the service if it was aborted
* Only launch the service once the GUI is ready


**Installing**

1. Ensure that `$DISPLAY` is set even when connecting over SSH `echo "export
   DISPLAY=:0.0 >> ~/.bashrc`
2. Create a new systemd service at `/lib/systemd/system/rctv.service`
3. Copy the file below
4. Reload the `systemctl` daemon using `sudo systemctl daemon-reload`
5. Enable our `rctv.service` to be run on boot using `sudo systemctl enable rctv.service`
6. Reboot the Raspberry Pi using `sudo reboot`
7. Testing Locally Without Rebooting
  * `sudo systemctl start rctv.service`
  * `sudo systemctl stop rctv.service`
  * `sudo systemctl restart rctv.service`
  * `journalctl -u rctv -b --no-pager` to show the `rctv.service` logs since the
    last boot `-b` and now use a pager to view the output `--no-pager`


**Debugging**

1. Use `systemd-analyze verify rctv.service` to see any issues with the service
   file
2. To see logs from systemd immediately after boot, view the file `sudo tail -f
   /var/log/boot.log` and search for `rctv.service`
3. If `systemd-analyze` shows a cyclic dependency (e.g. `multi-user.target`
   requires `graphical.target` which requires `multi-user.target`), this may be
   solved by removing symlinks to `rctv.service` in
   `/etc/systemd/system/multi-user.target.wants` or
   `/etc/systemd/system/graphical.target.wants`
4. Lots of googling


```systemd
# rctv.service

[Unit]
Description=RC TV Startup
Wants=graphical.target
After=graphical.target

[Service]
Type=simple
Environment=DISPLAY=:0.0
Environment=XAUTHORITY=/home/rctv/.Xauthority
ExecStartPre=/home/rctv/rctv-kiosk/kiosk.sh
ExecStart=/usr/bin/chromium-browser --no-sandbox --noerrdialogs --disable-infobars --kiosk https://rctv.recurse.com
Restart=on-abort
User=rctv
Group=rctv

[Install]
WantedBy=graphical.target

```
