---
title: "dsposv(3)"
name: "dsposv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsposv/"
description: "dsposv.f –"
---

<h2 class="name">NAME</h2>
<p> dsposv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dsposv</code> (UPLO, N, NRHS, A, LDA, B, LDB, X, LDX, WORK, SWORK, ITER, INFO)<br />
 <i></i><code> DSPOSV computes the solution to system of linear equations A * X = B for PO matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsposv (characterUPLO, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx, * )X, integerLDX, double precision, dimension( n, * )WORK, real, dimension( * )SWORK, integerITER, integerINFO)</h3>
<p> <code> DSPOSV computes the solution to system of linear equations A * X = B for PO matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSPOSV computes the solution to a real system of linear equations
    A * X = B,
 where A is an N-by-N symmetric positive definite matrix and X and B
 are N-by-NRHS matrices.
 DSPOSV first attempts to factorize the matrix in SINGLE PRECISION
 and use this factorization within an iterative refinement procedure
 to produce a solution with DOUBLE PRECISION normwise backward error
 quality (see below). If the approach fails the method switches to a
 DOUBLE PRECISION factorization and solve.
 The iterative refinement is not going to be a winning strategy if
 the ratio SINGLE PRECISION performance over DOUBLE PRECISION
 performance is too small. A reasonable strategy should take the
 number of right-hand sides and the size of the matrix into account.
 This might be done with a call to ILAENV in the future. Up to now, we
 always try iterative refinement.
 The iterative refinement process is stopped if
     ITER &gt; ITERMAX
 or for all the RHS we have:
     RNRM &lt; SQRT(N)*XNRM*ANRM*EPS*BWDMAX
 where
     o ITER is the number of the current iteration in the iterative
       refinement process
     o RNRM is the infinity-norm of the residual
     o XNRM is the infinity-norm of the solution
     o ANRM is the infinity-operator-norm of the matrix A
     o EPS is the machine epsilon returned by DLAMCH('Epsilon')
 The value ITERMAX and BWDMAX are fixed to 30 and 1.0D+00
 respectively.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of linear equations, i.e., the order of the
          matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array,
          dimension (LDA,N)
          On entry, the symmetric matrix A.  If UPLO = 'U', the leading
          N-by-N upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if iterative refinement has been successfully used
          (INFO.EQ.0 and ITER.GE.0, see description below), then A is
          unchanged, if double precision factorization has been used
          (INFO.EQ.0 and ITER.LT.0, see description below), then the
          array A contains the factor U or L from the Cholesky
          factorization A = U**T*U or A = L*L**T.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          The N-by-NRHS right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
          If INFO = 0, the N-by-NRHS solution matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N,NRHS)
          This array is used to hold the residual vectors.
</pre>
<p> <i>SWORK</i> </p>
<pre>
          SWORK is REAL array, dimension (N*(N+NRHS))
          This array is used to use the single precision matrix and the
          right-hand sides or solutions in single precision.
</pre>
<p> <i>ITER</i> </p>
<pre>
          ITER is INTEGER
          &lt; 0: iterative refinement has failed, double precision
               factorization has been performed
               -1 : the routine fell back to full precision for
                    implementation- or machine-specific reasons
               -2 : narrowing the precision induced an overflow,
                    the routine fell back to full precision
               -3 : failure of SPOTRF
               -31: stop the iterative refinement after the 30th
                    iterations
          &gt; 0: iterative refinement has been sucessfully used.
               Returns the number of iterations
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the leading minor of order i of (DOUBLE
                PRECISION) A is not positive definite, so the
                factorization could not be completed, and the solution
                has not been computed.
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
<p> Definition at line 199 of file dsposv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
