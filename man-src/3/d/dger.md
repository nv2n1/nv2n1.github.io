---
title: "dger(3)"
name: "dger"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dger/"
description: "dger.f –"
---

<h2 class="name">NAME</h2>
<p> dger.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dger</code> (M, N, ALPHA, X, INCX, Y, INCY, A, LDA)<br />
 <i></i><code>DGER</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dger (integerM, integerN, double precisionALPHA, double precision, dimension(*)X, integerINCX, double precision, dimension(*)Y, integerINCY, double precision, dimension(lda,*)A, integerLDA)</h3>
<p> <code>DGER</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGER   performs the rank 1 operation
    A := alpha*x*y**T + A,
 where alpha is a scalar, x is an m element vector, y is an n element
 vector and A is an m by n matrix.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
           On entry, M specifies the number of rows of the matrix A.
           M must be at least zero.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
           On entry, N specifies the number of columns of the matrix A.
           N must be at least zero.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION.
           On entry, ALPHA specifies the scalar alpha.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array of dimension at least
           ( 1 + ( m - 1 )*abs( INCX ) ).
           Before entry, the incremented array X must contain the m
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
          Y is DOUBLE PRECISION array of dimension at least
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
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array of DIMENSION ( LDA, n ).
           Before entry, the leading m by n part of the array A must
           contain the matrix of coefficients. On exit, A is
           overwritten by the updated matrix.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the calling (sub) program. LDA must be at least
           max( 1, m ).
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
<p> Definition at line 131 of file dger.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
