---
title: "quantlib_floatingratecouponpricer(3)"
name: "quantlib_floatingratecouponpricer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_floatingratecouponpricer/"
description: "QuantLib::FloatingRateCouponPricer – generic pricer for floating-rate coupons"
---

<p>QuantLib::FloatingRateCouponPricer &#8211; generic pricer for floating-rate coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/couponpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>CmsCouponPricer</code>, <code>IborCouponPricer</code>, RangeAccrualPricer, and SubPeriodsPricer. </p>
<h3>Public Member Functions</h3>
<p><code>required interface</code> </p>
<p> virtual <code>Real</code> <code>swapletPrice</code> () const =0 </p>
<p> virtual Rate <code>swapletRate</code> () const =0 </p>
<p> virtual <code>Real</code> <code>capletPrice</code> (Rate effectiveCap) const =0 </p>
<p> virtual Rate <code>capletRate</code> (Rate effectiveCap) const =0 </p>
<p> virtual <code>Real</code> <code>floorletPrice</code> (Rate effectiveFloor) const =0 </p>
<p> virtual Rate <code>floorletRate</code> (Rate effectiveFloor) const =0 </p>
<p> virtual void <code>initialize</code> (const <code>FloatingRateCoupon</code> &amp;coupon)=0 </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p>generic pricer for floating-rate coupons</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
