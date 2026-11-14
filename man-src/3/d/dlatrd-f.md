---
title: "dlatrd-f(3)"
name: "dlatrd-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlatrd-f/"
description: "dlatrd.f –"
---

<p>dlatrd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlatrd</code> (UPLO, N, NB, A, LDA, E, TAU, W, LDW)<br />
 <i></i><code>DLATRD</code> reduces the first nb rows and columns of a symmetric/Hermitian matrix A to real tridiagonal form by an orthogonal similarity transformation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlatrd (characterUPLO, integerN, integerNB, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )E, double precision, dimension( * )TAU, double precision, dimension( ldw, * )W, integerLDW)</h3>
<p><code>DLATRD</code> reduces the first nb rows and columns of a symmetric/Hermitian matrix A to real tridiagonal form by an orthogonal similarity transformation. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLATRD reduces NB rows and columns of a real symmetric matrix A to
 symmetric tridiagonal form by an orthogonal similarity
 transformation Q**T * A * Q, and returns the matrices V and W which are
 needed to apply the transformation to the unreduced part of A.
 If UPLO = 'U', DLATRD reduces the last NB rows and columns of a
 matrix, of which the upper triangle is supplied;
 if UPLO = 'L', DLATRD reduces the first NB rows and columns of a
 matrix, of which the lower triangle is supplied.
 This is an auxiliary routine called by DSYTRD.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is stored:
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The number of rows and columns to be reduced.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the symmetric matrix A. If UPLO = 'U', the leading
 n-by-n upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading n-by-n lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit:
 if UPLO = 'U', the last NB columns have been reduced to
 tridiagonal form, with the diagonal elements overwriting
 the diagonal elements of A; the elements above the diagonal
 with the array TAU, represent the orthogonal matrix Q as a
 product of elementary reflectors;
 if UPLO = 'L', the first NB columns have been reduced to
 tridiagonal form, with the diagonal elements overwriting
 the diagonal elements of A; the elements below the diagonal
 with the array TAU, represent the orthogonal matrix Q as a
 product of elementary reflectors.
 See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= (1,N).</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 If UPLO = 'U', E(n-nb:n-1) contains the superdiagonal
 elements of the last NB columns of the reduced matrix;
 if UPLO = 'L', E(1:nb) contains the subdiagonal elements of
 the first NB columns of the reduced matrix.</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (N-1)
 The scalar factors of the elementary reflectors, stored in
 TAU(n-nb:n-1) if UPLO = 'U', and in TAU(1:nb) if UPLO = 'L'.
 See Further Details.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (LDW,NB)
 The n-by-nb matrix W required to update the unreduced part
 of A.</pre>
<p><i>LDW</i> </p>
<pre> LDW is INTEGER
 The leading dimension of the array W. LDW &gt;= max(1,N).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> If UPLO = 'U', the matrix Q is represented as a product of elementary
 reflectors
 Q = <a href="//www.systutorials.com/docs/linux/man/n-H/">H</a>(n) H(n-1) . . . H(n-nb+1).
 Each H(i) has the form
 H(i) = I - tau * v * v**T
 where tau is a real scalar, and v is a real vector with
 v(i:n) = 0 and v(i-1) = 1; v(1:i-1) is stored on exit in A(1:i-1,i),
 and tau in TAU(i-1).
 If UPLO = 'L', the matrix Q is represented as a product of elementary
 reflectors
 Q = H(1) H(2) . . . H(nb).
 Each H(i) has the form
 H(i) = I - tau * v * v**T
 where tau is a real scalar, and v is a real vector with
 v(1:i) = 0 and v(i+1) = 1; v(i+1:n) is stored on exit in A(i+1:n,i),
 and tau in TAU(i).
 The elements of the vectors v together form the n-by-nb matrix V
 which is needed, with W, to apply the transformation to the unreduced
 part of the matrix, using a symmetric rank-2k update of the form:
 A := A - V*W**T - W*V**T.
 The contents of A on exit are illustrated by the following examples
 with n = 5 and nb = 2:
 if UPLO = 'U': if UPLO = 'L':
 ( a a a v4 v5 ) ( d )
 ( a a v4 v5 ) ( 1 d )
 ( a 1 v5 ) ( v1 1 a )
 ( d 1 ) ( v1 v2 a a )
 ( d ) ( v1 v2 a a a )
 where d denotes a diagonal element of the reduced matrix, a denotes
 an element of the original matrix that is unchanged, and vi denotes
 an element of the vector defining H(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 199 of file dlatrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
