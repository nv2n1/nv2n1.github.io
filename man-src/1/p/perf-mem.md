---
title: "perf-mem(1)"
name: "perf-mem"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-mem/"
description: "perf-mem – Profile memory accesses"
---

<h2 class="name">NAME</h2>
<p> perf-mem &#8211; Profile memory accesses </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf mem[&lt;options&gt;](record[&lt;command&gt;] | report)
</code></pre>
<h2>DESCRIPTION</h2>
<p> &quot;perf mem -t &lt;TYPE&gt; record&quot; runs a command and gathers memory operation data from it, into perf.data. Perf record options are accepted and are passed through. </p>
<p> &quot;perf mem -t &lt;TYPE&gt; report&quot; displays the result. It invokes perf report with the right set of options to display a memory access profile. </p>
<p> Note that on Intel systems the memory latency reported is the use-latency, not the pure load (or store latency). Use latency includes any pipeline queueing delays in addition to the memory subsystem latency.</p>
<h2>OPTIONS</h2>
<p> &lt;command&gt;&#8230;</p>
<dl>
<dt>
<dd> Any command you can specify in a shell.</dl>
<p> -t, &#8211;type=</p>
<dl>
<dt>
<dd> Select the memory operation type: load or store (default: load)</dl>
<p> -D, &#8211;dump-raw-samples=</p>
<dl>
<dt>
<dd> Dump the raw decoded samples on the screen in a format that is easy to parse with one sample per line.</dl>
<p> -x, &#8211;field-separator</p>
<dl>
<dt>
<dd> Specify the field separator used when dump raw samples (-D option). By default, The separator is the space character.</dl>
<p> -C, &#8211;cpu-list</p>
<dl>
<dt>
<dd> Restrict dump of raw samples to those provided via this option. Note that the same option can be passed in record mode. It will be interpreted the same way as perf record.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
