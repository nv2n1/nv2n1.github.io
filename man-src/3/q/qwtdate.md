---
title: "qwtdate(3)"
name: "qwtdate"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdate/"
description: "QwtDate –"
---

<p>QwtDate &#8211; </p>
<p> A collection of methods around date/time values.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_date.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Week0Type</code> { <code>FirstThursday</code>, <code>FirstDay</code> } </p>
<p> enum <code>IntervalType</code> { <code>Millisecond</code>, <code>Second</code>, <code>Minute</code>, <code>Hour</code>, <code>Day</code>, <code>Week</code>, <code>Month</code>, <code>Year</code> } </p>
<p> enum { <code>JulianDayForEpoch</code> = 2440588 } </p>
<h3>Static Public Member Functions</h3>
<p>static QDate <code>minDate</code> () </p>
<p> static QDate <code>maxDate</code> () </p>
<p> static QDateTime <code>toDateTime</code> (double value, Qt::TimeSpec=Qt::UTC) </p>
<p> static double <code>toDouble</code> (const QDateTime &amp;) </p>
<p> static QDateTime <code>ceil</code> (const QDateTime &amp;, <code>IntervalType</code>) </p>
<p> static QDateTime <code>floor</code> (const QDateTime &amp;, <code>IntervalType</code>) </p>
<p> static QDate <code>dateOfWeek0</code> (int year, <code>Week0Type</code>)<br />
 <i>Date of the first day of the first week for a year. </i><br />
 static int <code>weekNumber</code> (const QDate &amp;, <code>Week0Type</code>) </p>
<p> static int <code>utcOffset</code> (const QDateTime &amp;) </p>
<p> static QString <code>toString</code> (const QDateTime &amp;, const QString &amp;format, <code>Week0Type</code>) </p>
<h2>Detailed Description</h2>
<p>A collection of methods around date/time values. </p>
<p> Qt offers convenient classes for dealing with date/time values, but Qwt uses coordinate systems that are based on doubles. <code>QwtDate</code> offers methods to translate from QDateTime to double and v.v. </p>
<p> A double is interpreted as the number of milliseconds since 1970-01-01T00:00:00 Universal Coordinated Time &#8211; also known as &#8216;The Epoch&#8217;. </p>
<p> While the range of the Julian day in Qt4 is limited to [0, MAX_INT], Qt5 stores it as qint64 offering a huge range of valid dates. As the significance of a double is below this ( assuming a fraction of 52 bits ) the translation is not bijective with rounding errors for dates very far from Epoch. For a resolution of 1 ms those start to happen for dates above the year 144683. </p>
<p> An axis for a date/time interval is expected to be aligned and divided in time/date units like seconds, minutes, &#8230; <code>QwtDate</code> offers several algorithms that are needed to calculate these axes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDateScaleEngine</code>, <code>QwtDateScaleDraw</code>, QDate, QTime</dl>
<h2>Member Enumeration Documentation</h2>
<h3>anonymous enum</h3>
<p><code>Enumerator</code></p>
<dl COMPACT>
<dt><i>JulianDayForEpoch </i></p>
<dd>The Julian day of &#8216;The Epoch&#8217;.</dl>
<h3>enum <code>QwtDate::IntervalType</code></h3>
<p>Classification of an time interval </p>
<p> Time intervals needs to be classified to decide how to align and divide it. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Millisecond </i></p>
<dd>The interval is related to milliseconds.</p>
<dt><i>Second </i></p>
<dd>The interval is related to seconds.</p>
<dt><i>Minute </i></p>
<dd>The interval is related to minutes.</p>
<dt><i>Hour </i></p>
<dd>The interval is related to hours.</p>
<dt><i>Day </i></p>
<dd>The interval is related to days.</p>
<dt><i>Week </i></p>
<dd>The interval is related to weeks.</p>
<dt><i>Month </i></p>
<dd>The interval is related to months.</p>
<dt><i>Year </i></p>
<dd>The interval is related to years.</dl>
<h3>enum <code>QwtDate::Week0Type</code></h3>
<p>How to identify the first week of year differs between countries. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>FirstThursday </i></p>
<dd>According to ISO 8601 the first week of a year is defined as &#8216;the week with the year&#8217;s first Thursday in it&#8217;.</dl>
<p> FirstThursday corresponds to the numbering that is implemented in QDate::weekNumber().</p>
<dl COMPACT>
<dt><i>FirstDay </i></p>
<dd></dl>
<p> In the U.S. this definition is more common than FirstThursday.</p>
<h2>Member Function Documentation</h2>
<h3>QDateTime QwtDate::ceil (const QDateTime &amp;dateTime, <code>IntervalType</code>intervalType) [static]</h3>
<p>Ceil a datetime according the interval type </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value<br />
 <i>intervalType</i> Interval type, how to ceil. F.e. when intervalType = QwtDate::Months, the result will be ceiled to the next beginning of a month</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Ceiled datetime</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>floor()</code></dl>
<h3>QDate QwtDate::dateOfWeek0 (intyear, <code>Week0Type</code>type) [static]</h3>
<p>Date of the first day of the first week for a year. The first day of a week depends on the current locale ( QLocale::firstDayOfWeek() ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>year</i> Year<br />
 <i>type</i> Option how to identify the first week</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>First day of week 0</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QLocale::firstDayOfWeek(), <code>weekNumber()</code></dl>
<h3>QDateTime QwtDate::floor (const QDateTime &amp;dateTime, <code>IntervalType</code>intervalType) [static]</h3>
<p>Floor a datetime according the interval type </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value<br />
 <i>intervalType</i> Interval type, how to ceil. F.e. when intervalType = QwtDate::Months, the result will be ceiled to the next beginning of a month</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Floored datetime</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>floor()</code></dl>
<h3>QDate QwtDate::maxDate () [static]</h3>
<p>Maximum for the supported date range </p>
<p> The range of valid dates depends on how QDate stores the Julian day internally. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>For Qt4 it is &#8216;Tue Jun 3 5874898&#8217;</p>
<dt>&bull;</p>
<dd>For Qt5 it is &#8216;Tue Dec 31 2147483647&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>maximum of the date range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minDate()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The maximum differs between Qt4 and Qt5</dl>
<h3>QDate QwtDate::minDate () [static]</h3>
<p>Minimum for the supported date range </p>
<p> The range of valid dates depends on how QDate stores the Julian day internally. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>For Qt4 it is &#8216;Tue Jan 2 -4713&#8217;</p>
<dt>&bull;</p>
<dd>For Qt5 it is &#8216;Thu Jan 1 -2147483648&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>minimum of the date range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxDate()</code></dl>
<h3>QDateTime QwtDate::toDateTime (doublevalue, Qt::TimeSpectimeSpec = Qt::UTC) [static]</h3>
<p>Translate from double to QDateTime </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Number of milliseconds since the epoch, 1970-01-01T00:00:00 UTC<br />
 <i>timeSpec</i> Time specification</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Datetime value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>toDouble()</code>, QDateTime::setMSecsSinceEpoch()</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The return datetime for Qt::OffsetFromUTC will be Qt::UTC</dl>
<h3>double QwtDate::toDouble (const QDateTime &amp;dateTime) [static]</h3>
<p>Translate from QDateTime to double </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of milliseconds since 1970-01-01T00:00:00 UTC has passed.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>toDateTime()</code>, QDateTime::toMSecsSinceEpoch()</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>For values very far below or above 1970-01-01 UTC rounding errors will happen due to the limited significance of a double.</dl>
<h3>QString QwtDate::toString (const QDateTime &amp;dateTime, const QString &amp;format, <code>Week0Type</code>week0Type) [static]</h3>
<p>Translate a datetime into a string </p>
<p> Beside the format expressions documented in QDateTime::toString() the following expressions are supported: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>w </p>
<p>&nbsp;<wbr>week number:&nbsp;<wbr>(&nbsp;<wbr>1 &#8211; 53&nbsp;<wbr>)</p>
<dt>&bull;</p>
<dd>ww </p>
<p>&nbsp;<wbr>week number with a leading zero&nbsp;<wbr>(&nbsp;<wbr>01 &#8211; 53&nbsp;<wbr>)</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value<br />
 <i>format</i> Format string<br />
 <i>week0Type</i> Specification of week 0</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Datetime string</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QDateTime::toString(), <code>weekNumber()</code>, <code>QwtDateScaleDraw</code></dl>
<h3>int QwtDate::utcOffset (const QDateTime &amp;dateTime) [static]</h3>
<p>Offset in seconds from Coordinated Universal Time </p>
<p> The offset depends on the time specification of dateTime: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Qt::UTC 0, dateTime has no offset</p>
<dt>&bull;</p>
<dd>Qt::OffsetFromUTC returns dateTime.utcOffset()</p>
<dt>&bull;</p>
<dd>Qt::LocalTime: number of seconds from the UTC</dl>
<p> For Qt::LocalTime the offset depends on the timezone and daylight savings. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dateTime</i> Datetime value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Offset in seconds</dl>
<h3>int QwtDate::weekNumber (const QDate &amp;date, <code>Week0Type</code>type) [static]</h3>
<p>Find the week number of a date </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtDate::FirstThursday</code> </p>
<p>&nbsp;<wbr>Corresponding to ISO 8601&nbsp;<wbr>(&nbsp;<wbr>see QDate::weekNumber()&nbsp;<wbr>).</p>
<dt>&bull;</p>
<dd><code>QwtDate::FirstDay</code> </p>
<p>&nbsp;<wbr>Number of weeks that have begun since&nbsp;<wbr><code>dateOfWeek0()</code>.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>date</i> Date<br />
 <i>type</i> Option how to identify the first week</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Week number, starting with 1</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
