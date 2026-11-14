---
title: "cilc(1)"
name: "cilc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cilc/"
description: "cilc – Mono CIL-to-C binding generator"
---

<h2>NAME</h2>
<p> cilc &#8211; Mono CIL-to-C binding generator</p>
<h2>SYNOPSIS</h2>
<p> <code>cilc</code> [options] <i>assembly</i> <i>target</i></p>
<h2>DESCRIPTION</h2>
<p> cilc is the Mono CIL-to-C binding generator. It takes a CIL assembly as input and generates a directory of C sources which, when compiled, provide a C interface to the classes contained within that assembly by means of a shared object library. </p>
<p> Generated sources make use of the Mono embedding API. Thus a complete Mono development environment must be available on the development system and a complete Mono runtime environment must be available on target systems.</p>
<h2>AUTHOR</h2>
<p> Written by Alp Toker &lt;alp [at] atoker.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1) </p>
<h2>Index</h2>
