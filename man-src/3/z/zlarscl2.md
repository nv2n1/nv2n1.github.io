---
title: "zlarscl2(3)"
name: "zlarscl2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlarscl2/"
description: "zlarscl2.f –"
---

<p>zlarscl2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlarscl2</code> (M, N, D, X, LDX)<br />
 <i></i><code>ZLARSCL2</code> performs reciprocal diagonal scaling on a vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlarscl2 (integerM, integerN, double precision, dimension( * )D, complex*16, dimension( ldx, * )X, integerLDX)</h3>
<p><code>ZLARSCL2</code> performs reciprocal diagonal scaling on a vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARSCL2 performs a reciprocal diagonal scaling on an vector:
 x &lt;-- inv(D) * x
 where the DOUBLE PRECISION diagonal matrix D is stored as a vector.
 Eventually to be replaced by BLAS_zge_diag_scale in the new BLAS
 standard.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of D and X. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of D and X. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, length M
 Diagonal matrix D, stored as a vector of length M.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (LDX,N)
 On entry, the vector X to be scaled by D.
 On exit, the scaled vector.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the vector X. LDX &gt;= 0.</pre>
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
<p> Definition at line 92 of file zlarscl2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
