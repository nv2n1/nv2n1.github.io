---
title: "daycounter(3)"
name: "daycounter"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daycounter/"
description: "QuantLib::Coupon – coupon accruing over a fixed period"
---

<p>QuantLib::Coupon &#8211; coupon accruing over a fixed period </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/coupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::CashFlow</code>. </p>
<p> Inherited by <code>FixedRateCoupon</code>, and <code>FloatingRateCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Coupon</code> (<code>Real</code> nominal, const <code>Date</code> &amp;paymentDate, const <code>Date</code> &amp;accrualStartDate, const <code>Date</code> &amp;accrualEndDate, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>()) </p>
<p> <code>Partial CashFlow interface</code> </p>
<p> <code>Date</code> <code>date</code> () const </p>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>nominal</code> () const </p>
<p> const <code>Date</code> &amp; <code>accrualStartDate</code> () const<br />
 <i>start of the accrual period </i><br />
 const <code>Date</code> &amp; <code>accrualEndDate</code> () const<br />
 <i>end of the accrual period </i><br />
 const <code>Date</code> &amp; <code>referencePeriodStart</code> () const<br />
 <i>start date of the reference period </i><br />
 const <code>Date</code> &amp; <code>referencePeriodEnd</code> () const<br />
 <i>end date of the reference period </i><br />
 <code>Time</code> <code>accrualPeriod</code> () const<br />
 <i>accrual period as fraction of year </i><br />
 <code>Integer</code> <code>accrualDays</code> () const<br />
 <i>accrual period in days </i><br />
 virtual <code>Rate</code> <code>rate</code> () const =0<br />
 <i>accrued rate </i><br />
 virtual <code>DayCounter</code> <code>dayCounter</code> () const =0<br />
 <i>day counter for accrual calculation </i><br />
 virtual <code>Real</code> <code>accruedAmount</code> (const <code>Date</code> &amp;) const =0<br />
 <i>accrued amount at the given date </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>nominal_</code> </p>
<p> <code>Date</code> <code>paymentDate_</code> </p>
<p> <code>Date</code> <code>accrualStartDate_</code> </p>
<p> <code>Date</code> <code>accrualEndDate_</code> </p>
<p> <code>Date</code> <code>refPeriodStart_</code> </p>
<p> <code>Date</code> <code>refPeriodEnd_</code> </p>
<h2>Detailed Description</h2>
<p>coupon accruing over a fixed period </p>
<p> This class implements part of the <code>CashFlow</code> interface but it is still abstract and provides derived classes with methods for accrual period calculations. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Coupon</code> (<code>Real</code> nominal, const <code>Date</code> &amp; paymentDate, const <code>Date</code> &amp; accrualStartDate, const <code>Date</code> &amp; accrualEndDate, const <code>Date</code> &amp; refPeriodStart = <code>Date</code>(), const <code>Date</code> &amp; refPeriodEnd = <code>Date</code>())</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>the coupon does not adjust the payment date which must already be a business day.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> date () const [virtual]</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>This is inheriited from the event class</dl>
<p> Implements <code>CashFlow</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
