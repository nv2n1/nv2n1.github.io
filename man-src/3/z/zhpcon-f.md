---
title: "zhpcon-f(3)"
name: "zhpcon-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhpcon-f/"
description: "zhpcon.f –"
---

<p>zhpcon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhpcon</code> (UPLO, N, AP, IPIV, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>ZHPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhpcon (characterUPLO, integerN, complex*16, dimension( * )AP, integer, dimension( * )IPIV, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZHPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPCON estimates the reciprocal of the condition number of a complex
 Hermitian packed matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by ZHPTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**H;
 = 'L': Lower triangular, form is A = L*D*L**H.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by ZHPTRF, stored as a
 packed triangular matrix.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZHPTRF.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is DOUBLE PRECISION
 The 1-norm of the original matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
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
<p> Definition at line 119 of file zhpcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
