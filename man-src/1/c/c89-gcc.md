---
title: "c89-gcc(1)"
name: "c89-gcc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-c89-gcc/"
description: "c89 – ANSI (1989) C compiler"
---

<h2 class="name">NAME</h2>
<p> c89 &#8211; ANSI (1989) C compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>c89</code> <i></i>[-pedantic] [-pedantic-errors] [-D_ANSI_SOURCE] options &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Calls the C compiler (cc) with the given <code>options ,</code> using a C language environment compatible with the -ansiC specification. </p>
<p> This includes proper handling of trigraphs, disabling non-ANSI compiler features (such as <code>asm ,</code> <code>inline ,</code> <code>typeof ,</code> and the $ character in identifiers), and definition of the preprocessor symbol __STRICT_ANSI__ .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cc/">cc</a>(1) for a description of all options.</p>
<h2>HISTORY</h2>
<p> Appeared in NetBSD 1.4 .</p>
<h2>BUGS</h2>
<p> Since <code>c89</code> is a shell wrapper script to <code>cc ,</code> compile errors are prefixed by &quot;cc:&quot;. </p>
<h2>Index</h2>
