---
title: "legbps(3)"
name: "legbps"
section: "3"
letter: "l"
url: "/docs/linux/man/3-legbps/"
description: "QuantLib::Swap – Interest rate swap."
---

<p>QuantLib::Swap &#8211; Interest rate swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/swap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<p> Inherited by <code>AssetSwap</code>, <code>BMASwap</code>, and <code>VanillaSwap</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>Swap</code> (const Leg &amp;firstLeg, const Leg &amp;secondLeg) </p>
<p> <code>Swap</code> (const std::vector&lt; Leg &gt; &amp;legs, const std::vector&lt; bool &gt; &amp;payer) </p>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<p> <code>Additional interface</code> </p>
<p> <code>Date</code> <code>startDate</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> () const </p>
<p> <code>Real</code> <code>legBPS</code> (Size j) const </p>
<p> <code>Real</code> <code>legNPV</code> (Size j) const </p>
<p> const Leg &amp; <code>leg</code> (Size j) const </p>
<h3>Protected Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>Swap</code> (Size legs) </p>
<p> <code>Instrument interface</code> </p>
<p> void <code>setupExpired</code> () const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; Leg &gt; <code>legs_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>payer_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>legNPV_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>legBPS_</code> </p>
<h2>Detailed Description</h2>
<p>Interest rate swap. </p>
<p> The cash flows belonging to the first leg are paid; the ones belonging to the second leg are received.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Swap</code> (const Leg &amp; firstLeg, const Leg &amp; secondLeg)</h3>
<p>The cash flows belonging to the first leg are paid; the ones belonging to the second leg are received.</p>
<h3><code>Swap</code> (const std::vector&lt; Leg &gt; &amp; legs, const std::vector&lt; bool &gt; &amp; payer)</h3>
<p>Multi leg constructor.</p>
<h3><code>Swap</code> (Size legs) [protected]</h3>
<p>This constructor can be used by derived classes that will build their legs themselves.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>AssetSwap</code>, and <code>VanillaSwap</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>AssetSwap</code>, and <code>VanillaSwap</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
