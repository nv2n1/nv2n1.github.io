---
title: "antlr3-dbgcreatetypetoken(3)"
name: "antlr3-dbgcreatetypetoken"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-dbgcreatetypetoken/"
description: "src/antlr3basetreeadaptor.c –"
---

<p>src/antlr3basetreeadaptor.c &#8211; </p>
<p> Contains the base functions that all tree adaptors start with.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3basetreeadaptor.h">antlr3basetreeadaptor.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>addChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> child)<br />
 <i>Add a child to the tree t. </i><br />
 static void <code>addChildToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> child)<br />
 <i>Use the adaptor implementation to add a child node with the supplied token. </i><br />
 ANTLR3_API void <code>antlr3BaseTreeAdaptorInit</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)<br />
 <i>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>becomeRoot</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> newRootTree, <code>pANTLR3_BASE_TREE</code> oldRootTree)<br />
 <i>If oldRoot is a nil root, just copy or move the children to newRoot. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>becomeRootToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void *newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot)<br />
 <i>Use the adaptor interface to set a new tree node with the supplied token to the root of the tree. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>createTypeText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>createTypeToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken)<br />
 <i>Use the super class supplied </i><code>create()</code> method to create a new node from the supplied token.<br />
 static <code>pANTLR3_BASE_TREE</code> <code>createTypeTokenText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text) </p>
<p> static void <code>dbgAddChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> child) </p>
<p> static void <code>dbgAddChildToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> child) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgBecomeRoot</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgBecomeRootToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void *newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgCreateTypeText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgCreateTypeToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgCreateTypeTokenText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgDupTree</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgNil</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor) </p>
<p> static void <code>defineDotEdges</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void *t, <code>pANTLR3_STRING</code> dotSpec) </p>
<p> static void <code>defineDotNodes</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void *t, <code>pANTLR3_STRING</code> dotSpec) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dupTree</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Return a duplicate of the entire tree (implementation provided by the BASE_TREE interface. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>dupTreeTT</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> parent) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getChildCount</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>pANTLR3_STRING</code> <code>getText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Dummy implementation &#8211; will be supplied by super class. </i><br />
 static <code>ANTLR3_UINT32</code> <code>getType</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Dummy implementation &#8211; will be supplied by super class. </i><br />
 static <code>ANTLR3_UINT32</code> <code>getUniqueID</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> node)<br />
 <i>Returns a uniqueID for the node. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>isNilNode</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>pANTLR3_STRING</code> <code>makeDot</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void *theTree)<br />
 <i>Produce a DOT specification for graphviz. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>nilNode</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor)<br />
 <i>Create and return a nil tree node (no token payload). </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>rulePostProcessing</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> root)<br />
 <i>Transform ^(nil x) to x. </i><br />
 static void <code>setText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_STRING</code> t)<br />
 <i>Dummy implementation &#8211; will be supplied by super class. </i><br />
 static void <code>setText8</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_UINT8</code> t)<br />
 <i>Dummy implementation &#8211; will be supplied by super class. </i><br />
 static void <code>setType</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> type)<br />
 <i>Dummy implementation &#8211; will be supplied by super class. </i><br />
 static void <code>simulateTreeConstruction</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> tree)<br />
 <i>Sends the required debugging events for duplicating a tree to the debugger. </i></p>
<h2>Detailed Description</h2>
<p>Contains the base functions that all tree adaptors start with. </p>
<p> this implementation can then be overridden by any higher implementation.</p>
<h2>Function Documentation</h2>
<h3>static void addChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p>Add a child to the tree t. If child is a flat tree (a list), make all in list children of t. Warning: if t has no children, but child does and child isNilNode then it is ok to move children to t via t.children = child.children; i.e., without copying the array. This is for construction and I&#8217;m not sure it&#8217;s completely general for a tree&#8217;s addChild method to work this way. Make sure you differentiate between your tree&#8217;s addChild and this parser tree construction addChild if it&#8217;s not ok to move children to t with a simple assignment. </p>
<p> References ANTLR3_BASE_TREE_struct::addChild. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void addChildToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> child) [static]</h3>
<p>Use the adaptor implementation to add a child node with the supplied token. </p>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, and ANTLR3_BASE_TREE_ADAPTOR_struct::create. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>ANTLR3_API void antlr3BaseTreeAdaptorInit (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. </p>
<p> References ANTLR3_DEBUG_EVENT_LISTENER_struct::adaptor, addChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, addChildToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChildToken, becomeRoot(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot, becomeRootToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRootToken, createTypeText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeText, createTypeToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeToken, createTypeTokenText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeTokenText, dbgAddChild(), dbgAddChildToken(), dbgBecomeRoot(), dbgBecomeRootToken(), dbgCreateTypeText(), dbgCreateTypeToken(), dbgCreateTypeTokenText(), dbgDupTree(), dbgNil(), dupTree(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTree, dupTreeTT(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, getUniqueID(), ANTLR3_BASE_TREE_ADAPTOR_struct::getUniqueID, isNilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::isNilNode, makeDot(), ANTLR3_BASE_TREE_ADAPTOR_struct::makeDot, nilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::nilNode, rulePostProcessing(), ANTLR3_BASE_TREE_ADAPTOR_struct::rulePostProcessing, setText(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText, setText8(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText8, setType(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setType. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), ANTLR3_TREE_ADAPTORNew(), and setDebugEventListener().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> becomeRoot (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> newRootTree, <code>pANTLR3_BASE_TREE</code> oldRootTree) [static]</h3>
<p>If oldRoot is a nil root, just copy or move the children to newRoot. If not a nil root, make oldRoot a child of newRoot. </p>
<pre> old=^(nil a b c), new=r yields ^(r a b c)
 old=^(a b c), new=r yields ^(r ^(a b c))</pre>
<p>If newRoot is a nil-rooted single child tree, use the single child as the new root node. </p>
<pre> old=^(nil a b c), new=^(nil r) yields ^(r a b c)
 old=^(a b c), new=^(nil r) yields ^(r ^(a b c))</pre>
<p>If oldRoot was null, it&#8217;s ok, just return newRoot (even if isNilNode). </p>
<pre> old=null, new=r yields r
 old=null, new=^(nil r) yields ^(nil r)</pre>
<p>Return newRoot. Throw an exception if newRoot is not a simple node or nil root with a single child node&#8211;it must be a root node. If newRoot is ^(nil x)&lt;/endcode&gt; return x as newRoot. </p>
<p> Be advised that it&#8217;s ok for newRoot to point at oldRoot&#8217;s children; i.e., you don&#8217;t have to copy the list. We are constructing these nodes so we should have this control for efficiency. </p>
<p> References ANTLR3_BASE_TREE_struct::addChild, ANTLR3_FPRINTF, ANTLR3_BASE_TREE_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, ANTLR3_BASE_TREE_struct::isNilNode, and ANTLR3_BASE_TREE_struct::reuse. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), and dbgBecomeRoot().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> becomeRootToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void * newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) [static]</h3>
<p>Use the adaptor interface to set a new tree node with the supplied token to the root of the tree. </p>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot, and ANTLR3_BASE_TREE_ADAPTOR_struct::create. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> createTypeText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p>References ANTLR3_BASE_TREE_ADAPTOR_struct::create, and ANTLR3_BASE_TREE_ADAPTOR_struct::createToken. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), and dbgCreateTypeText().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> createTypeToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken) [static]</h3>
<p>Use the super class supplied <code>create()</code> method to create a new node from the supplied token. </p>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::create, ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken, and ANTLR3_COMMON_TOKEN_struct::setType. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), and dbgCreateTypeToken().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> createTypeTokenText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p>References ANTLR3_BASE_TREE_ADAPTOR_struct::create, ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken, ANTLR3_COMMON_TOKEN_struct::setText8, and ANTLR3_COMMON_TOKEN_struct::setType. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), and dbgCreateTypeTokenText().</p>
<h3>static void dbgAddChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_BASE_TREE_struct::addChild, and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void dbgAddChildToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> child) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, ANTLR3_BASE_TREE_ADAPTOR_struct::create, and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgBecomeRoot (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot, becomeRoot(), and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgBecomeRootToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void * newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot, ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot, ANTLR3_BASE_TREE_ADAPTOR_struct::create, and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgCreateTypeText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createTypeText(), and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgCreateTypeToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createTypeToken(), and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgCreateTypeTokenText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_COMMON_TOKEN</code> fromToken, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createTypeTokenText(), and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3><code>pANTLR3_BASE_TREE</code> dbgDupTree (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>References ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT, and simulateTreeConstruction(). </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgNil (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor) [static]</h3>
<p>References ANTLR3_BASE_TREE_ADAPTOR_struct::create, ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void defineDotEdges (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void * t, <code>pANTLR3_STRING</code> dotSpec) [static]</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::append8, ANTLR3_STRING_struct::charAt, ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, ANTLR3_BASE_TREE_ADAPTOR_struct::getText, and ANTLR3_STRING_struct::len. </p>
<p> Referenced by makeDot().</p>
<h3>static void defineDotNodes (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void * t, <code>pANTLR3_STRING</code> dotSpec) [static]</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::append8, ANTLR3_STRING_struct::charAt, ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, ANTLR3_BASE_TREE_ADAPTOR_struct::getText, and ANTLR3_STRING_struct::len. </p>
<p> Referenced by makeDot().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dupTree (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Return a duplicate of the entire tree (implementation provided by the BASE_TREE interface. ) </p>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3><code>pANTLR3_BASE_TREE</code> dupTreeTT (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_BASE_TREE</code> parent) [static]</h3>
<p>References ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT, ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, ANTLR3_BASE_TREE_struct::getChildIndex, ANTLR3_BASE_TREE_ADAPTOR_struct::setChildIndex, and ANTLR3_BASE_TREE_ADAPTOR_struct::setParent. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p>References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>ANTLR3_UINT32</code> getChildCount (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_STRING</code> getText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Dummy implementation &#8211; will be supplied by super class. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>ANTLR3_UINT32</code> getType (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Dummy implementation &#8211; will be supplied by super class. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>ANTLR3_UINT32</code> getUniqueID (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> node) [static]</h3>
<p>Returns a uniqueID for the node. Because this is the C implementation we can just use its address suitably converted/cast to an integer. </p>
<p> References ANTLR3_UINT32_CAST. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> isNilNode (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>References ANTLR3_BASE_TREE_struct::isNilNode. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_STRING</code> makeDot (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, void * theTree) [static]</h3>
<p>Produce a DOT specification for graphviz. </p>
<p> References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::append8, ANTLR3_STRING_struct::charAt, defineDotEdges(), defineDotNodes(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, ANTLR3_STRING_struct::len, ANTLR3_STRING_FACTORY_struct::newStr8, and ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> nilNode (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor) [static]</h3>
<p>Create and return a nil tree node (no token payload). </p>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::create. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), fillBuffer(), and toString().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> rulePostProcessing (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> root) [static]</h3>
<p>Transform ^(nil x) to x. </p>
<p> References ANTLR3_BASE_TREE_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_BASE_TREE_struct::reuse, ANTLR3_BASE_TREE_struct::setChildIndex, and ANTLR3_BASE_TREE_struct::setParent. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void setText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_STRING</code> t) [static]</h3>
<p>Dummy implementation &#8211; will be supplied by super class. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void setText8 (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_UINT8</code> t) [static]</h3>
<p>Dummy implementation &#8211; will be supplied by super class. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void setType (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> type) [static]</h3>
<p>Dummy implementation &#8211; will be supplied by super class. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit().</p>
<h3>static void simulateTreeConstruction (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> tree) [static]</h3>
<p>Sends the required debugging events for duplicating a tree to the debugger. </p>
<p> References ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, ANTLR3_BASE_TREE_ADAPTOR_struct::debugger, ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, and ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount. </p>
<p> Referenced by dbgDupTree().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
