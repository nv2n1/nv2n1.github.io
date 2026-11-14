---
title: "btparser(1)"
name: "btparser"
section: "1"
letter: "b"
url: "/docs/linux/man/1-btparser/"
description: "btparser – a backtrace analyzer"
---

<h2>NAME</h2>
<p> btparser &#8211; a backtrace analyzer</p>
<h2>SYNOPSIS</h2>
<p> <code>btparser</code> [option]&#8230; [FILE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>btparser</i> is a command line tool that analyzes backtraces produced by GDB and provides their textual representation useful for crash duplication detection. </p>
<p> By default, btparser prints the backtrace tree created by parsing the input file. </p>
<h2>OPTIONS</h2>
<p> <code>Basic startup options</code></p>
<dl>
<dt>-V, &#8211;version</p>
<dd> Displays version of btparser.</p>
<dt>-?, &#8211;help</p>
<dd> Print a help message describing all of btparser’s command-line options. </p>
</dl>
<p> <code>Actions</code></p>
<dl>
<dt>-r, &#8211;rate</p>
<dd> Print a float number between 0 and 1, representing the quality of the backtrace.</p>
<dt>-c, &#8211;crash-function</p>
<dd> Print the name of the function where the program crashed, if it&#8217;s successfully detected.</p>
<dt>-h, &#8211;duplicate-hash</p>
<dd> Print a short, textual representation of the backtrace, useful for detecting the backtrace duplicates.</p>
<dt>-s, &#8211;distances</p>
<dd> Print Damerau–Levenshtein distances between the backtraces specified on the command line.</p>
<dt>-g, &#8211;dendrogram</p>
<dd> Cluster backtraces by their distance and print an ASCII representation of the dendrogram.</p>
<dt>-l, &#8211;clusters=LEVEL</p>
<dd> Print clusters cut from the dendrogram at the specified level. </p>
</dl>
<p> <code>Additional options</code></p>
<dl>
<dt>-i, &#8211;stdin</p>
<dd> Read input from the standard input rather than file.</p>
<dt>-m, &#8211;max-frames=FRAMES</p>
<dd> When creating optimized backtrace or preparing backtrace for comparison, limit the number of frames to FRAMES. (default 8)</p>
<dt>-z, &#8211;min-cluster-size=SIZE</p>
<dd> When printing clusters, ignore clusters that contain fewer than SIZE objects. (default 2)</p>
<dt>-d, &#8211;debug</p>
<dd> Prints debug information when scanning/parsing the backtrace.</p>
<dt>-v, &#8211;verbose</p>
<dd> Print more output than usual. </p>
</dl>
<h2>Index</h2>
