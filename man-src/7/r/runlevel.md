---
title: "runlevel(7)"
name: "runlevel"
section: "7"
letter: "r"
url: "/docs/linux/man/7-runlevel/"
description: "runlevel – event signalling change of system runlevel"
---

<p>runlevel &#8211; event signalling change of system runlevel</p>
<h2>Synopsis</h2>
<p><code>runlevel</code> <code>RUNLEVEL</code>=<i>RUNLEVEL</i> <code>PREVLEVEL</code>=<i>PREVLEVEL</i> [<i>ENV</i>]&#8230;</p>
<h2>Description</h2>
<p>This page describes the <code>runlevel</code> Upstart event, and the general implementation of runlevels in the Upstart system. For the runlevel tool, see <code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8)</p>
<h3>The runlevel event</h3>
<p>The <code>runlevel</code> event signals a change of system runlevel. The new system runlevel is given in the <code>RUNLEVEL</code> argument, and the previous system runlevel in the <code>PREVLEVEL</code> argument (which may be empty). </p>
<p> Additional environment may follow these depending on the runlevel, and the tool that emitted the event. The <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) tool will supply an <code>INIT_HALT</code> variable set to either <i>HALT</i> or <i>POWEROFF</i> when called with <code>-H</code> or <code>-P</code> respectively.</p>
<h3>Runlevels</h3>
<p>Runlevels are a concept from UNIX&#174; System V used by the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon or other system initialisation system to define modes of system operation. </p>
<p> Eight runlevels are permitted, the first seven are numbered <code>0</code>&#8211;<code>6</code> and the eighth is named <code>S</code> or <code>s</code> (both are permitted). </p>
<p> Services and other system components are said to exist in one or more runlevels. When switching from one runlevel to another, the services that should not exist in the new runlevel are stopped and the services that only exist in the new runlevel are started. </p>
<p> This is performed by the <code>/etc/init.d/rc</code> script executed on a change of runlevel (by jobs run on the <code>runlevel</code> event in the Upstart system). This script examines symlinks in the <i>/etc/rc?.d</i> directories, symlinks beginning <code>K</code> are services to be stopped and symlinks beginning <code>S</code> are services to be started. </p>
<p> The authoritative documentation for this process can be found in the <i>System run levels and init.d scripts</i> section of the <i>Debian Policy Manual. This may be currently found at</i> &lt;<code><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-opersys.html#s-sysvinit">http://www.debian.org/doc/debian-policy/ch-opersys.html#s-sysvinit</a></code>&gt; </p>
<p> Runlevels <code>0</code>, <code>1</code> and <code>6</code> are reserved. Runlevel <code>0</code> is used to halt the system and <code>6</code> to reboot the system. Runlevel <code>1</code> is used to bring the system back down into single-user mode, after which the runlevel will be <code>S</code>.</p>
<h3>System V initialisation in Upstart</h3>
<p>The compatible implementation of runlevels permits Upstart jobs to be run on the <code>runlevel</code> event that perform the same functionality as the original System V <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon. </p>
<p> The <i>/etc/init/rc.conf</i> job is run on the <code>runlevel</code> event, thus receiving the <code>RUNLEVEL</code> and <code>PREVLEVEL</code> environment variables. Its sole job is to execute the <code>/etc/init.d/rc</code> script, passing the new runlevel as an argument. </p>
<p> Initial system startup is provided by the <i>/etc/init/rc-sysinit.conf</i> job. This is run on the <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7) event, and is primarily responsible for running the <code>/etc/init.d/rc</code> script with the special <code>S</code> argument and calling <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) to switch into the default runlevel when done. This also handles the <code>-b</code>, <code>emergency</code>, <code>-s</code> and <code>single</code> kernel command-line options as well as specifying an alternate runlevel on the kernel command-line. </p>
<p> Finally the <i>/etc/init/rcS.conf</i> job handles the special case of entering the single-user runlevel and providing a login shell. Once that shell terminates, this restarts the <i>rc-sysinit</i> job to re-enter the default runlevel.</p>
<h3>Implementation of runlevels in Upstart</h3>
<p>The Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon has no native concepts of runlevel, and unlike the System V daemon, makes no attempt to keep track of the current runlevel. </p>
<p> Instead a compatible implementation is provided by the <code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8), <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) and <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) tools supplied with Upstart. </p>
<p> The <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) and <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) tools are used by system administrators to change the runlevel, thus they both generate this <code>runlevel</code> event obtaining the value for the <code>PREVLEVEL</code> environment variable from their own environment (the <code>RUNLEVEL</code> variable) or the <i>/var/run/utmp</i> file. </p>
<p> Additionally they update the <i>/var/run/utmp</i> file with the new runlevel, and append a log entry to the <i>/var/log/wtmp</i> file. </p>
<p> The <code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8) tool may be used by system administrators to obtain the current runlevel, this reads the <code>RUNLEVEL</code> and <code>PREVLEVEL</code> variables from its own environment or reads the current and previous runlevel from <i>/var/run/utmp</i>. </p>
<p> The <code><a href="/docs/linux/man/1-who/">who</a></code>(1) <code>-r</code> command may also be used to read the current runlevel from <i>/var/run/utmp</i>. </p>
<p> This provides full compatibility with System V. </p>
<p> During the boot scripts, where the <i>/var/run/utmp</i> file may not yet be writable, the <code>RUNLEVEL</code> and <code>PREVLEVEL</code> environment variables will be available so <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) will still provide the correct values. </p>
<p> Once the boot scripts have finished, while the environment variables may no longer be available, the <i>/var/run/utmp</i> file will be and the most recent <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) invocation should have successfully written to it.</p>
<h3>Boot time records</h3>
<p>The <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) tool also takes care of writing the boot time record to both <i>/var/run/utmp</i> and <i>/var/log/wtmp</i>. </p>
<p> This is written if the previous runlevel in these files does not match the previous runlevel obtained from its environment. In general this occurs when switching from runlevel <code>S</code> to the default runlevel, at which point the <i>/var/run/utmp</i> and <i>/var/log/wtmp</i> files are both writable, and the <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) invocation to do the switch has <code>RUNLEVEL</code>=<i>S</i> in its environment.</p>
<h2>Example</h2>
<p>A service running in the typical multi-user runlevels might use: </p>
<dl>
<dd>
<pre>start on runlevel [2345]
stop on runlevel [!2345]</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runlevel/">runlevel</a></code>(8) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) <code><a href="/docs/linux/man/1-who/">who</a></code>(1) </p>
