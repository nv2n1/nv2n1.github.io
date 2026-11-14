---
title: "antlr3-ctns(3)"
name: "antlr3-ctns"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-ctns/"
description: "ANTLR3_TREE_NODE_STREAM_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_TREE_NODE_STREAM_struct &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontreenodestream.h">antlr3commontreenodestream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>_LT</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_INT32</code> k)<br />
 <i>Get tree node at current input pointer + i ahead where i=1 is next node. </i><br />
 <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>ctns</code><br />
 <i>Any interface that implements this interface (is a super structure containing this structure), may store the pointer to itself here in the super pointer, which is not used by the tree node stream. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)<br />
 <i>Release up any and all space the the interface allocate, including for this structure. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>get</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_INT32</code> i)<br />
 <i>Get a tree node at an absolute index i; 0..n-1. </i><br />
 <code>pANTLR3_BASE_TREE_ADAPTOR</code>(* <code>getTreeAdaptor</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)<br />
 <i>What adaptor can tell me how to interpret/navigate nodes and trees. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>getTreeSource</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)<br />
 <i>Where is this stream pulling nodes from? This is not the name, but the object that provides node objects. </i><br />
 <code>pANTLR3_INT_STREAM</code> <code>istream</code><br />
 <i>All input streams implement the ANTLR3_INT_STREAM interface. </i><br />
 void(* <code>replaceChildren</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Replace from start to stop child index of parent with t, which might be a list. </i><br />
 void(* <code>setUniqueNavigationNodes</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_BOOLEAN</code> uniqueNavigationNodes)<br />
 <i>As we flatten the tree, we use UP, DOWN nodes to represent the tree structure. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toString</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns) </p>
<p> <code>pANTLR3_STRING</code>(* <code>toStringSS</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop)<br />
 <i>Return the text of all nodes from start to stop, inclusive. </i><br />
 void(* <code>toStringWork</code> )(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop, <code>pANTLR3_STRING</code> buf)<br />
 <i>Return the text of all nodes from start to stop, inclusive, into the supplied buffer. </i></p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::_LT</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_INT32</code> k)</h3>
<p> Get tree node at current input pointer + i ahead where i=1 is next node. i&lt;0 indicates nodes in the past. So LT(-1) is previous node, but implementations are not required to provide results for k &lt; -1. LT(0) is undefined. For i&gt;=n, return null. Return NULL for LT(0) and any index that results in an absolute address that is negative (beyond the start of the list). </p>
<p> This is analogous to the <code>LT()</code> method of the TokenStream, but this returns a tree node instead of a token. Makes code gen identical for both parser and tree grammars. :) </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3RecognitionExceptionNew(), getCurrentInputSymbol(), and getMissingSymbol().</p>
<h3><code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>ANTLR3_TREE_NODE_STREAM_struct::ctns</code></h3>
<p> Any interface that implements this interface (is a super structure containing this structure), may store the pointer to itself here in the super pointer, which is not used by the tree node stream. This will point to an implementation of ANTLR3_COMMON_TREE_NODE_STREAM in this case. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), getCurrentInputSymbol(), getMissingSymbol(), and LB().</p>
<h3>void(* <code>ANTLR3_TREE_NODE_STREAM_struct::free</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)</h3>
<p> Release up any and all space the the interface allocate, including for this structure. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and antlr3TreeNodeStreamNew().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::get</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_INT32</code> i)</h3>
<p> Get a tree node at an absolute index i; 0..n-1. If you don&#8217;t want to buffer up nodes, then this method makes no sense for you. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE_ADAPTOR</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)</h3>
<p> What adaptor can tell me how to interpret/navigate nodes and trees. E.g., get text of a node. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::getTreeSource</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)</h3>
<p> Where is this stream pulling nodes from? This is not the name, but the object that provides node objects. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_INT_STREAM</code> <code>ANTLR3_TREE_NODE_STREAM_struct::istream</code></h3>
<p> All input streams implement the ANTLR3_INT_STREAM interface. .. </p>
<p> Referenced by alreadyParsedRule(), antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), reset(), and synpred().</p>
<h3>void(* <code>ANTLR3_TREE_NODE_STREAM_struct::replaceChildren</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p> Replace from start to stop child index of parent with t, which might be a list. Number of children may be different after this call. The stream is notified because it is walking the tree and might need to know you are monkeying with the underlying tree. Also, it might be able to modify the node stream to avoid restreaming for future phases. </p>
<p> If parent is null, don&#8217;t do anything; must be at root of overall tree. Can&#8217;t replace whatever points to the parent externally. Do nothing. </p>
<p> Referenced by antlr3TreeNodeStreamNew().</p>
<h3>void(* <code>ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>ANTLR3_BOOLEAN</code> uniqueNavigationNodes)</h3>
<p> As we flatten the tree, we use UP, DOWN nodes to represent the tree structure. When debugging we need unique nodes so we have to instantiate new ones. When doing normal tree parsing, it&#8217;s slow and a waste of memory to create unique navigation nodes. Default should be false; </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::toString</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns)</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_TREE_NODE_STREAM_struct::toStringSS</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop)</h3>
<p> Return the text of all nodes from start to stop, inclusive. If the stream does not buffer all the nodes then it can still walk recursively from start until stop. You can always return null or &#8221; too, but users should not access $ruleLabel.text in an action of course in that case. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>void(* <code>ANTLR3_TREE_NODE_STREAM_struct::toStringWork</code>)(struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> *tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop, <code>pANTLR3_STRING</code> buf)</h3>
<p> Return the text of all nodes from start to stop, inclusive, into the supplied buffer. If the stream does not buffer all the nodes then it can still walk recursively from start until stop. You can always return null or &#8221; too, but users should not access $ruleLabel.text in an action of course in that case. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
