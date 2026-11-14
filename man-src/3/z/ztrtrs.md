---
title: "ztrtrs(3)"
name: "ztrtrs"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztrtrs/"
description: "ztrtrs.f –"
---

<p>ztrtrs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztrtrs</code> (UPLO, TRANS, DIAG, N, NRHS, A, LDA, B, LDB, INFO)<br />
 <i></i><code>ZTRTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztrtrs (characterUPLO, characterTRANS, characterDIAG, integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>ZTRTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTRTRS solves a triangular system of the form
 A * X = B, A**T * X = B, or A**H * X = B,
 where A is a triangular matrix of order N, and B is an N-by-NRHS
 matrix. A check is made to verify that A is nonsingular.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose)</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 = 'N': A is non-unit triangular;
 = 'U': A is unit triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The triangular matrix A. If UPLO = 'U', the leading N-by-N
 upper triangular part of the array A contains the upper
 triangular matrix, and the strictly lower triangular part of
 A is not referenced. If UPLO = 'L', the leading N-by-N lower
 triangular part of the array A contains the lower triangular
 matrix, and the strictly upper triangular part of A is not
 referenced. If DIAG = 'U', the diagonal elements of A are
 also not referenced and are assumed to be 1.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
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
 indicating that the matrix is singular and the solutions
 X have not been computed.</pre>
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
<p> Definition at line 140 of file ztrtrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
