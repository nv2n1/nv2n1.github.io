---
title: "dlaic1(3)"
name: "dlaic1"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaic1/"
description: "dlaic1.f –"
---

<h2 class="name">NAME</h2>
<p> dlaic1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaic1</code> (JOB, J, X, SEST, W, GAMMA, SESTPR, S, C)<br />
 <i></i><code>DLAIC1</code> applies one step of incremental condition estimation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaic1 (integerJOB, integerJ, double precision, dimension( j )X, double precisionSEST, double precision, dimension( j )W, double precisionGAMMA, double precisionSESTPR, double precisionS, double precisionC)</h3>
<p> <code>DLAIC1</code> applies one step of incremental condition estimation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DLAIC1 applies one step of incremental condition estimation in
 its simplest version:
 Let x, twonorm(x) = 1, be an approximate singular vector of an j-by-j
 lower triangular matrix L, such that
          twonorm(L*x) = sest
 Then DLAIC1 computes sestpr, s, c such that
 the vector
                 [ s*x ]
          xhat = [  c  ]
 is an approximate singular vector of
                 [ L       0  ]
          Lhat = [ w**T gamma ]
 in the sense that
          twonorm(Lhat*xhat) = sestpr.
 Depending on JOB, an estimate for the largest or smallest singular
 value is computed.
 Note that [s c]**T and sestpr**2 is an eigenpair of the system
     diag(sest*sest, 0) + [alpha  gamma] * [ alpha ]
                                           [ gamma ]
 where  alpha =  x**T*w.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOB</i> </p>
<pre>
          JOB is INTEGER
          = 1: an estimate for the largest singular value is computed.
          = 2: an estimate for the smallest singular value is computed.
</pre>
<p> <i>J</i> </p>
<pre>
          J is INTEGER
          Length of X and W
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (J)
          The j-vector x.
</pre>
<p> <i>SEST</i> </p>
<pre>
          SEST is DOUBLE PRECISION
          Estimated singular value of j by j matrix L
</pre>
<p> <i>W</i> </p>
<pre>
          W is DOUBLE PRECISION array, dimension (J)
          The j-vector w.
</pre>
<p> <i>GAMMA</i> </p>
<pre>
          GAMMA is DOUBLE PRECISION
          The diagonal element gamma.
</pre>
<p> <i>SESTPR</i> </p>
<pre>
          SESTPR is DOUBLE PRECISION
          Estimated singular value of (j+1) by (j+1) matrix Lhat.
</pre>
<p> <i>S</i> </p>
<pre>
          S is DOUBLE PRECISION
          Sine needed in forming xhat.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION
          Cosine needed in forming xhat.
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
<p> Definition at line 135 of file dlaic1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
