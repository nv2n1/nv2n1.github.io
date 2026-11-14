---
title: "cheevd-f(3)"
name: "cheevd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cheevd-f/"
description: "cheevd.f –"
---

<p>cheevd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cheevd</code> (JOBZ, UPLO, N, A, LDA, W, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code> CHEEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cheevd (characterJOBZ, characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )W, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code> CHEEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHEEVD computes all eigenvalues and, optionally, eigenvectors of a
 complex Hermitian matrix A. If eigenvectors are desired, it uses a
 divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> A is COMPLEX array, dimension (LDA, N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the
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
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The length of the array WORK.
 If N &lt;= 1, LWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LWORK must be at least N + 1.
 If JOBZ = 'V' and N &gt; 1, LWORK must be at least 2*N + N**2.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal sizes of the WORK, RWORK and
 IWORK arrays, returns these values as the first entries of
 the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array,
 dimension (LRWORK)
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the optimal LRWORK.</pre>
<p><i>LRWORK</i> </p>
<pre> LRWORK is INTEGER
 The dimension of the array RWORK.
 If N &lt;= 1, LRWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LRWORK must be at least N.
 If JOBZ = 'V' and N &gt; 1, LRWORK must be at least
 1 + 5*N + 2*N**2.
 If LRWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK.
 If N &lt;= 1, LIWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LIWORK must be at least 1.
 If JOBZ = 'V' and N &gt; 1, LIWORK must be at least 3 + 5*N.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i and JOBZ = 'N', then the algorithm failed
 to converge; i off-diagonal elements of an intermediate
 tridiagonal form did not converge to zero;
 if INFO = i and JOBZ = 'V', then the algorithm failed
 to compute an eigenvalue while working on the submatrix
 lying in rows and columns INFO/(N+1) through
 mod(INFO,N+1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>Modified description of INFO. Sven, 16 Feb 05.</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 205 of file cheevd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
