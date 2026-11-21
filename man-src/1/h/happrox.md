---

title: "happrox(1)"
name: "happrox"
section: "1"
letter: "h"
url: "/docs/linux/man/1-happrox/"
description: "happrox – returns a simplified triangulation of a set of points using algorithm III of Garland and Heckbert (1995)."
---

<p> <code>happrox</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;[<i>input.pgm</i>|<i>input</i>]&nbsp;&gt;&nbsp;<i>output.gts</i> </p>
<p> This manual page documents briefly the <code>happrox</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-n&nbsp;</code><i>N</i>,&nbsp;<code>&#8211;number=</code><i>N</i></dt>
<dd> Stop the refinement process if the number of vertices is larger than <i>N</i>.</dd>
<dt><code>-c&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;cost=</code><i>C</i></dt>
<dd> Stop the refinement process if the cost of insertion of a vertex is smaller than <i>C</i>.</dd>
<dt><code>-f</code>,&nbsp;<code>&#8211;flat</code></dt>
<dd> Input is a flat file with three x,y,z columns (default is PGM file).</dd>
<dt><code>-r&nbsp;</code><i>Z</i>,&nbsp;<code>&#8211;relative=</code><i>Z</i></dt>
<dd> Use relative height cost for all heights larger than <i>Z</i>.</dd>
<dt><code>-k</code>,&nbsp;<code>&#8211;keep</code></dt>
<dd> Keep enclosing triangle.</dd>
<dt><code>-C</code>,&nbsp;<code>&#8211;closed</code></dt>
<dd> Close the surface.</dd>
<dt><code>-l</code>,&nbsp;<code>&#8211;log</code></dt>
<dd> Log evolution of cost.</dd>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></dt>
<dd> Display surface statistics.</dd>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></dt>
<dd> Display the help and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> happrox was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
