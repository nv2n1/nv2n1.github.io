---
title: "qwtdatescaledraw(3)"
name: "qwtdatescaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdatescaledraw/"
description: "QwtDateScaleDraw –"
---

<p>QwtDateScaleDraw &#8211; </p>
<p> A class for drawing datetime scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_date_scale_draw.h&gt; </p>
<p> Inherits <code>QwtScaleDraw</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtDateScaleDraw</code> (Qt::TimeSpec=Qt::LocalTime)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtDateScaleDraw</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setDateFormat</code> (<code>QwtDate::IntervalType</code>, const QString &amp;) </p>
<p> QString <code>dateFormat</code> (<code>QwtDate::IntervalType</code>) const </p>
<p> void <code>setTimeSpec</code> (Qt::TimeSpec) </p>
<p> Qt::TimeSpec <code>timeSpec</code> () const </p>
<p> void <code>setUtcOffset</code> (int seconds) </p>
<p> int <code>utcOffset</code> () const </p>
<p> void <code>setWeek0Type</code> (<code>QwtDate::Week0Type</code>) </p>
<p> <code>QwtDate::Week0Type</code> <code>week0Type</code> () const </p>
<p> virtual <code>QwtText</code> <code>label</code> (double) const<br />
 <i>Convert a value into its representing label. </i><br />
 QDateTime <code>toDateTime</code> (double) const </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>QwtDate::IntervalType</code> <code>intervalType</code> (const <code>QwtScaleDiv</code> &amp;) const </p>
<p> virtual QString <code>dateFormatOfDate</code> (const QDateTime &amp;, <code>QwtDate::IntervalType</code>) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A class for drawing datetime scales. </p>
<p> <code>QwtDateScaleDraw</code> displays values as datetime labels. The format of the labels depends on the alignment of the major tick labels. </p>
<p> The default format strings are: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Millisecond </p>
<p>&nbsp;<wbr>&#8216;hh:mm:ss:zzz
ddd dd MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Second </p>
<p>&nbsp;<wbr>&#8216;hh:mm:ss
ddd dd MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Minute </p>
<p>&nbsp;<wbr>&#8216;hh:mm
ddd dd MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Hour </p>
<p>&nbsp;<wbr>&#8216;hh:mm
ddd dd MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Day </p>
<p>&nbsp;<wbr>&#8216;ddd dd MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Week </p>
<p>&nbsp;<wbr>&#8216;Www yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Month </p>
<p>&nbsp;<wbr>&#8216;MMM yyyy&#8217;</p>
<dt>&bull;</p>
<dd>Year </p>
<p>&nbsp;<wbr>&#8216;yyyy&#8217;</dl>
<p> The format strings can be modified using <code>setDateFormat()</code> or individually for each tick label by overloading <code>dateFormatOfDate()</code>, </p>
<p> Usually <code>QwtDateScaleDraw</code> is used in combination with <code>QwtDateScaleEngine</code>, that calculates scales for datetime intervals. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDateScaleEngine</code>, <code>QwtPlot::setAxisScaleDraw()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDateScaleDraw::QwtDateScaleDraw (Qt::TimeSpectimeSpec = Qt::LocalTime)</h3>
<p>Constructor. The default setting is to display tick labels for the given time specification. The first week of a year is defined like for <code>QwtDate::FirstThursday</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeSpec</i> Time specification</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTimeSpec()</code>, <code>setWeek0Type()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QString QwtDateScaleDraw::dateFormat (<code>QwtDate::IntervalType</code>intervalType) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervalType</i> Interval type</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Default format string for an datetime interval type</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDateFormat()</code>, <code>dateFormatOfDate()</code></dl>
<h3>QString QwtDateScaleDraw::dateFormatOfDate (const QDateTime &amp;dateTime, <code>QwtDate::IntervalType</code>intervalType) const [protected], [virtual]</h3>
<p>Format string for the representation of a datetime </p>
<p> <code>dateFormatOfDate()</code> is intended to be overloaded for situations, where formats are individual for specific datetime values. </p>
<p> The default setting ignores dateTime and return the default format for the interval type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value<br />
 <i>intervalType</i> Interval type</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Format string</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDateFormat()</code>, <code>QwtDate::toString()</code></dl>
<h3><code>QwtDate::IntervalType</code> QwtDateScaleDraw::intervalType (const <code>QwtScaleDiv</code> &amp;scaleDiv) const [protected], [virtual]</h3>
<p>Find the less detailed datetime unit, where no rounding errors happen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale division</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval type</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>dateFormatOfDate()</code></dl>
<h3><code>QwtText</code> QwtDateScaleDraw::label (doublevalue) const [virtual]</h3>
<p>Convert a value into its representing label. The value is converted to a datetime value using <code>toDateTime()</code> and converted to a plain text using <code>QwtDate::toString()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Label string.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>dateFormatOfDate()</code></dl>
<p> Reimplemented from <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtDateScaleDraw::setDateFormat (<code>QwtDate::IntervalType</code>intervalType, const QString &amp;format)</h3>
<p>Set the default format string for an datetime interval type </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervalType</i> Interval type<br />
 <i>format</i> Default format string</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>dateFormat()</code>, <code>dateFormatOfDate()</code>, <code>QwtDate::toString()</code></dl>
<h3>void QwtDateScaleDraw::setTimeSpec (Qt::TimeSpectimeSpec)</h3>
<p>Set the time specification used for the tick labels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeSpec</i> Time specification</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>timeSpec()</code>, <code>setUtcOffset()</code>, <code>toDateTime()</code></dl>
<h3>void QwtDateScaleDraw::setUtcOffset (intseconds)</h3>
<p>Set the offset in seconds from Coordinated Universal Time </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>seconds</i> Offset in seconds</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The offset has no effect beside for the time specification Qt::OffsetFromUTC.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QDate::utcOffset(), <code>setTimeSpec()</code>, <code>toDateTime()</code></dl>
<h3>void QwtDateScaleDraw::setWeek0Type (<code>QwtDate::Week0Type</code>week0Type)</h3>
<p>Sets how to identify the first week of a year. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>week0Type</i> Mode how to identify the first week of a year</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>week0Type()</code>.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>week0Type has no effect beside for intervals classified as <code>QwtDate::Week</code>.</dl>
<h3>Qt::TimeSpec QwtDateScaleDraw::timeSpec () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Time specification used for the tick labels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTimeSpec()</code>, <code>utcOffset()</code>, <code>toDateTime()</code></dl>
<h3>QDateTime QwtDateScaleDraw::toDateTime (doublevalue) const</h3>
<p>Translate a double value into a QDateTime object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>QDateTime object initialized with <code>timeSpec()</code> and <code>utcOffset()</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>timeSpec()</code>, <code>utcOffset()</code>, <code>QwtDate::toDateTime()</code></dl>
<h3>int QwtDateScaleDraw::utcOffset () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Offset in seconds from Coordinated Universal Time</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The offset has no effect beside for the time specification Qt::OffsetFromUTC.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QDate::setUtcOffset(), <code>setTimeSpec()</code>, <code>toDateTime()</code></dl>
<h3><code>QwtDate::Week0Type</code> QwtDateScaleDraw::week0Type () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Setting how to identify the first week of a year.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWeek0Type()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
