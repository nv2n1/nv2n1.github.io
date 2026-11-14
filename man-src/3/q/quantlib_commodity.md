---
title: "quantlib_commodity(3)"
name: "quantlib_commodity"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_commodity/"
description: "QuantLib::Commodity – Commodity base class."
---

<p>QuantLib::Commodity &#8211; <code>Commodity</code> base class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/commodity.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<p> Inherited by <code>EnergyCommodity</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Commodity</code> (const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts) </p>
<p> const boost::shared_ptr&lt; SecondaryCosts &gt; &amp; <code>secondaryCosts</code> () const </p>
<p> const SecondaryCostAmounts &amp; <code>secondaryCostAmounts</code> () const </p>
<p> const PricingErrors &amp; <code>pricingErrors</code> () const </p>
<p> void <code>addPricingError</code> (PricingError::Level errorLevel, const std::string &amp;error, const std::string &amp;detail=&#8221;) const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; SecondaryCosts &gt; <code>secondaryCosts_</code> </p>
<p> PricingErrors <code>pricingErrors_</code> </p>
<p> SecondaryCostAmounts <code>secondaryCostAmounts_</code> </p>
<h2>Detailed Description</h2>
<p><code>Commodity</code> base class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
