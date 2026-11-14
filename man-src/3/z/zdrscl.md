---
title: "zdrscl(3)"
name: "zdrscl"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdrscl/"
description: "zdrscl.f –"
---

<p>zdrscl.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zdrscl</code> (N, SA, SX, INCX)<br />
 <i></i><code>ZDRSCL</code> multiplies a vector by the reciprocal of a real scalar.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zdrscl (integerN, double precisionSA, complex*16, dimension( * )SX, integerINCX)</h3>
<p><code>ZDRSCL</code> multiplies a vector by the reciprocal of a real scalar. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZDRSCL multiplies an n-element complex vector x by the real scalar
 1/a. This is done without overflow or underflow as long as
 the final result x/a does not overflow or underflow.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of components of the vector x.</pre>
<p><i>SA</i> </p>
<pre> SA is DOUBLE PRECISION
 The scalar a which is used to divide each component of x.
 SA must be &gt;= 0, or the subroutine will divide by zero.</pre>
<p><i>SX</i> </p>
<pre> SX is COMPLEX*16 array, dimension
 (1+(N-1)*abs(INCX))
 The n-element vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of the vector SX.
 &gt; 0: <a href="//www.systutorials.com/docs/linux/man/1-SX/">SX</a>(1) = <a href="//www.systutorials.com/docs/linux/man/1-X/">X</a>(1) and SX(1+(i-1)*INCX) = x(i), 1&lt; i&lt;= n</pre>
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
<p> Definition at line 85 of file zdrscl.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
