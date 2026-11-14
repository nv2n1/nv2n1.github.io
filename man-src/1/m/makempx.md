---
title: "makempx(1)"
name: "makempx"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makempx/"
description: "makempx – typeset labels in MetaPost pictures with TeX or Troff"
---

<h2 class="name">NAME</h2>
<p> makempx &#8211; typeset labels in MetaPost pictures with TeX or Troff </p>
<h2>SYNOPSIS</h2>
<p> <code>makempx</code> [<i>&#8211;tex</i>|<i>&#8211;troff</i>] <i>mpfile mpxfile</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> If <i>mpxfile</i> is older than <i>mpfile</i>, translate the labels from the MetaPost input file <i>mpfile</i> to low-level commands in <i>MPXFILE</i>, by running <code>mpto -tex</code>, <code>tex</code>, and <code>dvitomp</code> by default; or, if <code>-troff</code> is specified, <code>mpto -troff</code>, <code>eqn -d\$\$ | troff -Tpost</code>, and <code>dmp</code>. </p>
<p> The current directory is used for writing temporary files. Errors are left in <i>mpxerr.{tex,log,dvi}</i>. </p>
<p> If the file named in <i>$MPTEXPRE</i> (mptexpre.tex by default) exists, it is prepended to the output in tex mode. </p>
<p> <code>makempx</code> is typically called by <code>mpost</code>, not from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>makempx</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;tex</code></p>
<dd> Assume input file contains TeX commands.</p>
<dt><code>&#8211;troff</code></p>
<dd> Assume input file contains Troff commands.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-mpto/">mpto</a></code>(1). </p>
<h2>Index</h2>
