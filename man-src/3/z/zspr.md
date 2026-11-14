---
title: "zspr(3)"
name: "zspr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zspr/"
description: "zspr.f –"
---

<p>zspr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zspr</code> (UPLO, N, ALPHA, X, INCX, AP)<br />
 <i></i><code>ZSPR</code> performs the symmetrical rank-1 update of a complex symmetric packed matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zspr (characterUPLO, integerN, complex*16ALPHA, complex*16, dimension( * )X, integerINCX, complex*16, dimension( * )AP)</h3>
<p><code>ZSPR</code> performs the symmetrical rank-1 update of a complex symmetric packed matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSPR performs the symmetric rank 1 operation
 A := alpha*x*x**H + A,
 where alpha is a complex scalar, x is an n element vector and A is an
 n by n symmetric matrix, supplied in packed form.</pre>
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
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension at least
 ( ( N*( N + 1 ) )/2 ).
 Before entry, with UPLO = 'U' or 'u', the array AP must
 contain the upper triangular part of the symmetric matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 )
 and a( 2, 2 ) respectively, and so on. On exit, the array
 AP is overwritten by the upper triangular part of the
 updated matrix.
 Before entry, with UPLO = 'L' or 'l', the array AP must
 contain the lower triangular part of the symmetric matrix
 packed sequentially, column by column, so that AP( 1 )
 contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 )
 and a( 3, 1 ) respectively, and so on. On exit, the array
 AP is overwritten by the lower triangular part of the
 updated matrix.
 Note that the imaginary parts of the diagonal elements need
 not be set, they are assumed to be zero, and on exit they
 are set to zero.</pre>
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
<p> Definition at line 133 of file zspr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
