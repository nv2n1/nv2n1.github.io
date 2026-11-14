---
title: "qsgrep(1)"
name: "qsgrep"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsgrep/"
---

<h2 class="name">NAME</h2>
 

 qsgrep - prints matching patterns within a file. 

<h2>SYNOPSIS</h2>

 qsgrep -e &lt;pattern&gt; -o &lt;sub string&gt; [&lt;path&gt;]

<h2>DESCRIPTION</h2>

 qsgrep is a simple tool to search patterns within files. It uses regular expressions to find patterns and prints the submatches within a pre-defined format string.

<h2>OPTIONS</h2>

<dl>
<dt>-e &lt;pattern&gt;
<dd> Specifes the search pattern.
<dt>-o &lt;string&gt;
<dd> Defines the output string where $0-$9 are substituted by the submatches of the regular expression.
<dt>&lt;path&gt;
<dd> Defines the input file to process. qsgrep reads from from standard input if this parameter is omitted. 

</dl>

<h2>EXAMPLE</h2>

 Shows the IP addresses of clients causing mod_qos(031) messages): 

 
&nbsp;<wbr>&nbsp;<wbr>qsgrep -e&nbsp;<wbr>'mod_qos\(031\).*, c=([a-zA-Z0-9:.]*)'&nbsp;<wbr>-o&nbsp;<wbr>'ip=$1'&nbsp;<wbr>error_log 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


