---
title: "slaic1-f(3)"
name: "slaic1-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaic1-f/"
description: "slaic1.f –"
---

<p>slaic1.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaic1</code> (JOB, J, X, SEST, W, GAMMA, SESTPR, S, C)<br />
 <i></i><code>SLAIC1</code> applies one step of incremental condition estimation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaic1 (integerJOB, integerJ, real, dimension( j )X, realSEST, real, dimension( j )W, realGAMMA, realSESTPR, realS, realC)</h3>
<p><code>SLAIC1</code> applies one step of incremental condition estimation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAIC1 applies one step of incremental condition estimation in
 its simplest version:
 Let x, twonorm(x) = 1, be an approximate singular vector of an j-by-j
 lower triangular matrix L, such that
 twonorm(L*x) = sest
 Then SLAIC1 computes sestpr, s, c such that
 the vector
 [ s*x ]
 xhat = [ c ]
 is an approximate singular vector of
 [ L 0 ]
 Lhat = [ w**T gamma ]
 in the sense that
 twonorm(Lhat*xhat) = sestpr.
 Depending on JOB, an estimate for the largest or smallest singular
 value is computed.
 Note that [s c]**T and sestpr**2 is an eigenpair of the system
 diag(sest*sest, 0) + [alpha gamma] * [ alpha ]
 [ gamma ]
 where alpha = x**T*w.</pre>
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
<pre> X is REAL array, dimension (J)
 The j-vector x.</pre>
<p><i>SEST</i> </p>
<pre> SEST is REAL
 Estimated singular value of j by j matrix L</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (J)
 The j-vector w.</pre>
<p><i>GAMMA</i> </p>
<pre> GAMMA is REAL
 The diagonal element gamma.</pre>
<p><i>SESTPR</i> </p>
<pre> SESTPR is REAL
 Estimated singular value of (j+1) by (j+1) matrix Lhat.</pre>
<p><i>S</i> </p>
<pre> S is REAL
 Sine needed in forming xhat.</pre>
<p><i>C</i> </p>
<pre> C is REAL
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
<p> Definition at line 135 of file slaic1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
