---
title: "sptsv(3)"
name: "sptsv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sptsv/"
description: "sptsv.f –"
---

<h2 class="name">NAME</h2>
<p> sptsv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sptsv</code> (N, NRHS, D, E, B, LDB, INFO)<br />
 <i></i><code> SPTSV computes the solution to system of linear equations A * X = B for PT matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sptsv (integerN, integerNRHS, real, dimension( * )D, real, dimension( * )E, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code> SPTSV computes the solution to system of linear equations A * X = B for PT matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SPTSV computes the solution to a real system of linear equations
 A*X = B, where A is an N-by-N symmetric positive definite tridiagonal
 matrix, and X and B are N-by-NRHS matrices.
 A is factored as A = L*D*L**T, and the factored form of A is then
 used to solve the system of equations.
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
          On entry, the n diagonal elements of the tridiagonal matrix
          A.  On exit, the n diagonal elements of the diagonal matrix
          D from the factorization A = L*D*L**T.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          On entry, the (n-1) subdiagonal elements of the tridiagonal
          matrix A.  On exit, the (n-1) subdiagonal elements of the
          unit bidiagonal factor L from the L*D*L**T factorization of
          A.  (E can also be regarded as the superdiagonal of the unit
          bidiagonal factor U from the U**T*D*U factorization of A.)
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS right hand side matrix B.
          On exit, if INFO = 0, the N-by-NRHS solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the leading minor of order i is not
                positive definite, and the solution has not been
                computed.  The factorization has not been completed
                unless i = N.
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
<p> Definition at line 115 of file sptsv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
