---
title: "ldb_utf8_fns(3)"
name: "ldb_utf8_fns"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_utf8_fns/"
description: "ldb_utf8_fns –"
---

<h2 class="name">NAME</h2>
<p> ldb_utf8_fns &#8211; </p>
<p> The user can optionally supply a custom utf8 functions, to handle comparisons and casefolding.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ldb.h&gt;</p>
<h3>Data Fields</h3>
<p> void * <code>context</code> </p>
<p> char *(* <code>casefold</code> )(void *context, TALLOC_CTX *mem_ctx, const char *s, size_t n) </p>
<h2>Detailed Description</h2>
<p> The user can optionally supply a custom utf8 functions, to handle comparisons and casefolding. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
