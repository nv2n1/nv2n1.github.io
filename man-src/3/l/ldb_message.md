---
title: "ldb_message(3)"
name: "ldb_message"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_message/"
description: "ldb_message –"
---

<h2 class="name">NAME</h2>
<p> ldb_message &#8211; </p>
<p> a <code>ldb_message</code> represents all or part of a record.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ldb.h&gt;</p>
<h3>Data Fields</h3>
<p> struct ldb_dn * <code>dn</code> </p>
<p> unsigned int <code>num_elements</code> </p>
<p> struct <code>ldb_message_element</code> * <code>elements</code> </p>
<h2>Detailed Description</h2>
<p> a <code>ldb_message</code> represents all or part of a record. </p>
<p> It can contain an arbitrary number of elements. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
