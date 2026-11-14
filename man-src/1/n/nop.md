---
title: "nop(1)"
name: "nop"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nop/"
description: "nop – pretty-print graph file"
---

<h2 class="name">NAME</h2>
<p> nop &#8211; pretty-print graph file </p>
<h2>SYNOPSIS</h2>
<p> <code>nop</code> [ <code>-p?</code> ] [ <i>files </i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nop</code> reads a stream of graphs and prints each in pretty-printed (canonical) format on stdout. If no <i>files</i> are given, it reads from stdin.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-p</code></p>
<dd> Produce no output &#8211; just check the input for valid DOT.</p>
<dt><code>-?</code></p>
<dd> Print usage information.</dl>
<h2>EXIT STATUS</h2>
<p> If any errors occurred while processing any input, such as a file not found or a file containing illegal DOT, a non-zero exit value is returned. Otherwise, zero is returned.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wc/">wc</a>(1), <a href="/docs/linux/man/1-acyclic/">acyclic</a>(1), <a href="/docs/linux/man/1-gvpr/">gvpr</a>(1), <a href="/docs/linux/man/1-gvcolor/">gvcolor</a>(1), <a href="/docs/linux/man/1-ccomps/">ccomps</a>(1), <a href="/docs/linux/man/1-sccmap/">sccmap</a>(1), <a href="/docs/linux/man/1-tred/">tred</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3) </p>
<h2>Index</h2>
