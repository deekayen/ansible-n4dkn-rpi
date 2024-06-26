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
static ip_address=192.168.0.4/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.3 192.168.0.1
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

## APRS IGate

/home/pi/pigate-direwolf.conf

```
ADEVICE stdin null
ARATE 24000
CHANNEL 0

MYCALL N4DKN-10

IGSERVER noam.aprs2.net

IGLOGIN N4DKN-10 12345

PBEACON sendto=IG delay=0:30 every=10:00 symbol="igate" overlay=R lat=34^18.84N long=084^04.64W altitude=390 height=1278 dir=E comment="Silver City piGate ///stems.typists.attracts"
```
