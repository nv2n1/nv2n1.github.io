---
title: "ecl-config(1)"
name: "ecl-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecl-config/"
description: "ecl-config – Embeddable Common LISP configuration query"
---

<h2>NAME</h2>
<p> ecl-config &#8211; Embeddable Common LISP configuration query</p>
<h2>SYNOPSIS</h2>
<p> <code>ecl-config</code> [<code>-cflags] [-libs] [-ldflags] [ LIBS] </code></p>
<h2>DESCRIPTION</h2>
<p> ecl-config will return through the standard output the set of compiler or linker flags needed to build applications that embed ecl.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-cflags</code></p>
<dd> Output the flags required to compile a C/C++ file.</p>
<dt><code>-libs</code></p>
<dd>
<dt><code>-ldflags</code></p>
<dd> Return the linker flags required to build a C/C++ application or shared library.</p>
<dt><code>LIBS</code></p>
<dd> When also using <code>-ldflags</code> also add the cmp (compiler) library.</dl>
<h2>BUGS</h2>
<p> Probably some. Report them! </p>
<h2>Index</h2>
