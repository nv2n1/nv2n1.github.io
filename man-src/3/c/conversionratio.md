---
title: "conversionratio(3)"
name: "conversionratio"
section: "3"
letter: "c"
url: "/docs/linux/man/3-conversionratio/"
description: "QuantLib::ConvertibleBond – base class for convertible bonds"
---

<p>QuantLib::ConvertibleBond &#8211; base class for convertible bonds </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/convertiblebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<p> Inherited by <code>ConvertibleFixedCouponBond</code>, <code>ConvertibleFloatingRateBond</code>, and <code>ConvertibleZeroCouponBond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Real</code> <code>conversionRatio</code> () const </p>
<p> const DividendSchedule &amp; <code>dividends</code> () const </p>
<p> const CallabilitySchedule &amp; <code>callability</code> () const </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>creditSpread</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>ConvertibleBond</code> (const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise, <code>Real</code> conversionRatio, const DividendSchedule &amp;dividends, const CallabilitySchedule &amp;callability, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;creditSpread, const <code>Date</code> &amp;issueDate, <code>Natural</code> settlementDays, const <code>DayCounter</code> &amp;dayCounter, const <code>Schedule</code> &amp;schedule, <code>Real</code> redemption) </p>
<p> void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>conversionRatio_</code> </p>
<p> CallabilitySchedule <code>callability_</code> </p>
<p> DividendSchedule <code>dividends_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>creditSpread_</code> </p>
<p> boost::shared_ptr&lt; option &gt; <code>option_</code> </p>
<h2>Detailed Description</h2>
<p>base class for convertible bonds</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
