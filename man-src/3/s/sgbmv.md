---
title: "sgbmv(3)"
name: "sgbmv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbmv/"
---

<h2 class="name">NAME</h2>
 

 sgbmv.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbmv</b> (TRANS, M, N, KL, KU, ALPHA, A, LDA, X, INCX, BETA, Y, INCY) 
 <i></i><b>SGBMV</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbmv (characterTRANS, integerM, integerN, integerKL, integerKU, realALPHA, real, dimension(lda,*)A, integerLDA, real, dimension(*)X, integerINCX, realBETA, real, dimension(*)Y, integerINCY)</h3>

 

 

 <b>SGBMV</b> <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBMV  performs one of the matrix-vector operations
    y := alpha*A*x + beta*y,   or   y := alpha*A**T*x + beta*y,
 where alpha and beta are scalars, x and y are vectors and A is an
 m by n band matrix, with kl sub-diagonals and ku super-diagonals.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>TRANS</i> 

 <pre>
          TRANS is CHARACTER*1
           On entry, TRANS specifies the operation to be performed as
           follows:
              TRANS = 'N' or 'n'   y := alpha*A*x + beta*y.
              TRANS = 'T' or 't'   y := alpha*A**T*x + beta*y.
              TRANS = 'C' or 'c'   y := alpha*A**T*x + beta*y.
</pre> 

 
 <i>M</i> 

 <pre>
          M is INTEGER
           On entry, M specifies the number of rows of the matrix A.
           M must be at least zero.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
           On entry, N specifies the number of columns of the matrix A.
           N must be at least zero.
</pre> 

 
 <i>KL</i> 

 <pre>
          KL is INTEGER
           On entry, KL specifies the number of sub-diagonals of the
           matrix A. KL must satisfy  0 .le. KL.
</pre> 

 
 <i>KU</i> 

 <pre>
          KU is INTEGER
           On entry, KU specifies the number of super-diagonals of the
           matrix A. KU must satisfy  0 .le. KU.
</pre> 

 
 <i>ALPHA</i> 

 <pre>
          ALPHA is REAL
           On entry, ALPHA specifies the scalar alpha.
</pre> 

 
 <i>A</i> 

 <pre>
          A is REAL array of DIMENSION ( LDA, n ).
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

 
 <i>LDA</i> 

 <pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the calling (sub) program. LDA must be at least
           ( kl + ku + 1 ).
</pre> 

 
 <i>X</i> 

 <pre>
          X is REAL array of DIMENSION at least
           ( 1 + ( n - 1 )*abs( INCX ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( m - 1 )*abs( INCX ) ) otherwise.
           Before entry, the incremented array X must contain the
           vector x.
</pre> 

 
 <i>INCX</i> 

 <pre>
          INCX is INTEGER
           On entry, INCX specifies the increment for the elements of
           X. INCX must not be zero.
</pre> 

 
 <i>BETA</i> 

 <pre>
          BETA is REAL
           On entry, BETA specifies the scalar beta. When BETA is
           supplied as zero then Y need not be set on input.
</pre> 

 
 <i>Y</i> 

 <pre>
          Y is REAL array of DIMENSION at least
           ( 1 + ( m - 1 )*abs( INCY ) ) when TRANS = 'N' or 'n'
           and at least
           ( 1 + ( n - 1 )*abs( INCY ) ) otherwise.
           Before entry, the incremented array Y must contain the
           vector y. On exit, Y is overwritten by the updated vector y.
</pre> 

 
 <i>INCY</i> 

 <pre>
          INCY is INTEGER
           On entry, INCY specifies the increment for the elements of
           Y. INCY must not be zero.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl>
<dt>
<dd> Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl>
<dt>
<dd> November 2011</dl>
 

 <b>Further Details: </b>
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

 
&nbsp;<wbr></dl>
 

 

 

 Definition at line 186 of file sgbmv.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


