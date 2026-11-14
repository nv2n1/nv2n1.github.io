---
title: "systemd(7)"
name: "systemd"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd/"
description: "systemd.time – Time and date specifications"
---

<p>systemd.time &#8211; Time and date specifications</p>
<h2>Description</h2>
<p>In systemd, timestamps, time spans, and calendar events are displayed and may be specified in closely related syntaxes.</p>
<h2>Displaying Time Spans</h2>
<p>Time spans refer to time durations. On display, systemd will present time spans as a space-separated series of time values each suffixed by a time unit. </p>
<dl>
<dd>
<pre>2h 30min</pre>
</dl>
<p> All specified time values are meant to be added up. The above hence refers to 150 minutes.</p>
<h2>Parsing Time Spans</h2>
<p>When parsing, systemd will accept the same time span syntax. Separating spaces may be omitted. The following time units are understood: </p>
<dl>
<dd>&bull; usec, us</dl>
<dl>
<dd>&bull; msec, ms</dl>
<dl>
<dd>&bull; seconds, second, sec, s</dl>
<dl>
<dd>&bull; minutes, minute, min, m</dl>
<dl>
<dd>&bull; hours, hour, hr, h</dl>
<dl>
<dd>&bull; days, day, d</dl>
<dl>
<dd>&bull; weeks, week, w</dl>
<dl>
<dd>&bull; months, month</dl>
<dl>
<dd>&bull; years, year, y</dl>
<p> If no time unit is specified, generally seconds are assumed, but some exceptions exist and are marked as such. In a few cases &quot;ns&quot;, &quot;nsec&quot; is accepted too, where the granularity of the time span allows for this. </p>
<p> Examples for valid time span specifications: </p>
<dl>
<dd>
<pre>2 h
2hours
48hr
1y 12month
55s500ms
300ms20s 5day</pre>
</dl>
<h2>Displaying Timestamps</h2>
<p>Timestamps refer to specific, unique points in time. On display, systemd will format these in the local timezone as follows: </p>
<dl>
<dd>
<pre>Fri 2012-11-23 23:02:15 CET</pre>
</dl>
<p> The weekday is printed according to the locale choice of the user.</p>
<h2>Parsing Timestamps</h2>
<p>When parsing systemd will accept a similar timestamp syntax, but excluding any timezone specification (this limitation might be removed eventually). The weekday specification is optional, but when the weekday is specified it must either be in the abbreviated (&quot;Wed&quot;) or non-abbreviated (&quot;Wednesday&quot;) English language form (case does not matter), and is not subject to the locale choice of the user. Either the date, or the time part may be omitted, in which case the current date or 00:00:00, resp., is assumed. The seconds component of the time may also be omitted, in which case &quot;:00&quot; is assumed. Year numbers may be specified in full or may be abbreviated (omitting the century). </p>
<p> A timestamp is considered invalid if a weekday is specified and the date does not actually match the specified day of the week. </p>
<p> When parsing, systemd will also accept a few special placeholders instead of timestamps: &quot;now&quot; may be used to refer to the current time (or of the invocation of the command that is currently executed). &quot;today&quot;, &quot;yesterday&quot;, &quot;tomorrow&quot; refer to 00:00:00 of the current day, the day before or the next day, respectively. </p>
<p> When parsing, systemd will also accept relative time specifications. A time span (see above) that is prefixed with &quot;+&quot; is evaluated to the current time plus the specified time span. Correspondingly, a time span that is prefixed with &quot;-&quot; is evaluated to the current time minus the specified time span. Instead of prefixing the time span with &quot;+&quot; or &quot;-&quot;, it may also be suffixed with a space and the word &quot;left&quot; or &quot;ago&quot;. </p>
<p> Finally, a timespan prefixed with &quot;@&quot; is evaluated relative to the UNIX time epoch 1st Jan, 1970, 00:00. </p>
<p> Examples for valid timestamps and their normalized form (assuming the current time was 2012-11-23 18:15:22): </p>
<dl>
<dd>
<pre>Fri 2012-11-23 11:12:13 → Fri 2012-11-23 11:12:13
 2012-11-23 11:12:13 → Fri 2012-11-23 11:12:13
 2012-11-23 → Fri 2012-11-23 00:00:00
 12-11-23 → Fri 2012-11-23 00:00:00
 11:12:13 → Fri 2012-11-23 11:12:13
 11:12 → Fri 2012-11-23 11:12:00
 now → Fri 2012-11-23 18:15:22
 today → Fri 2012-11-23 00:00:00
 yesterday → Fri 2012-11-22 00:00:00
 tomorrow → Fri 2012-11-24 00:00:00
 +3h30min → Fri 2012-11-23 21:45:22
 -5s → Fri 2012-11-23 18:15:17
 11min ago → Fri 2012-11-23 18:04:22
 @1395716396 → Tue 2014-03-25 03:59:56</pre>
</dl>
<p> Note that timestamps printed by systemd will not be parsed correctly by systemd, as the timezone specification is not accepted, and printing timestamps is subject to locale settings for the weekday while parsing only accepts English weekday names. </p>
<p> In some cases, systemd will display a relative timestamp (relative to the current time, or the time of invocation of the command) instead or in addition to an absolute timestamp as described above. A relative timestamp is formatted as follows: </p>
<p> 2 months 5 days ago </p>
<p> Note that any relative timestamp will also parse correctly where a timestamp is expected. (see above)</p>
<h2>Calendar Events</h2>
<p>Calendar events may be used to refer to one or more points in time in a single expression. They form a superset of the absolute timestamps explained above: </p>
<dl>
<dd>
<pre>Thu,Fri 2012-*-1,5 11:12:13</pre>
</dl>
<p> The above refers to 11:12:13 of the first or fifth day of any month of the year 2012, given that it is a Thursday or Friday. </p>
<p> The weekday specification is optional. If specified, it should consist of one or more English language weekday names, either in the abbreviated (Wed) or non-abbreviated (Wednesday) form (case does not matter), separated by commas. Specifying two weekdays separated by &quot;-&quot; refers to a range of continuous weekdays. &quot;,&quot; and &quot;-&quot; may be combined freely. </p>
<p> In the date and time specifications, any component may be specified as &quot;*&quot; in which case any value will match. Alternatively, each component can be specified as a list of values separated by commas. Values may also be suffixed with &quot;/&quot; and a repetition value, which indicates that the value and all values plus multiples of the repetition value are matched. </p>
<p> Either time or date specification may be omitted, in which case the current day and 00:00:00 is implied, respectively. If the second component is not specified, &quot;:00&quot; is assumed. </p>
<p> Timezone names may not be specified. </p>
<p> The special expressions &quot;minutely&quot;, &quot;hourly&quot;, &quot;daily&quot;, &quot;monthly&quot;, &quot;weekly&quot;, &quot;yearly&quot;, &quot;quarterly&quot;, &quot;semiannually&quot; may be used as calendar events which refer to &quot;*-*-*&nbsp;<wbr>*:*:00&quot;, &quot;*-*-*&nbsp;<wbr>*:00:00&quot;, &quot;*-*-*&nbsp;<wbr>00:00:00&quot;, &quot;*-*-01 00:00:00&quot;, &quot;Mon&nbsp;<wbr>*-*-*&nbsp;<wbr>00:00:00&quot;, &quot;*-01-01 00:00:00&quot;, &quot;*-01,04,07,10-01 00:00:0&quot; and &quot;*-01,07-01 00:00:00&quot; respectively. </p>
<p> Examples for valid timestamps and their normalized form: </p>
<dl>
<dd>
<pre> Sat,Thu,Mon-Wed,Sat-Sun → Mon-Thu,Sat,Sun *-*-* 00:00:00
 Mon,Sun 12-*-* 2,1:23 → Mon,Sun 2012-*-* 01,02:23:00
 Wed *-1 → Wed *-*-01 00:00:00
 Wed-Wed,Wed *-1 → Wed *-*-01 00:00:00
 Wed, 17:48 → Wed *-*-* 17:48:00
Wed-Sat,Tue 12-10-15 1:2:3 → Tue-Sat 2012-10-15 01:02:03
 *-*-7 0:0:0 → *-*-07 00:00:00
 10-15 → *-10-15 00:00:00
 monday *-12-* 17:00 → Mon *-12-* 17:00:00
 Mon,Fri *-*-3,1,2 *:30:45 → Mon,Fri *-*-01,02,03 *:30:45
 12,14,13,12:20,10,30 → *-*-* 12,13,14:10,20,30:00
 mon,fri *-1/2-1,3 *:30:45 → Mon,Fri *-01/2-01,03 *:30:45
 03-05 08:05:40 → *-03-05 08:05:40
 08:05:40 → *-*-* 08:05:40
 05:40 → *-*-* 05:40:00
 Sat,Sun 12-05 08:05:40 → Sat,Sun *-12-05 08:05:40
 Sat,Sun 08:05:40 → Sat,Sun *-*-* 08:05:40
 2003-03-05 05:40 → 2003-03-05 05:40:00
 2003-03-05 → 2003-03-05 00:00:00
 03-05 → *-03-05 00:00:00
 hourly → *-*-* *:00:00
 daily → *-*-* 00:00:00
 monthly → *-*-01 00:00:00
 weekly → Mon *-*-* 00:00:00
 yearly → *-01-01 00:00:00
 annually → *-01-01 00:00:00
 *:2/3 → *-*-* *:02/3:00</pre>
</dl>
<p> Calendar events are used by timer units, see <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5) for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
