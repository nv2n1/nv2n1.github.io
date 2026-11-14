---
title: "happrox(1)"
name: "happrox"
section: "1"
letter: "h"
url: "/docs/linux/man/1-happrox/"
description: "happrox – returns a simplified triangulation of a set of points using algorithm III of Garland and Heckbert (1995)."
---

<h2 class="name">NAME</h2>
<p> happrox &#8211; returns a simplified triangulation of a set of points using algorithm III of Garland and Heckbert (1995).</p>
<h2>SYNOPSIS</h2>
<p> <code>happrox</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;[<i>input.pgm</i>|<i>input</i>]&nbsp;&gt;&nbsp;<i>output.gts</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>happrox</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-n&nbsp;</code><i>N</i>,&nbsp;<code>&#8211;number=</code><i>N</i></p>
<dd> Stop the refinement process if the number of vertices is larger than <i>N</i>.</p>
<dt><code>-c&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;cost=</code><i>C</i></p>
<dd> Stop the refinement process if the cost of insertion of a vertex is smaller than <i>C</i>.</p>
<dt><code>-f</code>,&nbsp;<code>&#8211;flat</code></p>
<dd> Input is a flat file with three x,y,z columns (default is PGM file).</p>
<dt><code>-r&nbsp;</code><i>Z</i>,&nbsp;<code>&#8211;relative=</code><i>Z</i></p>
<dd> Use relative height cost for all heights larger than <i>Z</i>.</p>
<dt><code>-k</code>,&nbsp;<code>&#8211;keep</code></p>
<dd> Keep enclosing triangle.</p>
<dt><code>-C</code>,&nbsp;<code>&#8211;closed</code></p>
<dd> Close the surface.</p>
<dt><code>-l</code>,&nbsp;<code>&#8211;log</code></p>
<dd> Log evolution of cost.</p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Display surface statistics.</p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display the help and exit. </p>
</dl>
<h2>AUTHOR</h2>
<p> happrox was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
