---
title: "optiontenorsininterpolation(3)"
name: "optiontenorsininterpolation"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optiontenorsininterpolation/"
description: "QuantLib::AbcdAtmVolCurve – Abcd-interpolated at-the-money (no-smile) volatility curve."
---

<p>QuantLib::AbcdAtmVolCurve &#8211; Abcd-interpolated at-the-money (no-smile) volatility curve. </p>
<h2>Synopsis</h2>
<pre><code>const std::vector&lt; Period &gt; &amp; optionTenors () const



const std::vector&lt; Period &gt; &amp; optionTenorsInInterpolation () const



const std::vector&lt; Date &gt; &amp; optionDates () const



const std::vector&lt; Time &gt; &amp; optionTimes () const</code></pre>
<p> Inherits <code>QuantLib::BlackAtmVolCurve</code>, and <code>QuantLib::LazyObject</code>.</p>
<h3>Public Member Functions</h3>
<p>const std::vector&lt; Period &gt; &amp; optionTenors () const</p>
<p>const std::vector&lt; Period &gt; &amp; optionTenorsInInterpolation () const</p>
<p>const std::vector&lt; Date &gt; &amp; optionDates () const</p>
<p>const std::vector&lt; Time &gt; &amp; optionTimes () const <code>TermStructure interface</code> </p>
<p> virtual <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> <code>LazyObject interface</code><br />
 const std::vector&lt; Period &gt; &amp; optionTenors () const</p>
<p>const std::vector&lt; Period &gt; &amp; optionTenorsInInterpolation () const</p>
<p>const std::vector&lt; Date &gt; &amp; optionDates () const</p>
<p>const std::vector&lt; Time &gt; &amp; optionTimes () const <code>some inspectors</code> </p>
<pre><code>const std::vector&lt; Period &gt; &amp; optionTenors () const



const std::vector&lt; Period &gt; &amp; optionTenorsInInterpolation () const



const std::vector&lt; Date &gt; &amp; optionDates () const



const std::vector&lt; Time &gt; &amp; optionTimes () const</code></pre>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<p><code>BlackAtmVolCurve interface</code> </p>
<p> virtual <code>Real</code> <code>atmVarianceImpl</code> (Time t) const<br />
 <i>spot at-the-money variance calculation (k adjusted) </i><br />
 virtual <code>Volatility</code> <code>atmVolImpl</code> (Time t) const<br />
 <i>spot at-the-money volatility calculation (k adjusted) </i></p>
<h2>Detailed Description</h2>
<p>Abcd-interpolated at-the-money (no-smile) volatility curve. </p>
<p> blah blah</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
