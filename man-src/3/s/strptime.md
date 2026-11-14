---
title: "strptime(3)"
name: "strptime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strptime/"
description: "strptime – convert a string representation of time to a time tm structure"
---

<p>strptime &#8211; convert a string representation of time to a time tm structure</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */

#include &lt;time.h&gt;
char *strptime(const char *s, const char *format,

               struct tm *tm);</code></pre>
<h2>Description</h2>
<p>The <code>strptime</code>() function is the converse of <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3); it converts the character string pointed to by <i>s</i> to values which are stored in the &quot;broken-down time&quot; structure pointed to by <i>tm</i>, using the format specified by <i>format</i>. The broken-down time structure <i>tm</i> is defined in <i>&lt;time.h&gt;</i> as follows: struct tm {<br />
    int tm_sec;   /* Seconds (0-60) */<br />
    int tm_min;   /* Minutes (0-59) */<br />
    int tm_hour;  /* Hours (0-23) */<br />
    int tm_mday;  /* Day of the month (1-31) */<br />
    int tm_mon;   /* Month (0-11) */<br />
    int tm_year;  /* Year &#8211; 1900 */<br />
    int tm_wday;  /* Day of the week (0-6, Sunday = 0) */<br />
    int tm_yday;  /* Day in the year (0-365, 1 Jan = 0) */<br />
    int tm_isdst; /* Daylight saving time */<br />
}; For more details on the <i>tm</i> structure, see <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3). The <i>format</i> argument is a character string that consists of field descriptors and text characters, reminiscent of <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3). Each field descriptor consists of a <code>%</code> character followed by another character that specifies the replacement for the field descriptor. All other characters in the <i>format</i> string must have a matching character in the input string, except for whitespace, which matches zero or more whitespace characters in the input string. There should be whitespace or other alphanumeric characters between any two field descriptors. The <code>strptime</code>() function processes the input string from left to right. Each of the three possible input elements (whitespace, literal, or format) are handled one after the other. If the input cannot be matched to the format string, the function stops. The remainder of the format and input strings are not processed. The supported input field descriptors are listed below. In case a text string (such as the name of a day of the week or a month name) is to be matched, the comparison is case insensitive. In case a number is to be matched, leading zeros are permitted but not required.</p>
<dl>
<dt><code>%%</code></p>
<dd>The <code>%</code> character.</p>
<dt><code>%a</code> or <code>%A</code></p>
<dd>The name of the day of the week according to the current locale, in abbreviated form or the full name.</p>
<dt><code>%b</code> or <code>%B</code> or <code>%h</code></p>
<dd>The month name according to the current locale, in abbreviated form or the full name.</p>
<dt><code>%c</code></p>
<dd>The date and time representation for the current locale.</p>
<dt><code>%C</code></p>
<dd>The century number (0-99).</p>
<dt><code>%d</code> or <code>%e</code></p>
<dd>The day of month (1-31).</p>
<dt><code>%D</code></p>
<dd>Equivalent to <code>%m/%d/%y</code>. (This is the American style date, very confusing to non-Americans, especially since <code>%d/%m/%y</code> is widely used in Europe. The ISO 8601 standard format is <code>%Y-%m-%d</code>.)</p>
<dt><code>%H</code></p>
<dd>The hour (0-23).</p>
<dt><code>%I</code></p>
<dd>The hour on a 12-hour clock (1-12).</p>
<dt><code>%j</code></p>
<dd>The day number in the year (1-366).</p>
<dt><code>%m</code></p>
<dd>The month number (1-12).</p>
<dt><code>%M</code></p>
<dd>The minute (0-59).</p>
<dt><code>%n</code></p>
<dd>Arbitrary whitespace.</p>
<dt><code>%p</code></p>
<dd>The locale&#8217;s equivalent of AM or PM. (Note: there may be none.)</p>
<dt><code>%r</code></p>
<dd>The 12-hour clock time (using the locale&#8217;s AM or PM). In the POSIX locale equivalent to <code>%I:%M:%S %p</code>. If <i>t_fmt_ampm</i> is empty in the <code>LC_TIME</code> part of the current locale, then the behavior is undefined.</p>
<dt><code>%R</code></p>
<dd>Equivalent to <code>%H:%M</code>.</p>
<dt><code>%S</code></p>
<dd>The second (0-60; 60 may occur for leap seconds; earlier also 61 was allowed).</p>
<dt><code>%t</code></p>
<dd>Arbitrary whitespace.</p>
<dt><code>%T</code></p>
<dd>Equivalent to <code>%H:%M:%S</code>.</p>
<dt><code>%U</code></p>
<dd>The week number with Sunday the first day of the week (0-53). The first Sunday of January is the first day of week 1.</p>
<dt><code>%w</code></p>
<dd>The ordinal number of the day of the week (0-6), with Sunday = 0.</p>
<dt><code>%W</code></p>
<dd>The week number with Monday the first day of the week (0-53). The first Monday of January is the first day of week 1.</p>
<dt><code>%x</code></p>
<dd>The date, using the locale&#8217;s date format.</p>
<dt><code>%X</code></p>
<dd>The time, using the locale&#8217;s time format.</p>
<dt><code>%y</code></p>
<dd>The year within century (0-99). When a century is not otherwise specified, values in the range 69-99 refer to years in the twentieth century (1969-1999); values in the range 00-68 refer to years in the twenty-first century (2000-2068).</p>
<dt><code>%Y</code></p>
<dd>The year, including century (for example, 1991).</dl>
<p> Some field descriptors can be modified by the E or O modifier characters to indicate that an alternative format or specification should be used. If the alternative format or specification does not exist in the current locale, the unmodified field descriptor is used. The E modifier specifies that the input string may contain alternative locale-dependent versions of the date and time representation:</p>
<dl>
<dt><code>%Ec</code></p>
<dd>The locale&#8217;s alternative date and time representation.</p>
<dt><code>%EC</code></p>
<dd>The name of the base year (period) in the locale&#8217;s alternative representation.</p>
<dt><code>%Ex</code></p>
<dd>The locale&#8217;s alternative date representation.</p>
<dt><code>%EX</code></p>
<dd>The locale&#8217;s alternative time representation.</p>
<dt><code>%Ey</code></p>
<dd>The offset from <code>%EC</code> (year only) in the locale&#8217;s alternative representation.</p>
<dt><code>%EY</code></p>
<dd>The full alternative year representation.</dl>
<p> The O modifier specifies that the numerical input may be in an alternative locale-dependent format:</p>
<dl>
<dt><code>%Od</code> or <code>%Oe</code></p>
<dd>The day of the month using the locale&#8217;s alternative numeric symbols; leading zeros are permitted but not required.</p>
<dt><code>%OH</code></p>
<dd>The hour (24-hour clock) using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%OI</code></p>
<dd>The hour (12-hour clock) using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%Om</code></p>
<dd>The month using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%OM</code></p>
<dd>The minutes using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%OS</code></p>
<dd>The seconds using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%OU</code></p>
<dd>The week number of the year (Sunday as the first day of the week) using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%Ow</code></p>
<dd>The ordinal number of the day of the week (Sunday=0),<br />
&nbsp;using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%OW</code></p>
<dd>The week number of the year (Monday as the first day of the week) using the locale&#8217;s alternative numeric symbols.</p>
<dt><code>%Oy</code></p>
<dd>The year (offset from <code>%C</code>) using the locale&#8217;s alternative numeric symbols.</dl>
<h2>Return Value</h2>
<p>The return value of the function is a pointer to the first character not processed in this function call. In case the input string contains more characters than required by the format string, the return value points right after the last consumed input character. In case the whole input string is consumed, the return value points to the null byte at the end of the string. If <code>strptime</code>() fails to match all of the format string and therefore an error occurred, the function returns NULL.</p>
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
<td> <code>strptime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>Notes</h2>
<p>In principle, this function does not initialize <i>tm</i> but stores only the values specified. This means that <i>tm</i> should be initialized before the call. Details differ a bit between different UNIX systems. The glibc implementation does not touch those fields which are not explicitly specified, except that it recomputes the <i>tm_wday</i> and <i>tm_yday</i> field if any of the year, month, or day elements changed. </p>
<p> The &#8216;y&#8217; (year in century) specification is taken to specify a year in the range 1950-2049 by glibc 2.0. It is taken to be a year in 1969-2068 since glibc 2.1.</p>
<h3>Glibc notes</h3>
<p>For reasons of symmetry, glibc tries to support for <code>strptime</code>() the same format characters as for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). (In most cases, the corresponding fields are parsed, but no field in <i>tm</i> is changed.) This leads to</p>
<dl>
<dt><code>%F</code></p>
<dd>Equivalent to <code>%Y-%m-%d</code>, the ISO 8601 date format.</p>
<dt><code>%g</code></p>
<dd>The year corresponding to the ISO week number, but without the century (0-99).</p>
<dt><code>%G</code></p>
<dd>The year corresponding to the ISO week number. (For example, 1991.)</p>
<dt><code>%u</code></p>
<dd>The day of the week as a decimal number (1-7, where Monday = 1).</p>
<dt><code>%V</code></p>
<dd>The ISO 8601:1988 week number as a decimal number (1-53). If the week (starting on Monday) containing 1 January has four or more days in the new year, then it is considered week 1. Otherwise, it is the last week of the previous year, and the next week is week 1.</p>
<dt><code>%z</code></p>
<dd>An RFC-822/ISO 8601 standard timezone specification.</p>
<dt><code>%Z</code></p>
<dd>The timezone name.</dl>
<p> Similarly, because of GNU extensions to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code>%k</code> is accepted as a synonym for <code>%H</code>, and <code>%l</code> should be accepted as a synonym for <code>%I</code>, and <code>%P</code> is accepted as a synonym for <code>%p</code>. Finally</p>
<dl>
<dt><code>%s</code></p>
<dd>The number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). Leap seconds are not counted unless leap second support is available.</dl>
<p> The glibc implementation does not require whitespace between two field descriptors.</p>
<h2>Examples</h2>
<p>The following example demonstrates the use of <code>strptime</code>() and <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). </p>
<pre><code>#define _XOPEN_SOURCE
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;time.h&gt;
int main(void)
{
    struct tm tm;
    char buf[255];
    memset(&amp;tm, 0, sizeof(tm));
    strptime(&quot;2001-11-12 18:31:01&quot;, &quot;%Y-%m-%d %H:%M:%S&quot;, &amp;tm);
    strftime(buf, sizeof(buf), &quot;%d %b %Y %H:%M&quot;, &amp;tm);
    puts(buf);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-getdate/">getdate</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
