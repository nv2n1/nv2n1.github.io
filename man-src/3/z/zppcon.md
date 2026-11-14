---
title: "zppcon(3)"
name: "zppcon"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zppcon/"
description: "zppcon.f –"
---

<p>zppcon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zppcon</code> (UPLO, N, AP, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>ZPPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zppcon (characterUPLO, integerN, complex*16, dimension( * )AP, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZPPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPPCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite packed matrix using
 the Cholesky factorization A = U**H*U or A = L*L**H computed by
 ZPPTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 The triangular factor U or L from the Cholesky factorization
 A = U**H*U or A = L*L**H, packed columnwise in a linear
 array. The j-th column of U or L is stored in the array AP
 as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j&lt;=i&lt;=n.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is DOUBLE PRECISION
 The 1-norm (or infinity-norm) of the Hermitian matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
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
<p> Definition at line 119 of file zppcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
