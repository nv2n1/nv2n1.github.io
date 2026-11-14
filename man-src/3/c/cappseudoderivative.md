---
title: "cappseudoderivative(3)"
name: "cappseudoderivative"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cappseudoderivative/"
description: "QuantLib::CapPseudoDerivative –"
---

<p>QuantLib::CapPseudoDerivative &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwisegreeks/swaptionpseudojacobian.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>CapPseudoDerivative</code> (boost::shared_ptr&lt; <code>MarketModel</code> &gt; inputModel, <code>Real</code> strike, Size startIndex, Size endIndex, <code>Real</code> firstDF) </p>
<p> const <code>Matrix</code> &amp; <code>volatilityDerivative</code> (Size i) const </p>
<p> const <code>Matrix</code> &amp; <code>priceDerivative</code> (Size i) const </p>
<p> <code>Real</code> <code>impliedVolatility</code> () const </p>
<h2>Detailed Description</h2>
<p>In order to compute market vegas, we need a class that gives the derivative of a cap implied vol against changes in pseudo-root elements. This is that class. </p>
<p> The operation is non-trivial because the cap implied vol has a complicated relationship with the caplet implied vols. </p>
<p> This is tested in the pathwise vegas routine in MarketModels.cpp </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
