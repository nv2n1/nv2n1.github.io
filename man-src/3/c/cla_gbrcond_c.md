---
title: "cla_gbrcond_c(3)"
name: "cla_gbrcond_c"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_gbrcond_c/"
description: "cla_gbrcond_c.f –"
---

<h2 class="name">NAME</h2>
<p> cla_gbrcond_c.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>cla_gbrcond_c</code> (TRANS, N, KL, KU, AB, LDAB, AFB, LDAFB, IPIV, C, CAPPLY, INFO, WORK, RWORK)<br />
 <i></i><code>CLA_GBRCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general banded matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function cla_gbrcond_c (characterTRANS, integerN, integerKL, integerKU, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, real, dimension( * )C, logicalCAPPLY, integerINFO, complex, dimension( * )WORK, real, dimension( * )RWORK)</h3>
<p> <code>CLA_GBRCOND_C</code> computes the infinity norm condition number of op(A)*inv(diag(c)) for general banded matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    CLA_GBRCOND_C Computes the infinity norm condition number of
    op(A) * inv(diag(C)) where C is a REAL vector.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
     Specifies the form of the system of equations:
       = 'N':  A * X = B     (No transpose)
       = 'T':  A**T * X = B  (Transpose)
       = 'C':  A**H * X = B  (Conjugate Transpose = Transpose)
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
     The number of linear equations, i.e., the order of the
     matrix A.  N &gt;= 0.
</pre>
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
     The number of subdiagonals within the band of A.  KL &gt;= 0.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
     The number of superdiagonals within the band of A.  KU &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre>
          AB is COMPLEX array, dimension (LDAB,N)
     On entry, the matrix A in band storage, in rows 1 to KL+KU+1.
     The j-th column of A is stored in the j-th column of the
     array AB as follows:
     AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+kl)
</pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
     The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre>
<p> <i>AFB</i> </p>
<pre>
          AFB is COMPLEX array, dimension (LDAFB,N)
     Details of the LU factorization of the band matrix A, as
     computed by CGBTRF.  U is stored as an upper triangular
     band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1,
     and the multipliers used during the factorization are stored
     in rows KL+KU+2 to 2*KL+KU+1.
</pre>
<p> <i>LDAFB</i> </p>
<pre>
          LDAFB is INTEGER
     The leading dimension of the array AFB.  LDAFB &gt;= 2*KL+KU+1.
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
     The pivot indices from the factorization A = P*L*U
     as computed by CGBTRF; row i of the matrix was interchanged
     with row IPIV(i).
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N)
     The vector C in the formula op(A) * inv(diag(C)).
</pre>
<p> <i>CAPPLY</i> </p>
<pre>
          CAPPLY is LOGICAL
     If .TRUE. then access the vector C in the formula above.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
       = 0:  Successful exit.
     i &gt; 0:  The ith argument is invalid.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N).
     Workspace.
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N).
     Workspace.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> Definition at line 160 of file cla_gbrcond_c.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
