---
title: "dpocon-f(3)"
name: "dpocon-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpocon-f/"
description: "dpocon.f –"
---

<p>dpocon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dpocon</code> (UPLO, N, A, LDA, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>DPOCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpocon (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, double precisionANORM, double precisionRCOND, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>DPOCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DPOCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite matrix using the
 Cholesky factorization A = U**T*U or A = L*L**T computed by DPOTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 The triangular factor U or L from the Cholesky factorization
 A = U**T*U or A = L*L**T, as computed by DPOTRF.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is DOUBLE PRECISION
 The 1-norm (or infinity-norm) of the symmetric matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
 estimate of the 1-norm of inv(A) computed in this routine.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (3*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)</pre>
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
<p> Definition at line 121 of file dpocon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
