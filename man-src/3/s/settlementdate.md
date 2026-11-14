---
title: "settlementdate(3)"
name: "settlementdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-settlementdate/"
description: "QuantLib::AssetSwap::arguments – Arguments for asset swap calculation"
---

<p>QuantLib::AssetSwap::arguments &#8211; Arguments for asset swap calculation </p>
<h2>Synopsis</h2>
<pre><code>void validate () const



Public Attributes</code></pre>
<p> Inherits QuantLib::Swap::arguments.</p>
<h3>Public Member Functions</h3>
<pre><code>void validate () const



Public Attributes</code></pre>
<p> Real <code>nominal</code> </p>
<p> <code>Date</code> <code>settlementDate</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixedResetDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixedPayDates</code> </p>
<p> std::vector&lt; Real &gt; <code>fixedCoupons</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>floatingAccrualTimes</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingResetDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingFixingDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingPayDates</code> </p>
<p> std::vector&lt; <code>Spread</code> &gt; <code>floatingSpreads</code> </p>
<p> <code>Rate</code> <code>currentFloatingCoupon</code></p>
<h2>Detailed Description</h2>
<p>Arguments for asset swap calculation</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
