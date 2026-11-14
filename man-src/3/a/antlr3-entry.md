---
title: "antlr3-entry(3)"
name: "antlr3-entry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-entry/"
description: "ANTLR3_HASH_ENUM_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_HASH_ENUM_struct &#8211; </p>
<p> Internal structure representing an enumeration of a table.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_UINT32</code> <code>bucket</code> </p>
<p> <code>pANTLR3_HASH_ENTRY</code> <code>entry</code> </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_HASH_ENUM_struct</code> *<code>table</code>) </p>
<p> int(* <code>next</code> )(struct <code>ANTLR3_HASH_ENUM_struct</code> *en, <code>pANTLR3_HASH_KEY</code> *key, void **data) </p>
<p> <code>pANTLR3_HASH_TABLE</code> <code>table</code> </p>
<h2>Detailed Description</h2>
<p> Internal structure representing an enumeration of a table. </p>
<p> This is returned by antlr3Enumeration() Allows the programmer to traverse the table in hash order without knowing what is in the actual table. </p>
<p> Note that it is up to the caller to ensure that the table structure does not change in the hash bucket that is currently being enumerated as this structure just tracks the next pointers in the bucket series.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_HASH_ENUM_struct::bucket</code></h3>
<p> Referenced by antlr3EnumNew(), antlr3EnumNext(), and antlr3EnumNextEntry().</p>
<h3><code>pANTLR3_HASH_ENTRY</code> <code>ANTLR3_HASH_ENUM_struct::entry</code></h3>
<p> Referenced by antlr3EnumNew(), antlr3EnumNext(), and antlr3EnumNextEntry().</p>
<h3>void(* <code>ANTLR3_HASH_ENUM_struct::free</code>)(struct <code>ANTLR3_HASH_ENUM_struct</code> *<code>table</code>)</h3>
<p> Referenced by antlr3BitsetList(), and antlr3EnumNew().</p>
<h3>int(* <code>ANTLR3_HASH_ENUM_struct::next</code>)(struct <code>ANTLR3_HASH_ENUM_struct</code> *en, <code>pANTLR3_HASH_KEY</code> *key, void **data)</h3>
<p> Referenced by antlr3BitsetList(), and antlr3EnumNew().</p>
<h3><code>pANTLR3_HASH_TABLE</code> <code>ANTLR3_HASH_ENUM_struct::table</code></h3>
<p> Referenced by antlr3EnumNew(), antlr3EnumNext(), and antlr3EnumNextEntry(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
