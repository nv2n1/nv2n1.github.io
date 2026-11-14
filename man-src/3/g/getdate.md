---
title: "getdate(3)"
name: "getdate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdate/"
description: "getdate, getdate_r – convert a date-plus-time string to broken-down time"
---

<h2 class="name">NAME</h2>
<p> getdate, getdate_r &#8211; convert a date-plus-time string to broken-down time </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>struct tm *getdate(const char *</code><i>string</i><code>);</code> </p>
<p> <code>extern int getdate_err;</code> </p>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int getdate_r(const char *</code><i>string</i><code>, struct tm *</code><i>res</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getdate</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<p> <code>getdate_r</code>():</p>
<dl>
<dt>
<dd> _GNU_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>getdate</code>() converts a string representation of a date and time, contained in the buffer pointed to by <i>string</i>, into a broken-down time. The broken-down time is stored in a <i>tm</i> structure, and a pointer to this structure is returned as the function result. This <i>tm</i> structure is allocated in static storage, and consequently it will be overwritten by further calls to <code>getdate</code>(). </p>
<p> In contrast to <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3), (which has a <i>format</i> argument), <code>getdate</code>() uses the formats found in the file whose full pathname is given in the environment variable <code>DATEMSK</code>. The first line in the file that matches the given input string is used for the conversion. </p>
<p> The matching is done case insensitively. Superfluous whitespace, either in the pattern or in the string to be converted, is ignored. </p>
<p> The conversion specifications that a pattern can contain are those given for <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3). One more conversion specification is specified in POSIX.1-2001:</p>
<dl>
<dt><code>%Z</code></p>
<dd> Timezone name. This is not implemented in glibc.</dl>
<p> When <code>%Z</code> is given, the structure containing the broken-down time is initialized with values corresponding to the current time in the given timezone. Otherwise, the structure is initialized to the broken-down time corresponding to the current local time (as by a call to <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3)). </p>
<p> When only the day of the week is given, the day is taken to be the first such day on or after today. </p>
<p> When only the month is given (and no year), the month is taken to be the first such month equal to or after the current month. If no day is given, it is the first day of the month. </p>
<p> When no hour, minute and second are given, the current hour, minute and second are taken. </p>
<p> If no date is given, but we know the hour, then that hour is taken to be the first such hour equal to or after the current hour. </p>
<p> <code>getdate_r</code>() is a GNU extension that provides a reentrant version of <code>getdate</code>(). Rather than using a global variable to report errors and a static buffer to return the broken down time, it returns errors via the function result value, and returns the resulting broken-down time in the caller-allocated buffer pointed to by the argument <i>res</i>.</p>
<h2>RETURN VALUE</h2>
<p> When successful, <code>getdate</code>() returns a pointer to a <i>struct tm</i>. Otherwise, it returns NULL and sets the global variable <i>getdate_err</i> to one of the error numbers shown below. Changes to <i>errno</i> are unspecified. </p>
<p> On success <code>getdate_r</code>() returns 0; on error it returns one of the error numbers shown below.</p>
<h2>ERRORS</h2>
<p> The following errors are returned via <i>getdate_err</i> (for <code>getdate</code>()) or as the function result (for <code>getdate_r</code>()):</p>
<dl>
<dt><code>1</code></p>
<dd> The <code>DATEMSK</code> environment variable is not defined, or its value is an empty string.</p>
<dt><code>2</code></p>
<dd> The template file specified by <code>DATEMSK</code> cannot be opened for reading.</p>
<dt><code>3</code></p>
<dd> Failed to get file status information.</p>
<dt><code>4</code></p>
<dd> The template file is not a regular file.</p>
<dt><code>5</code></p>
<dd> An error was encountered while reading the template file.</p>
<dt><code>6</code></p>
<dd> Memory allocation failed (not enough memory available).</p>
<dt><code>7</code></p>
<dd> There is no line in the file that matches the input.</p>
<dt><code>8</code></p>
<dd> Invalid input specification.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DATEMSK</code></p>
<dd> File containing format patterns.</p>
<dt><code>TZ</code>, <code>LC_TIME</code></p>
<dd> Variables used by <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3).</dl>
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
<td> <code>getdate</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:getdate env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getdate_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> The POSIX.1 specification for <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3) contains conversion specifications using the <code>%E</code> or <code>%O</code> modifier, while such specifications are not given for <code>getdate</code>(). In glibc, <code>getdate</code>() is implemented using <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3), so that precisely the same conversions are supported by both.</p>
<h2>EXAMPLES</h2>
<p> The program below calls <code>getdate</code>() for each of its command-line arguments, and for each call displays the values in the fields of the returned <i>tm</i> structure. The following shell session demonstrates the operation of the program: </p>
<p> $<code> TFILE=$PWD/tfile</code> $<code> echo &#8216;%A&#8217; &gt; $TFILE </code> # Full name of the day of the week $<code> echo &#8216;%T&#8217; &gt;&gt; $TFILE</code> # ISO date (YYYY-MM-DD) $<code> echo &#8216;%F&#8217; &gt;&gt; $TFILE</code> # Time (HH:MM:SS) $<code> date</code> $<code> export DATEMSK=$TFILE</code> $<code> ./a.out Tuesday &#8216;2009-12-28&#8242; &#8217;12:22:33&#8217;</code> Sun Sep 7 06:03:36 CEST 2008 Call 1 (&quot;Tuesday&quot;) succeeded:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_sec&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;36<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_min&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_hour&nbsp;<wbr>&nbsp;=&nbsp;6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mday&nbsp;<wbr>&nbsp;=&nbsp;9<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mon&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_year&nbsp;<wbr>&nbsp;=&nbsp;108<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_wday&nbsp;<wbr>&nbsp;=&nbsp;2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_yday&nbsp;<wbr>&nbsp;=&nbsp;252<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_isdst&nbsp;=&nbsp;1 Call 2 (&quot;2009-12-28&quot;) succeeded:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_sec&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;36<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_min&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_hour&nbsp;<wbr>&nbsp;=&nbsp;6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mday&nbsp;<wbr>&nbsp;=&nbsp;28<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mon&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;11<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_year&nbsp;<wbr>&nbsp;=&nbsp;109<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_wday&nbsp;<wbr>&nbsp;=&nbsp;1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_yday&nbsp;<wbr>&nbsp;=&nbsp;361<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_isdst&nbsp;=&nbsp;0 Call 3 (&quot;12:22:33&quot;) succeeded:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_sec&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;33<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_min&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;22<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_hour&nbsp;<wbr>&nbsp;=&nbsp;12<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mday&nbsp;<wbr>&nbsp;=&nbsp;7<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mon&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_year&nbsp;<wbr>&nbsp;=&nbsp;108<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_wday&nbsp;<wbr>&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_yday&nbsp;<wbr>&nbsp;=&nbsp;250<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_isdst&nbsp;=&nbsp;1</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;time.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct tm&nbsp;*tmp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;1;&nbsp;j&nbsp;&lt;&nbsp;argc;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tmp&nbsp;=&nbsp;getdate(argv[j]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(tmp&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Call&nbsp;%d failed;&nbsp;getdate_err&nbsp;=&nbsp;%d
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j, getdate_err);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continue;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Call&nbsp;%d&nbsp;(\&quot;%s\&quot;)&nbsp;succeeded:
&quot;, j, argv[j]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_sec&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_sec);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_min&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_min);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_hour&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_hour);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mday&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_mday);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_mon&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_mon);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_year&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_year);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_wday&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_wday);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_yday&nbsp;<wbr>&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_yday);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tm_isdst&nbsp;=&nbsp;%d
&quot;, tmp-&gt;tm_isdst);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
