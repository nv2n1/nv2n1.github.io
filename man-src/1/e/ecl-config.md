---

title: "ecl-config(1)"
name: "ecl-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecl-config/"
description: "ecl-config – Embeddable Common LISP configuration query"
---

<p> ecl-config &#8211; Embeddable Common LISP configuration query</p>
<h2>SYNOPSIS</h2>
<p> <code>ecl-config</code> [<code>-cflags] [-libs] [-ldflags] [ LIBS] </code></p>
<h2>DESCRIPTION</h2>
<p> ecl-config will return through the standard output the set of compiler or linker flags needed to build applications that embed ecl.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-cflags</code></dt>
<dd> Output the flags required to compile a C/C++ file.</dd>
<dt><code>-libs</code></dt>
<dd>
</dd><dt><code>-ldflags</code></dt>
<dd> Return the linker flags required to build a C/C++ application or shared library.</dd>
<dt><code>LIBS</code></dt>
<dd> When also using <code>-ldflags</code> also add the cmp (compiler) library.</dd></dl>
<h2>BUGS</h2>
<p> Probably some. Report them! </p>
