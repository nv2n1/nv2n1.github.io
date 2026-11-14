---
title: "interestrate(3)"
name: "interestrate"
section: "3"
letter: "i"
url: "/docs/linux/man/3-interestrate/"
description: "QuantLib::FixedRateCoupon – Coupon paying a fixed interest rate"
---

<p>QuantLib::FixedRateCoupon &#8211; Coupon paying a fixed interest rate </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/fixedratecoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::Coupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>constructors</code> </p>
<p> <code>FixedRateCoupon</code> (<code>Real</code> nominal, const <code>Date</code> &amp;paymentDate, <code>Rate</code> rate, const <code>DayCounter</code> &amp;dayCounter, const <code>Date</code> &amp;accrualStartDate, const <code>Date</code> &amp;accrualEndDate, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>()) </p>
<p> <code>FixedRateCoupon</code> (<code>Real</code> nominal, const <code>Date</code> &amp;paymentDate, const <code>InterestRate</code> &amp;interestRate, const <code>DayCounter</code> &amp;dayCounter, const <code>Date</code> &amp;accrualStartDate, const <code>Date</code> &amp;accrualEndDate, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>()) </p>
<p> <code>CashFlow interface</code> </p>
<p> <code>Real</code> <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i> </p>
<p> <code>Coupon interface</code> </p>
<p> <code>Rate</code> <code>rate</code> () const<br />
 <i>accrued rate </i><br />
 <code>InterestRate</code> <code>interestRate</code> () const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>day counter for accrual calculation </i><br />
 <code>Real</code> <code>accruedAmount</code> (const <code>Date</code> &amp;) const<br />
 <i>accrued amount at the given date </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Coupon paying a fixed interest rate</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> amount () const [virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>CashFlow</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
