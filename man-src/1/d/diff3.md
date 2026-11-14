---
title: "diff3(1)"
name: "diff3"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diff3/"
description: "diff3 – compare three files line by line"
---

<h2 class="name">NAME</h2>
<p> diff3 &#8211; compare three files line by line </p>
<h2>SYNOPSIS</h2>
<p> <code>diff3</code> [<i>OPTION</i>]&#8230; <i>MYFILE OLDFILE YOURFILE</i></p>
<h2>DESCRIPTION</h2>
<p> Compare three files line by line. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;show-all</code></p>
<dd> output all changes, bracketing conflicts</p>
<dt><code>-e</code>, <code>&#8211;ed</code></p>
<dd> output ed script incorporating changes from OLDFILE to YOURFILE into MYFILE</p>
<dt><code>-E</code>, <code>&#8211;show-overlap</code></p>
<dd> like <code>-e</code>, but bracket conflicts</p>
<dt><code>-3</code>, <code>&#8211;easy-only</code></p>
<dd> like <code>-e</code>, but incorporate only nonoverlapping changes</p>
<dt><code>-x</code>, <code>&#8211;overlap-only</code></p>
<dd> like <code>-e</code>, but incorporate only overlapping changes</p>
<dt><code>-X</code></p>
<dd> like <code>-x</code>, but bracket conflicts</p>
<dt><code>-i</code></p>
<dd> append &#8216;w&#8217; and &#8216;q&#8217; commands to ed scripts</p>
<dt><code>-m</code>, <code>&#8211;merge</code></p>
<dd> output actual merged file, according to <code>-A</code> if no other options are given</p>
<dt><code>-a</code>, <code>&#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>&#8211;strip-trailing-cr</code></p>
<dd> strip trailing carriage return on input</p>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></p>
<dd> make tabs line up by prepending a tab</p>
<dt><code>&#8211;diff-program</code>=<i>PROGRAM</i></p>
<dd> use PROGRAM to compare files</p>
<dt><code>-L</code>, <code>&#8211;label</code>=<i>LABEL</i></p>
<dd> use LABEL instead of file name (can be repeated up to three times)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The default output format is a somewhat human-readable representation of the changes. </p>
<p> The <code>-e</code>, <code>-E</code>, <code>-x</code>, <code>-X</code> (and corresponding long) options cause an ed script to be output instead of the default. </p>
<p> Finally, the <code>-m</code> (<code>&#8211;merge</code>) option causes diff3 to do the merge internally and output the actual merged file. For unusual input, this is more robust than using ed. </p>
<p> If a FILE is &#8216;-&#8216;, read standard input. Exit status is 0 if successful, 1 if conflicts, 2 if trouble.</p>
<h2>AUTHOR</h2>
<p> Written by Randy Smith.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: bug-diffutils [at] gnu.org<br />
 GNU diffutils home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/diffutils/">https://www.gnu.org/software/diffutils/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff/">diff</a>(1), <a href="/docs/linux/man/1-sdiff/">sdiff</a>(1) </p>
<p> The full documentation for <code>diff3</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>diff3</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info diff3</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
