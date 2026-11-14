---
title: "quantlib_actual365fixed(3)"
name: "quantlib_actual365fixed"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_actual365fixed/"
description: "QuantLib::Actual365Fixed – Actual/365 (Fixed) day count convention."
---

<p>QuantLib::Actual365Fixed &#8211; Actual/365 (Fixed) day count convention. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/daycounters/actual365fixed.hpp&gt; </p>
<p> Inherits <code>QuantLib::DayCounter</code>. </p>
<h2>Detailed Description</h2>
<p>Actual/365 (Fixed) day count convention. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>According to ISDA, &#8216;Actual/365&#8217; (without &#8216;Fixed&#8217;) is an alias for &#8216;Actual/Actual (ISDA)&#8217; (see <code>ActualActual</code>.) If Actual/365 is not explicitly specified as fixed in an instrument specification, you might want to double-check its meaning.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, and <code>Replication.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
