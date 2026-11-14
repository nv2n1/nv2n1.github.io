---
title: "antlr3_bitset_struct(3)"
name: "antlr3_bitset_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_bitset_struct/"
description: "ANTLR3_BITSET_struct –"
---

<p>ANTLR3_BITSET_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>add</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_INT32</code> bit) </p>
<p> <code>ANTLR3_BITSET_LIST</code> <code>blist</code><br />
 <i>The actual bits themselves. </i><br />
 <code>pANTLR3_BITSET</code>(* <code>bor</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset1, struct <code>ANTLR3_BITSET_struct</code> *bitset2) </p>
<p> void(* <code>borInPlace</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset, struct <code>ANTLR3_BITSET_struct</code> *bitset2) </p>
<p> <code>pANTLR3_BITSET</code>(* <code>clone</code> )(struct <code>ANTLR3_BITSET_struct</code> *inSet) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>equals</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset1, struct <code>ANTLR3_BITSET_struct</code> *bitset2) </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset) </p>
<p> void(* <code>grow</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_INT32</code> newSize) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>isMember</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_UINT32</code> bit) </p>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>isNilNode</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>numBits</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset) </p>
<p> void(* <code>remove</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_UINT32</code> bit) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset) </p>
<p> <code>pANTLR3_INT32</code>(* <code>toIntList</code> )(struct <code>ANTLR3_BITSET_struct</code> *bitset) </p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_BITSET_struct::add</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_INT32</code> bit)</h3>
<p>Referenced by addEdge(), antlr3BitsetList(), antlr3BitsetSetAPI(), and DFS().</p>
<h3><code>ANTLR3_BITSET_LIST</code> <code>ANTLR3_BITSET_struct::blist</code></h3>
<p>The actual bits themselves. </p>
<p> Referenced by antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetCopy(), antlr3BitsetEquals(), antlr3BitsetFree(), antlr3BitsetIsNil(), antlr3BitsetLoad(), antlr3BitsetMember(), antlr3BitsetNew(), antlr3BitsetNumBits(), antlr3BitsetORInPlace(), antlr3BitsetRemove(), antlr3BitsetSize(), grow(), and growToInclude().</p>
<h3><code>pANTLR3_BITSET</code>(* <code>ANTLR3_BITSET_struct::bor</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset1, struct <code>ANTLR3_BITSET_struct</code> *bitset2)</h3>
<p>Referenced by antlr3BitsetSetAPI().</p>
<h3>void(* <code>ANTLR3_BITSET_struct::borInPlace</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset, struct <code>ANTLR3_BITSET_struct</code> *bitset2)</h3>
<p>Referenced by antlr3BitsetSetAPI(), combineFollows(), and mismatchIsMissingToken().</p>
<h3><code>pANTLR3_BITSET</code>(* <code>ANTLR3_BITSET_struct::clone</code>)(struct <code>ANTLR3_BITSET_struct</code> *inSet)</h3>
<p>Referenced by antlr3BitsetSetAPI().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BITSET_struct::equals</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset1, struct <code>ANTLR3_BITSET_struct</code> *bitset2)</h3>
<p>Referenced by antlr3BitsetSetAPI().</p>
<h3>void(* <code>ANTLR3_BITSET_struct::free</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset)</h3>
<p>Referenced by antlr3BitsetSetAPI(), combineFollows(), freeTopo(), getTokensList(), getTokensType(), mismatchIsMissingToken(), recover(), and recoverFromMismatchedElement().</p>
<h3>void(* <code>ANTLR3_BITSET_struct::grow</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_INT32</code> newSize)</h3>
<p>Referenced by antlr3BitsetLoad(), antlr3BitsetSetAPI(), and growToInclude().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BITSET_struct::isMember</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_UINT32</code> bit)</h3>
<p>Referenced by antlr3BitsetSetAPI(), antlr3BitsetToIntList(), combineFollows(), DFS(), getTokensSet(), mismatchIsMissingToken(), recoverFromMismatchedElement(), and sortToArray().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BITSET_struct::isNilNode</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset)</h3>
<p>Referenced by antlr3BitsetSetAPI().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BITSET_struct::numBits</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset)</h3>
<p>Referenced by antlr3BitsetSetAPI(), antlr3BitsetToIntList(), DFS(), and displayRecognitionError().</p>
<h3>void(* <code>ANTLR3_BITSET_struct::remove</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset, <code>ANTLR3_UINT32</code> bit)</h3>
<p>Referenced by antlr3BitsetSetAPI(), combineFollows(), mismatchIsMissingToken(), and recoverFromMismatchedElement().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BITSET_struct::size</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset)</h3>
<p>Referenced by antlr3BitsetSetAPI(), antlr3BitsetToIntList(), DFS(), and displayRecognitionError().</p>
<h3><code>pANTLR3_INT32</code>(* <code>ANTLR3_BITSET_struct::toIntList</code>)(struct <code>ANTLR3_BITSET_struct</code> *bitset)</h3>
<p>Referenced by antlr3BitsetSetAPI(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
