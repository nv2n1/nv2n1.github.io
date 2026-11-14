---
title: "sla_gbrcond-3(3)"
name: "sla_gbrcond-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sla_gbrcond-3/"
description: "sla_gbrcond.f –"
---

<p>sla_gbrcond.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>sla_gbrcond</code> (TRANS, N, KL, KU, AB, LDAB, AFB, LDAFB, IPIV, CMODE, C, INFO, WORK, IWORK)<br />
 <i></i><code>SLA_GBRCOND</code> estimates the Skeel condition number for a general banded matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function sla_gbrcond (characterTRANS, integerN, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, integerCMODE, real, dimension( * )C, integerINFO, real, dimension( * )WORK, integer, dimension( * )IWORK)</h3>
<p><code>SLA_GBRCOND</code> estimates the Skeel condition number for a general banded matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLA_GBRCOND Estimates the Skeel condition number of op(A) * op2(C)
 where op2 is determined by CMODE as follows
 CMODE = 1 op2(C) = C
 CMODE = 0 op2(C) = I
 CMODE = -1 op2(C) = inv(C)
 The Skeel condition number cond(A) = norminf( |inv(A)||A| )
 is computed by computing scaling factors R such that
 diag(R)*A*op2(C) is row equilibrated and computing the standard
 infinity-norm condition number.</pre>
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
<pre> AB is REAL array, dimension (LDAB,N)
 On entry, the matrix A in band storage, in rows 1 to KL+KU+1.
 The j-th column of A is stored in the j-th column of the
 array AB as follows:
 AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+kl)</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KL+KU+1.</pre>
<p><i>AFB</i> </p>
<pre> AFB is REAL array, dimension (LDAFB,N)
 Details of the LU factorization of the band matrix A, as
 computed by SGBTRF. U is stored as an upper triangular
 band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1,
 and the multipliers used during the factorization are stored
 in rows KL+KU+2 to 2*KL+KU+1.</pre>
<p><i>LDAFB</i> </p>
<pre> LDAFB is INTEGER
 The leading dimension of the array AFB. LDAFB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices from the factorization A = P*L*U
 as computed by SGBTRF; row i of the matrix was interchanged
 with row IPIV(i).</pre>
<p><i>CMODE</i> </p>
<pre> CMODE is INTEGER
 Determines op2(C) in the formula op(A) * op2(C) as follows:
 CMODE = 1 op2(C) = C
 CMODE = 0 op2(C) = I
 CMODE = -1 op2(C) = inv(C)</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (N)
 The vector C in the formula op(A) * op2(C).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: Successful exit.
 i &gt; 0: The ith argument is invalid.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (5*N).
 Workspace.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N).
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
<p> Definition at line 168 of file sla_gbrcond.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
