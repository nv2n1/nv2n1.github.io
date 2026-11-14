---
title: "cgttrs-f(3)"
name: "cgttrs-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgttrs-f/"
description: "cgttrs.f –"
---

<p>cgttrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgttrs</code> (TRANS, N, NRHS, DL, D, DU, DU2, IPIV, B, LDB, INFO)<br />
 <i></i><code>CGTTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgttrs (characterTRANS, integerN, integerNRHS, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU, complex, dimension( * )DU2, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>CGTTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGTTRS solves one of the systems of equations
 A * X = B, A**T * X = B, or A**H * X = B,
 with a tridiagonal matrix A using the LU factorization computed
 by CGTTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations.
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose)</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>DL</i> </p>
<pre> DL is COMPLEX array, dimension (N-1)
 The (n-1) multipliers that define the matrix L from the
 LU factorization of A.</pre>
<p><i>D</i> </p>
<pre> D is COMPLEX array, dimension (N)
 The n diagonal elements of the upper triangular matrix U from
 the LU factorization of A.</pre>
<p><i>DU</i> </p>
<pre> DU is COMPLEX array, dimension (N-1)
 The (n-1) elements of the first super-diagonal of U.</pre>
<p><i>DU2</i> </p>
<pre> DU2 is COMPLEX array, dimension (N-2)
 The (n-2) elements of the second super-diagonal of U.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices; for 1 &lt;= i &lt;= n, row i of the matrix was
 interchanged with row IPIV(i). IPIV(i) will always be either
 i or i+1; IPIV(i) = i indicates a row interchange was not
 required.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
 On entry, the matrix of right hand side vectors B.
 On exit, B is overwritten by the solution vectors X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -k, the k-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 138 of file cgttrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
