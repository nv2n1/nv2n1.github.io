---
title: "cposv(3)"
name: "cposv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cposv/"
description: "cposv.f –"
---

<h2 class="name">NAME</h2>
<p> cposv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cposv</code> (UPLO, N, NRHS, A, LDA, B, LDB, INFO)<br />
 <i></i><code> CPOSV computes the solution to system of linear equations A * X = B for PO matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cposv (characterUPLO, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code> CPOSV computes the solution to system of linear equations A * X = B for PO matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPOSV computes the solution to a complex system of linear equations
    A * X = B,
 where A is an N-by-N Hermitian positive definite matrix and X and B
 are N-by-NRHS matrices.
 The Cholesky decomposition is used to factor A as
    A = U**H* U,  if UPLO = 'U', or
    A = L * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and  L is a lower triangular
 matrix.  The factored form of A is then used to solve the system of
 equations A * X = B.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of linear equations, i.e., the order of the
          matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the Hermitian matrix A.  If UPLO = 'U', the leading
          N-by-N upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if INFO = 0, the factor U or L from the Cholesky
          factorization A = U**H*U or A = L*L**H.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS right hand side matrix B.
          On exit, if INFO = 0, the N-by-NRHS solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the leading minor of order i of A is not
                positive definite, so the factorization could not be
                completed, and the solution has not been computed.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2011</dl>
<p> Definition at line 131 of file cposv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
