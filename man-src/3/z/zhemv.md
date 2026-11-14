---
title: "zhemv(3)"
name: "zhemv"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhemv/"
description: "zhemv.f –"
---

<p>zhemv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhemv</code> (UPLO, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>ZHEMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhemv (characterUPLO, integerN, complex*16ALPHA, complex*16, dimension(lda,*)A, integerLDA, complex*16, dimension(*)X, integerINCX, complex*16BETA, complex*16, dimension(*)Y, integerINCY)</h3>
<p><code>ZHEMV</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHEMV performs the matrix-vector operation
 y := alpha*A*x + beta*y,
 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n hermitian matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the array A is to be referenced as
 follows:
 UPLO = 'U' or 'u' Only the upper triangular part of A
 is to be referenced.
 UPLO = 'L' or 'l' Only the lower triangular part of A
 is to be referenced.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array A must contain the upper
 triangular part of the hermitian matrix and the strictly
 lower triangular part of A is not referenced.
 Before entry with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array A must contain the lower
 triangular part of the hermitian matrix and the strictly
 upper triangular part of A is not referenced.
 Note that the imaginary parts of the diagonal elements need
 not be set and are assumed to be zero.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 max( 1, n ).</pre>
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
<p> Definition at line 155 of file zhemv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
