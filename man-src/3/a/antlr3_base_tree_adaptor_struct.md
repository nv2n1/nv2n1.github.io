---
title: "antlr3_base_tree_adaptor_struct(3)"
name: "antlr3_base_tree_adaptor_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_base_tree_adaptor_struct/"
description: "ANTLR3_BASE_TREE_ADAPTOR_struct –"
---

<p>ANTLR3_BASE_TREE_ADAPTOR_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3basetreeadaptor.h">antlr3basetreeadaptor.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>addChild</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, void *child) </p>
<p> void(* <code>addChildToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>pANTLR3_COMMON_TOKEN</code> child) </p>
<p> void *(* <code>becomeRoot</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *newRoot, void *oldRoot) </p>
<p> void *(* <code>becomeRootToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *newRoot, void *oldRoot) </p>
<p> void *(* <code>create</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_COMMON_TOKEN</code> payload) </p>
<p> <code>pANTLR3_COMMON_TOKEN</code>(* <code>createToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) </p>
<p> <code>pANTLR3_COMMON_TOKEN</code>(* <code>createTokenFromToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_COMMON_TOKEN</code> fromToken) </p>
<p> void *(* <code>createTypeText</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) </p>
<p> void *(* <code>createTypeToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken) </p>
<p> void *(* <code>createTypeTokenText</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text) </p>
<p> <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code><br />
 <i>If set to something other than NULL, then this structure is points to an instance of the debugger interface. </i><br />
 void(* <code>deleteChild</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i) </p>
<p> void *(* <code>dupNode</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *treeNode) </p>
<p> void *(* <code>dupTree</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *tree) </p>
<p> void *(* <code>dupTreeTT</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, void *tree) </p>
<p> void *(* <code>errorNode</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_TOKEN_STREAM</code> tnstream, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken, <code>pANTLR3_EXCEPTION</code> e) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor) </p>
<p> void *(* <code>getChild</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getChildCount</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *) </p>
<p> <code>ANTLR3_INT32</code>(* <code>getChildIndex</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> void *(* <code>getParent</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *child) </p>
<p> <code>pANTLR3_STRING</code>(* <code>getText</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>pANTLR3_COMMON_TOKEN</code>(* <code>getToken</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>ANTLR3_MARKER</code>(* <code>getTokenStartIndex</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>ANTLR3_MARKER</code>(* <code>getTokenStopIndex</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getType</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getUniqueID</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>isNilNode</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t) </p>
<p> <code>pANTLR3_STRING</code>(* <code>makeDot</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *theTree)<br />
 <i>Produce a DOT (see graphviz freeware suite) from a base tree. </i><br />
 void *(* <code>nilNode</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor) </p>
<p> void(* <code>replaceChildren</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, void *t)<br />
 <i>Replace from start to stop child index of parent with t, which might be a list. </i><br />
 void *(* <code>rulePostProcessing</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *root) </p>
<p> void(* <code>setChild</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i, void *child) </p>
<p> void(* <code>setChildIndex</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i) </p>
<p> void(* <code>setDebugEventListener</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code>) </p>
<p> void(* <code>setParent</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *child, void *parent) </p>
<p> void(* <code>setText</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_STRING</code> t) </p>
<p> void(* <code>setText8</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_UINT8</code> t) </p>
<p> void(* <code>setTokenBoundaries</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken) </p>
<p> void(* <code>setType</code> )(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> type) </p>
<p> <code>pANTLR3_STRING_FACTORY</code> <code>strFactory</code><br />
 <i>We need a string factory for creating imaginary tokens, we take this from the stream we are supplied to walk. </i><br />
 void * <code>super</code><br />
 <i>Pointer to any enclosing structure/interface that contains this structure. </i><br />
 <code>pANTLR3_TOKEN_FACTORY</code> <code>tokenFactory</code> </p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::addChild</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, void *child)</h3>
<p>Referenced by addChildToken(), antlr3BaseTreeAdaptorInit(), dbgAddChildToken(), and dupTreeTT().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::addChildToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>pANTLR3_COMMON_TOKEN</code> child)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *newRoot, void *oldRoot)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit(), becomeRootToken(), and dbgBecomeRootToken().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRootToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *newRoot, void *oldRoot)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::create</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_COMMON_TOKEN</code> payload)</h3>
<p>Referenced by addChildToken(), ANTLR3_TREE_ADAPTORDebugNew(), ANTLR3_TREE_ADAPTORNew(), becomeRootToken(), createTypeText(), createTypeToken(), createTypeTokenText(), dbgAddChildToken(), dbgBecomeRootToken(), dbgNil(), nextNodeToken(), nilNode(), and setDebugEventListener().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::createToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), and createTypeText().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_COMMON_TOKEN</code> fromToken)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), createTypeToken(), and createTypeTokenText().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeText</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit(), and errorNode().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeTokenText</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3><code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>ANTLR3_BASE_TREE_ADAPTOR_struct::debugger</code></h3>
<p>If set to something other than NULL, then this structure is points to an instance of the debugger interface. In general, the debugger is only referenced internally in recovery/error operations so that it does not cause overhead by having to check this pointer in every function/method </p>
<p> Referenced by dbgAddChild(), dbgAddChildToken(), dbgBecomeRoot(), dbgBecomeRootToken(), dbgCreate(), dbgCreateTypeText(), dbgCreateTypeToken(), dbgCreateTypeTokenText(), dbgNil(), dbgSetTokenBoundaries(), and simulateTreeConstruction().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::deleteChild</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *treeNode)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), dupTree(), nextNode(), and toTreeNode().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::dupTree</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *tree)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, void *tree)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit(), dbgDupTree(), dupTree(), and dupTreeTT().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::errorNode</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_TOKEN_STREAM</code> tnstream, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken, <code>pANTLR3_EXCEPTION</code> e)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::free</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3CommonTreeNodeStreamFree(), and antlr3CommonTreeNodeStreamNew().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getChild</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), defineDotEdges(), defineDotNodes(), dupTreeTT(), fillBuffer(), and simulateTreeConstruction().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), defineDotEdges(), defineDotNodes(), dupTreeTT(), and simulateTreeConstruction().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getChildIndex</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getParent</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *child)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getText</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), defineDotEdges(), defineDotNodes(), makeDot(), and serializeNode().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getToken</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by serializeNode().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStartIndex</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), and serializeNode().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStopIndex</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getType</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), and serializeNode().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::getUniqueID</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit(), and serializeNode().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::isNilNode</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit(), and fillBuffer().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::makeDot</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *theTree)</h3>
<p>Produce a DOT (see graphviz freeware suite) from a base tree. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::nilNode</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::replaceChildren</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, void *t)</h3>
<p>Replace from start to stop child index of parent with t, which might be a list. Number of children may be different after this call. </p>
<p> If parent is null, don&#8217;t do anything; must be at root of overall tree. Can&#8217;t replace whatever points to the parent externally. Do nothing. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void*(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::rulePostProcessing</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *root)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setChild</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i, void *child)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setChildIndex</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> i)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), and dupTreeTT().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setDebugEventListener</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code>)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setParent</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *child, void *parent)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), and dupTreeTT().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setText</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_STRING</code> t)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setText8</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, <code>pANTLR3_UINT8</code> t)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken)</h3>
<p>Referenced by ANTLR3_TREE_ADAPTORDebugNew(), ANTLR3_TREE_ADAPTORNew(), and setDebugEventListener().</p>
<h3>void(* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::setType</code>)(struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> *adaptor, void *t, <code>ANTLR3_UINT32</code> type)</h3>
<p>Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory</code></h3>
<p>We need a string factory for creating imaginary tokens, we take this from the stream we are supplied to walk. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), createToken(), createTokenFromToken(), and makeDot().</p>
<h3>void* <code>ANTLR3_BASE_TREE_ADAPTOR_struct::super</code></h3>
<p>Pointer to any enclosing structure/interface that contains this structure. </p>
<p> Referenced by add(), ANTLR3_TREE_ADAPTORNew(), create(), ctaFree(), freeNodeRS(), and freeRS().</p>
<h3><code>pANTLR3_TOKEN_FACTORY</code> <code>ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory</code></h3>
<p>Referenced by ANTLR3_TREE_ADAPTORNew(), createToken(), createTokenFromToken(), and ctaFree(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
