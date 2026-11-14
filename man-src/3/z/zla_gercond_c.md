---
title: "zla_gercond_c(3)"
name: "zla_gercond_c"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zla_gercond_c/"
description: "zla_gercond_c.f –"
---

<p>zla_gercond_c.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zla_gercond_c</code> (TRANS, N, A, LDA, AF, LDAF, IPIV, C, CAPPLY, INFO, WORK, RWORK)<br />
 <i></i><code>ZLA_GERCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zla_gercond_c (characterTRANS, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, double precision, dimension( * )C, logicalCAPPLY, integerINFO, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK)</h3>
<p><code>ZLA_GERCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLA_GERCOND_C computes the infinity norm condition number of
 op(A) * inv(diag(C)) where C is a DOUBLE PRECISION vector.</pre>
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
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the N-by-N matrix A</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 The factors L and U from the factorization
 A = P*L*U as computed by ZGETRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices from the factorization A = P*L*U
 as computed by ZGETRF; row i of the matrix was interchanged
 with row IPIV(i).</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (N)
 The vector C in the formula op(A) * inv(diag(C)).</pre>
<p><i>CAPPLY</i> </p>
<pre> CAPPLY is LOGICAL
 If .TRUE. then access the vector C in the formula above.</pre>
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
<p> Definition at line 142 of file zla_gercond_c.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
