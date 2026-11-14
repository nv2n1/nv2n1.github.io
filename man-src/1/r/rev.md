---
title: "rev(1)"
name: "rev"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rev/"
description: "rev – reverse lines characterwise"
---

<h2 class="name">NAME</h2>
<p> rev &#8211; reverse lines characterwise </p>
<h2>SYNOPSIS</h2>
<p> <code>rev</code> [option] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>rev</code> utility copies the specified files to standard output, reversing the order of characters in every line. If no files are specified, standard input is read. </p>
<p> This utility is a line-oriented tool and it uses in-memory allocated buffer for a whole wide-char line. If the input file is huge and without line breaks than allocate the memory for the file may be unsuccessful.</p>
<h2>OPTIONS</h2>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tac/">tac</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>rev</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
