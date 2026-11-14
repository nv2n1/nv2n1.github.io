---
title: "antlr3-isrewriter(3)"
name: "antlr3-isrewriter"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-isrewriter/"
description: "ANTLR3_COMMON_TREE_NODE_STREAM_struct –"
---

<p>ANTLR3_COMMON_TREE_NODE_STREAM_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3commontreenodestream.h">antlr3commontreenodestream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_MARKER</code> <code>absoluteNodeIndex</code><br />
 <i>What node index did we just consume? i=0..n-1 for n node trees. </i><br />
 <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>adaptor</code><br />
 <i>Pointer to tree adaptor interface that manipulates/builds the tree. </i><br />
 void(* <code>addLookahead</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>pANTLR3_BASE_TREE</code> node) </p>
<p> void(* <code>addNavigationNode</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_UINT32</code> ttype) </p>
<p> <code>ANTLR3_INT32</code> <code>currentChildIndex</code><br />
 <i>Which child are we currently visiting? If -1 we have not visited this node yet; next </i><code>consume()</code> request will set currentIndex to 0.<br />
 <code>pANTLR3_BASE_TREE</code> <code>currentNode</code><br />
 <i>Which node are we currently visiting? </i><br />
 <code>ANTLR3_COMMON_TREE</code> <code>DOWN</code><br />
 <i>Dummy tree node that indicates a descent into a child tree. </i><br />
 <code>ANTLR3_COMMON_TREE</code> <code>EOF_NODE</code><br />
 <i>Dummy tree node that indicates the termination point of the tree. </i><br />
 void(* <code>fill</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_INT32</code> k) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getLookaheadSize</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>handleRootnode</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>hasNext</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>hasUniqueNavigationNodes</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>ANTLR3_UINT32</code> <code>head</code><br />
 <i>lookAhead[head] is the first symbol of lookahead, <a href="/docs/linux/man/1-lt/">LT</a>(1). </i><br />
 <code>ANTLR3_COMMON_TREE</code> <code>INVALID_NODE</code><br />
 <i>Dummy node that is returned if we need to indicate an invalid node for any reason. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>isRewriter</code><br />
 <i>Indicates whether this node stream was derived from a prior node stream to be used by a rewriting tree parser for instance. </i><br />
 <code>pANTLR3_BASE_TREE</code> * <code>lookAhead</code><br />
 <i>Buffer tree node stream for use with LT(i). </i><br />
 <code>ANTLR3_UINT32</code> <code>lookAheadLength</code><br />
 <i>Number of elements available in the lookahead buffer at any point in time. </i><br />
 <code>pANTLR3_VECTOR</code> <code>markers</code><br />
 <i>Calls to </i><code>mark()</code> may be nested so we have to track a stack of them.<br />
 <code>pANTLR3_BASE_TREE</code>(* <code>newDownNode</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>newUpNode</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_BASE_TREE</code>(* <code>next</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_VECTOR</code> <code>nodes</code><br />
 <i>The complete mapping from stream index to tree node. </i><br />
 <code>pANTLR3_STACK</code> <code>nodeStack</code><br />
 <i>As we walk down the nodes, we must track parent nodes so we know where to go after walking the last child of a node. </i><br />
 <code>ANTLR3_INT32</code> <code>p</code><br />
 <i>The current index into the nodes vector of the current tree we are parsing and possibly rewriting. </i><br />
 <code>ANTLR3_INT32</code>(* <code>pop</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_BASE_TREE</code> <code>previousNode</code><br />
 <i>Which node did we last visit? Used for LT(-1). </i><br />
 void(* <code>push</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_INT32</code> index) </p>
<p> void(* <code>reset</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<p> <code>pANTLR3_BASE_TREE</code> <code>root</code><br />
 <i>Which tree are we navigating ? </i><br />
 <code>pANTLR3_STRING_FACTORY</code> <code>stringFactory</code><br />
 <i>String factory for use by anything that wishes to create strings such as a tree representation or some copy of the text etc. </i><br />
 void * <code>super</code><br />
 <i>Any interface that implements this interface (is a super structure containing this structure), may store the pointer to itself here in the super pointer, which is not used by the common tree node stream. </i><br />
 <code>ANTLR3_UINT32</code> <code>tail</code><br />
 <i>Add new lookahead at lookahead[tail]. </i><br />
 <code>pANTLR3_TREE_NODE_STREAM</code> <code>tnstream</code><br />
 <i>Pointer to the tree node stream interface. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>uniqueNavigationNodes</code><br />
 <i>If set to ANTLR3_TRUE then the navigation nodes UP, DOWN are duplicated rather than reused within the tree. </i><br />
 <code>ANTLR3_COMMON_TREE</code> <code>UP</code><br />
 <i>Dummy tree node that indicates a descent up to a parent tree. </i><br />
 <code>pANTLR3_BASE_TREE</code>(* <code>visitChild</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_UINT32</code> child) </p>
<p> void(* <code>walkBackToMostRecentNodeWithUnvisitedChildren</code> )(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns) </p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::absoluteNodeIndex</code></h3>
<p>What node index did we just consume? i=0..n-1 for n node trees. <code>IntStream.next</code> is hence 1 + this value. Size will be same.</p>
<h3><code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor</code></h3>
<p>Pointer to tree adaptor interface that manipulates/builds the tree. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and fillBuffer().</p>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::addLookahead</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>pANTLR3_BASE_TREE</code> node)</h3>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_UINT32</code> ttype)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and fillBuffer().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::currentChildIndex</code></h3>
<p>Which child are we currently visiting? If -1 we have not visited this node yet; next <code>consume()</code> request will set currentIndex to 0.</p>
<h3><code>pANTLR3_BASE_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::currentNode</code></h3>
<p>Which node are we currently visiting?</p>
<h3><code>ANTLR3_COMMON_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN</code></h3>
<p>Dummy tree node that indicates a descent into a child tree. Initialized by a call to create a new interface. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>ANTLR3_COMMON_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE</code></h3>
<p>Dummy tree node that indicates the termination point of the tree. Initialized by a call to create a new interface. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and getMissingSymbol().</p>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::fill</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_INT32</code> k)</h3>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::free</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::getLookaheadSize</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::handleRootnode</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasNext</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::head</code></h3>
<p>lookAhead[head] is the first symbol of lookahead, <a href="/docs/linux/man/1-lt/">LT</a>(1).</p>
<h3><code>ANTLR3_COMMON_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE</code></h3>
<p>Dummy node that is returned if we need to indicate an invalid node for any reason. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and LB().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter</code></h3>
<p>Indicates whether this node stream was derived from a prior node stream to be used by a rewriting tree parser for instance. If this flag is set to ANTLR3_TRUE, then when this stream is closed it will not free the root tree as this tree always belongs to the origniating node stream. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNewStream(), and reset().</p>
<h3><code>pANTLR3_BASE_TREE</code>* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::lookAhead</code></h3>
<p>Buffer tree node stream for use with LT(i). This list grows to fit new lookahead depths, but <code>consume()</code> wraps like a circular buffer.</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::lookAheadLength</code></h3>
<p>Number of elements available in the lookahead buffer at any point in time. This is the current size of the array.</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers</code></h3>
<p>Calls to <code>mark()</code> may be nested so we have to track a stack of them. The marker is an index into this stack. Index 0 is the first marker. This is a List&lt;TreeWalkState&gt; </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::next</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes</code></h3>
<p>The complete mapping from stream index to tree node. This buffer includes pointers to DOWN, UP, and EOF nodes. It is built upon ctor invocation. The elements are type Object as we don&#8217;t what the trees look like. </p>
<p> Load upon first need of the buffer so we can set token types of interest for reverseIndexing. Slows us down a wee bit to do all of the if p==-1 testing everywhere though, though in C you won&#8217;t really be able to measure this. </p>
<p> Must be freed when the tree node stream is torn down. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), fillBuffer(), and LB().</p>
<h3><code>pANTLR3_STACK</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack</code></h3>
<p>As we walk down the nodes, we must track parent nodes so we know where to go after walking the last child of a node. When visiting a child, push current node and current index (current index is first stored in the tree node structure to avoid two stacks. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and reset().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::p</code></h3>
<p>The current index into the nodes vector of the current tree we are parsing and possibly rewriting. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), fillBufferRoot(), LB(), and reset().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::previousNode</code></h3>
<p>Which node did we last visit? Used for LT(-1).</p>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::push</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_INT32</code> index)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and setTreeNodeStream().</p>
<h3><code>pANTLR3_BASE_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::root</code></h3>
<p>Which tree are we navigating ? </p>
<p> Referenced by antlr3CommonTreeNodeStreamNewStream(), antlr3CommonTreeNodeStreamNewTree(), and fillBufferRoot().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory</code></h3>
<p>String factory for use by anything that wishes to create strings such as a tree representation or some copy of the text etc. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>void* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::super</code></h3>
<p>Any interface that implements this interface (is a super structure containing this structure), may store the pointer to itself here in the super pointer, which is not used by the common tree node stream. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::tail</code></h3>
<p>Add new lookahead at lookahead[tail]. tail wraps around at the end of the lookahead buffer so tail could be less than head.</p>
<h3><code>pANTLR3_TREE_NODE_STREAM</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream</code></h3>
<p>Pointer to the tree node stream interface. </p>
<p> Referenced by alreadyParsedRule(), antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), reset(), and synpred().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes</code></h3>
<p>If set to ANTLR3_TRUE then the navigation nodes UP, DOWN are duplicated rather than reused within the tree. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>ANTLR3_COMMON_TREE</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP</code></h3>
<p>Dummy tree node that indicates a descent up to a parent tree. Initialized by a call to create a new interface. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3><code>pANTLR3_BASE_TREE</code>(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::visitChild</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns, <code>ANTLR3_UINT32</code> child)</h3>
<h3>void(* <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct::walkBackToMostRecentNodeWithUnvisitedChildren</code>)(struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> *ctns)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
