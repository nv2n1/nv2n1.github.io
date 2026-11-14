---
title: "dlaed6-f(3)"
name: "dlaed6-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaed6-f/"
description: "dlaed6.f –"
---

<p>dlaed6.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlaed6</code> (KNITER, ORGATI, RHO, D, Z, FINIT, TAU, INFO)<br />
 <i></i><code>DLAED6</code> used by sstedc. Computes one Newton step in solution of the secular equation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaed6 (integerKNITER, logicalORGATI, double precisionRHO, double precision, dimension( 3 )D, double precision, dimension( 3 )Z, double precisionFINIT, double precisionTAU, integerINFO)</h3>
<p><code>DLAED6</code> used by sstedc. Computes one Newton step in solution of the secular equation. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAED6 computes the positive or negative root (closest to the origin)
 of
 <a href="//www.systutorials.com/docs/linux/man/1-z/">z</a>(1) <a href="//www.systutorials.com/docs/linux/man/2-z/">z</a>(2) <a href="//www.systutorials.com/docs/linux/man/3-z/">z</a>(3)
 f(x) = rho + --------- + ---------- + ---------
 <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1)-x <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2)-x <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3)-x
 It is assumed that
 if ORGATI = .true. the root is between <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2) and <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3);
 otherwise it is between <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1) and <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2)
 This routine will be called by DLAED4 when necessary. In most cases,
 the root sought is the smallest in magnitude, though it might not be
 in some extremely rare situations.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>KNITER</i> </p>
<pre> KNITER is INTEGER
 Refer to DLAED4 for its significance.</pre>
<p><i>ORGATI</i> </p>
<pre> ORGATI is LOGICAL
 If ORGATI is true, the needed root is between <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2) and
 <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3); otherwise it is between <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1) and <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2). See
 DLAED4 for further details.</pre>
<p><i>RHO</i> </p>
<pre> RHO is DOUBLE PRECISION
 Refer to the equation f(x) above.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (3)
 D satisfies <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1) &lt; <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2) &lt; <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3).</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (3)
 Each of the elements in z must be positive.</pre>
<p><i>FINIT</i> </p>
<pre> FINIT is DOUBLE PRECISION
 The value of f at 0. It is more accurate than the one
 evaluated inside this routine (if someone wants to do
 so).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION
 The root of the equation f(x).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &gt; 0: if INFO = 1, failure to converge</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> 10/02/03: This version has a few statements commented out for thread
 safety (machine parameters are computed on each entry). SJH.
 05/10/06: Modified from a new version of Ren-Cang Li, use
 Gragg-Thornton-Warner cubic convergent scheme for better stability.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 141 of file dlaed6.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
