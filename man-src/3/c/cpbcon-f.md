---
title: "cpbcon-f(3)"
name: "cpbcon-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpbcon-f/"
description: "cpbcon.f –"
---

<p>cpbcon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cpbcon</code> (UPLO, N, KD, AB, LDAB, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>CPBCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpbcon (characterUPLO, integerN, integerKD, complex, dimension( ldab, * )AB, integerLDAB, realANORM, realRCOND, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CPBCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CPBCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite band matrix using
 the Cholesky factorization A = U**H*U or A = L*L**H computed by
 CPBTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangular factor stored in AB;
 = 'L': Lower triangular factor stored in AB.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of sub-diagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX array, dimension (LDAB,N)
 The triangular factor U or L from the Cholesky factorization
 A = U**H*U or A = L*L**H of the band matrix A, stored in the
 first KD+1 rows of the array. The j-th column of U or L is
 stored in the j-th column of the array AB as follows:
 if UPLO ='U', AB(kd+1+i-j,j) = U(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO ='L', AB(1+i-j,j) = L(i,j) for j&lt;=i&lt;=min(n,j+kd).</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD+1.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is REAL
 The 1-norm (or infinity-norm) of the Hermitian band matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is REAL
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (N)</pre>
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
<p> Definition at line 133 of file cpbcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
