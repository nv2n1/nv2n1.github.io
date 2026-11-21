---

title: "varnishlog(1)"
name: "varnishlog"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishlog/"
description: "varnishlog – Display Varnish logs"
---

<p> varnishlog &#8211; Display Varnish logs</p>
<h2>SYNOPSIS</h2>
<p> varnishlog [-a] [-b] [-B] [-c] [-C] [-d] [-D] [-g &lt;session|request|vxid|raw&gt;] [-h] [-i taglist] [-I &lt;[taglist:]regex&gt;] [-k num] [-L limit] [-n name] [-N filename] [-P file] [-q query] [-r filename] [-T seconds] [-v] [-V] [-w filename] [-x taglist] [-X &lt;[taglist:]regex&gt;]</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-a</code></dt>
<dd> When writing output to a file, append to it rather than overwrite it.</dd>
<dt><code>-b</code></dt>
<dd> Only display transactions and log records coming from backend communication.</dd>
<dt><code>-B</code></dt>
<dd> Output binary data suitable for reading with -r. The -w option specifies where the binary output is written.</dd>
<dt><code>-c</code></dt>
<dd> Only display transactions and log records coming from client communication.</dd>
<dt><code>-C</code></dt>
<dd> Do all regular expression and string matching caseless.</dd>
<dt><code>-d</code></dt>
<dd> Start processing log records at the head of the log instead of the tail.</dd>
<dt><code>-D</code></dt>
<dd> Daemonize.</dd>
<dt><code>-g</code><i>&nbsp;<wbr>&lt;session|request|vxid|raw&gt;</i></dt>
<dd> The grouping of the log records. The default is to group by vxid.</dd>
<dt><code>-h</code></dt>
<dd> Print program usage and exit</dd>
<dt><code>-i</code><i>&nbsp;<wbr>taglist</i></dt>
<dd> Include log records of these tags in output. Taglist is a comma-separated list of tag globs. Multiple -i options may be given. </dd>
<p> If a tag include option is the first of any tag selection options, all tags are first marked excluded.</p>
<dt><code>-I</code><i>&nbsp;<wbr>&lt;[taglist:]regex&gt;</i></dt>
<dd> Include by regex matching. Output only records matching taglist and regular expression. Applies to any tag if taglist is absent. </dd>
<p> If a tag include option is the first of any tag selection options, all tags are first marked excluded.</p>
<dt><code>-k</code><i>&nbsp;<wbr>num</i></dt>
<dd> Process this number of matching log transactions before exiting.</dd>
<dt><code>-L</code><i>&nbsp;<wbr>limit</i></dt>
<dd> Sets the upper limit of incomplete transactions kept before the oldest transaction is force completed. A warning record is synthesized when this happens. This setting keeps an upper bound on the memory usage of running queries. Defaults to 1000 transactions.</dd>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></dt>
<dd> Specify the name of the varnishd instance to get logs from. If -n is not specified, the host name is used.</dd>
<dt><code>-N</code><i>&nbsp;<wbr>filename</i></dt>
<dd> Specify the filename of a stale VSM instance. When using this option the abandonment checking is disabled.</dd>
<dt><code>-P</code><i>&nbsp;<wbr>file</i></dt>
<dd> Write the process&#8217; PID to the specified file.</dd>
<dt><code>-q</code><i>&nbsp;<wbr>query</i></dt>
<dd> Specifies the VSL query to use.</dd>
<dt><code>-r</code><i>&nbsp;<wbr>filename</i></dt>
<dd> Read log in binary file format from this file. The file can be created with <code>varnishlog -B -w filename</code>.</dd>
<dt><code>-T</code><i>&nbsp;<wbr>seconds</i></dt>
<dd> Sets the transaction timeout in seconds. This defines the maximum number of seconds elapsed between a Begin tag and the End tag. If the timeout expires, a warning record is synthesized and the transaction is force completed. Defaults to 120 seconds.</dd>
<dt><code>-v</code></dt>
<dd> Use verbose output on record set printing, giving the VXID on every log line. Without this option, the VXID will only be given on the header of that transaction.</dd>
<dt><code>-V</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>-w</code><i>&nbsp;<wbr>filename</i></dt>
<dd> Redirect output to file. The file will be overwritten unless the -a option was specified. If the application receives a SIGHUP the file will be reopened allowing the old one to be rotated away.</dd>
<dt><code>-x</code><i>&nbsp;<wbr>taglist</i></dt>
<dd> Exclude log records of these tags in output. Taglist is a comma-separated list of tag globs. Multiple -x options may be given.</dd>
<dt><code>-X</code><i>&nbsp;<wbr>&lt;[taglist:]regex&gt;</i></dt>
<dd> Exclude by regex matching. Do not output records matching taglist and regular expression. Applies to any tag if taglist is absent.</dd></dl>
<h2>SIGNALS</h2>
<dl>
<dt>&bull;</dt>
<dd> SIGHUP </dd>
<p> Rotate the log file (see -w option)</p>
<dt>&bull;</dt>
<dd> SIGUSR1 </dd>
<p> Flush any outstanding transactions</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/7-vsl/">vsl</a>(7)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/7-vsl-query/">vsl-query</a>(7)</dd></dl>
<h2>HISTORY</h2>
<p> The varnishlog utility was developed by Poul-Henning Kamp &lt;<i>phk [at] phk.freebsd.dk</i>&gt; in cooperation with Verdens Gang AS and Varnish Software AS. This manual page was initially written by Dag-Erling Smørgrav, and later updated by Per Buer and Martin Blix Grydeland.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</dt>
<dd> Copyright (c) 2006 Verdens Gang AS</dd>
<dt>&bull;</dt>
<dd> Copyright (c) 2006-2014 Varnish Software AS </dd>
</dl>
