---
title: "zsycon_rook(3)"
name: "zsycon_rook"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsycon_rook/"
description: "zsycon_rook.f –"
---

<p>zsycon_rook.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zsycon_rook</code> (UPLO, N, A, LDA, IPIV, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>ZSYCON_ROOK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zsycon_rook (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZSYCON_ROOK</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSYCON_ROOK estimates the reciprocal of the condition number (in the
 1-norm) of a complex symmetric matrix A using the factorization
 A = U*D*U**T or A = L*D*L**T computed by ZSYTRF_ROOK.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**T;
 = 'L': Lower triangular, form is A = L*D*L**T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by ZSYTRF_ROOK.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZSYTRF_ROOK.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd></dl>
<p> November 2011, Igor Kozachenko, Computer Science Division, University of California, Berkeley </p>
<p> September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas, School of Mathematics, University of Manchester </p>
<p> Definition at line 139 of file zsycon_rook.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
