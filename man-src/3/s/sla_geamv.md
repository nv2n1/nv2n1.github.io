---
title: "sla_geamv(3)"
name: "sla_geamv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sla_geamv/"
description: "sla_geamv.f –"
---

<h2 class="name">NAME</h2>
<p> sla_geamv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sla_geamv</code> (TRANS, M, N, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>SLA_GEAMV</code> computes a matrix-vector product using a general matrix to calculate error bounds.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sla_geamv (integerTRANS, integerM, integerN, realALPHA, real, dimension( lda, * )A, integerLDA, real, dimension( * )X, integerINCX, realBETA, real, dimension( * )Y, integerINCY)</h3>
<p> <code>SLA_GEAMV</code> computes a matrix-vector product using a general matrix to calculate error bounds. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLA_GEAMV  performs one of the matrix-vector operations
         y := alpha*abs(A)*abs(x) + beta*abs(y),
    or   y := alpha*abs(A)**T*abs(x) + beta*abs(y),
 where alpha and beta are scalars, x and y are vectors and A is an
 m by n matrix.
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
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is INTEGER
           On entry, TRANS specifies the operation to be performed as
           follows:
             BLAS_NO_TRANS      y := alpha*abs(A)*abs(x) + beta*abs(y)
             BLAS_TRANS         y := alpha*abs(A**T)*abs(x) + beta*abs(y)
             BLAS_CONJ_TRANS    y := alpha*abs(A**T)*abs(x) + beta*abs(y)
           Unchanged on exit.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
           On entry, M specifies the number of rows of the matrix A.
           M must be at least zero.
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
          ALPHA is REAL
           On entry, ALPHA specifies the scalar alpha.
           Unchanged on exit.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array of DIMENSION ( LDA, n )
           Before entry, the leading m by n part of the array A must
           contain the matrix of coefficients.
           Unchanged on exit.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the calling (sub) program. LDA must be at least
           max( 1, m ).
           Unchanged on exit.
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension
           ( 1 + ( n - 1 )*abs( INCX ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( m - 1 )*abs( INCX ) ) otherwise.
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
          BETA is REAL
           On entry, BETA specifies the scalar beta. When BETA is
           supplied as zero then Y need not be set on input.
           Unchanged on exit.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is REAL
           Array of DIMENSION at least
           ( 1 + ( m - 1 )*abs( INCY ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( n - 1 )*abs( INCY ) ) otherwise.
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
  Level 2 Blas routine.
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
<p> Definition at line 174 of file sla_geamv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
