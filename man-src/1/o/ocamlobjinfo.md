---
title: "ocamlobjinfo(1)"
name: "ocamlobjinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlobjinfo/"
description: "ocamlobjinfo – dump information about OCaml compiled objects"
---

<h2 class="name">NAME</h2>
<p> ocamlobjinfo &#8211; dump information about OCaml compiled objects </p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlobjinfo</code> file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Dump information contained in OCaml compiled objects. It works on .cmi, .cmo, .cma, .cmx, .cmxa, .cmxs files and pure bytecode executables. </p>
<p> <code>ocamlobjinfo</code> is able to show information regarding: </p>
<dl>
<dt>
<dd> module names </p>
<p> unit names </p>
<p> declared primitives </p>
<p> imported interfaces </p>
<p> md5sums of imported interfaces </p>
<p> forced custom mode </p>
<p> extra C libraries needed </p>
<p> extra C flags needed </p>
<p> use of unsafe features</dl>
<p> depending on its arguments.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1), <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Stefano Zacchiroli &lt;zack [at] debian.org&gt; and Stéphane Glondu &lt;glondu [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
