---
title: "tail(1)"
name: "tail"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tail/"
description: "tail – output the last part of files"
---

<h2 class="name">NAME</h2>
<p> tail &#8211; output the last part of files </p>
<h2>SYNOPSIS</h2>
<p> <code>tail</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print the last 10 lines of each FILE to standard output. With more than one FILE, precede each with a header giving the file name. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;bytes</code>=<i>,[/</i>+]NUM</p>
<dd> output the last NUM bytes; or use <code>-c</code> +NUM to output starting with byte NUM of each file</p>
<dt><code>-f</code>, <code>&#8211;follow[=</code>{name|descriptor}]</p>
<dd> output appended data as the file grows;</p>
<dt>
<dd> an absent option argument means &#8216;descriptor&#8217;</p>
<dt><code>-F</code></p>
<dd> same as <code>&#8211;follow</code>=<i>,name/</i> <code>&#8211;retry</code></p>
<dt><code>-n</code>, <code>&#8211;lines</code>=<i>,[/</i>+]NUM</p>
<dd> output the last NUM lines, instead of the last 10; or use <code>-n</code> +NUM to output starting with line NUM</p>
<dt><code>&#8211;max-unchanged-stats</code>=<i>,N/</i></p>
<dd> with <code>&#8211;follow</code>=<i>,name/</i>, reopen a FILE which has not</p>
<dt>
<dd> changed size after N (default 5) iterations to see if it has been unlinked or renamed (this is the usual case of rotated log files); with inotify, this option is rarely useful</p>
<dt><code>&#8211;pid</code>=<i>,PID/</i></p>
<dd> with <code>-f</code>, terminate after process ID, PID dies</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> never output headers giving file names</p>
<dt><code>&#8211;retry</code></p>
<dd> keep trying to open a file if it is inaccessible</p>
<dt><code>-s</code>, <code>&#8211;sleep-interval</code>=<i>,N/</i></p>
<dd> with <code>-f</code>, sleep for approximately N seconds (default 1.0) between iterations; with inotify and <code>&#8211;pid</code>=<i>,P/</i>, check process P at least once every N seconds</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> always output headers giving file names</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> NUM may have a multiplier suffix: b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024, GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> With <code>&#8211;follow</code> (<code>-f</code>), tail defaults to following the file descriptor, which means that even if a tail&#8217;ed file is renamed, tail will continue to track its end. This default behavior is not desirable when you really want to track the actual name of the file, not the file descriptor (e.g., log rotation). Use <code>&#8211;follow</code>=<i>,name/</i> in that case. That causes tail to track the named file in a way that accommodates renaming, removal and creation.</p>
<h2>AUTHOR</h2>
<p> Written by Paul Rubin, David MacKenzie, Ian Lance Taylor, and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-head/">head</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/tail">https://www.gnu.org/software/coreutils/tail</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) tail invocation&#8217; </p>
<h2>Index</h2>
