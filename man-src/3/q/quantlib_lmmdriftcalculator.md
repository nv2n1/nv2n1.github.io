---
title: "quantlib_lmmdriftcalculator(3)"
name: "quantlib_lmmdriftcalculator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lmmdriftcalculator/"
description: "QuantLib::LMMDriftCalculator – Drift computation for log-normal Libor market models."
---

<p>QuantLib::LMMDriftCalculator &#8211; Drift computation for log-normal Libor market models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/driftcomputation/lmmdriftcalculator.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>LMMDriftCalculator</code> (const <code>Matrix</code> &amp;pseudo, const std::vector&lt; <code>Spread</code> &gt; &amp;displacements, const std::vector&lt; <code>Time</code> &gt; &amp;taus, Size numeraire, Size alive) </p>
<p> void <code>compute</code> (const <code>LMMCurveState</code> &amp;cs, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const<br />
 <i>Computes the drifts. </i><br />
 void <code>compute</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;fwds, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const </p>
<p> void <code>computePlain</code> (const <code>LMMCurveState</code> &amp;cs, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const </p>
<p> void <code>computePlain</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;fwds, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const </p>
<p> void <code>computeReduced</code> (const <code>LMMCurveState</code> &amp;cs, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const </p>
<p> void <code>computeReduced</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;fwds, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const </p>
<h2>Detailed Description</h2>
<p>Drift computation for log-normal Libor market models. </p>
<p> Returns the drift $ mu Delta t $. See Mark Joshi, <i>Rapid Computation of Drifts in a Reduced Factor </i><code>Libor</code> Market Model, Wilmott Magazine, May 2003.</p>
<h2>Member Function Documentation</h2>
<h3>void computePlain (const <code>LMMCurveState</code> &amp; cs, std::vector&lt; <code>Real</code> &gt; &amp; drifts) const</h3>
<p>Computes the drifts without factor reduction as in eqs. 2, 4 of ref. [1] (uses the covariance matrix directly).</p>
<h3>void computeReduced (const <code>LMMCurveState</code> &amp; cs, std::vector&lt; <code>Real</code> &gt; &amp; drifts) const</h3>
<p>Computes the drifts with factor reduction as in eq. 7 of ref. [1] (uses pseudo square root of the covariance matrix). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
