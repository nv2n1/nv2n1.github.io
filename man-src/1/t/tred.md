---
title: "tred(1)"
name: "tred"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tred/"
description: "tred – transitive reduction filter for directed graphs"
---

<h2 class="name">NAME</h2>
<p> tred &#8211; transitive reduction filter for directed graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>tred</code> [ <code>-v?</code> ] [ <i>files </i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>tred</code> computes the transitive reduction of directed graphs, and prints the resulting graphs to standard output. This removes edges implied by transitivity. Nodes and subgraphs are not otherwise affected. The &#8220;meaning&#8221; and validity of the reduced graphs is application dependent. <code>tred </code> is particularly useful as a preprocessor to <i>dot</i> to reduce clutter in dense layouts. </p>
<p> Undirected graphs are silently ignored.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-?</code></p>
<dd> Print usage information.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>BUGS</h2>
<p> Using bitmaps internally would substantially decrease running time.</p>
<h2>DIAGNOSTICS</h2>
<p> If a graph has cycles, its transitive reduction is not uniquely defined. In this case <i>tred</i> emits a warning.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
