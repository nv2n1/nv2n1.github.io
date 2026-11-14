---
title: "clatrd(3)"
name: "clatrd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clatrd/"
description: "clatrd.f –"
---

<h2 class="name">NAME</h2>
<p> clatrd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clatrd</code> (UPLO, N, NB, A, LDA, E, TAU, W, LDW)<br />
 <i></i><code>CLATRD</code> reduces the first nb rows and columns of a symmetric/Hermitian matrix A to real tridiagonal form by an unitary similarity transformation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clatrd (characterUPLO, integerN, integerNB, complex, dimension( lda, * )A, integerLDA, real, dimension( * )E, complex, dimension( * )TAU, complex, dimension( ldw, * )W, integerLDW)</h3>
<p> <code>CLATRD</code> reduces the first nb rows and columns of a symmetric/Hermitian matrix A to real tridiagonal form by an unitary similarity transformation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLATRD reduces NB rows and columns of a complex Hermitian matrix A to
 Hermitian tridiagonal form by a unitary similarity
 transformation Q**H * A * Q, and returns the matrices V and W which are
 needed to apply the transformation to the unreduced part of A.
 If UPLO = 'U', CLATRD reduces the last NB rows and columns of a
 matrix, of which the upper triangle is supplied;
 if UPLO = 'L', CLATRD reduces the first NB rows and columns of a
 matrix, of which the lower triangle is supplied.
 This is an auxiliary routine called by CHETRD.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the upper or lower triangular part of the
          Hermitian matrix A is stored:
          = 'U': Upper triangular
          = 'L': Lower triangular
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.
</pre>
<p> <i>NB</i> </p>
<pre>
          NB is INTEGER
          The number of rows and columns to be reduced.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is COMPLEX array, dimension(LDA, N) On entry, the Hermitian matrix A.If UPLO = 'U', the leading n - by - n upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced.If UPLO = 'L', the leading n - by - n lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.On exit : if UPLO = 'U', the last NB columns have been reduced to tridiagonal form, with the diagonal elements overwriting the diagonal elements of A;
the elements above the diagonal
    with the array TAU,
    represent the unitary matrix Q as a
        product of elementary reflectors;
if UPLO
    = 'L', the first NB columns have been reduced to tridiagonal form, with the diagonal elements overwriting the diagonal elements of A;
the elements below the diagonal
    with the array TAU,
    represent the unitary matrix Q as a
        product of elementary reflectors.See Further Details.
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          If UPLO = 'U', E(n-nb:n-1) contains the superdiagonal
          elements of the last NB columns of the reduced matrix;
          if UPLO = 'L', E(1:nb) contains the subdiagonal elements of
          the first NB columns of the reduced matrix.
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (N-1)
          The scalar factors of the elementary reflectors, stored in
          TAU(n-nb:n-1) if UPLO = 'U', and in TAU(1:nb) if UPLO = 'L'.
          See Further Details.
</pre>
<p> <i>W</i> </p>
<pre>
          W is COMPLEX array, dimension (LDW,NB)
          The n-by-nb matrix W required to update the unreduced part
          of A.
</pre>
<p> <i>LDW</i> </p>
<pre>
          LDW is INTEGER
          The leading dimension of the array W. LDW &gt;= max(1,N).
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
                       Q = H(n) H(n - 1)...H(n - nb + 1).Each H(i)
has the form
    H(i) = I - tau * v * v * *H where tau is a complex scalar,
    and v is a complex vector with
    v(i
      : n) = 0 and v(i - 1) = 1;
v(1
  : i - 1) is stored on exit in A(1
                                  : i - 1, i),
    and tau in TAU(i - 1).If UPLO = 'L', the matrix Q is represented as a product of elementary reflectors Q = H(1) H(2)...H(nb).Each H(i)
has the form
    H(i) = I - tau * v * v * *H where tau is a complex scalar,
    and v is a complex vector with
    v(1
      : i) = 0 and v(i + 1) = 1;
v(i + 1
  : n) is stored on exit in A(i + 1
                              : n, i),
    and tau in TAU(i).The elements of the vectors v together form the n - by - nb matrix V which is needed, with W, to apply the transformation to the unreduced part of the matrix, using a Hermitian rank - 2k update of the form : A : = A - V *W **H - W *V **H.The contents of A on exit are illustrated by the following examples with n = 5 and nb = 2 : if UPLO = 'U' : if UPLO = 'L' : (a a a v4 v5)(d)(a a v4 v5)(1 d)(a 1 v5)(v1 1 a)(d 1)(v1 v2 a a)(d)(v1 v2 a a a)where d denotes a diagonal element of the reduced matrix, a denotes an element of the original matrix that is unchanged, and vi denotes an element of the vector defining H(i).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 200 of file clatrd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
