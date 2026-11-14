---
title: "antlr3-children(3)"
name: "antlr3-children"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-children/"
description: "ANTLR3_BASE_TREE_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_BASE_TREE_struct &#8211; </p>
<p> A generic tree implementation with no payload.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3basetree.h">antlr3basetree.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> void(* <code>addChild</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, void *child) </p>
<p> void(* <code>addChildren</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>pANTLR3_LIST</code> kids) </p>
<p> <code>pANTLR3_VECTOR</code> <code>children</code><br />
 <i>The list of all the children that belong to this node. </i><br />
 void(* <code>createChildrenList</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void *(* <code>deleteChild</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i) </p>
<p> void *(* <code>dupNode</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *<code>dupNode</code>) </p>
<p> void *(* <code>dupTree</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void(* <code>freshenPACIndexes</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> offset) </p>
<p> void(* <code>freshenPACIndexesAll</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getCharPositionInLine</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void *(* <code>getChild</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getChildCount</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>ANTLR3_INT32</code>(* <code>getChildIndex</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void *(* <code>getFirstChildWithType</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> type) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getLine</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> struct <code>ANTLR3_BASE_TREE_struct</code> *(* <code>getParent</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>pANTLR3_STRING</code>(* <code>getText</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>pANTLR3_COMMON_TOKEN</code>(* <code>getToken</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)<br />
 <i>A pointer to a function that returns the common token pointer for the payload in the supplied tree. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getType</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>isNilNode</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void(* <code>replaceChildren</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, struct <code>ANTLR3_BASE_TREE_struct</code> *t) </p>
<p> void(* <code>reuse</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>ANTLR3_MARKER</code> <code>savedIndex</code><br />
 <i>This is used to store the current child index position while descending and ascending trees as the tree walk progresses. </i><br />
 void(* <code>setChild</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i, void *child) </p>
<p> void(* <code>setChildIndex</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_INT32</code>) </p>
<p> void(* <code>setParent</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, struct <code>ANTLR3_BASE_TREE_struct</code> *parent) </p>
<p> <code>pANTLR3_STRING_FACTORY</code> <code>strFactory</code><br />
 <i>A string factory to produce strings for toString etc. </i><br />
 void * <code>super</code><br />
 <i>Implementers of this interface sometimes require a pointer to their selves. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toString</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> <code>pANTLR3_STRING</code>(* <code>toStringTree</code> )(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) </p>
<p> void * <code>u</code><br />
 <i>Generic void pointer allows the grammar programmer to attach any structure they like to a tree node, in many cases saving the need to create their own tree and tree adaptors. </i></p>
<h2>Detailed Description</h2>
<p> A generic tree implementation with no payload. </p>
<p> You must subclass to actually have any user data. ANTLR v3 uses a list of children approach instead of the child-sibling approach in v2. A flat tree (a list) is an empty node whose children represent the list. An empty (as in it does not have payload itself), but non-null node is called &#8216;nil&#8217;.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::addChild</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, void *child)</h3>
<p> Referenced by addChild(), addChildren(), antlr3BaseTreeNew(), becomeRoot(), dbgAddChild(), and dupTree().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::addChildren</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>pANTLR3_LIST</code> kids)</h3>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_BASE_TREE_struct::children</code></h3>
<p> The list of all the children that belong to this node. They are not part of the node as they belong to the common tree node that implements this. </p>
<p> Referenced by addChild(), antlr3BaseTreeNew(), antlr3SetCTAPI(), createChildrenList(), deleteChild(), dupTree(), getChild(), getChildCount(), getFirstChildWithType(), replaceChildren(), reuse(), setChild(), and toStringTree().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::createChildrenList</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by addChild(), antlr3SetCTAPI(), and setChild().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_struct::deleteChild</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i)</h3>
<p> Referenced by antlr3BaseTreeNew(), and deleteChild().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_struct::dupNode</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *<code>dupNode</code>)</h3>
<p> Referenced by antlr3SetCTAPI(), dupNode(), dupTree(), dupTreeTT(), and getMissingSymbol().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_struct::dupTree</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew(), and dupTree().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::free</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by addChild(), and antlr3SetCTAPI().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::freshenPACIndexes</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> offset)</h3>
<p> Referenced by antlr3BaseTreeNew(), freshenPACIndexesAll(), and replaceChildren().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::freshenPACIndexesAll</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_struct::getCharPositionInLine</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew(), antlr3SetCTAPI(), displayRecognitionError(), and getCharPositionInLine().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_struct::getChild</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i)</h3>
<p> Referenced by antlr3BaseTreeNew(), becomeRoot(), freshenPACIndexes(), getCharPositionInLine(), getChild(), getLine(), and rulePostProcessing().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_struct::getChildCount</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew(), becomeRoot(), fillBuffer(), freshenPACIndexes(), getCharPositionInLine(), getChildCount(), getLine(), and rulePostProcessing().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_BASE_TREE_struct::getChildIndex</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3SetCTAPI(), dupTreeTT(), and getChildIndex().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_struct::getFirstChildWithType</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> type)</h3>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_struct::getLine</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew(), antlr3SetCTAPI(), and getLine().</p>
<h3>struct <code>ANTLR3_BASE_TREE_struct</code>*(* <code>ANTLR3_BASE_TREE_struct::getParent</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree) [read]</h3>
<p> Referenced by antlr3SetCTAPI(), and getParent().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_BASE_TREE_struct::getText</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3SetCTAPI(), getText(), and replaceChildren().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_BASE_TREE_struct::getToken</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> A pointer to a function that returns the common token pointer for the payload in the supplied tree. </p>
<p> Referenced by antlr3SetCTAPI(), displayRecognitionError(), and getMissingSymbol().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_struct::getType</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3SetCTAPI(), getFirstChildWithType(), and getType().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_TREE_struct::isNilNode</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by addChild(), antlr3SetCTAPI(), becomeRoot(), freeNodeRS(), isNilNode(), replaceChildren(), rulePostProcessing(), toString(), and toStringTree().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::replaceChildren</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, struct <code>ANTLR3_BASE_TREE_struct</code> *t)</h3>
<p> Referenced by antlr3BaseTreeNew(), and replaceChildren().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::reuse</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3SetCTAPI(), becomeRoot(), and rulePostProcessing().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_BASE_TREE_struct::savedIndex</code></h3>
<p> This is used to store the current child index position while descending and ascending trees as the tree walk progresses.</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::setChild</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_UINT32</code> i, void *child)</h3>
<p> Referenced by antlr3BaseTreeNew(), and setChild().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::setChildIndex</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, <code>ANTLR3_INT32</code>)</h3>
<p> Referenced by antlr3SetCTAPI(), freshenPACIndexes(), replaceChildren(), rulePostProcessing(), and setChildIndex().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_struct::setParent</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree, struct <code>ANTLR3_BASE_TREE_struct</code> *parent)</h3>
<p> Referenced by antlr3SetCTAPI(), freshenPACIndexes(), replaceChildren(), rulePostProcessing(), and setParent().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_BASE_TREE_struct::strFactory</code></h3>
<p> A string factory to produce strings for toString etc. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3BaseTreeNew(), antlr3CommonTreeNodeStreamNewTree(), newPoolTree(), toString(), and toStringTree().</p>
<h3>void* <code>ANTLR3_BASE_TREE_struct::super</code></h3>
<p> Implementers of this interface sometimes require a pointer to their selves. </p>
<p> Referenced by antlr3SetCTAPI(), createChildrenList(), displayRecognitionError(), dupNode(), getCharPositionInLine(), getChildIndex(), getLine(), getMissingSymbol(), getParent(), getToken(), getTokenStartIndex(), getTokenStopIndex(), getType(), isNilNode(), newFromToken(), newFromTree(), newPoolTree(), reuse(), setChildIndex(), setParent(), setTokenBoundaries(), and toString().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_BASE_TREE_struct::toString</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3SetCTAPI(), getText(), and toStringTree().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_BASE_TREE_struct::toStringTree</code>)(struct <code>ANTLR3_BASE_TREE_struct</code> *tree)</h3>
<p> Referenced by antlr3BaseTreeNew(), displayRecognitionError(), and toStringTree().</p>
<h3>void* <code>ANTLR3_BASE_TREE_struct::u</code></h3>
<p> Generic void pointer allows the grammar programmer to attach any structure they like to a tree node, in many cases saving the need to create their own tree and tree adaptors. ANTLR does not use this pointer, but will copy it for you and so on. </p>
<p> Referenced by newFromTree(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBM">Author</a></p>
<dd></dl>
