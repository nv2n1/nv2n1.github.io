---
title: "cptinfo(1)"
name: "cptinfo"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptinfo/"
description: "cptinfo – print summary information on GMT colour palette table (cpt) files."
---

<h2 class="name">NAME</h2>
<p> cptinfo &#8211; print summary information on GMT colour palette table (cpt) files. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cptinfo</code> [-c] [-h] [-o&nbsp;<wbr><i>file</i>] [-p] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cptinfo</code> utility prints summary information on the colour palette table (cpt) file which is its input. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;csv</code></p>
<dl>
<dt>
<dd> Output in a comma separated value format, suitable for easy parsing by other programs.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-p</code>, <code>&#8211;plain</code></p>
<dl>
<dt>
<dd> Output in a plain human-readable format.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1). </p>
<h2>Index</h2>
