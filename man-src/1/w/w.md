---
title: "w(1)"
name: "w"
section: "1"
letter: "w"
url: "/docs/linux/man/1-w/"
description: "w – Show who is logged on and what they are doing."
---

<h2>SYNOPSIS</h2>
<p> <code>w</code> [<i>options</i>] <i>user</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>w</code> displays information about the users currently on the machine, and their processes. The header shows, in this order, the current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes. </p>
<p> The following entries are displayed for each user: login name, the tty name, the remote host, login time, idle time, JCPU, PCPU, and the command line of their current process. </p>
<p> The JCPU time is the time used by all processes attached to the tty. It does not include past background jobs, but does include currently running background jobs. </p>
<p> The PCPU time is the time used by the current process, named in the &quot;what&quot; field.</p>
<h2>COMMAND-LINE OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;no-header</code></dt>
<dd> Don&#8217;t print the header.</dd>
<dt><code>-u</code>, <code>&#8211;no-current</code></dt>
<dd> Ignores the username while figuring out the current process and cpu times. To demonstrate this, do a <code>su</code> and do a <code>w</code> and a <code>w -u.</code></dd>
<dt><code>-s</code>, <code>&#8211;short</code></dt>
<dd> Use the short format. Don&#8217;t print the login time, JCPU or PCPU times.</dd>
<dt><code>-f</code>, <code>&#8211;from</code></dt>
<dd> Toggle printing the <code>from</code> (remote hostname) field. The default as released is for the <code>from</code> field to not be printed, although your system administrator or distribution maintainer may have compiled a version in which the <code>from</code> field is shown by default.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display help text and exit.</dd>
<dt><code>-i</code>, <code>&#8211;ip-addr</code></dt>
<dd> Display IP address instead of hostname for <code>from</code> field.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information.</dd>
<dt><code>-o</code>, <code>&#8211;old-style</code></dt>
<dd> Old style output. Prints blank space for idle times less than one minute.</dd>
<dt><code>user </code></dt>
<dd> Show information about the specified user only.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>PROCPS_USERLEN</dt>
<dd> Override the default width of the username column. Defaults to 8.</dd>
<dt>PROCPS_FROMLEN</dt>
<dd> Override the default width of the from column. Defaults to 16.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/var/run/utmp</i></dt>
<dd> information about who is currently logged on</dd>
<dt><i>/proc</i></dt>
<dd> process information</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5), <code><a href="/docs/linux/man/1-who/">who</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> <code>w</code> was re-written almost entirely by Charles Blake, based on the version by Larry Greenfield and Michael K. Johnson</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
