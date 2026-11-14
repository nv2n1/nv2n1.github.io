---
title: "himalayaoption(3)"
name: "himalayaoption"
section: "3"
letter: "h"
url: "/docs/linux/man/3-himalayaoption/"
description: "QuantLib::HimalayaOption – Himalaya option."
---

<p>QuantLib::HimalayaOption &#8211; Himalaya option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/himalayaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::MultiAssetOption</code>. </p>
<h3>Public Member Functions</h3>
<p><code>HimalayaOption</code> (const std::vector&lt; <code>Date</code> &gt; &amp;fixingDates, Real strike) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h2>Detailed Description</h2>
<p>Himalaya option. </p>
<p> The payoff of a Himalaya option is computed in the following way: Given a basket of N assets, and N time periods, at the end of each period the option who performed the best is added to the average and then discarded from the basket. At the end of the N, periods the option pays the max between the strike and the average of the best performers. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This implementation still does not manage seasoned options.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>MultiAssetOption</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
