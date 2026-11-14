---
title: "varnishlog(1)"
name: "varnishlog"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishlog/"
description: "varnishlog – Display Varnish logs"
---

<h2>NAME</h2>
<p> varnishlog &#8211; Display Varnish logs</p>
<h2>SYNOPSIS</h2>
<p> varnishlog [-a] [-b] [-B] [-c] [-C] [-d] [-D] [-g &lt;session|request|vxid|raw&gt;] [-h] [-i taglist] [-I &lt;[taglist:]regex&gt;] [-k num] [-L limit] [-n name] [-N filename] [-P file] [-q query] [-r filename] [-T seconds] [-v] [-V] [-w filename] [-x taglist] [-X &lt;[taglist:]regex&gt;]</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-a</code></p>
<dd> When writing output to a file, append to it rather than overwrite it.</p>
<dt><code>-b</code></p>
<dd> Only display transactions and log records coming from backend communication.</p>
<dt><code>-B</code></p>
<dd> Output binary data suitable for reading with -r. The -w option specifies where the binary output is written.</p>
<dt><code>-c</code></p>
<dd> Only display transactions and log records coming from client communication.</p>
<dt><code>-C</code></p>
<dd> Do all regular expression and string matching caseless.</p>
<dt><code>-d</code></p>
<dd> Start processing log records at the head of the log instead of the tail.</p>
<dt><code>-D</code></p>
<dd> Daemonize.</p>
<dt><code>-g</code><i>&nbsp;<wbr>&lt;session|request|vxid|raw&gt;</i></p>
<dd> The grouping of the log records. The default is to group by vxid.</p>
<dt><code>-h</code></p>
<dd> Print program usage and exit</p>
<dt><code>-i</code><i>&nbsp;<wbr>taglist</i></p>
<dd> Include log records of these tags in output. Taglist is a comma-separated list of tag globs. Multiple -i options may be given. </p>
<p> If a tag include option is the first of any tag selection options, all tags are first marked excluded.</p>
<dt><code>-I</code><i>&nbsp;<wbr>&lt;[taglist:]regex&gt;</i></p>
<dd> Include by regex matching. Output only records matching taglist and regular expression. Applies to any tag if taglist is absent. </p>
<p> If a tag include option is the first of any tag selection options, all tags are first marked excluded.</p>
<dt><code>-k</code><i>&nbsp;<wbr>num</i></p>
<dd> Process this number of matching log transactions before exiting.</p>
<dt><code>-L</code><i>&nbsp;<wbr>limit</i></p>
<dd> Sets the upper limit of incomplete transactions kept before the oldest transaction is force completed. A warning record is synthesized when this happens. This setting keeps an upper bound on the memory usage of running queries. Defaults to 1000 transactions.</p>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></p>
<dd> Specify the name of the varnishd instance to get logs from. If -n is not specified, the host name is used.</p>
<dt><code>-N</code><i>&nbsp;<wbr>filename</i></p>
<dd> Specify the filename of a stale VSM instance. When using this option the abandonment checking is disabled.</p>
<dt><code>-P</code><i>&nbsp;<wbr>file</i></p>
<dd> Write the process&#8217; PID to the specified file.</p>
<dt><code>-q</code><i>&nbsp;<wbr>query</i></p>
<dd> Specifies the VSL query to use.</p>
<dt><code>-r</code><i>&nbsp;<wbr>filename</i></p>
<dd> Read log in binary file format from this file. The file can be created with <code>varnishlog -B -w filename</code>.</p>
<dt><code>-T</code><i>&nbsp;<wbr>seconds</i></p>
<dd> Sets the transaction timeout in seconds. This defines the maximum number of seconds elapsed between a Begin tag and the End tag. If the timeout expires, a warning record is synthesized and the transaction is force completed. Defaults to 120 seconds.</p>
<dt><code>-v</code></p>
<dd> Use verbose output on record set printing, giving the VXID on every log line. Without this option, the VXID will only be given on the header of that transaction.</p>
<dt><code>-V</code></p>
<dd> Print version information and exit.</p>
<dt><code>-w</code><i>&nbsp;<wbr>filename</i></p>
<dd> Redirect output to file. The file will be overwritten unless the -a option was specified. If the application receives a SIGHUP the file will be reopened allowing the old one to be rotated away.</p>
<dt><code>-x</code><i>&nbsp;<wbr>taglist</i></p>
<dd> Exclude log records of these tags in output. Taglist is a comma-separated list of tag globs. Multiple -x options may be given.</p>
<dt><code>-X</code><i>&nbsp;<wbr>&lt;[taglist:]regex&gt;</i></p>
<dd> Exclude by regex matching. Do not output records matching taglist and regular expression. Applies to any tag if taglist is absent.</dl>
<h2>SIGNALS</h2>
<dl>
<dt>&bull;</p>
<dd> SIGHUP </p>
<p> Rotate the log file (see -w option)</p>
<dt>&bull;</p>
<dd> SIGUSR1 </p>
<p> Flush any outstanding transactions</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/7-vsl/">vsl</a>(7)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/7-vsl-query/">vsl-query</a>(7)</dl>
<h2>HISTORY</h2>
<p> The varnishlog utility was developed by Poul-Henning Kamp &lt;<i>phk [at] phk.freebsd.dk</i>&gt; in cooperation with Verdens Gang AS and Varnish Software AS. This manual page was initially written by Dag-Erling Smørgrav, and later updated by Per Buer and Martin Blix Grydeland.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2006 Verdens Gang AS</p>
<dt>&bull;</p>
<dd> Copyright (c) 2006-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>
