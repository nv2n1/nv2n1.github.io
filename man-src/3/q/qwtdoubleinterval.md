---
title: "qwtdoubleinterval(3)"
name: "qwtdoubleinterval"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdoubleinterval/"
description: "QwtDoubleInterval – A class representing an interval."
---

<p>QwtDoubleInterval &#8211; A class representing an interval. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_double_interval.h">qwt_double_interval.h</a>&gt; </p>
<h3>Public Types</h3>
<p>enum <code>BorderMode</code> { <code>IncludeBorders</code> = 0, <code>ExcludeMinimum</code> = 1, <code>ExcludeMaximum</code> = 2, <code>ExcludeBorders</code> = ExcludeMinimum | ExcludeMaximum } </p>
<h3>Public Member Functions</h3>
<p><code>QwtDoubleInterval</code> () </p>
<p> <code>QwtDoubleInterval</code> (double minValue, double maxValue, int borderFlags=IncludeBorders) </p>
<p> void <code>setInterval</code> (double minValue, double maxValue, int borderFlags=IncludeBorders) </p>
<p> <code>QwtDoubleInterval</code> <code>normalized</code> () const </p>
<p> <code>QwtDoubleInterval</code> <code>inverted</code> () const </p>
<p> <code>QwtDoubleInterval</code> <code>limited</code> (double minValue, double maxValue) const </p>
<p> int <code>operator==</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> int <code>operator!=</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> void <code>setBorderFlags</code> (int) </p>
<p> int <code>borderFlags</code> () const </p>
<p> double <code>minValue</code> () const </p>
<p> double <code>maxValue</code> () const </p>
<p> double <code>width</code> () const </p>
<p> void <code>setMinValue</code> (double) </p>
<p> void <code>setMaxValue</code> (double) </p>
<p> bool <code>contains</code> (double value) const </p>
<p> bool <code>intersects</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> <code>intersect</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> <code>unite</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> <code>operator|</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> <code>operator&amp;</code> (const <code>QwtDoubleInterval</code> &amp;) const </p>
<p> <code>QwtDoubleInterval</code> &amp; <code>operator|=</code> (const <code>QwtDoubleInterval</code> &amp;) </p>
<p> <code>QwtDoubleInterval</code> &amp; <code>operator&amp;=</code> (const <code>QwtDoubleInterval</code> &amp;) </p>
<p> <code>QwtDoubleInterval</code> <code>extend</code> (double value) const </p>
<p> <code>QwtDoubleInterval</code> <code>operator|</code> (double) const </p>
<p> <code>QwtDoubleInterval</code> &amp; <code>operator|=</code> (double) </p>
<p> bool <code>isValid</code> () const </p>
<p> bool <code>isNull</code> () const </p>
<p> void <code>invalidate</code> () </p>
<p> <code>QwtDoubleInterval</code> <code>symmetrize</code> (double value) const </p>
<h2>Detailed Description</h2>
<p>A class representing an interval. </p>
<p> The interval is represented by 2 doubles, the lower and the upper limit.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtDoubleInterval::BorderMode</code></h3>
<p>Flag indicating if a border is included/excluded from an interval </p>
<dl COMPACT>
<dt>*</p>
<dd>IncludeBorders </p>
<p>&nbsp;<wbr>min/max values are inside the interval</p>
<dt>*</p>
<dd>ExcludeMinimum </p>
<p>&nbsp;<wbr>min value is not included in the interval</p>
<dt>*</p>
<dd>ExcludeMaximum </p>
<p>&nbsp;<wbr>max value is not included in the interval</p>
<dt>*</p>
<dd>ExcludeBorders </p>
<p>&nbsp;<wbr>min/max values are not included in the interval</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>setBorderMode(), testBorderMode()</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDoubleInterval::QwtDoubleInterval () [inline]</h3>
<p>Default Constructor. </p>
<p> Creates an invalid interval [0.0, -1.0] </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code>, <code>isValid()</code></dl>
<h3>QwtDoubleInterval::QwtDoubleInterval (double minValue, double maxValue, int borderFlags = IncludeBorders) [inline]</h3>
<p>Constructor </p>
<p> Build an interval with from min/max values </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value<br />
 <i>maxValue</i> Maximum value<br />
 <i>borderFlags</i> Include/Exclude borders</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtDoubleInterval::borderFlags () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Border flags</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setBorderFlags()</code></dl>
<h3>bool QwtDoubleInterval::contains (double value) const</h3>
<p>Test if a value is inside an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if value &gt;= <code>minValue()</code> &amp;&amp; value &lt;= <code>maxValue()</code></dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::extend (double value) const</h3>
<p>Extend the interval </p>
<p> If value is below minValue, value becomes the lower limit. If value is above maxValue, value becomes the upper limit. </p>
<p> extend has no effect for invalid intervals </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::intersect (const <code>QwtDoubleInterval</code> &amp; other) const</h3>
<p>Intersect 2 intervals. </p>
<h3>bool QwtDoubleInterval::intersects (const <code>QwtDoubleInterval</code> &amp; other) const</h3>
<p>Test if two intervals overlap</p>
<h3>void QwtDoubleInterval::invalidate () [inline]</h3>
<p>Invalidate the interval </p>
<p> The limits are set to interval [0.0, -1.0] </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::inverted () const</h3>
<p>Invert the limits of the interval </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Inverted interval</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>normalized()</code></dl>
<h3>bool QwtDoubleInterval::isNull () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true, if <code>isValid()</code> &amp;&amp; (<code>minValue()</code> &gt;= <code>maxValue()</code>)</dl>
<h3>bool QwtDoubleInterval::isValid () const [inline]</h3>
<p>A interval is valid when <code>minValue()</code> &lt;= <code>maxValue()</code>. In case of QwtDoubleInterval::ExcludeBorders it is true when <code>minValue()</code> &lt; <code>maxValue()</code></p>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::limited (double lowerBound, double upperBound) const</h3>
<p>Limit the interval, keeping the border modes </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> Lower limit<br />
 <i>upperBound</i> Upper limit</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Limited interval</dl>
<h3>double QwtDoubleInterval::maxValue () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Upper limit of the interval</dl>
<h3>double QwtDoubleInterval::minValue () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Lower limit of the interval</dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::normalized () const</h3>
<p>Normalize the limits of the interval. </p>
<p> If <code>maxValue()</code> &lt; <code>minValue()</code> the limits will be inverted. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Normalized interval</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code>, <code>inverted()</code></dl>
<h3>int QwtDoubleInterval::operator!= (const <code>QwtDoubleInterval</code> &amp; other) const [inline]</h3>
<p>Compare two intervals. </p>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::operator&amp; (const <code>QwtDoubleInterval</code> &amp; interval) const [inline]</h3>
<p>Intersection of two intervals </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>intersect()</code></dl>
<h3><code>QwtDoubleInterval</code> &amp; QwtDoubleInterval::operator&amp;= (const <code>QwtDoubleInterval</code> &amp; interval)</h3>
<p>Intersects this interval with the given interval. </p>
<h3>int QwtDoubleInterval::operator== (const <code>QwtDoubleInterval</code> &amp; other) const [inline]</h3>
<p>Compare two intervals. </p>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::operator| (double value) const [inline]</h3>
<p>Extend an interval </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>extend()</code></dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::operator| (const <code>QwtDoubleInterval</code> &amp; interval) const [inline]</h3>
<p>Union of two intervals </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>unite()</code></dl>
<h3><code>QwtDoubleInterval</code> &amp; QwtDoubleInterval::operator|= (const <code>QwtDoubleInterval</code> &amp; interval)</h3>
<p>Unites this interval with the given interval. </p>
<h3>void QwtDoubleInterval::setBorderFlags (int borderFlags) [inline]</h3>
<p>Change the border flags </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>borderFlags</i> Or&#8217;d BorderMode flags</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>borderFlags()</code></dl>
<h3>void QwtDoubleInterval::setInterval (double minValue, double maxValue, int borderFlags = IncludeBorders) [inline]</h3>
<p>Assign the limits of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value<br />
 <i>maxValue</i> Maximum value<br />
 <i>borderFlags</i> Include/Exclude borders</dl>
<h3>void QwtDoubleInterval::setMaxValue (double maxValue) [inline]</h3>
<p>Assign the upper limit of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxValue</i> Maximum value</dl>
<h3>void QwtDoubleInterval::setMinValue (double minValue) [inline]</h3>
<p>Assign the lower limit of the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minValue</i> Minimum value</dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::symmetrize (double value) const</h3>
<p>Adjust the limit that is closer to value, so that value becomes the center of the interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Center</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval with value as center</dl>
<h3><code>QwtDoubleInterval</code> QwtDoubleInterval::unite (const <code>QwtDoubleInterval</code> &amp; other) const</h3>
<p>Unite 2 intervals. </p>
<h3>double QwtDoubleInterval::width () const [inline]</h3>
<p>Return the width of an interval The width of invalid intervals is 0.0, otherwise the result is <code>maxValue()</code> &#8211; <code>minValue()</code>. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
