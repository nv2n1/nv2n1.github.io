---
title: "zdrot(3)"
name: "zdrot"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdrot/"
description: "zdrot.f –"
---

<p>zdrot.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zdrot</code> (N, CX, INCX, CY, INCY, C, S)<br />
 <i></i><code>ZDROT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zdrot (integerN, complex*16, dimension( * )CX, integerINCX, complex*16, dimension( * )CY, integerINCY, double precisionC, double precisionS)</h3>
<p><code>ZDROT</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Applies a plane rotation, where the cos and sin (c and s) are real
 and the vectors cx and cy are complex.
 jack dongarra, linpack, 3/11/78.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the vectors cx and cy.
 N must be at least zero.</pre>
<p><i>CX</i> </p>
<pre> CX is COMPLEX*16 array, dimension at least
 ( 1 + ( N - 1 )*abs( INCX ) ).
 Before entry, the incremented array CX must contain the n
 element vector cx. On exit, CX is overwritten by the updated
 vector cx.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 CX. INCX must not be zero.</pre>
<p><i>CY</i> </p>
<pre> CY is COMPLEX*16 array, dimension at least
 ( 1 + ( N - 1 )*abs( INCY ) ).
 Before entry, the incremented array CY must contain the n
 element vector cy. On exit, CY is overwritten by the updated
 vector cy.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 On entry, INCY specifies the increment for the elements of
 CY. INCY must not be zero.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION
 On entry, C specifies the cosine, cos.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION
 On entry, S specifies the sine, sin.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 99 of file zdrot.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
