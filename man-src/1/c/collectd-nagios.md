---
title: "collectd-nagios(1)"
name: "collectd-nagios"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectd-nagios/"
description: "collectd-nagios – Nagios plugin for querying collectd"
---

<h2 class="name">NAME</h2>
<p> collectd-nagios &#8211; Nagios plugin for querying collectd </p>
<h2>SYNOPSIS</h2>
<p> collectd-nagios <code>-s</code> <i>socket</i> <code>-n</code> <i>value_spec</i> <code>-H</code> <i>hostname</i> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This small program is the glue between collectd and nagios. collectd collects various performance statistics which it provides via the <tt>&quot;unixsock plugin&quot;</tt>, see <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5). This program is called by Nagios, connects to the <font SIZE="-1">UNIX</font> socket and reads the values from collectd. It then returns <font SIZE="-1"><code>OKAY</code></font>, <font SIZE="-1"><code>WARNING</code></font> or <font SIZE="-1"><code>CRITICAL</code></font> depending on the values and the ranges provided by Nagios.</p>
<h2>ARGUMENTS AND OPTIONS</h2>
<p> The following arguments and options are required and understood by collectd-nagios. The order of the arguments generally doesn&#8217;t matter, as long as no argument is passed more than once.</p>
<dl>
<dt><code>-s</code> <i>socket</i></p>
<dd> Path of the <font SIZE="-1">UNIX</font> socket opened by collectd&#8217;s <tt>&quot;unixsock plugin&quot;</tt>.</p>
<dt><code>-n</code> <i>value_spec</i></p>
<dd> The value to read from collectd. The argument is in the form <tt>&quot;plugin[-instance]/type[-instance]&quot;</tt>.</p>
<dt><code>-H</code> <i>hostname</i></p>
<dd> Hostname to query the values for.</p>
<dt><code>-d</code> <i>data_source</i></p>
<dd> Each <i>value_spec</i> may be made of multiple &#8220;data sources&#8221;. With this option you can select one or more data sources. To select multiple data sources simply specify this option again. If multiple data sources are examined they are handled according to the consolidation function given with the <code>-g</code> option.</p>
<dt><code>-g</code> <code>none</code><i>|</i><code>average</code><i>|</i><code>sum</code></p>
<dd> When multiple data sources are selected from a value spec, they can be handled differently depending on this option. The values of the following meaning:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> No consolidation if done and the warning and critical regions are applied to each value independently.</p>
<dt><code>average</code></p>
<dd> The warning and critical ranges are applied to the average of all values.</p>
<dt><code>sum</code></p>
<dd> The warning and critical ranges are applied to the sum of all values.</p>
<dt><code>percentage</code></p>
<dd> The warning and critical ranges are applied to the ratio (in percent) of the first value and the sum of all values. A warning is returned if the first value is not defined or if all values sum up to zero.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-c</code> <i>range</i></p>
<dd>
<dt><code>-w</code> <i>range</i></p>
<dd> Set the critical (<code>-c</code>) and warning (<code>-w</code>) ranges. These options mostly follow the normal syntax of Nagios plugins. The general format is &quot;<i>min</i><code>:</code><i>max</i>&quot;. If a value is smaller than <i>min</i> or bigger than <i>max</i>, a <i>warning</i> or <i>critical</i> status is returned, otherwise the status is <i>success</i>. </p>
<p> The tilde sign (<code>~</code>) can be used to explicitly specify infinity. If <code>~</code> is used as a <i>min</i> value, negative infinity is used. In case of <i>max</i>, it is interpreted as positive infinity. </p>
<p> If the first character of the <i>range</i> is the at sign (<code>@</code>), the meaning of the range will be inverted. I. e. all values <i>within</i> the range will yield a <i>warning</i> or <i>critical</i> status, while all values <i>outside</i> the range will result in a <i>success</i> status. </p>
<p> <i>min</i> (and the colon) may be omitted, <i>min</i> is then assumed to be zero. If <i>max</i> (but not the trailing colon) is omitted, <i>max</i> is assumed to be positive infinity.</p>
<dt><code>-m</code></p>
<dd> If this option is given, &#8220;Not a Number&#8221; (NaN) is treated as <i>critical</i>. By default, the <i>none</i> consolidation reports NaNs as <i>warning</i>. Other consolidations simply ignore NaN values.</dl>
<h2>RETURN VALUE</h2>
<p> As usual for Nagios plugins, this program writes a short, one line status message to <font SIZE="-1">STDOUT</font> and signals success or failure with it&#8217;s return value. It exits with a return value of <code>0</code> for <i>success</i>, <code>1</code> for <i>warning</i> and <code>2</code> for <i>critical</i>. If the values are not available or some other error occurred, it returns <code>3</code> for <i>unknown</i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5), &lt;<a rel="nofollow" href="http://nagios.org/">http://nagios.org/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Florian Forster &lt;octo at collectd.org&gt; </p>
<h2>Index</h2>
