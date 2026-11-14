---
title: "varnishncsa(1)"
name: "varnishncsa"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishncsa/"
description: "varnishncsa – Display Varnish logs in Apache / NCSA combined log format"
---

<h2>NAME</h2>
<p> varnishncsa &#8211; Display Varnish logs in Apache / NCSA combined log format</p>
<h2>SYNOPSIS</h2>
<p> varnishncsa [-a] [-C] [-d] [-D] [-F format] [-g &lt;request|vxid&gt;] [-h] [-n name] [-N filename] [-P file] [-q query] [-V] [-w filename]</p>
<h2>DESCRIPTION</h2>
<p> The varnishncsa utility reads <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) shared memory logs and presents them in the Apache / NCSA &quot;combined&quot; log format. </p>
<p> Each log line produced is based on a single Request type transaction gathered from the shared memory log. The Request transaction is then scanned for the relevant parts in order to output one log line. To filter the log lines produced, use the query language to select the applicable transactions. Non-request transactions are ignored. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-a</code></p>
<dd> When writing output to a file, append to it rather than overwrite it.</p>
<dt><code>-C</code></p>
<dd> Do all regular expression and string matching caseless.</p>
<dt><code>-d</code></p>
<dd> Start processing log records at the head of the log instead of the tail.</p>
<dt><code>-D</code></p>
<dd> Daemonize.</p>
<dt><code>-F</code><i>&nbsp;<wbr>format</i></p>
<dd> Set the output log format string.</p>
<dt><code>-g</code><i>&nbsp;<wbr>&lt;request|vxid&gt;</i></p>
<dd> The grouping of the log records. The default is to group by vxid.</p>
<dt><code>-h</code></p>
<dd> Print program usage and exit</p>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></p>
<dd> Specify the name of the varnishd instance to get logs from. If -n is not specified, the host name is used.</p>
<dt><code>-N</code><i>&nbsp;<wbr>filename</i></p>
<dd> Specify the filename of a stale VSM instance. When using this option the abandonment checking is disabled.</p>
<dt><code>-P</code><i>&nbsp;<wbr>file</i></p>
<dd> Write the process&#8217; PID to the specified file.</p>
<dt><code>-q</code><i>&nbsp;<wbr>query</i></p>
<dd> Specifies the VSL query to use.</p>
<dt><code>-V</code></p>
<dd> Print version information and exit.</p>
<dt><code>-w</code><i>&nbsp;<wbr>filename</i></p>
<dd> Redirect output to file. The file will be overwritten unless the -a option was specified. If the application receives a SIGHUP the file will be reopened allowing the old one to be rotated away.</dl>
<h2>FORMAT</h2>
<p> Specify the log format used. If no format is specified the default log format is used. </p>
<p> The default log format is: </p>
<pre><code>
% h % l % u % t "%r" % s % b "%{Referer}i"
                             "%{User-agent}i"
</code></pre>
<p> Escape sequences 
 and 	 are supported. </p>
<p> Supported formatters are:</p>
<dl>
<dt><code>%b</code></p>
<dd> Size of response in bytes, excluding HTTP headers. In CLF format, i.e. a &#8216;-&#8216; rather than a 0 when no bytes are sent.</p>
<dt><code>%D</code></p>
<dd> Time taken to serve the request, in microseconds.</p>
<dt><code>%H</code></p>
<dd> The request protocol. Defaults to HTTP/1.0 if not known.</p>
<dt><code>%h</code></p>
<dd> Remote host. Defaults to &#8216;-&#8216; if not known.</p>
<dt><code>%I</code></p>
<dd> Total bytes received from client.</p>
<dt><code>%{X}i</code></p>
<dd> The contents of request header X.</p>
<dt><code>%l</code></p>
<dd> Remote logname (always &#8216;-&#8216;)</p>
<dt><code>%m</code></p>
<dd> Request method. Defaults to &#8216;-&#8216; if not known.</p>
<dt><code>%{X}o</code></p>
<dd> The contents of response header X.</p>
<dt><code>%O</code></p>
<dd> Total bytes sent to client.</p>
<dt><code>%q</code></p>
<dd> The query string, if no query string exists, an empty string.</p>
<dt><code>%r</code></p>
<dd> The first line of the request. Synthesized from other fields, so it may not be the request verbatim.</p>
<dt><code>%s</code></p>
<dd> Status sent to the client</p>
<dt><code>%t</code></p>
<dd> Time when the request was received, in HTTP date/time format.</p>
<dt><code>%{X}t</code></p>
<dd> Time when the request was received, in the format specified by X. The time specification format is the same as for <a href="/docs/linux/man/3-strftime/">strftime</a>(3).</p>
<dt><code>%T</code></p>
<dd> Time taken to serve the request, in seconds.</p>
<dt><code>%U</code></p>
<dd> The request URL without any query string. Defaults to &#8216;-&#8216; if not known.</p>
<dt><code>%u</code></p>
<dd> Remote user from auth</p>
<dt><code>%{X}x</code></p>
<dd> Extended variables. Supported variables are:</p>
<dt><code>Varnish:time_firstbyte</code></p>
<dd> Time from when the request processing starts until the first byte is sent to the client.</p>
<dt><code>Varnish:hitmiss</code></p>
<dd> Whether the request was a cache hit or miss. Pipe and pass are considered misses.</p>
<dt><code>Varnish:handling</code></p>
<dd> How the request was handled, whether it was a cache hit, miss, pass, pipe or error.</p>
<dt><code>VCL_Log:key</code></p>
<dd> Output value set by std.log(&quot;key:value&quot;) in VCL.</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd> Rotate the log file (see -w option)</p>
<dt><code>SIGUSR1</code></p>
<dd> Flush any outstanding transactions</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1) <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</p>
<h2>HISTORY</h2>
<p> The varnishncsa utility was developed by Poul-Henning Kamp in cooperation with Verdens Gang AS and Varnish Software AS. This manual page was initially written by Dag-Erling Smørgrav &lt;<i>des [at] des.no</i>&gt;, and later updated by Martin Blix Grydeland.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2006 Verdens Gang AS</p>
<dt>&bull;</p>
<dd> Copyright (c) 2006-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>
