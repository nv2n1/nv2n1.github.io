---
title: "zla_gbrcond_x(3)"
name: "zla_gbrcond_x"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zla_gbrcond_x/"
description: "zla_gbrcond_x.f –"
---

<p>zla_gbrcond_x.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zla_gbrcond_x</code> (TRANS, N, KL, KU, AB, LDAB, AFB, LDAFB, IPIV, X, INFO, WORK, RWORK)<br />
 <i></i><code>ZLA_GBRCOND_X</code> computes the infinity norm condition number of op(A)*diag(x) for general banded matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zla_gbrcond_x (characterTRANS, integerN, integerKL, integerKU, complex*16, dimension( ldab, * )AB, integerLDAB, complex*16, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, complex*16, dimension( * )X, integerINFO, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK)</h3>
<p><code>ZLA_GBRCOND_X</code> computes the infinity norm condition number of op(A)*diag(x) for general banded matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLA_GBRCOND_X Computes the infinity norm condition number of
 op(A) * diag(X) where X is a COMPLEX*16 vector.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate Transpose = Transpose)</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB,N)
 On entry, the matrix A in band storage, in rows 1 to KL+KU+1.
 The j-th column of A is stored in the j-th column of the
 array AB as follows:
 AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+kl)</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KL+KU+1.</pre>
<p><i>AFB</i> </p>
<pre> AFB is COMPLEX*16 array, dimension (LDAFB,N)
 Details of the LU factorization of the band matrix A, as
 computed by ZGBTRF. U is stored as an upper triangular
 band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1,
 and the multipliers used during the factorization are stored
 in rows KL+KU+2 to 2*KL+KU+1.</pre>
<p><i>LDAFB</i> </p>
<pre> LDAFB is INTEGER
 The leading dimension of the array AFB. LDAFB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices from the factorization A = P*L*U
 as computed by ZGBTRF; row i of the matrix was interchanged
 with row IPIV(i).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (N)
 The vector X in the formula op(A) * diag(X).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: Successful exit.
 i &gt; 0: The ith argument is invalid.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N).
 Workspace.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N).
 Workspace.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 154 of file zla_gbrcond_x.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
