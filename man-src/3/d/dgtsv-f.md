---
title: "dgtsv-f(3)"
name: "dgtsv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgtsv-f/"
description: "dgtsv.f –"
---

<p>dgtsv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgtsv</code> (N, NRHS, DL, D, DU, B, LDB, INFO)<br />
 <i></i><code> DGTSV computes the solution to system of linear equations A * X = B for GT matrices </code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgtsv (integerN, integerNRHS, double precision, dimension( * )DL, double precision, dimension( * )D, double precision, dimension( * )DU, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code> DGTSV computes the solution to system of linear equations A * X = B for GT matrices </code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 DGTSV  solves the equation
    A*X = B,
 where A is an n by n tridiagonal matrix, by Gaussian elimination with
 partial pivoting.
 Note that the equation  A**T*X = B  may be solved by interchanging the
 order of the arguments DU and DL.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<p> <i>DL</i> </p>
<pre>
          DL is DOUBLE PRECISION array, dimension (N-1)
          On entry, DL must contain the (n-1) sub-diagonal elements of
          A.
          On exit, DL is overwritten by the (n-2) elements of the
          second super-diagonal of the upper triangular matrix U from
          the LU factorization of A, in <a href="//www.systutorials.com/docs/linux/man/1-DL/">DL</a>(1), ..., DL(n-2).
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          On entry, D must contain the diagonal elements of A.
          On exit, D is overwritten by the n diagonal elements of U.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is DOUBLE PRECISION array, dimension (N-1)
          On entry, DU must contain the (n-1) super-diagonal elements
          of A.
          On exit, DU is overwritten by the (n-1) elements of the first
          super-diagonal of U.
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          On entry, the N by NRHS matrix of right hand side matrix B.
          On exit, if INFO = 0, the N by NRHS solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, U(i,i) is exactly zero, and the solution
               has not been computed.  The factorization has not been
               completed unless i = N.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> September 2012</dl>
<p> Definition at line 128 of file dgtsv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
