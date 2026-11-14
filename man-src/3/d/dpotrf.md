---
title: "dpotrf(3)"
name: "dpotrf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpotrf/"
description: "dpotrf.f –"
---

<h2 class="name">NAME</h2>
<p> dpotrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dpotrf</code> (UPLO, N, A, LDA, INFO)<br />
 <i></i><code>DPOTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpotrf (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p> <code>DPOTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DPOTRF computes the Cholesky factorization of a real symmetric
 positive definite matrix A.
 The factorization has the form
    A = U**T * U,  if UPLO = 'U', or
    A = L  * L**T,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.
 This is the block version of the algorithm, calling Level 3 BLAS.
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
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the symmetric matrix A.  If UPLO = 'U', the leading
          N-by-N upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if INFO = 0, the factor U or L from the Cholesky
          factorization A = U**T*U or A = L*L**T.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the leading minor of order i is not
                positive definite, and the factorization could not be
                completed.
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
<p> Definition at line 108 of file dpotrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
