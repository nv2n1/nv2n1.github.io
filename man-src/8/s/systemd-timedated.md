---
title: "systemd-timedated(8)"
name: "systemd-timedated"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-timedated/"
description: "systemd-timedated.service, systemd-timedated – Time and date bus mechanism"
---

<p>systemd-timedated.service, systemd-timedated &#8211; Time and date bus mechanism</p>
<h2>Synopsis</h2>
<p>systemd-timedated.service </p>
<p> /lib/systemd/systemd-timedated</p>
<h2>Description</h2>
<p>systemd-timedated.service is a system service that may be used as a mechanism to change the system clock and timezone, as well as to enable/disable network time synchronization. systemd-timedated is automatically activated on request and terminates itself when it is unused. </p>
<p> The tool <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1) is a command line client to this service. </p>
<p> systemd-timedated currently offers access to the following four settings: </p>
<dl>
<dd>&bull; The system time</dl>
<dl>
<dd>&bull; The system timezone</dl>
<dl>
<dd>&bull; A boolean controlling whether the system RTC is in local or UTC timezone</dl>
<dl>
<dd>&bull; Whether the time synchronization service is enabled/started or disabled/stopped, see next section.</dl>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-timedate1/">org.freedesktop.timedate1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for information about the D-Bus API.</p>
<h2>List Of Network Time Synchronization Services</h2>
<p><code>systemd-timesyncd</code> will look for files with a &quot;.list&quot; extension in ntp-units.d/ directories. Each file is parsed as a list of unit names, one per line. Empty lines and lines with comments (&quot;#&quot;) are ignored. Files are read from /usr/lib/systemd/ntp-units.d/ and the corresponding directories under /etc/, /run/, /usr/local/lib/. Files in /etc/ override files with the same name in /run/, /usr/local/lib/, and /lib/. Files in /run/ override files with the same name under /usr/. Packages should install their configuration files in /usr/lib/ (distribution packages) or /usr/local/lib/ (local installs). </p>
<p> <code>Example 1. ntp-units.d/ entry for systemd-timesyncd</code> </p>
<dl>
<dd>
<pre># /usr/lib/systemd/ntp-units.d/80-systemd-timesync.list
systemd-timesyncd.service</pre>
</dl>
<p> If the environment variable <i>$SYSTEMD_TIMEDATED_NTP_SERVICES</i> is set, <code>systemd-timesyncd</code> will parse the contents of that variable as a colon-separated list of unit names. When set, this variable overrides the file-based list described above. </p>
<p> <code>Example 2. An override that specifies that chronyd should be used if available</code> </p>
<dl>
<dd>
<pre>SYSTEMD_TIMEDATED_NTP_SERVICES=chronyd.service:systemd-timesyncd.service</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1), <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/8-systemd-timesyncd/">systemd-timesyncd</a></code>(8) </p>
