# ansible-n4dkn-rpi4

[![CI](https://github.com/deekayen/ansible-n4dkn-rpi4/actions/workflows/ci.yml/badge.svg)](https://github.com/deekayen/ansible-n4dkn-rpi4/actions/workflows/ci.yml)

Configuration for a Raspberry Pi 4 running mesh services for AREDN.

## Bridging to the Internet

When bridging to the Internet, the default route is the hard wire. Getting NTP or system updates from the Internet is a different default route.

# Edit dhcpcd's configuration.

```
$ sudo vi /etc/dhcpcd.conf
```

Add the following to the end of the file and save it:

```
interface wlan0
metric 0
```

Restart dhcpcd.

```
$ sudo systemctl restart dhcpcd
```

Test:

```
$ ip route list
```
