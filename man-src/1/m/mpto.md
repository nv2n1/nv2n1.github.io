---
title: "mpto(1)"
name: "mpto"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpto/"
description: "mpto – extract labels in MetaPost pictures for typesetting"
---

<h2 class="name">NAME</h2>
<p> mpto &#8211; extract labels in MetaPost pictures for typesetting </p>
<h2>SYNOPSIS</h2>
<p> <code>mpto</code> [<i>-tex</i>|<i>-troff</i>] <i>mpfile</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> Strip <i>btex..etex</i> and <i>verbatimtex&#8230;etex</i> parts from MetaPost input file <i>mpfile</i>, converting to either TeX or Troff (TeX by default). The generated code is dumped on standard output. </p>
<p> <code>mpto</code> is typically called by <code>makempx</code>, not from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>mpto</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print help message and exit.</dd>
<dt><code>-tex</code></dt>
<dd> Assume input file contains TeX commands.</dd>
<dt><code>-troff</code></dt>
<dd> Assume input file contains Troff commands.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-makempx/">makempx</a></code>(1). </p>
