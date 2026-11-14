---
title: "dla_lin_berr-f(3)"
name: "dla_lin_berr-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dla_lin_berr-f/"
description: "dla_lin_berr.f –"
---

<p>dla_lin_berr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dla_lin_berr</code> (N, NZ, NRHS, RES, AYB, BERR)<br />
 <i></i><code>DLA_LIN_BERR</code> computes a component-wise relative backward error.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dla_lin_berr (integerN, integerNZ, integerNRHS, double precision, dimension( n, nrhs )RES, double precision, dimension( n, nrhs )AYB, double precision, dimension( nrhs )BERR)</h3>
<p><code>DLA_LIN_BERR</code> computes a component-wise relative backward error. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLA_LIN_BERR computes component-wise relative backward error from
 the formula
 max(i) ( abs(R(i)) / ( abs(op(A_s))*abs(Y) + abs(B_s) )(i) )
 where abs(Z) is the component-wise absolute value of the matrix
 or vector Z.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>NZ</i> </p>
<pre> NZ is INTEGER
 We add (NZ+1)*SLAMCH( 'Safe minimum' ) to R(i) in the numerator to
 guard against spuriously zero residuals. Default value is N.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices AYB, RES, and BERR. NRHS &gt;= 0.</pre>
<p><i>RES</i> </p>
<pre> RES is DOUBLE PRECISION array, dimension (N,NRHS)
 The residual matrix, i.e., the matrix R in the relative backward
 error formula above.</pre>
<p><i>AYB</i> </p>
<pre> AYB is DOUBLE PRECISION array, dimension (N, NRHS)
 The denominator in the relative backward error formula above, i.e.,
 the matrix abs(op(A_s))*abs(Y) + abs(B_s). The matrices A, Y, and B
 are from iterative refinement (see dla_gerfsx_extended.f).</pre>
<p><i>BERR</i> </p>
<pre> BERR is DOUBLE PRECISION array, dimension (NRHS)
 The component-wise relative backward error from the formula above.</pre>
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
<p> Definition at line 102 of file dla_lin_berr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
