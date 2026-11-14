---
title: "ldb_vlv_req_control(3)"
name: "ldb_vlv_req_control"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_vlv_req_control/"
description: "ldb_vlv_req_control –"
---

<h2 class="name">NAME</h2>
<p> ldb_vlv_req_control &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> int <code>beforeCount</code> </p>
<p> int <code>afterCount</code> </p>
<p> int <code>type</code> </p>
<p> union { </p>
<p> struct { </p>
<p> int <code>offset</code> </p>
<p> int <code>contentCount</code> </p>
<p> } <code>byOffset</code> </p>
<p> struct { </p>
<p> int <code>value_len</code> </p>
<p> char * <code>value</code> </p>
<p> } <code>gtOrEq</code> </p>
<p> } <code>match</code> </p>
<p> int <code>ctxid_len</code> </p>
<p> char * <code>contextId</code> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
