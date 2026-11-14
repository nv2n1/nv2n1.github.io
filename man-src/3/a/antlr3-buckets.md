---
title: "antlr3-buckets(3)"
name: "antlr3-buckets"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-buckets/"
description: "ANTLR3_HASH_TABLE_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_HASH_TABLE_struct &#8211; </p>
<p> Structure that tracks a hash table.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> int <code>allowDups</code><br />
 <i>Indicates whether the table allows duplicate keys. </i><br />
 <code>pANTLR3_HASH_BUCKET</code> <code>buckets</code><br />
 <i>Points to the memory where the array of buckets starts. </i><br />
 <code>ANTLR3_UINT32</code> <code>count</code><br />
 <i>How many elements currently exist in the table. </i><br />
 void(* <code>del</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key) </p>
<p> void(* <code>delI</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>doStrdup</code><br />
 <i>Whether the hash table should strdup the keys it is given or not. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table)<br />
 <i>Pointer to function to completely delete this table. </i><br />
 void *(* <code>get</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key) </p>
<p> void *(* <code>getI</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>ANTLR3_UINT32</code> <code>modulo</code><br />
 <i>Number of buckets available in this table. </i><br />
 <code>ANTLR3_INT32</code>(* <code>put</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> <code>ANTLR3_INT32</code>(* <code>putI</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> <code>pANTLR3_HASH_ENTRY</code>(* <code>remove</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key) </p>
<p> <code>pANTLR3_HASH_ENTRY</code>(* <code>removeI</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_HASH_TABLE_struct</code> *table) </p>
<h2>Detailed Description</h2>
<p> Structure that tracks a hash table.</p>
<h2>Field Documentation</h2>
<h3>int <code>ANTLR3_HASH_TABLE_struct::allowDups</code></h3>
<p> Indicates whether the table allows duplicate keys. </p>
<p> Referenced by antlr3HashPut(), antlr3HashPutI(), and antlr3HashTableNew().</p>
<h3><code>pANTLR3_HASH_BUCKET</code> <code>ANTLR3_HASH_TABLE_struct::buckets</code></h3>
<p> Points to the memory where the array of buckets starts. </p>
<p> Referenced by antlr3EnumNew(), antlr3EnumNextEntry(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), and antlr3HashTableNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_HASH_TABLE_struct::count</code></h3>
<p> How many elements currently exist in the table. </p>
<p> Referenced by antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), antlr3HashSize(), and antlr3HashTableNew().</p>
<h3>void(* <code>ANTLR3_HASH_TABLE_struct::del</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key)</h3>
<p> Referenced by antlr3HashTableNew().</p>
<h3>void(* <code>ANTLR3_HASH_TABLE_struct::delI</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key)</h3>
<p> Referenced by antlr3HashTableNew(), and antlr3ListDelete().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_HASH_TABLE_struct::doStrdup</code></h3>
<p> Whether the hash table should strdup the keys it is given or not. </p>
<p> Referenced by antlr3HashPut(), antlr3HashRemove(), and antlr3HashTableNew().</p>
<h3>void(* <code>ANTLR3_HASH_TABLE_struct::free</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table)</h3>
<p> Pointer to function to completely delete this table. </p>
<p> Referenced by antlr3HashTableNew(), and antlr3ListFree().</p>
<h3>void*(* <code>ANTLR3_HASH_TABLE_struct::get</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key)</h3>
<p> Referenced by antlr3HashTableNew().</p>
<h3>void*(* <code>ANTLR3_HASH_TABLE_struct::getI</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key)</h3>
<p> Referenced by antlr3HashTableNew(), and antlr3ListGet().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_HASH_TABLE_struct::modulo</code></h3>
<p> Number of buckets available in this table. </p>
<p> Referenced by antlr3EnumNext(), antlr3EnumNextEntry(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), and antlr3HashTableNew().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_HASH_TABLE_struct::put</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p> Referenced by antlr3HashTableNew().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_HASH_TABLE_struct::putI</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p> Referenced by antlr3HashTableNew(), and antlr3ListPut().</p>
<h3><code>pANTLR3_HASH_ENTRY</code>(* <code>ANTLR3_HASH_TABLE_struct::remove</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, void *key)</h3>
<p> Referenced by antlr3HashTableNew().</p>
<h3><code>pANTLR3_HASH_ENTRY</code>(* <code>ANTLR3_HASH_TABLE_struct::removeI</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table, <code>ANTLR3_INTKEY</code> key)</h3>
<p> Referenced by antlr3HashTableNew(), and antlr3ListRemove().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_HASH_TABLE_struct::size</code>)(struct <code>ANTLR3_HASH_TABLE_struct</code> *table)</h3>
<p> Referenced by antlr3HashTableNew(), antlr3ListAdd(), and antlr3ListSize(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAV">Author</a></p>
<dd></dl>
