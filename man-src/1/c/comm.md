---
title: "comm(1)"
name: "comm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-comm/"
description: "comm – compare two sorted files line by line"
---

<h2 class="name">NAME</h2>
<p> comm &#8211; compare two sorted files line by line </p>
<h2>SYNOPSIS</h2>
<p> <code>comm</code> [<i>,OPTION/</i>]&#8230; <i>,FILE1 FILE2/</i></p>
<h2>DESCRIPTION</h2>
<p> Compare sorted files FILE1 and FILE2 line by line. </p>
<p> When FILE1 or FILE2 (not both) is -, read standard input. </p>
<p> With no options, produce three-column output. Column one contains lines unique to FILE1, column two contains lines unique to FILE2, and column three contains lines common to both files.</p>
<dl>
<dt><code>-1</code></p>
<dd> suppress column 1 (lines unique to FILE1)</p>
<dt><code>-2</code></p>
<dd> suppress column 2 (lines unique to FILE2)</p>
<dt><code>-3</code></p>
<dd> suppress column 3 (lines that appear in both files)</p>
<dt><code>&#8211;check-order</code></p>
<dd> check that the input is correctly sorted, even if all input lines are pairable</p>
<dt><code>&#8211;nocheck-order</code></p>
<dd> do not check that the input is correctly sorted</p>
<dt><code>&#8211;output-delimiter</code>=<i>,STR/</i></p>
<dd> separate columns with STR</p>
<dt><code>&#8211;total</code></p>
<dd> output a summary</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Note, comparisons honor the rules specified by &#8216;LC_COLLATE&#8217;.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>comm -12 file1 file2</p>
<dd> Print only lines present in both file1 and file2.</p>
<dt>comm -3 file1 file2</p>
<dd> Print lines in file1 not in file2, and vice versa.</dl>
<h2>AUTHOR</h2>
<p> Written by Richard M. Stallman and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-join/">join</a>(1), <a href="/docs/linux/man/1-uniq/">uniq</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/comm">https://www.gnu.org/software/coreutils/comm</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) comm invocation&#8217; </p>
<h2>Index</h2>
