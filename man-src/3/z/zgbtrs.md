---
title: "zgbtrs(3)"
name: "zgbtrs"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgbtrs/"
description: "zgbtrs.f –"
---

<p>zgbtrs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgbtrs</code> (TRANS, N, KL, KU, NRHS, AB, LDAB, IPIV, B, LDB, INFO)<br />
 <i></i><code>ZGBTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgbtrs (characterTRANS, integerN, integerKL, integerKU, integerNRHS, complex*16, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, complex*16, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>ZGBTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGBTRS solves a system of linear equations
 A * X = B, A**T * X = B, or A**H * X = B
 with a general band matrix A using the LU factorization computed
 by ZGBTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations.
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose)</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB,N)
 Details of the LU factorization of the band matrix A, as
 computed by ZGBTRF. U is stored as an upper triangular band
 matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
 the multipliers used during the factorization are stored in
 rows KL+KU+2 to 2*KL+KU+1.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices; for 1 &lt;= i &lt;= N, row i of the matrix was
 interchanged with row IPIV(i).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 On entry, the right hand side matrix B.
 On exit, the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 138 of file zgbtrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
