---
title: "update(3)"
name: "update"
section: "3"
letter: "u"
url: "/docs/linux/man/3-update/"
description: "QuantLib::CappedFlooredCoupon – Capped and/or floored floating-rate coupon."
---

<p>QuantLib::CappedFlooredCoupon &#8211; Capped and/or floored floating-rate coupon. </p>
<h2>Synopsis</h2>
<pre><code>void update ()



Visitability</code></pre>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>. Inherited by CappedFlooredCmsCoupon, and CappedFlooredIborCoupon.</p>
<h3>Public Member Functions</h3>
<p>void update ()</p>
<p>Visitability <code>Coupon interface</code> </p>
<p> <code>Rate</code> <code>rate</code> () const<br />
 <i>accrued rate </i><br />
 <code>Rate</code> <code>convexityAdjustment</code> () const<br />
 <i>convexity adjustment </i> <code>Observer interface</code> </p>
<pre><code>void update ()



Visitability</code></pre>
<p> boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying_</code> </p>
<p> bool <code>isCapped_</code> </p>
<p> bool <code>isFloored_</code> </p>
<p> <code>Rate</code> <code>cap_</code> </p>
<p> <code>Rate</code> <code>floor_</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<p> bool <code>isCapped</code> () const </p>
<p> bool <code>isFloored</code> () const </p>
<p> void <code>setPricer</code> (const boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; &amp;pricer)</p>
<h2>Detailed Description</h2>
<p>Capped and/or floored floating-rate coupon. </p>
<p> The payoff $ P $ of a capped floating-rate coupon is: [ P = N imes T imes min(a L + b, C). ] The payoff of a floored floating-rate coupon is: [ P = N imes T imes max(a L + b, F). ] The payoff of a collared floating-rate coupon is: [ P = N imes T imes min(max(a L + b, F), C). ] </p>
<p> where $ N $ is the notional, $ T $ is the accrual time, $ L $ is the floating rate, $ a $ is its gearing, $ b $ is the spread, and $ C $ and $ F $ the strikes. </p>
<p> They can be decomposed in the following manner. Decomposition of a capped floating rate coupon: [ R = min(a L + b, C) = (a L + b) + min(C &#8211; b &#8211; on&quot;</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>FloatingRateCoupon</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
