---
title: "compoundforwardimpl(3)"
name: "compoundforwardimpl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-compoundforwardimpl/"
description: "QuantLib::CompoundForward – compound-forward structure"
---

<p>QuantLib::CompoundForward &#8211; compound-forward structure </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/termstructures/compoundforward.hpp&gt; </p>
<p> Inherits <code>QuantLib::ForwardRateStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CompoundForward</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Rate</code> &gt; &amp;forwards, const <code>Calendar</code> &amp;calendar, const <code>BusinessDayConvention</code> conv, const Integer compounding, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> Integer <code>compounding</code> () const </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>forwards</code> () const </p>
<p> boost::shared_ptr&lt; <code>ExtendedDiscountCurve</code> &gt; <code>discountCurve</code> () const </p>
<p> <code>Rate</code> <code>compoundForward</code> (const <code>Date</code> &amp;d1, Integer f, bool extrapolate=false) const </p>
<p> <code>Rate</code> <code>compoundForward</code> (Time t1, Integer f, bool extrapolate=false) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>calibrateNodes</code> () const </p>
<p> boost::shared_ptr&lt; <code>YieldTermStructure</code> &gt; <code>bootstrap</code> () const </p>
<p> <code>Rate</code> <code>zeroYieldImpl</code> (Time) const </p>
<p> <code>DiscountFactor</code> <code>discountImpl</code> (Time) const </p>
<p> Size <code>referenceNode</code> (Time) const </p>
<p> <code>Rate</code> <code>forwardImpl</code> (Time) const<br />
 <i>instantaneous forward-rate calculation </i><br />
 <code>Rate</code> <code>compoundForwardImpl</code> (Time, Integer) const </p>
<h2>Detailed Description</h2>
<p>compound-forward structure </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the curve is tested by reproducing the input data.</p>
<dt>*</p>
<dd>the correctness of the curve is tested by checking the consistency between returned rates and swaps priced on the curve.</dl>
</dl>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>swap rates are not reproduced exactly when using indexed coupons. Apparently, some assumption about the swap fixings is hard-coded into the bootstrapping algorithm.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> zeroYieldImpl (Time t) const [protected, virtual]</h3>
<p>Returns the zero yield rate for the given date calculating it from the instantaneous forward rate. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is just a default, highly inefficient and possibly wildly inaccurate implementation. Derived classes should implement their own zeroYield method.</dl>
<p> Reimplemented from <code>ForwardRateStructure</code>.</p>
<h3><code>DiscountFactor</code> discountImpl (Time t) const [protected, virtual]</h3>
<p>Returns the discount factor for the given date calculating it from the instantaneous forward rate. </p>
<p> Reimplemented from <code>ForwardRateStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
