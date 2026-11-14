---
title: "ssyr2-f(3)"
name: "ssyr2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssyr2-f/"
description: "ssyr2.f –"
---

<p>ssyr2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssyr2</code> (UPLO, N, ALPHA, X, INCX, Y, INCY, A, LDA)<br />
 <i></i><code>SSYR2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssyr2 (characterUPLO, integerN, realALPHA, real, dimension(*)X, integerINCX, real, dimension(*)Y, integerINCY, real, dimension(lda,*)A, integerLDA)</h3>
<p><code>SSYR2</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYR2 performs the symmetric rank 2 operation
 A := alpha*x*y**T + alpha*y*x**T + A,
 where alpha is a scalar, x and y are n element vectors and A is an n
 by n symmetric matrix.</pre>
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
<pre> ALPHA is REAL
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>X</i> </p>
<pre> X is REAL array of dimension at least
 ( 1 + ( n - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the n
 element vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.</pre>
<p><i>Y</i> </p>
<pre> Y is REAL array of dimension at least
 ( 1 + ( n - 1 )*abs( INCY ) ).
 Before entry, the incremented array Y must contain the n
 element vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 On entry, INCY specifies the increment for the elements of
 Y. INCY must not be zero.</pre>
<p><i>A</i> </p>
<pre> A is REAL array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array A must contain the upper
 triangular part of the symmetric matrix and the strictly
 lower triangular part of A is not referenced. On exit, the
 upper triangular part of the array A is overwritten by the
 upper triangular part of the updated matrix.
 Before entry with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array A must contain the lower
 triangular part of the symmetric matrix and the strictly
 upper triangular part of A is not referenced. On exit, the
 lower triangular part of the array A is overwritten by the
 lower triangular part of the updated matrix.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 max( 1, n ).</pre>
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
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 148 of file ssyr2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
