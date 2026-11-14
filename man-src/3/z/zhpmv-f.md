---
title: "zhpmv-f(3)"
name: "zhpmv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhpmv-f/"
description: "zhpmv.f –"
---

<p>zhpmv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhpmv</code> (UPLO, N, ALPHA, AP, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>ZHPMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhpmv (characterUPLO, integerN, complex*16ALPHA, complex*16, dimension(*)AP, complex*16, dimension(*)X, integerINCX, complex*16BETA, complex*16, dimension(*)Y, integerINCY)</h3>
<p><code>ZHPMV</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPMV performs the matrix-vector operation
 y := alpha*A*x + beta*y,
 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n hermitian matrix, supplied in packed form.</pre>
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
 supplied in AP.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array of DIMENSION at least
 ( ( n*( n + 1 ) )/2 ).
 Before entry with UPLO = 'U' or 'u', the array AP must
 contain the upper triangular part of the hermitian matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 )
 and a( 2, 2 ) respectively, and so on.
 Before entry with UPLO = 'L' or 'l', the array AP must
 contain the lower triangular part of the hermitian matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 )
 and a( 3, 1 ) respectively, and so on.
 Note that the imaginary parts of the diagonal elements need
 not be set and are assumed to be zero.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array of dimension at least
 ( 1 + ( n - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the n
 element vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX*16
 On entry, BETA specifies the scalar beta. When BETA is
 supplied as zero then Y need not be set on input.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array of dimension at least
 ( 1 + ( n - 1 )*abs( INCY ) ).
 Before entry, the incremented array Y must contain the n
 element vector y. On exit, Y is overwritten by the updated
 vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 On entry, INCY specifies the increment for the elements of
 Y. INCY must not be zero.</pre>
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
<pre> Level 2 Blas routine.
 The vector and matrix arguments are not referenced when N = 0, or M = 0
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 150 of file zhpmv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
