---
title: "zher(3)"
name: "zher"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zher/"
description: "zher.f –"
---

<p>zher.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zher</code> (UPLO, N, ALPHA, X, INCX, A, LDA)<br />
 <i></i><code>ZHER</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zher (characterUPLO, integerN, double precisionALPHA, complex*16, dimension(*)X, integerINCX, complex*16, dimension(lda,*)A, integerLDA)</h3>
<p><code>ZHER</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHER performs the hermitian rank 1 operation
 A := alpha*x*x**H + A,
 where alpha is a real scalar, x is an n element vector and A is an
 n by n hermitian matrix.</pre>
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
<pre> ALPHA is DOUBLE PRECISION.
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array of dimension at least
 ( 1 + ( n - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the n
 element vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array A must contain the upper
 triangular part of the hermitian matrix and the strictly
 lower triangular part of A is not referenced. On exit, the
 upper triangular part of the array A is overwritten by the
 upper triangular part of the updated matrix.
 Before entry with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array A must contain the lower
 triangular part of the hermitian matrix and the strictly
 upper triangular part of A is not referenced. On exit, the
 lower triangular part of the array A is overwritten by the
 lower triangular part of the updated matrix.
 Note that the imaginary parts of the diagonal elements need
 not be set, they are assumed to be zero, and on exit they
 are set to zero.</pre>
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
<p> Definition at line 136 of file zher.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
