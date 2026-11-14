---
title: "rdate(8)"
name: "rdate"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdate/"
description: "rdate – set the system’s date from a remote host"
---

<p><code>rdate</code> &#8211; set the system&#8217;s date from a remote host</p>
<h2>Synopsis</h2>
<p><code>rdate</code> [-<code>46acnpsuv</code> ] [-<code>o </code><i>port</i> ] <i>host</i></p>
<h2>Description</h2>
<p><code>rdate</code> displays and sets the local date and time from the host name or address given as the argument. The time source may be an RFC 868 TCP protocol server, which is usually implemented as a built-in service of <a href="/docs/linux/man/8-inetd/">inetd</a>(8), or an RFC 2030 protocol SNTP/NTP server. By default, <code>rdate</code> uses the RFC 868 TCP protocol. The options are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd>Forces <code>rdate</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd>Forces <code>rdate</code> to use IPv6 addresses only.</p>
<dt><code>-a</code></p>
<dd>Use the <a href="/docs/linux/man/2-adjtime/">adjtime</a>(2) call to gradually skew the local time to the remote time rather than just hopping.</p>
<dt><code>-c</code></p>
<dd>Correct leap seconds. Sometimes required when synchronizing to an NTP server. When synchronizing using the RFC 868 protocol, use this option only if the server does not correctly account for leap seconds. You can determine if you need this parameter if you sync against an NTP server (with this parameter) or (recommended) check with a local radio controlled watch or phone service.</p>
<dt><code>-n</code></p>
<dd>Use SNTP (RFC 2030) instead of the RFC 868 time protocol.</p>
<dt><code>-o </code><i>port</i></p>
<dd>Use port <i>port</i> instead of port 37.</p>
<dt><code>-p</code></p>
<dd>Do not set, just print the remote time.</p>
<dt><code>-s</code></p>
<dd>Do not print the time.</p>
<dt><code>-u</code></p>
<dd>Use UDP instead of TCP as transport.</p>
<dt><code>-v</code></p>
<dd>Verbose output. Always show the adjustment.</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/log/wtmp </code></p>
<dd>record of date resets and time changes</dl>
<h2>Examples</h2>
<p>To get the legal time in Germany, set the /etc/localtime symlink to /usr/share/zoneinfo/right/Europe/Berlin and issue the following command: The command of course assumes you have a working internet connection and DNS set up to connect to the server at <code>Physikalisch-Technische Bundesanstalt</code> in Braunschweig, Germany. To gradually adjust time once an hour after the first Qq step adjustment, put the following line into root&#8217;s crontab: To to set the time through an ssh tunnel, use something like so: </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-date/">date</a>(1), <a href="/docs/linux/man/2-adjtime/">adjtime</a>(2), <a href="/docs/linux/man/8-inetd/">inetd</a>(8), <a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/8-timed/">timed</a>(8)</p>
<h2>Authors</h2>
<p>This manual page was written by An Christos Zoulas. It was changed by An Anibal Monsalve Salazar for the Debian Project.</p>
