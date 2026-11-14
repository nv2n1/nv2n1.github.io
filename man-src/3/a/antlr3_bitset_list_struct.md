---
title: "antlr3_bitset_list_struct(3)"
name: "antlr3_bitset_list_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_bitset_list_struct/"
description: "ANTLR3_BITSET_LIST_struct –"
---

<p>ANTLR3_BITSET_LIST_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>pANTLR3_BITWORD</code> <code>bits</code><br />
 <i>Pointer to the allocated array of bits for this bit set, which is an array of 64 bit elements (of the architecture). </i><br />
 <code>ANTLR3_UINT32</code> <code>length</code><br />
 <i>Length of the current bit set in ANTLR3_UINT64 units. </i></p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_BITWORD</code> <code>ANTLR3_BITSET_LIST_struct::bits</code></h3>
<p>Pointer to the allocated array of bits for this bit set, which is an array of 64 bit elements (of the architecture). If we find a machine/C compiler that does not know anything about 64 bit values then it should be easy enough to produce a 32 bit (or less) version of the bitset code. Note that the pointer here may be static if laid down by the code generation, and it must be copied if it is to be manipulated to perform followset calculations. </p>
<p> Referenced by antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetCopy(), antlr3BitsetEquals(), antlr3BitsetFree(), antlr3BitsetIsNil(), antlr3BitsetLoad(), antlr3BitsetMember(), antlr3BitsetNew(), antlr3BitsetORInPlace(), antlr3BitsetRemove(), antlr3BitsetSize(), and grow().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_BITSET_LIST_struct::length</code></h3>
<p>Length of the current bit set in ANTLR3_UINT64 units. </p>
<p> Referenced by antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetCopy(), antlr3BitsetEquals(), antlr3BitsetIsNil(), antlr3BitsetLoad(), antlr3BitsetMember(), antlr3BitsetNew(), antlr3BitsetNumBits(), antlr3BitsetORInPlace(), antlr3BitsetSize(), grow(), and growToInclude(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
