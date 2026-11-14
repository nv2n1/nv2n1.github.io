---
title: "acyclic(1)"
name: "acyclic"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acyclic/"
description: "acyclic – make directed graph acyclic"
---

<h2 class="name">NAME</h2>
<p> acyclic &#8211; make directed graph acyclic </p>
<h2>SYNOPSIS</h2>
<p> <code>acyclic</code> [ <code>-nv?</code> ] [ <code>-o</code> <i>outfile</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>acyclic</code> is a filter that takes a directed graph as input and outputs a copy of the graph with sufficient edges reversed to make the graph acyclic. The reversed edge inherits all of the attributes of the original edge. The optional file argument specifies where the input graph is stored; by default, the program reads from <code>stdin</code>.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-n</code></p>
<dd> No output is produced, though the return value will indicate whether the graph is acyclic or not.</p>
<dt><code>-v</code></p>
<dd> Print information about whether the file is acyclic, has a cycle or is undirected.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> causes the output to be written to the specified file; by default, output is written to <code>stdout</code>.</p>
<dt><code>-?</code></p>
<dd> option causes the program to print usage information.</dl>
<h2>RETURN CODES</h2>
<p> <code>acyclic</code> returns <code>0</code> if the graph is acyclic; <code>1</code> if the graph has a cycle; <code>2</code> if the graph is undirected; and <code>255</code> if there are any errors.</p>
<h2>BUGS</h2>
<p> If the graph is strict and there is a cycle of length 2, the attributes of the reversed edge are lost. </p>
<p> Some edge attributes are non-symmetric, referring to either the head or tail node. At present, there is no mechanism or convention for correctly switching or renaming these.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
