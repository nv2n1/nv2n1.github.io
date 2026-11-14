---
title: "valuedate_(3)"
name: "valuedate_"
section: "3"
letter: "v"
url: "/docs/linux/man/3-valuedate_/"
description: "QuantLib::Forward – Abstract base forward class."
---

<p>QuantLib::Forward &#8211; Abstract base forward class. </p>
<h2>Synopsis</h2>
<pre><code>Forward (const DayCounter &amp;dayCounter, const Calendar &amp;calendar, BusinessDayConvention businessDayConvention, Natural settlementDays, const boost::shared_ptr&lt; Payoff &gt; &amp;payoff, const Date &amp;valueDate, const Date &amp;maturityDate, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve=Handle&lt; YieldTermStructure &gt;())



void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>. Inherited by <code>FixedRateBondForward</code>, and ForwardRateAgreement.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>Real</code> <code>spotValue</code> () const =0<br />
 <i>returns spot value/price of an underlying financial instrument </i><br />
 virtual <code>Real</code> <code>spotIncome</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;incomeDiscountCurve) const =0<br />
 <i>NPV of income/dividends/storage-costs etc. of underlying instrument. </i> <code>Inspectors</code> </p>
<p> virtual <code>Date</code> <code>settlementDate</code> () const </p>
<p> const <code>Calendar</code> &amp; <code>calendar</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>dayCounter</code> () const </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>discountCurve</code> () const<br />
 <i>term structure relevant to the contract (e.g. repo curve) </i><br />
 <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>incomeDiscountCurve</code> () const<br />
 <i>term structure that discounts the underlying&#8217;s income cash flows </i><br />
 bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> <code>Calculations</code> </p>
<p> virtual <code>Real</code> <code>forwardValue</code> () const<br />
 <i>forward value/price of underlying, discounting income/dividends </i><br />
 <code>InterestRate</code> <code>impliedYield</code> (<code>Real</code> underlyingSpotValue, <code>Real</code> forwardValue, <code>Date</code> settlementDate, Compounding compoundingConvention, <code>DayCounter</code> dayCounter)</p>
<h3>Protected Member Functions</h3>
<pre><code>Forward (const DayCounter &amp;dayCounter, const Calendar &amp;calendar, BusinessDayConvention businessDayConvention, Natural settlementDays, const boost::shared_ptr&lt; Payoff &gt; &amp;payoff, const Date &amp;valueDate, const Date &amp;maturityDate, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve=Handle&lt; YieldTermStructure &gt;())



void performCalculations () const



Protected Attributes</code></pre>
<p> <code>Real</code> <code>underlyingIncome_</code> </p>
<p> <code>Real</code> <code>underlyingSpotValue_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention_</code> </p>
<p> <code>Natural</code> <code>settlementDays_</code> </p>
<p> boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff_</code> </p>
<p> <code>Date</code> <code>valueDate_</code> </p>
<p> <code>Date</code> <code>maturityDate_</code><br />
 <i>maturityDate of the forward contract or delivery date of underlying </i><br />
 <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>discountCurve_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>incomeDiscountCurve_</code></p>
<h2>Detailed Description</h2>
<p>Abstract base forward class. </p>
<p> Derived classes must implement the virtual functions <code>spotValue()</code> (NPV or spot price) and <code>spotIncome()</code> associated with the specific relevant underlying (e.g. bond, stock, commodity, loan/deposit). These functions must be used to set the protected member variables underlyingSpotValue_ and underlyingIncome_ within <code>performCalculations()</code> in the derived class before the base-class implementation is called. </p>
<p> <code>spotIncome()</code> refers generically to the present value of coupons, dividends or storage costs. </p>
<p> discountCurve_ is the curve used to discount forward contract cash flows back to the evaluation day, as well as to obtain forward values for spot values/prices. </p>
<p> incomeDiscountCurve_, which for generality is not automatically set to the discountCurve_, is the curve used to discount future income/dividends/storage-costs etc back to the evaluation date. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>Add preconditions and tests</dl>
<p> <code>Warning</code></p>
<dl>
<dd>This class still needs to be rigorously tested</dl>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Real</code> forwardValue () const [virtual]</h3>
<p>forward value/price of underlying, discounting income/dividends </p>
<p> <code>Note:</code></p>
<dl>
<dd>if this is a bond forward price, is must be a dirty forward price.</dl>
<h3><code>InterestRate</code> impliedYield (<code>Real</code> underlyingSpotValue, <code>Real</code> forwardValue, <code>Date</code> settlementDate, Compounding compoundingConvention, <code>DayCounter</code> dayCounter)</h3>
<p>Simple yield calculation based on underlying spot and forward values, taking into account underlying income. When $ t&gt;0 $, call with: underlyingSpotValue=spotValue(t), forwardValue=strikePrice, to get current yield. For a repo, if $ t=0 $, impliedYield should reproduce the spot repo rate. For FRA&#8217;s, this should reproduce the relevant zero rate at the FRA&#8217;s maturityDate_;</p>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>FixedRateBondForward</code>.</p>
<h2>Member Data Documentation</h2>
<h3><code>Real</code> <code>underlyingIncome_</code> [mutable, protected]</h3>
<p>derived classes must set this, typically via <code>spotIncome()</code></p>
<h3><code>Real</code> <code>underlyingSpotValue_</code> [mutable, protected]</h3>
<p>derived classes must set this, typically via <code>spotValue()</code></p>
<h3><code>Date</code> <code>valueDate_</code> [protected]</h3>
<p>valueDate = settlement date (date the fwd contract starts accruing)</p>
<h3><code>Handle</code>&lt;<code>YieldTermStructure</code>&gt; <code>incomeDiscountCurve_</code> [protected]</h3>
<p>must set this in derived classes, based on particular underlying</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
