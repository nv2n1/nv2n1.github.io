---
title: "chbgv-f(3)"
name: "chbgv-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chbgv-f/"
description: "chbgv.f –"
---

<p>chbgv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>chbgv</code> (JOBZ, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, W, Z, LDZ, WORK, RWORK, INFO)<br />
 <i></i><code>CHBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chbgv (characterJOBZ, characterUPLO, integerN, integerKA, integerKB, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldbb, * )BB, integerLDBB, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CHBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHBGV computes all the eigenvalues, and optionally, the eigenvectors
 of a complex generalized Hermitian-definite banded eigenproblem, of
 the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian
 and banded, and B is also positive definite.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> AB is COMPLEX array, dimension (LDAB, N)
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
<pre> BB is COMPLEX array, dimension (LDBB, N)
 On entry, the upper or lower triangle of the Hermitian band
 matrix B, stored in the first kb+1 rows of the array. The
 j-th column of B is stored in the j-th column of the array BB
 as follows:
 if UPLO = 'U', BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)&lt;=i&lt;=j;
 if UPLO = 'L', BB(1+i-j,j) = B(i,j) for j&lt;=i&lt;=min(n,j+kb).
 On exit, the factor S from the split Cholesky factorization
 B = S**H*S, as returned by CPBSTF.</pre>
<p><i>LDBB</i> </p>
<pre> LDBB is INTEGER
 The leading dimension of the array BB. LDBB &gt;= KB+1.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX array, dimension (LDZ, N)
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
<pre> WORK is COMPLEX array, dimension (N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (3*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is:
 &lt;= N: the algorithm failed to converge:
 i off-diagonal elements of an intermediate
 tridiagonal form did not converge to zero;
 &gt; N: if INFO = N + i, for 1 &lt;= i &lt;= N, then CPBSTF
 returned INFO = i: B is not positive definite.
 The factorization of B could not be completed and
 no eigenvalues or eigenvectors were computed.</pre>
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
<p> Definition at line 183 of file chbgv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
