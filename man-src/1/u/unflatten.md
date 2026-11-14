---
title: "unflatten(1)"
name: "unflatten"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unflatten/"
description: "unflatten – adjust directed graphs to improve layout aspect ratio"
---

<h2 class="name">NAME</h2>
<p> unflatten &#8211; adjust directed graphs to improve layout aspect ratio </p>
<h2>SYNOPSIS</h2>
<p> <code>unflatten</code> [<code>-f</code>] [<code>-l</code><i>len</i>] [<code>-c</code><i>len</i> ] [ <code>-o</code> <i>outfile</i> ] [ files ]</p>
<h2>DESCRIPTION</h2>
<p> <code>unflatten</code> is a preprocessor to <code>dot</code> that is used to improve the aspect ratio of graphs having many leaves or disconnected nodes. The usual layout for such a graph is generally very wide or tall. <code>unflatten</code> inserts invisible edges or adjusts the <code>minlen</code> on edges to improve layout compaction.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-l</code><i> len</i></p>
<dd> The minimum length of leaf edges is staggered between 1 and <i>len</i> (a small integer).</p>
<dt><code>-f</code></p>
<dd> Enables the staggering of the <code>-l</code> option to fanout nodes whose indegree and outdegree are both 1. This helps with structures such as <i>a -&gt; {w x y z} -&gt; b</i>. This option only works if the <code>-l</code> flag is set.</p>
<dt><code>-c</code><i> len</i></p>
<dd> Form disconnected nodes into chains of up to <i>len</i> nodes.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> causes the output to be written to the specified file; by default, output is written to <code>stdout</code>.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
