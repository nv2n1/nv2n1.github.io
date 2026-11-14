---
title: "dlagtm(3)"
name: "dlagtm"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlagtm/"
description: "dlagtm.f –"
---

<h2 class="name">NAME</h2>
<p> dlagtm.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlagtm</code> (TRANS, N, NRHS, ALPHA, DL, D, DU, X, LDX, BETA, B, LDB)<br />
 <i></i><code>DLAGTM</code> performs a matrix-matrix product of the form C = αAB+βC, where A is a tridiagonal matrix, B and C are rectangular matrices, and α and β are scalars, which may be 0, 1, or -1.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlagtm (characterTRANS, integerN, integerNRHS, double precisionALPHA, double precision, dimension( * )DL, double precision, dimension( * )D, double precision, dimension( * )DU, double precision, dimension( ldx, * )X, integerLDX, double precisionBETA, double precision, dimension( ldb, * )B, integerLDB)</h3>
<p> <code>DLAGTM</code> performs a matrix-matrix product of the form C = αAB+βC, where A is a tridiagonal matrix, B and C are rectangular matrices, and α and β are scalars, which may be 0, 1, or -1. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAGTM performs a matrix-vector product of the form
    B := alpha * A * X + beta * B
 where A is a tridiagonal matrix of order N, B and X are N by NRHS
 matrices, and alpha and beta are real scalars, each of which may be
 0., 1., or -1.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the operation applied to A.
          = 'N':  No transpose, B := alpha * A * X + beta * B
          = 'T':  Transpose,    B := alpha * A'* X + beta * B
          = 'C':  Conjugate transpose = Transpose
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
          of the matrices X and B.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION
          The scalar alpha.  ALPHA must be 0., 1., or -1.; otherwise,
          it is assumed to be 0.
</pre>
<p> <i>DL</i> </p>
<pre>
          DL is DOUBLE PRECISION array, dimension (N-1)
          The (n-1) sub-diagonal elements of T.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          The diagonal elements of T.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is DOUBLE PRECISION array, dimension (N-1)
          The (n-1) super-diagonal elements of T.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
          The N by NRHS matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(N,1).
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION
          The scalar beta.  BETA must be 0., 1., or -1.; otherwise,
          it is assumed to be 1.
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          On entry, the N by NRHS matrix B.
          On exit, B is overwritten by the matrix expression
          B := alpha * A * X + beta * B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(N,1).
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
<p> Definition at line 145 of file dlagtm.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
