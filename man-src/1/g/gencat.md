---
title: "gencat(1)"
name: "gencat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gencat/"
description: "gencat – Generate message catalog"
---

<h2 class="name">NAME</h2>
<p> gencat &#8211; Generate message catalog </p>
<h2>SYNOPSIS</h2>
<p> gencat [OPTION&#8230;] -o OUTPUT-FILE [INPUT-FILE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>gencat</code> program is specified in the X/Open standard and the GNU implementation follows this specification and so processes all correctly formed input files. Additionally some extension are implemented which help to work in a more reasonable way with the <code><a href="/docs/linux/man/3-catgets/">catgets</a></code>(3) functions. </p>
<dl>
<dt><code>-H</code>, <code>&#8211;header</code> <i>NAME</i></p>
<dd> Create C header file NAME containing symbol definitions</p>
<dt><code>&#8211;new</code></p>
<dd> Do not use existing catalog, force new output file</p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>NAME</i></p>
<dd> Write output to file NAME</dl>
<h2>AUTHOR</h2>
<p> <i>gencat</i> was written by Ulrich Drepper as part of the GNU C Library. </p>
<p> This man page was written by Jeff Bailey &lt;jbailey [at] debian.org&gt;. </p>
<h2>Index</h2>
