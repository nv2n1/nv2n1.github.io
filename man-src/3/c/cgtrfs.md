---
title: "cgtrfs(3)"
name: "cgtrfs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgtrfs/"
description: "cgtrfs.f –"
---

<h2 class="name">NAME</h2>
<p> cgtrfs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgtrfs</code> (TRANS, N, NRHS, DL, D, DU, DLF, DF, DUF, DU2, IPIV, B, LDB, X, LDX, FERR, BERR, WORK, RWORK, INFO)<br />
 <i></i><code>CGTRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgtrfs (characterTRANS, integerN, integerNRHS, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU, complex, dimension( * )DLF, complex, dimension( * )DF, complex, dimension( * )DUF, complex, dimension( * )DU2, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CGTRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGTRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is tridiagonal, and provides
 error bounds and backward error estimates for the solution.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations:
          = 'N':  A * X = B     (No transpose)
          = 'T':  A**T * X = B  (Transpose)
          = 'C':  A**H * X = B  (Conjugate transpose)
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
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>DL</i> </p>
<pre>
          DL is COMPLEX array, dimension (N-1)
          The (n-1) subdiagonal elements of A.
</pre>
<p> <i>D</i> </p>
<pre>
          D is COMPLEX array, dimension (N)
          The diagonal elements of A.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is COMPLEX array, dimension (N-1)
          The (n-1) superdiagonal elements of A.
</pre>
<p> <i>DLF</i> </p>
<pre>
          DLF is COMPLEX array, dimension (N-1)
          The (n-1) multipliers that define the matrix L from the
          LU factorization of A as computed by CGTTRF.
</pre>
<p> <i>DF</i> </p>
<pre>
          DF is COMPLEX array, dimension (N)
          The n diagonal elements of the upper triangular matrix U from
          the LU factorization of A.
</pre>
<p> <i>DUF</i> </p>
<pre>
          DUF is COMPLEX array, dimension (N-1)
          The (n-1) elements of the first superdiagonal of U.
</pre>
<p> <i>DU2</i> </p>
<pre>
          DU2 is COMPLEX array, dimension (N-2)
          The (n-2) elements of the second superdiagonal of U.
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices; for
    1 &lt;= i &lt;= n, row i of the matrix was
                         interchanged with row IPIV(i)
                             .IPIV(i) will always be either
                     i
                     or i + 1;
IPIV(i) = i indicates a row interchange was not required.
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (LDX,NRHS)
          On entry, the solution matrix X, as computed by CGTTRS.
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
          BERR is REAL array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
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
<p> Definition at line 209 of file cgtrfs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
