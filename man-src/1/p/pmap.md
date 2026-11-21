---
title: "pmap(1)"
name: "pmap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmap/"
description: "pmap – report memory map of a process"
---

<h2>SYNOPSIS</h2>
<p> <code>pmap</code> [<i>options</i>] <i>pid</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmap</code> command reports the memory map of a process or processes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code>, <code>&#8211;extended</code></dt>
<dd> Show the extended format.</dd>
<dt><code>-d</code>, <code>&#8211;device</code></dt>
<dd> Show the device format.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Do not display some header or footer lines.</dd>
<dt><code>-A</code>, <code>&#8211;range</code> <i>low</i>,<i>high</i></dt>
<dd> Limit results to the given range to <i>low</i> and <i>high</i> address range. Notice that the low and high arguments are single string separated with comma.</dd>
<dt><code>-X</code></dt>
<dd> Show even more details than the <code>-x</code> option. WARNING: format changes according to <i>/proc/PID/smaps</i></dd>
<dt><code>-XX</code></dt>
<dd> Show everything the kernel provides</dd>
<dt><code>-p</code>, <code>&#8211;show-path</code></dt>
<dd> Show full path to files in the mapping column</dd>
<dt><code>-c</code>, <code>&#8211;read-rc</code></dt>
<dd> Read the default configuration</dd>
<dt><code>-C</code>, <code>&#8211;read-rc-from</code> <i>file</i></dt>
<dd> Read the configuration from <i>file</i></dd>
<dt><code>-n</code>, <code>&#8211;create-rc</code></dt>
<dd> Create new default configuration</dd>
<dt><code>-N</code>, <code>&#8211;create-rc-to</code> <i>file</i></dt>
<dd> Create new configuration to <i>file</i></dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display help text and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information and exit.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> Success.</dd>
<dt><code>1</code></dt>
<dd> Failure.</dd>
<dt><code>42</code></dt>
<dd> Did not find all processes asked for.</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-pgrep/">pgrep</a></code>(1)</p>
<h2>STANDARDS</h2>
<p> No standards apply, but <code>pmap</code> looks an awful lot like a SunOS command.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
