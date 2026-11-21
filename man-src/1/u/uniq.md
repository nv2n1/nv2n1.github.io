---
title: "uniq(1)"
name: "uniq"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uniq/"
description: "uniq – report or omit repeated lines"
---

<h2>SYNOPSIS</h2>
<p> <code>uniq</code> [<i>,OPTION/</i>]&#8230; [<i>,INPUT /</i>[<i>,OUTPUT/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Filter adjacent matching lines from INPUT (or standard input), writing to OUTPUT (or standard output). </p>
<p> With no options, matching lines are merged to the first occurrence. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;count</code></dt>
<dd> prefix lines by the number of occurrences</dd>
<dt><code>-d</code>, <code>&#8211;repeated</code></dt>
<dd> only print duplicate lines, one for each group</dd>
<dt><code>-D</code></dt>
<dd> print all duplicate lines</dd>
<dt><code>&#8211;all-repeated</code>[=<i>,METHOD/</i>]</dt>
<dd> like <code>-D</code>, but allow separating groups with an empty line; METHOD={none(default),prepend,separate}</dd>
<dt><code>-f</code>, <code>&#8211;skip-fields</code>=<i>,N/</i></dt>
<dd> avoid comparing the first N fields</dd>
<dt><code>&#8211;group</code>[=<i>,METHOD/</i>]</dt>
<dd> show all items, separating groups with an empty line; METHOD={separate(default),prepend,append,both}</dd>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></dt>
<dd> ignore differences in case when comparing</dd>
<dt><code>-s</code>, <code>&#8211;skip-chars</code>=<i>,N/</i></dt>
<dd> avoid comparing the first N characters</dd>
<dt><code>-u</code>, <code>&#8211;unique</code></dt>
<dd> only print unique lines</dd>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></dt>
<dd> line delimiter is NUL, not newline</dd>
<dt><code>-w</code>, <code>&#8211;check-chars</code>=<i>,N/</i></dt>
<dd> compare no more than N characters in lines</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> A field is a run of blanks (usually spaces and/or TABs), then non-blank characters. Fields are skipped before chars. </p>
<p> Note: &#8216;uniq&#8217; does not detect repeated lines unless they are adjacent. You may want to sort the input first, or use &#8216;sort <code>-u</code>&#8216; without &#8216;uniq&#8217;.</p>
<h2>AUTHOR</h2>
<p> Written by Richard M. Stallman and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-comm/">comm</a>(1), <a href="/docs/linux/man/1-join/">join</a>(1), <a href="/docs/linux/man/1-sort/">sort</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/uniq">https://www.gnu.org/software/coreutils/uniq</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) uniq invocation&#8217; </p>
