---
title: "cmp(1)"
name: "cmp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmp/"
description: "cmp – compare two files byte by byte"
---

<h2 class="name">NAME</h2>
<p> cmp &#8211; compare two files byte by byte </p>
<h2>SYNOPSIS</h2>
<p> <code>cmp</code> [<i>OPTION</i>]&#8230; <i>FILE1 </i>[<i>FILE2 </i>[<i>SKIP1 </i>[<i>SKIP2</i>]]]</p>
<h2>DESCRIPTION</h2>
<p> Compare two files byte by byte. </p>
<p> The optional SKIP1 and SKIP2 specify the number of bytes to skip at the beginning of each file (zero by default). </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;print-bytes</code></p>
<dd> print differing bytes</p>
<dt><code>-i</code>, <code>&#8211;ignore-initial</code>=<i>SKIP</i></p>
<dd> skip first SKIP bytes of both inputs</p>
<dt><code>-i</code>, <code>&#8211;ignore-initial</code>=<i>SKIP1</i>:SKIP2</p>
<dd> skip first SKIP1 bytes of FILE1 and first SKIP2 bytes of FILE2</p>
<dt><code>-l</code>, <code>&#8211;verbose</code></p>
<dd> output byte numbers and differing byte values</p>
<dt><code>-n</code>, <code>&#8211;bytes</code>=<i>LIMIT</i></p>
<dd> compare at most LIMIT bytes</p>
<dt><code>-s</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> suppress all normal output</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> SKIP values may be followed by the following multiplicative suffixes: kB 1000, K 1024, MB 1,000,000, M 1,048,576, GB 1,000,000,000, G 1,073,741,824, and so on for T, P, E, Z, Y. </p>
<p> If a FILE is &#8216;-&#8216; or missing, read standard input. Exit status is 0 if inputs are the same, 1 if different, 2 if trouble.</p>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: bug-diffutils [at] gnu.org<br />
 GNU diffutils home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/diffutils/">https://www.gnu.org/software/diffutils/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-diff3/">diff3</a>(1), <a href="/docs/linux/man/1-sdiff/">sdiff</a>(1) </p>
<p> The full documentation for <code>cmp</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>cmp</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info cmp</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
