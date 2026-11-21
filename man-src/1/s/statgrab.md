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
<p> <code>statgrab</code> [OPTION]&#8230; [STAT]&#8230;</p>
<p> <code>statgrab</code> provides a sysctl-style interface to all the system statistics available through libstatgrab. This is useful for applications that don&#8217;t want to make library calls, but still want to access the statistics. </p>
<p> An example of such an application is mrtg, for which scripts are provided to generate configuration files.</p>
<h2>OPTIONS</h2>
<p> The following options are supported.</p>
<dl>
<dt><code>-l</code></dt>
<dd> Linux sysctl-style output (default)</dd>
<dt><code>-b</code></dt>
<dd> BSD sysctl-style output</dd>
<dt><code>-m</code></dt>
<dd> MRTG-compatible output</dd>
<dt><code>-u</code></dt>
<dd> Plain output (only show values)</dd>
<dt><code>-n</code></dt>
<dd> Display cumulative stats once (default)</dd>
<dt><code>-s</code></dt>
<dd> Display stat differences repeatedly</dd>
<dt><code>-o</code></dt>
<dd> Display stat differences once</dd>
<dt><code>-t</code> <i>DELAY</i></dt>
<dd> When repeating, wait DELAY seconds between updates (default 1)</dd>
<dt><code>-p</code></dt>
<dd> Display CPU usage differences as percentages rather than absolute values</dd>
<dt><code>-f</code> <i>FACTOR</i></dt>
<dd> Display floating-point values as integers scaled by FACTOR</dd>
<dt><code>-K</code></dt>
<dd> Display byte counts in kibibytes</dd>
<dt><code>-M</code></dt>
<dd> Display byte counts in mebibytes</dd>
<dt><code>-G</code></dt>
<dd> Display byte counts in gibibytes</dd></dl>
<p> If no <code>STAT</code> options are given, all will be displayed. Specify &#8216;STAT.&#8217; to display all statistics starting with that prefix.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-statgrab-make-mrtg-config/">statgrab-make-mrtg-config</a></code>(1) <code><a href="/docs/linux/man/1-statgrab-make-mrtg-index/">statgrab-make-mrtg-index</a></code>(1) <code><a href="/docs/linux/man/1-saidar/">saidar</a></code>(1) <code><a href="/docs/linux/man/3-statgrab/">statgrab</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> This man page was derived from the man page written by Bartosz Fenski for the Debian GNU/Linux distribution.</p>
<h2>WEBSITE</h2>
<p> &lt;<a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a>&gt; </p>
