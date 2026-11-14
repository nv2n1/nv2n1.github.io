---
title: "antlr3basetree(3)"
name: "antlr3basetree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3basetree/"
description: "include/antlr3basetree.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3basetree.h &#8211; </p>
<p> Definition of the ANTLR3 base tree.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_BASE_TREE_struct</code><br />
 <i>A generic tree implementation with no payload. </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_BASE_TREE_struct</code> <code>ANTLR3_BASE_TREE</code><br />
 <i>A generic tree implementation with no payload. </i></p>
<h2>Detailed Description</h2>
<p> Definition of the ANTLR3 base tree. </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_BASE_TREE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_BASE_TREE</code>&quot; </p>
<p> A generic tree implementation with no payload. You must subclass to actually have any user data. ANTLR v3 uses a list of children approach instead of the child-sibling approach in v2. A flat tree (a list) is an empty node whose children represent the list. An empty (as in it does not have payload itself), but non-null node is called &#8216;nil&#8217;.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
