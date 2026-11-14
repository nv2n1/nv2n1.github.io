---
title: "discountfactor(3)"
name: "discountfactor"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discountfactor/"
description: "QuantLib::InterestRate – Concrete interest rate class."
---

<p>QuantLib::InterestRate &#8211; Concrete interest rate class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/interestrate.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>constructors</code> </p>
<p> <code>InterestRate</code> ()<br />
 <i>Default constructor returning a null interest rate. </i><br />
 <code>InterestRate</code> (<code>Rate</code> r, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>(), Compounding comp=Continuous, <code>Frequency</code> freq=Annual)<br />
 <i>Standard constructor. </i> </p>
<p> <code>conversions</code> </p>
<p> <code>operator Rate</code> () const </p>
<p> <code>inspectors</code> </p>
<p> <code>Rate</code> <code>rate</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>dayCounter</code> () const </p>
<p> Compounding <code>compounding</code> () const </p>
<p> <code>Frequency</code> <code>frequency</code> () const </p>
<p> <code>discount/compound factor calculations</code> </p>
<p> <code>DiscountFactor</code> <code>discountFactor</code> (<code>Time</code> t) const<br />
 <i>discount factor implied by the rate compounded at time t. </i><br />
 <code>DiscountFactor</code> <code>discountFactor</code> (const <code>Date</code> &amp;d1, const <code>Date</code> &amp;d2, const <code>Date</code> &amp;refStart=<code>Date</code>(), const <code>Date</code> &amp;refEnd=<code>Date</code>()) const<br />
 <i>discount factor implied by the rate compounded between two dates </i><br />
 Real <code>compoundFactor</code> (<code>Time</code> t) const<br />
 <i>compound factor implied by the rate compounded at time t. </i><br />
 Real <code>compoundFactor</code> (const <code>Date</code> &amp;d1, const <code>Date</code> &amp;d2, const <code>Date</code> &amp;refStart=<code>Date</code>(), const <code>Date</code> &amp;refEnd=<code>Date</code>()) const<br />
 <i>compound factor implied by the rate compounded between two dates </i> </p>
<p> <code>equivalent rate calculations</code> </p>
<p> <code>InterestRate</code> <code>equivalentRate</code> (<code>Time</code> t, Compounding comp, <code>Frequency</code> freq=Annual) const<br />
 <i>equivalent interest rate for a compounding period t. </i><br />
 <code>InterestRate</code> <code>equivalentRate</code> (<code>Date</code> d1, <code>Date</code> d2, const <code>DayCounter</code> &amp;resultDC, Compounding comp, <code>Frequency</code> freq=Annual) const<br />
 <i>equivalent rate for a compounding period between two dates </i></p>
<h3>Static Public Member Functions</h3>
<p><code>implied rate calculations</code> </p>
<p> static <code>InterestRate</code> <code>impliedRate</code> (Real compound, <code>Time</code> t, const <code>DayCounter</code> &amp;resultDC, Compounding comp, <code>Frequency</code> freq=Annual)<br />
 <i>implied interest rate for a given compound factor at a given time. </i><br />
 static <code>InterestRate</code> <code>impliedRate</code> (Real compound, const <code>Date</code> &amp;d1, const <code>Date</code> &amp;d2, const <code>DayCounter</code> &amp;resultDC, Compounding comp, <code>Frequency</code> freq=Annual)<br />
 <i>implied rate for a given compound factor between two dates. </i></p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>InterestRate</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Concrete interest rate class. </p>
<p> This class encapsulate the interest rate compounding algebra. It manages day-counting conventions, compounding conventions, conversion between different conventions, discount/compound factor calculations, and implied/equivalent rate calculations. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>Converted rates are checked against known good results</dl>
<p> <code>Examples: </code> </p>
<p> <code>CallableBonds.cpp</code>, and <code>FittedBondCurve.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3><code>DiscountFactor</code> discountFactor (<code>Time</code> t) const</h3>
<p>discount factor implied by the rate compounded at time t. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Time must be measured using InterestRate&#8217;s own day counter.</dl>
<h3>Real compoundFactor (<code>Time</code> t) const</h3>
<p>compound factor implied by the rate compounded at time t. </p>
<p> returns the compound (a.k.a capitalization) factor implied by the rate compounded at time t. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Time must be measured using InterestRate&#8217;s own day counter.</dl>
<h3>Real compoundFactor (const <code>Date</code> &amp; d1, const <code>Date</code> &amp; d2, const <code>Date</code> &amp; refStart = <code>Date</code>(), const <code>Date</code> &amp; refEnd = <code>Date</code>()) const</h3>
<p>compound factor implied by the rate compounded between two dates </p>
<p> returns the compound (a.k.a capitalization) factor implied by the rate compounded between two dates.</p>
<h3>static <code>InterestRate</code> impliedRate (Real compound, <code>Time</code> t, const <code>DayCounter</code> &amp; resultDC, Compounding comp, <code>Frequency</code> freq = Annual) [static]</h3>
<p>implied interest rate for a given compound factor at a given time. </p>
<p> The resulting <code>InterestRate</code> has the day-counter provided as input. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Time must be measured using the day-counter provided as input.</dl>
<h3>static <code>InterestRate</code> impliedRate (Real compound, const <code>Date</code> &amp; d1, const <code>Date</code> &amp; d2, const <code>DayCounter</code> &amp; resultDC, Compounding comp, <code>Frequency</code> freq = Annual) [static]</h3>
<p>implied rate for a given compound factor between two dates. </p>
<p> The resulting rate is calculated taking the required day-counting rule into account.</p>
<h3><code>InterestRate</code> equivalentRate (<code>Time</code> t, Compounding comp, <code>Frequency</code> freq = Annual) const</h3>
<p>equivalent interest rate for a compounding period t. </p>
<p> The resulting <code>InterestRate</code> shares the same implicit day-counting rule of the original <code>InterestRate</code> instance. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Time must be measured using the InterestRate&#8217;s own day counter.</dl>
<h3><code>InterestRate</code> equivalentRate (<code>Date</code> d1, <code>Date</code> d2, const <code>DayCounter</code> &amp; resultDC, Compounding comp, <code>Frequency</code> freq = Annual) const</h3>
<p>equivalent rate for a compounding period between two dates </p>
<p> The resulting rate is calculated taking the required day-counting rule into account.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>InterestRate</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
