---
title: "qwtohlcsample(3)"
name: "qwtohlcsample"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtohlcsample/"
description: "QwtOHLCSample –"
---

<p>QwtOHLCSample &#8211; </p>
<p> Open-High-Low-Close sample used in financial charts.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_samples.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtOHLCSample</code> (double <code>time</code>=0.0, double <code>open</code>=0.0, double <code>high</code>=0.0, double <code>low</code>=0.0, double <code>close</code>=0.0) </p>
<p> <code>QwtInterval</code> <code>boundingInterval</code> () const<br />
 <i>Calculate the bounding interval of the OHLC values. </i><br />
 bool <code>isValid</code> () const<br />
 <i>Check if a sample is valid. </i></p>
<h3>Public Attributes</h3>
<p>double <code>time</code> </p>
<p> double <code>open</code><br />
 <i>Opening price. </i><br />
 double <code>high</code><br />
 <i>Highest price. </i><br />
 double <code>low</code><br />
 <i>Lowest price. </i><br />
 double <code>close</code><br />
 <i>Closing price. </i></p>
<h2>Detailed Description</h2>
<p>Open-High-Low-Close sample used in financial charts. </p>
<p> In financial charts the movement of a price in a time interval is often represented by the opening/closing prices and the lowest/highest prices in this interval. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTradingChartData</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtOHLCSample::QwtOHLCSample (doublet = 0.0, doubleo = 0.0, doubleh = 0.0, doublel = 0.0, doublec = 0.0) [inline]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>t</i> Time value<br />
 <i>o</i> Open value<br />
 <i>h</i> High value<br />
 <i>l</i> Low value<br />
 <i>c</i> Close value</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtInterval</code> QwtOHLCSample::boundingInterval () const [inline]</h3>
<p>Calculate the bounding interval of the OHLC values. For valid samples the limits of this interval are always low/high. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h3>bool QwtOHLCSample::isValid () const [inline]</h3>
<p>Check if a sample is valid. A sample is valid, when all of the following checks are true: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>low &lt;= high</p>
<dt>&bull;</p>
<dd>low &lt;= open &lt;= high</p>
<dt>&bull;</p>
<dd>low &lt;= close &lt;= high</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the sample is valid</dl>
<h2>Member Data Documentation</h2>
<h3>double QwtOHLCSample::time</h3>
<p>Time of the sample, usually a number representing a specific interval &#8211; like a day. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
