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
<dt><code>-c</code> <code>&#8211;cpu</code> &lt;<i>CPU</i>&gt;</p>
<dd>
&nbsp;<wbr>&lt;<i>CPU</i>&gt;&nbsp;<wbr>number which information shall be determined about.</p>
<dt><code>-e</code> <code>&#8211;debug</code></p>
<dd> Prints out debug information.</p>
<dt><code>-f</code> <code>&#8211;freq</code></p>
<dd> Get frequency the CPU currently runs at, according to the cpufreq core.</p>
<dt><code>-w</code> <code>&#8211;hwfreq</code></p>
<dd> Get frequency the CPU currently runs at, by reading it from hardware (only available to root).</p>
<dt><code>-l</code> <code>&#8211;hwlimits</code></p>
<dd> Determine the minimum and maximum CPU frequency allowed.</p>
<dt><code>-d</code> <code>&#8211;driver</code></p>
<dd> Determines the used cpufreq kernel driver.</p>
<dt><code>-p</code> <code>&#8211;policy</code></p>
<dd> Gets the currently used cpufreq policy.</p>
<dt><code>-g</code> <code>&#8211;governors</code></p>
<dd> Determines available cpufreq governors.</p>
<dt><code>-a</code> <code>&#8211;related-cpus</code></p>
<dd> Determines which CPUs run at the same hardware frequency.</p>
<dt><code>-a</code> <code>&#8211;affected-cpus</code></p>
<dd> Determines which CPUs need to have their frequency coordinated by software.</p>
<dt><code>-s</code> <code>&#8211;stats</code></p>
<dd> Shows cpufreq statistics if available.</p>
<dt><code>-y</code> <code>&#8211;latency</code></p>
<dd> Determines the maximum latency on CPU frequency changes.</p>
<dt><code>-o</code> <code>&#8211;proc</code></p>
<dd> Prints out information like provided by the /proc/cpufreq interface in 2.4. and early 2.6. kernels.</p>
<dt><code>-m</code> <code>&#8211;human</code></p>
<dd> human-readable output for the -f, -w, -s and -y parameters.</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Prints out the help screen.</dl>
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
<h2>Index</h2>
