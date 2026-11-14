---
title: "smmdriftcalculator(3)"
name: "smmdriftcalculator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smmdriftcalculator/"
description: "QuantLib::SMMDriftCalculator – Drift computation for coterminal swap market models."
---

<p>QuantLib::SMMDriftCalculator &#8211; Drift computation for coterminal swap market models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/driftcomputation/smmdriftcalculator.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>SMMDriftCalculator</code> (const <code>Matrix</code> &amp;pseudo, const std::vector&lt; <code>Spread</code> &gt; &amp;displacements, const std::vector&lt; <code>Time</code> &gt; &amp;taus, Size numeraire, Size alive) </p>
<p> void <code>compute</code> (const <code>CoterminalSwapCurveState</code> &amp;cs, std::vector&lt; <code>Real</code> &gt; &amp;drifts) const<br />
 <i>Computes the drifts. </i></p>
<h2>Detailed Description</h2>
<p>Drift computation for coterminal swap market models. </p>
<p> Returns the drift $ mu Delta t $. See Mark Joshi, Lorenzo Liesch, <i>Effective Implementation Of Generic Market Models</i>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
