---
title: "cpupower-frequency-set(1)"
name: "cpupower-frequency-set"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower-frequency-set/"
description: "cpupower frequency-set – A small tool which allows to modify cpufreq settings."
---

<h2>NAME</h2>
<p> cpupower frequency-set &#8211; A small tool which allows to modify cpufreq settings.</p>
<h2>SYNTAX</h2>
<p> cpupower [ -c cpu ] frequency-set [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> cpupower frequency-set allows you to modify cpufreq settings without having to type e.g. &quot;/sys/devices/system/cpu/cpu0/cpufreq/scaling_set_speed&quot; all the time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> <code>&#8211;min</code> &lt;FREQ&gt;</p>
<dd> new minimum CPU frequency the governor may select.</p>
<dt><code>-u</code> <code>&#8211;max</code> &lt;FREQ&gt;</p>
<dd> new maximum CPU frequency the governor may select.</p>
<dt><code>-g</code> <code>&#8211;governor</code> &lt;GOV&gt;</p>
<dd> new cpufreq governor.</p>
<dt><code>-f</code> <code>&#8211;freq</code> &lt;FREQ&gt;</p>
<dd> specific frequency to be set. Requires userspace governor to be available and loaded.</p>
<dt><code>-r</code> <code>&#8211;related</code></p>
<dd> modify all hardware-related CPUs at the same time</p>
<dt></dl>
<h2>REMARKS</h2>
<dd>
<p> By default values are applied on all cores. How to modify single core configurations is described in the <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1) manpage in the &#8211;cpu option section. </p>
<p> The -f FREQ, &#8211;freq FREQ parameter cannot be combined with any other parameter. </p>
<p> FREQuencies can be passed in Hz, kHz (default), MHz, GHz, or THz by postfixing the value with the wanted unit name, without any space (frequency in kHz =^ Hz * 0.001 =^ MHz * 1000 =^ GHz * 1000000). </p>
<p> On Linux kernels up to 2.6.29, the -r or &#8211;related parameter is ignored.</p>
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
<p> <a href="/docs/linux/man/1-cpupower-frequency-info/">cpupower-frequency-info</a>(1), <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1) </p>
<h2>Index</h2>
