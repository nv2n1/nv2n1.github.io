---
title: "dpttrs-f(3)"
name: "dpttrs-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpttrs-f/"
description: "dpttrs.f –"
---

<p>dpttrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dpttrs</code> (N, NRHS, D, E, B, LDB, INFO)<br />
 <i></i><code>DPTTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpttrs (integerN, integerNRHS, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>DPTTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DPTTRS solves a tridiagonal system of the form
 A * X = B
 using the L*D*L**T factorization of A computed by DPTTRF. D is a
 diagonal matrix specified in the vector D, L is a unit bidiagonal
 matrix whose subdiagonal is specified in the vector E, and X and B
 are N by NRHS matrices.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the tridiagonal matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The n diagonal elements of the diagonal matrix D from the
 L*D*L**T factorization of A.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 The (n-1) subdiagonal elements of the unit bidiagonal factor
 L from the L*D*L**T factorization of A. E can also be regarded
 as the superdiagonal of the unit bidiagonal factor U from the
 factorization A = U**T*D*U.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,NRHS)
 On entry, the right hand side vectors B for the system of
 linear equations.
 On exit, the solution vectors, X.</pre>
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
<p> Definition at line 110 of file dpttrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
