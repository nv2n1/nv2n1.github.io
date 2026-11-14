---
title: "forecastfixing(3)"
name: "forecastfixing"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forecastfixing/"
description: "QuantLib::BMAIndex – Bond Market Association index."
---

<p>QuantLib::BMAIndex &#8211; <code>Bond</code> Market Association index. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/bmaindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::InterestRateIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BMAIndex</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>Index interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> bool <code>isValidFixingDate</code> (const <code>Date</code> &amp;fixingDate) const<br />
 <i>returns TRUE if the fixing date is a valid one </i> </p>
<p> <code>InterestRateIndex interface</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const </p>
<p> <code>Date calculations</code> </p>
<p> <code>Schedule</code> <code>fixingSchedule</code> (const <code>Date</code> &amp;start, const <code>Date</code> &amp;end) </p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>forecastFixing</code> (const <code>Date</code> &amp;fixingDate) const </p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure_</code> </p>
<h2>Detailed Description</h2>
<p><code>Bond</code> Market Association index. </p>
<p> The BMA index is the short-term tax-exempt reference index of the <code>Bond</code> Market Association. It has tenor one week, is fixed weekly on Wednesdays and is applied with a one-day&#8217;s fixing gap from Thursdays on for one week. It is the tax-exempt correspondent of the 1M USD-Libor.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p>BMA is fixed weekly on Wednesdays. </p>
<p> Reimplemented from <code>InterestRateIndex</code>.</p>
<h3><code>Schedule</code> fixingSchedule (const <code>Date</code> &amp; start, const <code>Date</code> &amp; end)</h3>
<p>This method returns a schedule of fixing dates between start and end. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
