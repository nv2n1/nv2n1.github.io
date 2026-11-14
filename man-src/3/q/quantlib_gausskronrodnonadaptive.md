---
title: "quantlib_gausskronrodnonadaptive(3)"
name: "quantlib_gausskronrodnonadaptive"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gausskronrodnonadaptive/"
description: "QuantLib::GaussKronrodNonAdaptive – Integral of a 1-dimensional function using the Gauss-Kronrod methods."
---

<p>QuantLib::GaussKronrodNonAdaptive &#8211; Integral of a 1-dimensional function using the Gauss-Kronrod methods. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/kronrodintegral.hpp&gt; </p>
<p> Inherits QuantLib::Integrator. </p>
<h3>Public Member Functions</h3>
<p><code>GaussKronrodNonAdaptive</code> (Real absoluteAccuracy, Size maxEvaluations, Real relativeAccuracy) </p>
<p> void <code>setRelativeAccuracy</code> (Real) </p>
<p> Real <code>relativeAccuracy</code> () const </p>
<h3>Protected Member Functions</h3>
<p>Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<h2>Detailed Description</h2>
<p>Integral of a 1-dimensional function using the Gauss-Kronrod methods. </p>
<p> This class provide a non-adaptive integration procedure which uses fixed Gauss-Kronrod abscissae to sample the integrand at a maximum of 87 points. It is provided for fast integration of smooth functions. </p>
<p> This function applies the Gauss-Kronrod 10-point, 21-point, 43-point and 87-point integration rules in succession until an estimate of the integral of f over (a, b) is achieved within the desired absolute and relative error limits, epsabs and epsrel. The function returns the final approximation, result, an estimate of the absolute error, abserr and the number of function evaluations used, neval. The Gauss-Kronrod rules are designed in such a way that each rule uses all the results of its predecessors, in order to minimize the total number of function evaluations. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
