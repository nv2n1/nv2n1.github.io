---
title: "ethstatus(1)"
name: "ethstatus"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ethstatus/"
description: "ethstatus – Console-based ethernet statistics monitor"
---

<h2 class="name">NAME</h2>
<p> ethstatus &#8211; Console-based ethernet statistics monitor </p>
<h2>SYNOPSIS</h2>
<p> <code>ethstatus</code> [ -h ] [ -i interface ] [ -v videomode ] [ -S bps[k|m|g] ] [ -s speed ] (backward compatibility)</p>
<h2>DESCRIPTION</h2>
<p> <code>ethstatus</code> is a console-based monitoring utility for displaying statistical data of the ethernet interface on a quantity basis.</p>
<h2>OPTIONS</h2>
<p> The following options can be provided:</p>
<dl>
<dt><code>-i</code></p>
<dd> Specify the ethernet interface which shall be monitored. Default is &#8216;eth0&#8217;.</p>
<dt><code>-v</code></p>
<dd> Set the video mode used by curses. Possible choices are &#8216;vga&#8217; (the default) and &#8216;mono&#8217; (useful for black-and-white monitors).</p>
<dt><code>-S</code></p>
<dd> Set the maximum network speed in bits per second. ethstatus knows about the kilo (k), mega (m) and giga (g) modifiers. So you can specify the speed as e.g. 64k or 100m or 1g.</p>
<dt><code>-s</code></p>
<dd> Set the maximum network speed. Possible values are &#8217;10&#8217; (=10 Mbps), &#8216;100&#8217; (=100 Mbps), &#8217;64&#8217; (=64 kbps), &#8216;128&#8217; (=128 kbps), 256 (=256 kbps), &#8216;768&#8217; (=768 kbps) or &#8216;1540&#8217; (=1540 kbps). This option is provided for backward compatibility to prior versions of ethstatus. Please use the -S parameter instead.</p>
<dt></dl>
<h2>AUTHORS</h2>
<dd> The original program was written by Gabriel Montenegro &lt;johnpetrucci [at] users.sourceforge.net&gt;. Bug fixes, code cleanup, different improvements and this manual page were provided by Christoph Haas &lt;email [at] christoph-haas.de&gt; for the Debian GNU/Linux system. </p>
<h2>Index</h2>
