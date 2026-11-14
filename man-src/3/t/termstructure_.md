---
title: "termstructure_(3)"
name: "termstructure_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-termstructure_/"
---

QuantLib::BMAIndex - <b>Bond</b> Market Association index. 

<h2>Synopsis</h2>

<pre><code>BMAIndex (const Handle&lt; YieldTermStructure &gt; &amp;h=Handle&lt; YieldTermStructure &gt;())</code></pre> Inherits <b>QuantLib::InterestRateIndex</b>.

<h3>Public Member Functions</h3>

<pre><code>BMAIndex (const Handle&lt; YieldTermStructure &gt; &amp;h=Handle&lt; YieldTermStructure &gt;())</code></pre> <b>Index interface</b> 
 
 std::string <b>name</b> () const 
 
 bool <b>isValidFixingDate</b> (const <b>Date</b> &amp;fixingDate) const 
 <i>returns TRUE if the fixing date is a valid one </i> <b>InterestRateIndex interface</b> 
 
 <b>Handle</b>&lt; <b>YieldTermStructure</b> &gt; <b>termStructure</b> () const 
 
 <b>Date</b> <b>maturityDate</b> (const <b>Date</b> &amp;valueDate) const 
 <b>Date calculations</b> 
 
 <b>Schedule</b> <b>fixingSchedule</b> (const <b>Date</b> &amp;start, const <b>Date</b> &amp;end)

<h3>Protected Member Functions</h3>

<b>Rate</b> <b>forecastFixing</b> (const <b>Date</b> &amp;fixingDate) const

<h3>Protected Attributes</h3>

<b>Handle</b>&lt; <b>YieldTermStructure</b> &gt; <b>termStructure_</b>

<h2>Detailed Description</h2>

<b>Bond</b> Market Association index. 

 The BMA index is the short-term tax-exempt reference index of the <b>Bond</b> Market Association. It has tenor one week, is fixed weekly on Wednesdays and is applied with a one-day's fixing gap from Thursdays on for one week. It is the tax-exempt correspondent of the 1M USD-Libor.

<h2>Member Function Documentation</h2>

<h3>std::string name () const [virtual]</h3>

BMA is fixed weekly on Wednesdays. 

 Reimplemented from <b>InterestRateIndex</b>.

<h3><b>Schedule</b> fixingSchedule (const <b>Date</b> &amp; start, const <b>Date</b> &amp; end)</h3>

This method returns a schedule of fixing dates between start and end.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
