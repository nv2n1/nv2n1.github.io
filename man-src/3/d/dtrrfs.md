---
title: "dtrrfs(3)"
name: "dtrrfs"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtrrfs/"
description: "dtrrfs.f –"
---

<h2 class="name">NAME</h2>
<p> dtrrfs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtrrfs</code> (UPLO, TRANS, DIAG, N, NRHS, A, LDA, B, LDB, X, LDX, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code>DTRRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtrrfs (characterUPLO, characterTRANS, characterDIAG, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx, * )X, integerLDX, double precision, dimension( * )FERR, double precision, dimension( * )BERR, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DTRRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTRRFS provides error bounds and backward error estimates for the
 solution to a system of linear equations with a triangular
 coefficient matrix.
 The solution matrix X must be computed by DTRTRS or some other
 means before entering this routine.  DTRRFS does not do iterative
 refinement because doing so cannot improve the backward error.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  A is upper triangular;
          = 'L':  A is lower triangular.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations:
          = 'N':  A * X = B  (No transpose)
          = 'T':  A**T * X = B  (Transpose)
          = 'C':  A**H * X = B  (Conjugate transpose = Transpose)
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
          = 'N':  A is non-unit triangular;
          = 'U':  A is unit triangular.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          The triangular matrix A.  If UPLO = 'U', the leading N-by-N
          upper triangular part of the array A contains the upper
          triangular matrix, and the strictly lower triangular part of
          A is not referenced.  If UPLO = 'L', the leading N-by-N lower
          triangular part of the array A contains the lower triangular
          matrix, and the strictly upper triangular part of A is not
          referenced.  If DIAG = 'U', the diagonal elements of A are
          also not referenced and are assumed to be 1.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
          The solution matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is DOUBLE PRECISION array, dimension (NRHS)
          The estimated forward error bound for each solution vector
          X(j) (the j-th column of the solution matrix X).
          If XTRUE is the true solution corresponding to X(j), FERR(j)
          is an estimated upper bound for the magnitude of the largest
          element in (X(j) - XTRUE) divided by the magnitude of the
          largest element in X(j).  The estimate is as reliable as
          the estimate for RCOND, and is almost always a slight
          overestimate of the true error.
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is DOUBLE PRECISION array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (3*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<p> Definition at line 182 of file dtrrfs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
