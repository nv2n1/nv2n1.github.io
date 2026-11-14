---
title: "ldb_debug_ops(3)"
name: "ldb_debug_ops"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_debug_ops/"
description: "ldb_debug_ops –"
---

<h2 class="name">NAME</h2>
<p> ldb_debug_ops &#8211; </p>
<p> the user can optionally supply a debug function.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ldb.h&gt;</p>
<h3>Data Fields</h3>
<p> void(* <code>debug</code> )(void *context, enum ldb_debug_level level, const char *fmt, va_list ap) PRINTF_ATTRIBUTE(3 </p>
<p> void(*) void <code>context</code> ) </p>
<h2>Detailed Description</h2>
<p> the user can optionally supply a debug function. </p>
<p> The function is based on the vfprintf() style of interface, but with the addition of a severity level </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
