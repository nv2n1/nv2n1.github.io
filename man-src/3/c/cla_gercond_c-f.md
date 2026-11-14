---
title: "cla_gercond_c-f(3)"
name: "cla_gercond_c-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_gercond_c-f/"
description: "cla_gercond_c.f –"
---

<p>cla_gercond_c.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>cla_gercond_c</code> (TRANS, N, A, LDA, AF, LDAF, IPIV, C, CAPPLY, INFO, WORK, RWORK)<br />
 <i></i><code>CLA_GERCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function cla_gercond_c (characterTRANS, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, real, dimension( * )C, logicalCAPPLY, integerINFO, complex, dimension( * )WORK, real, dimension( * )RWORK)</h3>
<p><code>CLA_GERCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general matrices. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLA_GERCOND_C computes the infinity norm condition number of
 op(A) * inv(diag(C)) where C is a REAL vector.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the N-by-N matrix A</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX array, dimension (LDAF,N)
 The factors L and U from the factorization
 A = P*L*U as computed by CGETRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices from the factorization A = P*L*U
 as computed by CGETRF; row i of the matrix was interchanged
 with row IPIV(i).</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (N)
 The vector C in the formula op(A) * inv(diag(C)).</pre>
<p><i>CAPPLY</i> </p>
<pre> CAPPLY is LOGICAL
 If .TRUE. then access the vector C in the formula above.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: Successful exit.
 i &gt; 0: The ith argument is invalid.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (2*N).
 Workspace.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (N).
 Workspace.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 142 of file cla_gercond_c.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
