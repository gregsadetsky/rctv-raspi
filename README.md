# NOTE NOTE NOTE

the raspberry pi has been rebuilt with a new pi 5 w/ ssd, and it now runs a completely different rust-based Tauri program - whose code [is here](https://github.com/gregsadetsky/rctv-tauri)!!!

---

# rctv-raspi

Hardware counterpart to RCTV software -- [repo here](https://github.com/gregsadetsky/rctv/).

## Setup Documentation

The Raspberry Pi running locally to render RC TV has some configuration files
which need to be inserted and tested to turn the TV into a proper display


**SSH Into the Raspberry PI**

```
# Connect to the Recurse WIFI 

# SSH password is the same as the Recurse WIFI password
ssh rctv@rctv.local
```


### docs

- [systemd-service.md](docs/systemd-service.md)
- [mouse-hiding.md](docs/mouse-hiding.md)
- [021124-rctogether-fixes.md](docs/021124-rctogether-fixes.md)
