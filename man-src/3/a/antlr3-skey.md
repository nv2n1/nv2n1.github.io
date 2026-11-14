---
title: "antlr3-skey(3)"
name: "antlr3-skey"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-skey/"
description: "ANTLR3_HASH_KEY_struct –"
---

<p>ANTLR3_HASH_KEY_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>union { </p>
<p> <code>ANTLR3_INTKEY</code> <code>iKey</code><br />
 <i>used if type is ANTLR3_HASH_TYPE_INT </i><br />
 <code>pANTLR3_UINT8</code> <code>sKey</code><br />
 <i>Used if type is ANTLR3_HASH_TYPE_STR. </i><br />
 } <code>key</code> </p>
<p> <code>ANTLR3_UINT8</code> <code>type</code><br />
 <i>One of #</i><code>ANTLR3_HASH_TYPE_INT</code> or #<code>ANTLR3_HASH_TYPE_STR</code>.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_INTKEY</code> <code>ANTLR3_HASH_KEY_struct::iKey</code></h3>
<p>used if type is ANTLR3_HASH_TYPE_INT </p>
<p> Referenced by antlr3HashGetI(), antlr3HashPutI(), and antlr3HashRemoveI().</p>
<h3>union { &#8230; }</h3>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>ANTLR3_HASH_KEY_struct::key</code>&quot;</p>
<p> Referenced by antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), and antlr3HashRemoveI().</p>
<h3><code>pANTLR3_UINT8</code> <code>ANTLR3_HASH_KEY_struct::sKey</code></h3>
<p>Used if type is ANTLR3_HASH_TYPE_STR. </p>
<p> Referenced by antlr3HashFree(), antlr3HashGet(), antlr3HashPut(), and antlr3HashRemove().</p>
<h3><code>ANTLR3_UINT8</code> <code>ANTLR3_HASH_KEY_struct::type</code></h3>
<p>One of #<code>ANTLR3_HASH_TYPE_INT</code> or #<code>ANTLR3_HASH_TYPE_STR</code>. </p>
<p> Referenced by antlr3HashFree(), antlr3HashPut(), and antlr3HashPutI(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
