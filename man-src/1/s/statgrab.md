---
title: "statgrab(1)"
name: "statgrab"
section: "1"
letter: "s"
url: "/docs/linux/man/1-statgrab/"
description: "statgrab – sysctl-style interface to system statistics"
---

<h2>NAME</h2>
<p> statgrab &#8211; sysctl-style interface to system statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>statgrab</code> [OPTION]&#8230; [STAT]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>statgrab</code> provides a sysctl-style interface to all the system statistics available through libstatgrab. This is useful for applications that don&#8217;t want to make library calls, but still want to access the statistics. </p>
<p> An example of such an application is mrtg, for which scripts are provided to generate configuration files.</p>
<h2>OPTIONS</h2>
<p> The following options are supported.</p>
<dl>
<dt><code>-l</code></p>
<dd> Linux sysctl-style output (default)</p>
<dt><code>-b</code></p>
<dd> BSD sysctl-style output</p>
<dt><code>-m</code></p>
<dd> MRTG-compatible output</p>
<dt><code>-u</code></p>
<dd> Plain output (only show values)</p>
<dt><code>-n</code></p>
<dd> Display cumulative stats once (default)</p>
<dt><code>-s</code></p>
<dd> Display stat differences repeatedly</p>
<dt><code>-o</code></p>
<dd> Display stat differences once</p>
<dt><code>-t</code> <i>DELAY</i></p>
<dd> When repeating, wait DELAY seconds between updates (default 1)</p>
<dt><code>-p</code></p>
<dd> Display CPU usage differences as percentages rather than absolute values</p>
<dt><code>-f</code> <i>FACTOR</i></p>
<dd> Display floating-point values as integers scaled by FACTOR</p>
<dt><code>-K</code></p>
<dd> Display byte counts in kibibytes</p>
<dt><code>-M</code></p>
<dd> Display byte counts in mebibytes</p>
<dt><code>-G</code></p>
<dd> Display byte counts in gibibytes</dl>
<p> If no <code>STAT</code> options are given, all will be displayed. Specify &#8216;STAT.&#8217; to display all statistics starting with that prefix.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-statgrab-make-mrtg-config/">statgrab-make-mrtg-config</a></code>(1) <code><a href="/docs/linux/man/1-statgrab-make-mrtg-index/">statgrab-make-mrtg-index</a></code>(1) <code><a href="/docs/linux/man/1-saidar/">saidar</a></code>(1) <code><a href="/docs/linux/man/3-statgrab/">statgrab</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> This man page was derived from the man page written by Bartosz Fenski for the Debian GNU/Linux distribution.</p>
<h2>WEBSITE</h2>
<p> &lt;<a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a>&gt; </p>
<h2>Index</h2>
