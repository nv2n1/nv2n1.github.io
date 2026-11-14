---
title: "zspmv-f(3)"
name: "zspmv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zspmv-f/"
description: "zspmv.f –"
---

<p>zspmv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zspmv</code> (UPLO, N, ALPHA, AP, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>ZSPMV</code> computes a matrix-vector product for complex vectors using a complex symmetric packed matrix</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zspmv (characterUPLO, integerN, complex*16ALPHA, complex*16, dimension( * )AP, complex*16, dimension( * )X, integerINCX, complex*16BETA, complex*16, dimension( * )Y, integerINCY)</h3>
<p><code>ZSPMV</code> computes a matrix-vector product for complex vectors using a complex symmetric packed matrix </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSPMV performs the matrix-vector operation
 y := alpha*A*x + beta*y,
 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n symmetric matrix, supplied in packed form.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the matrix A is supplied in the packed
 array AP as follows:
 UPLO = 'U' or 'u' The upper triangular part of A is
 supplied in AP.
 UPLO = 'L' or 'l' The lower triangular part of A is
 supplied in AP.
 Unchanged on exit.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.
 Unchanged on exit.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16
 On entry, ALPHA specifies the scalar alpha.
 Unchanged on exit.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension at least
 ( ( N*( N + 1 ) )/2 ).
 Before entry, with UPLO = 'U' or 'u', the array AP must
 contain the upper triangular part of the symmetric matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 )
 and a( 2, 2 ) respectively, and so on.
 Before entry, with UPLO = 'L' or 'l', the array AP must
 contain the lower triangular part of the symmetric matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 )
 and a( 3, 1 ) respectively, and so on.
 Unchanged on exit.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension at least
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
<pre> BETA is COMPLEX*16
 On entry, BETA specifies the scalar beta. When BETA is
 supplied as zero then Y need not be set on input.
 Unchanged on exit.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array, dimension at least
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
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 152 of file zspmv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
