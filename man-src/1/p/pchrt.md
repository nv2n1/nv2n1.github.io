---
title: "pchrt(1)"
name: "pchrt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pchrt/"
description: "pchrt (python-schedutils) – manipulate the real-time attributes of a process"
---

<h2>NAME</h2>
<p> <code>pchrt (python-schedutils) &#8211; manipulate the real-time attributes of a process</code></p>
<h2>SYNOPSIS</h2>
<p> pchrt [options] [prio] [pid | cmd [args&#8230;]]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b, &#8211;batch</code></p>
<dd> set policy to SCHED_BATCH</p>
<dt><code>-f, &#8211;fifo</code></p>
<dd> set policy to SCHED_FIFO</p>
<dt><code>-i, &#8211;idle</code></p>
<dd> set policy to SCHED_IDLE</p>
<dt><code>-p, &#8211;pid</code></p>
<dd> operate on existing given pid</p>
<dt><code>-m, &#8211;max</code></p>
<dd> show min and max valid priorities</p>
<dt><code>-o, &#8211;other</code></p>
<dd> set policy to SCHED_OTHER</p>
<dt><code>-r, &#8211;rr</code></p>
<dd> set policy to SCHED_RR (default)</p>
<dt><code>-R, &#8211;reset-on-fork</code></p>
<dd> set SCHED_RESET_ON_FORK for FIFO or RR</p>
<dt><code>-h, &#8211;help</code></p>
<dd> display help</p>
<dt><code>Note:</code></p>
<dd> You must give a priority if changing policy.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> pchrt was written by Arnaldo Carvalho de Melo &lt;acme [at] redhat.com&gt;<br />
 as part of python-schedutils </p>
<p> This manual page was written by John Kacur &lt;jkacur [at] redhat.com&gt; </p>
<p> Report bugs and send patches to &lt;tuna-devel [at] lists.fedorahosted.org&gt; </p>
<h2>Index</h2>
