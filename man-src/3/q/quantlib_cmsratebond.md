---
title: "quantlib_cmsratebond(3)"
name: "quantlib_cmsratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cmsratebond/"
description: "QuantLib::CmsRateBond – CMS-rate bond."
---

<p>QuantLib::CmsRateBond &#8211; CMS-rate bond. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/cmsratebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CmsRateBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;index, const <code>DayCounter</code> &amp;paymentDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Natural</code> fixingDays=<code>Null</code>&lt; <code>Natural</code> &gt;(), const std::vector&lt; <code>Real</code> &gt; &amp;gearings=std::vector&lt; <code>Real</code> &gt;(1, 1.0), const std::vector&lt; <code>Spread</code> &gt; &amp;spreads=std::vector&lt; <code>Spread</code> &gt;(1, 0.0), const std::vector&lt; <code>Rate</code> &gt; &amp;caps=std::vector&lt; <code>Rate</code> &gt;(), const std::vector&lt; <code>Rate</code> &gt; &amp;floors=std::vector&lt; <code>Rate</code> &gt;(), bool inArrears=false, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<h2>Detailed Description</h2>
<p>CMS-rate bond. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are tested by checking results against cached values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
