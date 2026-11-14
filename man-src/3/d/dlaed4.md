---
title: "dlaed4(3)"
name: "dlaed4"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaed4/"
description: "dlaed4.f –"
---

<h2 class="name">NAME</h2>
<p> dlaed4.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaed4</code> (N, I, D, Z, DELTA, RHO, DLAM, INFO)<br />
 <i></i><code>DLAED4</code> used by sstedc. Finds a single root of the secular equation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaed4 (integerN, integerI, double precision, dimension( * )D, double precision, dimension( * )Z, double precision, dimension( * )DELTA, double precisionRHO, double precisionDLAM, integerINFO)</h3>
<p> <code>DLAED4</code> used by sstedc. Finds a single root of the secular equation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This subroutine computes the I-th updated eigenvalue of a symmetric
 rank-one modification to a diagonal matrix whose elements are
 given in the array d, and that
            D(i) &lt; D(j)  for  i &lt; j
 and that RHO &gt; 0.  This is arranged by the calling routine, and is
 no loss in generality.  The rank-one modified system is thus
            diag( D )  +  RHO * Z * Z_transpose.
 where we assume the Euclidean norm of Z is 1.
 The method consists of approximating the rational functions in the
 secular equation by simpler interpolating rational functions.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
         The length of all arrays.
</pre>
<p> <i>I</i> </p>
<pre>
          I is INTEGER
         The index of the eigenvalue to be computed.  1 &lt;= I &lt;= N.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
         The original eigenvalues.  It is assumed that they are in
         order, D(I) &lt; D(J)  for I &lt; J.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (N)
         The components of the updating vector.
</pre>
<p> <i>DELTA</i> </p>
<pre>
          DELTA is DOUBLE PRECISION array, dimension (N)
         If N .GT. 2, DELTA contains (D(j) - lambda_I) in its  j-th
         component.  If N = 1, then <a href="//www.systutorials.com/docs/linux/man/1-DELTA/">DELTA</a>(1) = 1. If N = 2, see DLAED5
         for detail. The vector DELTA contains the information necessary
         to construct the eigenvectors by DLAED3 and DLAED9.
</pre>
<p> <i>RHO</i> </p>
<pre>
          RHO is DOUBLE PRECISION
         The scalar in the symmetric updating formula.
</pre>
<p> <i>DLAM</i> </p>
<pre>
          DLAM is DOUBLE PRECISION
         The computed lambda_I, the I-th updated eigenvalue.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
         = 0:  successful exit
         &gt; 0:  if INFO = 1, the updating process failed.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre><code>
  Logical variable ORGATI (origin-at-i?) is used for distinguishing
  whether D(i) or D(i+1) is treated as the origin.
            ORGATI = .true.    origin at i
            ORGATI = .false.   origin at i+1
   Logical variable SWTCH3 (switch-for-3-poles?) is for noting
   if we are working with THREE poles!
   MAXIT is the maximum number of iterations allowed for each
   eigenvalue.
</code></pre>
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
<p> Definition at line 146 of file dlaed4.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
