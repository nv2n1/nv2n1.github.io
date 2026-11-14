---
title: "refperiodend_(3)"
name: "refperiodend_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-refperiodend_/"
description: "QuantLib::Coupon – coupon accruing over a fixed period"
---

<p>QuantLib::Coupon &#8211; coupon accruing over a fixed period </p>
<h2>Synopsis</h2>
<pre><code>Real nominal () const



const Date &amp; accrualStartDate () const


start of the accrual period


const Date &amp; accrualEndDate () const


end of the accrual period


const Date &amp; referencePeriodStart () const


start date of the reference period


const Date &amp; referencePeriodEnd () const


end date of the reference period


Time accrualPeriod () const


accrual period as fraction of year


Integer accrualDays () const


accrual period in days


virtual Rate rate () const =0


accrued rate


virtual DayCounter dayCounter () const =0


day counter for accrual calculation


virtual Real accruedAmount (const Date &amp;) const =0


accrued amount at the given date</code></pre>
<p> Inherits <code>QuantLib::CashFlow</code>. Inherited by <code>FixedRateCoupon</code>, and <code>FloatingRateCoupon</code>.</p>
<h3>Public Member Functions</h3>
<p>Real nominal () const</p>
<p>const Date &amp; accrualStartDate () const</p>
<p>start of the accrual period</p>
<p>const Date &amp; accrualEndDate () const</p>
<p>end of the accrual period</p>
<p>const Date &amp; referencePeriodStart () const</p>
<p>start date of the reference period</p>
<p>const Date &amp; referencePeriodEnd () const</p>
<p>end date of the reference period</p>
<p>Time accrualPeriod () const</p>
<p>accrual period as fraction of year</p>
<p>Integer accrualDays () const</p>
<p>accrual period in days</p>
<p>virtual Rate rate () const =0</p>
<p>accrued rate</p>
<p>virtual DayCounter dayCounter () const =0</p>
<p>day counter for accrual calculation</p>
<p>virtual Real accruedAmount (const Date &amp;) const =0</p>
<p>accrued amount at the given date <code>Partial CashFlow interface</code> </p>
<p> <code>Date</code> <code>date</code> () const<br />
 <code>Inspectors</code> </p>
<pre><code>Real nominal () const



const Date &amp; accrualStartDate () const


start of the accrual period


const Date &amp; accrualEndDate () const


end of the accrual period


const Date &amp; referencePeriodStart () const


start date of the reference period


const Date &amp; referencePeriodEnd () const


end date of the reference period


Time accrualPeriod () const


accrual period as fraction of year


Integer accrualDays () const


accrual period in days


virtual Rate rate () const =0


accrued rate


virtual DayCounter dayCounter () const =0


day counter for accrual calculation


virtual Real accruedAmount (const Date &amp;) const =0


accrued amount at the given date</code></pre>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;)</p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>nominal_</code> </p>
<p> <code>Date</code> <code>paymentDate_</code> </p>
<p> <code>Date</code> <code>accrualStartDate_</code> </p>
<p> <code>Date</code> <code>accrualEndDate_</code> </p>
<p> <code>Date</code> <code>refPeriodStart_</code> </p>
<p> <code>Date</code> <code>refPeriodEnd_</code></p>
<h2>Detailed Description</h2>
<p>coupon accruing over a fixed period </p>
<p> This class implements part of the <code>CashFlow</code> interface but it is still abstract and provides derived classes with methods for accrual period calculations. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Coupon</code> (<code>Real</code> nominal, const <code>Date</code> &amp; paymentDate, const <code>Date</code> &amp; accrualStartDate, const <code>Date</code> &amp; accrualEndDate, const <code>Date</code> &amp; refPeriodStart = <code>Date</code>(), const <code>Date</code> &amp; refPeriodEnd = <code>Date</code>())</h3>
<p><code>Warning</code></p>
<dl>
<dd>the coupon does not adjust the payment date which must already be a business day.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> date () const [virtual]</h3>
<p><code>Note:</code></p>
<dl>
<dd>This is inheriited from the event class</dl>
<p> Implements <code>CashFlow</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
