---
title: "mktime(3)"
name: "mktime"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mktime/"
description: "asctime, ctime, gmtime, localtime, mktime, asctime_r, ctime_r, gmtime_r, localtime_r – transform date and time to broken-down time or ASCII"
---

<h2 class="name">NAME</h2>
<p> asctime, ctime, gmtime, localtime, mktime, asctime_r, ctime_r, gmtime_r, localtime_r &#8211; transform date and time to broken-down time or ASCII </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;time.h&gt;
char *asctime(const struct tm *tm);
char *asctime_r(const struct tm *tm, char *buf);
char *ctime(const time_t *timep);
char *ctime_r(const time_t *timep, char *buf);
struct tm *gmtime(const time_t *timep);
struct tm *gmtime_r(const time_t *timep, struct tm *result);
struct tm *localtime(const time_t *timep);
struct tm *localtime_r(const time_t *timep, struct tm *result);
time_t mktime(struct tm *tm);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>asctime_r</code>(), <code>ctime_r</code>(), <code>gmtime_r</code>(), <code>localtime_r</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ctime</code>(), <code>gmtime</code>(), and <code>localtime</code>() functions all take an argument of data type <i>time_t</i>, which represents calendar time. When interpreted as an absolute time value, it represents the number of seconds elapsed since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). </p>
<p> The <code>asctime</code>() and <code>mktime</code>() functions both take an argument representing broken-down time, which is a representation separated into year, month, day, and so on. </p>
<p> Broken-down time is stored in the structure <i>tm</i>, which is defined in <i>&lt;time.h&gt;</i> as follows: </p>
<p> struct tm {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds&nbsp;(0-60)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_min;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Minutes&nbsp;(0-59)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_hour;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Hours&nbsp;(0-23)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_mday;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Day of the month&nbsp;(1-31)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_mon;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Month&nbsp;(0-11)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_year;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Year &#8211; 1900&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_wday;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Day of the week&nbsp;(0-6, Sunday&nbsp;=&nbsp;0)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_yday;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Day in the year&nbsp;(0-365, 1 Jan&nbsp;=&nbsp;0)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_isdst;&nbsp;<wbr>&nbsp;/*&nbsp;Daylight saving time&nbsp;*/ }; </p>
<p> The members of the <i>tm</i> structure are:</p>
<dl>
<dt><i>tm_sec</i></p>
<dd> The number of seconds after the minute, normally in the range 0 to 59, but can be up to 60 to allow for leap seconds.</p>
<dt><i>tm_min</i></p>
<dd> The number of minutes after the hour, in the range 0 to 59.</p>
<dt><i>tm_hour</i></p>
<dd> The number of hours past midnight, in the range 0 to 23.</p>
<dt><i>tm_mday</i></p>
<dd> The day of the month, in the range 1 to 31.</p>
<dt><i>tm_mon</i></p>
<dd> The number of months since January, in the range 0 to 11.</p>
<dt><i>tm_year</i></p>
<dd> The number of years since 1900.</p>
<dt><i>tm_wday</i></p>
<dd> The number of days since Sunday, in the range 0 to 6.</p>
<dt><i>tm_yday</i></p>
<dd> The number of days since January 1, in the range 0 to 365.</p>
<dt><i>tm_isdst</i></p>
<dd> A flag that indicates whether daylight saving time is in effect at the time described. The value is positive if daylight saving time is in effect, zero if it is not, and negative if the information is not available.</dl>
<p> The call <code>ctime(</code><i>t</i><code>)</code> is equivalent to <code>asctime(localtime(</code><i>t</i><code>))</code><i></i>. It converts the calendar time <i>t</i> into a null-terminated string of the form </p>
<p> &quot;Wed Jun 30 21:49:08 1993
&quot; </p>
<p> The abbreviations for the days of the week are &quot;Sun&quot;, &quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, and &quot;Sat&quot;. The abbreviations for the months are &quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;, &quot;Apr&quot;, &quot;May&quot;, &quot;Jun&quot;, &quot;Jul&quot;, &quot;Aug&quot;, &quot;Sep&quot;, &quot;Oct&quot;, &quot;Nov&quot;, and &quot;Dec&quot;. The return value points to a statically allocated string which might be overwritten by subsequent calls to any of the date and time functions. The function also sets the external variables <i>tzname</i>, <i>timezone</i>, and <i>daylight</i> (see <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3)) with information about the current timezone. The reentrant version <code>ctime_r</code>() does the same, but stores the string in a user-supplied buffer which should have room for at least 26 bytes. It need not set <i>tzname</i>, <i>timezone</i>, and <i>daylight</i>. </p>
<p> The <code>gmtime</code>() function converts the calendar time <i>timep</i> to broken-down time representation, expressed in Coordinated Universal Time (UTC). It may return NULL when the year does not fit into an integer. The return value points to a statically allocated struct which might be overwritten by subsequent calls to any of the date and time functions. The <code>gmtime_r</code>() function does the same, but stores the data in a user-supplied struct. </p>
<p> The <code>localtime</code>() function converts the calendar time <i>timep</i> to broken-down time representation, expressed relative to the user&#8217;s specified timezone. The function acts as if it called <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) and sets the external variables <i>tzname</i> with information about the current timezone, <i>timezone</i> with the difference between Coordinated Universal Time (UTC) and local standard time in seconds, and <i>daylight</i> to a nonzero value if daylight savings time rules apply during some part of the year. The return value points to a statically allocated struct which might be overwritten by subsequent calls to any of the date and time functions. The <code>localtime_r</code>() function does the same, but stores the data in a user-supplied struct. It need not set <i>tzname</i>, <i>timezone</i>, and <i>daylight</i>. </p>
<p> The <code>asctime</code>() function converts the broken-down time value <i>tm</i> into a null-terminated string with the same format as <code>ctime</code>(). The return value points to a statically allocated string which might be overwritten by subsequent calls to any of the date and time functions. The <code>asctime_r</code>() function does the same, but stores the string in a user-supplied buffer which should have room for at least 26 bytes. </p>
<p> The <code>mktime</code>() function converts a broken-down time structure, expressed as local time, to calendar time representation. The function ignores the values supplied by the caller in the <i>tm_wday</i> and <i>tm_yday</i> fields. The value specified in the <i>tm_isdst</i> field informs <code>mktime</code>() whether or not daylight saving time (DST) is in effect for the time supplied in the <i>tm</i> structure: a positive value means DST is in effect; zero means that DST is not in effect; and a negative value means that <code>mktime</code>() should (use timezone information and system databases to) attempt to determine whether DST is in effect at the specified time. </p>
<p> The <code>mktime</code>() function modifies the fields of the <i>tm</i> structure as follows: <i>tm_wday</i> and <i>tm_yday</i> are set to values determined from the contents of the other fields; if structure members are outside their valid interval, they will be normalized (so that, for example, 40 October is changed into 9 November); <i>tm_isdst</i> is set (regardless of its initial value) to a positive value or to 0, respectively, to indicate whether DST is or is not in effect at the specified time. Calling <code>mktime</code>() also sets the external variable <i>tzname</i> with information about the current timezone. </p>
<p> If the specified broken-down time cannot be represented as calendar time (seconds since the Epoch), <code>mktime</code>() returns <i>(time_t)&nbsp;-1</i> and does not alter the members of the broken-down time structure.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>gmtime</code>() and <code>localtime</code>() return a pointer to a <i>struct tm</i>. </p>
<p> On success, <code>gmtime_r</code>() and <code>localtime_r</code>() return the address of the structure pointed to by <i>result</i>. </p>
<p> On success, <code>asctime</code>() and <code>ctime</code>() return a pointer to a string. </p>
<p> On success, <code>asctime_r</code>() and <code>ctime_r</code>() return a pointer to the string pointed to by <i>buf</i>. </p>
<p> On success, <code>mktime</code>() returns the calendar time (seconds since the Epoch), expressed as a value of type <i>time_t</i>. </p>
<p> On error, <code>mktime</code>() returns the value <i>(time_t)&nbsp;-1</i>. The remaining functions return NULL on error. On error, <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EOVERFLOW</code></p>
<dd> The result cannot be represented.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>asctime</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:asctime locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>asctime_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>ctime</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:tmbuf<br />
 race:asctime env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>ctime_r</code>(), <code>gmtime_r</code>(), <code>localtime_r</code>(), <code>mktime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtime</code>(), <code>localtime</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:tmbuf env locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001. C89 and C99 specify <code>asctime</code>(), <code>ctime</code>(), <code>gmtime</code>(), <code>localtime</code>(), and <code>mktime</code>(). POSIX.1-2008 marks <code>asctime</code>(), <code>asctime_r</code>(), <code>ctime</code>(), and <code>ctime_r</code>() as obsolete, recommending the use of <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) instead.</p>
<h2>NOTES</h2>
<p> The four functions <code>asctime</code>(), <code>ctime</code>(), <code>gmtime</code>(), and <code>localtime</code>() return a pointer to static data and hence are not thread-safe. The thread-safe versions, <code>asctime_r</code>(), <code>ctime_r</code>(), <code>gmtime_r</code>(), and <code>localtime_r</code>(), are specified by SUSv2. </p>
<p> POSIX.1-2001 says: &quot;The <code>asctime</code>(), <code>ctime</code>(), <code>gmtime</code>(), and <code>localtime</code>() functions shall return values in one of two static objects: a broken-down time structure and an array of type <i>char</i>. Execution of any of the functions may overwrite the information returned in either of these objects by any of the other functions.&quot; This can occur in the glibc implementation. </p>
<p> In many implementations, including glibc, a 0 in <i>tm_mday</i> is interpreted as meaning the last day of the preceding month. </p>
<p> The glibc version of <i>struct tm</i> has additional fields </p>
<p> const char *tm_zone; /* Timezone abbreviation */ </p>
<p> defined when <code>_BSD_SOURCE</code> was set before including <i>&lt;time.h&gt;</i>. This is a BSD extension, present in 4.3BSD-Reno. </p>
<p> According to POSIX.1-2001, <code>localtime</code>() is required to behave as though <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) was called, while <code>localtime_r</code>() does not have this requirement. For portable code, <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) should be called before <code>localtime_r</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/3-clock/">clock</a></code>(3), <code><a href="/docs/linux/man/3-difftime/">difftime</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3), <code><a href="/docs/linux/man/3-timegm/">timegm</a></code>(3), <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
