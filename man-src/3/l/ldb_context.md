---
title: "ldb_context(3)"
name: "ldb_context"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_context/"
description: "ldb_context –"
---

<h2 class="name">NAME</h2>
<p> ldb_context &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Data Structures</h3>
<p> struct <code>ldb_extended_match_entry</code> </p>
<p> struct <code>ldb_opaque</code> </p>
<h3>Data Fields</h3>
<p> struct <code>ldb_module</code> * <code>modules</code> </p>
<p> struct <code>ldb_debug_ops</code> <code>debug_ops</code> </p>
<p> struct<br />
 <code>ldb_context::ldb_extended_match_entry</code> * <code>extended_match_rules</code>&quot; </p>
<p> struct <code>ldb_utf8_fns</code> <code>utf8_fns</code> </p>
<p> struct <code>ldb_context::ldb_opaque</code> * <code>opaque</code> </p>
<p> struct <code>ldb_schema</code> <code>schema</code> </p>
<p> char * <code>err_string</code> </p>
<p> int <code>transaction_active</code> </p>
<p> int <code>default_timeout</code> </p>
<p> unsigned int <code>flags</code> </p>
<p> unsigned int <code>create_perms</code> </p>
<p> struct tevent_context * <code>ev_ctx</code> </p>
<p> bool <code>prepare_commit_done</code> </p>
<p> char * <code>partial_debug</code> </p>
<p> struct poptOption * <code>popt_options</code> </p>
<h2>Detailed Description</h2>
<p> <code>Examples: </code> <code>ldbreader.c</code>, and <code>ldifreader.c</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
