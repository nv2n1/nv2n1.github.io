---
title: "quantlib_capletvariancecurve(3)"
name: "quantlib_capletvariancecurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_capletvariancecurve/"
description: "QuantLib::CapletVarianceCurve –"
---

<p>QuantLib::CapletVarianceCurve &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/capletvariancecurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::OptionletVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CapletVarianceCurve</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; Volatility &gt; &amp;capletVolCurve, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time t) const<br />
 <i>implements the actual smile calculation in derived classes </i><br />
 Volatility <code>volatilityImpl</code> (Time t, Rate) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p><code>Deprecated</code></p>
<dl COMPACT>
<dd>use the <code>StrippedOptionletAdapter</code> of a <code>StrippedOptionlet</code> instance</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
