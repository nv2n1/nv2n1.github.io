---
title: "zhegst(3)"
name: "zhegst"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhegst/"
description: "zhegst.f –"
---

<p>zhegst.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhegst</code> (ITYPE, UPLO, N, A, LDA, B, LDB, INFO)<br />
 <i></i><code>ZHEGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhegst (integerITYPE, characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>ZHEGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHEGST reduces a complex Hermitian-definite generalized
 eigenproblem to standard form.
 If ITYPE = 1, the problem is A*x = lambda*B*x,
 and A is overwritten by inv(U**H)*A*inv(U) or inv(L)*A*inv(L**H)
 If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or
 B*A*x = lambda*x, and A is overwritten by U*A*U**H or L**H*A*L.
 B must have been previously factorized as U**H*U or L*L**H by ZPOTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ITYPE</i> </p>
<pre> ITYPE is INTEGER
 = 1: compute inv(U**H)*A*inv(U) or inv(L)*A*inv(L**H);
 = 2 or 3: compute U*A*U**H or L**H*A*L.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored and B is factored as
 U**H*U;
 = 'L': Lower triangle of A is stored and B is factored as
 L*L**H.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the leading
 N-by-N upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading N-by-N lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, if INFO = 0, the transformed matrix, stored in the
 same format as A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 The triangular factor from the Cholesky factorization of B,
 as returned by ZPOTRF.</pre>
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
<dd>September 2012</dl>
<p> Definition at line 128 of file zhegst.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
