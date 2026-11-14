---
title: "qslogger(1)"
name: "qslogger"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qslogger/"
---

<h2 class="name">NAME</h2>
 

 qslogger - another shell command interface to the system log module (syslog). 

<h2>SYNOPSIS</h2>

 qslogger [-r &lt;expression&gt;] [-t &lt;tag&gt;] [-f &lt;facility&gt;] [-l &lt;level&gt;] [-d &lt;level&gt;] [-p]

<h2>DESCRIPTION</h2>

 Use this utility to forward log messages to the systems syslog facility, e.g., to forward the messages to a remote host. It reads data from stdin.

<h2>OPTIONS</h2>

 

<dl>
<dt>-r &lt;expression&gt;
<dd> Specifies a regular expression which shall be used to determine the severity (syslog level) for each log line. The default pattern '^\[[0-9a-zA-Z :]+\] \[([a-z]+)\] ' can be used for Apache error log messages but you may configure your own pattern matching and other log format too. Use brackets to define the string enclosing the severity string. Default level (if severity can't be determined) is defined by the option '-d' (see below).
<dt>-t &lt;tag&gt;
<dd> Defines the tag name which shall be used to define the origin of the messages, e.g. 'httpd'.
<dt>-f &lt;facility&gt;
<dd> Defines the syslog facility. Default is 'daemon'.
<dt>-l &lt;level&gt;
<dd> Defines the minimal severity a message must have in order to be forwarded. Default is 'DEBUG'.
<dt>-d &lt;level&gt;
<dd> The default severity if the specified pattern (-r) does not match and the message's serverity can't be determined. Default is 'NOTICE'.
<dt>-p
<dd> Writes data also to stdout (for piped logging).</dl>

<h2>EXAMPLE</h2>

 
&nbsp;<wbr>&nbsp;<wbr>ErrorLog&nbsp;<wbr>&quot;|./qslogger -t apache -f local7&quot; 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


