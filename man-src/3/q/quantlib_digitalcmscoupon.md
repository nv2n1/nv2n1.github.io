---
title: "quantlib_digitalcmscoupon(3)"
name: "quantlib_digitalcmscoupon"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_digitalcmscoupon/"
description: "QuantLib::DigitalCmsCoupon – Cms-rate coupon with digital digital call/put option."
---

<p>QuantLib::DigitalCmsCoupon &#8211; Cms-rate coupon with digital digital call/put option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/digitalcmscoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::DigitalCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DigitalCmsCoupon</code> (const boost::shared_ptr&lt; <code>CmsCoupon</code> &gt; &amp;underlying, <code>Rate</code> callStrike=<code>Null</code>&lt; <code>Rate</code> &gt;(), Position::Type callPosition=Position::Long, bool isCallATMIncluded=false, <code>Rate</code> callDigitalPayoff=<code>Null</code>&lt; <code>Rate</code> &gt;(), <code>Rate</code> putStrike=<code>Null</code>&lt; <code>Rate</code> &gt;(), Position::Type putPosition=Position::Long, bool isPutATMIncluded=false, <code>Rate</code> putDigitalPayoff=<code>Null</code>&lt; <code>Rate</code> &gt;(), const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication=boost::shared_ptr&lt; DigitalReplication &gt;()) </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Cms-rate coupon with digital digital call/put option. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
