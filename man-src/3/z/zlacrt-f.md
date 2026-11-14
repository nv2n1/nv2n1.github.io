---
title: "zlacrt-f(3)"
name: "zlacrt-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlacrt-f/"
description: "zlacrt.f –"
---

<p>zlacrt.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlacrt</code> (N, CX, INCX, CY, INCY, C, S)<br />
 <i></i><code>ZLACRT</code> performs a linear transformation of a pair of complex vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlacrt (integerN, complex*16, dimension( * )CX, integerINCX, complex*16, dimension( * )CY, integerINCY, complex*16C, complex*16S)</h3>
<p><code>ZLACRT</code> performs a linear transformation of a pair of complex vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLACRT performs the operation
 ( c s )( x ) ==&gt; ( x )
 ( -s c )( y ) ( y )
 where c and s are complex and the vectors x and y are complex.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of elements in the vectors CX and CY.</pre>
<p><i>CX</i> </p>
<pre> CX is COMPLEX*16 array, dimension (N)
 On input, the vector x.
 On output, CX is overwritten with c*x + s*y.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of CX. INCX &lt;&gt; 0.</pre>
<p><i>CY</i> </p>
<pre> CY is COMPLEX*16 array, dimension (N)
 On input, the vector y.
 On output, CY is overwritten with -s*x + c*y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between successive values of CY. INCY &lt;&gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16</pre>
<p><i>S</i> </p>
<pre> S is COMPLEX*16
 C and S define the matrix
 [ C S ].
 [ -S C ]</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 106 of file zlacrt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
