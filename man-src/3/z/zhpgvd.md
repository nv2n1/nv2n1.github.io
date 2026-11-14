---
title: "zhpgvd(3)"
name: "zhpgvd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhpgvd/"
description: "zhpgvd.f –"
---

<p>zhpgvd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhpgvd</code> (ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>ZHPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhpgvd (integerITYPE, characterJOBZ, characterUPLO, integerN, complex*16, dimension( * )AP, complex*16, dimension( * )BP, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>ZHPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPGVD computes all the eigenvalues and, optionally, the eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x, A*Bx=(lambda)*x, or B*A*x=(lambda)*x. Here A and
 B are assumed to be Hermitian, stored in packed format, and B is also
 positive definite.
 If eigenvectors are desired, it uses a divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ITYPE</i> </p>
<pre> ITYPE is INTEGER
 Specifies the problem type to be solved:
 = 1: A*x = (lambda)*B*x
 = 2: A*B*x = (lambda)*x
 = 3: B*A*x = (lambda)*x</pre>
<p><i>JOBZ</i> </p>
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
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 On exit, the contents of AP are destroyed.</pre>
<p><i>BP</i> </p>
<pre> BP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 B, packed columnwise in a linear array. The j-th column of B
 is stored in the array BP as follows:
 if UPLO = 'U', BP(i + (j-1)*j/2) = B(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j&lt;=i&lt;=n.
 On exit, the triangular factor U or L from the Cholesky
 factorization B = U**H*U or B = L*L**H, in the same storage
 format as B.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of
 eigenvectors. The eigenvectors are normalized as follows:
 if ITYPE = 1 or 2, Z**H*B*Z = I;
 if ITYPE = 3, Z**H*inv(B)*Z = I.
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the required LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If N &lt;= 1, LWORK &gt;= 1.
 If JOBZ = 'N' and N &gt; 1, LWORK &gt;= N.
 If JOBZ = 'V' and N &gt; 1, LWORK &gt;= 2*N.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the required sizes of the WORK, RWORK and
 IWORK arrays, returns these values as the first entries of
 the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (MAX(1,LRWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the required LRWORK.</pre>
<p><i>LRWORK</i> </p>
<pre> LRWORK is INTEGER
 The dimension of array RWORK.
 If N &lt;= 1, LRWORK &gt;= 1.
 If JOBZ = 'N' and N &gt; 1, LRWORK &gt;= N.
 If JOBZ = 'V' and N &gt; 1, LRWORK &gt;= 1 + 5*N + 2*N**2.
 If LRWORK = -1, then a workspace query is assumed; the
 routine only calculates the required sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the required LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of array IWORK.
 If JOBZ = 'N' or N &lt;= 1, LIWORK &gt;= 1.
 If JOBZ = 'V' and N &gt; 1, LIWORK &gt;= 3 + 5*N.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the required sizes of the WORK, RWORK
 and IWORK arrays, returns these values as the first entries
 of the WORK, RWORK and IWORK arrays, and no error message
 related to LWORK or LRWORK or LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: ZPPTRF or ZHPEVD returned an error code:
 &lt;= N: if INFO = i, ZHPEVD failed to converge;
 i off-diagonal elements of an intermediate
 tridiagonal form did not convergeto zero;
 &gt; N: if INFO = N + i, for 1 &lt;= i &lt;= n, then the leading
 minor of order i of B is not positive definite.
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
<p> Definition at line 231 of file zhpgvd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
