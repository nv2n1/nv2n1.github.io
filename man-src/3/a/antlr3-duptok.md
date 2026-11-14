---
title: "antlr3-duptok(3)"
name: "antlr3-duptok"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-duptok/"
description: "src/antlr3rewritestreams.c –"
---

<p>src/antlr3rewritestreams.c &#8211; </p>
<p> Implementation of token/tree streams that are used by the tree re-write rules to manipulate the tokens and trees produced by rules that are subject to rewrite directives.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3rewritestreams.h">antlr3rewritestreams.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void * <code>_next</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Do the work of getting the next element, making sure that it&#8217;s a tree node or subtree. </i><br />
 static void <code>add</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *el, void(ANTLR3_CDECL *freePtr)(void *)) </p>
<p> static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> <code>antlr3RewriteRuleElementStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> <code>antlr3RewriteRuleElementStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> <code>antlr3RewriteRuleElementStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> static void * <code>dupTok</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *el)<br />
 <i>When constructing trees, sometimes we need to dup a token or AST subtree. </i><br />
 static void * <code>dupTree</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *element)<br />
 <i>When constructing trees, sometimes we need to dup a token or AST subtree. </i><br />
 static void * <code>dupTreeNode</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *element)<br />
 <i>When constructing trees, sometimes we need to dup a token or AST subtree. </i><br />
 static void <code>expungeRS</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) </p>
<p> static void <code>freeNodeRS</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Do special nilNode reuse detection for node streams. </i><br />
 static void <code>freeRS</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) </p>
<p> static void * <code>getDescription</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Returns the description string if there is one available (check for NULL). </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>hasNext</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Returns ANTLR3_TRUE if there is a next element available. </i><br />
 static void * <code>next</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Return the next element in the stream. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>nextNode</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Treat next element as a single node even if it&#8217;s a subtree. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>nextNodeNode</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>nextNodeToken</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Get the next token from the list and create a node for it This is the implementation for token streams. </i><br />
 static void * <code>nextToken</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Return the next element for a caller that wants just the token. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>nextTree</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Return the next element in the stream. </i><br />
 static void <code>reset</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Reset the condition of this stream so that it appears we have not consumed any of its elements. </i><br />
 static <code>ANTLR3_UINT32</code> <code>size</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream)<br />
 <i>Number of elements available in the stream. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>toTree</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *element)<br />
 <i>We don;t explicitly convert to a tree unless the call goes to nextTree, which means rewrites are heterogeneous. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>toTreeNode</code> (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void *element)<br />
 <i>Ensure stream emits trees; tokens must be converted to AST nodes. </i></p>
<h2>Detailed Description</h2>
<p>Implementation of token/tree streams that are used by the tree re-write rules to manipulate the tokens and trees produced by rules that are subject to rewrite directives. </p>
<h2>Function Documentation</h2>
<h3>static void * _next (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Do the work of getting the next element, making sure that it&#8217;s a tree node or subtree. Deal with the optimization of single- element list versus list of size &gt; 1. Throw an exception (or something similar) if the stream is empty or we&#8217;re out of elements and size&gt;1. You can override in a &#8216;subclass&#8217; if necessary. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, ANTLR3_VECTOR_struct::get, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static void add (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * el, void(ANTLR3_CDECL *freePtr)(void *)) [static]</h3>
<p>References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, ANTLR3_VECTOR_struct::add, ANTLR3_TRUE, ANTLR3_VECTOR_struct::count, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements, ANTLR3_VECTOR_FACTORY_struct::newVector, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement, and ANTLR3_BASE_TREE_ADAPTOR_struct::super. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> antlr3RewriteRuleElementStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) [static]</h3>
<p>References _next(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, add(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::add, ANTLR3_FALSE, ANTLR3_MALLOC, ANTLR3_VECTOR_struct::count, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dirty, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elementDescription, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements, freeRS(), getDescription(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::getDescription, hasNext(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::hasNext, next(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::next, nextNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextToken(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextToken, nextTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextTree, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::rec, ANTLR3_VECTOR_struct::remove, reset(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::reset, ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement, size(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size, ANTLR3_BASE_RECOGNIZER_struct::state, toTree(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAEE(), antlr3RewriteRuleElementStreamNewAEV(), antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAE(), and antlr3RewriteRuleTOKENStreamNewAE().</p>
<h3>static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> antlr3RewriteRuleElementStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement) [static]</h3>
<p>References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::add, and antlr3RewriteRuleElementStreamNewAE(). </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAEE(), antlr3RewriteRuleSubtreeStreamNewAEE(), and antlr3RewriteRuleTOKENStreamNewAEE().</p>
<h3>static <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> antlr3RewriteRuleElementStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, ANTLR3_VECTOR_struct::factoryMade, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAEV(), antlr3RewriteRuleSubtreeStreamNewAEV(), and antlr3RewriteRuleTOKENStreamNewAEV().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>static void * dupTok (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * el) [static]</h3>
<p>When constructing trees, sometimes we need to dup a token or AST subtree. Dup&#8217;ing a token means just creating another AST node around it. For trees, you must call the <code>adaptor.dupTree()</code>. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3RewriteRuleTOKENStreamNewAE(), antlr3RewriteRuleTOKENStreamNewAEE(), and antlr3RewriteRuleTOKENStreamNewAEV().</p>
<h3>static void * dupTree (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * element) [static]</h3>
<p>When constructing trees, sometimes we need to dup a token or AST subtree. Dup&#8217;ing a token means just creating another AST node around it. For trees, you must call the <code>adaptor.dupTree()</code>. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, and ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode. </p>
<p> Referenced by antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), and antlr3RewriteRuleSubtreeStreamNewAEV().</p>
<h3>static void * dupTreeNode (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * element) [static]</h3>
<p>When constructing trees, sometimes we need to dup a token or AST subtree. Dup&#8217;ing a token means just creating another AST node around it. For trees, you must call the <code>adaptor.dupTree()</code>. </p>
<p> References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), and antlr3RewriteRuleNODEStreamNewAEV().</p>
<h3>static void expungeRS (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_TRUE, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements. </p>
<p> Referenced by freeNodeRS(), and freeRS().</p>
<h3>static void freeNodeRS (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Do special nilNode reuse detection for node streams. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_VECTOR_struct::clear, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, expungeRS(), ANTLR3_VECTOR_struct::factoryMade, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements, ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::rec, ANTLR3_VECTOR_FACTORY_struct::returnVector, ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_BASE_TREE_ADAPTOR_struct::super. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), antlr3RewriteRuleNODEStreamNewAEV(), antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), and antlr3RewriteRuleSubtreeStreamNewAEV().</p>
<h3>static void freeRS (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_VECTOR_struct::clear, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, expungeRS(), ANTLR3_VECTOR_struct::factoryMade, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::rec, ANTLR3_VECTOR_FACTORY_struct::returnVector, ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_BASE_TREE_ADAPTOR_struct::super. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static void * getDescription (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Returns the description string if there is one available (check for NULL). </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elementDescription. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> hasNext (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Returns ANTLR3_TRUE if there is a next element available. </p>
<p> References ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement, and ANTLR3_VECTOR_struct::size. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static void * next (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Return the next element in the stream. If out of elements, throw an exception unless <code>size()</code>==1. If size is 1, then return elements[0]. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size. </p>
<p> Referenced by antlr3ExceptionFree(), and antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> nextNode (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Treat next element as a single node even if it&#8217;s a subtree. This is used instead of <code>next()</code> when the result has to be a tree root node. Also prevents us from duplicating recently-added children; e.g., ^(type ID)+ adds ID to type and then 2nd iteration must dup the type node, but ID has been added. </p>
<p> Referencing to a rule result twice is ok; dup entire tree as we can&#8217;t be adding trees; e.g., expr expr. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, ANTLR3_TRUE, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dirty, ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), antlr3RewriteRuleSubtreeStreamNewAEV(), intTrieAdd(), and intTrieGet().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> nextNodeNode (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), and antlr3RewriteRuleNODEStreamNewAEV().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> nextNodeToken (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Get the next token from the list and create a node for it This is the implementation for token streams. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, and ANTLR3_BASE_TREE_ADAPTOR_struct::create. </p>
<p> Referenced by antlr3RewriteRuleTOKENStreamNewAE(), antlr3RewriteRuleTOKENStreamNewAEE(), and antlr3RewriteRuleTOKENStreamNewAEV().</p>
<h3>static void * nextToken (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Return the next element for a caller that wants just the token. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> nextTree (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Return the next element in the stream. If out of elements, throw an exception unless <code>size()</code>==1. If size is 1, then return elements[0]. Return a duplicate node/subtree if stream is out of elements and size==1. If we&#8217;ve already used the element, dup (dirty bit set). </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dirty, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static void reset (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Reset the condition of this stream so that it appears we have not consumed any of its elements. Elements themselves are untouched. </p>
<p> References ANTLR3_TRUE, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dirty. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>ANTLR3_UINT32</code> size (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream) [static]</h3>
<p>Number of elements available in the stream. </p>
<p> Should be a count of one if singleElement is set. I copied this logic from the java implementation, which I suspect is just guarding against someone setting singleElement and forgetting to NULL it out </p>
<p> References ANTLR3_VECTOR_struct::count, ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements, and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> toTree (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * element) [static]</h3>
<p>We don;t explicitly convert to a tree unless the call goes to nextTree, which means rewrites are heterogeneous. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> toTreeNode (<code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> stream, void * element) [static]</h3>
<p>Ensure stream emits trees; tokens must be converted to AST nodes. AST nodes can be passed through unmolested. </p>
<p> References ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor, and ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), and antlr3RewriteRuleNODEStreamNewAEV().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
