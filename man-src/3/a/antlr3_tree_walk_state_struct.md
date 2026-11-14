---
title: "antlr3_tree_walk_state_struct(3)"
name: "antlr3_tree_walk_state_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_tree_walk_state_struct/"
description: "ANTLR3_TREE_WALK_STATE_struct –"
---

<p>ANTLR3_TREE_WALK_STATE_struct &#8211; </p>
<p> This structure is used to save the state information in the treenodestream when walking ahead with cyclic DFA or for syntactic predicates, we need to record the state of the tree node stream.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3commontreenodestream.h">antlr3commontreenodestream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_MARKER</code> <code>absoluteNodeIndex</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>currentChildIndex</code> </p>
<p> <code>pANTLR3_BASE_TREE</code> <code>currentNode</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>head</code> </p>
<p> <code>pANTLR3_BASE_TREE</code> * <code>lookAhead</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>lookAheadLength</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>nodeStackSize</code> </p>
<p> <code>pANTLR3_BASE_TREE</code> <code>previousNode</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>tail</code> </p>
<h2>Detailed Description</h2>
<p>This structure is used to save the state information in the treenodestream when walking ahead with cyclic DFA or for syntactic predicates, we need to record the state of the tree node stream. </p>
<p> This class wraps up the current state of the CommonTreeNodeStream. Calling <code>mark()</code> will push another of these on the markers stack.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_TREE_WALK_STATE_struct::absoluteNodeIndex</code></h3>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TREE_WALK_STATE_struct::currentChildIndex</code></h3>
<h3><code>pANTLR3_BASE_TREE</code> <code>ANTLR3_TREE_WALK_STATE_struct::currentNode</code></h3>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TREE_WALK_STATE_struct::head</code></h3>
<h3><code>pANTLR3_BASE_TREE</code>* <code>ANTLR3_TREE_WALK_STATE_struct::lookAhead</code></h3>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TREE_WALK_STATE_struct::lookAheadLength</code></h3>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TREE_WALK_STATE_struct::nodeStackSize</code></h3>
<h3><code>pANTLR3_BASE_TREE</code> <code>ANTLR3_TREE_WALK_STATE_struct::previousNode</code></h3>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TREE_WALK_STATE_struct::tail</code></h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
