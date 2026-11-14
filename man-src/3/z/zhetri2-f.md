---
title: "zhetri2-f(3)"
name: "zhetri2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhetri2-f/"
description: "zhetri2.f –"
---

<p>zhetri2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhetri2</code> (UPLO, N, A, LDA, IPIV, WORK, LWORK, INFO)<br />
 <i></i><code>ZHETRI2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhetri2 (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex*16, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>ZHETRI2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHETRI2 computes the inverse of a COMPLEX*16 hermitian indefinite matrix
 A using the factorization A = U*D*U**T or A = L*D*L**T computed by
 ZHETRF. ZHETRI2 set the LEADING DIMENSION of the workspace
 before calling ZHETRI2X that actually computes the inverse.</pre>
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
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the NB diagonal matrix D and the multipliers
 used to obtain the factor U or L as computed by ZHETRF.
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
 as determined by ZHETRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N+NB+1)*(NB+3)</pre>
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
<dd>November 2011</dl>
<p> Definition at line 128 of file zhetri2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
