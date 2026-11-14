---
title: "cut(1)"
name: "cut"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cut/"
description: "cut – remove sections from each line of files"
---

<h2 class="name">NAME</h2>
<p> cut &#8211; remove sections from each line of files </p>
<h2>SYNOPSIS</h2>
<p> <code>cut</code> <i>,OPTION/</i>&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print selected parts of lines from each FILE to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;bytes</code>=<i>,LIST/</i></p>
<dd> select only these bytes</p>
<dt><code>-c</code>, <code>&#8211;characters</code>=<i>,LIST/</i></p>
<dd> select only these characters</p>
<dt><code>-d</code>, <code>&#8211;delimiter</code>=<i>,DELIM/</i></p>
<dd> use DELIM instead of TAB for field delimiter</p>
<dt><code>-f</code>, <code>&#8211;fields</code>=<i>,LIST/</i></p>
<dd> select only these fields; also print any line that contains no delimiter character, unless the <code>-s</code> option is specified</p>
<dt><code>-n</code></p>
<dd> (ignored)</p>
<dt><code>&#8211;complement</code></p>
<dd> complement the set of selected bytes, characters or fields</p>
<dt><code>-s</code>, <code>&#8211;only-delimited</code></p>
<dd> do not print lines not containing delimiters</p>
<dt><code>&#8211;output-delimiter</code>=<i>,STRING/</i></p>
<dd> use STRING as the output delimiter the default is to use the input delimiter</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Use one, and only one of <code>-b</code>, <code>-c</code> or <code>-f</code>. Each LIST is made up of one range, or many ranges separated by commas. Selected input is written in the same order that it is read, and is written exactly once. Each range is one of:</p>
<dl>
<dt>N</p>
<dd> N&#8217;th byte, character or field, counted from 1</p>
<dt>N-</p>
<dd> from N&#8217;th byte, character or field, to end of line</p>
<dt>N-M</p>
<dd> from N&#8217;th to M&#8217;th (included) byte, character or field</p>
<dt><code>-M</code></p>
<dd> from first to M&#8217;th (included) byte, character or field</dl>
<h2>AUTHOR</h2>
<p> Written by David M. Ihnat, David MacKenzie, and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/cut">https://www.gnu.org/software/coreutils/cut</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) cut invocation&#8217; </p>
<h2>Index</h2>
