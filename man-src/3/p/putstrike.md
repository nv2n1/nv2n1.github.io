---
title: "putstrike(3)"
name: "putstrike"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putstrike/"
description: "QuantLib::DigitalCoupon – Digital-payoff coupon."
---

<p>QuantLib::DigitalCoupon &#8211; Digital-payoff coupon. </p>
<h2>Synopsis</h2>
<pre><code>void update ()</code></pre>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>. Inherited by <code>DigitalCmsCoupon</code>, and <code>DigitalIborCoupon</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 void update () <code>Coupon interface</code> </p>
<p> <code>Rate</code> <code>rate</code> () const<br />
 <i>accrued rate </i><br />
 <code>Rate</code> <code>convexityAdjustment</code> () const<br />
 <i>convexity adjustment </i> <code>Digital inspectors</code> </p>
<p> <code>Rate</code> <code>callStrike</code> () const </p>
<p> <code>Rate</code> <code>putStrike</code> () const </p>
<p> <code>Rate</code> <code>callDigitalPayoff</code> () const </p>
<p> <code>Rate</code> <code>putDigitalPayoff</code> () const </p>
<p> bool <code>hasPut</code> () const </p>
<p> bool <code>hasCall</code> () const </p>
<p> bool <code>hasCollar</code> () const </p>
<p> bool <code>isLongPut</code> () const </p>
<p> bool <code>isLongCall</code> () const </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying</code> () const </p>
<p> <code>Rate</code> <code>callOptionRate</code> () const </p>
<p> <code>Rate</code> <code>putOptionRate</code> () const<br />
 <code>Observer interface</code> </p>
<pre><code>void update ()</code></pre>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<p> void <code>setPricer</code> (const boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; &amp;pricer)</p>
<h3>Protected Attributes</h3>
<p><code>Data members</code> </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying_</code> </p>
<p> <code>Rate</code> <code>callStrike_</code><br />
 <i>strike rate for the the call option </i><br />
 <code>Rate</code> <code>putStrike_</code><br />
 <i>strike rate for the the put option </i><br />
 <code>Real</code> <code>callCsi_</code><br />
 <i>multiplicative factor of call payoff </i><br />
 <code>Real</code> <code>putCsi_</code><br />
 <i>multiplicative factor of put payoff </i><br />
 bool <code>isCallATMIncluded_</code><br />
 <i>inclusion flag og the call payoff if the call option ends at-the-money </i><br />
 bool <code>isPutATMIncluded_</code><br />
 <i>inclusion flag og the put payoff if the put option ends at-the-money </i><br />
 bool <code>isCallCashOrNothing_</code><br />
 <i>digital call option type: if true, cash-or-nothing, if false asset-or-nothing </i><br />
 bool <code>isPutCashOrNothing_</code><br />
 <i>digital put option type: if true, cash-or-nothing, if false asset-or-nothing </i><br />
 <code>Rate</code> <code>callDigitalPayoff_</code><br />
 <i>digital call option payoff rate, if any </i><br />
 <code>Rate</code> <code>putDigitalPayoff_</code><br />
 <i>digital put option payoff rate, if any </i><br />
 <code>Real</code> <code>callLeftEps_</code><br />
 <i>the left and right gaps applied in payoff replication for call </i><br />
 <code>Real</code> <code>callRightEps_</code> </p>
<p> <code>Real</code> <code>putLeftEps_</code><br />
 <i>the left and right gaps applied in payoff replication for puf </i><br />
 <code>Real</code> <code>putRightEps_</code> </p>
<p> bool <code>hasPutStrike_</code> </p>
<p> bool <code>hasCallStrike_</code> </p>
<p> Replication::Type <code>replicationType_</code><br />
 <i>Type of replication. </i></p>
<h2>Detailed Description</h2>
<p>Digital-payoff coupon. </p>
<p> Implementation of a floating-rate coupon with digital call/put option. Payoffs:</p>
<dl>
<dt>*</p>
<dd><code>Coupon</code> with cash-or-nothing Digital Call rate + csi * payoffRate * Heaviside(rate-strike)</p>
<dt>*</p>
<dd><code>Coupon</code> with cash-or-nothing Digital Put rate + csi * payoffRate * Heaviside(strike-rate) where csi=+1 or csi=-1.</p>
<dt>*</p>
<dd><code>Coupon</code> with asset-or-nothing Digital Call rate + csi * rate * Heaviside(rate-strike)</p>
<dt>*</p>
<dd><code>Coupon</code> with asset-or-nothing Digital Put rate + csi * rate * Heaviside(strike-rate) where csi=+1 or csi=-1. The evaluation of the coupon is made using the call/put spread replication method.</dl>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned value in case of Asset-or-nothing embedded option is tested by pricing the digital option with Cox-Rubinstein formula.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of deep-in-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of deep-out-of-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of Cash-or-nothing embedded option is tested by pricing the digital option with Reiner-Rubinstein formula.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of deep-in-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of deep-out-of-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested checking the correctness of the call-put parity relation.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by the relationship between prices in case of different replication types.</dl>
</dl>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> callOptionRate () const</h3>
<p>Returns the call option rate (multiplied by: nominal*accrualperiod*discount is the NPV of the option)</p>
<h3><code>Rate</code> putOptionRate () const</h3>
<p>Returns the put option rate (multiplied by: nominal*accrualperiod*discount is the NPV of the option)</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>FloatingRateCoupon</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
