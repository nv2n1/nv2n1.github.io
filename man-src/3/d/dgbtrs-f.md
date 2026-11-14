---
title: "dgbtrs-f(3)"
name: "dgbtrs-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgbtrs-f/"
description: "dgbtrs.f –"
---

<p>dgbtrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgbtrs</code> (TRANS, N, KL, KU, NRHS, AB, LDAB, IPIV, B, LDB, INFO)<br />
 <i></i><code>DGBTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgbtrs (characterTRANS, integerN, integerKL, integerKU, integerNRHS, double precision, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>DGBTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGBTRS solves a system of linear equations
 A * X = B or A**T * X = B
 with a general band matrix A using the LU factorization computed
 by DGBTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations.
 = 'N': A * X = B (No transpose)
 = 'T': A**T* X = B (Transpose)
 = 'C': A**T* X = B (Conjugate transpose = Transpose)</pre>
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
<pre> AB is DOUBLE PRECISION array, dimension (LDAB,N)
 Details of the LU factorization of the band matrix A, as
 computed by DGBTRF. U is stored as an upper triangular band
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
<pre> B is DOUBLE PRECISION array, dimension (LDB,NRHS)
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
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 138 of file dgbtrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
