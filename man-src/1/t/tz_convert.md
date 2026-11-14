---
title: "tz_convert(1)"
name: "tz_convert"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tz_convert/"
description: "tz_convert – Timezone converter from operating system tz format into libical format used by Orage and several other calander tools."
---

<h2 class="name">NAME</h2>
<p> tz_convert &#8211; Timezone converter from operating system tz format into libical format used by Orage and several other calander tools. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>tz_convert [OPTION&#8230;] [INFILE]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>tz_convert</code></p>
<dd>is a command line tool, which can be used to convert timezone data from so called tz binary format, usually used in operating systems, to libical format, used by several calenders like Orage. </p>
<p> There are several options available to only convert certain files or files in certain directory. Or only convert part of the file and ignore for example old data. It is also possible to add new timezone files, which are based on old timezone data. </p>
<p> There are tools, which generate ical timezones data from tz source database, but those are often not available for normal users and are difficult to use. So often libical timezones are not upto date. <code>tz_convert</code> reads directly the binary tz data and makes it possible to keep libical timezones up to date. The tool is mainly meant to be used by distro maintainers, but it should be easy and clear enough for all users.</p>
<h2>FILES</h2>
<p> tz timezone files often can be found in directory <i>/usr/share/zoneinfo</i>. For example Europe/Helsinki. libical timezone files needs to be where you calendar can find them. For Xfce and Orage systems they are located under your Xfce directory in <i>share/orage/libical/zoneinfo</i>. For example Europe/Helsinki.ics. (use <code>locate</code> to find them.)</p>
<h2>OPTIONS</h2>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show this help message and exit.</dl>
<p> <code>&#8211;usage</code></p>
<dl>
<dt>
<dd> Show short usage summary.</dl>
<p> <code>-i</code>, <code>&#8211;infile</code></p>
<dl>
<dt>
<dd> tz file name from operating system to convert from. If this is directory, all files in it are processed. Default is <i>/usr/share/zoneinfo</i></dl>
<p> <code>-o</code>, <code>&#8211;outfile</code></p>
<dl>
<dt>
<dd> ical timezone file name to be written. This can not be directory. It is meant to be used together with timezone parameter. This is very seldom used. Default is timezone/<i>infile</i>.ics</dl>
<p> <code>-m</code>, <code>&#8211;message</code></p>
<dl>
<dt>
<dd> debug message level. How much exra information is shown. 0 is least and 10 is highest (1=default). May give usefull information when things do not work as expected.</dl>
<p> <code>-l</code>, <code>&#8211;limit</code></p>
<dl>
<dt>
<dd> limit processing to newer than this year. Often there is a lot of old data available, which is not needed in normal day to day work and skipping unused years helps to improve performance. Default is to ignore older than year 1970 time changes.</dl>
<p> <code>-t</code>, <code>&#8211;timezone</code></p>
<dl>
<dt>
<dd> timezone name to be used in the actual file. Normally file name is the same as timezone name, but if you want to create your own timezone, you need new file name, which contains some known timezone name. This is used together with outfile parameter.</dl>
<p> <code>-r</code>, <code>&#8211;norecursive</code></p>
<dl>
<dt>
<dd> process only main directory, instead of all subdirectories. 0 = recursive 1 = only main directory (0=default).</dl>
<p> <code>-c</code>, <code>&#8211;exclude count</code></p>
<dl>
<dt>
<dd> number of excluded directories. 5 = default (You only need this if you have more than 5 excluded directories). This is used together with exclude parameter.</dl>
<p> <code>-x</code>, <code>&#8211;exclude</code></p>
<dl>
<dt>
<dd> do not process this directory, skip it. You can give several directories with separate parameters. By default directories <i>right</i> and <i>posix</i> are excluded, but if you use this parameter, you have to specify those also. You need to use exclude count if you have more than 5 exclude directories.</dl>
<p> <code>-u</code>, <code>&#8211;norrule</code></p>
<dl>
<dt>
<dd> do not use RRULE ical repeating rule, but use RDATE instead. Not all calendars are able to understand RRULE correctly with timezones. (Orage should work fine with RRULE). 0 = use RRULE 1 = do not use RRULE (0=default).</dl>
<h2>BUGS</h2>
<p> Please report any bugs and enhancement requests to <i><a rel="nofollow" href="http://bugzilla.xfce.org/">http://bugzilla.xfce.org/</a></i>. Note that <code>tz_convert</code> is part of <code>orage</code> so bugs are reported against orage and component tz_convert. Usage related questions can be sent to <i>xfce [at] xfce.org</i> email list.</p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="http://www.xfce.org/projects/orage/">http://www.xfce.org/projects/orage/</a></i></p>
<h2>AUTHOR</h2>
<p> <code>tz_convert</code> was written by Juha Kautto &lt;juha [at] xfce.org&gt;. </p>
<p> This manual page was written by Juha Kautto &lt;juha [at] xfce.org&gt;. </p>
<h2>Index</h2>
