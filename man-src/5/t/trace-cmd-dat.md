---
title: "trace-cmd-dat(5)"
name: "trace-cmd-dat"
section: "5"
letter: "t"
url: "/docs/linux/man/5-trace-cmd-dat/"
description: "trace-cmd.dat – trace-cmd file format"
---

<p>trace-cmd.dat &#8211; trace-cmd file format</p>
<h2>Description</h2>
<p>The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) utility produces a &quot;trace.dat&quot; file. The file may also be named anything depending if the user specifies a different output name, but it must have a certain binary format. The file is used by trace-cmd to save kernel traces into it and be able to extract the trace from it at a later point (see <code><a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1)</code>).</p>
<h2>Initial Format</h2>
<dl>
<dd>
<pre>The first three bytes contain the magic value:</pre>
</dl>
<dl>
<dd>
<pre>0x17 0x08 0x44</pre>
</dl>
<dl>
<dd>
<pre>The next 7 bytes contain the characters:</pre>
</dl>
<dl>
<dd>
<pre>&quot;tracing&quot;</pre>
</dl>
<dl>
<dd>
<pre>The next set of characters contain a null '
