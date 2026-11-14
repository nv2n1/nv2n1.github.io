---
title: "qwtdatescaleengine(3)"
name: "qwtdatescaleengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdatescaleengine/"
description: "QwtDateScaleEngine –"
---

<p>QwtDateScaleEngine &#8211; </p>
<p> A scale engine for date/time values.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_date_scale_engine.h&gt; </p>
<p> Inherits <code>QwtLinearScaleEngine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtDateScaleEngine</code> (Qt::TimeSpec=Qt::LocalTime)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtDateScaleEngine</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setTimeSpec</code> (Qt::TimeSpec) </p>
<p> Qt::TimeSpec <code>timeSpec</code> () const </p>
<p> void <code>setUtcOffset</code> (int seconds) </p>
<p> int <code>utcOffset</code> () const </p>
<p> void <code>setWeek0Type</code> (<code>QwtDate::Week0Type</code>) </p>
<p> <code>QwtDate::Week0Type</code> <code>week0Type</code> () const </p>
<p> void <code>setMaxWeeks</code> (int) </p>
<p> int <code>maxWeeks</code> () const </p>
<p> virtual void <code>autoScale</code> (int maxNumSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const </p>
<p> virtual <code>QwtScaleDiv</code> <code>divideScale</code> (double x1, double x2, int maxMajorSteps, int maxMinorSteps, double stepSize=0.0) const<br />
 <i>Calculate a scale division for a date/time interval. </i><br />
 virtual <code>QwtDate::IntervalType</code> <code>intervalType</code> (const QDateTime &amp;, const QDateTime &amp;, int maxSteps) const </p>
<p> QDateTime <code>toDateTime</code> (double) const </p>
<h3>Protected Member Functions</h3>
<p>virtual QDateTime <code>alignDate</code> (const QDateTime &amp;, double stepSize, <code>QwtDate::IntervalType</code>, bool up) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A scale engine for date/time values. </p>
<p> <code>QwtDateScaleEngine</code> builds scales from a time intervals. Together with <code>QwtDateScaleDraw</code> it can be used for axes according to date/time values. </p>
<p> Years, months, weeks, days, hours and minutes are organized in steps with non constant intervals. <code>QwtDateScaleEngine</code> classifies intervals and aligns the boundaries and tick positions according to this classification. </p>
<p> <code>QwtDateScaleEngine</code> supports representations depending on Qt::TimeSpec specifications. The valid range for scales is limited by the range of QDateTime, that differs between Qt4 and Qt5. </p>
<p> Datetime values are expected as the number of milliseconds since 1970-01-01T00:00:00 Universal Coordinated Time &#8211; also known as &#8216;The Epoch&#8217;, that can be converted to QDateTime using <code>QwtDate::toDateTime()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDate</code>, <code>QwtPlot::setAxisScaleEngine()</code>, <code>QwtAbstractScale::setScaleEngine()</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDateScaleEngine::QwtDateScaleEngine (Qt::TimeSpectimeSpec = Qt::LocalTime)</h3>
<p>Constructor. The engine is initialized to build scales for the given time specification. It classifies intervals &gt; 4 weeks as &gt;= Qt::Month. The first week of a year is defined like for <code>QwtDate::FirstThursday</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeSpec</i> Time specification</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTimeSpec()</code>, <code>setMaxWeeks()</code>, <code>setWeek0Type()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QDateTime QwtDateScaleEngine::alignDate (const QDateTime &amp;dateTime, doublestepSize, <code>QwtDate::IntervalType</code>intervalType, boolup) const [protected], [virtual]</h3>
<p>Align a date/time value for a step size </p>
<p> For Qt::Day alignments there is no &#8216;natural day 0&#8217; &#8211; instead the first day of the year is used to avoid jumping major ticks positions when panning a scale. For other alignments ( f.e according to the first day of the month ) <code>alignDate()</code> has to be overloaded. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Date/time value<br />
 <i>stepSize</i> Step size<br />
 <i>intervalType</i> Interval type<br />
 <i>up</i> When true dateTime is ceiled &#8211; otherwise it is floored</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Aligned date/time value</dl>
<h3>void QwtDateScaleEngine::autoScale (intmaxNumSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const [virtual]</h3>
<p>Align and divide an interval </p>
<p> The algorithm aligns and divides the interval into steps. </p>
<p> Datetime interval divisions are usually not equidistant and the calculated stepSize can only be used as an approximation for the steps calculated by <code>divideScale()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxNumSteps</i> Max. number of steps<br />
 <i>x1</i> First limit of the interval (In/Out)<br />
 <i>x2</i> Second limit of the interval (In/Out)<br />
 <i>stepSize</i> Step size (Out)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleEngine::setAttribute()</code></dl>
<p> Reimplemented from <code>QwtLinearScaleEngine</code>.</p>
<h3><code>QwtScaleDiv</code> QwtDateScaleEngine::divideScale (doublex1, doublex2, intmaxMajorSteps, intmaxMinorSteps, doublestepSize = 0.0) const [virtual]</h3>
<p>Calculate a scale division for a date/time interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x1</i> First interval limit<br />
 <i>x2</i> Second interval limit<br />
 <i>maxMajorSteps</i> Maximum for the number of major steps<br />
 <i>maxMinorSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size. If stepSize == 0, the scaleEngine calculates one.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated scale division</dl>
<p> Reimplemented from <code>QwtLinearScaleEngine</code>.</p>
<h3><code>QwtDate::IntervalType</code> QwtDateScaleEngine::intervalType (const QDateTime &amp;minDate, const QDateTime &amp;maxDate, intmaxSteps) const [virtual]</h3>
<p>Classification of a date/time interval division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minDate</i> Minimum ( = earlier ) of the interval<br />
 <i>maxDate</i> Maximum ( = later ) of the interval<br />
 <i>maxSteps</i> Maximum for the number of steps</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval classification</dl>
<h3>int QwtDateScaleEngine::maxWeeks () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Upper limit for the number of weeks, when an interval can be classified as Qt::Week.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaxWeeks()</code>, <code>week0Type()</code></dl>
<h3>void QwtDateScaleEngine::setMaxWeeks (intweeks)</h3>
<p>Set a upper limit for the number of weeks, when an interval can be classified as Qt::Week. </p>
<p> The default setting is 4 weeks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>weeks</i> Upper limit for the number of weeks</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>In business charts a year is often devided into weeks [1-52]</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxWeeks()</code>, <code>setWeek0Type()</code></dl>
<h3>void QwtDateScaleEngine::setTimeSpec (Qt::TimeSpectimeSpec)</h3>
<p>Set the time specification used by the engine </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>timeSpec</i> Time specification</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>timeSpec()</code>, <code>setUtcOffset()</code>, <code>toDateTime()</code></dl>
<h3>void QwtDateScaleEngine::setUtcOffset (intseconds)</h3>
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
<h3>void QwtDateScaleEngine::setWeek0Type (<code>QwtDate::Week0Type</code>week0Type)</h3>
<p>Sets how to identify the first week of a year. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>week0Type</i> Mode how to identify the first week of a year</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>week0Type()</code>, <code>setMaxWeeks()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>week0Type has no effect beside for intervals classified as <code>QwtDate::Week</code>.</dl>
<h3>Qt::TimeSpec QwtDateScaleEngine::timeSpec () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Time specification used by the engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTimeSpec()</code>, <code>utcOffset()</code>, <code>toDateTime()</code></dl>
<h3>QDateTime QwtDateScaleEngine::toDateTime (doublevalue) const</h3>
<p>Translate a double value into a QDateTime object. </p>
<p> For QDateTime result is bounded by <code>QwtDate::minDate()</code> and <code>QwtDate::maxDate()</code> </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>QDateTime object initialized with <code>timeSpec()</code> and <code>utcOffset()</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>timeSpec()</code>, <code>utcOffset()</code>, <code>QwtDate::toDateTime()</code></dl>
<h3>int QwtDateScaleEngine::utcOffset () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Offset in seconds from Coordinated Universal Time</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The offset has no effect beside for the time specification Qt::OffsetFromUTC.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QDate::setUtcOffset(), <code>setTimeSpec()</code>, <code>toDateTime()</code></dl>
<h3><code>QwtDate::Week0Type</code> QwtDateScaleEngine::week0Type () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Setting how to identify the first week of a year.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWeek0Type()</code>, <code>maxWeeks()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
