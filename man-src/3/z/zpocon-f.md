---
title: "zpocon-f(3)"
name: "zpocon-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zpocon-f/"
description: "zpocon.f –"
---

<p>zpocon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zpocon</code> (UPLO, N, A, LDA, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>ZPOCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zpocon (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZPOCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite matrix using the
 Cholesky factorization A = U**H*U or A = L*L**H computed by ZPOTRF.
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
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The triangular factor U or L from the Cholesky factorization
 A = U**H*U or A = L*L**H, as computed by ZPOTRF.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
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
<p> Definition at line 121 of file zpocon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
