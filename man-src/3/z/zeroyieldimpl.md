---
title: "zeroyieldimpl(3)"
name: "zeroyieldimpl"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zeroyieldimpl/"
description: "QuantLib::CompoundForward – compound-forward structure"
---

<p>QuantLib::CompoundForward &#8211; compound-forward structure </p>
<h2>Synopsis</h2>
<pre><code>CompoundForward (const Date &amp;referenceDate, const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Rate &gt; &amp;forwards, const Calendar &amp;calendar, const BusinessDayConvention conv, const Integer compounding, const DayCounter &amp;dayCounter)



BusinessDayConvention businessDayConvention () const



Integer compounding () const



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Rate &gt; &amp; forwards () const



boost::shared_ptr&lt; ExtendedDiscountCurve &gt; discountCurve () const



Rate compoundForward (const Date &amp;d1, Integer f, bool extrapolate=false) const



Rate compoundForward (Time t1, Integer f, bool extrapolate=false) const



Protected Member Functions
void calibrateNodes () const



boost::shared_ptr&lt; YieldTermStructure &gt; bootstrap () const



Rate zeroYieldImpl (Time) const



DiscountFactor discountImpl (Time) const



Size referenceNode (Time) const



Rate forwardImpl (Time) const


instantaneous forward-rate calculation


Rate compoundForwardImpl (Time, Integer) const</code></pre>
<p> Inherits <code>QuantLib::ForwardRateStructure</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CompoundForward (const Date &amp;referenceDate, const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Rate &gt; &amp;forwards, const Calendar &amp;calendar, const BusinessDayConvention conv, const Integer compounding, const DayCounter &amp;dayCounter)



BusinessDayConvention businessDayConvention () const



Integer compounding () const



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Rate &gt; &amp; forwards () const



boost::shared_ptr&lt; ExtendedDiscountCurve &gt; discountCurve () const



Rate compoundForward (const Date &amp;d1, Integer f, bool extrapolate=false) const



Rate compoundForward (Time t1, Integer f, bool extrapolate=false) const



Protected Member Functions
void calibrateNodes () const



boost::shared_ptr&lt; YieldTermStructure &gt; bootstrap () const



Rate zeroYieldImpl (Time) const



DiscountFactor discountImpl (Time) const



Size referenceNode (Time) const



Rate forwardImpl (Time) const


instantaneous forward-rate calculation


Rate compoundForwardImpl (Time, Integer) const</code></pre>
<h2>Detailed Description</h2>
<p>compound-forward structure </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the curve is tested by reproducing the input data.</p>
<dt>*</p>
<dd>the correctness of the curve is tested by checking the consistency between returned rates and swaps priced on the curve.</dl>
</dl>
<p> <code>Bug</code></p>
<dl>
<dd>swap rates are not reproduced exactly when using indexed coupons. Apparently, some assumption about the swap fixings is hard-coded into the bootstrapping algorithm.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> zeroYieldImpl (Time t) const [protected, virtual]</h3>
<p>Returns the zero yield rate for the given date calculating it from the instantaneous forward rate. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This is just a default, highly inefficient and possibly wildly inaccurate implementation. Derived classes should implement their own zeroYield method.</dl>
<p> Reimplemented from <code>ForwardRateStructure</code>.</p>
<h3><code>DiscountFactor</code> discountImpl (Time t) const [protected, virtual]</h3>
<p>Returns the discount factor for the given date calculating it from the instantaneous forward rate. </p>
<p> Reimplemented from <code>ForwardRateStructure</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
