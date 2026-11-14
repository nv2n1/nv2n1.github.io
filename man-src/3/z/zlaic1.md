---
title: "zlaic1(3)"
name: "zlaic1"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaic1/"
description: "zlaic1.f –"
---

<p>zlaic1.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaic1</code> (JOB, J, X, SEST, W, GAMMA, SESTPR, S, C)<br />
 <i></i><code>ZLAIC1</code> applies one step of incremental condition estimation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaic1 (integerJOB, integerJ, complex*16, dimension( j )X, double precisionSEST, complex*16, dimension( j )W, complex*16GAMMA, double precisionSESTPR, complex*16S, complex*16C)</h3>
<p><code>ZLAIC1</code> applies one step of incremental condition estimation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAIC1 applies one step of incremental condition estimation in
 its simplest version:
 Let x, twonorm(x) = 1, be an approximate singular vector of an j-by-j
 lower triangular matrix L, such that
 twonorm(L*x) = sest
 Then ZLAIC1 computes sestpr, s, c such that
 the vector
 [ s*x ]
 xhat = [ c ]
 is an approximate singular vector of
 [ L 0 ]
 Lhat = [ w**H gamma ]
 in the sense that
 twonorm(Lhat*xhat) = sestpr.
 Depending on JOB, an estimate for the largest or smallest singular
 value is computed.
 Note that [s c]**H and sestpr**2 is an eigenpair of the system
 diag(sest*sest, 0) + [alpha gamma] * [ conjg(alpha) ]
 [ conjg(gamma) ]
 where alpha = x**H * w.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is INTEGER
 = 1: an estimate for the largest singular value is computed.
 = 2: an estimate for the smallest singular value is computed.</pre>
<p><i>J</i> </p>
<pre> J is INTEGER
 Length of X and W</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (J)
 The j-vector x.</pre>
<p><i>SEST</i> </p>
<pre> SEST is DOUBLE PRECISION
 Estimated singular value of j by j matrix L</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX*16 array, dimension (J)
 The j-vector w.</pre>
<p><i>GAMMA</i> </p>
<pre> GAMMA is COMPLEX*16
 The diagonal element gamma.</pre>
<p><i>SESTPR</i> </p>
<pre> SESTPR is DOUBLE PRECISION
 Estimated singular value of (j+1) by (j+1) matrix Lhat.</pre>
<p><i>S</i> </p>
<pre> S is COMPLEX*16
 Sine needed in forming xhat.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16
 Cosine needed in forming xhat.</pre>
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
<p> Definition at line 136 of file zlaic1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
