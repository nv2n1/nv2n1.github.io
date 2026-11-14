---
title: "sptts2-f(3)"
name: "sptts2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sptts2-f/"
description: "sptts2.f –"
---

<p>sptts2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sptts2</code> (N, NRHS, D, E, B, LDB)<br />
 <i></i><code>SPTTS2</code> solves a tridiagonal system of the form AX=B using the L D LH factorization computed by spttrf.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sptts2 (integerN, integerNRHS, real, dimension( * )D, real, dimension( * )E, real, dimension( ldb, * )B, integerLDB)</h3>
<p><code>SPTTS2</code> solves a tridiagonal system of the form AX=B using the L D LH factorization computed by spttrf. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPTTS2 solves a tridiagonal system of the form
 A * X = B
 using the L*D*L**T factorization of A computed by SPTTRF. D is a
 diagonal matrix specified in the vector D, L is a unit bidiagonal
 matrix whose subdiagonal is specified in the vector E, and X and B
 are N by NRHS matrices.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the tridiagonal matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 The n diagonal elements of the diagonal matrix D from the
 L*D*L**T factorization of A.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 The (n-1) subdiagonal elements of the unit bidiagonal factor
 L from the L*D*L**T factorization of A. E can also be regarded
 as the superdiagonal of the unit bidiagonal factor U from the
 factorization A = U**T*D*U.</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
 On entry, the right hand side vectors B for the system of
 linear equations.
 On exit, the solution vectors, X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 103 of file sptts2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
