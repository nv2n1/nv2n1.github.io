---
title: "antlr3-leftn(3)"
name: "antlr3-leftn"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-leftn/"
description: "ANTLR3_INT_TRIE_NODE_struct –"
---

<p>ANTLR3_INT_TRIE_NODE_struct &#8211; </p>
<p> Structure that defines an element/node in an ANTLR3_INT_TRIE.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_UINT32</code> <code>bitNum</code><br />
 <i>This is the left/right bit index for traversal along the nodes. </i><br />
 <code>pANTLR3_TRIE_ENTRY</code> <code>buckets</code><br />
 <i>This is the data bucket(s) that the key indexes, which may be NULL. </i><br />
 <code>ANTLR3_INTKEY</code> <code>key</code><br />
 <i>This is the actual key that the entry represents if it is a terminal node. </i><br />
 struct <code>ANTLR3_INT_TRIE_NODE_struct</code> * <code>leftN</code><br />
 <i>Pointer to the left node from here when sKey &amp; bitNum = 0. </i><br />
 struct <code>ANTLR3_INT_TRIE_NODE_struct</code> * <code>rightN</code><br />
 <i>Pointer to the right node from here when sKey &amp; bitNum, = 1. </i></p>
<h2>Detailed Description</h2>
<p>Structure that defines an element/node in an ANTLR3_INT_TRIE.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INT_TRIE_NODE_struct::bitNum</code></h3>
<p>This is the left/right bit index for traversal along the nodes. </p>
<p> Referenced by antlr3IntTrieNew(), freeIntNode(), intTrieAdd(), and intTrieGet().</p>
<h3><code>pANTLR3_TRIE_ENTRY</code> <code>ANTLR3_INT_TRIE_NODE_struct::buckets</code></h3>
<p>This is the data bucket(s) that the key indexes, which may be NULL. </p>
<p> Referenced by freeIntNode(), intTrieAdd(), and intTrieGet().</p>
<h3><code>ANTLR3_INTKEY</code> <code>ANTLR3_INT_TRIE_NODE_struct::key</code></h3>
<p>This is the actual key that the entry represents if it is a terminal node. </p>
<p> Referenced by intTrieAdd(), and intTrieGet().</p>
<h3>struct <code>ANTLR3_INT_TRIE_NODE_struct</code>* <code>ANTLR3_INT_TRIE_NODE_struct::leftN</code> [read]</h3>
<p>Pointer to the left node from here when sKey &amp; bitNum = 0. </p>
<p> Referenced by antlr3IntTrieNew(), freeIntNode(), intTrieAdd(), and intTrieGet().</p>
<h3>struct <code>ANTLR3_INT_TRIE_NODE_struct</code>* <code>ANTLR3_INT_TRIE_NODE_struct::rightN</code> [read]</h3>
<p>Pointer to the right node from here when sKey &amp; bitNum, = 1. </p>
<p> Referenced by antlr3IntTrieNew(), freeIntNode(), intTrieAdd(), and intTrieGet(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
