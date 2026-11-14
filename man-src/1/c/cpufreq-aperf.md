---
title: "cpufreq-aperf(1)"
name: "cpufreq-aperf"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpufreq-aperf/"
description: "cpufreq-aperf – Calculates the average frequency over a time period"
---

<h2 class="name">NAME</h2>
<p> cpufreq-aperf &#8211; Calculates the average frequency over a time period </p>
<h2>SYNTAX</h2>
<p> cpufreq-aperf [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> On latest processors exist two MSR registers refered to as:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; MPERF increasing with maxium&nbsp;<wbr>(P0)&nbsp;<wbr>frequency in C0<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; APERF increasing with current/actual frequency in C0 </p>
<p> From this information the average frequency over a time period can be calculated and this is what this tool does. </p>
<p> A nice falloff feature beside the average frequency is the time a processor core remained in C0 (working state) or any CX (sleep state) processor sleep state during the measured time period. This information can be determined from the fact that MPERF only increases in C0 state.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <code>&#8211;cpu</code> &lt;<i>CPU</i>&gt;</p>
<dd>
&nbsp;<wbr>The&nbsp;<wbr>&lt;<i>CPU</i>&gt;&nbsp;<wbr>core to measure &#8211; default all cores.</p>
<dt><code>-i</code> <code>&#8211;interval</code> &lt;<i>seconds</i>&gt;</p>
<dd> Refresh rate &#8211; default 1 second.</p>
<dt><code>-o</code> <code>&#8211;once</code></p>
<dd> Exit after one interval.</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Prints the available options.</dl>
<h2>REMARKS</h2>
<p> The msr driver must be loaded for this command to work.</p>
<h2>AUTHORS</h2>
<pre>
Thomas Renninger &lt;trenn [at] suse.de&gt;
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpufreq-set/">cpufreq-set</a>(1), <a href="/docs/linux/man/1-cpufreq-info/">cpufreq-info</a>(1) </p>
<h2>Index</h2>
