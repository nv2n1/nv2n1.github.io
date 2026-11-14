---
title: "value(3)"
name: "value"
section: "3"
letter: "v"
url: "/docs/linux/man/3-value/"
description: "QuantLib::DiscreteGeometricASO – Discrete geometric average-strike Asian option (European style)."
---

<p>QuantLib::DiscreteGeometricASO &#8211; Discrete geometric average-strike Asian option (European style). </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/legacy/pricers/discretegeometricaso.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::SingleAssetOption</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DiscreteGeometricASO</code> (Option::Type type, <code>Real</code> underlying, <code>Spread</code> dividendYield, <code>Rate</code> riskFreeRate, const std::vector&lt; <code>Time</code> &gt; &amp;times, <code>Volatility</code> volatility) </p>
<p> <code>Real</code> <code>value</code> () const </p>
<p> <code>Real</code> <code>delta</code> () const </p>
<p> <code>Real</code> <code>gamma</code> () const </p>
<p> <code>Real</code> <code>theta</code> () const </p>
<p> boost::shared_ptr&lt; <code>SingleAssetOption</code> &gt; <code>clone</code> () const</p>
<h2>Detailed Description</h2>
<p>Discrete geometric average-strike Asian option (European style). </p>
<p> This class implements a discrete geometric average strike asian option, with european exercise. The formula is from &#8216;Asian Option&#8217;, E. Levy (1997) in &#8216;Exotic Options: The State of the Art&#8217;, edited by L. Clewlow, C. Strickland, pag65-97</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
