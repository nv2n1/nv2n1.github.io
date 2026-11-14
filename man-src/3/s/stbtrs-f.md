---
title: "stbtrs-f(3)"
name: "stbtrs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stbtrs-f/"
description: "stbtrs.f –"
---

<p>stbtrs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stbtrs</code> (UPLO, TRANS, DIAG, N, KD, NRHS, AB, LDAB, B, LDB, INFO)<br />
 <i></i><code>STBTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stbtrs (characterUPLO, characterTRANS, characterDIAG, integerN, integerKD, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>STBTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STBTRS solves a triangular system of the form
 A * X = B or A**T * X = B,
 where A is a triangular band matrix of order N, and B is an
 N-by NRHS matrix. A check is made to verify that A is nonsingular.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose = Transpose)</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 = 'N': A is non-unit triangular;
 = 'U': A is unit triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals or subdiagonals of the
 triangular band matrix A. KD &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is REAL array, dimension (LDAB,N)
 The upper or lower triangular band matrix A, stored in the
 first kd+1 rows of AB. The j-th column of A is stored
 in the j-th column of the array AB as follows:
 if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
 If DIAG = 'U', the diagonal elements of A are not referenced
 and are assumed to be 1.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD+1.</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
 On entry, the right hand side matrix B.
 On exit, if INFO = 0, the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the i-th diagonal element of A is zero,
 indicating that the matrix is singular and the
 solutions X have not been computed.</pre>
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
<p> Definition at line 146 of file stbtrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
