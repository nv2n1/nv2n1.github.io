---
title: "csplit(1)"
name: "csplit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csplit/"
description: "csplit – split a file into sections determined by context lines"
---

<h2 class="name">NAME</h2>
<p> csplit &#8211; split a file into sections determined by context lines </p>
<h2>SYNOPSIS</h2>
<p> <code>csplit</code> [<i>,OPTION/</i>]&#8230; <i>,FILE PATTERN/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Output pieces of FILE separated by PATTERN(s) to files &#8216;xx00&#8217;, &#8216;xx01&#8217;, &#8230;, and output byte counts of each piece to standard output. </p>
<p> Read standard input if FILE is &#8211; </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;suffix-format</code>=<i>,FORMAT/</i></p>
<dd> use sprintf FORMAT instead of %02d</p>
<dt><code>-f</code>, <code>&#8211;prefix</code>=<i>,PREFIX/</i></p>
<dd> use PREFIX instead of &#8216;xx&#8217;</p>
<dt><code>-k</code>, <code>&#8211;keep-files</code></p>
<dd> do not remove output files on errors</p>
<dt><code>&#8211;suppress-matched</code></p>
<dd> suppress the lines matching PATTERN</p>
<dt><code>-n</code>, <code>&#8211;digits</code>=<i>,DIGITS/</i></p>
<dd> use specified number of digits instead of 2</p>
<dt><code>-s</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> do not print counts of output file sizes</p>
<dt><code>-z</code>, <code>&#8211;elide-empty-files</code></p>
<dd> remove empty output files</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h3>Each PATTERN may be:</h3>
<dl>
<dt>INTEGER</p>
<dd> copy up to but not including specified line number</p>
<dt>/REGEXP/[OFFSET]</p>
<dd> copy up to but not including a matching line</p>
<dt>%REGEXP%[OFFSET]</p>
<dd> skip to, but not including a matching line</p>
<dt>{INTEGER}</p>
<dd> repeat the previous pattern specified number of times</p>
<dt>{*}</p>
<dd> repeat the previous pattern as many times as possible</dl>
<p> A line OFFSET is a required &#8216;+&#8217; or &#8216;-&#8216; followed by a positive integer.</p>
<h2>AUTHOR</h2>
<p> Written by Stuart Kemp and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/csplit">https://www.gnu.org/software/coreutils/csplit</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) csplit invocation&#8217; </p>
<h2>Index</h2>
