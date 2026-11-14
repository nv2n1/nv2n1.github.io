---
title: "bcomps(1)"
name: "bcomps"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcomps/"
description: "bcomps – biconnected components filter for graphs"
---

<h2 class="name">NAME</h2>
<p> bcomps &#8211; biconnected components filter for graphs </p>
<h2>SYNOPSIS</h2>
<p> <code>bcomps</code> [ <code>-stvx?</code> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>bcomps</code> decomposes graphs into their biconnected components, printing the components to standard output.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-s</code></p>
<dd> No output graph is printed. Implies the <code>-v </code> flag.</p>
<dt><code>-t</code></p>
<dd> Print the underlying block-cutvertex tree.</p>
<dt><code>-x</code></p>
<dd> Each biconnected component is printed as a separate root graph.</p>
<dt><code>-v</code></p>
<dd> Prints number of blocks and cutvertices.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> If specified, each root graph will be written to a different file with the names derived from <i>outfile</i>. In particular, if both <code>-o</code> and <code>-x</code> flags are used, then each block is written to a different file. If <i>outfile</i> does not have a suffix, the nth block of the ith graph is written to <i>outfile_n_i</i>. However, the 0th block of the 0th graph is written to <i>outfile</i>. </p>
<p> If <i>outfile</i> has a suffix, i.e., has the form <i>base.sfx</i>, then the files will have the same name as above, except appended with <i>.sfx</i>. </p>
<p> The block-cutvertex tree of ith graph is written to <i>outfile_n_T</i>, with an appended suffix if specified.</dl>
<p> By default, each input graph is printed, with each block given as a subgraph whose name is a concatenation of the name of the input graph, the string &quot;_bcc_&quot; and the number of the block.</p>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in dot format. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> <code>bcomps</code> returns <code>0</code> if all the input graphs are biconnected; and non-zero if any graph has multiple blocks, or any error occurred.</p>
<h2>BUGS</h2>
<p> It is possible, though unlikely, that the names used for connected components and their subgraphs may conflict with existing subgraph names.</p>
<h2>AUTHORS</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-gc/">gc</a>(1), <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
