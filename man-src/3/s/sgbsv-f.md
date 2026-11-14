---
title: "sgbsv-f(3)"
name: "sgbsv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbsv-f/"
description: "sgbsv.f –"
---

<p>sgbsv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine sgbsv (N, KL, KU, NRHS, AB, LDAB, IPIV, B, LDB, INFO)


SGBSV computes the solution to system of linear equations A * X = B for GB matrices (simple driver)</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgbsv (integerN, integerKL, integerKU, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code> SGBSV computes the solution to system of linear equations A * X = B for GB matrices</code> (simple driver) </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SGBSV computes the solution to a real system of linear equations
 A * X = B, where A is a band matrix of order N with KL subdiagonals
 and KU superdiagonals, and X and B are N-by-NRHS matrices.
 The LU decomposition with partial pivoting and row interchanges is
 used to factor A as A = L * U, where L is a product of permutation
 and unit lower triangular matrices with KL subdiagonals, and U is
 upper triangular with KL+KU superdiagonals. The factored form of A
 is then used to solve the system of equations A * X = B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
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
<pre> AB is REAL array, dimension (LDAB,N)
 On entry, the matrix A in band storage, in rows KL+1 to
 2*KL+KU+1; rows 1 to KL of the array need not be set.
 The j-th column of A is stored in the j-th column of the
 array AB as follows:
 AB(KL+KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+KL)
 On exit, details of the factorization: U is stored as an
 upper triangular band matrix with KL+KU superdiagonals in
 rows 1 to KL+KU+1, and the multipliers used during the
 factorization are stored in rows KL+KU+2 to 2*KL+KU+1.
 See below for further details.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices that define the permutation matrix P;
 row i of the matrix was interchanged with row IPIV(i).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
 On entry, the N-by-NRHS right hand side matrix B.
 On exit, if INFO = 0, the N-by-NRHS solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, U(i,i) is exactly zero. The factorization
 has been completed, but the factor U is exactly
 singular, and the solution has not been computed.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The band storage scheme is illustrated by the following example, when
 M = N = 6, KL = 2, KU = 1:
 On entry: On exit:
 * * * + + + * * * u14 u25 u36
 * * + + + + * * u13 u24 u35 u46
 * a12 a23 a34 a45 a56 * u12 u23 u34 u45 u56
 a11 a22 a33 a44 a55 a66 u11 u22 u33 u44 u55 u66
 a21 a32 a43 a54 a65 * m21 m32 m43 m54 m65 *
 a31 a42 a53 a64 * * m31 m42 m53 m64 * *
 Array elements marked * are not used by the routine; elements marked
 + need not be set on entry, but are required by the routine to store
 elements of U because of fill-in resulting from the row interchanges.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 163 of file sgbsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
