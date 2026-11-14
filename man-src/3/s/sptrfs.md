---
title: "sptrfs(3)"
name: "sptrfs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sptrfs/"
description: "sptrfs.f –"
---

<h2 class="name">NAME</h2>
<p> sptrfs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sptrfs</code> (N, NRHS, D, E, DF, EF, B, LDB, X, LDX, FERR, BERR, WORK, INFO)<br />
 <i></i><code>SPTRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sptrfs (integerN, integerNRHS, real, dimension( * )D, real, dimension( * )E, real, dimension( * )DF, real, dimension( * )EF, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SPTRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SPTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is symmetric positive definite
 and tridiagonal, and provides error bounds and backward error
 estimates for the solution.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The n diagonal elements of the tridiagonal matrix A.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          The (n-1) subdiagonal elements of the tridiagonal matrix A.
</pre>
<p> <i>DF</i> </p>
<pre>
          DF is REAL array, dimension (N)
          The n diagonal elements of the diagonal matrix D from the
          factorization computed by SPTTRF.
</pre>
<p> <i>EF</i> </p>
<pre>
          EF is REAL array, dimension (N-1)
          The (n-1) subdiagonal elements of the unit bidiagonal factor
          L from the factorization computed by SPTTRF.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (LDX,NRHS)
          On entry, the solution matrix X, as computed by SPTTRS.
          On exit, the improved solution matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is REAL array, dimension (NRHS)
          The forward error bound for each solution vector
          X(j) (the j-th column of the solution matrix X).
          If XTRUE is the true solution corresponding to X(j), FERR(j)
          is an estimated upper bound for the magnitude of the largest
          element in (X(j) - XTRUE) divided by the magnitude of the
          largest element in X(j).
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is REAL array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (2*N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  ITMAX is the maximum number of steps of iterative refinement.
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
<p> Definition at line 163 of file sptrfs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
