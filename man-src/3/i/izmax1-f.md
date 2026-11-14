---
title: "izmax1-f(3)"
name: "izmax1-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-izmax1-f/"
description: "izmax1.f –"
---

<p>izmax1.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>izmax1</code> (N, CX, INCX)<br />
 <i></i><code>IZMAX1</code> finds the index of the vector element whose real part has maximum absolute value.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function izmax1 (integerN, complex*16, dimension( * )CX, integerINCX)</h3>
<p><code>IZMAX1</code> finds the index of the vector element whose real part has maximum absolute value. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> IZMAX1 finds the index of the element whose real part has maximum
 absolute value.
 Based on IZAMAX from Level 1 BLAS.
 The change is to use the 'genuine' absolute value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of elements in the vector CX.</pre>
<p><i>CX</i> </p>
<pre> CX is COMPLEX*16 array, dimension (N)
 The vector whose elements will be summed.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The spacing between successive values of CX. INCX &gt;= 1.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Nick Higham for use with ZLACON.</dl>
<p> Definition at line 82 of file izmax1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
