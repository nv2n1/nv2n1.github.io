---
title: "cptclip(1)"
name: "cptclip"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptclip/"
description: "cptclip – extract a sub-table from a GMT colour palette table (cpt)."
---

<h2 class="name">NAME</h2>
<p> cptclip &#8211; extract a sub-table from a GMT colour palette table (cpt). </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cptclip</code> -R&nbsp;<wbr><i>min</i>/<i>max</i> [-h] [-o&nbsp;<wbr><i>file</i>] [-s] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cptclip</code> utility extracts a sub-table from a cpt format file. The arguments to the mandatory <code>-R</code> option, <i>min</i>/<i>max</i>, are interpreted as the (z) limits of the output unless the <code>-s</code> switch is specified, in which case they are the segment numbers. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified. </p>
<p> Note that much of the functionality of this program is included in recent versions of the GMT program <code><a href="/docs/linux/man/1-makecpt/">makecpt</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-R</code>, <code>&#8211;range</code> <i>min</i>/<i>max</i></p>
<dl>
<dt>
<dd> The (z) range of the output, or the segments if the <code>-s</code> switch is also given.</dl>
<p> <code>-s</code>, <code>&#8211;segments</code></p>
<dl>
<dt>
<dd> The <i>min</i> and <i>max</i> arguments of the <code>-R</code> switch are interpreted as the segment numbers (starting at one).</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLES</h2>
<p> Extract the table with z-range from 2.5 to 5: </p>
<dl>
<dt>
<dd>
<pre>
  cptclip -v -o new.cpt -R 2.5/5 old.cpt
</pre>
</dl>
<p> Extract the table with the first 5 segments: </p>
<dl>
<dt>
<dd>
<pre>
  cptclip -v -s -o new.cpt -R 1/5 old.cpt
</pre>
</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-makecpt/">makecpt</a></code>(1). </p>
<h2>Index</h2>
