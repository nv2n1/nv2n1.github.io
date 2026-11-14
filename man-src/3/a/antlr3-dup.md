---
title: "antlr3-dup(3)"
name: "antlr3-dup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-dup/"
description: "ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct &#8211; </p>
<p> A generic list of elements tracked in an alternative to be used in a -&gt; rewrite rule.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3rewritestreams.h">antlr3rewritestreams.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> void *(* <code>_next</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream) </p>
<p> <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>adaptor</code><br />
 <i>Pointer to the tree adaptor in use for this stream. </i><br />
 void(* <code>add</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el, void(ANTLR3_CDECL *freePtr)(void *))<br />
 <i>Add a new pANTLR3_BASE_TREE to this stream. </i><br />
 <code>ANTLR3_UINT32</code> <code>cursor</code><br />
 <i>Cursor 0..n-1. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>dirty</code><br />
 <i>Once a node / subtree has been used in a stream, it must be dup&#8217;ed from then on. </i><br />
 void *(* <code>dup</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el)<br />
 <i>When constructing trees, sometimes we need to dup a token or AST subtree. </i><br />
 void * <code>elementDescription</code><br />
 <i>The element or stream description; usually has name of the token or rule reference that this list tracks. </i><br />
 <code>pANTLR3_VECTOR</code> <code>elements</code><br />
 <i>The list of tokens or subtrees we are tracking. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>freeElements</code><br />
 <i>Indicates whether we should free the vector or it was supplied to us. </i><br />
 void *(* <code>getDescription</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Returns the description string if there is one available (check for NULL). </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>hasNext</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Returns ANTLR3_TRUE if there is a next element available. </i><br />
 void *(* <code>next</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Return the next element in the stream. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>nextNode</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Treat next element as a single node even if it&#8217;s a subtree. </i><br />
 void *(* <code>nextToken</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>nextTree</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream) </p>
<p> <code>pANTLR3_BASE_RECOGNIZER</code> <code>rec</code> </p>
<p> void(* <code>reset</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Reset the condition of this stream so that it appears we have not consumed any of its elements. </i><br />
 void * <code>singleElement</code><br />
 <i>Track single elements w/o creating a list. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)<br />
 <i>Number of elements available in the stream. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>toTree</code> )(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el)<br />
 <i>Ensure stream emits trees; tokens must be converted to AST nodes. </i></p>
<h2>Detailed Description</h2>
<p> A generic list of elements tracked in an alternative to be used in a -&gt; rewrite rule. </p>
<p> In the C implementation, all tree oriented streams return a pointer to the same type: pANTLR3_BASE_TREE. Anything that has subclassed from this still passes this type, within which there is a super pointer, which points to it&#8217;s own data and methods. Hence we do not need to implement this as the equivalent of an abstract class, but just fill in the appropriate interface as usual with this model. </p>
<p> Once you start <code>next()</code>ing, do not try to add more elements. It will break the cursor tracking I believe. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> </p>
<p> <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code> </p>
<p> <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code></dl>
<p> TODO: add mechanism to detect/puke on modification after reading from stream</p>
<h2>Field Documentation</h2>
<h3>void*(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::_next</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), next(), nextNode(), nextNodeNode(), nextNodeToken(), nextToken(), and nextTree().</p>
<h3><code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::adaptor</code></h3>
<p> Pointer to the tree adaptor in use for this stream. </p>
<p> Referenced by add(), antlr3RewriteRuleElementStreamNewAE(), dupTree(), freeNodeRS(), freeRS(), nextNode(), nextNodeToken(), and toTreeNode().</p>
<h3>void(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::add</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el, void(ANTLR3_CDECL *freePtr)(void *))</h3>
<p> Add a new pANTLR3_BASE_TREE to this stream. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), and antlr3RewriteRuleElementStreamNewAEE().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::cursor</code></h3>
<p> Cursor 0..n-1. If singleElement!=NULL, cursor is 0 until you <code>next()</code>, which bumps it to 1 meaning no more elements. </p>
<p> Referenced by _next(), antlr3RewriteRuleElementStreamNewAE(), hasNext(), next(), nextNode(), nextTree(), and reset().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dirty</code></h3>
<p> Once a node / subtree has been used in a stream, it must be dup&#8217;ed from then on. Streams are reset after sub rules so that the streams can be reused in future sub rules. So, reset must set a dirty bit. If dirty, then <code>next()</code> always returns a dup. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), nextNode(), nextTree(), and reset().</p>
<h3>void*(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el)</h3>
<p> When constructing trees, sometimes we need to dup a token or AST subtree. Dup&#8217;ing a token means just creating another AST node around it. For trees, you must call the <code>adaptor.dupTree()</code>. </p>
<p> Referenced by antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), antlr3RewriteRuleNODEStreamNewAEV(), antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), antlr3RewriteRuleSubtreeStreamNewAEV(), antlr3RewriteRuleTOKENStreamNewAE(), antlr3RewriteRuleTOKENStreamNewAEE(), antlr3RewriteRuleTOKENStreamNewAEV(), next(), and nextTree().</p>
<h3>void* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elementDescription</code></h3>
<p> The element or stream description; usually has name of the token or rule reference that this list tracks. Can include rulename too, but the exception would track that info. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), and getDescription().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::elements</code></h3>
<p> The list of tokens or subtrees we are tracking. </p>
<p> Referenced by _next(), add(), antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleElementStreamNewAEV(), expungeRS(), freeNodeRS(), freeRS(), hasNext(), and size().</p>
<h3>void(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), antlr3RewriteRuleNODEStreamNewAEV(), antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), and antlr3RewriteRuleSubtreeStreamNewAEV().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::freeElements</code></h3>
<p> Indicates whether we should free the vector or it was supplied to us. </p>
<p> Referenced by add(), antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleElementStreamNewAEV(), expungeRS(), freeNodeRS(), and freeRS().</p>
<h3>void*(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::getDescription</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Returns the description string if there is one available (check for NULL). </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::hasNext</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Returns ANTLR3_TRUE if there is a next element available. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>void*(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::next</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Return the next element in the stream. If out of elements, throw an exception unless <code>size()</code>==1. If size is 1, then return elements[0]. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Treat next element as a single node even if it&#8217;s a subtree. This is used instead of <code>next()</code> when the result has to be a tree root node. Also prevents us from duplicating recently-added children; e.g., ^(type ID)+ adds ID to type and then 2nd iteration must dup the type node, but ID has been added. </p>
<p> Referencing to a rule result twice is ok; dup entire tree as we can&#8217;t be adding trees; e.g., expr expr. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), antlr3RewriteRuleNODEStreamNewAEV(), antlr3RewriteRuleSubtreeStreamNewAE(), antlr3RewriteRuleSubtreeStreamNewAEE(), antlr3RewriteRuleSubtreeStreamNewAEV(), antlr3RewriteRuleTOKENStreamNewAE(), antlr3RewriteRuleTOKENStreamNewAEE(), and antlr3RewriteRuleTOKENStreamNewAEV().</p>
<h3>void*(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextToken</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextTree</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3><code>pANTLR3_BASE_RECOGNIZER</code> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::rec</code></h3>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE(), freeNodeRS(), and freeRS().</p>
<h3>void(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::reset</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Reset the condition of this stream so that it appears we have not consumed any of its elements. Elements themselves are untouched. </p>
<p> Referenced by antlr3RewriteRuleElementStreamNewAE().</p>
<h3>void* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::singleElement</code></h3>
<p> Track single elements w/o creating a list. Upon 2nd add, alloc list </p>
<p> Referenced by _next(), add(), antlr3RewriteRuleElementStreamNewAE(), freeNodeRS(), hasNext(), and size().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::size</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream)</h3>
<p> Number of elements available in the stream. </p>
<p> Referenced by _next(), antlr3RewriteRuleElementStreamNewAE(), next(), nextNode(), and nextTree().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree</code>)(struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> *stream, void *el)</h3>
<p> Ensure stream emits trees; tokens must be converted to AST nodes. AST nodes can be passed through unmolested. </p>
<p> Referenced by _next(), antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleNODEStreamNewAE(), antlr3RewriteRuleNODEStreamNewAEE(), and antlr3RewriteRuleNODEStreamNewAEV(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBB">Author</a></p>
<dd></dl>
