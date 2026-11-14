---
title: "clagtm-f(3)"
name: "clagtm-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clagtm-f/"
description: "clagtm.f –"
---

<p>clagtm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clagtm</code> (TRANS, N, NRHS, ALPHA, DL, D, DU, X, LDX, BETA, B, LDB)<br />
 <i></i><code>CLAGTM</code> performs a matrix-matrix product of the form C = αAB+βC, where A is a tridiagonal matrix, B and C are rectangular matrices, and α and β are scalars, which may be 0, 1, or -1.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clagtm (characterTRANS, integerN, integerNRHS, realALPHA, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU, complex, dimension( ldx, * )X, integerLDX, realBETA, complex, dimension( ldb, * )B, integerLDB)</h3>
<p><code>CLAGTM</code> performs a matrix-matrix product of the form C = αAB+βC, where A is a tridiagonal matrix, B and C are rectangular matrices, and α and β are scalars, which may be 0, 1, or -1. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAGTM performs a matrix-vector product of the form
 B := alpha * A * X + beta * B
 where A is a tridiagonal matrix of order N, B and X are N by NRHS
 matrices, and alpha and beta are real scalars, each of which may be
 0., 1., or -1.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the operation applied to A.
 = 'N': No transpose, B := alpha * A * X + beta * B
 = 'T': Transpose, B := alpha * A**T * X + beta * B
 = 'C': Conjugate transpose, B := alpha * A**H * X + beta * B</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices X and B.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is REAL
 The scalar alpha. ALPHA must be 0., 1., or -1.; otherwise,
 it is assumed to be 0.</pre>
<p><i>DL</i> </p>
<pre> DL is COMPLEX array, dimension (N-1)
 The (n-1) sub-diagonal elements of T.</pre>
<p><i>D</i> </p>
<pre> D is COMPLEX array, dimension (N)
 The diagonal elements of T.</pre>
<p><i>DU</i> </p>
<pre> DU is COMPLEX array, dimension (N-1)
 The (n-1) super-diagonal elements of T.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (LDX,NRHS)
 The N by NRHS matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(N,1).</pre>
<p><i>BETA</i> </p>
<pre> BETA is REAL
 The scalar beta. BETA must be 0., 1., or -1.; otherwise,
 it is assumed to be 1.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
 On entry, the N by NRHS matrix B.
 On exit, B is overwritten by the matrix expression
 B := alpha * A * X + beta * B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(N,1).</pre>
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
<p> Definition at line 145 of file clagtm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
