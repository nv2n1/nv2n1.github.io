---
title: "qwtinterval(3)"
name: "qwtinterval"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtinterval/"
description: "QwtInterval –"
---

<p>QwtInterval &#8211; </p>
<p> A class representing an interval.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_interval.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>BorderFlag</code> { <code>IncludeBorders</code> = 0x00, <code>ExcludeMinimum</code> = 0x01, <code>ExcludeMaximum</code> = 0x02, <code>ExcludeBorders</code> = ExcludeMinimum | ExcludeMaximum } </p>
<p> typedef QFlags&lt; <code>BorderFlag</code> &gt; <code>BorderFlags</code><br />
 <i>Border flags. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtInterval</code> ()<br />
 <i>Default Constructor. </i><br />
 <code>QwtInterval</code> (double <code>minValue</code>, double <code>maxValue</code>, <code>BorderFlags</code>=<code>IncludeBorders</code>) </p>
<p> void <code>setInterval</code> (double <code>minValue</code>, double <code>maxValue</code>, <code>BorderFlags</code>=<code>IncludeBorders</code>) </p>
<p> <code>QwtInterval</code> <code>normalized</code> () const<br />
 <i>Normalize the limits of the interval. </i><br />
 <code>QwtInterval</code> <code>inverted</code> () const </p>
<p> <code>QwtInterval</code> <code>limited</code> (double <code>minValue</code>, double <code>maxValue</code>) const </p>
<p> bool <code>operator==</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Compare two intervals. </i><br />
 bool <code>operator!=</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Compare two intervals. </i><br />
 void <code>setBorderFlags</code> (<code>BorderFlags</code>) </p>
<p> <code>BorderFlags</code> <code>borderFlags</code> () const </p>
<p> double <code>minValue</code> () const </p>
<p> double <code>maxValue</code> () const </p>
<p> double <code>width</code> () const<br />
 <i>Return the width of an interval. </i><br />
 void <code>setMinValue</code> (double) </p>
<p> void <code>setMaxValue</code> (double) </p>
<p> bool <code>contains</code> (double value) const </p>
<p> bool <code>intersects</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Test if two intervals overlap. </i><br />
 <code>QwtInterval</code> <code>intersect</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Intersect 2 intervals. </i><br />
 <code>QwtInterval</code> <code>unite</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Unite 2 intervals. </i><br />
 <code>QwtInterval</code> <code>operator|</code> (const <code>QwtInterval</code> &amp;) const </p>
<p> <code>QwtInterval</code> <code>operator&amp;</code> (const <code>QwtInterval</code> &amp;) const<br />
 <i>Intersection of two intervals. </i><br />
 <code>QwtInterval</code> &amp; <code>operator|=</code> (const <code>QwtInterval</code> &amp;)<br />
 <i>Unite this interval with the given interval. </i><br />
 <code>QwtInterval</code> &amp; <code>operator&amp;=</code> (const <code>QwtInterval</code> &amp;)<br />
 <i>Intersect this interval with the given interval. </i><br />
 <code>QwtInterval</code> <code>extend</code> (double value) const<br />
 <i>Extend the interval. </i><br />
 <code>QwtInterval</code> <code>operator|</code> (double) const </p>
<p> <code>QwtInterval</code> &amp; <code>operator|=</code> (double) </p>
<p> bool <code>isValid</code> () const </p>
<p> bool <code>isNull</code> () const </p>
<p> void <code>invalidate</code> () </p>
<p> <code>QwtInterval</code> <code>symmetrize</code> (double value) const </p>
<h2>Detailed Description</h2>
<p>A class representing an interval. </p>
<p> The interval is represented by 2 doubles, the lower and the upper limit.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtInterval::BorderFlag</code></h3>
<p>Flag indicating if a border is included or excluded </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderFlags()</code>, <code>borderFlags()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>IncludeBorders </i></p>
<dd>Min/Max values are inside the interval.</p>
<dt><i>ExcludeMinimum </i></p>
<dd>Min value is not included in the interval.</p>
<dt><i>ExcludeMaximum </i></p>
<dd>Max value is not included in the interval.</p>
<dt><i>ExcludeBorders </i></p>
<dd>Min/Max values are not included in the interval.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtInterval::QwtInterval () [inline]</h3>
<p>Default Constructor. Creates an invalid interval [0.0, -1.0] </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code>, <code>isValid()</code></dl>
<h3>QwtInterval::QwtInterval (doubleminValue, doublemaxValue, <code>BorderFlags</code>borderFlags = <code>IncludeBorders</code>) [inline]</h3>
<p>Constructor </p>
<p> Build an interval with from min/max values </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value<br />
 <i>maxValue</i> Maximum value<br />
 <i>borderFlags</i> Include/Exclude borders</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtInterval::BorderFlags</code> QwtInterval::borderFlags () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Border flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderFlags()</code></dl>
<h3>bool QwtInterval::contains (doublevalue) const</h3>
<p>Test if a value is inside an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if value &gt;= <code>minValue()</code> &amp;&amp; value &lt;= <code>maxValue()</code></dl>
<h3><code>QwtInterval</code> QwtInterval::extend (doublevalue) const</h3>
<p>Extend the interval. If value is below <code>minValue()</code>, value becomes the lower limit. If value is above <code>maxValue()</code>, value becomes the upper limit. </p>
<p> <code>extend()</code> has no effect for invalid intervals </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>extended interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h3><code>QwtInterval</code> QwtInterval::intersect (const <code>QwtInterval</code> &amp;other) const</h3>
<p>Intersect 2 intervals. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to be intersect with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Intersection</dl>
<h3>bool QwtInterval::intersects (const <code>QwtInterval</code> &amp;other) const</h3>
<p>Test if two intervals overlap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the intervals are intersecting</dl>
<h3>void QwtInterval::invalidate () [inline]</h3>
<p>Invalidate the interval </p>
<p> The limits are set to interval [0.0, -1.0] </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h3><code>QwtInterval</code> QwtInterval::inverted () const</h3>
<p>Invert the limits of the interval </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Inverted interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>normalized()</code></dl>
<h3>bool QwtInterval::isNull () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true, if <code>isValid()</code> &amp;&amp; (<code>minValue()</code> &gt;= <code>maxValue()</code>)</dl>
<h3>bool QwtInterval::isValid () const [inline]</h3>
<p>A interval is valid when <code>minValue()</code> &lt;= <code>maxValue()</code>. In case of <code>QwtInterval::ExcludeBorders</code> it is true when <code>minValue()</code> &lt; <code>maxValue()</code> </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the interval is valid</dl>
<h3><code>QwtInterval</code> QwtInterval::limited (doublelowerBound, doubleupperBound) const</h3>
<p>Limit the interval, keeping the border modes </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> Lower limit<br />
 <i>upperBound</i> Upper limit</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Limited interval</dl>
<h3>double QwtInterval::maxValue () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Upper limit of the interval</dl>
<h3>double QwtInterval::minValue () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Lower limit of the interval</dl>
<h3><code>QwtInterval</code> QwtInterval::normalized () const</h3>
<p>Normalize the limits of the interval. If <code>maxValue()</code> &lt; <code>minValue()</code> the limits will be inverted. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Normalized interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code>, <code>inverted()</code></dl>
<h3>bool QwtInterval::operator!= (const <code>QwtInterval</code> &amp;other) const [inline]</h3>
<p>Compare two intervals. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to compare with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when this and other are not equal</dl>
<h3><code>QwtInterval</code> QwtInterval::operator&amp; (const <code>QwtInterval</code> &amp;other) const [inline]</h3>
<p>Intersection of two intervals. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to intersect with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Intersection of this and other</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>intersect()</code></dl>
<h3><code>QwtInterval</code> &amp; QwtInterval::operator&amp;= (const <code>QwtInterval</code> &amp;other)</h3>
<p>Intersect this interval with the given interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to be intersected with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This interval</dl>
<h3>bool QwtInterval::operator== (const <code>QwtInterval</code> &amp;other) const [inline]</h3>
<p>Compare two intervals. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to compare with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when this and other are equal</dl>
<h3><code>QwtInterval</code> QwtInterval::operator| (const <code>QwtInterval</code> &amp;other) const [inline]</h3>
<p>Union of two intervals </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to unite with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Union of this and other</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>unite()</code></dl>
<h3><code>QwtInterval</code> QwtInterval::operator| (doublevalue) const [inline]</h3>
<p>Extend an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Extended interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>extend()</code></dl>
<h3><code>QwtInterval</code> &amp; QwtInterval::operator|= (const <code>QwtInterval</code> &amp;other)</h3>
<p>Unite this interval with the given interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Interval to be united with</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This interval</dl>
<h3><code>QwtInterval</code> &amp; QwtInterval::operator|= (doublevalue)</h3>
<p>Extend an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Reference of the extended interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>extend()</code></dl>
<h3>void QwtInterval::setBorderFlags (<code>BorderFlags</code>borderFlags) [inline]</h3>
<p>Change the border flags </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>borderFlags</i> Or&#8217;d BorderMode flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderFlags()</code></dl>
<h3>void QwtInterval::setInterval (doubleminValue, doublemaxValue, <code>BorderFlags</code>borderFlags = <code>IncludeBorders</code>) [inline]</h3>
<p>Assign the limits of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value<br />
 <i>maxValue</i> Maximum value<br />
 <i>borderFlags</i> Include/Exclude borders</dl>
<h3>void QwtInterval::setMaxValue (doublemaxValue) [inline]</h3>
<p>Assign the upper limit of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxValue</i> Maximum value</dl>
<h3>void QwtInterval::setMinValue (doubleminValue) [inline]</h3>
<p>Assign the lower limit of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value</dl>
<h3><code>QwtInterval</code> QwtInterval::symmetrize (doublevalue) const</h3>
<p>Adjust the limit that is closer to value, so that value becomes the center of the interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Center</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval with value as center</dl>
<h3>double QwtInterval::width () const [inline]</h3>
<p>Return the width of an interval. The width of invalid intervals is 0.0, otherwise the result is <code>maxValue()</code> &#8211; <code>minValue()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
