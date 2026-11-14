---
title: "zhecon(3)"
name: "zhecon"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhecon/"
description: "zhecon.f –"
---

<p>zhecon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhecon</code> (UPLO, N, A, LDA, IPIV, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>ZHECON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhecon (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZHECON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHECON estimates the reciprocal of the condition number of a complex
 Hermitian matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by ZHETRF.
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
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by ZHETRF.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZHETRF.</pre>
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
<p> Definition at line 125 of file zhecon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
