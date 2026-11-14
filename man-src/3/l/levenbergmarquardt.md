---
title: "levenbergmarquardt(3)"
name: "levenbergmarquardt"
section: "3"
letter: "l"
url: "/docs/linux/man/3-levenbergmarquardt/"
description: "QuantLib::LevenbergMarquardt – Levenberg-Marquardt optimization method."
---

<p>QuantLib::LevenbergMarquardt &#8211; Levenberg-Marquardt optimization method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/levenbergmarquardt.hpp&gt; </p>
<p> Inherits <code>QuantLib::OptimizationMethod</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LevenbergMarquardt</code> (<code>Real</code> epsfcn=1.0e-8, Real xtol=1.0e-8, Real gtol=1.0e-8) </p>
<p> virtual EndCriteria::Type <code>minimize</code> (<code>Problem</code> &amp;P, const <code>EndCriteria</code> &amp;endCriteria)<br />
 <i>minimize the optimization problem P </i><br />
 virtual <code>Integer</code> <code>getInfo</code> () const </p>
<p> void <code>fcn</code> (int m, int n, double *x, double *fvec, int *iflag) </p>
<h2>Detailed Description</h2>
<p>Levenberg-Marquardt optimization method. </p>
<p> This implementation is based on MINPACK (&lt;<a rel="nofollow" href="http://www.netlib.org/minpack">http://www.netlib.org/minpack</a>&gt;, &lt;<a href="http://www.netlib.org/cephes/linalg.tgz">http://www.netlib.org/cephes/linalg.tgz</a>&gt;) </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
