---
title: "uptime(1)"
name: "uptime"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uptime/"
description: "uptime – Tell how long the system has been running."
---

<h2 class="name">NAME</h2>
<p> uptime &#8211; Tell how long the system has been running. </p>
<h2>SYNOPSIS</h2>
<p> <code>uptime</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>uptime</code> gives a one line display of the following information. The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes. </p>
<p> This is the same information contained in the header line displayed by <code><a href="/docs/linux/man/1-w/">w</a></code>(1). </p>
<p> System load averages is the average number of processes that are either in a runnable or uninterruptable state. A process in a runnable state is either using the CPU or waiting to use the CPU. A process in uninterruptable state is waiting for some I/O access, eg waiting for disk. The averages are taken over the three time intervals. Load averages are not normalized for the number of CPUs in a system, so a load average of 1 means a single CPU system is loaded all the time while on a 4 CPU system it means it was idle 75% of the time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;pretty</code></p>
<dd> show uptime in pretty format</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help text</p>
<dt><code>-s</code>, <code>&#8211;since</code></p>
<dd> system up since, in yyyy-mm-dd HH:MM:SS format</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/utmp</i></p>
<dd> information about who is currently logged on</p>
<dt><i>/proc</i></p>
<dd> process information</dl>
<h2>AUTHORS</h2>
<p> <code>uptime</code> was written by Larry Greenfield and Michael K. Johnson</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5), <code><a href="/docs/linux/man/1-w/">w</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
