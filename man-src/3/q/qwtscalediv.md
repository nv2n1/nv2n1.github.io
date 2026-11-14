---
title: "qwtscalediv(3)"
name: "qwtscalediv"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscalediv/"
description: "QwtScaleDiv –"
---

<p>QwtScaleDiv &#8211; </p>
<p> A class representing a scale division.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_div.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>TickType</code> { <code>NoTick</code> = -1, <code>MinorTick</code>, <code>MediumTick</code>, <code>MajorTick</code>, <code>NTickTypes</code> }<br />
 <i>Scale tick types. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleDiv</code> (double <code>lowerBound</code>=0.0, double <code>upperBound</code>=0.0) </p>
<p> <code>QwtScaleDiv</code> (const <code>QwtInterval</code> &amp;, QList&lt; double &gt;[<code>NTickTypes</code>]) </p>
<p> <code>QwtScaleDiv</code> (double <code>lowerBound</code>, double <code>upperBound</code>, QList&lt; double &gt;[<code>NTickTypes</code>]) </p>
<p> <code>QwtScaleDiv</code> (double <code>lowerBound</code>, double <code>upperBound</code>, const QList&lt; double &gt; &amp;minorTicks, const QList&lt; double &gt; &amp;mediumTicks, const QList&lt; double &gt; &amp;majorTicks) </p>
<p> bool <code>operator==</code> (const <code>QwtScaleDiv</code> &amp;) const<br />
 <i>Equality operator. </i><br />
 bool <code>operator!=</code> (const <code>QwtScaleDiv</code> &amp;) const<br />
 <i>Inequality. </i><br />
 void <code>setInterval</code> (double <code>lowerBound</code>, double <code>upperBound</code>) </p>
<p> void <code>setInterval</code> (const <code>QwtInterval</code> &amp;) </p>
<p> <code>QwtInterval</code> <code>interval</code> () const </p>
<p> void <code>setLowerBound</code> (double) </p>
<p> double <code>lowerBound</code> () const </p>
<p> void <code>setUpperBound</code> (double) </p>
<p> double <code>upperBound</code> () const </p>
<p> double <code>range</code> () const </p>
<p> bool <code>contains</code> (double value) const </p>
<p> void <code>setTicks</code> (int tickType, const QList&lt; double &gt; &amp;) </p>
<p> QList&lt; double &gt; <code>ticks</code> (int tickType) const </p>
<p> bool <code>isEmpty</code> () const<br />
 <i>Check if the scale division is empty( </i><code>lowerBound()</code> == <code>upperBound()</code> )<br />
 bool <code>isIncreasing</code> () const<br />
 <i>Check if the scale division is increasing( </i><code>lowerBound()</code> &lt;= <code>upperBound()</code> )<br />
 void <code>invert</code> () </p>
<p> <code>QwtScaleDiv</code> <code>inverted</code> () const </p>
<p> <code>QwtScaleDiv</code> <code>bounded</code> (double <code>lowerBound</code>, double <code>upperBound</code>) const </p>
<h2>Detailed Description</h2>
<p>A class representing a scale division. </p>
<p> A Qwt scale is defined by its boundaries and 3 list for the positions of the major, medium and minor ticks. </p>
<p> The upperLimit() might be smaller than the lowerLimit() to indicate inverted scales. </p>
<p> Scale divisions can be calculated from a <code>QwtScaleEngine</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleEngine::divideScale()</code>, <code>QwtPlot::setAxisScaleDiv()</code>, QwtAbstractSlider::setScaleDiv()</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtScaleDiv::TickType</code></h3>
<p>Scale tick types. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoTick </i></p>
<dd>No ticks.</p>
<dt><i>MinorTick </i></p>
<dd>Minor ticks.</p>
<dt><i>MediumTick </i></p>
<dd>Medium ticks.</p>
<dt><i>MajorTick </i></p>
<dd>Major ticks.</p>
<dt><i>NTickTypes </i></p>
<dd>Number of valid tick types.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleDiv::QwtScaleDiv (doublelowerBound = 0.0, doubleupperBound = 0.0) [explicit]</h3>
<p>Construct a division without ticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> First boundary<br />
 <i>upperBound</i> Second boundary</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>lowerBound might be greater than upperBound for inverted scales</dl>
<h3>QwtScaleDiv::QwtScaleDiv (const <code>QwtInterval</code> &amp;interval, QList&lt; double &gt;ticks[NTickTypes]) [explicit]</h3>
<p>Construct a scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval<br />
 <i>ticks</i> List of major, medium and minor ticks</dl>
<h3>QwtScaleDiv::QwtScaleDiv (doublelowerBound, doubleupperBound, QList&lt; double &gt;ticks[NTickTypes]) [explicit]</h3>
<p>Construct a scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> First boundary<br />
 <i>upperBound</i> Second boundary<br />
 <i>ticks</i> List of major, medium and minor ticks</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>lowerBound might be greater than upperBound for inverted scales</dl>
<h3>QwtScaleDiv::QwtScaleDiv (doublelowerBound, doubleupperBound, const QList&lt; double &gt; &amp;minorTicks, const QList&lt; double &gt; &amp;mediumTicks, const QList&lt; double &gt; &amp;majorTicks) [explicit]</h3>
<p>Construct a scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> First boundary<br />
 <i>upperBound</i> Second boundary<br />
 <i>minorTicks</i> List of minor ticks<br />
 <i>mediumTicks</i> List medium ticks<br />
 <i>majorTicks</i> List of major ticks</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>lowerBound might be greater than upperBound for inverted scales</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtScaleDiv</code> QwtScaleDiv::bounded (doublelowerBound, doubleupperBound) const</h3>
<p>Return a scale division with an interval [lowerBound, upperBound] where all ticks outside this interval are removed </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> Lower bound<br />
 <i>upperBound</i> Upper bound</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scale division with all ticks inside of the given interval</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>lowerBound might be greater than upperBound for inverted scales</dl>
<h3>bool QwtScaleDiv::contains (doublevalue) const</h3>
<p>Return if a value is between <code>lowerBound()</code> and <code>upperBound()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<h3><code>QwtInterval</code> QwtScaleDiv::interval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>lowerBound -&gt; upperBound</dl>
<h3>void QwtScaleDiv::invert ()</h3>
<p>Invert the scale division </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>inverted()</code></dl>
<h3><code>QwtScaleDiv</code> QwtScaleDiv::inverted () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A scale division with inverted boundaries and ticks</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invert()</code></dl>
<h3>double QwtScaleDiv::lowerBound () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>First boundary</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>upperBound()</code></dl>
<h3>bool QwtScaleDiv::operator!= (const <code>QwtScaleDiv</code> &amp;other) const</h3>
<p>Inequality. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if this instance is not equal to other</dl>
<h3>bool QwtScaleDiv::operator== (const <code>QwtScaleDiv</code> &amp;other) const</h3>
<p>Equality operator. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if this instance is equal to other</dl>
<h3>double QwtScaleDiv::range () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>upperBound()</code> &#8211; <code>lowerBound()</code></dl>
<h3>void QwtScaleDiv::setInterval (doublelowerBound, doubleupperBound)</h3>
<p>Change the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> First boundary<br />
 <i>upperBound</i> Second boundary</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>lowerBound might be greater than upperBound for inverted scales</dl>
<h3>void QwtScaleDiv::setInterval (const <code>QwtInterval</code> &amp;interval)</h3>
<p>Change the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval</dl>
<h3>void QwtScaleDiv::setLowerBound (doublelowerBound)</h3>
<p>Set the first boundary </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> First boundary</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>lowerBiound(), <code>setUpperBound()</code></dl>
<h3>void QwtScaleDiv::setTicks (inttype, const QList&lt; double &gt; &amp;ticks)</h3>
<p>Assign ticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> MinorTick, MediumTick or MajorTick<br />
 <i>ticks</i> Values of the tick positions</dl>
<h3>void QwtScaleDiv::setUpperBound (doubleupperBound)</h3>
<p>Set the second boundary </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>upperBound</i> Second boundary</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>upperBound()</code>, <code>setLowerBound()</code></dl>
<h3>QList&lt; double &gt; QwtScaleDiv::ticks (inttype) const</h3>
<p>Return a list of ticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> MinorTick, MediumTick or MajorTick</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Tick list</dl>
<h3>double QwtScaleDiv::upperBound () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>upper bound</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lowerBound()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
