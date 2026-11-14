---
title: "strikes(3)"
name: "strikes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strikes/"
description: "QuantLib::CapFloorTermVolSurface – Cap/floor smile volatility surface."
---

<p>QuantLib::CapFloorTermVolSurface &#8211; Cap/floor smile volatility surface. </p>
<h2>Synopsis</h2>
<pre><code>const std::vector&lt; Period &gt; &amp; optionTenors () const



const std::vector&lt; Date &gt; &amp; optionDates () const



const std::vector&lt; Time &gt; &amp; optionTimes () const



const std::vector&lt; Rate &gt; &amp; strikes () const



Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::CapFloorTermVolatilityStructure</code>, and <code>QuantLib::LazyObject</code>.</p>
<h3>Public Member Functions</h3>
<p>const std::vector&lt; Period &gt; &amp; optionTenors () const</p>
<p>const std::vector&lt; Date &gt; &amp; optionDates () const</p>
<p>const std::vector&lt; Time &gt; &amp; optionTimes () const</p>
<p>const std::vector&lt; Rate &gt; &amp; strikes () const</p>
<p>Protected Member Functions <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> <code>LazyObject interface</code><br />
 const std::vector&lt; Period &gt; &amp; optionTenors () const</p>
<p>const std::vector&lt; Date &gt; &amp; optionDates () const</p>
<p>const std::vector&lt; Time &gt; &amp; optionTimes () const</p>
<p>const std::vector&lt; Rate &gt; &amp; strikes () const</p>
<p>Protected Member Functions <code>some inspectors</code> </p>
<pre><code>const std::vector&lt; Period &gt; &amp; optionTenors () const



const std::vector&lt; Date &gt; &amp; optionDates () const



const std::vector&lt; Time &gt; &amp; optionTimes () const



const std::vector&lt; Rate &gt; &amp; strikes () const



Protected Member Functions</code></pre>
<p> <code>Volatility</code> <code>volatilityImpl</code> (Time t, Rate strike) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Cap/floor smile volatility surface. </p>
<p> This class provides the volatility for a given cap by interpolating a volatility surface whose elements are the market term volatilities of a set of caps/floors with given length and given strike.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
