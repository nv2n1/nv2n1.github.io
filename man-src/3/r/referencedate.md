---
title: "referencedate(3)"
name: "referencedate"
section: "3"
letter: "r"
url: "/docs/linux/man/3-referencedate/"
description: "QuantLib::SabrVolSurface – SABR volatility (smile) surface."
---

<p>QuantLib::SabrVolSurface &#8211; <code>SABR</code> volatility (smile) surface. </p>
<h2>Synopsis</h2>
<pre><code>void performCalculations () const



virtual void update ()</code></pre>
<p> Inherits <code>QuantLib::InterestRateVolSurface</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SabrVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, const <code>Handle</code>&lt; <code>BlackAtmVolCurve</code> &gt; &amp;, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Spread</code> &gt; &amp;atmRateSpreads, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;volSpreads) </p>
<p> const <code>Handle</code>&lt; <code>BlackAtmVolCurve</code> &gt; &amp; <code>atmCurve</code> () const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>volatilitySpreads</code> (const <code>Period</code> &amp;) const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>volatilitySpreads</code> (const <code>Date</code> &amp;) const<br />
 <code>TermStructure interface</code><br />
 void performCalculations () const</p>
<p>virtual void update () <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;)<br />
 <code>BlackVolSurface interface</code> </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time) const</p>
<h3>Protected Member Functions</h3>
<p>boost::array&lt; <code>Real</code>, 4 &gt; <code>sabrGuesses</code> (const <code>Date</code> &amp;) const<br />
 <code>LazyObject interface</code> </p>
<pre><code>void performCalculations () const



virtual void update ()</code></pre>
<h2>Detailed Description</h2>
<p><code>SABR</code> volatility (smile) surface. </p>
<p> blah blah</p>
<h2>Member Function Documentation</h2>
<h3>virtual void update () [protected, virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
