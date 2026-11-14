---
title: "dvihp(1)"
name: "dvihp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvihp/"
description: "dvihp – convert a TeX DVI file to Hewlett-Packard PCL"
---

<h2 class="name">NAME</h2>
<p> dvihp &#8211; convert a TeX DVI file to Hewlett-Packard PCL </p>
<h2>SYNOPSIS</h2>
<p> <code>dvihp</code> [<i>options</i>] <i>dvifile</i>[.dvi]</p>
<h2>DESCRIPTION</h2>
<p> <code>dvihp</code> translates the given <i>dvifile</i> to Hewlett-Packard PCL using <code><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></code>(1) then $DVILJ (dvilj4 by default). </p>
<p> In the absence of other options, pipe the PCL to $SPOOL (lpr by default).</p>
<h2>OPTIONS</h2>
<p> Options are recognized from dvips where possible:</p>
<dl>
<dt><code>-A</code></p>
<dd> print odd pages</p>
<dt><code>-B</code></p>
<dd> print even pages</p>
<dt><code>-d</code> <i>n</i></p>
<dd> set debug bits to <i>n</i> (see documentation)</p>
<dt><code>-D</code> <i>n</i></p>
<dd> set resolution to <i>n</i></p>
<dt><code>-f</code></p>
<dd> run as filter</p>
<dt><code>-l</code> <i>n</i></p>
<dd> don&#8217;t print pages after <i>n</i></p>
<dt><code>-m</code></p>
<dd> manual feed</p>
<dt><code>-n</code> <i>n</i></p>
<dd> print <i>n</i> pages</p>
<dt><code>-O</code> <i>a</i>,<i>b</i></p>
<dd> set/change paper offset to <i>a</i>,<i>b</i> mm.</p>
<dt><code>-o</code> <i>s</i></p>
<dd> output to <i>s</i> instead of spooling</p>
<dt><code>-p</code> <i>n</i></p>
<dd> don&#8217;t print pages before <i>n</i>.</p>
<dt><code>-Ps</code></p>
<dd> pass directly to lpr.</p>
<dt><code>-v</code></p>
<dd> verbose operation.</p>
<dt><code>-x</code> <i>n</i></p>
<dd> set magnification to <i>n</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> write usage summary.</dl>
<p> Other options are passed to the dvilj program.</p>
<h2>BUGS</h2>
<p> Email bug reports to tex-k [at] tug.org.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></code>(1), <code><a href="/docs/linux/man/1-dvilj4/">dvilj4</a></code>(1). </p>
<h2>Index</h2>
