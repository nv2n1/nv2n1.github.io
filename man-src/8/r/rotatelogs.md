---
title: "rotatelogs(8)"
name: "rotatelogs"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rotatelogs/"
description: "rotatelogs – Piped logging program to rotate Apache logs"
---

<p>rotatelogs &#8211; Piped logging program to rotate Apache logs</p>
<h2>Synopsis</h2>
<p> <code>rotatelogs</code> [ &#8211;<code>l</code> ] [ &#8211;<code>L</code> <i>linkname</i> ] [ &#8211;<code>p</code> <i>program</i> ] [ &#8211;<code>f</code> ] [ &#8211;<code>D</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] [ &#8211;<code>e</code> ] [ &#8211;<code>c</code> ] [ &#8211;<code>n</code> <i>number-of-files</i> ] <i>logfile</i> <i>rotationtime</i>|<i>filesize</i>(B|K|M|G) [ <i>offset</i> ]<br />
&nbsp; </p>
<h2>Summary</h2>
<p>&nbsp; </p>
<p> <code>rotatelogs</code> is a simple program for use in conjunction with Apache&#8217;s piped logfile feature. It supports rotation based on a time interval or maximum size of the log.<br />
&nbsp;</p>
<h2>Options</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-l</code></p>
<dd>Causes the use of local time rather than GMT as the base for the interval or for <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> formatting with size-based rotation.</p>
<dt><code>-L</code> <i>linkname</i></p>
<dd></dl>
<dl>
<dt><code>-p</code> <i>program</i></p>
<dd>If given, <code>rotatelogs</code> will execute the specified program every time a new log file is opened. The filename of the newly opened file is passed as the first argument to the program. If executing after a rotation, the old log file is passed as the second argument. <code>rotatelogs</code> does not wait for the specified program to terminate before continuing to operate, and will not log any error code returned on termination. The spawned program uses the same stdin, stdout, and stderr as rotatelogs itself, and also inherits the environment.</p>
<dt><code>-f</code></p>
<dd>Causes the logfile to be opened immediately, as soon as <code>rotatelogs</code> starts, instead of waiting for the first logfile entry to be read (for non-busy sites, there may be a substantial delay between when the server is started and when the first request is handled, meaning that the associated logfile does not &quot;exist&quot; until then, which causes problems from some automated logging tools)</p>
<dt><code>-D</code></p>
<dd>Creates the parent directories of the path that the log file will be placed in if they do not already exist. This allows <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> formatting to be used in the path and not just the filename.</p>
<dt><code>-t</code></p>
<dd>Causes the logfile to be truncated instead of rotated. This is useful when a log is processed in real time by a command like tail, and there is no need for archived data. No suffix will be added to the filename, however format strings containing &#8216;%&#8217; characters will be respected.</p>
<dt><code>-v</code></p>
<dd>Produce verbose output on STDERR. The output contains the result of the configuration parsing, and all file open and close actions.</p>
<dt><code>-e</code></p>
<dd>Echo logs through to stdout. Useful when logs need to be further processed in real time by a further tool in the chain.</p>
<dt><code>-c</code></p>
<dd>Create log file for each interval, even if empty.</p>
<dt><code>-n </code><i>number-of-files</i></p>
<dd>Use a circular list of filenames without timestamps. With -n 3, the series of log files opened would be &quot;logfile&quot;, &quot;logfile.1&quot;, &quot;logfile.2&quot;, then overwriting &quot;logfile&quot;. Available in 2.4.5 and later.</p>
<dt><i>logfile</i></p>
<dd></dl>
<dl>
<dt><i>rotationtime</i></p>
<dd>The time between log file rotations in seconds. The rotation occurs at the beginning of this interval. For example, if the rotation time is 3600, the log file will be rotated at the beginning of every hour; if the rotation time is 86400, the log file will be rotated every night at midnight. (If no data is logged during an interval, no file will be created.)</p>
<dt><i>filesize</i>(B|K|M|G)</p>
<dd>The maximum file size in followed by exactly one of the letters <code>B</code> (Bytes), <code>K</code> (KBytes), <code>M</code> (MBytes) or <code>G</code> (GBytes). .PP When time and size are specified, the size must be given after the time. Rotation will occur whenever either time or size limits are reached.</p>
<dt><i>offset</i></p>
<dd>The number of minutes offset from UTC. If omitted, zero is assumed and UTC is used. For example, to use local time in the zone UTC -5 hours, specify a value of <code>-300</code> for this argument. In most cases, <code>-l</code> should be used instead of specifying an offset.<br />
&nbsp;</dl>
<h2>Examples</h2>
<p>&nbsp; </p>
<pre> CustomLog &quot;|bin/rotatelogs /var/log/logfile 86400&quot; common</pre>
<p>&nbsp; </p>
<p> This creates the files /var/log/logfile.nnnn where nnnn is the system time at which the log nominally starts (this time will always be a multiple of the rotation time, so you can synchronize cron scripts with it). At the end of each rotation time (here after 24 hours) a new log is started.<br />
&nbsp; </p>
<pre> CustomLog &quot;|bin/rotatelogs -l /var/log/logfile.%Y.%m.%d 86400&quot; common</pre>
<p>&nbsp; </p>
<p> This creates the files /var/log/logfile.yyyy.mm.dd where yyyy is the year, mm is the month, and dd is the day of the month. Logging will switch to a new file every day at midnight, local time.<br />
&nbsp; </p>
<pre> CustomLog &quot;|bin/rotatelogs /var/log/logfile 5M&quot; common</pre>
<p>&nbsp; </p>
<p> This configuration will rotate the logfile whenever it reaches a size of 5 megabytes.<br />
&nbsp; </p>
<pre> ErrorLog &quot;|bin/rotatelogs /var/log/errorlog.%Y-%m-%d-%H_%M_%S 5M&quot;</pre>
<p>&nbsp; </p>
<p> This configuration will rotate the error logfile whenever it reaches a size of 5 megabytes, and the suffix to the logfile name will be created of the form <code>errorlog.YYYY-mm-dd-HH_MM_SS</code>.<br />
&nbsp; </p>
<pre> CustomLog &quot;|bin/rotatelogs -t /var/log/logfile 86400&quot; common</pre>
<p>&nbsp; </p>
<p> This creates the file /var/log/logfile, truncating the file at startup and then truncating the file once per day. It is expected in this scenario that a separate process (such as tail) would process the file in real time.<br />
&nbsp;</p>
<h2>Portability</h2>
<p>&nbsp; </p>
<p> The following logfile format string substitutions should be supported by all <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> implementations, see the <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> man page for library-specific extensions.<br />
&nbsp;<wbr>&nbsp; </p>
<dl>
<dt>&bull; <font SIZE="-1"><code>%A</code></font> &#8211; full weekday name (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%a</code></font> &#8211; 3-character weekday name (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%B</code></font> &#8211; full month name (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%b</code></font> &#8211; 3-character month name (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%c</code></font> &#8211; date and time (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%d</code></font> &#8211; 2-digit day of month</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%H</code></font> &#8211; 2-digit hour (24 hour clock)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%I</code></font> &#8211; 2-digit hour (12 hour clock)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%j</code></font> &#8211; 3-digit day of year</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%M</code></font> &#8211; 2-digit minute</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%m</code></font> &#8211; 2-digit month</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%p</code></font> &#8211; am/pm of 12 hour clock (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%S</code></font> &#8211; 2-digit second</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%U</code></font> &#8211; 2-digit week of year (Sunday first day of week)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%W</code></font> &#8211; 2-digit week of year (Monday first day of week)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%w</code></font> &#8211; 1-digit weekday (Sunday first day of week)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%X</code></font> &#8211; time (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%x</code></font> &#8211; date (localized)</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%Y</code></font> &#8211; 4-digit year</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%y</code></font> &#8211; 2-digit year</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%Z</code></font> &#8211; time zone name</p>
<dd>&nbsp; </p>
<dt>&bull; <font SIZE="-1"><code>%%</code></font> &#8211; literal `%&#8217;</p>
<dd>&nbsp;<wbr>&nbsp; </p>
</dl>
