---
title: "zdump(8)"
name: "zdump"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zdump/"
description: "zdump – timezone dumper"
---

<p>zdump &#8211; timezone dumper</p>
<h2>Synopsis</h2>
<p><code>zdump</code> [ <i>option</i> &#8230; ] [ <i>timezone</i> &#8230; ]</p>
<h2>Description</h2>
<p>ds &#8211; &#8211; The <code>zdump</code> program prints the current time in each <i>timezone</i> named on the command line.</p>
<h2>Options</h2>
<dl>
<dt><code>version</code></p>
<dd>Output version information and exit.</p>
<dt><code>help</code></p>
<dd>Output short usage message and exit.</p>
<dt><code>i</code></p>
<dd>Output a description of time intervals. For each <i>timezone</i> on the command line, output an interval-format description of the timezone. See below.</p>
<dt><code>v</code></p>
<dd>Output a verbose description of time intervals. For each <i>timezone</i> on the command line, print the time at the lowest possible time value, the time one day after the lowest possible time value, the times both one second before and exactly at each detected time discontinuity, the time at one day less than the highest possible time value, and the time at the highest possible time value. Each line is followed by <code>isdst=</code><i>D</i> where <i>D</i> is positive, zero, or negative depending on whether the given time is daylight saving time, standard time, or an unknown time type, respectively. Each line is also followed by <code>gmtoff=</code><i>N</i> if the given local time is known to be <i>N</i> seconds east of Greenwich.</p>
<dt><code>V</code></p>
<dd>Like <code>v</code>, except omit the times relative to the extreme time values. This generates output that is easier to compare to that of implementations with different time representations.</p>
<dt><code>c </code><i></i>[<i>loyear</i><code>,</code><i></i>]<i>hiyear</i></p>
<dd>Cut off interval output at the given year(s). Cutoff times are computed using the proleptic Gregorian calendar with year 0 and with Universal Time (UT) ignoring leap seconds. Cutoffs are at the start of each year, where the lower-bound timestamp is exclusive and the upper is inclusive; for example, <code>c 1970,2070</code> selects transitions after 1970-01-01 00:00:00 UTC and on or before 2070-01-01 00:00:00 UTC. The default cutoff is <code>500,2500</code>.</p>
<dt><code>t </code><i></i>[<i>lotime</i><code>,</code><i></i>]<i>hitime</i></p>
<dd>Cut off interval output at the given time(s), given in decimal seconds since 1970-01-01 00:00:00 Coordinated Universal Time (UTC). The <i>timezone</i> determines whether the count includes leap seconds. As with <code>c</code>, the cutoff&#8217;s lower bound is exclusive and its upper bound is inclusive.</dl>
<h2>Interval Format</h2>
<p>The interval format is a compact text representation that is intended to be both human- and machine-readable. It consists of an empty line, then a line where <i>string</i> is a double-quoted string giving the timezone, a second line describing the time interval before the first transition if any, and zero or more following lines one line for each transition time and following interval. Fields are separated by single tabs. </p>
<p> Dates are in <i>yyyy</i>&#8211;<i>mm</i>&#8211;<i>dd</i> format and times are in 24-hour <i>hh</i>:<i>mm</i>:<i>ss</i> format where <i>hh</i>&lt;24. Times are in local time immediately after the transition. A time interval description consists of a UT offset in signed &plusmn;<i>hhmmss</i> format, a time zone abbreviation, and an isdst flag. An abbreviation that equals the UT offset is omitted; other abbreviations are double-quoted strings unless they consist of one or more alphabetic characters. An isdst flag is omitted for standard time, and otherwise is a decimal integer that is unsigned and positive (typically 1) for daylight saving time and negative for unknown. </p>
<p> In times and in UT offsets with absolute value less than 100 hours, the seconds are omitted if they are zero, and the minutes are also omitted if they are also zero. Positive UT offsets are east of Greenwich. The UT offset 00 denotes a UT placeholder in areas where the actual offset is unspecified; by convention, this occurs when the UT offset is zero and the time zone abbreviation begins with or is </p>
<p> In double-quoted strings, escape sequences represent unusual characters. The escape sequences are \s for space, and \&quot;, \, , 
, , 	, and  with their usual meaning in the C programming language. E.g., the double-quoted string &#8221; &quot;CET\s\&quot;\&quot;&#8221; represents the character sequence &#8221; CET &quot;\&#8221; .</p>
<p> Here is an example of the output, with the leading empty line omitted. (This example is shown with tab stops set far enough apart so that the tabbed columns line up.) </p>
<pre>TZ=&quot;Pacific/Honolulu&quot;
- - -103126 LMT
1896-01-13 12:01:26 -1030 HST
1933-04-30 03 -0930 HDT 1
1933-05-21 11 -1030 HST
1942-02-09 03 -0930 HWT 1
1945-08-14 13:30 -0930 HPT 1
1945-09-30 01 -1030 HST
1947-06-08 02:30 -10 HST</pre>
<p>Here, local time begins 10 hours, 31 minutes and 26 seconds west of UT, and is a standard time abbreviated LMT. Immediately after the first transition, the date is 1896-01-13 and the time is 12:01:26, and the following time interval is 10.5 hours west of UT, a standard time abbreviated HST. Immediately after the second transition, the date is 1933-04-30 and the time is 03:00:00 and the following time interval is 9.5 hours west of UT, is abbreviated HDT, and is daylight saving time. Immediately after the last transition the date is 1947-06-08 and the time is 02:30:00, and the following time interval is 10 hours west of UT, a standard time abbreviated HST. </p>
<p> Here are excerpts from another example: </p>
<pre>TZ=&quot;Europe/Astrakhan&quot;
- - +031212 LMT
1924-04-30 23:47:48 +03
1930-06-21 01 +04
1981-04-01 01 +05 1
1981-09-30 23 +04
...
2014-10-26 01 +03
2016-03-27 03 +04</pre>
<p>This time zone is east of UT, so its UT offsets are positive. Also, many of its time zone abbreviations are omitted since they duplicate the text of the UT offset.</p>
<h2>Limitations</h2>
<p>Time discontinuities are found by sampling the results returned by localtime at twelve-hour intervals. This works in all real-world cases; one can construct artificial time zones for which this fails. </p>
<p> In the <code>v</code> and <code>V</code> output, denotes the value returned by <code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3), which uses UTC for modern timestamps and some other UT flavor for timestamps that predate the introduction of UTC. No attempt is currently made to have the output use for newer and for older timestamps, partly because the exact date of the introduction of UTC is problematic.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5), <code><a href="/docs/linux/man/8-zic/">zic</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
