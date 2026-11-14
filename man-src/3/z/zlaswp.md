---
title: "zlaswp(3)"
name: "zlaswp"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaswp/"
description: "zlaswp.f –"
---

<p>zlaswp.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaswp</code> (N, A, LDA, K1, K2, IPIV, INCX)<br />
 <i></i><code>ZLASWP</code> performs a series of row interchanges on a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaswp (integerN, complex*16, dimension( lda, * )A, integerLDA, integerK1, integerK2, integer, dimension( * )IPIV, integerINCX)</h3>
<p><code>ZLASWP</code> performs a series of row interchanges on a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLASWP performs a series of row interchanges on the matrix A.
 One row interchange is initiated for each of rows K1 through K2 of A.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the matrix of column dimension N to which the row
 interchanges will be applied.
 On exit, the permuted matrix.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A.</pre>
<p><i>K1</i> </p>
<pre> K1 is INTEGER
 The first element of IPIV for which a row interchange will
 be done.</pre>
<p><i>K2</i> </p>
<pre> K2 is INTEGER
 The last element of IPIV for which a row interchange will
 be done.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (K2*abs(INCX))
 The vector of pivot indices. Only the elements in positions
 K1 through K2 of IPIV are accessed.
 IPIV(K) = L implies rows K and L are to be interchanged.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of IPIV. If IPIV
 is negative, the pivots are applied in reverse order.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> Modified by
 R. C. Whaley, Computer Science Dept., Univ. of Tenn., Knoxville, USA</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 115 of file zlaswp.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
