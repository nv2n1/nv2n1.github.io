---
title: "ssytd2(3)"
name: "ssytd2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytd2/"
description: "ssytd2.f –"
---

<h2 class="name">NAME</h2>
<p> ssytd2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssytd2</code> (UPLO, N, A, LDA, D, E, TAU, INFO)<br />
 <i></i><code>SSYTD2</code> reduces a symmetric matrix to real symmetric tridiagonal form by an orthogonal similarity transformation (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytd2 (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )D, real, dimension( * )E, real, dimension( * )TAU, integerINFO)</h3>
<p> <code>SSYTD2</code> reduces a symmetric matrix to real symmetric tridiagonal form by an orthogonal similarity transformation (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSYTD2 reduces a real symmetric matrix A to symmetric tridiagonal
 form T by an orthogonal similarity transformation: Q**T * A * Q = T.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the upper or lower triangular part of the
          symmetric matrix A is stored:
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
          A is REAL array, dimension (LDA,N)
          On entry, the symmetric matrix A.  If UPLO = 'U', the leading
          n-by-n upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading n-by-n lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if UPLO = 'U', the diagonal and first superdiagonal
          of A are overwritten by the corresponding elements of the
          tridiagonal matrix T, and the elements above the first
          superdiagonal, with the array TAU, represent the orthogonal
          matrix Q as a product of elementary reflectors; if UPLO
          = 'L', the diagonal and first subdiagonal of A are over-
          written by the corresponding elements of the tridiagonal
          matrix T, and the elements below the first subdiagonal, with
          the array TAU, represent the orthogonal matrix Q as a product
          of elementary reflectors. See Further Details.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The diagonal elements of the tridiagonal matrix T:
          D(i) = A(i,i).
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          The off-diagonal elements of the tridiagonal matrix T:
          E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is REAL array, dimension (N-1)
          The scalar factors of the elementary reflectors (see Further
          Details).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre><code>
If UPLO = 'U', the matrix Q is represented as a product of elementary
                   reflectors
                       Q = H(n - 1)...H(2) H(1).Each H(i)
has the form
    H(i) = I - tau * v * v * *T where tau is a real scalar,
    and v is a real vector with
    v(i + 1
      : n) = 0 and v(i) = 1;
v(1
  : i - 1) is stored on exit in
    A(1
      : i - 1, i + 1),
    and tau in TAU(i).If UPLO = 'L', the matrix Q is represented as a product of elementary reflectors Q = H(1) H(2)...H(n - 1).Each H(i)
has the form
    H(i) = I - tau * v * v * *T where tau is a real scalar,
    and v is a real vector with
    v(1
      : i) = 0 and v(i + 1) = 1;
v(i + 2
  : n) is stored on exit in A(i + 2
                              : n, i),
    and tau in TAU(i).The contents of A on exit are illustrated by the following examples
        with n = 5 : if UPLO = 'U' : if UPLO = 'L' : (d e v2 v3 v4)(d)(d e v3 v4)(e d)(d e v4)(v1 e d)(d e)(v1 v2 e d)(d)(v1 v2 v3 e d)
                                                         where d
                                                     and
                                                     e denote diagonal and off - diagonal elements of T,
             and vi
                 denotes an element of the vector defining H(i)
                     .
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 174 of file ssytd2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
