---
title: "join(1)"
name: "join"
section: "1"
letter: "j"
url: "/docs/linux/man/1-join/"
description: "join – join lines of two files on a common field"
---

<h2 class="name">NAME</h2>
<p> join &#8211; join lines of two files on a common field </p>
<h2>SYNOPSIS</h2>
<p> <code>join</code> [<i>,OPTION/</i>]&#8230; <i>,FILE1 FILE2/</i></p>
<h2>DESCRIPTION</h2>
<p> For each pair of input lines with identical join fields, write a line to standard output. The default join field is the first, delimited by blanks. </p>
<p> When FILE1 or FILE2 (not both) is -, read standard input.</p>
<dl>
<dt><code>-a</code> FILENUM</p>
<dd> also print unpairable lines from file FILENUM, where FILENUM is 1 or 2, corresponding to FILE1 or FILE2</p>
<dt><code>-e</code> EMPTY</p>
<dd> replace missing input fields with EMPTY</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> ignore differences in case when comparing fields</p>
<dt><code>-j</code> FIELD</p>
<dd> equivalent to &#8216;-1 FIELD <code>-2</code> FIELD&#8217;</p>
<dt><code>-o</code> FORMAT</p>
<dd> obey FORMAT while constructing output line</p>
<dt><code>-t</code> CHAR</p>
<dd> use CHAR as input and output field separator</p>
<dt><code>-v</code> FILENUM</p>
<dd> like <code>-a</code> FILENUM, but suppress joined output lines</p>
<dt><code>-1</code> FIELD</p>
<dd> join on this FIELD of file 1</p>
<dt><code>-2</code> FIELD</p>
<dd> join on this FIELD of file 2</p>
<dt><code>&#8211;check-order</code></p>
<dd> check that the input is correctly sorted, even if all input lines are pairable</p>
<dt><code>&#8211;nocheck-order</code></p>
<dd> do not check that the input is correctly sorted</p>
<dt><code>&#8211;header</code></p>
<dd> treat the first line in each file as field headers, print them without trying to pair them</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Unless <code>-t</code> CHAR is given, leading blanks separate fields and are ignored, else fields are separated by CHAR. Any FIELD is a field number counted from 1. FORMAT is one or more comma or blank separated specifications, each being &#8216;FILENUM.FIELD&#8217; or &#8216;0&#8217;. Default FORMAT outputs the join field, the remaining fields from FILE1, the remaining fields from FILE2, all separated by CHAR. If FORMAT is the keyword &#8216;auto&#8217;, then the first line of each file determines the number of fields output for each line. </p>
<p> Important: FILE1 and FILE2 must be sorted on the join fields. E.g., use &quot;sort <code>-k</code> 1b,1&quot; if &#8216;join&#8217; has no options, or use &quot;join <code>-t</code> &#8221;&quot; if &#8216;sort&#8217; has no options. Note, comparisons honor the rules specified by &#8216;LC_COLLATE&#8217;. If the input is not sorted and some lines cannot be joined, a warning message will be given.</p>
<h2>AUTHOR</h2>
<p> Written by Mike Haertel.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-comm/">comm</a>(1), <a href="/docs/linux/man/1-uniq/">uniq</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/join">https://www.gnu.org/software/coreutils/join</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) join invocation&#8217; </p>
<h2>Index</h2>
