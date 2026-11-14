---
title: "antlr3_list_struct(3)"
name: "antlr3_list_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_list_struct/"
description: "ANTLR3_LIST_struct –"
---

<p>ANTLR3_LIST_struct &#8211; </p>
<p> Structure that represents a LIST collection.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_INT32</code>(* <code>add</code> )(struct <code>ANTLR3_LIST_struct</code> *list, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> void(* <code>del</code> )(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_LIST_struct</code> *list) </p>
<p> void *(* <code>get</code> )(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>ANTLR3_INT32</code>(* <code>put</code> )(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> void *(* <code>remove</code> )(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_LIST_struct</code> *list) </p>
<p> <code>pANTLR3_HASH_TABLE</code> <code>table</code><br />
 <i>Hash table that is storing the list elements. </i></p>
<h2>Detailed Description</h2>
<p>Structure that represents a LIST collection.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_LIST_struct::add</code>)(struct <code>ANTLR3_LIST_struct</code> *list, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p>Referenced by antlr3ListNew().</p>
<h3>void(* <code>ANTLR3_LIST_struct::del</code>)(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key)</h3>
<p>Referenced by antlr3ListNew().</p>
<h3>void(* <code>ANTLR3_LIST_struct::free</code>)(struct <code>ANTLR3_LIST_struct</code> *list)</h3>
<p>Referenced by antlr3CTSFree(), antlr3ListNew(), and getTokensSet().</p>
<h3>void*(* <code>ANTLR3_LIST_struct::get</code>)(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key)</h3>
<p>Referenced by addChildren(), and antlr3ListNew().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_LIST_struct::put</code>)(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p>Referenced by antlr3ListAdd(), antlr3ListNew(), discardTokenType(), getTokensSet(), and setTokenTypeChannel().</p>
<h3>void*(* <code>ANTLR3_LIST_struct::remove</code>)(struct <code>ANTLR3_LIST_struct</code> *list, <code>ANTLR3_INTKEY</code> key)</h3>
<p>Referenced by antlr3ListNew().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_LIST_struct::size</code>)(struct <code>ANTLR3_LIST_struct</code> *list)</h3>
<p>Referenced by addChildren(), antlr3ListNew(), and getTokensSet().</p>
<h3><code>pANTLR3_HASH_TABLE</code> <code>ANTLR3_LIST_struct::table</code></h3>
<p>Hash table that is storing the list elements. </p>
<p> Referenced by antlr3ListAdd(), antlr3ListDelete(), antlr3ListFree(), antlr3ListGet(), antlr3ListNew(), antlr3ListPut(), antlr3ListRemove(), antlr3ListSize(), and getTokensList(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
