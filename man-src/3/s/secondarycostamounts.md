---
title: "secondarycostamounts(3)"
name: "secondarycostamounts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-secondarycostamounts/"
description: "QuantLib::Commodity – Commodity base class."
---

<p>QuantLib::Commodity &#8211; <code>Commodity</code> base class. </p>
<h2>Synopsis</h2>
<pre><code>Commodity (const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts)



const boost::shared_ptr&lt; SecondaryCosts &gt; &amp; secondaryCosts () const



const SecondaryCostAmounts &amp; secondaryCostAmounts () const



const PricingErrors &amp; pricingErrors () const



void addPricingError (PricingError::Level errorLevel, const std::string &amp;error, const std::string &amp;detail='') const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>. Inherited by <code>EnergyCommodity</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Commodity (const boost::shared_ptr&lt; SecondaryCosts &gt; &amp;secondaryCosts)



const boost::shared_ptr&lt; SecondaryCosts &gt; &amp; secondaryCosts () const



const SecondaryCostAmounts &amp; secondaryCostAmounts () const



const PricingErrors &amp; pricingErrors () const



void addPricingError (PricingError::Level errorLevel, const std::string &amp;error, const std::string &amp;detail='') const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; SecondaryCosts &gt; <code>secondaryCosts_</code> </p>
<p> PricingErrors <code>pricingErrors_</code> </p>
<p> SecondaryCostAmounts <code>secondaryCostAmounts_</code></p>
<h2>Detailed Description</h2>
<p><code>Commodity</code> base class.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
