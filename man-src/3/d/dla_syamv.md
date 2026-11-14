---
title: "dla_syamv(3)"
name: "dla_syamv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dla_syamv/"
description: "dla_syamv.f –"
---

<h2 class="name">NAME</h2>
<p> dla_syamv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dla_syamv</code> (UPLO, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>DLA_SYAMV</code> computes a matrix-vector product using a symmetric indefinite matrix to calculate error bounds.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dla_syamv (integerUPLO, integerN, double precisionALPHA, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )X, integerINCX, double precisionBETA, double precision, dimension( * )Y, integerINCY)</h3>
<p> <code>DLA_SYAMV</code> computes a matrix-vector product using a symmetric indefinite matrix to calculate error bounds. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLA_SYAMV  performs the matrix-vector operation
         y := alpha*abs(A)*abs(x) + beta*abs(y),
 where alpha and beta are scalars, x and y are vectors and A is an
 n by n symmetric matrix.
 This function is primarily used in calculating error bounds.
 To protect against underflow during evaluation, components in
 the resulting vector are perturbed away from zero by (N+1)
 times the underflow threshold.  To prevent unnecessarily large
 errors for block-structure embedded in general matrices,
 &quot;symbolically&quot; zero components are not perturbed.  A zero
 entry is considered &quot;symbolic&quot; if all multiplications involved
 in computing that entry have at least one zero multiplicand.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is INTEGER
           On entry, UPLO specifies whether the upper or lower
           triangular part of the array A is to be referenced as
           follows:
              UPLO = BLAS_UPPER   Only the upper triangular part of A
                                  is to be referenced.
              UPLO = BLAS_LOWER   Only the lower triangular part of A
                                  is to be referenced.
           Unchanged on exit.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
           On entry, N specifies the number of columns of the matrix A.
           N must be at least zero.
           Unchanged on exit.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION .
           On entry, ALPHA specifies the scalar alpha.
           Unchanged on exit.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array of DIMENSION ( LDA, n ).
           Before entry, the leading m by n part of the array A must
           contain the matrix of coefficients.
           Unchanged on exit.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the calling (sub) program. LDA must be at least
           max( 1, n ).
           Unchanged on exit.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension
           ( 1 + ( n - 1 )*abs( INCX ) )
           Before entry, the incremented array X must contain the
           vector x.
           Unchanged on exit.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
           On entry, INCX specifies the increment for the elements of
           X. INCX must not be zero.
           Unchanged on exit.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION .
           On entry, BETA specifies the scalar beta. When BETA is
           supplied as zero then Y need not be set on input.
           Unchanged on exit.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is DOUBLE PRECISION array, dimension
           ( 1 + ( n - 1 )*abs( INCY ) )
           Before entry with BETA non-zero, the incremented array Y
           must contain the vector y. On exit, Y is overwritten by the
           updated vector y.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
           On entry, INCY specifies the increment for the elements of
           Y. INCY must not be zero.
           Unchanged on exit.
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
<dd> September 2012</dl>
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
  -- Modified for the absolute-value product, April 2006
     Jason Riedy, UC Berkeley
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 177 of file dla_syamv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
