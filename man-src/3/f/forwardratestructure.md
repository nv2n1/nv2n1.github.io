---
title: "forwardratestructure(3)"
name: "forwardratestructure"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardratestructure/"
description: "QuantLib::ForwardRateStructure – Forward-rate term structure"
---

<p>QuantLib::ForwardRateStructure &#8211; Forward-rate term structure </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/forwardstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::YieldTermStructure</code>. </p>
<p> Inherited by <code>CompoundForward</code>, <code>ForwardSpreadedTermStructure</code>, and <code>InterpolatedForwardCurve&lt; Interpolator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>ForwardRateStructure</code> (const <code>DayCounter</code> &amp;dayCounter=<code>Actual365Fixed</code>()) </p>
<p> <code>ForwardRateStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>Actual365Fixed</code>()) </p>
<p> <code>ForwardRateStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;dayCounter=<code>Actual365Fixed</code>()) </p>
<h3>Protected Member Functions</h3>
<p><code>YieldTermStructure implementation</code> </p>
<p> <code>DiscountFactor</code> <code>discountImpl</code> (Time) const </p>
<p> virtual <code>Rate</code> <code>forwardImpl</code> (Time) const =0<br />
 <i>instantaneous forward-rate calculation </i><br />
 virtual <code>Rate</code> <code>zeroYieldImpl</code> (Time) const </p>
<h2>Detailed Description</h2>
<p>Forward-rate term structure </p>
<p> This abstract class acts as an adapter to <code>TermStructure</code> allowing the programmer to implement only the forwardImpl(const Date&amp;, bool) method in derived classes. Zero yields and discounts are calculated from forwards. </p>
<p> Rates are assumed to be annual continuous compounding.</p>
<h2>Member Function Documentation</h2>
<h3><code>DiscountFactor</code> discountImpl (Time t) const [protected, virtual]</h3>
<p>Returns the discount factor for the given date calculating it from the instantaneous forward rate. </p>
<p> Implements <code>YieldTermStructure</code>. </p>
<p> Reimplemented in <code>CompoundForward</code>.</p>
<h3><code>Rate</code> zeroYieldImpl (Time t) const [protected, virtual]</h3>
<p>Returns the zero yield rate for the given date calculating it from the instantaneous forward rate. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is just a default, highly inefficient and possibly wildly inaccurate implementation. Derived classes should implement their own zeroYield method.</dl>
<p> Reimplemented in <code>CompoundForward</code>, <code>InterpolatedForwardCurve&lt; Interpolator &gt;</code>, and <code>ForwardSpreadedTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
