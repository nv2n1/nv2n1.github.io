---
title: "zhbgvd-f(3)"
name: "zhbgvd-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhbgvd-f/"
description: "zhbgvd.f –"
---

<p>zhbgvd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhbgvd</code> (JOBZ, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, W, Z, LDZ, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>ZHBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhbgvd (characterJOBZ, characterUPLO, integerN, integerKA, integerKB, complex*16, dimension( ldab, * )AB, integerLDAB, complex*16, dimension( ldbb, * )BB, integerLDBB, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>ZHBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHBGVD computes all the eigenvalues, and optionally, the eigenvectors
 of a complex generalized Hermitian-definite banded eigenproblem, of
 the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian
 and banded, and B is also positive definite. If eigenvectors are
 desired, it uses a divide and conquer algorithm.
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
 = 'U': Upper triangles of A and B are stored;
 = 'L': Lower triangles of A and B are stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>KA</i> </p>
<pre> KA is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KA &gt;= 0.</pre>
<p><i>KB</i> </p>
<pre> KB is INTEGER
 The number of superdiagonals of the matrix B if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KB &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB, N)
 On entry, the upper or lower triangle of the Hermitian band
 matrix A, stored in the first ka+1 rows of the array. The
 j-th column of A is stored in the j-th column of the array AB
 as follows:
 if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+ka).
 On exit, the contents of AB are destroyed.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KA+1.</pre>
<p><i>BB</i> </p>
<pre> BB is COMPLEX*16 array, dimension (LDBB, N)
 On entry, the upper or lower triangle of the Hermitian band
 matrix B, stored in the first kb+1 rows of the array. The
 j-th column of B is stored in the j-th column of the array BB
 as follows:
 if UPLO = 'U', BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)&lt;=i&lt;=j;
 if UPLO = 'L', BB(1+i-j,j) = B(i,j) for j&lt;=i&lt;=min(n,j+kb).
 On exit, the factor S from the split Cholesky factorization
 B = S**H*S, as returned by ZPBSTF.</pre>
<p><i>LDBB</i> </p>
<pre> LDBB is INTEGER
 The leading dimension of the array BB. LDBB &gt;= KB+1.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of
 eigenvectors, with the i-th column of Z holding the
 eigenvector associated with W(i). The eigenvectors are
 normalized so that Z**H*B*Z = I.
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO=0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If N &lt;= 1, LWORK &gt;= 1.
 If JOBZ = 'N' and N &gt; 1, LWORK &gt;= N.
 If JOBZ = 'V' and N &gt; 1, LWORK &gt;= 2*N**2.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal sizes of the WORK, RWORK and
 IWORK arrays, returns these values as the first entries of
 the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (MAX(1,LRWORK))
 On exit, if INFO=0, <a href="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the optimal LRWORK.</pre>
<p><i>LRWORK</i> </p>
<pre> LRWORK is INTEGER
 The dimension of array RWORK.
 If N &lt;= 1, LRWORK &gt;= 1.
 If JOBZ = 'N' and N &gt; 1, LRWORK &gt;= N.
 If JOBZ = 'V' and N &gt; 1, LRWORK &gt;= 1 + 5*N + 2*N**2.
 If LRWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO=0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of array IWORK.
 If JOBZ = 'N' or N &lt;= 1, LIWORK &gt;= 1.
 If JOBZ = 'V' and N &gt; 1, LIWORK &gt;= 3 + 5*N.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is:
 &lt;= N: the algorithm failed to converge:
 i off-diagonal elements of an intermediate
 tridiagonal form did not converge to zero;
 &gt; N: if INFO = N + i, for 1 &lt;= i &lt;= N, then ZPBSTF
 returned INFO = i: B is not positive definite.
 The factorization of B could not be completed and
 no eigenvalues or eigenvectors were computed.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 251 of file zhbgvd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
