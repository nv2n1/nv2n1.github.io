---
title: "dpbcon(3)"
name: "dpbcon"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpbcon/"
description: "dpbcon.f –"
---

<h2 class="name">NAME</h2>
<p> dpbcon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dpbcon</code> (UPLO, N, KD, AB, LDAB, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>DPBCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpbcon (characterUPLO, integerN, integerKD, double precision, dimension( ldab, * )AB, integerLDAB, double precisionANORM, double precisionRCOND, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DPBCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DPBCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite band matrix using the
 Cholesky factorization A = U**T*U or A = L*L**T computed by DPBTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangular factor stored in AB;
          = 'L':  Lower triangular factor stored in AB.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>KD</i> </p>
<pre>
          KD is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'.  KD &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is DOUBLE PRECISION array, dimension (LDAB,N)
          The triangular factor U or L from the Cholesky factorization
          A = U**T*U or A = L*L**T of the band matrix A, stored in the
          first KD+1 rows of the array.  The j-th column of U or L is
          stored in the j-th column of the array AB as follows:
          if UPLO ='U', AB(kd+1+i-j,j) = U(i,j) for max(1,j-kd)&lt;=i&lt;=j;
          if UPLO ='L', AB(1+i-j,j)    = L(i,j) for j&lt;=i&lt;=min(n,j+kd).
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KD+1.
</pre>
<p> <i>ANORM</i> </p>
<pre>
          ANORM is DOUBLE PRECISION
          The 1-norm (or infinity-norm) of the symmetric band matrix A.
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is DOUBLE PRECISION
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
          estimate of the 1-norm of inv(A) computed in this routine.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (3*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd> November 2011</dl>
<p> Definition at line 132 of file dpbcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
