---
title: "zhetrs2(3)"
name: "zhetrs2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhetrs2/"
description: "zhetrs2.f –"
---

<p>zhetrs2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhetrs2</code> (UPLO, N, NRHS, A, LDA, IPIV, B, LDB, WORK, INFO)<br />
 <i></i><code>ZHETRS2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhetrs2 (characterUPLO, integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZHETRS2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHETRS2 solves a system of linear equations A*X = B with a complex
 Hermitian matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by ZHETRF and converted by ZSYCONV.</pre>
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
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
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
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 On entry, the right hand side matrix B.
 On exit, the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (N)</pre>
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
<p> Definition at line 127 of file zhetrs2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
