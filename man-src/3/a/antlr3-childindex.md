---
title: "antlr3-childindex(3)"
name: "antlr3-childindex"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-childindex/"
description: "ANTLR3_COMMON_TREE_struct –"
---

<p>ANTLR3_COMMON_TREE_struct &#8211; </p>
<p> Interface for an ANTLR3 common tree which is what gets passed around by the AST producing parser.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontree.h">antlr3commontree.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_BASE_TREE</code> <code>baseTree</code><br />
 <i>An encapsulated BASE TREE structure (NOT a pointer) that performs a lot of the dirty work of node management To this we add just a few functions that are specific to the payload. </i><br />
 <code>ANTLR3_INT32</code> <code>childIndex</code><br />
 <i>What index is this particular node in the child list it belongs to? </i><br />
 <code>pANTLR3_ARBORETUM</code> <code>factory</code><br />
 <i>Pointer to the tree factory that manufactured this token. </i><br />
 <code>pANTLR3_COMMON_TREE</code> <code>parent</code><br />
 <i>Points to the node that has this node as a child. </i><br />
 <code>ANTLR3_MARKER</code> <code>startIndex</code><br />
 <i>Start token index that encases this tree. </i><br />
 <code>ANTLR3_MARKER</code> <code>stopIndex</code><br />
 <i>End token that encases this tree. </i><br />
 void * <code>super</code><br />
 <i>Not used by ANTLR, but if a super structure is created above this structure, it can be used to point to the start of the super structure, where additional data and function pointers can be stored. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code> <code>token</code><br />
 <i>A single token, this is the payload for the tree. </i></p>
<h2>Detailed Description</h2>
<p> Interface for an ANTLR3 common tree which is what gets passed around by the AST producing parser.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_BASE_TREE</code> <code>ANTLR3_COMMON_TREE_struct::baseTree</code></h3>
<p> An encapsulated BASE TREE structure (NOT a pointer) that performs a lot of the dirty work of node management To this we add just a few functions that are specific to the payload. You can further abstract common tree so long as you always have a baseTree pointer in the top structure and copy it from the next one down. So, lets say we have a structure JIMS_TREE. It needs an ANTLR3_BASE_TREE that will support all the general tree duplication stuff. It needs a ANTLR3_COMMON_TREE structure embedded or completely provides the equivalent interface. It provides it&#8217;s own methods and data. To create a new one of these, the function provided to the tree adaptor (see comments there) should allocate the memory for a new JIMS_TREE structure, then call antlr3InitCommonTree(&lt;addressofembeddedCOMMON_TREE&gt;) antlr3BaseTreeNew(&lt;addressofBASETREE&gt;) The interfaces for BASE_TREE and COMMON_TREE will then be initialized. You then call and you can override them or just init JIMS_TREE (note that the base tree in common tree will be ignored) just the top level base tree is used). Codegen will take care of the rest. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3SetCTAPI(), getMissingSymbol(), LB(), newFromTree(), newPoolTree(), and reuse().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_COMMON_TREE_struct::childIndex</code></h3>
<p> What index is this particular node in the child list it belongs to? </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3><code>pANTLR3_ARBORETUM</code> <code>ANTLR3_COMMON_TREE_struct::factory</code></h3>
<p> Pointer to the tree factory that manufactured this token. This can be used by duplication methods and so on to manufacture another auto-tracked common tree structure </p>
<p> Referenced by antlr3ArboretumNew(), dupNode(), newPoolTree(), and reuse().</p>
<h3><code>pANTLR3_COMMON_TREE</code> <code>ANTLR3_COMMON_TREE_struct::parent</code></h3>
<p> Points to the node that has this node as a child. If this is NULL, then this is the root node. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TREE_struct::startIndex</code></h3>
<p> Start token index that encases this tree. </p>
<p> Referenced by antlr3SetCTAPI(), and setTokenBoundaries().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TREE_struct::stopIndex</code></h3>
<p> End token that encases this tree. </p>
<p> Referenced by antlr3SetCTAPI(), and setTokenBoundaries().</p>
<h3>void* <code>ANTLR3_COMMON_TREE_struct::super</code></h3>
<p> Not used by ANTLR, but if a super structure is created above this structure, it can be used to point to the start of the super structure, where additional data and function pointers can be stored.</p>
<h3><code>pANTLR3_COMMON_TOKEN</code> <code>ANTLR3_COMMON_TREE_struct::token</code></h3>
<p> A single token, this is the payload for the tree. </p>
<p> Referenced by antlr3CommonTreeNewFromToken(), antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3RecognitionExceptionNew(), antlr3SetCTAPI(), getLine(), getType(), and newFromTree(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code.</p>
