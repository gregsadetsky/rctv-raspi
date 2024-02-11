### Mouse Hiding


**Goals**

* We don't want a mouse pointer floating around the screen at all times
* We can use `unclutter` command line tool to hide the mouse adter `0.5s` of
  inactivity
* Again we can use `systemd` to define a service which only starts `unclutter`
  when the GUI is ready


**Installing**

2. Create a new systemd service at `/lib/systemd/system/hidemouse.service`
3. Copy the file below
4. Reload the `systemctl` daemon using `sudo systemctl daemon-reload`
5. Enable our `hidemouse.service` to be run on boot using `sudo systemctl enable hidemouse.service`
6. Reboot the Raspberry Pi using `sudo reboot`
7. Testing Locally Without Rebooting
  * `sudo systemctl start hidemouse.service`
  * `sudo systemctl stop hidemouse.service`
  * `sudo systemctl restart hidemouse.service`
  * `journalctl -u hidemouse -b --no-pager` to show the `hidemouse.service` logs since the
    last boot `-b` and now use a pager to view the output `--no-pager`


```systemd
# hidemouse.service

[Unit]
Description=RC TV Hide Mouse
Wants=graphical.target
After=graphical.target

[Service]
Type=simple
Environment=DISPLAY=:0.0
Environment=XAUTHORITY=/home/rctv/.Xauthority
ExecStart=/usr/bin/bash -c "/usr/bin/unclutter -idle 0.5 -root > /home/rctv/rctv-kiosk/hidemouse.log 2>&1"
Restart=on-abort
User=rctv
Group=rctv

[Install]
WantedBy=graphical.target
```


**Debugging**

- see [systemd-service.md](./systemd-service.md)
