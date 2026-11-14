---
title: "zlacgv-f(3)"
name: "zlacgv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlacgv-f/"
description: "zlacgv.f –"
---

<p>zlacgv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlacgv</code> (N, X, INCX)<br />
 <i></i><code>ZLACGV</code> conjugates a complex vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlacgv (integerN, complex*16, dimension( * )X, integerINCX)</h3>
<p><code>ZLACGV</code> conjugates a complex vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLACGV conjugates a complex vector of length N.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The length of the vector X. N &gt;= 0.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension
 (1+(N-1)*abs(INCX))
 On entry, the vector of length N to be conjugated.
 On exit, X is overwritten with conjg(X).</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The spacing between successive elements of X.</pre>
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
<p> Definition at line 75 of file zlacgv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
