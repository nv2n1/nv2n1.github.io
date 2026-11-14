---
title: "csymv-f(3)"
name: "csymv-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csymv-f/"
description: "csymv.f –"
---

<p>csymv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>csymv</code> (UPLO, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>CSYMV</code> computes a matrix-vector product for a complex symmetric matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csymv (characterUPLO, integerN, complexALPHA, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )X, integerINCX, complexBETA, complex, dimension( * )Y, integerINCY)</h3>
<p><code>CSYMV</code> computes a matrix-vector product for a complex symmetric matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSYMV performs the matrix-vector operation
 y := alpha*A*x + beta*y,
 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n symmetric matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the array A is to be referenced as
 follows:
 UPLO = 'U' or 'u' Only the upper triangular part of A
 is to be referenced.
 UPLO = 'L' or 'l' Only the lower triangular part of A
 is to be referenced.
 Unchanged on exit.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.
 Unchanged on exit.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX
 On entry, ALPHA specifies the scalar alpha.
 Unchanged on exit.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension ( LDA, N )
 Before entry, with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array A must contain the upper
 triangular part of the symmetric matrix and the strictly
 lower triangular part of A is not referenced.
 Before entry, with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array A must contain the lower
 triangular part of the symmetric matrix and the strictly
 upper triangular part of A is not referenced.
 Unchanged on exit.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 max( 1, N ).
 Unchanged on exit.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension at least
 ( 1 + ( N - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the N-
 element vector x.
 Unchanged on exit.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.
 Unchanged on exit.</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX
 On entry, BETA specifies the scalar beta. When BETA is
 supplied as zero then Y need not be set on input.
 Unchanged on exit.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX array, dimension at least
 ( 1 + ( N - 1 )*abs( INCY ) ).
 Before entry, the incremented array Y must contain the n
 element vector y. On exit, Y is overwritten by the updated
 vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 On entry, INCY specifies the increment for the elements of
 Y. INCY must not be zero.
 Unchanged on exit.</pre>
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
<p> Definition at line 158 of file csymv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
