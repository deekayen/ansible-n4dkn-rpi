# chrony

Instructions:
* https://photobyte.org/raspberry-pi-stretch-gps-dongle-as-a-time-source-with-chrony-timedatectl/
* https://chrony.tuxfamily.org/doc/3.4/chrony.conf.html

```
sudo apt -y install gpsd gpsd-clients python-gps chrony python-gi-cairo
```

```
sudo nano /etc/default/gpsd
```

Add lines:

```
START_DAEMON="true"
USBAUTO="true"
DEVICES="/dev/ttyACM0"
GPSD_OPTIONS="-n"
```

```
systemctl enable gpsd
systemctl enable chronyd
```

Validate:

```
cgps –s
gpsmon -n
```

```
sudo "echo refclock SHM 0 offset 0.5 delay 0.2 refid NMEA" >> /etc/chrony/chrony.conf
```

```
chronyc sources -v
sudo chronyc tracking
```

Speed up the clock sync with an explicit step:

```
sudo chronyc makestep
```
