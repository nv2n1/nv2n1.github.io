---
title: "antlr3-current(3)"
name: "antlr3-current"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-current/"
description: "ANTLR3_INT_TRIE_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_INT_TRIE_struct &#8211; </p>
<p> Structure that defines an ANTLR3_INT_TRIE.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>add</code> )(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key, <code>ANTLR3_UINT32</code> type, <code>ANTLR3_INTKEY</code> intVal, void *data, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>allowDups</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>count</code> </p>
<p> <code>pANTLR3_INT_TRIE_NODE</code> <code>current</code> </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>del</code> )(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_INT_TRIE_struct</code> *trie) </p>
<p> <code>pANTLR3_TRIE_ENTRY</code>(* <code>get</code> )(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key) </p>
<p> <code>pANTLR3_INT_TRIE_NODE</code> <code>root</code> </p>
<h2>Detailed Description</h2>
<p> Structure that defines an ANTLR3_INT_TRIE. </p>
<p> For this particular implementation, as you might expect, the key is turned into a &#8216;string&#8217; by looking at bit(key, depth) of the integer key. Using 64 bit keys gives us a depth limit of 64 (or bit 0..63) and potentially a huge trie. This is the algorithm for a Patricia Trie. Note also that this trie [can] accept multiple entries for the same key and is therefore a kind of elastic bucket patricia trie. </p>
<p> If you find this code useful, please feel free to &#8216;steal&#8217; it for any purpose as covered by the BSD license under which ANTLR is issued. You can cut the code but as the ANTLR library is only about 50K (Windows Vista), you might find it easier to just link the library. Please keep all comments and licenses and so on in any version of this you create of course. </p>
<p> Jim Idle.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_INT_TRIE_struct::add</code>)(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key, <code>ANTLR3_UINT32</code> type, <code>ANTLR3_INTKEY</code> intVal, void *data, void(ANTLR3_CDECL *freeptr)(void *))</h3>
<p> Referenced by antlr3IntTrieNew(), getRuleMemoization(), and memoize().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_INT_TRIE_struct::allowDups</code></h3>
<p> Referenced by intTrieAdd().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INT_TRIE_struct::count</code></h3>
<p> Referenced by antlr3IntTrieNew(), intTrieAdd(), and intTrieGet().</p>
<h3><code>pANTLR3_INT_TRIE_NODE</code> <code>ANTLR3_INT_TRIE_struct::current</code></h3>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_INT_TRIE_struct::del</code>)(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key)</h3>
<p> Referenced by antlr3IntTrieNew().</p>
<h3>void(* <code>ANTLR3_INT_TRIE_struct::free</code>)(struct <code>ANTLR3_INT_TRIE_struct</code> *trie)</h3>
<p> Referenced by antlr3IntTrieNew(), freeBR(), and reset().</p>
<h3><code>pANTLR3_TRIE_ENTRY</code>(* <code>ANTLR3_INT_TRIE_struct::get</code>)(struct <code>ANTLR3_INT_TRIE_struct</code> *trie, <code>ANTLR3_INTKEY</code> key)</h3>
<p> Referenced by antlr3IntTrieNew(), getRuleMemoization(), and memoize().</p>
<h3><code>pANTLR3_INT_TRIE_NODE</code> <code>ANTLR3_INT_TRIE_struct::root</code></h3>
<p> Referenced by antlr3IntTrieNew(), intTrieAdd(), intTrieDel(), intTrieFree(), and intTrieGet(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
