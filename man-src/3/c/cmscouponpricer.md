---
title: "cmscouponpricer(3)"
name: "cmscouponpricer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmscouponpricer/"
description: "QuantLib::CmsCouponPricer – base pricer for vanilla CMS coupons"
---

<p>QuantLib::CmsCouponPricer &#8211; base pricer for vanilla CMS coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/couponpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::FloatingRateCouponPricer</code>. </p>
<p> Inherited by <code>HaganPricer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CmsCouponPricer</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;v=<code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt;()) </p>
<p> <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; <code>swaptionVolatility</code> () const </p>
<p> void <code>setSwaptionVolatility</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;v=<code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>base pricer for vanilla CMS coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
