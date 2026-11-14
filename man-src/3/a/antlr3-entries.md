---
title: "antlr3-entries(3)"
name: "antlr3-entries"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-entries/"
description: "ANTLR3_HASH_BUCKET_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_HASH_BUCKET_struct &#8211; </p>
<p> Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>pANTLR3_HASH_ENTRY</code> <code>entries</code><br />
 <i>Pointer to the first entry in the bucket (if any, it may be NULL). </i></p>
<h2>Detailed Description</h2>
<p> Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket.</p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_HASH_ENTRY</code> <code>ANTLR3_HASH_BUCKET_struct::entries</code></h3>
<p> Pointer to the first entry in the bucket (if any, it may be NULL). Duplicate entries are chained from here. </p>
<p> Referenced by antlr3EnumNew(), antlr3EnumNextEntry(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), and antlr3HashTableNew(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
