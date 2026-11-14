---
title: "ssytrs_rook(3)"
name: "ssytrs_rook"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytrs_rook/"
description: "ssytrs_rook.f –"
---

<p>ssytrs_rook.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssytrs_rook</code> (UPLO, N, NRHS, A, LDA, IPIV, B, LDB, INFO)<br />
 <i></i><code>SSYTRS_ROOK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytrs_rook (characterUPLO, integerN, integerNRHS, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>SSYTRS_ROOK</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYTRS_ROOK solves a system of linear equations A*X = B with
 a real symmetric matrix A using the factorization A = U*D*U**T or
 A = L*D*L**T computed by SSYTRF_ROOK.</pre>
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
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by SSYTRF_ROOK.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by SSYTRF_ROOK.</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
 On entry, the right hand side matrix B.
 On exit, the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
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
<dd>April 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>
<pre> April 2012, Igor Kozachenko,
 Computer Science Division,
 University of California, Berkeley
 September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas,
 School of Mathematics,
 University of Manchester</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 136 of file ssytrs_rook.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
