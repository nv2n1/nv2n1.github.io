---
title: "sppcon-f(3)"
name: "sppcon-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sppcon-f/"
description: "sppcon.f –"
---

<p>sppcon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sppcon</code> (UPLO, N, AP, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>SPPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sppcon (characterUPLO, integerN, real, dimension( * )AP, realANORM, realRCOND, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>SPPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPPCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite packed matrix using
 the Cholesky factorization A = U**T*U or A = L*L**T computed by
 SPPTRF.
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
<pre> AP is REAL array, dimension (N*(N+1)/2)
 The triangular factor U or L from the Cholesky factorization
 A = U**T*U or A = L*L**T, packed columnwise in a linear
 array. The j-th column of U or L is stored in the array AP
 as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j&lt;=i&lt;=n.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is REAL
 The 1-norm (or infinity-norm) of the symmetric matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is REAL
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (3*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)</pre>
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
<p> Definition at line 119 of file sppcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
