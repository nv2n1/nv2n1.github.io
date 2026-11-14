---
title: "localtime(5)"
name: "localtime"
section: "5"
letter: "l"
url: "/docs/linux/man/5-localtime/"
description: "localtime – Local timezone configuration file"
---

<p>localtime &#8211; Local timezone configuration file</p>
<h2>Synopsis</h2>
<p>/etc/localtime -&gt; ../usr/share/zoneinfo/&#8230;</p>
<h2>Description</h2>
<p>The /etc/localtime file configures the system-wide timezone of the local system that is used by applications for presentation to the user. It should be an absolute or relative symbolic link pointing to /usr/share/zoneinfo/, followed by a timezone identifier such as &quot;Europe/Berlin&quot; or &quot;Etc/UTC&quot;. The resulting link should lead to the corresponding binary <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5) timezone data for the configured timezone. </p>
<p> Because the timezone identifier is extracted from the symlink target name of /etc/localtime, this file may not be a normal file or hardlink. </p>
<p> If /etc/localtime is missing, the default &quot;UTC&quot; timezone is used. </p>
<p> The timezone may be overridden for individual programs by using the <i>$TZ</i> environment variable. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<p> You may use <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1) to change the settings of this file from the command line during runtime. Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize the time zone on mounted (but not booted) system images.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-timedated-service/">systemd-timedated.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) </p>
