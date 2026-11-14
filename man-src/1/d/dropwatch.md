---
title: "dropwatch(1)"
name: "dropwatch"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dropwatch/"
description: "dropwatch – kernel dropped packet monitoring utility"
---

<h2>NAME</h2>
<p> dropwatch &#8211; kernel dropped packet monitoring utility</p>
<h2>SYNOPSIS</h2>
<p> <code>dropwatch [-l &lt;method&gt; | list]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>dropwatch </i> dropwatch is an interactive utility for monitoring and recording packets that are dropped by the kernel</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l &lt;method&gt; | list</code></p>
<dd> Select the translation method to use when a drop alert arrives. By default the raw instruction pointer of a drop location is output, but by the use of the -l option, we can assign a translation method so that the instruction pointer can be translated into function names. Currently supported lookup methods are:</dl>
<p> <code>kas &#8211; use /proc/kallsyms to lookup instruction pointers to function mappings</code></p>
<h2>INTERACTIVE COMMANDS</h2>
<dl>
<dt><code>start </code></p>
<dd> Tells the kernel to start reporting dropped packets</p>
<dt><code>stop </code></p>
<dd> Tells the kernel to discontinue reporting dropped packets</p>
<dt><code>exit </code></p>
<dd> Exits the dropmonitor program</p>
<dt><code>help </code></p>
<dd> Displays summary of all commands</p>
<dt><code>set alertlimit &lt;value&gt;</code></p>
<dd> Sets a triggerpoint to stop monitoring for dropped packets after &lt;value&gt; alerts have been received </p>
</dl>
<h2>Index</h2>
