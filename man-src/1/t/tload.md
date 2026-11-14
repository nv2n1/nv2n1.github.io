---
title: "tload(1)"
name: "tload"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tload/"
description: "tload – graphic representation of system load average"
---

<h2 class="name">NAME</h2>
<p> tload &#8211; graphic representation of system load average </p>
<h2>SYNOPSIS</h2>
<p> <code>tload</code> [<i>options</i>] [<i>tty</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>tload</code> prints a graph of the current system load average to the specified <i>tty</i> (or the tty of the <code>tload</code> process if none is specified).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;scale</code> <i>number</i></p>
<dd> The scale option allows a vertical scale to be specified for the display (in characters between graph ticks); thus, a smaller value represents a larger scale, and vice versa.</p>
<dt><code>-d</code>, <code>&#8211;delay</code> <i>seconds</i></p>
<dd> The delay sets the delay between graph updates in <i>seconds</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display this help text.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>FILES</h2>
<p> <i>/proc/loadavg</i> load average information</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/1-w/">w</a></code>(1)</p>
<h2>BUGS</h2>
<p> The <code>-d</code><i> delay</i> option sets the time argument for an <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2); if -d 0 is specified, the alarm is set to 0, which will never send the <code>SIGALRM</code> and update the display.</p>
<h2>AUTHORS</h2>
<p> Branko Lankester, David Engel Michael K. Johnson</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
