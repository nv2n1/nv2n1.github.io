---
title: "cpupower(1)"
name: "cpupower"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower/"
description: "cpupower – Shows and sets processor power related values"
---

<h2>NAME</h2>
<p> cpupower &#8211; Shows and sets processor power related values</p>
<h2>SYNOPSIS</h2>
<p> <code> cpupower [ -c cpulist ] &lt;command&gt; [ARGS]</code> </p>
<p> <code>cpupower -v|&#8211;version</code> </p>
<p> <code>cpupower -h|&#8211;help</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>cpupower </code> is a collection of tools to examine and tune power saving related features of your processor. </p>
<p> The manpages of the commands (cpupower-&lt;command&gt;(1)) provide detailed descriptions of supported features. Run <code>cpupower help</code> to get an overview of supported commands. </p>
<h2>Options</h2>
<p> &#8211;help, -h</p>
<dl>
<dt>
<dd> Shows supported commands and general usage.</dl>
<p> &#8211;cpu cpulist, -c cpulist</p>
<dl>
<dt>
<dd> Only show or set values for specific cores. This option is not supported by all commands, details can be found in the manpages of the commands. </p>
<p> Some commands access all cores (typically the *-set commands), some only the first core (typically the *-info commands) by default. </p>
<p> The syntax for &lt;cpulist&gt; is based on how the kernel exports CPU bitmasks via sysfs files. Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Input</p>
<dd> Equivalent to</p>
<dt>all</p>
<dd> all cores</p>
<dt>0-3</p>
<dd> 0,1,2,3</p>
<dt>0-7:2</p>
<dd> 0,2,4,6</p>
<dt>1,3,5-7</p>
<dd> 1,3,5,6,7</p>
<dt>0-3:2,8-15:4</p>
<dd> 0,2,8,12<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
</dl>
</dl>
</dl>
<p> &#8211;version, -v</p>
<dl>
<dt>
<dd> Print the package name and version number. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpupower-set/">cpupower-set</a>(1), <a href="/docs/linux/man/1-cpupower-info/">cpupower-info</a>(1), <a href="/docs/linux/man/1-cpupower-idle/">cpupower-idle</a>(1), <a href="/docs/linux/man/1-cpupower-frequency-set/">cpupower-frequency-set</a>(1), <a href="/docs/linux/man/1-cpupower-frequency-info/">cpupower-frequency-info</a>(1), <a href="/docs/linux/man/1-cpupower-monitor/">cpupower-monitor</a>(1), <a href="/docs/linux/man/1-powertop/">powertop</a>(1) </p>
<h2>AUTHORS</h2>
<pre><code>
--perf - bias parts written by Len Brown&lt;len.brown[at] intel.com&gt;
             Thomas Renninger&lt;trenn[at] suse.de&gt;
</code></pre>
<h2>Index</h2>
