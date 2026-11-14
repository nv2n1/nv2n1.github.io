---
title: "ldb_val(3)"
name: "ldb_val"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_val/"
description: "ldb_val –"
---

<h2 class="name">NAME</h2>
<p> ldb_val &#8211; </p>
<p> Result value.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ldb.h&gt;</p>
<h3>Data Fields</h3>
<p> uint8_t * <code>data</code> </p>
<p> size_t <code>length</code> </p>
<h2>Detailed Description</h2>
<p> Result value. </p>
<p> An individual lump of data in a result comes in this format. The pointer will usually be to a UTF-8 string if the application is sensible, but it can be to anything you like, including binary data blobs of arbitrary size. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> the data is null (0x00) terminated, but the length does not include the terminator.</dl>
<h2>Field Documentation</h2>
<h3>uint8_t* ldb_val::data</h3>
<p> result data</p>
<h3>size_t ldb_val::length</h3>
<p> length of data </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
