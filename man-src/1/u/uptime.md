---

title: "uptime(1)"
name: "uptime"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uptime/"
description: "uptime – Tell how long the system has been running."
---

<p> <code>uptime</code> [<i>options</i>]</p>
<p> <code>uptime</code> gives a one line display of the following information. The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes. </p>
<p> This is the same information contained in the header line displayed by <code><a href="/docs/linux/man/1-w/">w</a></code>(1). </p>
<p> System load averages is the average number of processes that are either in a runnable or uninterruptable state. A process in a runnable state is either using the CPU or waiting to use the CPU. A process in uninterruptable state is waiting for some I/O access, eg waiting for disk. The averages are taken over the three time intervals. Load averages are not normalized for the number of CPUs in a system, so a load average of 1 means a single CPU system is loaded all the time while on a 4 CPU system it means it was idle 75% of the time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;pretty</code></dt>
<dd> show uptime in pretty format</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help text</dd>
<dt><code>-s</code>, <code>&#8211;since</code></dt>
<dd> system up since, in yyyy-mm-dd HH:MM:SS format</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> display version information and exit</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/utmp</i></dt>
<dd> information about who is currently logged on</dd>
<dt><i>/proc</i></dt>
<dd> process information</dd></dl>
<h2>AUTHORS</h2>
<p> <code>uptime</code> was written by Larry Greenfield and Michael K. Johnson</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5), <code><a href="/docs/linux/man/1-w/">w</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
