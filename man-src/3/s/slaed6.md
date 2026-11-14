---
title: "slaed6(3)"
name: "slaed6"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed6/"
description: "slaed6.f –"
---

<h2 class="name">NAME</h2>
<p> slaed6.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaed6</code> (KNITER, ORGATI, RHO, D, Z, FINIT, TAU, INFO)<br />
 <i></i><code>SLAED6</code> used by sstedc. Computes one Newton step in solution of the secular equation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed6 (integerKNITER, logicalORGATI, realRHO, real, dimension( 3 )D, real, dimension( 3 )Z, realFINIT, realTAU, integerINFO)</h3>
<p> <code>SLAED6</code> used by sstedc. Computes one Newton step in solution of the secular equation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SLAED6 computes the positive or negative root(closest to the origin)
                                    of
    z(1) z(2) z(3)
        f(x) = rho + -- -- -- -- -+-- -- -- -- --+-- -- -- -- -d(1) - x d(2) - x d(3) - x It is assumed that if ORGATI =.true.the root is between d(2) and d(3);
otherwise it is between d(1) and d(2)
                                     This routine will be called by SLAED4 when necessary.In most cases,
    the root sought is the smallest in magnitude, though it might not be in some extremely rare situations.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>KNITER</i> </p>
<pre>
          KNITER is INTEGER
               Refer to SLAED4 for its significance.
</pre>
<p> <i>ORGATI</i> </p>
<pre>
          ORGATI is LOGICAL
               If ORGATI is true, the needed root is between <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2) and
               <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3); otherwise it is between <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1) and <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2).  See
               SLAED4 for further details.
</pre>
<p> <i>RHO</i> </p>
<pre>
          RHO is REAL
               Refer to the equation f(x) above.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (3)
               D satisfies <a href="//www.systutorials.com/docs/linux/man/1-d/">d</a>(1) &lt; <a href="//www.systutorials.com/docs/linux/man/2-d/">d</a>(2) &lt; <a href="//www.systutorials.com/docs/linux/man/3-d/">d</a>(3).
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (3)
               Each of the elements in z must be positive.
</pre>
<p> <i>FINIT</i> </p>
<pre>
          FINIT is REAL
               The value of f at 0. It is more accurate than the one
               evaluated inside this routine (if someone wants to do
               so).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is REAL
               The root of the equation f(x).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
               = 0: successful exit
               &gt; 0: if INFO = 1, failure to converge
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  10/02/03: This version has a few statements commented out for thread
  safety (machine parameters are computed on each entry). SJH.
  05/10/06: Modified from a new version of Ren-Cang Li, use
     Gragg-Thornton-Warner cubic convergent scheme for better stability.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 141 of file slaed6.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
