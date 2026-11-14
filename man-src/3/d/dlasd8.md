---
title: "dlasd8(3)"
name: "dlasd8"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasd8/"
description: "dlasd8.f –"
---

<h2 class="name">NAME</h2>
<p> dlasd8.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasd8</code> (ICOMPQ, K, D, Z, VF, VL, DIFL, DIFR, LDDIFR, DSIGMA, WORK, INFO)<br />
 <i></i><code>DLASD8</code> finds the square roots of the roots of the secular equation, and stores, for each element in D, the distance to its two nearest poles. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasd8 (integerICOMPQ, integerK, double precision, dimension( * )D, double precision, dimension( * )Z, double precision, dimension( * )VF, double precision, dimension( * )VL, double precision, dimension( * )DIFL, double precision, dimension( lddifr, * )DIFR, integerLDDIFR, double precision, dimension( * )DSIGMA, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DLASD8</code> finds the square roots of the roots of the secular equation, and stores, for each element in D, the distance to its two nearest poles. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLASD8 finds the square roots of the roots of the secular equation,
 as defined by the values in DSIGMA and Z. It makes the appropriate
 calls to DLASD4, and stores, for each  element in D, the distance
 to its two nearest poles (elements in DSIGMA). It also updates
 the arrays VF and VL, the first and last components of all the
 right singular vectors of the original bidiagonal matrix.
 DLASD8 is called from DLASD6.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
          Specifies whether singular vectors are to be computed in
          factored form in the calling routine:
          = 0: Compute singular values only.
          = 1: Compute singular vectors in factored form as well.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
          The number of terms in the rational function to be solved
          by DLASD4.  K &gt;= 1.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension ( K )
          On output, D contains the updated singular values.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension ( K )
          On entry, the first K elements of this array contain the
          components of the deflation-adjusted updating row vector.
          On exit, Z is updated.
</pre>
<p> <i>VF</i> </p>
<pre>
          VF is DOUBLE PRECISION array, dimension ( K )
          On entry, VF contains  information passed through DBEDE8.
          On exit, VF contains the first K components of the first
          components of all right singular vectors of the bidiagonal
          matrix.
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION array, dimension ( K )
          On entry, VL contains  information passed through DBEDE8.
          On exit, VL contains the first K components of the last
          components of all right singular vectors of the bidiagonal
          matrix.
</pre>
<p> <i>DIFL</i> </p>
<pre>
          DIFL is DOUBLE PRECISION array, dimension ( K )
          On exit, DIFL(I) = D(I) - DSIGMA(I).
</pre>
<p> <i>DIFR</i> </p>
<pre>
          DIFR is DOUBLE PRECISION array,
                   dimension ( LDDIFR, 2 ) if ICOMPQ = 1 and
                   dimension ( K ) if ICOMPQ = 0.
          On exit, DIFR(I,1) = D(I) - DSIGMA(I+1), DIFR(K,1) is not
          defined and will not be referenced.
          If ICOMPQ = 1, DIFR(1:K,2) is an array containing the
          normalizing factors for the right singular vector matrix.
</pre>
<p> <i>LDDIFR</i> </p>
<pre>
          LDDIFR is INTEGER
          The leading dimension of DIFR, must be at least K.
</pre>
<p> <i>DSIGMA</i> </p>
<pre>
          DSIGMA is DOUBLE PRECISION array, dimension ( K )
          On entry, the first K elements of this array contain the old
          roots of the deflated updating problem.  These are the poles
          of the secular equation.
          On exit, the elements of DSIGMA may be very slightly altered
          in value.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension at least 3 * K
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = 1, a singular value did not converge
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
<dd> Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 166 of file dlasd8.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
