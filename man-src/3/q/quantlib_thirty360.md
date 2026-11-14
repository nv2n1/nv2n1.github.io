---
title: "quantlib_thirty360(3)"
name: "quantlib_thirty360"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_thirty360/"
description: "QuantLib::Thirty360 – 30/360 day count convention"
---

<p>QuantLib::Thirty360 &#8211; 30/360 day count convention </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/daycounters/thirty360.hpp&gt; </p>
<p> Inherits <code>QuantLib::DayCounter</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Convention</code> { <code>USA</code>, <code>BondBasis</code>, <code>European</code>, <code>EurobondBasis</code>, <code>Italian</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Thirty360</code> (Convention c=Thirty360::BondBasis) </p>
<h2>Detailed Description</h2>
<p>30/360 day count convention </p>
<p> The 30/360 day count can be calculated according to US, European, or Italian conventions. </p>
<p> US (NASD) convention: if the starting date is the 31st of a month, it becomes equal to the 30th of the same month. If the ending date is the 31st of a month and the starting date is earlier than the 30th of a month, the ending date becomes equal to the 1st of the next month, otherwise the ending date becomes equal to the 30th of the same month. Also known as &#8217;30/360&#8242;, &#8216;360/360&#8217;, or &#8216;Bond Basis&#8217; </p>
<p> European convention: starting dates or ending dates that occur on the 31st of a month become equal to the 30th of the same month. Also known as &#8217;30E/360&#8242;, or &#8216;Eurobond Basis&#8217; </p>
<p> Italian convention: starting dates or ending dates that occur on February and are grater than 27 become equal to 30 for computational sake. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
