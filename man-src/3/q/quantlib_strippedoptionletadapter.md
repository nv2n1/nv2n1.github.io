---
title: "quantlib_strippedoptionletadapter(3)"
name: "quantlib_strippedoptionletadapter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_strippedoptionletadapter/"
description: "QuantLib::StrippedOptionletAdapter –"
---

<p>QuantLib::StrippedOptionletAdapter &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/strippedoptionletadapter.hpp&gt; </p>
<p> Inherits <code>QuantLib::OptionletVolatilityStructure</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StrippedOptionletAdapter</code> (const boost::shared_ptr&lt; <code>StrippedOptionletBase</code> &gt; &amp;) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Rate <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Rate <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>update</code> () </p>
<p> void <code>performCalculations</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>OptionletVolatilityStructure interface</code> </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time optionTime) const<br />
 <i>implements the actual smile calculation in derived classes </i><br />
 <code>Volatility</code> <code>volatilityImpl</code> (Time length, Rate strike) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Adapter class for turning a <code>StrippedOptionletBase</code> object into an <code>OptionletVolatilityStructure</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
