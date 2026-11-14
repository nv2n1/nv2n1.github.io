---
title: "cpotf2(3)"
name: "cpotf2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpotf2/"
description: "cpotf2.f –"
---

<h2 class="name">NAME</h2>
<p> cpotf2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpotf2</code> (UPLO, N, A, LDA, INFO)<br />
 <i></i><code>CPOTF2</code> computes the Cholesky factorization of a symmetric/Hermitian positive definite matrix (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpotf2 (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p> <code>CPOTF2</code> computes the Cholesky factorization of a symmetric/Hermitian positive definite matrix (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPOTF2 computes the Cholesky factorization of a complex Hermitian
 positive definite matrix A.
 The factorization has the form
    A = U**H * U ,  if UPLO = 'U', or
    A = L  * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.
 This is the unblocked version of the algorithm, calling Level 2 BLAS.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the upper or lower triangular part of the
          Hermitian matrix A is stored.
          = 'U':  Upper triangular
          = 'L':  Lower triangular
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the Hermitian matrix A.  If UPLO = 'U', the leading
          n by n upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading n by n lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if INFO = 0, the factor U or L from the Cholesky
          factorization A = U**H *U  or A = L*L**H.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -k, the k-th argument had an illegal value
          &gt; 0: if INFO = k, the leading minor of order k is not
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
<dd> September 2012</dl>
<p> Definition at line 110 of file cpotf2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
