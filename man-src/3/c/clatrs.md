---
title: "clatrs(3)"
name: "clatrs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clatrs/"
description: "clatrs.f –"
---

<h2 class="name">NAME</h2>
<p> clatrs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clatrs</code> (UPLO, TRANS, DIAG, NORMIN, N, A, LDA, X, SCALE, CNORM, INFO)<br />
 <i></i><code>CLATRS</code> solves a triangular system of equations with the scale factor set to prevent overflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clatrs (characterUPLO, characterTRANS, characterDIAG, characterNORMIN, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )X, realSCALE, real, dimension( * )CNORM, integerINFO)</h3>
<p> <code>CLATRS</code> solves a triangular system of equations with the scale factor set to prevent overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLATRS solves one of the triangular systems
    A * x = s*b,  A**T * x = s*b,  or  A**H * x = s*b,
 with scaling to prevent overflow.  Here A is an upper or lower
 triangular matrix, A**T denotes the transpose of A, A**H denotes the
 conjugate transpose of A, x and b are n-element vectors, and s is a
 scaling factor, usually less than or equal to 1, chosen so that the
 components of x will be less than the overflow threshold.  If the
 unscaled problem will not cause overflow, the Level 2 BLAS routine
 CTRSV is called. If the matrix A is singular (A(j,j) = 0 for some j),
 then s is set to 0 and a non-trivial solution to A*x = 0 is returned.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the matrix A is upper or lower triangular.
          = 'U':  Upper triangular
          = 'L':  Lower triangular
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the operation applied to A.
          = 'N':  Solve A * x = s*b     (No transpose)
          = 'T':  Solve A**T * x = s*b  (Transpose)
          = 'C':  Solve A**H * x = s*b  (Conjugate transpose)
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
          Specifies whether or not the matrix A is unit triangular.
          = 'N':  Non-unit triangular
          = 'U':  Unit triangular
</pre>
<p> <i>NORMIN</i> </p>
<pre>
          NORMIN is CHARACTER*1
          Specifies whether CNORM has been set or not.
          = 'Y':  CNORM contains the column norms on entry
          = 'N':  CNORM is not set on entry.  On exit, the norms will
                  be computed and stored in CNORM.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          The triangular matrix A.  If UPLO = 'U', the leading n by n
          upper triangular part of the array A contains the upper
          triangular matrix, and the strictly lower triangular part of
          A is not referenced.  If UPLO = 'L', the leading n by n lower
          triangular part of the array A contains the lower triangular
          matrix, and the strictly upper triangular part of A is not
          referenced.  If DIAG = 'U', the diagonal elements of A are
          also not referenced and are assumed to be 1.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max (1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (N)
          On entry, the right hand side b of the triangular system.
          On exit, X is overwritten by the solution vector x.
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is REAL
          The scaling factor s for the triangular system
             A * x = s*b,  A**T * x = s*b,  or  A**H * x = s*b.
          If SCALE = 0, the matrix A is singular or badly scaled, and
          the vector x is an exact or approximate solution to A*x = 0.
</pre>
<p> <i>CNORM</i> </p>
<pre>
          CNORM is REAL array, dimension (N)
          If NORMIN = 'Y', CNORM is an input argument and CNORM(j)
          contains the norm of the off-diagonal part of the j-th column
          of A.  If TRANS = 'N', CNORM(j) must be greater than or equal
          to the infinity-norm, and if TRANS = 'T' or 'C', CNORM(j)
          must be greater than or equal to the 1-norm.
          If NORMIN = 'N', CNORM is an output argument and CNORM(j)
          returns the 1-norm of the offdiagonal part of the j-th column
          of A.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -k, the k-th argument had an illegal value
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
<pre><code>
A rough bound on x is computed;
if that is less than overflow, CTRSV
  is called, otherwise, specific code is used which checks for possible
  overflow or divide-by-zero at every operation.
  A columnwise scheme is used for solving A*x = b.  The basic algorithm
  if A is lower triangular is
       x[1:n] := b[1:n]
       for j = 1, ..., n
            x(j) := x(j) / A(j,j)
            x[j+1:n] := x[j+1:n] - x(j) * A[j+1:n,j]
       end
  Define bounds on the components of x after j iterations of the loop:
     M(j) = bound on x[1:j]
     G(j) = bound on x[j+1:n]
  Initially, let M(0) = 0 and G(0) = max{x(i), i=1,...,n}.
  Then for iteration j+1 we have
     M(j+1) &lt;= G(j) / | A(j+1,j+1) |
     G(j+1) &lt;= G(j) + M(j+1) * | A[j+2:n,j+1] |
            &lt;= G(j) ( 1 + CNORM(j+1) / | A(j+1,j+1) | )
  where CNORM(j+1) is greater than or equal to the infinity-norm of
  column j+1 of A, not counting the diagonal.  Hence
     G(j) &lt;= G(0) product ( 1 + CNORM(i) / | A(i,i) | )
                  1&lt;=i&lt;=j
  and
     |x(j)| &lt;= ( G(0) / |A(j,j)| ) product ( 1 + CNORM(i) / |A(i,i)| )
                                   1&lt;=i&lt; j
  Since |x(j)| &lt;= M(j), we use the Level 2 BLAS routine CTRSV if the
  reciprocal of the largest M(j), j=1,..,n, is larger than
  max(underflow, 1/overflow).
  The bound on x(j) is also used to determine when a step in the
  columnwise method can be performed without fear of overflow.  If
  the computed bound is greater than a large constant, x is scaled to
  prevent overflow, but if the bound overflows, x is set to 0, x(j) to
  1, and scale to 0, and a non-trivial solution to A*x = 0 is found.
  Similarly, a row-wise scheme is used to solve A**T *x = b  or
  A**H *x = b.  The basic algorithm for A upper triangular is
       for j = 1, ..., n
            x(j) := ( b(j) - A[1:j-1,j]' * x[1:j-1] ) / A(j,j)
       end
  We simultaneously compute two bounds
       G(j) = bound on ( b(i) - A[1:i-1,i]' * x[1:i-1] ), 1&lt;=i&lt;=j
       M(j) = bound on x(i), 1&lt;=i&lt;=j
  The initial values are G(0) = 0, M(0) = max{b(i), i=1,..,n}, and we
  add the constraint G(j) &gt;= G(j-1) and M(j) &gt;= M(j-1) for j &gt;= 1.
  Then the bound on x(j) is
       M(j) &lt;= M(j-1) * ( 1 + CNORM(j) ) / | A(j,j) |
            &lt;= M(0) * product ( ( 1 + CNORM(i) ) / |A(i,i)| )
                      1&lt;=i&lt;=j
  and we can safely call CTRSV if 1/M(n) and 1/G(n) are both greater
  than max(underflow, 1/overflow).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 239 of file clatrs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
