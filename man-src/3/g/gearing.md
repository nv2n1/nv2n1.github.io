---
title: "gearing(3)"
name: "gearing"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gearing/"
description: "QuantLib::FloatingRateCoupon – base floating-rate coupon class"
---

<h2 class="name">NAME</h2>
<p> QuantLib::FloatingRateCoupon &#8211; base floating-rate coupon class </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/cashflows/floatingratecoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::Coupon</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by <code>AverageBMACoupon</code>, <code>CappedFlooredCoupon</code>, <code>CmsCoupon</code>, <code>DigitalCoupon</code>, <code>IborCoupon</code>, RangeAccrualFloatersCoupon, and SubPeriodsCoupon. </p>
<h3>Public Member Functions</h3>
<p> <code>FloatingRateCoupon</code> (const <code>Date</code> &amp;paymentDate, const <code>Real</code> nominal, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const <code>Natural</code> fixingDays, const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;index, const <code>Real</code> gearing=1.0, const <code>Spread</code> spread=0.0, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>(), bool isInArrears=false) </p>
<p> void <code>setPricer</code> (const boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; &amp;) </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; <code>pricer</code> () const </p>
<p> <code>CashFlow interface</code> </p>
<p> <code>Real</code> <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i> </p>
<p> <code>Coupon interface</code> </p>
<p> <code>Rate</code> <code>rate</code> () const<br />
 <i>accrued rate </i><br />
 <code>Real</code> <code>price</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountingCurve) const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>day counter for accrual calculation </i><br />
 <code>Real</code> <code>accruedAmount</code> (const <code>Date</code> &amp;) const<br />
 <i>accrued amount at the given date </i> </p>
<p> <code>Inspectors</code> </p>
<p> const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp; <code>index</code> () const<br />
 <i>floating index </i><br />
 <code>Natural</code> <code>fixingDays</code> () const<br />
 <i>fixing days </i><br />
 virtual <code>Date</code> <code>fixingDate</code> () const<br />
 <i>fixing date </i><br />
 <code>Real</code> <code>gearing</code> () const<br />
 <i>index gearing, i.e. multiplicative coefficient for the index </i><br />
 <code>Spread</code> <code>spread</code> () const<br />
 <i>spread paid over the fixing of the underlying index </i><br />
 virtual <code>Rate</code> <code>indexFixing</code> () const<br />
 <i>fixing of the underlying index </i><br />
 virtual <code>Rate</code> <code>convexityAdjustment</code> () const<br />
 <i>convexity adjustment </i><br />
 virtual <code>Rate</code> <code>adjustedFixing</code> () const<br />
 <i>convexity-adjusted fixing </i><br />
 bool <code>isInArrears</code> () const<br />
 <i>whether or not the coupon fixes in arrears </i> </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p> <code>Rate</code> <code>convexityAdjustmentImpl</code> (<code>Rate</code> fixing) const<br />
 <i>convexity adjustment for the given index fixing </i></p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; <code>index_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<p> <code>Natural</code> <code>fixingDays_</code> </p>
<p> <code>Real</code> <code>gearing_</code> </p>
<p> <code>Spread</code> <code>spread_</code> </p>
<p> bool <code>isInArrears_</code> </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCouponPricer</code> &gt; <code>pricer_</code> </p>
<h2>Detailed Description</h2>
<p> base floating-rate coupon class</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> amount () const [virtual]</h3>
<p> returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>CashFlow</code>.</p>
<h3>void update () [virtual]</h3>
<p> This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>CappedFlooredCoupon</code>, and <code>DigitalCoupon</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
