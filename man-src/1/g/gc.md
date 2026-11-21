---
title: "gc(1)"
name: "gc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gc/"
description: "gc – count graph components"
---

<h2>SYNOPSIS</h2>
<p> <code>gc</code> [ <code>-necCaDUrsv?</code> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gc</code> is a graph analogue to <code>wc </code> in that it prints to standard output the number of nodes, edges, connected components or clusters contained in the input files. It also prints a total count for all graphs if more than one graph is given.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-n</code></dt>
<dd> Count nodes.</dd>
<dt><code>-e</code></dt>
<dd> Count edges.</dd>
<dt><code>-c</code></dt>
<dd> Count connected components.</dd>
<dt><code>-C</code></dt>
<dd> Count clusters. By definition, a cluster is a graph or subgraph whose name begins with &quot;cluster&quot;.</dd>
<dt><code>-a</code></dt>
<dd> Count all. Equivalent to <code>-encC</code></dd>
<dt><code>-r</code></dt>
<dd> Recursively analyze subgraphs.</dd>
<dt><code>-s</code></dt>
<dd> Print no output. Only exit value is important.</dd>
<dt><code>-D</code></dt>
<dd> Only analyze directed graphs.</dd>
<dt><code>-U</code></dt>
<dd> Only analyze undirected graphs.</dd>
<dt><code>-v</code></dt>
<dd> Verbose output.</dd>
<dt><code>-?</code></dt>
<dd> Print usage information.</dd></dl>
<p> By default, <i>gc</i> returns the number of nodes and edges.</p>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></dt>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dd></dl>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned:</p>
<dl>
<dt><code>0</code></dt>
<dd> Successful completion.</dd>
<dt><code>1</code></dt>
<dd> The <code>-U</code> or <code>-E</code> option was used, and a graph of the wrong type was encountered.</dd></dl>
<h2>AUTHOR</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wc/">wc</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), libgraph(3) </p>
