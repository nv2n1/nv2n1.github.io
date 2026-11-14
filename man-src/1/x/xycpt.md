---
title: "xycpt(1)"
name: "xycpt"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xycpt/"
description: "xycpt – generate GMT colour palette table (cpt) files from column data."
---

<h2 class="name">NAME</h2>
<p> xycpt &#8211; generate GMT colour palette table (cpt) files from column data. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xycpt</code> [-b&nbsp;<wbr><i>rgb</i>] [-d] [-f&nbsp;<wbr><i>rgb</i>] [-h] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>file</i>] [-r&nbsp;<wbr><i>registration</i>] [-u] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>xycpt</code> program generates discrete or continuous cpt files from simple input describing sample values of the colour (or greyscale) range. The input consists of 1-4 columns. For 2 and 4 columns, the first column is interpreted as a (double) z value, for 1 and 3 the z value is taken implicitly. For 1 and 2 columns the final column will be taken as a greyscale value. For 3 and 4, the last 3 columns are taken as RGB values. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the background colour of the output.</dl>
<p> <code>-d</code>, <code>&#8211;discrete</code></p>
<dl>
<dt>
<dd> Output a discrete cpt file, the default is continuous.</dl>
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
<p> <code>-r</code>, <code>&#8211;registration</code> <i>string</i></p>
<dl>
<dt>
<dd> For discrete (using the <code>-d</code> option) conversion, specifies <code>upper</code>, <code>middle</code> or <code>lower</code> registration of the data value. For the <code>upper</code> and <code>lower</code> types the final (respectively the first) colour is omitted from the output; only the z value is used. For <code>middle</code> registration all the colours appear in the output.</dl>
<p> <code>-u</code>, <code>&#8211;unit</code></p>
<dl>
<dt>
<dd> Colour values are specified as floating point numbers in the range 0-1 rather than as integers in the range 0-255.</dl>
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
