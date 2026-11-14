---
title: "zhbevd-f(3)"
name: "zhbevd-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhbevd-f/"
description: "zhbevd.f –"
---

<p>zhbevd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhbevd</code> (JOBZ, UPLO, N, KD, AB, LDAB, W, Z, LDZ, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code> ZHBEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhbevd (characterJOBZ, characterUPLO, integerN, integerKD, complex*16, dimension( ldab, * )AB, integerLDAB, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code> ZHBEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHBEVD computes all the eigenvalues and, optionally, eigenvectors of
 a complex Hermitian band matrix A. If eigenvectors are desired, it
 uses a divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
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
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB, N)
 On entry, the upper or lower triangle of the Hermitian band
 matrix A, stored in the first KD+1 rows of the array. The
 j-th column of A is stored in the j-th column of the array AB
 as follows:
 if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
 On exit, AB is overwritten by values generated during the
 reduction to tridiagonal form. If UPLO = 'U', the first
 superdiagonal and the diagonal of the tridiagonal matrix T
 are returned in rows KD and KD+1 of AB, and if UPLO = 'L',
 the diagonal and first subdiagonal of T are returned in the
 first two rows of AB.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD + 1.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
 eigenvectors of the matrix A, with the i-th column of Z
 holding the eigenvector associated with W(i).
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If N &lt;= 1, LWORK must be at least 1.
 If JOBZ = 'N' and N &gt; 1, LWORK must be at least N.
 If JOBZ = 'V' and N &gt; 1, LWORK must be at least 2*N**2.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal sizes of the WORK, RWORK and
 IWORK arrays, returns these values as the first entries of
 the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array,
 dimension (LRWORK)
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the optimal LRWORK.</pre>
<p><i>LRWORK</i> </p>
<pre> LRWORK is INTEGER
 The dimension of array RWORK.
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
 The dimension of array IWORK.
 If JOBZ = 'N' or N &lt;= 1, LIWORK must be at least 1.
 If JOBZ = 'V' and N &gt; 1, LIWORK must be at least 3 + 5*N .
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
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
<p> Definition at line 215 of file zhbevd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
