---
title: "prices(3)"
name: "prices"
section: "3"
letter: "p"
url: "/docs/linux/man/3-prices/"
description: "ql/prices.hpp – price classes"
---

<p>ql/prices.hpp &#8211; price classes </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/timeseries.hpp&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>IntervalPrice</code><br />
 <i>interval price </i></p>
<h3>Enumerations</h3>
<p>enum <code>PriceType</code> { <code>Bid</code>, <code>Ask</code>, <code>Last</code>, <code>Close</code>, <code>Mid</code>, <code>MidEquivalent</code>, <code>MidSafe</code> }<br />
 <i>Price types. </i></p>
<h3>Functions</h3>
<p>Real <code>midEquivalent</code> (const Real bid, const Real ask, const Real last, const Real close) </p>
<p> Real <code>midSafe</code> (const Real bid, const Real ask)</p>
<h2>Detailed Description</h2>
<p>price classes</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
