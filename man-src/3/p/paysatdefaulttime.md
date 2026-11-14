---
title: "paysatdefaulttime(3)"
name: "paysatdefaulttime"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paysatdefaulttime/"
description: "QuantLib::CreditDefaultSwap – Credit default swap."
---

<p>QuantLib::CreditDefaultSwap &#8211; Credit default swap. </p>
<h2>Synopsis</h2>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 void setupExpired () const</p>
<p>Protected Attributes <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const<br />
 <code>Inspectors</code> </p>
<p> Protection::Side <code>side</code> () const </p>
<p> Real <code>notional</code> () const </p>
<p> <code>Rate</code> <code>spread</code> () const </p>
<p> bool <code>settlesAccrual</code> () const </p>
<p> bool <code>paysAtDefaultTime</code> () const </p>
<p> const Leg &amp; <code>coupons</code> () const<br />
 <code>Results</code><br />
 void setupExpired () const</p>
<p>Protected Attributes <code>Instrument interface</code> </p>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> Protection::Side <code>side_</code> </p>
<p> Real <code>notional_</code> </p>
<p> <code>Rate</code> <code>spread_</code> </p>
<p> bool <code>settlesAccrual_</code> </p>
<p> bool <code>paysAtDefaultTime_</code> </p>
<p> boost::shared_ptr&lt; <code>Claim</code> &gt; <code>claim_</code> </p>
<p> Leg <code>leg_</code> </p>
<p> <code>Rate</code> <code>fairSpread_</code> </p>
<p> Real <code>couponLegBPS_</code> </p>
<p> Real <code>couponLegNPV_</code> </p>
<p> Real <code>defaultLegNPV_</code></p>
<h2>Detailed Description</h2>
<p>Credit default swap. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This instrument currently assumes that the issuer did not default until today&#8217;s date.</dl>
<p> <code>Warning</code></p>
<dl>
<dd>if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-spread calculation. This might not be what you want.</dl>
<p> <code>Examples: </code> </p>
<p> <code>CDS.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
