---
title: "chpcon-f(3)"
name: "chpcon-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chpcon-f/"
description: "chpcon.f –"
---

<p>chpcon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>chpcon</code> (UPLO, N, AP, IPIV, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>CHPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chpcon (characterUPLO, integerN, complex, dimension( * )AP, integer, dimension( * )IPIV, realANORM, realRCOND, complex, dimension( * )WORK, integerINFO)</h3>
<p><code>CHPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHPCON estimates the reciprocal of the condition number of a complex
 Hermitian packed matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by CHPTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by CHPTRF, stored as a
 packed triangular matrix.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by CHPTRF.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is REAL
 The 1-norm of the original matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is REAL
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (2*N)</pre>
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
<p> Definition at line 119 of file chpcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
