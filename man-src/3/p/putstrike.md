---

title: "putstrike(3)"
name: "putstrike"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putstrike/"
description: "QuantLib::DigitalCoupon – Digital-payoff coupon."
---

<p>QuantLib::DigitalCoupon &#8211; Digital-payoff coupon. </p>

<p> <br />
 </p>
<p>#include &lt;ql/cashflows/digitalcoupon.hpp&gt; </p>
<p>Inherits <code>QuantLib::FloatingRateCoupon</code>. </p>
<p>Inherited by <code>DigitalCmsCoupon</code>, and <code>DigitalIborCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>Constructors</code> <br />
 </p>
<p> <br />
 <code>DigitalCoupon</code> (const boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; &amp;underlying, <code>Rate</code> callStrike=<code>Null</code>&lt; <code>Rate</code> &gt;(), Position::Type callPosition=Position::Long, bool isCallITMIncluded=false, <code>Rate</code> callDigitalPayoff=<code>Null</code>&lt; <code>Rate</code> &gt;(), <code>Rate</code> putStrike=<code>Null</code>&lt; <code>Rate</code> &gt;(), Position::Type putPosition=Position::Long, bool isPutITMIncluded=false, <code>Rate</code> putDigitalPayoff=<code>Null</code>&lt; <code>Rate</code> &gt;(), const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication=boost::shared_ptr&lt; DigitalReplication &gt;()) <br />
 <i>general constructor </i> </p>
<p> <code>Coupon interface</code> <br />
 </p>
<p> <br />
 <code>Rate</code> <code>rate</code> () const <br />
 <i>accrued rate </i> <br />
 <code>Rate</code> <code>convexityAdjustment</code> () const <br />
 <i>convexity adjustment </i> </p>
<p> <code>Digital inspectors</code> <br />
 </p>
<p> <br />
 <code>Rate</code> <code>callStrike</code> () const <br />
 <br />
 <code>Rate</code> <code>putStrike</code> () const <br />
 <br />
 <code>Rate</code> <code>callDigitalPayoff</code> () const <br />
 <br />
 <code>Rate</code> <code>putDigitalPayoff</code> () const <br />
 <br />
 bool <code>hasPut</code> () const <br />
 <br />
 bool <code>hasCall</code> () const <br />
 <br />
 bool <code>hasCollar</code> () const <br />
 <br />
 bool <code>isLongPut</code> () const <br />
 <br />
 bool <code>isLongCall</code> () const <br />
 <br />
 boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying</code> () const <br />
 <br />
 <code>Rate</code> <code>callOptionRate</code> () const <br />
 <br />
 <code>Rate</code> <code>putOptionRate</code> () const <br />
 </p>
<p> <code>Observer interface</code> <br />
 </p>
<p> <br />
 void <code>update</code> () <br />
 </p>
<p> <code>Visitability</code> <br />
 </p>
<p> <br />
 virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) <br />
 <br />
 void <code>setPricer</code> (const boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; &amp;pricer) <br />
  </p>
<h3>Protected Attributes</h3>
<p> <code>Data members</code> <br />
 </p>
<p> <br />
 boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying_</code> <br />
 <br />
 <code>Rate</code> <code>callStrike_</code> <br />
 <i>strike rate for the the call option </i> <br />
 <code>Rate</code> <code>putStrike_</code> <br />
 <i>strike rate for the the put option </i> <br />
 <code>Real</code> <code>callCsi_</code> <br />
 <i>multiplicative factor of call payoff </i> <br />
 <code>Real</code> <code>putCsi_</code> <br />
 <i>multiplicative factor of put payoff </i> <br />
 bool <code>isCallATMIncluded_</code> <br />
 <i>inclusion flag og the call payoff if the call option ends at-the-money </i> <br />
 bool <code>isPutATMIncluded_</code> <br />
 <i>inclusion flag og the put payoff if the put option ends at-the-money </i> <br />
 bool <code>isCallCashOrNothing_</code> <br />
 <i>digital call option type: if true, cash-or-nothing, if false asset-or-nothing </i> <br />
 bool <code>isPutCashOrNothing_</code> <br />
 <i>digital put option type: if true, cash-or-nothing, if false asset-or-nothing </i> <br />
 <code>Rate</code> <code>callDigitalPayoff_</code> <br />
 <i>digital call option payoff rate, if any </i> <br />
 <code>Rate</code> <code>putDigitalPayoff_</code> <br />
 <i>digital put option payoff rate, if any </i> <br />
 <code>Real</code> <code>callLeftEps_</code> <br />
 <i>the left and right gaps applied in payoff replication for call </i> <br />
 <code>Real</code> <code>callRightEps_</code> <br />
 <br />
 <code>Real</code> <code>putLeftEps_</code> <br />
 <i>the left and right gaps applied in payoff replication for puf </i> <br />
 <code>Real</code> <code>putRightEps_</code> <br />
 <br />
 bool <code>hasPutStrike_</code> <br />
 <br />
 bool <code>hasCallStrike_</code> <br />
 <br />
 Replication::Type <code>replicationType_</code> <br />
 <i>Type of replication. </i>  </p>
<h2>Detailed Description</h2>
<p>Digital-payoff coupon. </p>
<p>Implementation of a floating-rate coupon with digital call/put option. Payoffs: </p>
<dl>
<dt>*</dt>
<dd> <p> <code>Coupon</code> with cash-or-nothing Digital Call rate + csi * payoffRate * Heaviside(rate-strike) </p>
 </dd>
<dt>*</dt>
<dd> <p> <code>Coupon</code> with cash-or-nothing Digital Put rate + csi * payoffRate * Heaviside(strike-rate) where csi=+1 or csi=-1. </p>
 </dd>
<dt>*</dt>
<dd> <p> <code>Coupon</code> with asset-or-nothing Digital Call rate + csi * rate * Heaviside(rate-strike) </p>
 </dd>
<dt>*</dt>
<dd> <p> <code>Coupon</code> with asset-or-nothing Digital Put rate + csi * rate * Heaviside(strike-rate) where csi=+1 or csi=-1. The evaluation of the coupon is made using the call/put spread replication method. </p>
 </dd></dl>
<p> <code>Tests</code> </p>
<dl>
<dd>  </dd>
<dl>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of Asset-or-nothing embedded option is tested by pricing the digital option with Cox-Rubinstein formula. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of deep-in-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of deep-out-of-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of Cash-or-nothing embedded option is tested by pricing the digital option with Reiner-Rubinstein formula. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of deep-in-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value in case of deep-out-of-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value is tested checking the correctness of the call-put parity relation. </p>
 </dd>
<dt>*</dt>
<dd> <p> the correctness of the returned value is tested by the relationship between prices in case of different replication types. </p>
 </dd></dl>
<h2>Member Function Documentation</h2>
<code></code><h3>Rate callOptionRate () const</h3>
<p>Returns the call option rate (multiplied by: nominal*accrualperiod*discount is the NPV of the option)  </p>
<code></code><h3>Rate putOptionRate () const</h3>
<p>Returns the put option rate (multiplied by: nominal*accrualperiod*discount is the NPV of the option)  </p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p>Reimplemented from <code>FloatingRateCoupon</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
