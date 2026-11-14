---
title: "quantlib_zerocouponinflationswap(3)"
name: "quantlib_zerocouponinflationswap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zerocouponinflationswap/"
description: "QuantLib::ZeroCouponInflationSwap – Zero-coupon inflation-indexed swap."
---

<p>QuantLib::ZeroCouponInflationSwap &#8211; Zero-coupon inflation-indexed swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/zerocouponinflationswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::InflationSwap</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ZeroCouponInflationSwap</code> (const <code>Date</code> &amp;start, const <code>Date</code> &amp;maturity, const <code>Period</code> &amp;lag, <code>Rate</code> fixedRate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, const <code>DayCounter</code> &amp;dayCounter, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS, const <code>Handle</code>&lt; <code>ZeroInflationTermStructure</code> &gt; &amp;inflationTS) </p>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> </p>
<p> <code>InflationSwap interface</code> </p>
<p> <code>Rate</code> <code>fairRate</code> () const<br />
 <i>the rate $ ilde{K} $ such that NPV = 0. </i> </p>
<p> <code>Inspectors</code> </p>
<p> <code>Rate</code> <code>fixedRate</code> () const<br />
 <i>$ K $ in the above formula. </i></p>
<h3>Protected Member Functions</h3>
<p><code>Instrument interface</code> </p>
<p> void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Rate</code> <code>fixedRate_</code> </p>
<p> <code>Handle</code>&lt; <code>ZeroInflationTermStructure</code> &gt; <code>inflationTS_</code> </p>
<h2>Detailed Description</h2>
<p>Zero-coupon inflation-indexed swap. </p>
<p> Quoted as a fixed rate $ K $. At start: [ P_n(0,T) N [(1+K)^{T}-1] = P_n(0,T) N </p>
<hr>
<p>re $ T $ is the maturity time, $ P_n(0,t) $ is the nominal discount factor at time $ t $, $ N $ is the notional, and $ I(t) $ is the inflation index value at time $ t $.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
