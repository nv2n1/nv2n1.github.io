---
title: "graphml2gv(1)"
name: "graphml2gv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-graphml2gv/"
description: "graphml2gv – GRAPHML-DOT converter"
---

<h2 class="name">NAME</h2>
<p> graphml2gv &#8211; GRAPHML-DOT converter </p>
<h2>SYNOPSIS</h2>
<p> <code>graphml2gv</code> [ <code>-?v</code> ] [ <code>-g</code><i>gname</i> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>graphml2gv</code> converts a graph specified in the GRAPHML format to a graph in the GV (formerly DOT) format.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-v</code></p>
<dd> Turns on verbose mode</p>
<dt><code>-?</code></p>
<dd> Prints usage information and exits.</p>
<dt><code>-g</code><i>gname</i></p>
<dd> The string <i>gname</i> is used as the name of the generated graph. If multiple graphs are generated, subsequent graphs use the name <i>gname</i> appended with an integer.</p>
<dt><code>-o</code><i>outfile</i></p>
<dd> Prints output to the file <i>outfile</i>. If not given, <code>graphml2gv</code> uses stdout.</p>
<dt></dl>
<h2>OPERANDS</h2>
<dd> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in GRAPHML. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> Return <code>0</code> if there were no problems during conversion; and non-zero if any error occurred.</p>
<h2>LIMITATIONS</h2>
<p> As both the graph and graphics models of GV and GML differ significantly, the conversion can only be at best approximate. In particular, GV currently has no notion of hyperedges or edges containing graphs. </p>
<p> At present, <code>graphml2gv</code> only supports the basic graph topology. Specifically, the &lt;KEY&gt; and &lt;DATA&gt; elements are not handled, though they could be.</p>
<h2>AUTHORS</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/3-libcgraph/">libcgraph</a>(3) </p>
<h2>Index</h2>
