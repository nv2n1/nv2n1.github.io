---
title: "ssytri2x-f(3)"
name: "ssytri2x-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytri2x-f/"
description: "ssytri2x.f –"
---

<p>ssytri2x.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssytri2x</code> (UPLO, N, A, LDA, IPIV, WORK, NB, INFO)<br />
 <i></i><code>SSYTRI2X</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytri2x (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, real, dimension( n+nb+1,* )WORK, integerNB, integerINFO)</h3>
<p><code>SSYTRI2X</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYTRI2X computes the inverse of a real symmetric indefinite matrix
 A using the factorization A = U*D*U**T or A = L*D*L**T computed by
 SSYTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**T;
 = 'L': Lower triangular, form is A = L*D*L**T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the NNB diagonal matrix D and the multipliers
 used to obtain the factor U or L as computed by SSYTRF.
 On exit, if INFO = 0, the (symmetric) inverse of the original
 matrix. If UPLO = 'U', the upper triangular part of the
 inverse is formed and the part of A below the diagonal is not
 referenced; if UPLO = 'L' the lower triangular part of the
 inverse is formed and the part of A above the diagonal is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the NNB structure of D
 as determined by SSYTRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (N+NNB+1,NNB+3)</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 Block size</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, D(i,i) = 0; the matrix is singular and its
 inverse could not be computed.</pre>
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
<p> Definition at line 121 of file ssytri2x.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
