---

title: "paysatdefaulttime_(3)"
name: "paysatdefaulttime_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paysatdefaulttime_/"
description: "QuantLib::CreditDefaultSwap – Credit default swap."
---

<p>QuantLib::CreditDefaultSwap &#8211; Credit default swap. </p>

<p> <br />
 </p>
<p>#include &lt;ql/instruments/creditdefaultswap.hpp&gt; </p>
<p>Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>Constructors</code> <br />
 </p>
<p> <br />
 <code>CreditDefaultSwap</code> (Protection::Side side, Real notional, <code>Rate</code> spread, const <code>Schedule</code> &amp;schedule, <code>BusinessDayConvention</code> paymentConvention, const <code>DayCounter</code> &amp;dayCounter, bool settlesAccrual=true, bool paysAtDefaultTime=true, const boost::shared_ptr&lt; <code>Claim</code> &gt; &amp;=boost::shared_ptr&lt; <code>Claim</code> &gt;()) <br />
 </p>
<p> <code>Instrument interface</code> <br />
 </p>
<p> <br />
 bool <code>isExpired</code> () const <br />
 <i>returns whether the instrument is still tradable. </i> <br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const <br />
 <br />
 void <code>fetchResults</code> (const PricingEngine::results *) const <br />
 </p>
<p> <code>Inspectors</code> <br />
 </p>
<p> <br />
 Protection::Side <code>side</code> () const <br />
 <br />
 Real <code>notional</code> () const <br />
 <br />
 <code>Rate</code> <code>spread</code> () const <br />
 <br />
 bool <code>settlesAccrual</code> () const <br />
 <br />
 bool <code>paysAtDefaultTime</code> () const <br />
 <br />
 const Leg &amp; <code>coupons</code> () const <br />
 </p>
<p> <code>Results</code> <br />
 </p>
<p> <br />
 <code>Rate</code> <code>fairSpread</code> () const <br />
 <br />
 Real <code>couponLegBPS</code> () const <br />
 <br />
 Real <code>couponLegNPV</code> () const <br />
 <br />
 Real <code>defaultLegNPV</code> () const <br />
 <br />
 <code>Rate</code> <code>impliedHazardRate</code> (Real targetNPV, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, const <code>DayCounter</code> &amp;dayCounter, Real recoveryRate=0.4, Real accuracy=1.0e-6) const <br />
  </p>
<h3>Protected Member Functions</h3>
<p> <code>Instrument interface</code> <br />
 </p>
<p> <br />
 void <code>setupExpired</code> () const <br />
  </p>
<h3>Protected Attributes</h3>
<p> <br />
 Protection::Side <code>side_</code> <br />
 <br />
 Real <code>notional_</code> <br />
 <br />
 <code>Rate</code> <code>spread_</code> <br />
 <br />
 bool <code>settlesAccrual_</code> <br />
 <br />
 bool <code>paysAtDefaultTime_</code> <br />
 <br />
 boost::shared_ptr&lt; <code>Claim</code> &gt; <code>claim_</code> <br />
 <br />
 Leg <code>leg_</code> <br />
 <br />
 <code>Rate</code> <code>fairSpread_</code> <br />
 <br />
 Real <code>couponLegBPS_</code> <br />
 <br />
 Real <code>couponLegNPV_</code> <br />
 <br />
 Real <code>defaultLegNPV_</code> <br />
  </p>
<h2>Detailed Description</h2>
<p>Credit default swap. </p>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> This instrument currently assumes that the issuer did not default until today&#8217;s date. </p>
 </dd></dl>
<p> <code>Warning</code> </p>
<dl>
<dd> <p> if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-spread calculation. This might not be what you want. </p>
 </dd></dl>
<p> <code>Examples: </code> </p>
<p> <code>CDS.cpp</code>.  </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p>Reimplemented from <code>Instrument</code>.  </p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p>Reimplemented from <code>Instrument</code>.  </p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p>Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
