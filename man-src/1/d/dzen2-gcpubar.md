---
title: "dzen2-gcpubar(1)"
name: "dzen2-gcpubar"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dzen2-gcpubar/"
description: "dzen2-gcpubar – graphical CPU usage meter"
---

<h2>NAME</h2>
<p> dzen2-gcpubar &#8211; graphical CPU usage meter</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dzen2-gcpubar</code> [-i <i>interval</i>] [-c <i>count</i>] [-fg <i>color</i>] [-bg <i>color</i>] [-w <i>pixel</i>] [-h&nbsp;<wbr><i>pixel</i>] [-nonl]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gcpubar</code></p>
<dd>is a CPU utilization meter for Linux. It relies on the existence of the /proc/stat file and generates fully graphical meters viewable with dzen.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-i</code></p>
<dd> Update interval in seconds (default 1). You can use positive values less than 1 for intervals shorter than 1 second.</p>
<dt><code>-c</code></p>
<dd> Terminate after displaying argument to this option (default infinite).</p>
<dt><code>-fg</code></p>
<dd> Foreground color</p>
<dt><code>-bg</code></p>
<dd> Background color</p>
<dt><code>-w</code></p>
<dd> Width in piwels</p>
<dt><code>-h</code></p>
<dd> Height in pixels</p>
<dt><code>-nonl</code></p>
<dd> No new line, don&#8217;t put &#8216; at the end of the bar (default: do print &#8216;)</dl>
<p> gcpubar was written by Robert Manea. </p>
<p> This manual page was written by bertagaz &lt;bertagaz [at] ptitcanardnoir.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
