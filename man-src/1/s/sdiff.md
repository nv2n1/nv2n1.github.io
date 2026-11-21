---

title: "sdiff(1)"
name: "sdiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sdiff/"
description: "sdiff – side-by-side merge of file differences"
---

<p> sdiff &#8211; side-by-side merge of file differences </p>
<h2>SYNOPSIS</h2>
<p> <code>sdiff</code> [<i>OPTION</i>]&#8230; <i>FILE1 FILE2</i></p>
<h2>DESCRIPTION</h2>
<p> Side-by-side merge of differences between FILE1 and FILE2. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> operate interactively, sending output to FILE</dd>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></dt>
<dd> consider upper- and lower-case to be the same</dd>
<dt><code>-E</code>, <code>&#8211;ignore-tab-expansion</code></dt>
<dd> ignore changes due to tab expansion</dd>
<dt><code>-Z</code>, <code>&#8211;ignore-trailing-space</code></dt>
<dd> ignore white space at line end</dd>
<dt><code>-b</code>, <code>&#8211;ignore-space-change</code></dt>
<dd> ignore changes in the amount of white space</dd>
<dt><code>-W</code>, <code>&#8211;ignore-all-space</code></dt>
<dd> ignore all white space</dd>
<dt><code>-B</code>, <code>&#8211;ignore-blank-lines</code></dt>
<dd> ignore changes whose lines are all blank</dd>
<dt><code>-I</code>, <code>&#8211;ignore-matching-lines</code>=<i>RE</i></dt>
<dd> ignore changes all whose lines match RE</dd>
<dt><code>&#8211;strip-trailing-cr</code></dt>
<dd> strip trailing carriage return on input</dd>
<dt><code>-a</code>, <code>&#8211;text</code></dt>
<dd> treat all files as text</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>NUM</i></dt>
<dd> output at most NUM (default 130) print columns</dd>
<dt><code>-l</code>, <code>&#8211;left-column</code></dt>
<dd> output only the left column of common lines</dd>
<dt><code>-s</code>, <code>&#8211;suppress-common-lines</code></dt>
<dd> do not output common lines</dd>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></dt>
<dd> expand tabs to spaces in output</dd>
<dt><code>&#8211;tabsize</code>=<i>NUM</i></dt>
<dd> tab stops at every NUM (default 8) print columns</dd>
<dt><code>-d</code>, <code>&#8211;minimal</code></dt>
<dd> try hard to find a smaller set of changes</dd>
<dt><code>-H</code>, <code>&#8211;speed-large-files</code></dt>
<dd> assume large files, many scattered small changes</dd>
<dt><code>&#8211;diff-program</code>=<i>PROGRAM</i></dt>
<dd> use PROGRAM to compare files</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
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
</dt><dd> <code>info sdiff</code></dd></dl>
<p> should give you access to the complete manual. </p>
