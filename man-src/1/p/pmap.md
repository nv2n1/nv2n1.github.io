---
title: "pmap(1)"
name: "pmap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmap/"
description: "pmap – report memory map of a process"
---

<h2 class="name">NAME</h2>
<p> pmap &#8211; report memory map of a process </p>
<h2>SYNOPSIS</h2>
<p> <code>pmap</code> [<i>options</i>] <i>pid</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmap</code> command reports the memory map of a process or processes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code>, <code>&#8211;extended</code></p>
<dd> Show the extended format.</p>
<dt><code>-d</code>, <code>&#8211;device</code></p>
<dd> Show the device format.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not display some header or footer lines.</p>
<dt><code>-A</code>, <code>&#8211;range</code> <i>low</i>,<i>high</i></p>
<dd> Limit results to the given range to <i>low</i> and <i>high</i> address range. Notice that the low and high arguments are single string separated with comma.</p>
<dt><code>-X</code></p>
<dd> Show even more details than the <code>-x</code> option. WARNING: format changes according to <i>/proc/PID/smaps</i></p>
<dt><code>-XX</code></p>
<dd> Show everything the kernel provides</p>
<dt><code>-p</code>, <code>&#8211;show-path</code></p>
<dd> Show full path to files in the mapping column</p>
<dt><code>-c</code>, <code>&#8211;read-rc</code></p>
<dd> Read the default configuration</p>
<dt><code>-C</code>, <code>&#8211;read-rc-from</code> <i>file</i></p>
<dd> Read the configuration from <i>file</i></p>
<dt><code>-n</code>, <code>&#8211;create-rc</code></p>
<dd> Create new default configuration</p>
<dt><code>-N</code>, <code>&#8211;create-rc-to</code> <i>file</i></p>
<dd> Create new configuration to <i>file</i></p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Success.</p>
<dt><code>1</code></p>
<dd> Failure.</p>
<dt><code>42</code></p>
<dd> Did not find all processes asked for.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-pgrep/">pgrep</a></code>(1)</p>
<h2>STANDARDS</h2>
<p> No standards apply, but <code>pmap</code> looks an awful lot like a SunOS command.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
