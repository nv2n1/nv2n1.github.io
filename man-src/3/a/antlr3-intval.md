---
title: "antlr3-intval(3)"
name: "antlr3-intval"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-intval/"
description: "ANTLR3_TRIE_ENTRY_struct –"
---

<p>ANTLR3_TRIE_ENTRY_struct &#8211; </p>
<p> Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Public Member Functions</h3>
<p><code>void</code> (ANTLR3_CDECL *freeptr)(void *) </p>
<h3>Data Fields</h3>
<p>union { </p>
<p> <code>ANTLR3_INTKEY</code> <code>intVal</code> </p>
<p> void * <code>ptr</code> </p>
<p> } <code>data</code> </p>
<p> struct <code>ANTLR3_TRIE_ENTRY_struct</code> * <code>next</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>type</code> </p>
<h2>Detailed Description</h2>
<p>Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE.</p>
<h2>Member Function Documentation</h2>
<h3>ANTLR3_TRIE_ENTRY_struct::void (ANTLR3_CDECL * freeptr)</h3>
<h2>Field Documentation</h2>
<h3>union { &#8230; } <code>ANTLR3_TRIE_ENTRY_struct::data</code></h3>
<p>Referenced by freeIntNode(), getRuleMemoization(), intTrieAdd(), and memoize().</p>
<h3><code>ANTLR3_INTKEY</code> <code>ANTLR3_TRIE_ENTRY_struct::intVal</code></h3>
<p>Referenced by getRuleMemoization(), and intTrieAdd().</p>
<h3>struct <code>ANTLR3_TRIE_ENTRY_struct</code>* <code>ANTLR3_TRIE_ENTRY_struct::next</code> [read]</h3>
<p>Referenced by freeIntNode(), and intTrieAdd().</p>
<h3>void* <code>ANTLR3_TRIE_ENTRY_struct::ptr</code></h3>
<p>Referenced by freeIntNode(), getRuleMemoization(), intTrieAdd(), and memoize().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TRIE_ENTRY_struct::type</code></h3>
<p>Referenced by freeIntNode(), and intTrieAdd(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
