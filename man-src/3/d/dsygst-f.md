---
title: "dsygst-f(3)"
name: "dsygst-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsygst-f/"
description: "dsygst.f –"
---

<p>dsygst.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsygst</code> (ITYPE, UPLO, N, A, LDA, B, LDB, INFO)<br />
 <i></i><code>DSYGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsygst (integerITYPE, characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>DSYGST</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSYGST reduces a real symmetric-definite generalized eigenproblem
 to standard form.
 If ITYPE = 1, the problem is A*x = lambda*B*x,
 and A is overwritten by inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T)
 If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or
 B*A*x = lambda*x, and A is overwritten by U*A*U**T or L**T*A*L.
 B must have been previously factorized as U**T*U or L*L**T by DPOTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ITYPE</i> </p>
<pre> ITYPE is INTEGER
 = 1: compute inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T);
 = 2 or 3: compute U*A*U**T or L**T*A*L.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored and B is factored as
 U**T*U;
 = 'L': Lower triangle of A is stored and B is factored as
 L*L**T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the symmetric matrix A. If UPLO = 'U', the leading
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
<pre> B is DOUBLE PRECISION array, dimension (LDB,N)
 The triangular factor from the Cholesky factorization of B,
 as returned by DPOTRF.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
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
<p> Definition at line 128 of file dsygst.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
