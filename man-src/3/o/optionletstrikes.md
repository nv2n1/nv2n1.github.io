---
title: "optionletstrikes(3)"
name: "optionletstrikes"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionletstrikes/"
description: "QuantLib::StrippedOptionlet –"
---

<p>QuantLib::StrippedOptionlet &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/termstructures/volatility/optionlet/strippedoptionlet.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::StrippedOptionletBase</code>.</p>
<h3>Public Member Functions</h3>
<p>StrippedOptionlet (Natural settlementDays, const Calendar &amp;calendar, BusinessDayConvention bdc, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, const std::vector&lt; Date &gt; &amp;optionletDates, const std::vector&lt; Rate &gt; &amp;strikes, const std::vector&lt; std::vector&lt; Handle&lt; Quote &gt; &gt; &gt; &amp;, const DayCounter &amp;dc=Actual365Fixed()) <code>StrippedOptionletBase interface</code> </p>
<pre><code>const std::vector&lt; Rate &gt; &amp; optionletStrikes (Size i) const



const std::vector&lt; Volatility &gt; &amp; optionletVolatilities (Size i) const



const std::vector&lt; Date &gt; &amp; optionletFixingDates () const



const std::vector&lt; Time &gt; &amp; optionletFixingTimes () const



Size optionletMaturities () const



const std::vector&lt; Rate &gt; &amp; atmOptionletRates () const



DayCounter dayCounter () const



Calendar calendar () const



Natural settlementDays () const



BusinessDayConvention businessDayConvention () const</code></pre>
<h2>Detailed Description</h2>
<p>Helper class to wrap in a <code>StrippedOptionletBase</code> object a matrix of exogenously calculated optionlet (i.e. caplet/floorlet) volatilities (a.k.a. forward-forward volatilities).</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
