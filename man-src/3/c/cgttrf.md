---
title: "cgttrf(3)"
name: "cgttrf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgttrf/"
description: "cgttrf.f –"
---

<h2 class="name">NAME</h2>
<p> cgttrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgttrf</code> (N, DL, D, DU, DU2, IPIV, INFO)<br />
 <i></i><code>CGTTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgttrf (integerN, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU, complex, dimension( * )DU2, integer, dimension( * )IPIV, integerINFO)</h3>
<p> <code>CGTTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGTTRF computes an LU factorization of a complex tridiagonal matrix A
 using elimination with partial pivoting and row interchanges.
 The factorization has the form
    A = L * U
 where L is a product of permutation and unit lower bidiagonal
 matrices and U is upper triangular with nonzeros in only the main
 diagonal and first two superdiagonals.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.
</pre>
<p> <i>DL</i> </p>
<pre>
          DL is COMPLEX array, dimension (N-1)
          On entry, DL must contain the (n-1) sub-diagonal elements of
          A.
          On exit, DL is overwritten by the (n-1) multipliers that
          define the matrix L from the LU factorization of A.
</pre>
<p> <i>D</i> </p>
<pre>
          D is COMPLEX array, dimension (N)
          On entry, D must contain the diagonal elements of A.
          On exit, D is overwritten by the n diagonal elements of the
          upper triangular matrix U from the LU factorization of A.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is COMPLEX array, dimension (N-1)
          On entry, DU must contain the (n-1) super-diagonal elements
          of A.
          On exit, DU is overwritten by the (n-1) elements of the first
          super-diagonal of U.
</pre>
<p> <i>DU2</i> </p>
<pre>
          DU2 is COMPLEX array, dimension (N-2)
          On exit, DU2 is overwritten by the (n-2) elements of the
          second super-diagonal of U.
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
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -k, the k-th argument had an illegal value
          &gt; 0:  if INFO = k, U(k,k) is exactly zero. The factorization
                has been completed, but the factor U is exactly
                singular, and division by zero will occur if it is used
                to solve a system of equations.
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
<p> Definition at line 125 of file cgttrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
