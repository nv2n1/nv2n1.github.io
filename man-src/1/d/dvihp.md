---

title: "dvihp(1)"
name: "dvihp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvihp/"
description: "dvihp – convert a TeX DVI file to Hewlett-Packard PCL"
---

<p> dvihp &#8211; convert a TeX DVI file to Hewlett-Packard PCL </p>
<h2>SYNOPSIS</h2>
<p> <code>dvihp</code> [<i>options</i>] <i>dvifile</i>[.dvi]</p>
<h2>DESCRIPTION</h2>
<p> <code>dvihp</code> translates the given <i>dvifile</i> to Hewlett-Packard PCL using <code><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></code>(1) then $DVILJ (dvilj4 by default). </p>
<p> In the absence of other options, pipe the PCL to $SPOOL (lpr by default).</p>
<h2>OPTIONS</h2>
<p> Options are recognized from dvips where possible:</p>
<dl>
<dt><code>-A</code></dt>
<dd> print odd pages</dd>
<dt><code>-B</code></dt>
<dd> print even pages</dd>
<dt><code>-d</code> <i>n</i></dt>
<dd> set debug bits to <i>n</i> (see documentation)</dd>
<dt><code>-D</code> <i>n</i></dt>
<dd> set resolution to <i>n</i></dd>
<dt><code>-f</code></dt>
<dd> run as filter</dd>
<dt><code>-l</code> <i>n</i></dt>
<dd> don&#8217;t print pages after <i>n</i></dd>
<dt><code>-m</code></dt>
<dd> manual feed</dd>
<dt><code>-n</code> <i>n</i></dt>
<dd> print <i>n</i> pages</dd>
<dt><code>-O</code> <i>a</i>,<i>b</i></dt>
<dd> set/change paper offset to <i>a</i>,<i>b</i> mm.</dd>
<dt><code>-o</code> <i>s</i></dt>
<dd> output to <i>s</i> instead of spooling</dd>
<dt><code>-p</code> <i>n</i></dt>
<dd> don&#8217;t print pages before <i>n</i>.</dd>
<dt><code>-Ps</code></dt>
<dd> pass directly to lpr.</dd>
<dt><code>-v</code></dt>
<dd> verbose operation.</dd>
<dt><code>-x</code> <i>n</i></dt>
<dd> set magnification to <i>n</i>.</dd>
<dt><code>&#8211;help</code></dt>
<dd> write usage summary.</dd></dl>
<p> Other options are passed to the dvilj program.</p>
<h2>BUGS</h2>
<p> Email bug reports to tex-k [at] tug.org.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvicopy/">dvicopy</a></code>(1), <code><a href="/docs/linux/man/1-dvilj4/">dvilj4</a></code>(1). </p>
