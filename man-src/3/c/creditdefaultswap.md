---
title: "creditdefaultswap(3)"
name: "creditdefaultswap"
section: "3"
letter: "c"
url: "/docs/linux/man/3-creditdefaultswap/"
description: "QuantLib::CreditDefaultSwap – Credit default swap."
---

<p>QuantLib::CreditDefaultSwap &#8211; Credit default swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/creditdefaultswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>CreditDefaultSwap</code> (Protection::Side side, Real notional, <code>Rate</code> spread, const <code>Schedule</code> &amp;schedule, <code>BusinessDayConvention</code> paymentConvention, const <code>DayCounter</code> &amp;dayCounter, bool settlesAccrual=true, bool paysAtDefaultTime=true, const boost::shared_ptr&lt; <code>Claim</code> &gt; &amp;=boost::shared_ptr&lt; <code>Claim</code> &gt;()) </p>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<p> <code>Inspectors</code> </p>
<p> Protection::Side <code>side</code> () const </p>
<p> Real <code>notional</code> () const </p>
<p> <code>Rate</code> <code>spread</code> () const </p>
<p> bool <code>settlesAccrual</code> () const </p>
<p> bool <code>paysAtDefaultTime</code> () const </p>
<p> const Leg &amp; <code>coupons</code> () const </p>
<p> <code>Results</code> </p>
<p> <code>Rate</code> <code>fairSpread</code> () const </p>
<p> Real <code>couponLegBPS</code> () const </p>
<p> Real <code>couponLegNPV</code> () const </p>
<p> Real <code>defaultLegNPV</code> () const </p>
<p> <code>Rate</code> <code>impliedHazardRate</code> (Real targetNPV, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, const <code>DayCounter</code> &amp;dayCounter, Real recoveryRate=0.4, Real accuracy=1.0e-6) const </p>
<h3>Protected Member Functions</h3>
<p><code>Instrument interface</code> </p>
<p> void <code>setupExpired</code> () const </p>
<h3>Protected Attributes</h3>
<p>Protection::Side <code>side_</code> </p>
<p> Real <code>notional_</code> </p>
<p> <code>Rate</code> <code>spread_</code> </p>
<p> bool <code>settlesAccrual_</code> </p>
<p> bool <code>paysAtDefaultTime_</code> </p>
<p> boost::shared_ptr&lt; <code>Claim</code> &gt; <code>claim_</code> </p>
<p> Leg <code>leg_</code> </p>
<p> <code>Rate</code> <code>fairSpread_</code> </p>
<p> Real <code>couponLegBPS_</code> </p>
<p> Real <code>couponLegNPV_</code> </p>
<p> Real <code>defaultLegNPV_</code> </p>
<h2>Detailed Description</h2>
<p>Credit default swap. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This instrument currently assumes that the issuer did not default until today&#8217;s date.</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
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
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
