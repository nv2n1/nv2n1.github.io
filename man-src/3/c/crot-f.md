---
title: "crot-f(3)"
name: "crot-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-crot-f/"
description: "crot.f –"
---

<p>crot.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>crot</code> (N, CX, INCX, CY, INCY, C, S)<br />
 <i></i><code>CROT</code> applies a plane rotation with real cosine and complex sine to a pair of complex vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine crot (integerN, complex, dimension( * )CX, integerINCX, complex, dimension( * )CY, integerINCY, realC, complexS)</h3>
<p><code>CROT</code> applies a plane rotation with real cosine and complex sine to a pair of complex vectors. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CROT applies a plane rotation, where the cos (C) is real and the
 sin (S) is complex, and the vectors CX and CY are complex.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of elements in the vectors CX and CY.</pre>
<p><i>CX</i> </p>
<pre> CX is COMPLEX array, dimension (N)
 On input, the vector X.
 On output, CX is overwritten with C*X + S*Y.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of CY. INCX &lt;&gt; 0.</pre>
<p><i>CY</i> </p>
<pre> CY is COMPLEX array, dimension (N)
 On input, the vector Y.
 On output, CY is overwritten with -CONJG(S)*X + C*Y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between successive values of CY. INCX &lt;&gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is REAL</pre>
<p><i>S</i> </p>
<pre> S is COMPLEX
 C and S define a rotation
 [ C S ]
 [ -conjg(S) C ]
 where C*C + S*CONJG(S) = 1.0.</pre>
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
<p> Definition at line 104 of file crot.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
