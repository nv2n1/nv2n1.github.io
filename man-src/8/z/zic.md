---
title: "zic(8)"
name: "zic"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zic/"
description: "zic – timezone compiler"
---

<p>zic &#8211; timezone compiler</p>
<h2>Synopsis</h2>
<p><code>zic</code> [ <i>option</i> &#8230; ] [ <i>filename</i> &#8230; ]</p>
<h2>Description</h2>
<p>The <code>zic</code> program reads text from the file(s) named on the command line and creates the time conversion information files specified in this input. If a <i>filename</i> is standard input is read.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Output version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd>Output short usage message and exit.</p>
<dt><code>-b </code><i>bloat</i></p>
<dd>Output backward-compatibility data as specified by <i>bloat</i>. If <i>bloat</i> is <code>fat</code>, generate additional data entries that work around potential bugs or incompatibilities in older software, such as software that mishandles the 64-bit generated data. If <i>bloat</i> is <code>slim</code>, keep the output files small; this can help check for the bugs and incompatibilities. Although the default is currently <code>fat</code>, this is intended to change in future <code>zic</code> versions, as software that mishandles the 64-bit data typically mishandles timestamps after the year 2038 anyway. Also see the <code>-r</code> option for another way to shrink output size.</p>
<dt><code>-d </code><i>directory</i></p>
<dd>Create time conversion information files in the named directory rather than in the standard directory named below.</p>
<dt><code>-l </code><i>timezone</i></p>
<dd>Use <i>timezone</i> as local time. <code>zic</code> will act as if the input contained a link line of the form </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; Link<tt>&nbsp;<wbr>&nbsp;</tt><i>timezone</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>localtime</p>
<dt><code>-L </code><i>leapsecondfilename</i></p>
<dd>Read leap second information from the file with the given name. If this option is not used, no leap second information appears in output files.</p>
<dt><code>-p </code><i>timezone</i></p>
<dd>Use <i>timezone</i>&#8216;s rules when handling nonstandard TZ strings like &quot;EET-2EEST&quot; that lack transition rules. <code>zic</code> will act as if the input contained a link line of the form </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; Link<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>timezone</i>posixrules</p>
<p> This feature is obsolete and poorly supported. Among other things it should not be used for timestamps after the year 2037, and it should not be combined with <code>-b slim</code> if <i>timezone</i>&#8216;s transitions are at standard time or Universal Time (UT) instead of local time.</p>
<dt><code>-r </code>[<code>@</code><i>lo</i>][<code>/@</code><i>hi</i>]</p>
<dd>Reduce the size of output files by limiting their applicability to timestamps in the range from <i>lo</i> (inclusive) to <i>hi</i> (exclusive), where <i>lo</i> and <i>hi</i> are possibly-signed decimal counts of seconds since the Epoch (1970-01-01 00:00:00 UTC). Omitted counts default to extreme values. For example, omits data intended for negative timestamps (i.e., before the Epoch), and outputs data intended only for nonnegative timestamps that fit into 31-bit signed integers. On platforms with GNU <code>date</code>, omits data intended for past timestamps. Also see the <code>-b slim</code> option for another way to shrink output size.</p>
<dt><code>-t </code><i>file</i></p>
<dd>When creating local time information, put the configuration link in the named file rather than in the standard location.</p>
<dt><code>-v</code></p>
<dd>Be more verbose, and complain about the following situations:</p>
<dl>
<dd>The input specifies a link to a link. </p>
<p> A year that appears in a data file is outside the range of representable years. </p>
<p> A time of 24:00 or more appears in the input. Pre-1998 versions of <code>zic</code> prohibit 24:00, and pre-2007 versions prohibit times greater than 24:00. </p>
<p> A rule goes past the start or end of the month. Pre-2004 versions of <code>zic</code> prohibit this. </p>
<p> A time zone abbreviation uses a <code>%z</code> format. Pre-2015 versions of <code>zic</code> do not support this. </p>
<p> A timestamp contains fractional seconds. Pre-2018 versions of <code>zic</code> do not support this. </p>
<p> The input contains abbreviations that are mishandled by pre-2018 versions of <code>zic</code> due to a longstanding coding bug. These abbreviations include for for for and for </p>
<p> The output file does not contain all the information about the long-term future of a timezone, because the future cannot be summarized as an extended POSIX TZ string. For example, as of 2019 this problem occurs for Iran&#8217;s daylight-saving rules for the predicted future, as these rules are based on the Iranian calendar, which cannot be represented. </p>
<p> The output contains data that may not be handled properly by client code designed for older <code>zic</code> output formats. These compatibility issues affect only timestamps before 1970 or after the start of 2038. </p>
<p> The output file contains more than 1200 transitions, which may be mishandled by some clients. The current reference client supports at most 2000 transitions; pre-2014 versions of the reference client support at most 1200 transitions. </p>
<p> A time zone abbreviation has fewer than 3 or more than 6 characters. POSIX requires at least 3, and requires implementations to support at least 6. </p>
<p> An output file name contains a byte that is not an ASCII letter, or or it contains a file name component that contains more than 14 bytes or that starts with</dl>
</dl>
<h2>Files</h2>
<p>Input files use the format described in this section; output files use <code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5) format. </p>
<p> Input files should be text files, that is, they should be a series of zero or more lines, each ending in a newline byte and containing at most 511 bytes, and without any NUL bytes. The input text&#8217;s encoding is typically UTF-8 or ASCII; it should have a unibyte representation for the POSIX Portable Character Set (PPCS) &lt;<a rel="nofollow" href="http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap06.html">http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap06.html</a>&gt; and the encoding&#8217;s non-unibyte characters should consist entirely of non-PPCS bytes. Non-PPCS characters typically occur only in comments: although output file names and time zone abbreviations can contain nearly any character, other software will work better if these are limited to the restricted syntax described under the <code>-v</code> option. </p>
<p> Input lines are made up of fields. Fields are separated from one another by one or more white space characters. The white space characters are space, form feed, carriage return, newline, tab, and vertical tab. Leading and trailing white space on input lines is ignored. An unquoted sharp character (#) in the input introduces a comment which extends to the end of the line the sharp character appears on. White space characters and sharp characters may be enclosed in double quotes (&quot;) if they&#8217;re to be used as part of a field. Any line that is blank (after comment stripping) is ignored. Nonblank lines are expected to be of one of three types: rule lines, zone lines, and link lines. </p>
<p> Names must be in English and are case insensitive. They appear in several contexts, and include month and weekday names and keywords such as <code>maximum</code>, <code>only</code>, <code>Rolling</code>, and <code>Zone</code>. A name can be abbreviated by omitting all but an initial prefix; any abbreviation must be unambiguous in context. </p>
<p> A rule line has the form </p>
<pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Rule NAME FROM TO TYPE IN ON AT SAVE LETTER/S
For example:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Rule US 1967 1973 - Apr lastSun 2:00w 1:00d D</pre>
<p>The fields that make up a rule line are:</p>
<dl>
<dt><code>NAME</code></p>
<dd>Gives the name of the rule set that contains this line. The name must start with a character that is neither an ASCII digit nor nor To allow for future extensions, an unquoted name should not contain characters from the set</p>
<dt><code>FROM</code></p>
<dd>Gives the first year in which the rule applies. Any signed integer year can be supplied; the proleptic Gregorian calendar is assumed, with year 0 preceding year 1. The word <code>minimum</code> (or an abbreviation) means the indefinite past. The word <code>maximum</code> (or an abbreviation) means the indefinite future. Rules can describe times that are not representable as time values, with the unrepresentable times ignored; this allows rules to be portable among hosts with differing time value types.</p>
<dt><code>TO</code></p>
<dd>Gives the final year in which the rule applies. In addition to <code>minimum</code> and <code>maximum</code> (as above), the word <code>only</code> (or an abbreviation) may be used to repeat the value of the <code>FROM</code> field.</p>
<dt><code>TYPE</code></p>
<dd>should be and is present for compatibility with older versions of <code>zic</code> in which it could contain year types.</p>
<dt><code>IN</code></p>
<dd>Names the month in which the rule takes effect. Month names may be abbreviated.</p>
<dt><code>ON</code></p>
<dd>Gives the day on which the rule takes effect. Recognized forms include: </p>
<pre>5 the fifth of the month
lastSun the last Sunday in the month
lastMon the last Monday in the month
Sun&gt;=8 first Sunday on or after the eighth
Sun&lt;=25 last Sunday on or before the 25th</pre>
<p>A weekday name (e.g., <code>Sunday</code>) or a weekday name preceded by (e.g., <code>lastSunday</code>) may be abbreviated or spelled out in full. There must be no white space characters within the <code>ON</code> field. The and constructs can result in a day in the neighboring month; for example, the IN-ON combination stands for the first Sunday on or after October 31, even if that Sunday occurs in November.</p>
<dt><code>AT</code></p>
<dd>Gives the time of day at which the rule takes effect, relative to 00:00, the start of a calendar day. Recognized forms include: </p>
<pre>2 time in hours
2:00 time in hours and minutes
01:28:14 time in hours, minutes, and seconds
00:19:32.13 time with fractional seconds
12:00 midday, 12 hours after 00:00
15:00 3 PM, 15 hours after 00:00
24:00 end of day, 24 hours after 00:00
260:00 260 hours after 00:00
-2:30 2.5 hours before 00:00
- equivalent to 0</pre>
<p>Although <code>zic</code> rounds times to the nearest integer second (breaking ties to the even integer), the fractions may be useful to other applications requiring greater precision. The source format does not specify any maximum precision. Any of these forms may be followed by the letter <code>w</code> if the given time is local or time, <code>s</code> if the given time is standard time without any adjustment for daylight saving, or <code>u</code> (or <code>g</code> or <code>z</code>) if the given time is universal time; in the absence of an indicator, local (wall clock) time is assumed. These forms ignore leap seconds; for example, if a leap second occurs at 00:59:60 local time, stands for 3601 seconds after local midnight instead of the usual 3600 seconds. The intent is that a rule line describes the instants when a clock/calendar set to the type of time specified in the <code>AT</code> field would show the specified date and time of day.</p>
<dt><code>SAVE</code></p>
<dd>Gives the amount of time to be added to local standard time when the rule is in effect, and whether the resulting time is standard or daylight saving. This field has the same format as the <code>AT</code> field except with a different set of suffix letters: <code>s</code> for standard time and <code>d</code> for daylight saving time. The suffix letter is typically omitted, and defaults to <code>s</code> if the offset is zero and to <code>d</code> otherwise. Negative offsets are allowed; in Ireland, for example, daylight saving time is observed in winter and has a negative offset relative to Irish Standard Time. The offset is merely added to standard time; for example, <code>zic</code> does not distinguish a 10:30 standard time plus an 0:30 <code>SAVE</code> from a 10:00 standard time plus a 1:00 <code>SAVE</code>.</p>
<dt><code>LETTER/S</code></p>
<dd>Gives the (for example, the or in or of time zone abbreviations to be used when this rule is in effect. If this field is the variable part is null.</dl>
<p> A zone line has the form </p>
<pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Zone NAME STDOFF RULES FORMAT [UNTIL]
For example:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Zone Asia/Amman 2:00 JordanEE%sT2017 Oct 27 01:00</pre>
<p>The fields that make up a zone line are:</p>
<dl>
<dt><code>NAME</code></p>
<dd>The name of the timezone. This is the name used in creating the time conversion information file for the timezone. It should not contain a file name component or a file name component is a maximal substring that does not contain</p>
<dt><code>STDOFF</code></p>
<dd>The amount of time to add to UT to get standard time, without any adjustment for daylight saving. This field has the same format as the <code>AT</code> and <code>SAVE</code> fields of rule lines; begin the field with a minus sign if time must be subtracted from UT.</p>
<dt><code>RULES</code></p>
<dd>The name of the rules that apply in the timezone or, alternatively, a field in the same format as a rule-line SAVE column, giving of the amount of time to be added to local standard time effect, and whether the resulting time is standard or daylight saving. If this field is <code>&#8211;</code> then standard time always applies. When an amount of time is given, only the sum of standard time and this amount matters.</p>
<dt><code>FORMAT</code></p>
<dd>The format for time zone abbreviations. The pair of characters <code>%s</code> is used to show where the of the time zone abbreviation goes. Alternatively, a format can use the pair of characters <code>%z</code> to stand for the UT offset in the form &plusmn;<i>hh</i>, &plusmn;<i>hhmm</i>, or &plusmn;<i>hhmmss</i>, using the shortest form that does not lose information, where <i>hh</i>, <i>mm</i>, and <i>ss</i> are the hours, minutes, and seconds east (+) or west (-) of UT. Alternatively, a slash (/) separates standard and daylight abbreviations. To conform to POSIX, a time zone abbreviation should contain only alphanumeric ASCII characters, and</p>
<dt><code>UNTIL</code></p>
<dd>The time at which the UT offset or the rule(s) change for a location. It takes the form of one to four fields YEAR [MONTH [DAY [TIME]]]. If this is specified, the time zone information is generated from the given UT offset and rule change until the time specified, which is interpreted using the rules in effect just before the transition. The month, day, and time of day have the same format as the IN, ON, and AT fields of a rule; trailing fields can be omitted, and default to the earliest possible value for the missing fields.</p>
<dd>The next line must be a line; this has the same form as a zone line except that the string and the name are omitted, as the continuation line will place information starting at the time specified as the information in the previous line in the file used by the previous line. Continuation lines may contain information, just as zone lines do, indicating that the next line is a further continuation.</dl>
<p> If a zone changes at the same instant that a rule would otherwise take effect in the earlier zone or continuation line, the rule is ignored. A zone or continuation line <i>L</i> with a named rule set starts with standard time by default: that is, any of <i>L</i>&#8216;s timestamps preceding <i>L</i>&#8216;s earliest rule use the rule in effect after <i>L</i>&#8216;s first transition into standard time. In a single zone it is an error if two rules take effect at the same instant, or if two zone changes take effect at the same instant. </p>
<p> A link line has the form </p>
<pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Link TARGET LINK-NAME
For example:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Link Europe/IstanbulAsia/Istanbul</pre>
<p>The <code>TARGET</code> field should appear as the <code>NAME</code> field in some zone line. The <code>LINK-NAME</code> field is used as an alternative name for that zone; it has the same syntax as a zone line&#8217;s <code>NAME</code> field. </p>
<p> Except for continuation lines, lines may appear in any order in the input. However, the behavior is unspecified if multiple zone or link lines define the same name, or if the source of one link line is the target of another. </p>
<p> The file that describes leap seconds can have leap lines and an expiration line. Leap lines have the following form: </p>
<pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Leap YEAR MONTH DAY HH:MM:SS CORR R/S
For example:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Leap 2016 Dec 31 23:59:60 + S</pre>
<p>The <code>YEAR</code>, <code>MONTH</code>, <code>DAY</code>, and <code>HH:MM:SS</code> fields tell when the leap second happened. The <code>CORR</code> field should be if a second was added or if a second was skipped. The <code>R/S</code> field should be (an abbreviation of) if the leap second time given by the other fields should be interpreted as UTC or (an abbreviation of) if the leap second time given by the other fields should be interpreted as local (wall clock) time. </p>
<p> The expiration line, if present, has the form: </p>
<pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Expires YEAR MONTH DAY HH:MM:SS
For example:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
Expires 2020 Dec 28 00:00:00</pre>
<p>The <code>YEAR</code>, <code>MONTH</code>, <code>DAY</code>, and <code>HH:MM:SS</code> fields give the expiration timestamp in UTC for the leap second table; <code>zic</code> outputs this expiration timestamp by truncating the end of the output file to the timestamp. If there is no expiration line, <code>zic</code> also accepts a comment where <i>E</i> is the expiration timestamp as a decimal integer count of seconds since the Epoch, not counting leap seconds. However, the comment is an obsolescent feature, and the leap second file should use an expiration line instead of relying on a comment.</p>
<h2>Extended Example</h2>
<p>Here is an extended example of <code>zic</code> input, intended to illustrate many of its features. In this example, the EU rules are for the European Union and for its predecessor organization, the European Communities. </p>
<pre># Rule NAME FROM TO TYPE IN ON AT SAVE LETTER/S
Rule Swiss 1941 1942 - May Mon&gt;=1 1:00 1:00 S
Rule Swiss 1941 1942 - Oct Mon&gt;=1 2:00 0 -
Rule EU 1977 1980 - Apr Sun&gt;=1 1:00u 1:00 S
Rule EU 1977 only - Sep lastSun 1:00u 0 -
Rule EU 1978 only - Oct 1 1:00u 0 -
Rule EU 1979 1995 - Sep lastSun 1:00u 0 -
Rule EU 1981 max - Mar lastSun 1:00u 1:00 S
Rule EU 1996 max - Oct lastSun 1:00u 0 -
# Zone NAME STDOFF RULES FORMAT [UNTIL]
Zone Europe/Zurich 0:34:08 - LMT 1853 Jul 16
 0:29:45.50 - BMT 1894 Jun
 1:00 Swiss CE%sT 1981
 1:00 EU CE%sT
Link Europe/Zurich Europe/Vaduz</pre>
<p>In this example, the timezone is named Europe/Zurich but it has an alias as Europe/Vaduz. This example says that Zurich was 34 minutes and 8 seconds east of UT until 1853-07-16 at 00:00, when the legal offset was changed to 7 degrees 26 minutes 22.50 seconds, which works out to 0:29:45.50; <code>zic</code> treats this by rounding it to 0:29:46. After 1894-06-01 at 00:00 the UT offset became one hour and Swiss daylight saving rules (defined with lines beginning with apply. From 1981 to the present, EU daylight saving rules have applied, and the UTC offset has remained at one hour. </p>
<p> In 1941 and 1942, daylight saving time applied from the first Monday in May at 01:00 to the first Monday in October at 02:00. The pre-1981 EU daylight-saving rules have no effect here, but are included for completeness. Since 1981, daylight saving has begun on the last Sunday in March at 01:00 UTC. Until 1995 it ended the last Sunday in September at 01:00 UTC, but this changed to the last Sunday in October starting in 1996. </p>
<p> For purposes of display, and were initially used, respectively. Since Swiss rules and later EU rules were applied, the time zone abbreviation has been CET for standard time and CEST for daylight saving time.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/localtime</i></p>
<dd>Default local timezone file.</p>
<dt><i>/usr/share/zoneinfo</i></p>
<dd>Default timezone information directory.</dl>
<h2>Notes</h2>
<p>For areas with more than two types of local time, you may need to use local standard time in the <code>AT</code> field of the earliest transition time&#8217;s rule to ensure that the earliest transition time recorded in the compiled file is correct. </p>
<p> If, for a particular timezone, a clock advance caused by the start of daylight saving coincides with and is equal to a clock retreat caused by a change in UT offset, <code>zic</code> produces a single transition to daylight saving at the new UT offset without any change in local (wall clock) time. To get separate transitions use multiple zone continuation lines specifying transition instants using universal time.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5), <code><a href="/docs/linux/man/8-zdump/">zdump</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
