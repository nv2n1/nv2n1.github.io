---
title: "freecolor(1)"
name: "freecolor"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freecolor/"
description: "freecolor – Display amount of free and used memory graphically"
---

<h2>NAME</h2>
<p> freecolor &#8211; Display amount of free and used memory graphically</p>
<h2>SYNOPSIS</h2>
<p> <code>freecolor</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>freecolor</code> displays the total amount of free and used physical and swap memory in the system as a colored bargraph on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Display the amount of memory in bytes.</p>
<dt><code>-k</code></p>
<dd> Display the amount of memory in kilobytes. This is the default.</p>
<dt><code>-m</code></p>
<dd> Display the amount of memory in megabytes.</p>
<dt><code>-o</code></p>
<dd> Display the output in old format, the only difference being this option will disable the display of the &quot;buffer adjusted&quot; line.</p>
<dt><code>-s</code></p>
<dd> Continuously display the result delay <i>seconds</i> apart. You may actually specify any floating point number for <i>delay</i>, <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3) is used for microsecond resolution delay times.</p>
<dt><code>-t</code></p>
<dd> Display a line showing the column totals.</p>
<dt><code>-V</code></p>
<dd> Display version information.</dl>
<h2>FILES</h2>
<dl>
<dt>/proc/meminfo</p>
<dd> memory information</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-slabtop/">slabtop</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8).</p>
<h2>AUTHORS</h2>
<p> Written by Roy Keene.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
