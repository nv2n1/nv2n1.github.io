---
title: "ssytri2-f(3)"
name: "ssytri2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytri2-f/"
description: "ssytri2.f –"
---

<p>ssytri2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssytri2</code> (UPLO, N, A, LDA, IPIV, WORK, LWORK, INFO)<br />
 <i></i><code>SSYTRI2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytri2 (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SSYTRI2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYTRI2 computes the inverse of a REAL symmetric indefinite matrix
 A using the factorization A = U*D*U**T or A = L*D*L**T computed by
 SSYTRF. SSYTRI2 sets the LEADING DIMENSION of the workspace
 before calling SSYTRI2X that actually computes the inverse.</pre>
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
 On entry, the NB diagonal matrix D and the multipliers
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
 Details of the interchanges and the NB structure of D
 as determined by SSYTRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (N+NB+1)*(NB+3)</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 WORK is size &gt;= (N+NB+1)*(NB+3)
 If LDWORK = -1, then a workspace query is assumed; the routine
 calculates:
 - the optimal size of the WORK array, returns
 this value as the first entry of the WORK array,
 - and no error message related to LDWORK is issued by XERBLA.</pre>
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
<dd>September 2012</dl>
<p> Definition at line 128 of file ssytri2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
