---
title: "sccmap(1)"
name: "sccmap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sccmap/"
description: "sccmap – extract strongly connected components of directed graphs"
---

<h2 class="name">NAME</h2>
<p> sccmap &#8211; extract strongly connected components of directed graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>sccmap</code> [<code>-dsv</code>] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>sccmap</i> decomposes digraphs into strongly connected components and an auxiliary map of the relationship between components. In this map, each component is collapsed into a node. The resulting graphs are printed to standard out. The number of nodes, edges and strongly connected components are printed to standard error. <code>sccmap</code> is a way of partitioning large graphs into more manageable pieces.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-d</code></p>
<dd> Preserve degenerate components of only one node.</p>
<dt><code>-s</code></p>
<dd> Do not print the resulting graphs. Only the statistics are important.</p>
<dt><code>-S</code></p>
<dd> Just print the resulting graphs. No statistics are printed.</p>
<dt><code>-o</code><i>output</i></p>
<dd> Prints output to the file <i>output</i>. If not given, <code>sccmap</code> uses stdout.</p>
<dt><code>-v</code></p>
<dd> Generate additional statistics. In particular, <code>sccmap</code> prints the number of nodes, edges, connected components, and strongly connected components, followed by the fraction of nodes in a non-trivial strongly connected components, the maximum degree of the graph, and fraction of non-tree edges in the graph.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>sccmap</code> emits a warning if it encounters an undirected graph, and ignores it.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
