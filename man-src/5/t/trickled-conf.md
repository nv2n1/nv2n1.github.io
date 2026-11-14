---
title: "trickled-conf(5)"
name: "trickled-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-trickled-conf/"
description: "trickled.conf – format of the configuration file used by trickled(8)."
---

<p><code>trickled.conf</code> &#8211; format of the configuration file used by <a href="/docs/linux/man/8-trickled/">trickled</a>(8).</p>
<h2>Description</h2>
<p>The configuration file format is quite simple. Sections are delimited by square brackets:</p>
<dl>
<dd>[Section]</dl>
<p> And options within brackets sections are simple key value pairs:</p>
<dl>
<dd>Option = Value</dl>
<h2>Options</h2>
<p>Per-application customizable variables are specified within sections with section names matching the application name. The options are:</p>
<dl>
<dt><code>Priority</code></p>
<dd>Sets the priority of the application, see <a href="/docs/linux/man/8-trickled/">trickled</a>(8) for details.</p>
<dt><code>Time-Smoothing</code></p>
<dd>Sets the time smoothing parameter of the application, see <a href="/docs/linux/man/8-trickled/">trickled</a>(8) for an details.</p>
<dt><code>Length-Smoothing</code></p>
<dd>Sets the length smoothing parameter of the application, see <a href="/docs/linux/man/8-trickled/">trickled</a>(8) for details.</dl>
</dl>
<h2>Examples</h2>
<pre>[ssh]
Priority = 1
Time-Smoothing = 0.1
Length-Smoothing = 2
[ftp]
Priority = 8
Time-Smoothing = 5
Length-Smoothing = 20</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-trickle/">trickle</a>(1), <a href="/docs/linux/man/3-syslog/">syslog</a>(3), <a href="/docs/linux/man/4-netintro/">netintro</a>(4)</p>
<h2>Authors</h2>
<p>has been developed by Marius Aamodt Eriksen Aq marius [at] monkey.org .</p>
