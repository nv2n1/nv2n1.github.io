---
title: "antlr3-wordnumber(3)"
name: "antlr3-wordnumber"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-wordnumber/"
description: "src/antlr3bitset.c –"
---

<p>src/antlr3bitset.c &#8211; </p>
<p> Contains the C implementation of ANTLR3 bitsets as adapted from Terence Parr&#8217;s Java implementation.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>antlr3BitsetAdd</code> (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> bit) </p>
<p> static <code>pANTLR3_BITSET</code> <code>antlr3BitsetClone</code> (<code>pANTLR3_BITSET</code> inSet) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetCopy</code> (<code>pANTLR3_BITSET_LIST</code> blist) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>antlr3BitsetEquals</code> (<code>pANTLR3_BITSET</code> bitset1, <code>pANTLR3_BITSET</code> bitset2) </p>
<p> static void <code>antlr3BitsetFree</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>antlr3BitsetIsNil</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetList</code> (<code>pANTLR3_HASH_TABLE</code> list) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetLoad</code> (<code>pANTLR3_BITSET_LIST</code> inBits)<br />
 <i>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>antlr3BitsetMember</code> (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_UINT32</code> bit) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetNew</code> (<code>ANTLR3_UINT32</code> numBits) </p>
<p> static <code>ANTLR3_UINT32</code> <code>antlr3BitsetNumBits</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetOf</code> (<code>ANTLR3_INT32</code> bit,&#8230;)<br />
 <i>Creates a new bitset with at least one element, but as many elements are required. </i><br />
 static <code>pANTLR3_BITSET</code> <code>antlr3BitsetOR</code> (<code>pANTLR3_BITSET</code> bitset1, <code>pANTLR3_BITSET</code> bitset2) </p>
<p> static void <code>antlr3BitsetORInPlace</code> (<code>pANTLR3_BITSET</code> bitset, <code>pANTLR3_BITSET</code> bitset2) </p>
<p> static void <code>antlr3BitsetRemove</code> (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_UINT32</code> bit) </p>
<p> ANTLR3_API void <code>antlr3BitsetSetAPI</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> static <code>ANTLR3_UINT32</code> <code>antlr3BitsetSize</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> static <code>pANTLR3_INT32</code> <code>antlr3BitsetToIntList</code> (<code>pANTLR3_BITSET</code> bitset)<br />
 <i>Produce an integer list of all the bits that are turned on in this bitset. </i><br />
 static <code>ANTLR3_UINT64</code> <code>bitMask</code> (<code>ANTLR3_UINT32</code> bitNumber) </p>
<p> static void <code>grow</code> (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> newSize) </p>
<p> static void <code>growToInclude</code> (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> bit) </p>
<p> static <code>ANTLR3_UINT32</code> <code>numWordsToHold</code> (<code>ANTLR3_UINT32</code> bit) </p>
<p> static <code>ANTLR3_UINT32</code> <code>wordNumber</code> (<code>ANTLR3_UINT32</code> bit) </p>
<h2>Detailed Description</h2>
<p>Contains the C implementation of ANTLR3 bitsets as adapted from Terence Parr&#8217;s Java implementation. </p>
<h2>Function Documentation</h2>
<h3>static void antlr3BitsetAdd (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> bit) [static]</h3>
<p>References bitMask(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, growToInclude(), ANTLR3_BITSET_LIST_struct::length, and wordNumber(). </p>
<p> Referenced by antlr3BitsetOf(), and antlr3BitsetSetAPI().</p>
<h3>static <code>pANTLR3_BITSET</code> antlr3BitsetClone (<code>pANTLR3_BITSET</code> inSet) [static]</h3>
<p>References ANTLR3_BITSET_BITS, ANTLR3_MEMCPY, antlr3BitsetNew(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetOR(), and antlr3BitsetSetAPI().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetCopy (<code>pANTLR3_BITSET_LIST</code> blist)</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_MEMCPY, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length.</p>
<h3>static <code>ANTLR3_BOOLEAN</code> antlr3BitsetEquals (<code>pANTLR3_BITSET</code> bitset1, <code>pANTLR3_BITSET</code> bitset2) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static void antlr3BitsetFree (<code>pANTLR3_BITSET</code> bitset) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_BITSET_LIST_struct::bits, and ANTLR3_BITSET_struct::blist. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> antlr3BitsetIsNil (<code>pANTLR3_BITSET</code> bitset) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetList (<code>pANTLR3_HASH_TABLE</code> list)</h3>
<p>References ANTLR3_BITSET_struct::add, ANTLR3_SUCCESS, antlr3BitsetNew(), antlr3EnumNew(), ANTLR3_HASH_ENUM_struct::free, and ANTLR3_HASH_ENUM_struct::next. </p>
<p> Referenced by getTokensList().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetLoad (<code>pANTLR3_BITSET_LIST</code> inBits)</h3>
<p>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>bset</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new bit set with all of the specified bitmaps in it and the API initialized.</dl>
<p> Call as:</p>
<dl COMPACT>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetLoad(bset, bset11, &#8230;, -1);</p>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Stdargs function &#8211; must supply -1 as last paremeter, which is NOT added to the set.</dl>
<p> References antlr3BitsetNew(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, ANTLR3_BITSET_struct::grow, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by combineFollows(), displayRecognitionError(), mismatchIsMissingToken(), and recoverFromMismatchedElement().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> antlr3BitsetMember (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_UINT32</code> bit) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, bitMask(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, ANTLR3_BITSET_LIST_struct::length, and wordNumber(). </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetNew (<code>ANTLR3_UINT32</code> numBits)</h3>
<p>References ANTLR3_BITSET_BITS, ANTLR3_BITSET_LOG_BITS, ANTLR3_FREE, ANTLR3_MALLOC, antlr3BitsetSetAPI(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by addEdge(), antlr3BitsetClone(), antlr3BitsetList(), antlr3BitsetLoad(), antlr3BitsetOf(), combineFollows(), and sortToArray().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3BitsetNumBits (<code>pANTLR3_BITSET</code> bitset) [static]</h3>
<p>References ANTLR3_BITSET_LOG_BITS, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetOf (<code>ANTLR3_INT32</code> bit, &#8230;)</h3>
<p>Creates a new bitset with at least one element, but as many elements are required. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>bit</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new bit set with all of the specified elements added into it.</dl>
<p> Call as:</p>
<dl COMPACT>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(n, n1, n2, -1);</p>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Stdargs function &#8211; must supply -1 as last paremeter, which is NOT added to the set.</dl>
<p> References antlr3BitsetAdd(), and antlr3BitsetNew(). </p>
<p> Referenced by getTokensType().</p>
<h3>static <code>pANTLR3_BITSET</code> antlr3BitsetOR (<code>pANTLR3_BITSET</code> bitset1, <code>pANTLR3_BITSET</code> bitset2) [static]</h3>
<p>References antlr3BitsetClone(), and antlr3BitsetORInPlace(). </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static void antlr3BitsetORInPlace (<code>pANTLR3_BITSET</code> bitset, <code>pANTLR3_BITSET</code> bitset2) [static]</h3>
<p>References ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, growToInclude(), and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetOR(), and antlr3BitsetSetAPI().</p>
<h3>static void antlr3BitsetRemove (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_UINT32</code> bit) [static]</h3>
<p>References bitMask(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and wordNumber(). </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>ANTLR3_API void antlr3BitsetSetAPI (<code>pANTLR3_BITSET</code> bitset)</h3>
<p>References ANTLR3_BITSET_struct::add, antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetEquals(), antlr3BitsetFree(), antlr3BitsetIsNil(), antlr3BitsetMember(), antlr3BitsetNumBits(), antlr3BitsetOR(), antlr3BitsetORInPlace(), antlr3BitsetRemove(), antlr3BitsetSize(), antlr3BitsetToIntList(), ANTLR3_BITSET_struct::bor, ANTLR3_BITSET_struct::borInPlace, ANTLR3_BITSET_struct::clone, ANTLR3_BITSET_struct::equals, ANTLR3_BITSET_struct::free, grow(), ANTLR3_BITSET_struct::grow, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::isNilNode, ANTLR3_BITSET_struct::numBits, ANTLR3_BITSET_struct::remove, ANTLR3_BITSET_struct::size, and ANTLR3_BITSET_struct::toIntList. </p>
<p> Referenced by antlr3BitsetNew().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3BitsetSize (<code>pANTLR3_BITSET</code> bitset) [static]</h3>
<p>References ANTLR3_BITSET_BITS, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static <code>pANTLR3_INT32</code> antlr3BitsetToIntList (<code>pANTLR3_BITSET</code> bitset) [static]</h3>
<p>Produce an integer list of all the bits that are turned on in this bitset. Used for error processing in the main as the bitset reresents a number of integer tokens which we use for follow sets and so on. </p>
<p> The first entry is the number of elements following in the list. </p>
<p> References ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::numBits, and ANTLR3_BITSET_struct::size. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static <code>ANTLR3_UINT64</code> bitMask (<code>ANTLR3_UINT32</code> bitNumber) [static]</h3>
<p>References ANTLR3_BITSET_MOD_MASK. </p>
<p> Referenced by antlr3BitsetAdd(), antlr3BitsetMember(), and antlr3BitsetRemove().</p>
<h3>static void grow (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> newSize) [static]</h3>
<p>References ANTLR3_CALLOC, ANTLR3_FREE, ANTLR3_MEMCPY, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by antlr3BitsetSetAPI().</p>
<h3>static void growToInclude (<code>pANTLR3_BITSET</code> bitset, <code>ANTLR3_INT32</code> bit) [static]</h3>
<p>References ANTLR3_BITSET_struct::blist, ANTLR3_BITSET_struct::grow, ANTLR3_BITSET_LIST_struct::length, and numWordsToHold(). </p>
<p> Referenced by antlr3BitsetAdd(), and antlr3BitsetORInPlace().</p>
<h3>static <code>ANTLR3_UINT32</code> numWordsToHold (<code>ANTLR3_UINT32</code> bit) [static]</h3>
<p>References ANTLR3_BITSET_LOG_BITS. </p>
<p> Referenced by growToInclude().</p>
<h3>static <code>ANTLR3_UINT32</code> wordNumber (<code>ANTLR3_UINT32</code> bit) [static]</h3>
<p>References ANTLR3_BITSET_LOG_BITS. </p>
<p> Referenced by antlr3BitsetAdd(), antlr3BitsetMember(), and antlr3BitsetRemove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
