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
<dt><code>-b, &#8211;batch</code></dt>
<dd> set policy to SCHED_BATCH</dd>
<dt><code>-f, &#8211;fifo</code></dt>
<dd> set policy to SCHED_FIFO</dd>
<dt><code>-i, &#8211;idle</code></dt>
<dd> set policy to SCHED_IDLE</dd>
<dt><code>-p, &#8211;pid</code></dt>
<dd> operate on existing given pid</dd>
<dt><code>-m, &#8211;max</code></dt>
<dd> show min and max valid priorities</dd>
<dt><code>-o, &#8211;other</code></dt>
<dd> set policy to SCHED_OTHER</dd>
<dt><code>-r, &#8211;rr</code></dt>
<dd> set policy to SCHED_RR (default)</dd>
<dt><code>-R, &#8211;reset-on-fork</code></dt>
<dd> set SCHED_RESET_ON_FORK for FIFO or RR</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> display help</dd>
<dt><code>Note:</code></dt>
<dd> You must give a priority if changing policy.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> pchrt was written by Arnaldo Carvalho de Melo &lt;acme [at] redhat.com&gt;<br />
 as part of python-schedutils </p>
<p> This manual page was written by John Kacur &lt;jkacur [at] redhat.com&gt; </p>
<p> Report bugs and send patches to &lt;tuna-devel [at] lists.fedorahosted.org&gt; </p>
