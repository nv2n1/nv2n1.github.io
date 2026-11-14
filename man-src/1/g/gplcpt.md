---
title: "gplcpt(1)"
name: "gplcpt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gplcpt/"
description: "gplcpt – convert GIMP colour palette (gpl) to GMT colour palette table (cpt)."
---

<h2 class="name">NAME</h2>
<p> gplcpt &#8211; convert GIMP colour palette (gpl) to GMT colour palette table (cpt). </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gplcpt</code> [-b&nbsp;<wbr><i>rgb</i>] [-f&nbsp;<wbr><i>rgb</i>] [-h] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>file</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gplcpt</code> converts <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1) colour palette (gpl) files to the <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1) colour palette table (cpt) format. The output is a piecewise constant (step or discrete) gradient. One could use <code><a href="/docs/linux/man/1-cptcont/">cptcont</a></code>(1) program to convert the output to a continuous cpt file if so desired. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the background colour of the output.</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the foreground colour of the output.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-n</code>, <code>&#8211;nan</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the NaN (no data) colour of the output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
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
<p> <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-cptcont/">cptcont</a></code>(1). </p>
<h2>Index</h2>
