---
title: "cptts2(3)"
name: "cptts2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cptts2/"
description: "cptts2.f –"
---

<h2 class="name">NAME</h2>
<p> cptts2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cptts2</code> (IUPLO, N, NRHS, D, E, B, LDB)<br />
 <i></i><code>CPTTS2</code> solves a tridiagonal system of the form AX=B using the L D LH factorization computed by spttrf.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cptts2 (integerIUPLO, integerN, integerNRHS, real, dimension( * )D, complex, dimension( * )E, complex, dimension( ldb, * )B, integerLDB)</h3>
<p> <code>CPTTS2</code> solves a tridiagonal system of the form AX=B using the L D LH factorization computed by spttrf. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPTTS2 solves a tridiagonal system of the form
    A * X = B
 using the factorization A = U**H*D*U or A = L*D*L**H computed by CPTTRF.
 D is a diagonal matrix specified in the vector D, U (or L) is a unit
 bidiagonal matrix whose superdiagonal (subdiagonal) is specified in
 the vector E, and X and B are N by NRHS matrices.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>IUPLO</i> </p>
<pre>
          IUPLO is INTEGER
          Specifies the form of the factorization and whether the
          vector E is the superdiagonal of the upper bidiagonal factor
          U or the subdiagonal of the lower bidiagonal factor L.
          = 1:  A = U**H *D*U, E is the superdiagonal of U
          = 0:  A = L*D*L**H, E is the subdiagonal of L
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the tridiagonal matrix A.  N &gt;= 0.
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
          The n diagonal elements of the diagonal matrix D from the
          factorization A = U**H *D*U or A = L*D*L**H.
</pre>
<p> <i>E</i> </p>
<pre>
          E is COMPLEX array, dimension (N-1)
          If IUPLO = 1, the (n-1) superdiagonal elements of the unit
          bidiagonal factor U from the factorization A = U**H*D*U.
          If IUPLO = 0, the (n-1) subdiagonal elements of the unit
          bidiagonal factor L from the factorization A = L*D*L**H.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          On entry, the right hand side vectors B for the system of
          linear equations.
          On exit, the solution vectors, X.
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
<p> Definition at line 114 of file cptts2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
