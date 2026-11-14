---
title: "dmp(1)"
name: "dmp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmp/"
description: "dmp – translate Troff output to low-level MetaPost input"
---

<h2 class="name">NAME</h2>
<p> dmp &#8211; translate Troff output to low-level MetaPost input </p>
<h2>SYNOPSIS</h2>
<p> <code>dmp</code> [<i>option</i>] <i>ditrofffile</i> [<i>mpxfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>dmp</code> program generates MetaPost source code from the <i>ditrofffile</i>. The generated code is written in <i>mpxfile</i> if it is specified, and to standard output otherwise. </p>
<p> <code>dmp</code> is typically called from scripts like <code>makempx</code>, not from the command line.</p>
<h2>OPTIONS</h2>
<p> <code>dmp</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-makempx/">makempx</a></code>(1). </p>
<h2>Index</h2>
