---
title: "gc(1)"
name: "gc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gc/"
description: "gc – count graph components"
---

<h2 class="name">NAME</h2>
<p> gc &#8211; count graph components </p>
<h2>SYNOPSIS</h2>
<p> <code>gc</code> [ <code>-necCaDUrsv?</code> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gc</code> is a graph analogue to <code>wc </code> in that it prints to standard output the number of nodes, edges, connected components or clusters contained in the input files. It also prints a total count for all graphs if more than one graph is given.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-n</code></p>
<dd> Count nodes.</p>
<dt><code>-e</code></p>
<dd> Count edges.</p>
<dt><code>-c</code></p>
<dd> Count connected components.</p>
<dt><code>-C</code></p>
<dd> Count clusters. By definition, a cluster is a graph or subgraph whose name begins with &quot;cluster&quot;.</p>
<dt><code>-a</code></p>
<dd> Count all. Equivalent to <code>-encC</code></p>
<dt><code>-r</code></p>
<dd> Recursively analyze subgraphs.</p>
<dt><code>-s</code></p>
<dd> Print no output. Only exit value is important.</p>
<dt><code>-D</code></p>
<dd> Only analyze directed graphs.</p>
<dt><code>-U</code></p>
<dd> Only analyze undirected graphs.</p>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-?</code></p>
<dd> Print usage information.</dl>
<p> By default, <i>gc</i> returns the number of nodes and edges.</p>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned:</p>
<dl>
<dt><code>0</code></p>
<dd> Successful completion.</p>
<dt><code>1</code></p>
<dd> The <code>-U</code> or <code>-E</code> option was used, and a graph of the wrong type was encountered.</dl>
<h2>AUTHOR</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wc/">wc</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
