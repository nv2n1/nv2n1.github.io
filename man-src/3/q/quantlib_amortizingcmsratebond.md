---
title: "quantlib_amortizingcmsratebond(3)"
name: "quantlib_amortizingcmsratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_amortizingcmsratebond/"
description: "QuantLib::AmortizingCmsRateBond – amortizing CMS-rate bond"
---

<p>QuantLib::AmortizingCmsRateBond &#8211; amortizing CMS-rate bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/amortizingbonds/amortizingcmsratebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AmortizingCmsRateBond</code> (<code>Natural</code> settlementDays, const std::vector&lt; <code>Real</code> &gt; &amp;faceAmount, const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;index, const <code>DayCounter</code> &amp;paymentDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Natural</code> fixingDays=<code>Null</code>&lt; <code>Natural</code> &gt;(), const std::vector&lt; <code>Real</code> &gt; &amp;gearings=std::vector&lt; <code>Real</code> &gt;(1, 1.0), const std::vector&lt; <code>Spread</code> &gt; &amp;spreads=std::vector&lt; <code>Spread</code> &gt;(1, 0.0), const std::vector&lt; <code>Rate</code> &gt; &amp;caps=std::vector&lt; <code>Rate</code> &gt;(), const std::vector&lt; <code>Rate</code> &gt; &amp;floors=std::vector&lt; <code>Rate</code> &gt;(), bool inArrears=false, const std::vector&lt; <code>Real</code> &gt; &amp;redemptions=std::vector&lt; <code>Real</code> &gt;(1, 100.0), const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<h2>Detailed Description</h2>
<p>amortizing CMS-rate bond </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
