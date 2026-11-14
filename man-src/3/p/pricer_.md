---
title: "pricer_(3)"
name: "pricer_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pricer_/"
description: "QuantLib::FloatingRateCoupon – base floating-rate coupon class"
---

<p>QuantLib::FloatingRateCoupon &#8211; base floating-rate coupon class </p>
<h2>Synopsis</h2>
<pre><code>void update ()</code></pre>
<p> Inherits <code>QuantLib::Coupon</code>, and <code>QuantLib::Observer</code>. Inherited by <code>AverageBMACoupon</code>, <code>CappedFlooredCoupon</code>, <code>CmsCoupon</code>, <code>DigitalCoupon</code>, <code>IborCoupon</code>, RangeAccrualFloatersCoupon, and SubPeriodsCoupon.</p>
<h3>Public Member Functions</h3>
<p>void update () <code>CashFlow interface</code> </p>
<p> <code>Real</code> <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i> <code>Coupon interface</code> </p>
<p> <code>Rate</code> <code>rate</code> () const<br />
 <i>accrued rate </i><br />
 <code>Real</code> <code>price</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountingCurve) const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>day counter for accrual calculation </i><br />
 <code>Real</code> <code>accruedAmount</code> (const <code>Date</code> &amp;) const<br />
 <i>accrued amount at the given date </i> <code>Inspectors</code><br />
 void update () <code>Observer interface</code> </p>
<pre><code>void update ()</code></pre>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>convexityAdjustmentImpl</code> (<code>Rate</code> fixing) const<br />
 <i>convexity adjustment for the given index fixing </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; <code>index_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<p> <code>Natural</code> <code>fixingDays_</code> </p>
<p> <code>Real</code> <code>gearing_</code> </p>
<p> <code>Spread</code> <code>spread_</code> </p>
<p> bool <code>isInArrears_</code> </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; <code>pricer_</code></p>
<h2>Detailed Description</h2>
<p>base floating-rate coupon class</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> amount () const [virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>CashFlow</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>CappedFlooredCoupon</code>, and <code>DigitalCoupon</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
