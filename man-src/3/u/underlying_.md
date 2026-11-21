---
title: "underlying_(3)"
name: "underlying_"
section: "3"
letter: "u"
url: "/docs/linux/man/3-underlying_/"
description: "QuantLib::CappedFlooredCoupon – Capped and/or floored floating-rate coupon."
---
<p>QuantLib::CappedFlooredCoupon &#8211; Capped and/or floored floating-rate coupon. </p>
<h2>SYNOPSIS</h2>
<p> <br />
 </p>
<p>#include &lt;ql/cashflows/capflooredcoupon.hpp&gt; </p>
<p>Inherits <code>QuantLib::FloatingRateCoupon</code>. </p>
<p>Inherited by CappedFlooredCmsCoupon, and CappedFlooredIborCoupon. </p>
<h3>Public Member Functions</h3>
<p> <br />
 <code>CappedFlooredCoupon</code> (const boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; &amp;underlying, <code>Rate</code> cap=<code>Null</code>&lt; <code>Rate</code> &gt;(), <code>Rate</code> floor=<code>Null</code>&lt; <code>Rate</code> &gt;()) <br />
 <br />
 <code>Rate</code> <code>cap</code> () const <br />
 <i>cap </i> <br />
 <code>Rate</code> <code>floor</code> () const <br />
 <i>floor </i> <br />
 <code>Rate</code> <code>effectiveCap</code> () const <br />
 <i>effective cap of fixing </i> <br />
 <code>Rate</code> <code>effectiveFloor</code> () const <br />
 <i>effective floor of fixing </i> </p>
<p> <code>Coupon interface</code> <br />
 </p>
<p> <br />
 <code>Rate</code> <code>rate</code> () const <br />
 <i>accrued rate </i> <br />
 <code>Rate</code> <code>convexityAdjustment</code> () const <br />
 <i>convexity adjustment </i> </p>
<p> <code>Observer interface</code> <br />
 </p>
<p> <br />
 void <code>update</code> () <br />
  </p>
<h3>Visitability</h3>
<p> <br />
 boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>underlying_</code> <br />
 <br />
 bool <code>isCapped_</code> <br />
 <br />
 bool <code>isFloored_</code> <br />
 <br />
 <code>Rate</code> <code>cap_</code> <br />
 <br />
 <code>Rate</code> <code>floor_</code> <br />
 <br />
 virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) <br />
 <br />
 bool <code>isCapped</code> () const <br />
 <br />
 bool <code>isFloored</code> () const <br />
 <br />
 void <code>setPricer</code> (const boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; &amp;pricer) <br />
  </p>
<h2>Detailed Description</h2>
<p>Capped and/or floored floating-rate coupon. </p>
<p>The payoff $ P $ of a capped floating-rate coupon is: [ P = N imes T imes min(a L + b, C). ] The payoff of a floored floating-rate coupon is: [ P = N imes T imes max(a L + b, F). ] The payoff of a collared floating-rate coupon is: [ P = N imes T imes min(max(a L + b, F), C). ] </p>
<p>where $ N $ is the notional, $ T $ is the accrual time, $ L $ is the floating rate, $ a $ is its gearing, $ b $ is the spread, and $ C $ and $ F $ the strikes. </p>
<p>They can be decomposed in the following manner. Decomposition of a capped floating rate coupon: [ R = min(a L + b, C) = (a L + b) + min(C &#8211; b &#8211; on&quot; </p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p>Reimplemented from <code>FloatingRateCoupon</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">Public Member Functions</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Visitability</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAF">Detailed Description</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAG">void update () [virtual]</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAH">Author</a></dt>
<dd>  </dd></dl>
