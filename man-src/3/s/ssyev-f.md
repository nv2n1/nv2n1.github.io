---
title: "ssyev-f(3)"
name: "ssyev-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssyev-f/"
description: "ssyev.f –"
---

<p>ssyev.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssyev</code> (JOBZ, UPLO, N, A, LDA, W, WORK, LWORK, INFO)<br />
 <i></i><code> SSYEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssyev (characterJOBZ, characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )W, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> SSYEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYEV computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric matrix A.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA, N)
 On entry, the symmetric matrix A. If UPLO = 'U', the
 leading N-by-N upper triangular part of A contains the
 upper triangular part of the matrix A. If UPLO = 'L',
 the leading N-by-N lower triangular part of A contains
 the lower triangular part of the matrix A.
 On exit, if JOBZ = 'V', then if INFO = 0, A contains the
 orthonormal eigenvectors of the matrix A.
 If JOBZ = 'N', then on exit the lower triangle (if UPLO='L')
 or the upper triangle (if UPLO='U') of A, including the
 diagonal, is destroyed.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The length of the array WORK. LWORK &gt;= max(1,3*N-1).
 For optimal efficiency, LWORK &gt;= (NB+2)*N,
 where NB is the blocksize for SSYTRD returned by ILAENV.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the algorithm failed to converge; i
 off-diagonal elements of an intermediate tridiagonal
 form did not converge to zero.</pre>
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
<p> Definition at line 133 of file ssyev.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
