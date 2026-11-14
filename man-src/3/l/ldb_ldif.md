---
title: "ldb_ldif(3)"
name: "ldb_ldif"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_ldif/"
description: "ldb_ldif –"
---

<h2 class="name">NAME</h2>
<p> ldb_ldif &#8211; </p>
<p> LDIF record.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ldb.h&gt;</p>
<h3>Data Fields</h3>
<p> enum ldb_changetype <code>changetype</code> </p>
<p> struct <code>ldb_message</code> * <code>msg</code> </p>
<h2>Detailed Description</h2>
<p> LDIF record. </p>
<p> This structure contains a LDIF record, as returned from ldif_read() and equivalent functions. </p>
<p> <code>Examples: </code> <code>ldbreader.c</code>, and <code>ldifreader.c</code>.</p>
<h2>Field Documentation</h2>
<h3>enum ldb_changetype ldb_ldif::changetype</h3>
<p> The type of change </p>
<p> <code>Examples: </code> <code>ldifreader.c</code>.</p>
<h3>struct <code>ldb_message</code>* ldb_ldif::msg</h3>
<p> The changes </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
