---
title: "quantlib_cmsmmdriftcalculator(3)"
name: "quantlib_cmsmmdriftcalculator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cmsmmdriftcalculator/"
description: "QuantLib::CMSMMDriftCalculator – Drift computation for CMS market models."
---

<p>QuantLib::CMSMMDriftCalculator &#8211; Drift computation for CMS market models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/driftcomputation/cmsmmdriftcalculator.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>CMSMMDriftCalculator</code> (const <code>Matrix</code> &amp;pseudo, const std::vector&lt; <code>Spread</code> &gt; &amp;displacements, const std::vector&lt; <code>Time</code> &gt; &amp;taus, Size numeraire, Size alive, Size spanningFwds) </p>
<p> void <code>compute</code> (const <code>CMSwapCurveState</code> &amp;cs, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const<br />
 <i>Computes the drifts. </i></p>
<h2>Detailed Description</h2>
<p>Drift computation for CMS market models. </p>
<p> Returns the drift $ mu Delta t $. See Mark Joshi, <i>Rapid Computation of Drifts in a Reduced Factor </i><code>Libor</code> Market Model, Wilmott Magazine, May 2003. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
