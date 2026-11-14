---
title: "paymentconvention_(3)"
name: "paymentconvention_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paymentconvention_/"
description: "QuantLib::ZciisInflationHelper – Zero-coupon inflation-swap bootstrap helper."
---

<p>QuantLib::ZciisInflationHelper &#8211; Zero-coupon inflation-swap bootstrap helper. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/termstructures/inflation/inflationhelpers.hpp&gt;</code></pre>
<p> Inherits <code>BootstrapHelper&lt; ZeroInflationTermStructure &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ZciisInflationHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;quote, const <code>Period</code> &amp;lag, const <code>Date</code> &amp;maturity, <code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dayCounter, <code>Frequency</code> frequency) </p>
<p> void <code>setTermStructure</code> (<code>ZeroInflationTermStructure</code> *)<br />
 <i>sets the term structure to be used for pricing </i><br />
 <code>Real</code> <code>impliedQuote</code> () const</p>
<h3>Protected Attributes</h3>
<p><code>Period</code> <code>lag_</code> </p>
<p> <code>Date</code> <code>maturity_</code> </p>
<p> <code>Natural</code> <code>settlementDays_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> <code>BusinessDayConvention</code> <code>paymentConvention_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> boost::shared_ptr&lt; <code>ZeroCouponInflationSwap</code> &gt; <code>zciis_</code></p>
<h2>Detailed Description</h2>
<p>Zero-coupon inflation-swap bootstrap helper.</p>
<h2>Member Function Documentation</h2>
<h3>void setTermStructure (<code>ZeroInflationTermStructure</code> *) [virtual]</h3>
<p>sets the term structure to be used for pricing </p>
<p> <code>Warning</code></p>
<dl>
<dd>Being a pointer and not a shared_ptr, the term structure is not guaranteed to remain allocated for the whole life of the rate helper. It is responsibility of the programmer to ensure that the pointer remains valid. It is advised that this method is called only inside the term structure being bootstrapped, setting the pointer to <code>this</code>, i.e., the term structure itself.</dl>
<p> Reimplemented from <code>BootstrapHelper&lt; ZeroInflationTermStructure &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
