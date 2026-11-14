---
title: "antlr3-duptree(3)"
name: "antlr3-duptree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-duptree/"
description: "src/antlr3basetree.c –"
---

<p>src/antlr3basetree.c &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3basetree.h">antlr3basetree.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>addChild</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_BASE_TREE</code> child) </p>
<p> static void <code>addChildren</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_LIST</code> kids)<br />
 <i>Add all elements of the supplied list as children of this node. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_TREE</code> <code>antlr3BaseTreeNew</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static void * <code>deleteChild</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i) </p>
<p> static void * <code>dupTree</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static void <code>freshenPACIndexes</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> offset)<br />
 <i>Set the parent and child indexes for some of the children of the supplied tree, starting with the child at the supplied index. </i><br />
 static void <code>freshenPACIndexesAll</code> (<code>pANTLR3_BASE_TREE</code> tree)<br />
 <i>Set the parent and child indexes for all children of the supplied tree. </i><br />
 static <code>ANTLR3_UINT32</code> <code>getCharPositionInLine</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static void * <code>getChild</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getChildCount</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getFirstChildWithType</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> type) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getLine</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static void <code>replaceChildren</code> (<code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> newTree)<br />
 <i>Delete children from start to stop and replace with t even if t is a list (nil-root tree). </i><br />
 static void <code>setChild</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i, void *child) </p>
<p> static <code>pANTLR3_STRING</code> <code>toStringTree</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<h2>Function Documentation</h2>
<h3>void addChild (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p>References ANTLR3_VECTOR_struct::add, ANTLR3_CDECL, ANTLR3_FPRINTF, ANTLR3_TRUE, ANTLR3_BASE_TREE_struct::children, ANTLR3_BASE_TREE_struct::createChildrenList, ANTLR3_BASE_TREE_struct::free, freshenPACIndexesAll(), ANTLR3_VECTOR_struct::get, ANTLR3_BASE_TREE_struct::isNilNode, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static void addChildren (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_LIST</code> kids) [static]</h3>
<p>Add all elements of the supplied list as children of this node. </p>
<p> References ANTLR3_BASE_TREE_struct::addChild, ANTLR3_LIST_struct::get, and ANTLR3_LIST_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE</code> antlr3BaseTreeNew (<code>pANTLR3_BASE_TREE</code> tree)</h3>
<p>References addChild(), ANTLR3_BASE_TREE_struct::addChild, addChildren(), ANTLR3_BASE_TREE_struct::addChildren, ANTLR3_BASE_TREE_struct::children, deleteChild(), ANTLR3_BASE_TREE_struct::deleteChild, dupTree(), ANTLR3_BASE_TREE_struct::dupTree, freshenPACIndexes(), ANTLR3_BASE_TREE_struct::freshenPACIndexes, freshenPACIndexesAll(), ANTLR3_BASE_TREE_struct::freshenPACIndexesAll, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChild(), ANTLR3_BASE_TREE_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_struct::getChildCount, getFirstChildWithType(), ANTLR3_BASE_TREE_struct::getFirstChildWithType, getLine(), ANTLR3_BASE_TREE_struct::getLine, replaceChildren(), ANTLR3_BASE_TREE_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_struct::setChild, ANTLR3_BASE_TREE_struct::strFactory, toStringTree(), and ANTLR3_BASE_TREE_struct::toStringTree. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static void * deleteChild (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::children, and ANTLR3_VECTOR_struct::remove. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static void * dupTree (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::addChild, ANTLR3_BASE_TREE_struct::children, ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_BASE_TREE_struct::dupTree, ANTLR3_VECTOR_struct::get, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static void freshenPACIndexes (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> offset) [static]</h3>
<p>Set the parent and child indexes for some of the children of the supplied tree, starting with the child at the supplied index. </p>
<p> References ANTLR3_BASE_TREE_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, ANTLR3_BASE_TREE_struct::setChildIndex, and ANTLR3_BASE_TREE_struct::setParent. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static void freshenPACIndexesAll (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Set the parent and child indexes for all children of the supplied tree. </p>
<p> References ANTLR3_BASE_TREE_struct::freshenPACIndexes. </p>
<p> Referenced by addChild(), and antlr3BaseTreeNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getCharPositionInLine (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Referenced by antlr3BaseTreeNew(), and antlr3RecognitionExceptionNew().</p>
<h3>static void * getChild (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::children, ANTLR3_VECTOR_struct::get, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getChildCount (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::children, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getFirstChildWithType (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> type) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::children, ANTLR3_VECTOR_struct::get, ANTLR3_BASE_TREE_struct::getType, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getLine (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Referenced by antlr3BaseTreeNew(), and antlr3RecognitionExceptionNew().</p>
<h3>static void replaceChildren (<code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> newTree) [static]</h3>
<p>Delete children from start to stop and replace with t even if t is a list (nil-root tree). Num of children can increase or decrease. For huge child lists, inserting children can force walking rest of children to set their child index; could be slow. </p>
<p> References ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_FREE, ANTLR3_TRUE, antlr3VectorNew(), ANTLR3_STRING_struct::chars, ANTLR3_BASE_TREE_struct::children, ANTLR3_VECTOR_struct::elements, ANTLR3_BASE_TREE_struct::freshenPACIndexes, ANTLR3_VECTOR_struct::get, ANTLR3_BASE_TREE_struct::getText, ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_VECTOR_struct::remove, ANTLR3_VECTOR_struct::set, ANTLR3_BASE_TREE_struct::setChildIndex, ANTLR3_BASE_TREE_struct::setParent, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static void setChild (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> i, void * child) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_BASE_TREE_struct::children, ANTLR3_BASE_TREE_struct::createChildrenList, and ANTLR3_VECTOR_struct::set. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h3>static <code>pANTLR3_STRING</code> toStringTree (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_STRING_struct::append8, ANTLR3_BASE_TREE_struct::children, ANTLR3_VECTOR_struct::get, ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_STRING_FACTORY_struct::newRaw, ANTLR3_VECTOR_struct::size, ANTLR3_BASE_TREE_struct::strFactory, ANTLR3_BASE_TREE_struct::toString, and ANTLR3_BASE_TREE_struct::toStringTree. </p>
<p> Referenced by antlr3BaseTreeNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
