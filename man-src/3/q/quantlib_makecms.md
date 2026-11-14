---
title: "quantlib_makecms(3)"
name: "quantlib_makecms"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makecms/"
description: "QuantLib::MakeCms – helper class for instantiating CMS"
---

<p>QuantLib::MakeCms &#8211; helper class for instantiating CMS </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/makecms.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeCms</code> (const <code>Period</code> &amp;swapTenor, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, <code>Spread</code> iborSpread=0.0, const <code>Period</code> &amp;forwardStart=0 *Days) </p>
<p> <code>MakeCms</code> (const <code>Period</code> &amp;swapTenor, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, <code>Spread</code> iborSpread=0.0, const <code>Period</code> &amp;forwardStart=0 *Days) </p>
<p> <code>operator Swap</code> () const </p>
<p> <code>operator boost::shared_ptr&lt; Swap &gt;</code> () const </p>
<p> <code>MakeCms</code> &amp; <code>receiveCms</code> (bool flag=true) </p>
<p> <code>MakeCms</code> &amp; <code>withNominal</code> (<code>Real</code> n) </p>
<p> <code>MakeCms</code> &amp; <code>withEffectiveDate</code> (const <code>Date</code> &amp;) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegTenor</code> (const <code>Period</code> &amp;t) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegCalendar</code> (const <code>Calendar</code> &amp;cal) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegTerminationDateConvention</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegEndOfMonth</code> (bool flag=true) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsLegDayCount</code> (const <code>DayCounter</code> &amp;dc) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegTenor</code> (const <code>Period</code> &amp;t) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegCalendar</code> (const <code>Calendar</code> &amp;cal) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegTerminationDateConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegEndOfMonth</code> (bool flag=true) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCms</code> &amp; <code>withFloatingLegDayCount</code> (const <code>DayCounter</code> &amp;dc) </p>
<p> <code>MakeCms</code> &amp; <code>withAtmSpread</code> (bool flag=true) </p>
<p> <code>MakeCms</code> &amp; <code>withDiscountingTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountingTermStructure) </p>
<p> <code>MakeCms</code> &amp; <code>withCmsCouponPricer</code> (const boost::shared_ptr&lt; <code>CmsCouponPricer</code> &gt; &amp;couponPricer) </p>
<h2>Detailed Description</h2>
<p>helper class for instantiating CMS </p>
<p> This class provides a more comfortable way to instantiate standard market constant maturity swap. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
