---
title: "antlr3-arboretum(3)"
name: "antlr3-arboretum"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-arboretum/"
description: "ANTLR3_COMMON_TREE_ADAPTOR_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_COMMON_TREE_ADAPTOR_struct &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontreeadaptor.h">antlr3commontreeadaptor.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>pANTLR3_ARBORETUM</code> <code>arboretum</code><br />
 <i>Tree factory for producing new nodes as required without needing to track memory allocation per node. </i><br />
 <code>ANTLR3_TREE_ADAPTOR</code> <code>baseAdaptor</code><br />
 <i>Base interface implementation, embedded structure. </i><br />
 void * <code>super</code><br />
 <i>Any enclosing structure/class can use this pointer to point to its own interface. </i></p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_ARBORETUM</code> <code>ANTLR3_COMMON_TREE_ADAPTOR_struct::arboretum</code></h3>
<p> Tree factory for producing new nodes as required without needing to track memory allocation per node. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), and ctaFree().</p>
<h3><code>ANTLR3_TREE_ADAPTOR</code> <code>ANTLR3_COMMON_TREE_ADAPTOR_struct::baseAdaptor</code></h3>
<p> Base interface implementation, embedded structure. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void* <code>ANTLR3_COMMON_TREE_ADAPTOR_struct::super</code></h3>
<p> Any enclosing structure/class can use this pointer to point to its own interface. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
