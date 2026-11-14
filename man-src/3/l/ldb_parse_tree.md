---
title: "ldb_parse_tree(3)"
name: "ldb_parse_tree"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_parse_tree/"
description: "ldb_parse_tree –"
---

<h2 class="name">NAME</h2>
<p> ldb_parse_tree &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> enum ldb_parse_op <code>operation</code> </p>
<p> union { </p>
<p> struct { </p>
<p> struct <code>ldb_parse_tree</code> * <code>child</code> </p>
<p> } <code>isnot</code> </p>
<p> struct { </p>
<p> const char * <code>attr</code> </p>
<p> struct <code>ldb_val</code> <code>value</code> </p>
<p> } <code>equality</code> </p>
<p> struct { </p>
<p> const char * <code>attr</code> </p>
<p> int <code>start_with_wildcard</code> </p>
<p> int <code>end_with_wildcard</code> </p>
<p> struct <code>ldb_val</code> ** <code>chunks</code> </p>
<p> } <code>substring</code> </p>
<p> struct { </p>
<p> const char * <code>attr</code> </p>
<p> } <code>present</code> </p>
<p> struct { </p>
<p> const char * <code>attr</code> </p>
<p> struct <code>ldb_val</code> <code>value</code> </p>
<p> } <code>comparison</code> </p>
<p> struct { </p>
<p> const char * <code>attr</code> </p>
<p> int <code>dnAttributes</code> </p>
<p> const char * <code>rule_id</code> </p>
<p> struct <code>ldb_val</code> <code>value</code> </p>
<p> } <code>extended</code> </p>
<p> struct { </p>
<p> unsigned int <code>num_elements</code> </p>
<p> struct <code>ldb_parse_tree</code> ** <code>elements</code> </p>
<p> } <code>list</code> </p>
<p> } <code>u</code> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
