---
title: "memusagestat(1)"
name: "memusagestat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memusagestat/"
description: "memusagestat – generate graphic from memory profiling data"
---

<h2 class="name">NAME</h2>
<p> memusagestat &#8211; generate graphic from memory profiling data </p>
<h2>SYNOPSIS</h2>
<p> <code>memusagestat</code> [<i>option</i>]&#8230; <i>datafile</i> [<i>outfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>memusagestat</code> creates a PNG file containing a graphical representation of the memory profiling data in the file <i>datafile</i>; that file is generated via the <i>-d</i> (or <i>&#8211;data</i>) option of <code><a href="/docs/linux/man/1-memusage/">memusage</a></code>(1). </p>
<p> The red line in the graph shows the heap usage (allocated memory) and the green line shows the stack usage. The x-scale is either the number of memory-handling function calls or (if the <i>-t</i> option is specified) time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;output=</code><i>file</i></p>
<dd> Name of the output file.</p>
<dt><code>-s&nbsp;</code><i>string</i>,&nbsp;<code>&#8211;string=</code><i>string</i></p>
<dd> Use <i>string</i> as the title inside the output graph.</p>
<dt><code>-t</code>,&nbsp;<code>&#8211;time</code></p>
<dd> Use time (rather than number of function calls) as the scale for the X axis.</p>
<dt><code>-T</code>,&nbsp;<code>&#8211;total</code></p>
<dd> Also draw a graph of total memory consumption.</p>
<dt><code>-x&nbsp;</code><i>size</i>,&nbsp;<code>&#8211;x-size=</code><i>size</i></p>
<dd> Make the output graph <i>size</i> pixels wide.</p>
<dt><code>-y&nbsp;</code><i>size</i>,&nbsp;<code>&#8211;y-size=</code><i>size</i></p>
<dd> Make the output graph <i>size</i> pixels high.</p>
<dt><code>-?</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>,&nbsp;<code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>BUGS</h2>
<p> To report bugs, see</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/1-memusage/">memusage</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-memusage/">memusage</a></code>(1), <code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
