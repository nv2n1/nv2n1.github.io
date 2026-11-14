---
title: "thinkjettopbm(1)"
name: "thinkjettopbm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-thinkjettopbm/"
description: "thinkjettopbm – convert HP ThinkJet printer commands file to PBM"
---

<h2 class="name">NAME</h2>
<p> thinkjettopbm &#8211; convert HP ThinkJet printer commands file to PBM </p>
<h2>SYNOPSIS</h2>
<p> <code>thinkjettopbm</code> [<i>-d</i>] [<i>thinkjet_file</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads HP ThinkJet printer commands from the standard input, or <i>thinkjet_file</i> if specified, and writes a PBM image to the standard output. Text and non-graphics command sequences are silently ignored. </p>
<p> The <code>-d</code> option turns on debugging messages which are written to the standard error stream. </p>
<h2>BUGS</h2>
<p> Handles only a small subset of ThinkJet command sequences, but enough to convert screen images from older HP test equipment. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/1-pjtoppm/">pjtoppm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2001 by W. Eric Norum </p>
<h2>Index</h2>
