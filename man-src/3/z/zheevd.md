---
title: "zheevd(3)"
name: "zheevd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zheevd/"
---

zheevd.f -

<h2>Synopsis</h2>



<h3>Functions/Subroutines</h3>

subroutine <b>zheevd</b> (JOBZ, UPLO, N, A, LDA, W, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO) 
 <i></i><b> ZHEEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</b>

<h2>Function/Subroutine Documentation</h2>

<h3>subroutine zheevd (characterJOBZ, characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, double precision, dimension( * )W, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>

<b> ZHEEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</b> 

 <b>Purpose: </b>
<dl><dd><pre> ZHEEVD computes all eigenvalues and, optionally, eigenvectors of a
 complex Hermitian matrix A. If eigenvectors are desired, it uses a
 divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl><dd><i>JOBZ</i> 

 <pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre><i>UPLO</i> 

 <pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre><i>N</i> 

 <pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre><i>A</i> 

 <pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the
 leading N-by-N upper triangular part of A contains the
 upper triangular part of the matrix A. If UPLO = 'L',
 the leading N-by-N lower triangular part of A contains
 the lower triangular part of the matrix A.
 On exit, if JOBZ = 'V', then if INFO = 0, A contains the
 orthonormal eigenvectors of the matrix A.
 If JOBZ = 'N', then on exit the lower triangle (if UPLO='L')
 or the upper triangle (if UPLO='U') of A, including the
 diagonal, is destroyed.</pre><i>LDA</i> 

 <pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre><i>W</i> 

 <pre> W is DOUBLE PRECISION array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre><i>WORK</i> 

 <pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre><i>LWORK</i> 

 <pre> LWORK is INTEGER
 The length of the array WORK.
 If N &lt;= 1, LWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LWORK must be at least N + 1.
 If JOBZ = 'V' and N &gt; 1, LWORK must be at least 2*N + N**2.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal sizes of the WORK, RWORK and
 IWORK arrays, returns these values as the first entries of
 the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre><i>RWORK</i> 

 <pre> RWORK is DOUBLE PRECISION array,
 dimension (LRWORK)
 On exit, if INFO = 0, <a HREF="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the optimal LRWORK.</pre><i>LRWORK</i> 

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
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre><i>IWORK</i> 

 <pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a HREF="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre><i>LIWORK</i> 

 <pre> LIWORK is INTEGER
 The dimension of the array IWORK.
 If N &lt;= 1, LIWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LIWORK must be at least 1.
 If JOBZ = 'V' and N &gt; 1, LIWORK must be at least 3 + 5*N.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre><i>INFO</i> 

 <pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i and JOBZ = 'N', then the algorithm failed
 to converge; i off-diagonal elements of an intermediate
 tridiagonal form did not converge to zero;
 if INFO = i and JOBZ = 'V', then the algorithm failed
 to compute an eigenvalue while working on the submatrix
 lying in rows and columns INFO/(N+1) through
 mod(INFO,N+1).</pre>&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl><dd>Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl><dd>November 2011</dl>
 

 <b>Further Details: </b>
<dl><dd>Modified description of INFO. Sven, 16 Feb 05.</dl>
 

 <b>Contributors: </b>
<dl><dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
 

 

 

 Definition at line 205 of file zheevd.f.

<h2>Author</h2>

Generated automatically by Doxygen for LAPACK from the source code.
