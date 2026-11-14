---
title: "antlr3commontreenodestream(3)"
name: "antlr3commontreenodestream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3commontreenodestream/"
description: "include/antlr3commontreenodestream.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3commontreenodestream.h &#8211; </p>
<p> Definition of the ANTLR3 common tree node stream.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontreeadaptor.h">antlr3commontreeadaptor.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontree.h">antlr3commontree.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3intstream.h">antlr3intstream.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> </p>
<p> struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> </p>
<p> struct <code>ANTLR3_TREE_WALK_STATE_struct</code><br />
 <i>This structure is used to save the state information in the treenodestream when walking ahead with cyclic DFA or for syntactic predicates, we need to record the state of the tree node stream. </i></p>
<h3>Defines</h3>
<p> #define <code>DEFAULT_INITIAL_BUFFER_SIZE</code> 100<br />
 <i>Token buffer initial size settings ( will auto increase). </i><br />
 #define <code>INITIAL_CALL_STACK_SIZE</code> 10 </p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> <code>ANTLR3_COMMON_TREE_NODE_STREAM</code> </p>
<p> typedef struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> <code>ANTLR3_TREE_NODE_STREAM</code> </p>
<p> typedef struct <code>ANTLR3_TREE_WALK_STATE_struct</code> <code>ANTLR3_TREE_WALK_STATE</code><br />
 <i>This structure is used to save the state information in the treenodestream when walking ahead with cyclic DFA or for syntactic predicates, we need to record the state of the tree node stream. </i></p>
<h2>Detailed Description</h2>
<p> Definition of the ANTLR3 common tree node stream. </p>
<h2>Define Documentation</h2>
<h3>#define DEFAULT_INITIAL_BUFFER_SIZE 100</h3>
<p> Token buffer initial size settings ( will auto increase). </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>#define INITIAL_CALL_STACK_SIZE 10</h3>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and reset().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_COMMON_TREE_NODE_STREAM</code>&quot;</p>
<h3>typedef struct <code>ANTLR3_TREE_NODE_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TREE_NODE_STREAM</code>&quot;</p>
<h3>typedef struct <code>ANTLR3_TREE_WALK_STATE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TREE_WALK_STATE</code>&quot; </p>
<p> This structure is used to save the state information in the treenodestream when walking ahead with cyclic DFA or for syntactic predicates, we need to record the state of the tree node stream. This class wraps up the current state of the CommonTreeNodeStream. Calling <code>mark()</code> will push another of these on the markers stack.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
