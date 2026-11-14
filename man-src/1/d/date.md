---
title: "date(1)"
name: "date"
section: "1"
letter: "d"
url: "/docs/linux/man/1-date/"
description: "date – print or set the system date and time"
---

<h2 class="name">NAME</h2>
<p> date &#8211; print or set the system date and time </p>
<h2>SYNOPSIS</h2>
<p> <code>date</code> [<i>,OPTION/</i>]&#8230; [<i>,+FORMAT/</i>]<br />
 <code>date</code> [<i>,-u|&#8211;utc|&#8211;universal/</i>] [<i>,MMDDhhmm/</i>[[<i>,CC/</i>]<i>,YY/</i>][<i>,.ss/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Display the current time in the given FORMAT, or set the system date. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;date</code>=<i>,STRING/</i></p>
<dd> display time described by STRING, not &#8216;now&#8217;</p>
<dt><code>&#8211;debug</code></p>
<dd> annotate the parsed date, and warn about questionable usage to stderr</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>,DATEFILE/</i></p>
<dd> like <code>&#8211;date</code>; once for each line of DATEFILE</p>
<dt><code>-I[FMT]</code>, <code>&#8211;iso-8601</code>[=<i>,FMT/</i>]</p>
<dd> output date/time in ISO 8601 format. FMT=&#8217;date&#8217; for date only (the default), &#8216;hours&#8217;, &#8216;minutes&#8217;, &#8216;seconds&#8217;, or &#8216;ns&#8217; for date and time to the indicated precision. Example: 2006-08-14T02:34:56-06:00</p>
<dt><code>-R</code>, <code>&#8211;rfc-email</code></p>
<dd> output date and time in RFC 5322 format. Example: Mon, 14 Aug 2006 02:34:56 <code>-0600</code></p>
<dt><code>&#8211;rfc-3339</code>=<i>,FMT/</i></p>
<dd> output date/time in RFC 3339 format. FMT=&#8217;date&#8217;, &#8216;seconds&#8217;, or &#8216;ns&#8217; for date and time to the indicated precision. Example: 2006-08-14 02:34:56-06:00</p>
<dt><code>-r</code>, <code>&#8211;reference</code>=<i>,FILE/</i></p>
<dd> display the last modification time of FILE</p>
<dt><code>-s</code>, <code>&#8211;set</code>=<i>,STRING/</i></p>
<dd> set time described by STRING</p>
<dt><code>-u</code>, <code>&#8211;utc</code>, <code>&#8211;universal</code></p>
<dd> print or set Coordinated Universal Time (UTC)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> FORMAT controls the output. Interpreted sequences are:</p>
<dl>
<dt>%%</p>
<dd> a literal %</p>
<dt>%a</p>
<dd> locale&#8217;s abbreviated weekday name (e.g., Sun)</p>
<dt>%A</p>
<dd> locale&#8217;s full weekday name (e.g., Sunday)</p>
<dt>%b</p>
<dd> locale&#8217;s abbreviated month name (e.g., Jan)</p>
<dt>%B</p>
<dd> locale&#8217;s full month name (e.g., January)</p>
<dt>%c</p>
<dd> locale&#8217;s date and time (e.g., Thu Mar 3 23:05:25 2005)</p>
<dt>%C</p>
<dd> century; like %Y, except omit last two digits (e.g., 20)</p>
<dt>%d</p>
<dd> day of month (e.g., 01)</p>
<dt>%D</p>
<dd> date; same as %m/%d/%y</p>
<dt>%e</p>
<dd> day of month, space padded; same as %_d</p>
<dt>%F</p>
<dd> full date; like %+4Y-%m-%d</p>
<dt>%g</p>
<dd> last two digits of year of ISO week number (see %G)</p>
<dt>%G</p>
<dd> year of ISO week number (see %V); normally useful only with %V</p>
<dt>%h</p>
<dd> same as %b</p>
<dt>%H</p>
<dd> hour (00..23)</p>
<dt>%I</p>
<dd> hour (01..12)</p>
<dt>%j</p>
<dd> day of year (001..366)</p>
<dt>%k</p>
<dd> hour, space padded ( 0..23); same as %_H</p>
<dt>%l</p>
<dd> hour, space padded ( 1..12); same as %_I</p>
<dt>%m</p>
<dd> month (01..12)</p>
<dt>%M</p>
<dd> minute (00..59)</p>
<dt>%n</p>
<dd> a newline</p>
<dt>%N</p>
<dd> nanoseconds (000000000..999999999)</p>
<dt>%p</p>
<dd> locale&#8217;s equivalent of either AM or PM; blank if not known</p>
<dt>%P</p>
<dd> like %p, but lower case</p>
<dt>%q</p>
<dd> quarter of year (1..4)</p>
<dt>%r</p>
<dd> locale&#8217;s 12-hour clock time (e.g., 11:11:04 PM)</p>
<dt>%R</p>
<dd> 24-hour hour and minute; same as %H:%M</p>
<dt>%s</p>
<dd> seconds since 1970-01-01 00:00:00 UTC</p>
<dt>%S</p>
<dd> second (00..60)</p>
<dt>%t</p>
<dd> a tab</p>
<dt>%T</p>
<dd> time; same as %H:%M:%S</p>
<dt>%u</p>
<dd> day of week (1..7); 1 is Monday</p>
<dt>%U</p>
<dd> week number of year, with Sunday as first day of week (00..53)</p>
<dt>%V</p>
<dd> ISO week number, with Monday as first day of week (01..53)</p>
<dt>%w</p>
<dd> day of week (0..6); 0 is Sunday</p>
<dt>%W</p>
<dd> week number of year, with Monday as first day of week (00..53)</p>
<dt>%x</p>
<dd> locale&#8217;s date representation (e.g., 12/31/99)</p>
<dt>%X</p>
<dd> locale&#8217;s time representation (e.g., 23:13:48)</p>
<dt>%y</p>
<dd> last two digits of year (00..99)</p>
<dt>%Y</p>
<dd> year</p>
<dt>%z</p>
<dd> +hhmm numeric time zone (e.g., <code>-0400</code>)</p>
<dt>%:z</p>
<dd> +hh:mm numeric time zone (e.g., <code>-04</code>:00)</p>
<dt>%::z</p>
<dd> +hh:mm:ss numeric time zone (e.g., <code>-04</code>:00:00)</p>
<dt>%:::z</p>
<dd> numeric time zone with : to necessary precision (e.g., <code>-04</code>, +05:30)</p>
<dt>%Z</p>
<dd> alphabetic time zone abbreviation (e.g., EDT)</dl>
<p> By default, date pads numeric fields with zeroes. The following optional flags may follow &#8216;%&#8217;:</p>
<dl>
<dt>&#8211;</p>
<dd> (hyphen) do not pad the field</p>
<dt>_</p>
<dd> (underscore) pad with spaces</p>
<dt>0</p>
<dd> (zero) pad with zeros</p>
<dt>+</p>
<dd> pad with zeros, and put &#8216;+&#8217; before future years with &gt;4 digits</p>
<dt>^</p>
<dd> use upper case if possible</p>
<dt>#</p>
<dd> use opposite case if possible</dl>
<p> After any flags comes an optional field width, as a decimal number; then an optional modifier, which is either E to use the locale&#8217;s alternate representations if available, or O to use the locale&#8217;s alternate numeric symbols if available.</p>
<h2>EXAMPLES</h2>
<p> Convert seconds since the epoch (1970-01-01 UTC) to a date</p>
<dl>
<dt>
<dd> <tt>$ date --date='@2147483647'</tt></dl>
<p> Show the time on the west coast of the US (use <a href="/docs/linux/man/1-tzselect/">tzselect</a>(1) to find TZ)</p>
<dl>
<dt>
<dd> <tt>$ TZ='America/Los_Angeles' date</tt></dl>
<p> Show the local time for 9AM next Friday on the west coast of the US</p>
<dl>
<dt>
<dd> <tt>$ date --date='TZ=&quot;America/Los_Angeles&quot; 09:00 next Fri'</tt></dl>
<h2>DATE STRING</h2>
<p> The &#8211;date=STRING is a mostly free format human readable date string such as &quot;Sun, 29 Feb 2004 16:21:42 -0800&quot; or &quot;2004-02-29 16:21:42&quot; or even &quot;next Thursday&quot;. A date string may contain items indicating calendar date, time of day, time zone, day of week, relative time, relative date, and numbers. An empty string indicates the beginning of the day. The date string format is more complex than is easily documented here but is fully described in the info documentation.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/date">https://www.gnu.org/software/coreutils/date</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) date invocation&#8217; </p>
<h2>Index</h2>
