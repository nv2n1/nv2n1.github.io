---
title: "tzset(3)"
name: "tzset"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tzset/"
description: "tzset, tzname, timezone, daylight – initialize time conversion information"
---

<p>tzset, tzname, timezone, daylight &#8211; initialize time conversion information</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;time.h&gt;

void tzset(void);

extern char *tzname[2];
extern long timezone;
extern int daylight;</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>tzset</code>(): _POSIX_C_SOURCE<br />
 <i>tzname</i>: _POSIX_C_SOURCE<br />
 <i>timezone</i>, <i>daylight</i>: _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>tzset</code>() function initializes the <i>tzname</i> variable from the <code>TZ</code> environment variable. This function is automatically called by the other time conversion functions that depend on the timezone. In a System-V-like environment, it will also set the variables <i>timezone</i> (seconds West of UTC) and <i>daylight</i> (to 0 if this timezone does not have any daylight saving time rules, or to nonzero if there is a time, past, present or future when daylight saving time applies). If the <code>TZ</code> variable does not appear in the environment, the system timezone is used. The system timezone is configured by copying, or linking, a file in the <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5) format to <i>/etc/localtime</i>. A timezone database of these files may be located in the system timezone directory (see the <code>FILES</code> section below). If the <code>TZ</code> variable does appear in the environment, but its value is empty, or its value cannot be interpreted using any of the formats specified below, then Coordinated Universal Time (UTC) is used. The value of <code>TZ</code> can be one of two formats. The first format is a string of characters that directly represent the timezone to be used: <i>std offset</i>[<i>dst</i>[<i>offset</i>][,<i>start</i>[<i>/time</i>],<i>end</i>[<i>/time</i>]]] There are no spaces in the specification. The <i>std</i> string specifies an abbreviation for the timezone and must be three or more alphabetic characters. When enclosed between the less-than (&lt;) and greater-than (&gt;) signs, the characters set is expanded to include the plus (+) sign, the minus (-) sign, and digits. The <i>offset</i> string immediately follows <i>std</i> and specifies the time value to be added to the local time to get Coordinated Universal Time (UTC). The <i>offset</i> is positive if the local timezone is west of the Prime Meridian and negative if it is east. The hour must be between 0 and 24, and the minutes and seconds 00 and 59: [<i>+</i>|<i>&#8211;</i>]<i>hh</i>[<i>:mm</i>[<i>:ss</i>]] The <i>dst</i> string and <i>offset</i> specify the name and offset for the corresponding daylight saving timezone. If the offset is omitted, it defaults to one hour ahead of standard time. The <i>start</i> field specifies when daylight saving time goes into effect and the <i>end</i> field specifies when the change is made back to standard time. These fields may have the following formats:</p>
<dl>
<dt>J<i>n</i></p>
<dd>This specifies the Julian day with <i>n</i> between 1 and 365. Leap days are not counted. In this format, February 29 can&#8217;t be represented; February 28 is day 59, and March 1 is always day 60.</p>
<dt><i>n</i></p>
<dd>This specifies the zero-based Julian day with <i>n</i> between 0 and 365. February 29 is counted in leap years.</p>
<dt>M<i>m</i>.<i>w</i>.<i>d</i></p>
<dd>This specifies day <i>d</i> (0 &lt;= <i>d</i> &lt;= 6) of week <i>w</i> (1 &lt;= <i>w</i> &lt;= 5) of month <i>m</i> (1 &lt;= <i>m</i> &lt;= 12). Week 1 is the first week in which day <i>d</i> occurs and week 5 is the last week in which day <i>d</i> occurs. Day 0 is a Sunday.</dl>
<p> The <i>time</i> fields specify when, in the local time currently in effect, the change to the other time occurs. If omitted, the default is 02:00:00. Here is an example for New Zealand, where the standard time (NZST) is 12 hours ahead of UTC, and daylight saving time (NZDT), 13 hours ahead of UTC, runs from the first Sunday in October to the third Sunday in March, and the changeovers happen at the default time of 02:00:00: TZ=&quot;:Pacific/Auckland&quot; The second format specifies that the timezone information should be read from a file: :[filespec] If the file specification <i>filespec</i> is omitted, or its value cannot be interpreted, then Coordinated Universal Time (UTC) is used. If <i>filespec</i> is given, it specifies another <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5)-format file to read the timezone information from. If <i>filespec</i> does not begin with a &#8216;/&#8217;, the file specification is relative to the system timezone directory. If the colon is omitted each of the above <code>TZ</code> formats will be tried. Here&#8217;s an example, once more for New Zealand: </p>
<pre><code>TZ=&quot;:Pacific/Auckland&quot;</code></pre>
<h2>Environment</h2>
<dl>
<dt><code>TZ</code></p>
<dd>If this variable is set its value takes precedence over the system configured timezone.</p>
<dt><code>TZDIR</code></p>
<dd>If this variable is set its value takes precedence over the system configured timezone database directory path.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/localtime</i></p>
<dd>The system timezone file.</p>
<dt><i>/usr/share/zoneinfo/</i></p>
<dd>The system timezone database directory.</p>
<dt><i>/usr/share/zoneinfo/posixrules</i></p>
<dd>When a TZ string includes a dst timezone without anything following it, then this file is used for the start/end rules. It is in the <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5) format. By default, the zoneinfo Makefile hard links it to the <i>America/New_York</i> tzfile.</dl>
<p> Above are the current standard file locations, but they are configurable when glibc is compiled.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>tzset</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>4.3BSD had a function <code>char *timezone(</code><i>zone</i><code>, </code><i>dst</i><code>)</code> that returned the name of the timezone corresponding to its first argument (minutes West of UTC). If the second argument was 0, the standard name was used, otherwise the daylight saving time version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
