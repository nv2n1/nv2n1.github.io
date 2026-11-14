---
title: "quantlib_zerocouponbond(3)"
name: "quantlib_zerocouponbond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zerocouponbond/"
description: "QuantLib::ZeroCouponBond – zero-coupon bond"
---

<p>QuantLib::ZeroCouponBond &#8211; zero-coupon bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/zerocouponbond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ZeroCouponBond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp;maturityDate, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<h2>Detailed Description</h2>
<p>zero-coupon bond </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are tested by checking results against cached values.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
