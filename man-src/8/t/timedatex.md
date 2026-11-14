---
title: "timedatex(8)"
name: "timedatex"
section: "8"
letter: "t"
url: "/docs/linux/man/8-timedatex/"
description: "timedatex – D-Bus service for system clock and RTC settings"
---

<p>timedatex &#8211; D-Bus service for system clock and RTC settings </p>
<h2>Synopsis</h2>
<p><code>timedatex</code> </p>
<h2>Description</h2>
<p>timedatex is a D-Bus service that implements the org.freedesktop.timedate1 interface. It can be used to read and set the system clock, the real-time clock (RTC), the system timezone, and enable or disable an NTP client installed on the system. It is a replacement for the systemd-timedated service. The system clock is read and set with microsecond resolution, the precision is limited mostly by D-Bus latency. When setting the clock to an absolute time, a correction is applied for the time spent in the polkit authorization check. The clock can be also adjusted precisely by an offset. The RTC is read with a resolution of one second. The hwclock program is used to set the RTC with a high precision, update the estimated drift, and change the UTC/LOCAL setting. The system timezone is set by creating symlink /etc/localtime to a file in the /usr/share/zoneinfo directory. NTP units that should be controlled by timedatex need to be listed in text files in /etc/systemd/ntp-units.d and /usr/lib/systemd/ntp-units.d directories. The first valid unit from the files sorted by name can be enabled/disabled and started/stopped. Other NTP units will be disabled and stopped. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-timedated/">systemd-timedated</a></code>(8), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) </p>
<h2>Author</h2>
<p>Miroslav Lichvar &lt;mlichvar [at] redhat.com&gt;</p>
