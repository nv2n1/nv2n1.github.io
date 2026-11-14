---
title: "saidar(1)"
name: "saidar"
section: "1"
letter: "s"
url: "/docs/linux/man/1-saidar/"
description: "saidar – a curses-based tool for viewing system statistics"
---

<h2>NAME</h2>
<p> saidar &#8211; a curses-based tool for viewing system statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>saidar</code> [-d <i>delay</i>] [-c] [-v] [-h]</p>
<h2>DESCRIPTION</h2>
<p> <code>saidar</code> is a curses-based tool for viewing the system statistics available through libstatgrab. Statistics include CPU, processes, load, memory, swap, network I/O, disk I/O, and file system information.</p>
<h2>OPTIONS</h2>
<p> The following options are supported.</p>
<dl>
<dt><code>-d</code> <i>DELAY</i></p>
<dd> Wait DELAY seconds between updates (default 3)</p>
<dt><code>-c</code></p>
<dd> Enables coloured output</p>
<dt><code>-v</code></p>
<dd> Prints the version number</p>
<dt><code>-h</code></p>
<dd> Display help and exits</dl>
<h2>COLOURED OUTPUT</h2>
<p> When the <code>-c</code> option is used saidar uses colours to display the data. Each area has a different colour to distinguish it from the nearby fields. Bold and reverse video effects are used to emphasis fields where necessary. </p>
<p> The load average figures are displayed in bold when they&#8217;re notably (greater that 1) different to each other. This purely shows that a change in the load is occurring. </p>
<p> When CPU usage goes over 60% it will be displayed in bold. At 90% the field is displayed using reverse video. Likewise for memory, swap and disk usage at 75% and 90%. Zombie processes are also highlighted. </p>
<p> Other values (paging, disk I/O and network I/O) are not highlighted due to the nature of the values; it&#8217;s not easy to determine what thresholds are significant.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-statgrab/">statgrab</a></code>(1) <code><a href="/docs/linux/man/3-statgrab/">statgrab</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> This man page was derived from the man page written by Bartosz Fenski for the Debian GNU/Linux distribution.</p>
<h2>WEBSITE</h2>
<p> &lt;<a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a>&gt; </p>
<h2>Index</h2>
