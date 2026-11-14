---
title: "qsrotate(1)"
name: "qsrotate"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsrotate/"
---

<h2 class="name">NAME</h2>
 

 qsrotate - a log rotation tool (similar to Apache's rotatelogs). 

<h2>SYNOPSIS</h2>

 qsrotate -o &lt;file&gt; [-s &lt;sec&gt; [-t &lt;hours&gt;]] [-f] [-z] [-g &lt;num&gt;] [-u &lt;name&gt;] [-p]

<h2>DESCRIPTION</h2>

 qsrotate reads from stdin (piped log) and writes the data to the provided file rotating the file after the specified time.

<h2>OPTIONS</h2>

<dl>
<dt>-o &lt;file&gt;
<dd> Output log file to write the data to (use an absolute path).
<dt>-s &lt;sec&gt;
<dd> Rotation interval in seconds, default are 86400 seconds.
<dt>-t &lt;hours&gt;
<dd> Offset to UTC (enables also DST support), default is 0.
<dt>-b &lt;bytes&gt;
<dd> File size limitation (default are 2147352576 bytes).
<dt>-f
<dd> Forced log rotation even no data is written.
<dt>-z
<dd> Compress (gzip) the rotated file.
<dt>-g &lt;num&gt;
<dd> Generations (number of files to keep).
<dt>-u &lt;name&gt;
<dd> Become another user, e.g. www-data.
<dt>-p
<dd> Writes data also to stdout (for piped logging).</dl>

<h2>EXAMPLE</h2>

 
&nbsp;<wbr>&nbsp;<wbr>TransferLog&nbsp;<wbr>&quot;|qsrotate -f -z -g 3 -o&nbsp;<wbr>/dest/file -s 86400&quot; 

 The name of the rotated file will be /dest/filee.YYYYmmddHHMMSS where YYYYmmddHHMMSS is the system time at which the data has been rotated.

<h2>NOTE</h2>

 Each qsrotate instance must use an individual file.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


