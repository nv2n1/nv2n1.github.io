---
title: "head(1)"
name: "head"
section: "1"
letter: "h"
url: "/docs/linux/man/1-head/"
description: "head – output the first part of files"
---

<h2>SYNOPSIS</h2>
<p> <code>head</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print the first 10 lines of each FILE to standard output. With more than one FILE, precede each with a header giving the file name. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;bytes</code>=<i>,[-]NUM/</i></dt>
<dd> print the first NUM bytes of each file; with the leading &#8216;-&#8216;, print all but the last NUM bytes of each file</dd>
<dt><code>-n</code>, <code>&#8211;lines</code>=<i>,[-]NUM/</i></dt>
<dd> print the first NUM lines instead of the first 10; with the leading &#8216;-&#8216;, print all but the last NUM lines of each file</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></dt>
<dd> never print headers giving file names</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> always print headers giving file names</dd>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></dt>
<dd> line delimiter is NUL, not newline</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> NUM may have a multiplier suffix: b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024, GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tail/">tail</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/head">https://www.gnu.org/software/coreutils/head</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) head invocation&#8217; </p>
