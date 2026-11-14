---
title: "strftime(3)"
name: "strftime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strftime/"
description: "strftime – format date and time"
---

<p>strftime &#8211; format date and time</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;time.h&gt;

size_t strftime(char *s, size_t max, const char *format,
                const struct tm *tm);</code></pre>
<h2>Description</h2>
<p>The <code>strftime</code>() function formats the broken-down time <i>tm</i> according to the format specification <i>format</i> and places the result in the character array <i>s</i> of size <i>max</i>. The broken-down time structure <i>tm</i> is defined in <i>&lt;time.h&gt;</i>. See also <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3). </p>
<p> The format specification is a null-terminated string and may contain special character sequences called <i>conversion specifications,</i> each of which is introduced by a &#8216;%&#8217; character and terminated by some other character known as a <i>conversion specifier character.</i> All other character sequences are <i>ordinary character sequences.</i> </p>
<p> The characters of ordinary character sequences (including the null byte) are copied verbatim from <i>format</i> to <i>s</i>. However, the characters of conversion specifications are replaced as shown in the list below. In this list, the field(s) employed from the <i>tm</i> structure are also shown.</p>
<dl>
<dt><code>%a</code></p>
<dd>The abbreviated name of the day of the week according to the current locale. (Calculated from <i>tm_wday</i>.) (The specific names used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>ABDAY_</code>{<code>1</code>&#8211;<code>7</code>} as an argument.)</p>
<dt><code>%A</code></p>
<dd>The full name of the day of the week according to the current locale. (Calculated from <i>tm_wday</i>.) (The specific names used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>DAY_</code>{<code>1</code>&#8211;<code>7</code>} as an argument.)</p>
<dt><code>%b</code></p>
<dd>The abbreviated month name according to the current locale. (Calculated from <i>tm_mon</i>.) (The specific names used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>ABMON_</code>{<code>1</code>&#8211;<code>12</code>} as an argument.)</p>
<dt><code>%B</code></p>
<dd>The full month name according to the current locale. (Calculated from <i>tm_mon</i>.) (The specific names used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>MON_</code>{<code>1</code>&#8211;<code>12</code>} as an argument.)</p>
<dt><code>%c</code></p>
<dd>The preferred date and time representation for the current locale. (The specific format used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>D_T_FMT</code> as an argument for the <code>%c</code> conversion specification, and with <code>ERA_D_T_FMT</code> for the <code>%Ec</code> conversion specification.) (In the POSIX locale this is equivalent to <code>%a %b %e %H:%M:%S %Y</code>.)</p>
<dt><code>%C</code></p>
<dd>The century number (year/100) as a 2-digit integer. (SU) (The <code>%EC</code> conversion specification corresponds to the name of the era.) (Calculated from <i>tm_year</i>.)</p>
<dt><code>%d</code></p>
<dd>The day of the month as a decimal number (range 01 to 31). (Calculated from <i>tm_mday</i>.)</p>
<dt><code>%D</code></p>
<dd>Equivalent to <code>%m/%d/%y</code>. (Yecch&#8212;for Americans only. Americans should note that in other countries <code>%d/%m/%y</code> is rather common. This means that in international context this format is ambiguous and should not be used.) (SU)</p>
<dt><code>%e</code></p>
<dd>Like <code>%d</code>, the day of the month as a decimal number, but a leading zero is replaced by a space. (SU) (Calculated from <i>tm_mday</i>.)</p>
<dt><code>%E</code></p>
<dd>Modifier: use alternative (&quot;era-based&quot;) format, see below. (SU)</p>
<dt><code>%F</code></p>
<dd>Equivalent to <code>%Y-%m-%d</code> (the ISO 8601 date format). (C99)</p>
<dt><code>%G</code></p>
<dd>The ISO 8601 week-based year (see NOTES) with century as a decimal number. The 4-digit year corresponding to the ISO week number (see <code>%V</code>). This has the same format and value as <code>%Y</code>, except that if the ISO week number belongs to the previous or next year, that year is used instead. (TZ) (Calculated from <i>tm_year</i>, <i>tm_yday</i>, and <i>tm_wday</i>.)</p>
<dt><code>%g</code></p>
<dd>Like <code>%G</code>, but without century, that is, with a 2-digit year (00-99). (TZ) (Calculated from <i>tm_year</i>, <i>tm_yday</i>, and <i>tm_wday</i>.)</p>
<dt><code>%h</code></p>
<dd>Equivalent to <code>%b</code>. (SU)</p>
<dt><code>%H</code></p>
<dd>The hour as a decimal number using a 24-hour clock (range 00 to 23). (Calculated from <i>tm_hour</i>.)</p>
<dt><code>%I</code></p>
<dd>The hour as a decimal number using a 12-hour clock (range 01 to 12). (Calculated from <i>tm_hour</i>.)</p>
<dt><code>%j</code></p>
<dd>The day of the year as a decimal number (range 001 to 366). (Calculated from <i>tm_yday</i>.)</p>
<dt><code>%k</code></p>
<dd>The hour (24-hour clock) as a decimal number (range 0 to 23); single digits are preceded by a blank. (See also <code>%H</code>.) (Calculated from <i>tm_hour</i>.) (TZ)</p>
<dt><code>%l</code></p>
<dd>The hour (12-hour clock) as a decimal number (range 1 to 12); single digits are preceded by a blank. (See also <code>%I</code>.) (Calculated from <i>tm_hour</i>.) (TZ)</p>
<dt><code>%m</code></p>
<dd>The month as a decimal number (range 01 to 12). (Calculated from <i>tm_mon</i>.)</p>
<dt><code>%M</code></p>
<dd>The minute as a decimal number (range 00 to 59). (Calculated from <i>tm_min</i>.)</p>
<dt><code>%n</code></p>
<dd>A newline character. (SU)</p>
<dt><code>%O</code></p>
<dd>Modifier: use alternative numeric symbols, see below. (SU)</p>
<dt><code>%p</code></p>
<dd>Either &quot;AM&quot; or &quot;PM&quot; according to the given time value, or the corresponding strings for the current locale. Noon is treated as &quot;PM&quot; and midnight as &quot;AM&quot;. (Calculated from <i>tm_hour</i>.) (The specific string representations used for &quot;AM&quot; and &quot;PM&quot; in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>AM_STR</code> and <code>PM_STR</code>, respectively.)</p>
<dt><code>%P</code></p>
<dd>Like <code>%p</code> but in lowercase: &quot;am&quot; or &quot;pm&quot; or a corresponding string for the current locale. (Calculated from <i>tm_hour</i>.) (GNU)</p>
<dt><code>%r</code></p>
<dd>The time in a.m. or p.m. notation. (SU) (The specific format used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>T_FMT_AMPM</code> as an argument.) (In the POSIX locale this is equivalent to <code>%I:%M:%S %p</code>.)</p>
<dt><code>%R</code></p>
<dd>The time in 24-hour notation (<code>%H:%M</code>). (SU) For a version including the seconds, see <code>%T</code> below.</p>
<dt><code>%s</code></p>
<dd>The number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). (TZ) (Calculated from <i>mktime(tm)</i>.)</p>
<dt><code>%S</code></p>
<dd>The second as a decimal number (range 00 to 60). (The range is up to 60 to allow for occasional leap seconds.) (Calculated from <i>tm_sec</i>.)</p>
<dt><code>%t</code></p>
<dd>A tab character. (SU)</p>
<dt><code>%T</code></p>
<dd>The time in 24-hour notation (<code>%H:%M:%S</code>). (SU)</p>
<dt><code>%u</code></p>
<dd>The day of the week as a decimal, range 1 to 7, Monday being 1. See also <code>%w</code>. (Calculated from <i>tm_wday</i>.) (SU)</p>
<dt><code>%U</code></p>
<dd>The week number of the current year as a decimal number, range 00 to 53, starting with the first Sunday as the first day of week 01. See also <code>%V</code> and <code>%W</code>. (Calculated from <i>tm_yday</i> and <i>tm_wday</i>.)</p>
<dt><code>%V</code></p>
<dd>The ISO 8601 week number (see NOTES) of the current year as a decimal number, range 01 to 53, where week 1 is the first week that has at least 4 days in the new year. See also <code>%U</code> and <code>%W</code>. (Calculated from <i>tm_year</i>, <i>tm_yday</i>, and <i>tm_wday</i>.) (SU)</p>
<dt><code>%w</code></p>
<dd>The day of the week as a decimal, range 0 to 6, Sunday being 0. See also <code>%u</code>. (Calculated from <i>tm_wday</i>.)</p>
<dt><code>%W</code></p>
<dd>The week number of the current year as a decimal number, range 00 to 53, starting with the first Monday as the first day of week 01. (Calculated from <i>tm_yday</i> and <i>tm_wday</i>.)</p>
<dt><code>%x</code></p>
<dd>The preferred date representation for the current locale without the time. (The specific format used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>D_FMT</code> as an argument for the <code>%x</code> conversion specification, and with <code>ERA_D_FMT</code> for the <code>%Ex</code> conversion specification.) (In the POSIX locale this is equivalent to <code>%m/%d/%y</code>.)</p>
<dt><code>%X</code></p>
<dd>The preferred time representation for the current locale without the date. (The specific format used in the current locale can be obtained by calling <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3) with <code>T_FMT</code> as an argument for the <code>%X</code> conversion specification, and with <code>ERA_T_FMT</code> for the <code>%EX</code> conversion specification.) (In the POSIX locale this is equivalent to <code>%H:%M:%S</code>.)</p>
<dt><code>%y</code></p>
<dd>The year as a decimal number without a century (range 00 to 99). (The <code>%Ey</code> conversion specification corresponds to the year since the beginning of the era denoted by the <code>%EC</code> conversion specification.) (Calculated from <i>tm_year</i>)</p>
<dt><code>%Y</code></p>
<dd>The year as a decimal number including the century. (The <code>%EY</code> conversion specification corresponds to the full alternative year representation.) (Calculated from <i>tm_year</i>)</p>
<dt><code>%z</code></p>
<dd>The <i>+hhmm</i> or <i>-hhmm</i> numeric timezone (that is, the hour and minute offset from UTC). (SU)</p>
<dt><code>%Z</code></p>
<dd>The timezone name or abbreviation.</p>
<dt><code>%+</code></p>
<dd>The date and time in <code><a href="/docs/linux/man/1-date/">date</a></code>(1) format. (TZ) (Not supported in glibc2.)</p>
<dt><code>%%</code></p>
<dd>A literal &#8216;%&#8217; character.</dl>
<p> Some conversion specifications can be modified by preceding the conversion specifier character by the <code>E</code> or <code>O</code> <i>modifier</i> to indicate that an alternative format should be used. If the alternative format or specification does not exist for the current locale, the behavior will be as if the unmodified conversion specification were used. (SU) The Single UNIX Specification mentions <code>%Ec</code>, <code>%EC</code>, <code>%Ex</code>, <code>%EX</code>, <code>%Ey</code>, <code>%EY</code>, <code>%Od</code>, <code>%Oe</code>, <code>%OH</code>, <code>%OI</code>, <code>%Om</code>, <code>%OM</code>, <code>%OS</code>, <code>%Ou</code>, <code>%OU</code>, <code>%OV</code>, <code>%Ow</code>, <code>%OW</code>, <code>%Oy</code>, where the effect of the <code>O</code> modifier is to use alternative numeric symbols (say, roman numerals), and that of the <code>E</code> modifier is to use a locale-dependent alternative representation. The rules governing date representation with the <code>E</code> modifier can be obtained by supplying <code>ERA</code> as an argument to a <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3). One example of such alternative forms is the Japanese era calendar scheme in the <code>ja_JP</code> glibc locale.</p>
<h2>Return Value</h2>
<p>Provided that the result string, including the terminating null byte, does not exceed <i>max</i> bytes, <code>strftime</code>() returns the number of bytes (excluding the terminating null byte) placed in the array <i>s</i>. If the length of the result string (including the terminating null byte) would exceed <i>max</i> bytes, then <code>strftime</code>() returns 0, and the contents of the array are undefined. </p>
<p> Note that the return value 0 does not necessarily indicate an error. For example, in many locales <code>%p</code> yields an empty string. An empty <i>format</i> string will likewise yield an empty string.</p>
<h2>Environment</h2>
<p>The environment variables <code>TZ</code> and <code>LC_TIME</code> are used.</p>
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
<td> <code>strftime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4, C89, C99. There are strict inclusions between the set of conversions given in ANSI C (unmarked), those given in the Single UNIX Specification (marked SU), those given in Olson&#8217;s timezone package (marked TZ), and those given in glibc (marked GNU), except that <code>%+</code> is not supported in glibc2. On the other hand glibc2 has several more extensions. POSIX.1 only refers to ANSI C; POSIX.2 describes under <code><a href="/docs/linux/man/1-date/">date</a></code>(1) several extensions that could apply to <code>strftime</code>() as well. The <code>%F</code> conversion is in C99 and POSIX.1-2001. </p>
<p> In SUSv2, the <code>%S</code> specifier allowed a range of 00 to 61, to allow for the theoretical possibility of a minute that included a double leap second (there never has been such a minute).</p>
<h2>Notes</h2>
<h3>ISO 8601 week dates</h3>
<p><code>%G</code>, <code>%g</code>, and <code>%V</code> yield values calculated from the week-based year defined by the ISO 8601 standard. In this system, weeks start on a Monday, and are numbered from 01, for the first week, up to 52 or 53, for the last week. Week 1 is the first week where four or more days fall within the new year (or, synonymously, week 01 is: the first week of the year that contains a Thursday; or, the week that has 4 January in it). When three or fewer days of the first calendar week of the new year fall within that year, then the ISO 8601 week-based system counts those days as part of week 52 or 53 of the preceding year. For example, 1 January 2010 is a Friday, meaning that just three days of that calendar week fall in 2010. Thus, the ISO 8601 week-based system considers these days to be part of week 53 (<code>%V</code>) of the year 2009 (<code>%G</code>); week 01 of ISO 8601 year 2010 starts on Monday, 4 January 2010. Similarly, the first two days of January 2011 are considered to be part of week 52 of the year 2010.</p>
<h3>Glibc notes</h3>
<p>Glibc provides some extensions for conversion specifications. (These extensions are not specified in POSIX.1-2001, but a few other systems provide similar features.) Between the &#8216;%&#8217; character and the conversion specifier character, an optional <i>flag</i> and field <i>width</i> may be specified. (These precede the <code>E</code> or <code>O</code> modifiers, if present.) </p>
<p> The following flag characters are permitted:</p>
<dl>
<dt><code>_</code></p>
<dd>(underscore) Pad a numeric result string with spaces.</p>
<dt><code>&#8211;</code></p>
<dd>(dash) Do not pad a numeric result string.</p>
<dt><code>0</code></p>
<dd>Pad a numeric result string with zeros even if the conversion specifier character uses space-padding by default.</p>
<dt><code>ha</code></p>
<dd>Convert alphabetic characters in result string to uppercase.</p>
<dt><code>#</code></p>
<dd>Swap the case of the result string. (This flag works only with certain conversion specifier characters, and of these, it is only really useful with <code>%Z</code>.)</dl>
<p> An optional decimal width specifier may follow the (possibly absent) flag. If the natural size of the field is smaller than this width, then the result string is padded (on the left) to the specified width.</p>
<h2>Bugs</h2>
<p>If the output string would exceed <i>max</i> bytes, <i>errno</i> is <i>not</i> set. This makes it impossible to distinguish this error case from cases where the <i>format</i> string legitimately produces a zero-length output string. POSIX.1-2001 does <i>not</i> specify any <i>errno</i> settings for <code>strftime</code>(). Some buggy versions of <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) complain about the use of <code>%c</code>: <i>warning: `%c&#8217; yields only last 2 digits of year in some locales</i>. Of course programmers are encouraged to use <code>%c</code>, as it gives the preferred date and time representation. One meets all kinds of strange obfuscations to circumvent this <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) problem. A relatively clean one is to add an intermediate function size_t<br />
my_strftime(char *s, size_t max, const char *fmt,<br />
            const struct tm *tm)<br />
{<br />
    return strftime(s, max, fmt, tm);<br />
} Nowadays, <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) provides the <i>-Wno-format-y2k</i> option to prevent the warning, so that the above workaround is no longer required.</p>
<h2>Examples</h2>
<p><code>RFC 2822-compliant date format</code> (with an English locale for %a and %b) &quot;%a,&nbsp;%d&nbsp;%b&nbsp;%Y&nbsp;%T&nbsp;%z&quot; <code>RFC 822-compliant date format</code> (with an English locale for %a and %b) &quot;%a,&nbsp;%d&nbsp;%b&nbsp;%y&nbsp;%T&nbsp;%z&quot;</p>
<h3>Example program</h3>
<p>The program below can be used to experiment with <code>strftime</code>(). Some examples of the result string produced by the glibc implementation of <code>strftime</code>() are as follows: </p>
<pre><code>$ ./a.out '%m'

Result string is &quot;11&quot;
$ ./a.out '%5m'

Result string is &quot;00011&quot;
$ ./a.out '%_5m'

Result string is &quot;   11&quot;



Program source



#include &lt;time.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int
main(int argc, char *argv[])
{
    char outstr[200];
    time_t t;
    struct tm *tmp;
    t = time(NULL);
    tmp = localtime(&amp;t);
    if (tmp == NULL) {
        perror(&quot;localtime&quot;);
        exit(EXIT_FAILURE);
    }
    if (strftime(outstr, sizeof(outstr), argv[1], tmp) == 0) {
        fprintf(stderr, &quot;strftime returned 0&quot;);
        exit(EXIT_FAILURE);
    }
    printf(&quot;Result string is \&quot;%s\&quot;
&quot;, outstr);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
