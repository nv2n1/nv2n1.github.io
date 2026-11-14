---
title: "zhetrd-f(3)"
name: "zhetrd-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhetrd-f/"
description: "zhetrd.f –"
---

<p>zhetrd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhetrd</code> (UPLO, N, A, LDA, D, E, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>ZHETRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhetrd (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, double precision, dimension( * )D, double precision, dimension( * )E, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>ZHETRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHETRD reduces a complex Hermitian matrix A to real symmetric
 tridiagonal form T by a unitary similarity transformation:
 Q**H * A * Q = T.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the leading
 N-by-N upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading N-by-N lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, if UPLO = 'U', the diagonal and first superdiagonal
 of A are overwritten by the corresponding elements of the
 tridiagonal matrix T, and the elements above the first
 superdiagonal, with the array TAU, represent the unitary
 matrix Q as a product of elementary reflectors; if UPLO
 = 'L', the diagonal and first subdiagonal of A are over-
 written by the corresponding elements of the tridiagonal
 matrix T, and the elements below the first subdiagonal, with
 the array TAU, represent the unitary matrix Q as a product
 of elementary reflectors. See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The diagonal elements of the tridiagonal matrix T:
 D(i) = A(i,i).</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 The off-diagonal elements of the tridiagonal matrix T:
 E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (N-1)
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= 1.
 For optimum performance LWORK &gt;= N*NB, where NB is the
 optimal blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> If UPLO = 'U', the matrix Q is represented as a product of elementary
 reflectors
 Q = H(n-1) . . . H(2) H(1).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(i+1:n) = 0 and v(i) = 1; v(1:i-1) is stored on exit in
 A(1:i-1,i+1), and tau in TAU(i).
 If UPLO = 'L', the matrix Q is represented as a product of elementary
 reflectors
 Q = H(1) H(2) . . . H(n-1).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(1:i) = 0 and v(i+1) = 1; v(i+2:n) is stored on exit in A(i+2:n,i),
 and tau in TAU(i).
 The contents of A on exit are illustrated by the following examples
 with n = 5:
 if UPLO = 'U': if UPLO = 'L':
 ( d e v2 v3 v4 ) ( d )
 ( d e v3 v4 ) ( e d )
 ( d e v4 ) ( v1 e d )
 ( d e ) ( v1 v2 e d )
 ( d ) ( v1 v2 v3 e d )
 where d and e denote diagonal and off-diagonal elements of T, and vi
 denotes an element of the vector defining H(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 193 of file zhetrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
