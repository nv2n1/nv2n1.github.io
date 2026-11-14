---
title: "dsbmv-f(3)"
name: "dsbmv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsbmv-f/"
description: "dsbmv.f –"
---

<p>dsbmv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsbmv</code> (UPLO, N, K, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>DSBMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsbmv (characterUPLO, integerN, integerK, double precisionALPHA, double precision, dimension(lda,*)A, integerLDA, double precision, dimension(*)X, integerINCX, double precisionBETA, double precision, dimension(*)Y, integerINCY)</h3>
<p><code>DSBMV</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSBMV performs the matrix-vector operation
 y := alpha*A*x + beta*y,
 where alpha and beta are scalars, x and y are n element vectors and
 A is an n by n symmetric band matrix, with k super-diagonals.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the band matrix A is being supplied as
 follows:
 UPLO = 'U' or 'u' The upper triangular part of A is
 being supplied.
 UPLO = 'L' or 'l' The lower triangular part of A is
 being supplied.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 On entry, K specifies the number of super-diagonals of the
 matrix A. K must satisfy 0 .le. K.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is DOUBLE PRECISION.
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading ( k + 1 )
 by n part of the array A must contain the upper triangular
 band part of the symmetric matrix, supplied column by
 column, with the leading diagonal of the matrix in row
 ( k + 1 ) of the array, the first super-diagonal starting at
 position 2 in row k, and so on. The top left k by k triangle
 of the array A is not referenced.
 The following program segment will transfer the upper
 triangular part of a symmetric band matrix from conventional
 full matrix storage to band storage:
 DO 20, J = 1, N
 M = K + 1 - J
 DO 10, I = MAX( 1, J - K ), J
 A( M + I, J ) = matrix( I, J )
 10 CONTINUE
 20 CONTINUE
 Before entry with UPLO = 'L' or 'l', the leading ( k + 1 )
 by n part of the array A must contain the lower triangular
 band part of the symmetric matrix, supplied column by
 column, with the leading diagonal of the matrix in row 1 of
 the array, the first sub-diagonal starting at position 1 in
 row 2, and so on. The bottom right k by k triangle of the
 array A is not referenced.
 The following program segment will transfer the lower
 triangular part of a symmetric band matrix from conventional
 full matrix storage to band storage:
 DO 20, J = 1, N
 M = 1 - J
 DO 10, I = J, MIN( N, J + K )
 A( M + I, J ) = matrix( I, J )
 10 CONTINUE
 20 CONTINUE</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 ( k + 1 ).</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array of DIMENSION at least
 ( 1 + ( n - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the
 vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.</pre>
<p><i>BETA</i> </p>
<pre> BETA is DOUBLE PRECISION.
 On entry, BETA specifies the scalar beta.</pre>
<p><i>Y</i> </p>
<pre> Y is DOUBLE PRECISION array of DIMENSION at least
 ( 1 + ( n - 1 )*abs( INCY ) ).
 Before entry, the incremented array Y must contain the
 vector y. On exit, Y is overwritten by the updated vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 On entry, INCY specifies the increment for the elements of
 Y. INCY must not be zero.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> Level 2 Blas routine.
 The vector and matrix arguments are not referenced when N = 0, or M = 0
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 185 of file dsbmv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
