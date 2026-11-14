---
title: "quantlib_cmscoupon(3)"
name: "quantlib_cmscoupon"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cmscoupon/"
description: "QuantLib::CmsCoupon – CMS coupon class."
---

<p>QuantLib::CmsCoupon &#8211; CMS coupon class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/cmscoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CmsCoupon</code> (const <code>Date</code> &amp;paymentDate, const <code>Real</code> nominal, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const <code>Natural</code> fixingDays, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;index, const <code>Real</code> gearing=1.0, const <code>Spread</code> spread=0.0, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>(), bool isInArrears=false) </p>
<p> <code>Inspectors</code> </p>
<p> const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp; <code>swapIndex</code> () const </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>CMS coupon class. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This class does not perform any date adjustment, i.e., the start and end date passed upon construction should be already rolled to a business day.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
