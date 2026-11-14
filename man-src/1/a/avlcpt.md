---
title: "avlcpt(1)"
name: "avlcpt"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avlcpt/"
description: "avlcpt – convert ArcView Legend gradients to GMT colour palette tables"
---

<h2 class="name">NAME</h2>
<p> avlcpt &#8211; convert ArcView Legend gradients to GMT colour palette tables </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>avlcpt</code> [-b&nbsp;<wbr><i>rgb</i>] [-f&nbsp;<wbr><i>rgb</i>] [-h] [-l&nbsp;<wbr><i>adjust</i>] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>file</i>] [-p&nbsp;<wbr><i>precision</i>] [-u&nbsp;<wbr><i>adjust</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>avlcpt</code> utility will extract a gradient from an ArcView Legend (avl) file and write it to the GMT (Generic Mapping Tools) cpt format. Note that not every avl file will contain a gradient, some just have patterns. </p>
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
<p> <code>-l</code>, <code>&#8211;lower</code> <i>adjust</i></p>
<dl>
<dt>
<dd> Decrease the lower limit on each segment by the specified amount.</dl>
<p> <code>-n</code>, <code>&#8211;nan</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the NaN (no data) colour of the output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-p</code>, <code>&#8211;precision</code> <i>precision</i></p>
<dl>
<dt>
<dd> Specify rounding. ArcView legends have a rather interesting approach to height specification whereby colour ranges might be 0-49, 50-99, and so on. The cpt format requires that the end of one segment be at the same as the start of the next, so some rounding of the input will usually be required. The precision is specified directly rather than by number of digits, so that <code>-p10</code> will round to the nearest 10 and so on.</dl>
<p> <code>-u</code>, <code>&#8211;upper</code> <i>adjust</i></p>
<dl>
<dt>
<dd> Increase the upper limit on each segment by the specified amount.</dl>
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
