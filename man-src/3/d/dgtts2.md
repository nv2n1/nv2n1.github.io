---
title: "dgtts2(3)"
name: "dgtts2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgtts2/"
description: "dgtts2.f –"
---

<h2 class="name">NAME</h2>
<p> dgtts2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgtts2</code> (ITRANS, N, NRHS, DL, D, DU, DU2, IPIV, B, LDB)<br />
 <i></i><code>DGTTS2</code> solves a system of linear equations with a tridiagonal matrix using the LU factorization computed by sgttrf.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgtts2 (integerITRANS, integerN, integerNRHS, double precision, dimension( * )DL, double precision, dimension( * )D, double precision, dimension( * )DU, double precision, dimension( * )DU2, integer, dimension( * )IPIV, double precision, dimension( ldb, * )B, integerLDB)</h3>
<p> <code>DGTTS2</code> solves a system of linear equations with a tridiagonal matrix using the LU factorization computed by sgttrf. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGTTS2 solves one of the systems of equations
    A*X = B  or  A**T*X = B,
 with a tridiagonal matrix A using the LU factorization computed
 by DGTTRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ITRANS</i> </p>
<pre>
          ITRANS is INTEGER
          Specifies the form of the system of equations.
          = 0:  A * X = B  (No transpose)
          = 1:  A**T* X = B  (Transpose)
          = 2:  A**T* X = B  (Conjugate transpose = Transpose)
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.
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
          The (n-1) multipliers that define the matrix L from the
          LU factorization of A.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          The n diagonal elements of the upper triangular matrix U from
          the LU factorization of A.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is DOUBLE PRECISION array, dimension (N-1)
          The (n-1) elements of the first super-diagonal of U.
</pre>
<p> <i>DU2</i> </p>
<pre>
          DU2 is DOUBLE PRECISION array, dimension (N-2)
          The (n-2) elements of the second super-diagonal of U.
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
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          On entry, the matrix of right hand side vectors B.
          On exit, B is overwritten by the solution vectors X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
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
<p> Definition at line 129 of file dgtts2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
