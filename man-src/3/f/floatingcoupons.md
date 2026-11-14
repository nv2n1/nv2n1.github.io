---
title: "floatingcoupons(3)"
name: "floatingcoupons"
section: "3"
letter: "f"
url: "/docs/linux/man/3-floatingcoupons/"
description: "QuantLib::VanillaSwap::arguments – Arguments for simple swap calculation"
---

<p>QuantLib::VanillaSwap::arguments &#8211; Arguments for simple swap calculation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/vanillaswap.hpp&gt; </p>
<p> Inherits QuantLib::Swap::arguments. </p>
<p> Inherited by <code>arguments</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>validate</code> () const </p>
<h3>Public Attributes</h3>
<p>Type <code>type</code> </p>
<p> <code>Real</code> <code>nominal</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixedResetDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixedPayDates</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>floatingAccrualTimes</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingResetDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingFixingDates</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>floatingPayDates</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>fixedCoupons</code> </p>
<p> std::vector&lt; <code>Spread</code> &gt; <code>floatingSpreads</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>floatingCoupons</code> </p>
<h2>Detailed Description</h2>
<p>Arguments for simple swap calculation </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
