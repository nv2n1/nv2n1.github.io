---
title: "quantlib_iborcoupon(3)"
name: "quantlib_iborcoupon"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_iborcoupon/"
description: "QuantLib::IborCoupon – Coupon paying a Libor-type index"
---

<p>QuantLib::IborCoupon &#8211; Coupon paying a Libor-type index </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/iborcoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>IborCoupon</code> (const <code>Date</code> &amp;paymentDate, const <code>Real</code> nominal, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const <code>Natural</code> fixingDays, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const <code>Real</code> gearing=1.0, const <code>Spread</code> spread=0.0, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>(), bool isInArrears=false) </p>
<p> <code>Inspectors</code> </p>
<p> const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp; <code>iborIndex</code> () const </p>
<p> <code>Rate</code> <code>indexFixing</code> () const<br />
 <i>Implemented in order to manage the case of par coupon. </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Coupon paying a Libor-type index </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
