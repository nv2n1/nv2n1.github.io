---
title: "paymentdates(3)"
name: "paymentdates"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paymentdates/"
description: "QuantLib::YearOnYearInflationSwap – Year-on-year inflation-indexed swap."
---

<p>QuantLib::YearOnYearInflationSwap &#8211; Year-on-year inflation-indexed swap. </p>
<h2>Synopsis</h2>
<pre><code>void setupExpired () const



void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::InflationSwap</code>.</p>
<h3>Public Member Functions</h3>
<p>void setupExpired () const</p>
<p>void performCalculations () const</p>
<p>Protected Attributes <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> <code>InflationSwap interface</code><br />
 void setupExpired () const</p>
<p>void performCalculations () const</p>
<p>Protected Attributes <code>Inspectors</code> </p>
<p> <code>Rate</code> <code>fixedRate</code> () const<br />
 <i>$ K $ in the above formula. </i><br />
 std::vector&lt; <code>Date</code> &gt; <code>paymentDates</code> () const</p>
<h3>Protected Member Functions</h3>
<p><code>Instrument interface</code> </p>
<pre><code>void setupExpired () const



void performCalculations () const



Protected Attributes</code></pre>
<p> <code>Rate</code> <code>fixedRate_</code> </p>
<p> <code>Handle</code>&lt; <code>YoYInflationTermStructure</code> &gt; <code>inflationTS_</code> </p>
<p> bool <code>allowAmbiguousPayments_</code> </p>
<p> <code>Period</code> <code>ambiguousPaymentPeriod_</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>paymentDates_</code> </p>
<p> <code>Rate</code> <code>fairRate_</code></p>
<h2>Detailed Description</h2>
<p>Year-on-year inflation-indexed swap. </p>
<p> Quoted as a fixed rate $ K $. At start: [ um_{i=1}^{M} P_n(0,t_i) N K = um_{i=1}^{M} P_n(0,t_i) N </p>
<hr>
<p>re $ t_M $ is the maturity time, $ P_n(0,t) $ is the nominal discount factor at time $ t $, $ N $ is the notional, and $ I(t) $ is the inflation index value at time $ t $. </p>
<p> <code>Note:</code></p>
<dl>
<dd>The allowAmbiguousPayments parameter is to allow for payment arithmetic being ambiguous. If the maturity is in, say, 30.01 years according to the day-counter and roll rules, does this mean that there is a payment in 0.01 years? If allowAmbiguousPayments is false, the ambiguousPaymentPeriod parameter sets the period within which the answer is no.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
