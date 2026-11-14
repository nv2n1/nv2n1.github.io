---
title: "antlr3_bitset_bits(3)"
name: "antlr3_bitset_bits"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_bitset_bits/"
description: "include/antlr3bitset.h –"
---

<p>include/antlr3bitset.h &#8211; </p>
<p> Defines the basic structures of an ANTLR3 bitset.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_BITSET_LIST_struct</code> </p>
<p> struct <code>ANTLR3_BITSET_struct</code> </p>
<h3>Defines</h3>
<p>#define <code>ANTLR3_BITSET_BITS</code> 64<br />
 <i>How many bits in the elements. </i><br />
 #define <code>ANTLR3_BITSET_LOG_BITS</code> 6<br />
 <i>log2 of ANTLR3_BITSET_BITS 2^ANTLR3_BITSET_LOG_BITS = ANTLR3_BITSET_BITS </i><br />
 #define <code>ANTLR3_BITSET_MOD_MASK</code> ANTLR3_BITSET_BITS &#8211; 1<br />
 <i>We will often need to do a mod operator (i mod nbits). </i><br />
 #define <code>ANTLR3_BITSET_NIBBLE</code> 4<br />
 <i>How many bits in a nible of bits. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_BITSET_struct</code> <code>ANTLR3_BITSET</code> </p>
<p> typedef struct <code>ANTLR3_BITSET_LIST_struct</code> <code>ANTLR3_BITSET_LIST</code> </p>
<h2>Detailed Description</h2>
<p>Defines the basic structures of an ANTLR3 bitset. </p>
<p> this is a C version of the cut down Bitset class provided with the java version of antlr 3.</p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_BITSET_BITS 64</h3>
<p>How many bits in the elements. </p>
<p> Referenced by antlr3BitsetClone(), antlr3BitsetNew(), and antlr3BitsetSize().</p>
<h3>#define ANTLR3_BITSET_LOG_BITS 6</h3>
<p>log2 of ANTLR3_BITSET_BITS 2^ANTLR3_BITSET_LOG_BITS = ANTLR3_BITSET_BITS </p>
<p> Referenced by antlr3BitsetNew(), antlr3BitsetNumBits(), numWordsToHold(), and wordNumber().</p>
<h3>#define ANTLR3_BITSET_MOD_MASK ANTLR3_BITSET_BITS &#8211; 1</h3>
<p>We will often need to do a mod operator (i mod nbits). For powers of two, this mod operation is the same as:</p>
<dl COMPACT>
<dt>*</p>
<dd>(i &amp; (nbits-1)).</dl>
<p> Since mod is relatively slow, we use an easily precomputed mod mask to do the mod instead. </p>
<p> Referenced by bitMask().</p>
<h3>#define ANTLR3_BITSET_NIBBLE 4</h3>
<p>How many bits in a nible of bits.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_BITSET_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_BITSET</code>&quot;</p>
<h3>typedef struct <code>ANTLR3_BITSET_LIST_struct</code></h3>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>ANTLR3_BITSET_LIST</code>&quot;</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
