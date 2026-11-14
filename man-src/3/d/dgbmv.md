---
title: "dgbmv(3)"
name: "dgbmv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgbmv/"
description: "dgbmv.f –"
---

<h2 class="name">NAME</h2>
<p> dgbmv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgbmv</code> (TRANS, M, N, KL, KU, ALPHA, A, LDA, X, INCX, BETA, Y, INCY)<br />
 <i></i><code>DGBMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgbmv (characterTRANS, integerM, integerN, integerKL, integerKU, double precisionALPHA, double precision, dimension(lda,*)A, integerLDA, double precision, dimension(*)X, integerINCX, double precisionBETA, double precision, dimension(*)Y, integerINCY)</h3>
<p> <code>DGBMV</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGBMV  performs one of the matrix-vector operations
    y := alpha*A*x + beta*y,   or   y := alpha*A**T*x + beta*y,
 where alpha and beta are scalars, x and y are vectors and A is an
 m by n band matrix, with kl sub-diagonals and ku super-diagonals.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
           On entry, TRANS specifies the operation to be performed as
           follows:
              TRANS = 'N' or 'n'   y := alpha*A*x + beta*y.
              TRANS = 'T' or 't'   y := alpha*A**T*x + beta*y.
              TRANS = 'C' or 'c'   y := alpha*A**T*x + beta*y.
</pre>
<p> <i>M</i> </p>
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
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
           On entry, KL specifies the number of sub-diagonals of the
           matrix A. KL must satisfy  0 .le. KL.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
           On entry, KU specifies the number of super-diagonals of the
           matrix A. KU must satisfy  0 .le. KU.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION.
           On entry, ALPHA specifies the scalar alpha.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array of DIMENSION ( LDA, n ).
           Before entry, the leading ( kl + ku + 1 ) by n part of the
           array A must contain the matrix of coefficients, supplied
           column by column, with the leading diagonal of the matrix in
           row ( ku + 1 ) of the array, the first super-diagonal
           starting at position 2 in row ku, the first sub-diagonal
           starting at position 1 in row ( ku + 2 ), and so on.
           Elements in the array A that do not correspond to elements
           in the band matrix (such as the top left ku by ku triangle)
           are not referenced.
           The following program segment will transfer a band matrix
           from conventional full matrix storage to band storage:
                 DO 20, J = 1, N
                    K = KU + 1 - J
                    DO 10, I = MAX( 1, J - KU ), MIN( M, J + KL )
                       A( K + I, J ) = matrix( I, J )
              10    CONTINUE
              20 CONTINUE
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the calling (sub) program. LDA must be at least
           ( kl + ku + 1 ).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array of DIMENSION at least
           ( 1 + ( n - 1 )*abs( INCX ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( m - 1 )*abs( INCX ) ) otherwise.
           Before entry, the incremented array X must contain the
           vector x.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
           On entry, INCX specifies the increment for the elements of
           X. INCX must not be zero.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION.
           On entry, BETA specifies the scalar beta. When BETA is
           supplied as zero then Y need not be set on input.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is DOUBLE PRECISION array of DIMENSION at least
           ( 1 + ( m - 1 )*abs( INCY ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( n - 1 )*abs( INCY ) ) otherwise.
           Before entry, the incremented array Y must contain the
           vector y. On exit, Y is overwritten by the updated vector y.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
           On entry, INCY specifies the increment for the elements of
           Y. INCY must not be zero.
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
  The vector and matrix arguments are not referenced when N = 0, or M = 0
  -- Written on 22-October-1986.
     Jack Dongarra, Argonne National Lab.
     Jeremy Du Croz, Nag Central Office.
     Sven Hammarling, Nag Central Office.
     Richard Hanson, Sandia National Labs.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 186 of file dgbmv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
