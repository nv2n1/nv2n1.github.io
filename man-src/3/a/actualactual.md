---
title: "actualactual(3)"
name: "actualactual"
section: "3"
letter: "a"
url: "/docs/linux/man/3-actualactual/"
description: "QuantLib::ActualActual – Actual/Actual day count."
---

<p>QuantLib::ActualActual &#8211; Actual/Actual day count. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/daycounters/actualactual.hpp&gt; </p>
<p> Inherits <code>QuantLib::DayCounter</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Convention</code> { <code>ISMA</code>, <code>Bond</code>, <code>ISDA</code>, <code>Historical</code>, <code>Actual365</code>, <code>AFB</code>, <code>Euro</code> } </p>
<h3>Public Member Functions</h3>
<p><code>ActualActual</code> (Convention c=ActualActual::ISDA) </p>
<h2>Detailed Description</h2>
<p>Actual/Actual day count. </p>
<p> The day count can be calculated according to: </p>
<dl COMPACT>
<dt>*</p>
<dd>the ISDA convention, also known as &#8216;Actual/Actual (Historical)&#8217;, &#8216;Actual/Actual&#8217;, &#8216;Act/Act&#8217;, and according to ISDA also &#8216;Actual/365&#8217;, &#8216;Act/365&#8217;, and &#8216;A/365&#8217;;</p>
<dt>*</p>
<dd>the ISMA and US Treasury convention, also known as &#8216;Actual/Actual (Bond)&#8217;;</p>
<dt>*</p>
<dd>the AFB convention, also known as &#8216;Actual/Actual (Euro)&#8217;.</dl>
<p> For more details, refer to <a rel="nofollow" href="http://www.isda.org/publications/pdf/Day-Count-Fracation1999.pdf">http://www.isda.org/publications/pdf/Day-Count-Fracation1999.pdf</a> </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the results is checked against known good values.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>FRA.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
