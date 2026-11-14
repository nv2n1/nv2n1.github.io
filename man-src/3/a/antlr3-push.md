---
title: "antlr3-push(3)"
name: "antlr3-push"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-push/"
description: "src/antlr3commontreenodestream.c –"
---

<h2 class="name">NAME</h2>
<p> src/antlr3commontreenodestream.c &#8211; </p>
<p> Defines the implementation of the common node stream the default tree node stream used by ANTLR.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontreenodestream.h">antlr3commontreenodestream.h</a>&gt; </p>
<h3>Functions</h3>
<p> static <code>ANTLR3_UINT32</code> <code>_LA</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>_LT</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) </p>
<p> static void <code>addNavigationNode</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>ANTLR3_UINT32</code> ttype) </p>
<p> static void <code>antlr3CommonTreeNodeStreamFree</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns)<br />
 <i>Free up any resources that belong to this common tree node stream. </i><br />
 ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNewStream</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> inStream) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNewTree</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint) </p>
<p> static void <code>antlr3TreeNodeStreamFree</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns) </p>
<p> ANTLR3_API <code>pANTLR3_TREE_NODE_STREAM</code> <code>antlr3TreeNodeStreamNew</code> () </p>
<p> static void <code>consume</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>fillBuffer</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Walk tree with depth-first-search and fill nodes buffer. </i><br />
 static void <code>fillBufferRoot</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns)<br />
 <i>Walk and fill the tree node buffer from the root tree. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>get</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getLookaheadSize</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) </p>
<p> static <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>getTreeAdaptor</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getTreeSource</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>hasUniqueNavigationNodes</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>LB</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) </p>
<p> static <code>ANTLR3_MARKER</code> <code>mark</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>newDownNode</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>newUpNode</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) </p>
<p> static <code>ANTLR3_INT32</code> <code>pop</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) </p>
<p> static void <code>push</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>ANTLR3_INT32</code> index) </p>
<p> static void <code>release</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>replaceChildren</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>reset</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns)<br />
 <i>Reset the input stream to the start of the input nodes. </i><br />
 static void <code>rewindLast</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>rewindMark</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>seek</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) </p>
<p> static void <code>setUniqueNavigationNodes</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_BOOLEAN</code> uniqueNavigationNodes) </p>
<p> static <code>ANTLR3_UINT32</code> <code>size</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>ANTLR3_MARKER</code> <code>tindex</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>pANTLR3_STRING</code> <code>toString</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns) </p>
<p> static <code>pANTLR3_STRING</code> <code>toStringSS</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop) </p>
<p> static void <code>toStringWork</code> (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop, <code>pANTLR3_STRING</code> buf) </p>
<h2>Detailed Description</h2>
<p> Defines the implementation of the common node stream the default tree node stream used by ANTLR. </p>
<h2>Function Documentation</h2>
<h3>static <code>ANTLR3_UINT32</code> _LA (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> _LT (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void addNavigationNode (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>ANTLR3_UINT32</code> ttype) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void antlr3CommonTreeNodeStreamFree (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Free up any resources that belong to this common tree node stream. </p>
<p> References ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, ANTLR3_FREE, ANTLR3_TRUE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_INT_STREAM_struct::free, ANTLR3_STACK_struct::free, ANTLR3_BASE_TREE_ADAPTOR_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNew (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint)</h3>
<p> References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TEXT_CHARP, ANTLR3_TOKEN_DOWN, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TOKEN_UP, ANTLR3_TREE_ADAPTORNew(), antlr3CommonTokenNew(), antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3StackNew(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), ANTLR3_COMMON_TOKEN_struct::chars, consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_BASE_TREE_ADAPTOR_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, INITIAL_CALL_STACK_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, ANTLR3_COMMON_TOKEN_struct::textState, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, ANTLR3_COMMON_TOKEN_struct::tokText, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNewTree().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNewStream (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> inStream)</h3>
<p> References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TRUE, antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getLookaheadSize(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::getLookaheadSize, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP.</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNewTree (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint)</h3>
<p> References antlr3CommonTreeNodeStreamNew(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, and ANTLR3_BASE_TREE_struct::strFactory.</p>
<h3>static void antlr3TreeNodeStreamFree (<code>pANTLR3_TREE_NODE_STREAM</code> tns) [static]</h3>
<p> References ANTLR3_FREE. </p>
<p> Referenced by antlr3TreeNodeStreamNew().</p>
<h3>ANTLR3_API <code>pANTLR3_TREE_NODE_STREAM</code> antlr3TreeNodeStreamNew ()</h3>
<p> References ANTLR3_CALLOC, antlr3TreeNodeStreamFree(), ANTLR3_TREE_NODE_STREAM_struct::free, replaceChildren(), and ANTLR3_TREE_NODE_STREAM_struct::replaceChildren. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void consume (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void fillBuffer (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> Walk tree with depth-first-search and fill nodes buffer. Don&#8217;t add in DOWN, UP nodes if the supplied tree is a list (t is isNilNode) </p>
<p> References ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, ANTLR3_VECTOR_struct::add, ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_FALSE, ANTLR3_TOKEN_DOWN, ANTLR3_TOKEN_UP, ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, ANTLR3_BASE_TREE_struct::getChildCount, ANTLR3_BASE_TREE_ADAPTOR_struct::isNilNode, nilNode(), and ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes. </p>
<p> Referenced by fillBufferRoot().</p>
<h3>static void fillBufferRoot (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Walk and fill the tree node buffer from the root tree. </p>
<p> References fillBuffer(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::root.</p>
<h3>static <code>pANTLR3_BASE_TREE</code> get (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) [static]</h3>
<h3>static <code>ANTLR3_UINT32</code> getLookaheadSize (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_BASE_TREE_ADAPTOR</code> getTreeAdaptor (<code>pANTLR3_TREE_NODE_STREAM</code> tns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getTreeSource (<code>pANTLR3_TREE_NODE_STREAM</code> tns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> hasUniqueNavigationNodes (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> LB (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_INT32</code> k) [static]</h3>
<p> References ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_TREE_NODE_STREAM_struct::ctns, ANTLR3_VECTOR_struct::get, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::p.</p>
<h3>static <code>ANTLR3_MARKER</code> mark (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and antlr3dfapredict().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> newDownNode (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> newUpNode (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>ANTLR3_INT32</code> pop (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void push (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns, <code>ANTLR3_INT32</code> index) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void release (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void replaceChildren (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> Referenced by antlr3TreeNodeStreamNew().</p>
<h3>static void reset (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctns) [static]</h3>
<p> Reset the input stream to the start of the input nodes. </p>
<p> References ANTLR3_TRUE, antlr3StackNew(), ANTLR3_STACK_struct::free, INITIAL_CALL_STACK_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::lastMarker, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void rewindLast (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void rewindMark (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void seek (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void setUniqueNavigationNodes (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>ANTLR3_BOOLEAN</code> uniqueNavigationNodes) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>ANTLR3_UINT32</code> size (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and displayRecognitionError().</p>
<h3>static <code>ANTLR3_MARKER</code> tindex (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_STRING</code> toString (<code>pANTLR3_TREE_NODE_STREAM</code> tns) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static <code>pANTLR3_STRING</code> toStringSS (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>static void toStringWork (<code>pANTLR3_TREE_NODE_STREAM</code> tns, <code>pANTLR3_BASE_TREE</code> start, <code>pANTLR3_BASE_TREE</code> stop, <code>pANTLR3_STRING</code> buf) [static]</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBP">Author</a></p>
<dd></dl>
