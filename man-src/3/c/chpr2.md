---
title: "chpr2(3)"
name: "chpr2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chpr2/"
description: "chpr2.f –"
---

<h2 class="name">NAME</h2>
<p> chpr2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chpr2</code> (UPLO, N, ALPHA, X, INCX, Y, INCY, AP)<br />
 <i></i><code>CHPR2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chpr2 (characterUPLO, integerN, complexALPHA, complex, dimension(*)X, integerINCX, complex, dimension(*)Y, integerINCY, complex, dimension(*)AP)</h3>
<p> <code>CHPR2</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHPR2  performs the hermitian rank 2 operation
    A := alpha*x*y**H + conjg( alpha )*y*x**H + A,
 where alpha is a scalar, x and y are n element vectors and A is an
 n by n hermitian matrix, supplied in packed form.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
           On entry, UPLO specifies whether the upper or lower
           triangular part of the matrix A is supplied in the packed
           array AP as follows:
              UPLO = 'U' or 'u'   The upper triangular part of A is
                                  supplied in AP.
              UPLO = 'L' or 'l'   The lower triangular part of A is
                                  supplied in AP.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
           On entry, N specifies the order of the matrix A.
           N must be at least zero.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is COMPLEX
           On entry, ALPHA specifies the scalar alpha.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array of dimension at least
           ( 1 + ( n - 1 )*abs( INCX ) ).
           Before entry, the incremented array X must contain the n
           element vector x.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
           On entry, INCX specifies the increment for the elements of
           X. INCX must not be zero.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array of dimension at least
           ( 1 + ( n - 1 )*abs( INCY ) ).
           Before entry, the incremented array Y must contain the n
           element vector y.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
           On entry, INCY specifies the increment for the elements of
           Y. INCY must not be zero.
</pre>
<p> <i>AP</i> </p>
<pre>
          AP is COMPLEX array of DIMENSION at least
           ( ( n*( n + 1 ) )/2 ).
           Before entry with  UPLO = 'U' or 'u', the array AP must
           contain the upper triangular part of the hermitian matrix
           packed sequentially, column by column, so that AP( 1 )
           contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 1, 2 )
           and a( 2, 2 ) respectively, and so on. On exit, the array
           AP is overwritten by the upper triangular part of the
           updated matrix.
           Before entry with UPLO = 'L' or 'l', the array AP must
           contain the lower triangular part of the hermitian matrix
           packed sequentially, column by column, so that AP( 1 )
           contains a( 1, 1 ), AP( 2 ) and AP( 3 ) contain a( 2, 1 )
           and a( 3, 1 ) respectively, and so on. On exit, the array
           AP is overwritten by the lower triangular part of the
           updated matrix.
           Note that the imaginary parts of the diagonal elements need
           not be set, they are assumed to be zero, and on exit they
           are set to zero.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Level 2 Blas routine.
  -- Written on 22-October-1986.
     Jack Dongarra, Argonne National Lab.
     Jeremy Du Croz, Nag Central Office.
     Sven Hammarling, Nag Central Office.
     Richard Hanson, Sandia National Labs.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 146 of file chpr2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
