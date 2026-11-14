---
title: "antlr3-keybase(3)"
name: "antlr3-keybase"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-keybase/"
description: "ANTLR3_HASH_ENTRY_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_HASH_ENTRY_struct &#8211; </p>
<p> Internal structure representing an element in a hash bucket.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Public Member Functions</h3>
<p> <code>void</code> (ANTLR3_CDECL *free)(void *<code>data</code>)<br />
 <i>Pointer to routine that knows how to release the memory structure pointed at by data. </i></p>
<h3>Data Fields</h3>
<p> void * <code>data</code><br />
 <i>Pointer to the data for this particular entry. </i><br />
 <code>ANTLR3_HASH_KEY</code> <code>keybase</code><br />
 <i>Key that created this particular entry. </i><br />
 struct <code>ANTLR3_HASH_ENTRY_struct</code> * <code>nextEntry</code><br />
 <i>Pointer to the next entry in this bucket if there is one. </i></p>
<h2>Detailed Description</h2>
<p> Internal structure representing an element in a hash bucket. </p>
<p> Stores the original key so that duplicate keys can be rejected if necessary, and contains function can be supported. If the hash key could be unique I would have invented the perfect compression algorithm ;-)</p>
<h2>Member Function Documentation</h2>
<h3>ANTLR3_HASH_ENTRY_struct::void (ANTLR3_CDECL * free)</h3>
<p> Pointer to routine that knows how to release the memory structure pointed at by data. If this is NULL then we assume that the data pointer does not need to be freed when the entry is deleted from the table.</p>
<h2>Field Documentation</h2>
<h3>void* <code>ANTLR3_HASH_ENTRY_struct::data</code></h3>
<p> Pointer to the data for this particular entry. </p>
<p> Referenced by antlr3EnumNext(), antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), and antlr3ListRemove().</p>
<h3><code>ANTLR3_HASH_KEY</code> <code>ANTLR3_HASH_ENTRY_struct::keybase</code></h3>
<p> Key that created this particular entry. </p>
<p> Referenced by antlr3EnumNext(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), and antlr3HashRemoveI().</p>
<h3>struct <code>ANTLR3_HASH_ENTRY_struct</code>* <code>ANTLR3_HASH_ENTRY_struct::nextEntry</code> [read]</h3>
<p> Pointer to the next entry in this bucket if there is one. Sometimes different keys will hash to the same bucket (especially if the number of buckets is small). We could implement dual hashing algorithms to minimize this, but that seems over the top for what this is needed for. </p>
<p> Referenced by antlr3EnumNextEntry(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), and antlr3HashRemoveI(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
