---
title: "varnishtop(1)"
name: "varnishtop"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishtop/"
description: "varnishtop – Varnish log entry ranking"
---

<h2>NAME</h2>
<p> varnishtop &#8211; Varnish log entry ranking</p>
<h2>SYNOPSIS</h2>
<p> varnishtop [-1] [-b] [-c] [-C] [-d] [-f] [-g &lt;session|request|vxid|raw&gt;] [-h] [-i taglist] [-I &lt;[taglist:]regex&gt;] [-L limit] [-n name] [-N filename] [-p period] [-q query] [-r filename] [-T seconds] [-x taglist] [-X &lt;[taglist:]regex&gt;] [-V]</p>
<h2>DESCRIPTION</h2>
<p> The varnishtop utility reads <code><a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</code> shared memory logs and presents a continuously updated list of the most commonly occurring log entries. With suitable filtering using the <code>-I</code>, <code>-i</code>, <code>-X</code> and <code>-x</code> options, it can be used to display a ranking of requested documents, clients, user agents, or any other information which is recorded in the log. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-1</code></p>
<dd> Instead of a continously updated display, print the statistics once and exit. Implies <code>-d</code>.</p>
<dt><code>-b</code></p>
<dd> Only display transactions and log records coming from backend communication.</p>
<dt><code>-c</code></p>
<dd> Only display transactions and log records coming from client communication.</p>
<dt><code>-C</code></p>
<dd> Do all regular expression and string matching caseless.</p>
<dt><code>-d</code></p>
<dd> Start processing log records at the head of the log instead of the tail.</p>
<dt><code>-f</code></p>
<dd> Sort and group only on the first field of each log entry. This is useful when displaying e.g. stataddr entries, where the first field is the client IP address.</p>
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
<dt><code>-L</code><i>&nbsp;<wbr>limit</i></p>
<dd> Sets the upper limit of incomplete transactions kept before the oldest transaction is force completed. A warning record is synthesized when this happens. This setting keeps an upper bound on the memory usage of running queries. Defaults to 1000 transactions.</p>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></p>
<dd> Specify the name of the varnishd instance to get logs from. If -n is not specified, the host name is used.</p>
<dt><code>-N</code><i>&nbsp;<wbr>filename</i></p>
<dd> Specify the filename of a stale VSM instance. When using this option the abandonment checking is disabled.</p>
<dt><code>-p</code><i>&nbsp;<wbr>period</i></p>
<dd> Specified the number of seconds to measure over, the default is 60 seconds. The first number in the list is the average number of requests seen over this time period.</p>
<dt><code>-q</code><i>&nbsp;<wbr>query</i></p>
<dd> Specifies the VSL query to use.</p>
<dt><code>-r</code><i>&nbsp;<wbr>filename</i></p>
<dd> Read log in binary file format from this file. The file can be created with <code>varnishlog -B -w filename</code>.</p>
<dt><code>-T</code><i>&nbsp;<wbr>seconds</i></p>
<dd> Sets the transaction timeout in seconds. This defines the maximum number of seconds elapsed between a Begin tag and the End tag. If the timeout expires, a warning record is synthesized and the transaction is force completed. Defaults to 120 seconds.</p>
<dt><code>-x</code><i>&nbsp;<wbr>taglist</i></p>
<dd> Exclude log records of these tags in output. Taglist is a comma-separated list of tag globs. Multiple -x options may be given.</p>
<dt><code>-X</code><i>&nbsp;<wbr>&lt;[taglist:]regex&gt;</i></p>
<dd> Exclude by regex matching. Do not output records matching taglist and regular expression. Applies to any tag if taglist is absent.</p>
<dt><code>-V</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> The following example displays a continuously updated list of the most frequently requested URLs: </p>
<pre>
varnishtop -i ReqURL
</pre>
<p> The following example displays a continuously updated list of the most commonly used user agents: </p>
<pre>
varnishtop -C -I ReqHeader:User-Agent
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</dl>
<h2>HISTORY</h2>
<p> The varnishtop utility was originally developed by Poul-Henning Kamp in cooperation with Verdens Gang AS and Varnish Software AS, and later substantially rewritten by Dag-Erling Smørgrav. This manual page was written by Dag-Erling Smørgrav, and later updated by Martin Blix Grydeland.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2006 Verdens Gang AS</p>
<dt>&bull;</p>
<dd> Copyright (c) 2006-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>
