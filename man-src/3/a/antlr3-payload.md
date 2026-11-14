---
title: "antlr3-payload(3)"
name: "antlr3-payload"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-payload/"
description: "ANTLR3_PARSE_TREE_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_PARSE_TREE_struct &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3parsetree.h">antlr3parsetree.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_BASE_TREE</code> <code>baseTree</code><br />
 <i>An encapsulated BASE TREE strcuture (NOT a pointer) that perfoms a lot of the dirty work of node management. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>dupNode</code> )(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree)<br />
 <i>How to dup this node. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getType</code> )(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree)<br />
 <i>Return the type of this node. </i><br />
 void * <code>payload</code><br />
 <i>The payload that the parse tree node passes around. </i><br />
 void * <code>super</code><br />
 <i>Any interface that implements methods in this interface may need to point back to itself using this pointer to its super structure. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toString</code> )(struct <code>ANTLR3_PARSE_TREE_struct</code> *<code>payload</code>)<br />
 <i>Return the string representation of the payload (must be installed when the payload is added and point to a function that knwos how to manifest a pANTLR3_STRING from a node. </i></p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_BASE_TREE</code> <code>ANTLR3_PARSE_TREE_struct::baseTree</code></h3>
<p> An encapsulated BASE TREE strcuture (NOT a pointer) that perfoms a lot of the dirty work of node management.</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_PARSE_TREE_struct::dupNode</code>)(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree)</h3>
<p> How to dup this node.</p>
<h3>void(* <code>ANTLR3_PARSE_TREE_struct::free</code>)(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree)</h3>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_PARSE_TREE_struct::getType</code>)(struct <code>ANTLR3_PARSE_TREE_struct</code> *tree)</h3>
<p> Return the type of this node.</p>
<h3>void* <code>ANTLR3_PARSE_TREE_struct::payload</code></h3>
<p> The payload that the parse tree node passes around.</p>
<h3>void* <code>ANTLR3_PARSE_TREE_struct::super</code></h3>
<p> Any interface that implements methods in this interface may need to point back to itself using this pointer to its super structure.</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_PARSE_TREE_struct::toString</code>)(struct <code>ANTLR3_PARSE_TREE_struct</code> *<code>payload</code>)</h3>
<p> Return the string representation of the payload (must be installed when the payload is added and point to a function that knwos how to manifest a pANTLR3_STRING from a node. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
