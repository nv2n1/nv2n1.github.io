---
title: "fairliborfraction(3)"
name: "fairliborfraction"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fairliborfraction/"
description: "QuantLib::BMASwap – swap paying Libor against BMA coupons"
---

<p>QuantLib::BMASwap &#8211; swap paying <code>Libor</code> against BMA coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bmaswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Swap</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Receiver</code> = -1, <code>Payer</code> = 1 } </p>
<h3>Public Member Functions</h3>
<p><code>BMASwap</code> (Type type, <code>Real</code> nominal, const <code>Schedule</code> &amp;liborSchedule, <code>Rate</code> liborFraction, <code>Rate</code> liborSpread, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;liborIndex, const <code>DayCounter</code> &amp;liborDayCount, const <code>Schedule</code> &amp;bmaSchedule, const boost::shared_ptr&lt; <code>BMAIndex</code> &gt; &amp;bmaIndex, const <code>DayCounter</code> &amp;bmaDayCount) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>liborFraction</code> () const </p>
<p> <code>Spread</code> <code>liborSpread</code> () const </p>
<p> <code>Real</code> <code>nominal</code> () const </p>
<p> Type <code>type</code> () const<br />
 <i>&#8216;payer&#8217; or &#8216;receiver&#8217; refer to the BMA leg </i><br />
 const Leg &amp; <code>bmaLeg</code> () const </p>
<p> const Leg &amp; <code>liborLeg</code> () const </p>
<p> <code>Results</code> </p>
<p> <code>Real</code> <code>liborLegBPS</code> () const </p>
<p> <code>Real</code> <code>liborLegNPV</code> () const </p>
<p> <code>Rate</code> <code>fairLiborFraction</code> () const </p>
<p> <code>Spread</code> <code>fairLiborSpread</code> () const </p>
<p> <code>Real</code> <code>bmaLegBPS</code> () const </p>
<p> <code>Real</code> <code>bmaLegNPV</code> () const </p>
<h2>Detailed Description</h2>
<p>swap paying <code>Libor</code> against BMA coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
