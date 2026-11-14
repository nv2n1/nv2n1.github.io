---
title: "quantlib_convertiblefloatingratebond(3)"
name: "quantlib_convertiblefloatingratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_convertiblefloatingratebond/"
description: "QuantLib::ConvertibleFloatingRateBond – convertible floating-rate bond"
---

<p>QuantLib::ConvertibleFloatingRateBond &#8211; convertible floating-rate bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/convertiblebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::ConvertibleBond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ConvertibleFloatingRateBond</code> (const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise, <code>Real</code> conversionRatio, const DividendSchedule &amp;dividends, const CallabilitySchedule &amp;callability, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;creditSpread, const <code>Date</code> &amp;issueDate, <code>Natural</code> settlementDays, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, <code>Natural</code> fixingDays, const std::vector&lt; <code>Spread</code> &gt; &amp;spreads, const <code>DayCounter</code> &amp;dayCounter, const <code>Schedule</code> &amp;schedule, <code>Real</code> redemption=100) </p>
<h2>Detailed Description</h2>
<p>convertible floating-rate bond </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Most methods inherited from <code>Bond</code> (such as yield or the yield-based dirtyPrice and cleanPrice) refer to the underlying plain-vanilla bond and do not take convertibility and callability into account.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
