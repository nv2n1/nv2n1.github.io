---

title: "date(1)"
name: "date"
section: "1"
letter: "d"
url: "/docs/linux/man/1-date/"
description: "date – print or set the system date and time"
---

<p> date &#8211; print or set the system date and time </p>
<h2>SYNOPSIS</h2>
<p> <code>date</code> [<i>,OPTION/</i>]&#8230; [<i>,+FORMAT/</i>]<br/>
 <code>date</code> [<i>,-u|&#8211;utc|&#8211;universal/</i>] [<i>,MMDDhhmm/</i>[[<i>,CC/</i>]<i>,YY/</i>][<i>,.ss/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Display the current time in the given FORMAT, or set the system date. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;date</code>=<i>,STRING/</i></dt>
<dd> display time described by STRING, not &#8216;now&#8217;</dd>
<dt><code>&#8211;debug</code></dt>
<dd> annotate the parsed date, and warn about questionable usage to stderr</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>,DATEFILE/</i></dt>
<dd> like <code>&#8211;date</code>; once for each line of DATEFILE</dd>
<dt><code>-I[FMT]</code>, <code>&#8211;iso-8601</code>[=<i>,FMT/</i>]</dt>
<dd> output date/time in ISO 8601 format. FMT=&#8217;date&#8217; for date only (the default), &#8216;hours&#8217;, &#8216;minutes&#8217;, &#8216;seconds&#8217;, or &#8216;ns&#8217; for date and time to the indicated precision. Example: 2006-08-14T02:34:56-06:00</dd>
<dt><code>-R</code>, <code>&#8211;rfc-email</code></dt>
<dd> output date and time in RFC 5322 format. Example: Mon, 14 Aug 2006 02:34:56 <code>-0600</code></dd>
<dt><code>&#8211;rfc-3339</code>=<i>,FMT/</i></dt>
<dd> output date/time in RFC 3339 format. FMT=&#8217;date&#8217;, &#8216;seconds&#8217;, or &#8216;ns&#8217; for date and time to the indicated precision. Example: 2006-08-14 02:34:56-06:00</dd>
<dt><code>-r</code>, <code>&#8211;reference</code>=<i>,FILE/</i></dt>
<dd> display the last modification time of FILE</dd>
<dt><code>-s</code>, <code>&#8211;set</code>=<i>,STRING/</i></dt>
<dd> set time described by STRING</dd>
<dt><code>-u</code>, <code>&#8211;utc</code>, <code>&#8211;universal</code></dt>
<dd> print or set Coordinated Universal Time (UTC)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> FORMAT controls the output. Interpreted sequences are:</p>
<dl>
<dt>%%</dt>
<dd> a literal %</dd>
<dt>%a</dt>
<dd> locale&#8217;s abbreviated weekday name (e.g., Sun)</dd>
<dt>%A</dt>
<dd> locale&#8217;s full weekday name (e.g., Sunday)</dd>
<dt>%b</dt>
<dd> locale&#8217;s abbreviated month name (e.g., Jan)</dd>
<dt>%B</dt>
<dd> locale&#8217;s full month name (e.g., January)</dd>
<dt>%c</dt>
<dd> locale&#8217;s date and time (e.g., Thu Mar 3 23:05:25 2005)</dd>
<dt>%C</dt>
<dd> century; like %Y, except omit last two digits (e.g., 20)</dd>
<dt>%d</dt>
<dd> day of month (e.g., 01)</dd>
<dt>%D</dt>
<dd> date; same as %m/%d/%y</dd>
<dt>%e</dt>
<dd> day of month, space padded; same as %_d</dd>
<dt>%F</dt>
<dd> full date; like %+4Y-%m-%d</dd>
<dt>%g</dt>
<dd> last two digits of year of ISO week number (see %G)</dd>
<dt>%G</dt>
<dd> year of ISO week number (see %V); normally useful only with %V</dd>
<dt>%h</dt>
<dd> same as %b</dd>
<dt>%H</dt>
<dd> hour (00..23)</dd>
<dt>%I</dt>
<dd> hour (01..12)</dd>
<dt>%j</dt>
<dd> day of year (001..366)</dd>
<dt>%k</dt>
<dd> hour, space padded ( 0..23); same as %_H</dd>
<dt>%l</dt>
<dd> hour, space padded ( 1..12); same as %_I</dd>
<dt>%m</dt>
<dd> month (01..12)</dd>
<dt>%M</dt>
<dd> minute (00..59)</dd>
<dt>%n</dt>
<dd> a newline</dd>
<dt>%N</dt>
<dd> nanoseconds (000000000..999999999)</dd>
<dt>%p</dt>
<dd> locale&#8217;s equivalent of either AM or PM; blank if not known</dd>
<dt>%P</dt>
<dd> like %p, but lower case</dd>
<dt>%q</dt>
<dd> quarter of year (1..4)</dd>
<dt>%r</dt>
<dd> locale&#8217;s 12-hour clock time (e.g., 11:11:04 PM)</dd>
<dt>%R</dt>
<dd> 24-hour hour and minute; same as %H:%M</dd>
<dt>%s</dt>
<dd> seconds since 1970-01-01 00:00:00 UTC</dd>
<dt>%S</dt>
<dd> second (00..60)</dd>
<dt>%t</dt>
<dd> a tab</dd>
<dt>%T</dt>
<dd> time; same as %H:%M:%S</dd>
<dt>%u</dt>
<dd> day of week (1..7); 1 is Monday</dd>
<dt>%U</dt>
<dd> week number of year, with Sunday as first day of week (00..53)</dd>
<dt>%V</dt>
<dd> ISO week number, with Monday as first day of week (01..53)</dd>
<dt>%w</dt>
<dd> day of week (0..6); 0 is Sunday</dd>
<dt>%W</dt>
<dd> week number of year, with Monday as first day of week (00..53)</dd>
<dt>%x</dt>
<dd> locale&#8217;s date representation (e.g., 12/31/99)</dd>
<dt>%X</dt>
<dd> locale&#8217;s time representation (e.g., 23:13:48)</dd>
<dt>%y</dt>
<dd> last two digits of year (00..99)</dd>
<dt>%Y</dt>
<dd> year</dd>
<dt>%z</dt>
<dd> +hhmm numeric time zone (e.g., <code>-0400</code>)</dd>
<dt>%:z</dt>
<dd> +hh:mm numeric time zone (e.g., <code>-04</code>:00)</dd>
<dt>%::z</dt>
<dd> +hh:mm:ss numeric time zone (e.g., <code>-04</code>:00:00)</dd>
<dt>%:::z</dt>
<dd> numeric time zone with : to necessary precision (e.g., <code>-04</code>, +05:30)</dd>
<dt>%Z</dt>
<dd> alphabetic time zone abbreviation (e.g., EDT)</dd></dl>
<p> By default, date pads numeric fields with zeroes. The following optional flags may follow &#8216;%&#8217;:</p>
<dl>
<dt>&#8211;</dt>
<dd> (hyphen) do not pad the field</dd>
<dt>_</dt>
<dd> (underscore) pad with spaces</dd>
<dt>0</dt>
<dd> (zero) pad with zeros</dd>
<dt>+</dt>
<dd> pad with zeros, and put &#8216;+&#8217; before future years with &gt;4 digits</dd>
<dt>^</dt>
<dd> use upper case if possible</dd>
<dt>#</dt>
<dd> use opposite case if possible</dd></dl>
<p> After any flags comes an optional field width, as a decimal number; then an optional modifier, which is either E to use the locale&#8217;s alternate representations if available, or O to use the locale&#8217;s alternate numeric symbols if available.</p>
<h2>EXAMPLES</h2>
<p> Convert seconds since the epoch (1970-01-01 UTC) to a date</p>
<dl>
<dt>
</dt><dd> <tt>$ date --date='@2147483647'</tt></dd></dl>
<p> Show the time on the west coast of the US (use <a href="/docs/linux/man/1-tzselect/">tzselect</a>(1) to find TZ)</p>
<dl>
<dt>
</dt><dd> <tt>$ TZ='America/Los_Angeles' date</tt></dd></dl>
<p> Show the local time for 9AM next Friday on the west coast of the US</p>
<dl>
<dt>
</dt><dd> <tt>$ date --date='TZ=&quot;America/Los_Angeles&quot; 09:00 next Fri'</tt></dd></dl>
<h2>DATE STRING</h2>
<p> The &#8211;date=STRING is a mostly free format human readable date string such as &quot;Sun, 29 Feb 2004 16:21:42 -0800&quot; or &quot;2004-02-29 16:21:42&quot; or even &quot;next Thursday&quot;. A date string may contain items indicating calendar date, time of day, time zone, day of week, relative time, relative date, and numbers. An empty string indicates the beginning of the day. The date string format is more complex than is easily documented here but is fully described in the info documentation.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/date">https://www.gnu.org/software/coreutils/date</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) date invocation&#8217; </p>
