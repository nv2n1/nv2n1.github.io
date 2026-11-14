---
title: "zlib-flate(1)"
name: "zlib-flate"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zlib-flate/"
description: "zlib-flate – raw zlib compression program"
---

<h2 class="name">NAME</h2>
<p> zlib-flate &#8211; raw zlib compression program </p>
<h2>SYNOPSIS</h2>
<p> <code>zlib-flate</code> <i>-compress | -uncompress</i></p>
<h2>DESCRIPTION</h2>
<p> The zlib-flate program is part of the qpdf package. </p>
<p> The zlib-flate program reads from standard input and writes to standard output either compressing or uncompressing its input using raw zlib compression. It can be used to uncompress or compress raw PDF streams or other data that is compressed with raw zlib compression. This program is provided primarily as a debugging tool, though it could be used for other purposes, such as being called from a script that creates simple PDF files. </p>
<p> This program should not be used as a general purpose compression tool. Use something like <a href="/docs/linux/man/1-gzip/">gzip</a>(1) instead. </p>
<p> For details about qpdf, please see the qpdf manual, which can be found at <a rel="nofollow" href="https://qpdf.readthedocs.io.">https://qpdf.readthedocs.io.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-qpdf/">qpdf</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1) </p>
<h2>Index</h2>
