---
title: "orthogonalizedbumpfinder(3)"
name: "orthogonalizedbumpfinder"
section: "3"
letter: "o"
url: "/docs/linux/man/3-orthogonalizedbumpfinder/"
description: "QuantLib::OrthogonalizedBumpFinder –"
---

<p>QuantLib::OrthogonalizedBumpFinder &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwisegreeks/bumpinstrumentjacobian.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>OrthogonalizedBumpFinder</code> (const <code>VegaBumpCollection</code> &amp;bumps, const std::vector&lt; VolatilityBumpInstrumentJacobian::Swaption &gt; &amp;swaptions, const std::vector&lt; VolatilityBumpInstrumentJacobian::Cap &gt; &amp;caps, <code>Real</code> multiplierCutOff, <code>Real</code> tolerance) </p>
<p> void <code>GetVegaBumps</code> (std::vector&lt; std::vector&lt; <code>Matrix</code> &gt; &gt; &amp;theBumps) const </p>
<h2>Detailed Description</h2>
<p>Pass in a market model, a list of instruments, and possible bumps. </p>
<p> Get out pseudo-root bumps that shift each implied vol by one percent, and leave the other instruments fixed. </p>
<p> If the contribution of an instrument is too correlated with other instruments used, discard it. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
