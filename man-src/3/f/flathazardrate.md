---
title: "flathazardrate(3)"
name: "flathazardrate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-flathazardrate/"
description: "QuantLib::FlatHazardRate – flat hazard-rate curve"
---

<p>QuantLib::FlatHazardRate &#8211; flat hazard-rate curve </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/flathazardrate.hpp&gt; </p>
<p> Inherits <code>QuantLib::HazardRateStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>FlatHazardRate</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;hazardRate, const <code>DayCounter</code> &amp;) </p>
<p> <code>FlatHazardRate</code> (const <code>Date</code> &amp;todaysDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;hazardRate, const <code>DayCounter</code> &amp;) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h2>Detailed Description</h2>
<p>flat hazard-rate curve </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
