---
title: "cpufreq-info(1)"
name: "cpufreq-info"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpufreq-info/"
description: "cpufreq-info – Utility to retrieve cpufreq kernel information"
---

<h2 class="name">NAME</h2>
<p> cpufreq-info &#8211; Utility to retrieve cpufreq kernel information </p>
<h2>SYNTAX</h2>
<p> cpufreq-info [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> A small tool which prints out cpufreq information helpful to developers and interested users.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <code>&#8211;cpu</code> &lt;<i>CPU</i>&gt;</dt>
<dd>
&nbsp;<wbr>&lt;<i>CPU</i>&gt;&nbsp;<wbr>number which information shall be determined about.</dd>
<dt><code>-e</code> <code>&#8211;debug</code></dt>
<dd> Prints out debug information.</dd>
<dt><code>-f</code> <code>&#8211;freq</code></dt>
<dd> Get frequency the CPU currently runs at, according to the cpufreq core.</dd>
<dt><code>-w</code> <code>&#8211;hwfreq</code></dt>
<dd> Get frequency the CPU currently runs at, by reading it from hardware (only available to root).</dd>
<dt><code>-l</code> <code>&#8211;hwlimits</code></dt>
<dd> Determine the minimum and maximum CPU frequency allowed.</dd>
<dt><code>-d</code> <code>&#8211;driver</code></dt>
<dd> Determines the used cpufreq kernel driver.</dd>
<dt><code>-p</code> <code>&#8211;policy</code></dt>
<dd> Gets the currently used cpufreq policy.</dd>
<dt><code>-g</code> <code>&#8211;governors</code></dt>
<dd> Determines available cpufreq governors.</dd>
<dt><code>-a</code> <code>&#8211;related-cpus</code></dt>
<dd> Determines which CPUs run at the same hardware frequency.</dd>
<dt><code>-a</code> <code>&#8211;affected-cpus</code></dt>
<dd> Determines which CPUs need to have their frequency coordinated by software.</dd>
<dt><code>-s</code> <code>&#8211;stats</code></dt>
<dd> Shows cpufreq statistics if available.</dd>
<dt><code>-y</code> <code>&#8211;latency</code></dt>
<dd> Determines the maximum latency on CPU frequency changes.</dd>
<dt><code>-o</code> <code>&#8211;proc</code></dt>
<dd> Prints out information like provided by the /proc/cpufreq interface in 2.4. and early 2.6. kernels.</dd>
<dt><code>-m</code> <code>&#8211;human</code></dt>
<dd> human-readable output for the -f, -w, -s and -y parameters.</dd>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> Prints out the help screen.</dd></dl>
<h2>REMARKS</h2>
<p> You can&#8217;t specify more than one of the output specific options -o -e -a -g -p -d -l -w -f -y. </p>
<p> You also can&#8217;t specify the -o option combined with the -c option.</p>
<h2>FILES</h2>
<pre>
<i>/sys/devices/system/cpu/cpu*/cpufreq/</i>  
<i>/proc/cpufreq</i> (deprecated) 
<i>/proc/sys/cpu/</i> (deprecated)
</pre>
<h2>AUTHORS</h2>
<pre><code>
Dominik Brodowski&lt;linux[at] brodo.de&gt; - author Mattia Dongili&lt;malattia[at] gmail.com&gt; - first autolibtoolization
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpufreq-set/">cpufreq-set</a>(1), <a href="/docs/linux/man/1-cpufreq-aperf/">cpufreq-aperf</a>(1) </p>
