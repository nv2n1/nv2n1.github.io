---
title: "spotri-4(3)"
name: "spotri-4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spotri-4/"
description: "spotri.f –"
---

<p>spotri.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>spotri</code> (UPLO, N, A, LDA, INFO)<br />
 <i></i><code>SPOTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spotri (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>SPOTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPOTRI computes the inverse of a real symmetric positive definite
 matrix A using the Cholesky factorization A = U**T*U or A = L*L**T
 computed by SPOTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the triangular factor U or L from the Cholesky
 factorization A = U**T*U or A = L*L**T, as computed by
 SPOTRF.
 On exit, the upper or lower triangle of the (symmetric)
 inverse of A, overwriting the input factor U or L.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the (i,i) element of the factor U or L is
 zero, and the inverse could not be computed.</pre>
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
<p> Definition at line 96 of file spotri.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
