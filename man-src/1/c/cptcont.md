---
title: "cptcont(1)"
name: "cptcont"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptcont/"
description: "cptcont – create a continuous GMT colour palette table (cpt) file based on the colours of a non-continuous cpt file."
---

<h2 class="name">NAME</h2>
<p> cptcont &#8211; create a continuous GMT colour palette table (cpt) file based on the colours of a non-continuous cpt file. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cptcont</code> [-h] [-m] [-o&nbsp;<wbr><i>file</i>] [-p&nbsp;<wbr><i>percent</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cptcont</code> program converts a (possibly) discontinuous colour palette in the input to a continuous palette in the output. This is achieved by replacing the endpoints of segments at which a discontinuity occurs by their mean colour. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-m</code>, <code>&#8211;midpoint</code></p>
<dl>
<dt>
<dd> Split each input segment into two output segments with the colour at the common point being the colour of the original segment. This gives a more faithful conversion of gradients with &quot;corners&quot;, such as diverging gradients, albeit at the cost of larger files.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-p</code>, <code>&#8211;partial</code> <i>percentage</i></p>
<dl>
<dt>
<dd> The endpoints are moved the specified <i>pecentage</i> towards the mean colour, so that a value of 100 (the default) moves the endpoints to the mean colour, 50 moves them half-way there, and so on. </p>
<p> Negative values and values greater than 100 are permitted.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLE</h2>
<p> Create an almost-continuous table: </p>
<dl>
<dt>
<dd>
<pre>
  cptcont -v -p 66 -o new.cpt old.cpt
</pre>
</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1). </p>
<h2>Index</h2>
