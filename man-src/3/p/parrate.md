---
title: "parrate(3)"
name: "parrate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parrate/"
description: "QuantLib::YieldTermStructure – Interest-rate term structure."
---

<p>QuantLib::YieldTermStructure &#8211; Interest-rate term structure. </p>
<h2>Synopsis</h2>
<pre><code>virtual DiscountFactor discountImpl (Time) const =0


discount calculation</code></pre>
<p> Inherits <code>QuantLib::TermStructure</code>. Inherited by <code>InterpolatedDiscountCurve&lt; LogLinear &gt;</code>, <code>FittedBondDiscountCurve</code>, <code>FlatForward</code>, <code>ForwardRateStructure</code>, <code>ImpliedTermStructure</code>, <code>InterpolatedDiscountCurve&lt; Interpolator &gt;</code>, and <code>ZeroYieldStructure</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. virtual DiscountFactor discountImpl (Time) const =0</p>
<p>discount calculation <code>zero-yield rates</code><br />
 These methods return the implied zero-yield rate for a given date or time. In the former case, the time is calculated as a fraction of year from the reference date. virtual DiscountFactor discountImpl (Time) const =0</p>
<p>discount calculation <code>discount factors</code><br />
 These methods return the discount factor for a given date or time. In the former case, the time is calculated as a fraction of year from the reference date. virtual DiscountFactor discountImpl (Time) const =0</p>
<p>discount calculation <code>forward rates</code><br />
 These methods returns the implied forward interest rate between two dates or times. In the former case, times are calculated as fractions of year from the reference date. virtual DiscountFactor discountImpl (Time) const =0</p>
<p>discount calculation <code>par rates</code><br />
 These methods returns the implied par rate for a given sequence of payments at the given dates or times. In the former case, times are calculated as fractions of year from the reference date. <code>Warning</code></p>
<dl>
<dd>though somewhat related to a swap rate, this method is not to be used for the fair rate of a real swap, since it does not take into account all the market conventions&#8217; details. The correct way to evaluate such rate is to instantiate a SimpleSwap with the correct conventions, pass it the term structure and call the swap&#8217;s fairRate() method.</dl>
<p> virtual DiscountFactor discountImpl (Time) const =0</p>
<p>discount calculation <code>Calculations</code><br />
 These methods must be implemented in derived classes to perform the actual discount and rate calculations. When they are called, range check has already been performed; therefore, they must assume that extrapolation is required. </p>
<pre><code>virtual DiscountFactor discountImpl (Time) const =0


discount calculation</code></pre>
<h2>Detailed Description</h2>
<p>Interest-rate term structure. </p>
<p> This abstract class defines the interface of concrete rate structures which will be derived from this one. </p>
<p> Rates are assumed to be annual continuous compounding. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add derived class ParSwapTermStructure similar to ZeroYieldTermStructure, DiscountStructure, <code>ForwardRateStructure</code></dl>
<p> <code>Tests</code></p>
<dl>
<dd>observability against evaluation date changes is checked.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>YieldTermStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3><code>InterestRate</code> zeroRate (const <code>Date</code> &amp; d, const <code>DayCounter</code> &amp; resultDayCounter, Compounding comp, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>The resulting interest rate has the required daycounting rule.</p>
<h3><code>InterestRate</code> zeroRate (Time t, Compounding comp, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>The resulting interest rate has the same day-counting rule used by the term structure. The same rule should be used for calculating the passed time t.</p>
<h3><code>DiscountFactor</code> discount (Time t, bool extrapolate = false) const</h3>
<p>The same day-counting rule used by the term structure should be used for calculating the passed time t.</p>
<h3><code>InterestRate</code> forwardRate (const <code>Date</code> &amp; d1, const <code>Date</code> &amp; d2, const <code>DayCounter</code> &amp; resultDayCounter, Compounding comp, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>The resulting interest rate has the required day-counting rule.</p>
<h3><code>InterestRate</code> forwardRate (const <code>Date</code> &amp; d, const <code>Period</code> &amp; p, const <code>DayCounter</code> &amp; resultDayCounter, Compounding comp, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>The resulting interest rate has the required day-counting rule. </p>
<p> <code>Warning</code></p>
<dl>
<dd>dates are not adjusted for holidays</dl>
<h3><code>InterestRate</code> forwardRate (Time t1, Time t2, Compounding comp, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>The resulting interest rate has the same day-counting rule used by the term structure. The same rule should be used for the calculating the passed times t1 and t2.</p>
<h3><code>Rate</code> parRate (const std::vector&lt; <code>Date</code> &gt; &amp; dates, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>the first date in the vector must equal the start date; the following dates must equal the payment dates.</p>
<h3><code>Rate</code> parRate (const std::vector&lt; Time &gt; &amp; times, <code>Frequency</code> freq = Annual, bool extrapolate = false) const</h3>
<p>the first time in the vector must equal the start time; the following times must equal the payment times.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
