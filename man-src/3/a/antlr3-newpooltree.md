---
title: "antlr3-newpooltree(3)"
name: "antlr3-newpooltree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-newpooltree/"
description: "src/antlr3commontree.c –"
---

<p>src/antlr3commontree.c &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3commontree.h">antlr3commontree.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_ARBORETUM</code> <code>antlr3ArboretumNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE</code> <code>antlr3CommonTreeNew</code> () </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE</code> <code>antlr3CommonTreeNewFromToken</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> ANTLR3_API void <code>antlr3SetCTAPI</code> (<code>pANTLR3_COMMON_TREE</code> tree) </p>
<p> static void <code>createChildrenList</code> (<code>pANTLR3_BASE_TREE</code> tree)<br />
 <i>Create a new vector for holding child nodes using the inbuilt vector factory. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>dupNode</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static void <code>factoryClose</code> (<code>pANTLR3_ARBORETUM</code> factory) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getCharPositionInLine</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>ANTLR3_INT32</code> <code>getChildIndex</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getLine</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getParent</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>pANTLR3_STRING</code> <code>getText</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>getToken</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getType</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>isNilNode</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>newFromToken</code> (<code>pANTLR3_ARBORETUM</code> factory, <code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>newFromTree</code> (<code>pANTLR3_ARBORETUM</code> factory, <code>pANTLR3_COMMON_TREE</code> tree) </p>
<p> static void <code>newPool</code> (<code>pANTLR3_ARBORETUM</code> factory) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>newPoolTree</code> (<code>pANTLR3_ARBORETUM</code> factory) </p>
<p> static void <code>reuse</code> (<code>pANTLR3_BASE_TREE</code> tree)<br />
 <i>Clean up any child vector that the tree might have, so it can be reused, then add it into the reuse stack. </i><br />
 static void <code>setChildIndex</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_INT32</code> i) </p>
<p> static void <code>setParent</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_BASE_TREE</code> parent) </p>
<p> static <code>pANTLR3_STRING</code> <code>toString</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_ARBORETUM</code> antlr3ArboretumNew (<code>pANTLR3_STRING_FACTORY</code> strFactory)</h3>
<p>References ANTLR3_MALLOC, antlr3SetCTAPI(), antlr3StackNew(), antlr3VectorFactoryNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_ARBORETUM_struct::close, ANTLR3_COMMON_TREE_struct::factory, factoryClose(), ANTLR3_TREE_PARSER_struct::free, newFromToken(), ANTLR3_ARBORETUM_struct::newFromToken, newFromTree(), ANTLR3_ARBORETUM_struct::newFromTree, newPool(), newPoolTree(), ANTLR3_ARBORETUM_struct::newTree, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_ARBORETUM_struct::pools, ANTLR3_BASE_TREE_struct::strFactory, ANTLR3_ARBORETUM_struct::thisPool, ANTLR3_ARBORETUM_struct::unTruc, and ANTLR3_ARBORETUM_struct::vFactory. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE</code> antlr3CommonTreeNew (void)</h3>
<p>References ANTLR3_MALLOC, and antlr3SetCTAPI(). </p>
<p> Referenced by antlr3CommonTreeNewFromToken().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE</code> antlr3CommonTreeNewFromToken (<code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p>References antlr3CommonTreeNew(), and ANTLR3_COMMON_TREE_struct::token.</p>
<h3>ANTLR3_API void antlr3SetCTAPI (<code>pANTLR3_COMMON_TREE</code> tree)</h3>
<p>References antlr3BaseTreeNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_COMMON_TREE_struct::childIndex, ANTLR3_BASE_TREE_struct::children, createChildrenList(), ANTLR3_BASE_TREE_struct::createChildrenList, dupNode(), ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_BASE_TREE_struct::free, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChildIndex(), ANTLR3_BASE_TREE_struct::getChildIndex, getLine(), ANTLR3_BASE_TREE_struct::getLine, getParent(), ANTLR3_BASE_TREE_struct::getParent, getText(), ANTLR3_BASE_TREE_struct::getText, getToken(), ANTLR3_BASE_TREE_struct::getToken, getType(), ANTLR3_BASE_TREE_struct::getType, isNilNode(), ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_COMMON_TREE_struct::parent, reuse(), ANTLR3_BASE_TREE_struct::reuse, setChildIndex(), ANTLR3_BASE_TREE_struct::setChildIndex, setParent(), ANTLR3_BASE_TREE_struct::setParent, ANTLR3_COMMON_TREE_struct::startIndex, ANTLR3_COMMON_TREE_struct::stopIndex, ANTLR3_BASE_TREE_struct::super, ANTLR3_COMMON_TREE_struct::token, toString(), and ANTLR3_BASE_TREE_struct::toString. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3CommonTreeNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and newPoolTree().</p>
<h3>static void createChildrenList (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Create a new vector for holding child nodes using the inbuilt vector factory. </p>
<p> References ANTLR3_BASE_TREE_struct::children, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dupNode (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_COMMON_TREE_struct::factory, ANTLR3_ARBORETUM_struct::newFromTree, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static void factoryClose (<code>pANTLR3_ARBORETUM</code> factory) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_VECTOR_FACTORY_struct::close, ANTLR3_STACK_struct::free, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_ARBORETUM_struct::pools, ANTLR3_ARBORETUM_struct::thisPool, and ANTLR3_ARBORETUM_struct::vFactory. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getCharPositionInLine (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_BASE_TREE_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>ANTLR3_INT32</code> getChildIndex (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>ANTLR3_UINT32</code> getLine (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, ANTLR3_BASE_TREE_struct::getLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_BASE_TREE_struct::super, and ANTLR3_COMMON_TREE_struct::token. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getParent (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_STRING</code> getText (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::toString. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> getToken (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>ANTLR3_UINT32</code> getType (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_BASE_TREE_struct::super, and ANTLR3_COMMON_TREE_struct::token. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> isNilNode (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> newFromToken (<code>pANTLR3_ARBORETUM</code> factory, <code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_ARBORETUM_struct::newTree, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> newFromTree (<code>pANTLR3_ARBORETUM</code> factory, <code>pANTLR3_COMMON_TREE</code> tree) [static]</h3>
<p>References ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_ARBORETUM_struct::newTree, ANTLR3_BASE_TREE_struct::super, ANTLR3_COMMON_TREE_struct::token, and ANTLR3_BASE_TREE_struct::u. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>static void newPool (<code>pANTLR3_ARBORETUM</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_POOL_SIZE, ANTLR3_MALLOC, ANTLR3_REALLOC, ANTLR3_ARBORETUM_struct::nextTree, ANTLR3_ARBORETUM_struct::pools, and ANTLR3_ARBORETUM_struct::thisPool. </p>
<p> Referenced by antlr3ArboretumNew(), and newPoolTree().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> newPoolTree (<code>pANTLR3_ARBORETUM</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_POOL_SIZE, antlr3SetCTAPI(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_COMMON_TREE_struct::factory, newPool(), ANTLR3_ARBORETUM_struct::nextTree, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_STACK_struct::peek, ANTLR3_ARBORETUM_struct::pools, ANTLR3_STACK_struct::pop, ANTLR3_BASE_TREE_struct::strFactory, ANTLR3_BASE_TREE_struct::super, ANTLR3_ARBORETUM_struct::thisPool, and ANTLR3_ARBORETUM_struct::unTruc. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>static void reuse (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Clean up any child vector that the tree might have, so it can be reused, then add it into the reuse stack. </p>
<p> References ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_BASE_TREE_struct::children, ANTLR3_VECTOR_struct::clear, ANTLR3_COMMON_TREE_struct::factory, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_STACK_struct::push, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static void setChildIndex (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static void setParent (<code>pANTLR3_BASE_TREE</code> tree, <code>pANTLR3_BASE_TREE</code> parent) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>static <code>pANTLR3_STRING</code> toString (<code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>References ANTLR3_TRUE, ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_STRING_FACTORY_struct::newPtr, nilNode(), ANTLR3_BASE_TREE_struct::strFactory, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
