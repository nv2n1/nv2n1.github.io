---
title: "sdiff(1)"
name: "sdiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sdiff/"
description: "sdiff – side-by-side merge of file differences"
---

<h2 class="name">NAME</h2>
<p> sdiff &#8211; side-by-side merge of file differences </p>
<h2>SYNOPSIS</h2>
<p> <code>sdiff</code> [<i>OPTION</i>]&#8230; <i>FILE1 FILE2</i></p>
<h2>DESCRIPTION</h2>
<p> Side-by-side merge of differences between FILE1 and FILE2. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> operate interactively, sending output to FILE</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> consider upper- and lower-case to be the same</p>
<dt><code>-E</code>, <code>&#8211;ignore-tab-expansion</code></p>
<dd> ignore changes due to tab expansion</p>
<dt><code>-Z</code>, <code>&#8211;ignore-trailing-space</code></p>
<dd> ignore white space at line end</p>
<dt><code>-b</code>, <code>&#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-W</code>, <code>&#8211;ignore-all-space</code></p>
<dd> ignore all white space</p>
<dt><code>-B</code>, <code>&#8211;ignore-blank-lines</code></p>
<dd> ignore changes whose lines are all blank</p>
<dt><code>-I</code>, <code>&#8211;ignore-matching-lines</code>=<i>RE</i></p>
<dd> ignore changes all whose lines match RE</p>
<dt><code>&#8211;strip-trailing-cr</code></p>
<dd> strip trailing carriage return on input</p>
<dt><code>-a</code>, <code>&#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUM</i></p>
<dd> output at most NUM (default 130) print columns</p>
<dt><code>-l</code>, <code>&#8211;left-column</code></p>
<dd> output only the left column of common lines</p>
<dt><code>-s</code>, <code>&#8211;suppress-common-lines</code></p>
<dd> do not output common lines</p>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></p>
<dd> expand tabs to spaces in output</p>
<dt><code>&#8211;tabsize</code>=<i>NUM</i></p>
<dd> tab stops at every NUM (default 8) print columns</p>
<dt><code>-d</code>, <code>&#8211;minimal</code></p>
<dd> try hard to find a smaller set of changes</p>
<dt><code>-H</code>, <code>&#8211;speed-large-files</code></p>
<dd> assume large files, many scattered small changes</p>
<dt><code>&#8211;diff-program</code>=<i>PROGRAM</i></p>
<dd> use PROGRAM to compare files</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If a FILE is &#8216;-&#8216;, read standard input. Exit status is 0 if inputs are the same, 1 if different, 2 if trouble.</p>
<h2>AUTHOR</h2>
<p> Written by Thomas Lord.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: bug-diffutils [at] gnu.org<br />
 GNU diffutils home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/diffutils/">https://www.gnu.org/software/diffutils/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-diff3/">diff3</a>(1) </p>
<p> The full documentation for <code>sdiff</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>sdiff</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info sdiff</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
