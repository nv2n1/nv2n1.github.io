---
title: "slaed5(3)"
name: "slaed5"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed5/"
description: "slaed5.f –"
---

<h2 class="name">NAME</h2>
<p> slaed5.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaed5</code> (I, D, Z, DELTA, RHO, DLAM)<br />
 <i></i><code>SLAED5</code> used by sstedc. Solves the 2-by-2 secular equation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed5 (integerI, real, dimension( 2 )D, real, dimension( 2 )Z, real, dimension( 2 )DELTA, realRHO, realDLAM)</h3>
<p> <code>SLAED5</code> used by sstedc. Solves the 2-by-2 secular equation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This subroutine computes the I-th eigenvalue of a symmetric rank-one
 modification of a 2-by-2 diagonal matrix
            diag( D )  +  RHO * Z * transpose(Z) .
 The diagonal elements in the array D are assumed to satisfy
            D(i) &lt; D(j)  for  i &lt; j .
 We also assume RHO &gt; 0 and that the Euclidean norm of the vector
 Z is one.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>I</i> </p>
<pre>
          I is INTEGER
         The index of the eigenvalue to be computed.  I = 1 or I = 2.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (2)
         The original eigenvalues.  We assume <a href="//www.systutorials.com/docs/linux/man/1-D/">D</a>(1) &lt; <a href="//www.systutorials.com/docs/linux/man/2-D/">D</a>(2).
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (2)
         The components of the updating vector.
</pre>
<p> <i>DELTA</i> </p>
<pre>
          DELTA is REAL array, dimension (2)
         The vector DELTA contains the information necessary
         to construct the eigenvectors.
</pre>
<p> <i>RHO</i> </p>
<pre>
          RHO is REAL
         The scalar in the symmetric updating formula.
</pre>
<p> <i>DLAM</i> </p>
<pre>
          DLAM is REAL
         The computed lambda_I, the I-th updated eigenvalue.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 109 of file slaed5.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
