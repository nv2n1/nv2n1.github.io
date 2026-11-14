---
title: "perf-kmem(1)"
name: "perf-kmem"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-kmem/"
description: "perf-kmem – Tool to trace/measure kernel memory(slab) properties"
---

<h2 class="name">NAME</h2>
<p> perf-kmem &#8211; Tool to trace/measure kernel memory(slab) properties </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf kmem{record | stat}[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> There are two variants of perf kmem: </p>
<dl>
<dt>
<dd>
<pre>
'perf kmem record &lt;command&gt;' to record the kmem events
of an arbitrary workload.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'perf kmem stat' to report kernel memory statistics.
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -i &lt;file&gt;, &#8211;input=&lt;file&gt;</p>
<dl>
<dt>
<dd> Select the input file (default: perf.data unless stdin is a fifo)</dl>
<p> &#8211;caller</p>
<dl>
<dt>
<dd> Show per-callsite statistics</dl>
<p> &#8211;alloc</p>
<dl>
<dt>
<dd> Show per-allocation statistics</dl>
<p> -s &lt;key[,key2&#8230;]&gt;, &#8211;sort=&lt;key[,key2&#8230;]&gt;</p>
<dl>
<dt>
<dd> Sort the output (default: frag,hit,bytes)</dl>
<p> -l &lt;num&gt;, &#8211;line=&lt;num&gt;</p>
<dl>
<dt>
<dd> Print n lines only</dl>
<p> &#8211;raw-ip</p>
<dl>
<dt>
<dd> Print raw ip instead of symbol</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1) </p>
<h2>Index</h2>
