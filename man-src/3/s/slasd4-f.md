---
title: "slasd4-f(3)"
name: "slasd4-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasd4-f/"
description: "slasd4.f –"
---

<p>slasd4.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasd4</code> (N, I, D, Z, DELTA, RHO, SIGMA, WORK, INFO)<br />
 <i></i><code>SLASD4</code> computes the square root of the i-th updated eigenvalue of a positive symmetric rank-one modification to a positive diagonal matrix. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasd4 (integerN, integerI, real, dimension( * )D, real, dimension( * )Z, real, dimension( * )DELTA, realRHO, realSIGMA, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SLASD4</code> computes the square root of the i-th updated eigenvalue of a positive symmetric rank-one modification to a positive diagonal matrix. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This subroutine computes the square root of the I-th updated
 eigenvalue of a positive symmetric rank-one modification to
 a positive diagonal matrix whose entries are given as the squares
 of the corresponding entries in the array d, and that
 0 &lt;= D(i) &lt; D(j) for i &lt; j
 and that RHO &gt; 0. This is arranged by the calling routine, and is
 no loss in generality. The rank-one modified system is thus
 diag( D ) * diag( D ) + RHO * Z * Z_transpose.
 where we assume the Euclidean norm of Z is 1.
 The method consists of approximating the rational functions in the
 secular equation by simpler interpolating rational functions.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The length of all arrays.</pre>
<p><i>I</i> </p>
<pre> I is INTEGER
 The index of the eigenvalue to be computed. 1 &lt;= I &lt;= N.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension ( N )
 The original eigenvalues. It is assumed that they are in
 order, 0 &lt;= D(I) &lt; D(J) for I &lt; J.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension ( N )
 The components of the updating vector.</pre>
<p><i>DELTA</i> </p>
<pre> DELTA is REAL array, dimension ( N )
 If N .ne. 1, DELTA contains (D(j) - sigma_I) in its j-th
 component. If N = 1, then <a href="//www.systutorials.com/docs/linux/man/1-DELTA/">DELTA</a>(1) = 1. The vector DELTA
 contains the information necessary to construct the
 (singular) eigenvectors.</pre>
<p><i>RHO</i> </p>
<pre> RHO is REAL
 The scalar in the symmetric updating formula.</pre>
<p><i>SIGMA</i> </p>
<pre> SIGMA is REAL
 The computed sigma_I, the I-th updated eigenvalue.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension ( N )
 If N .ne. 1, WORK contains (D(j) + sigma_I) in its j-th
 component. If N = 1, then WORK( 1 ) = 1.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &gt; 0: if INFO = 1, the updating process failed.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dd>
<pre> Logical variable ORGATI (origin-at-i?) is used for distinguishing
 whether D(i) or D(i+1) is treated as the origin.
 ORGATI = .true. origin at i
 ORGATI = .false. origin at i+1
 Logical variable SWTCH3 (switch-for-3-poles?) is for noting
 if we are working with THREE poles!
 MAXIT is the maximum number of iterations allowed for each
 eigenvalue.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 154 of file slasd4.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
