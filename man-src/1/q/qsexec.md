---
title: "qsexec(1)"
name: "qsexec"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsexec/"
---

<h2 class="name">NAME</h2>
 

 qsexec - parses the data received via stdin and executes the defined command on a pattern match.

<h2>SYNOPSIS</h2>

 qsexec -e &lt;pattern&gt; [-t &lt;number&gt;:&lt;sec&gt;] [-c &lt;pattern&gt; [&lt;command string&gt;]] [-p] [-u &lt;user&gt;] &lt;command string&gt;

<h2>DESCRIPTION</h2>

 qsexec reads log lines from stdin and searches for the defined pattern. It executes the defined command string on pattern match.

<h2>OPTIONS</h2>

<dl>
<dt>-e &lt;pattern&gt;
<dd> Specifes the search pattern causing an event which shall trigger the command.
<dt>-t &lt;number&gt;:&lt;sec&gt;
<dd> Defines the number of pattern match within the the defined number of seconds in order to trigger the command execution. By default, every pattern match causes a command execution.
<dt>-c &lt;pattern&gt; [&lt;command string&gt;]
<dd> Pattern which clears the event counter. Executes optionally a command if an event command has been executed before.
<dt>-p
<dd> Writes data also to stdout (for piped logging).
<dt>-u &lt;name&gt;
<dd> Become another user, e.g. www-data.
<dt>&lt;command string&gt;
<dd> Defines the event command string where $0-$9 are substituted by the submatches of the regular expression.</dl>

<h2>EXAMPLE</h2>

 Executes the deny.sh script providing the IP address of the client causing a mod_qos(031) messages whenever the log message appears 10 times within at most one minute: 
&nbsp;<wbr>&nbsp;<wbr>ErrorLog&nbsp;<wbr>&quot;|qsexec -e&nbsp;<wbr>\'mod_qos\(031\).*, c=([0-9a-zA-Z:.]*)\'&nbsp;<wbr>-t 10:60&nbsp;<wbr>\'/bin/deny.sh&nbsp;<wbr>$1\'&quot; 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


