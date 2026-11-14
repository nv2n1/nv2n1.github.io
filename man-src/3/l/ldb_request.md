---
title: "ldb_request(3)"
name: "ldb_request"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_request/"
description: "ldb_request –"
---

<h2 class="name">NAME</h2>
<p> ldb_request &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> enum ldb_request_type <code>operation</code> </p>
<p> union { </p>
<p> struct <code>ldb_search</code> <code>search</code> </p>
<p> struct <code>ldb_add</code> <code>add</code> </p>
<p> struct <code>ldb_modify</code> <code>mod</code> </p>
<p> struct <code>ldb_delete</code> <code>del</code> </p>
<p> struct <code>ldb_rename</code> <code>rename</code> </p>
<p> struct <code>ldb_extended</code> <code>extended</code> </p>
<p> struct <code>ldb_register_control</code> <code>reg_control</code> </p>
<p> struct <code>ldb_register_partition</code> <code>reg_partition</code> </p>
<p> } <code>op</code> </p>
<p> struct <code>ldb_control</code> ** <code>controls</code> </p>
<p> void * <code>context</code> </p>
<p> ldb_request_callback_t <code>callback</code> </p>
<p> int <code>timeout</code> </p>
<p> time_t <code>starttime</code> </p>
<p> struct <code>ldb_handle</code> * <code>handle</code> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
