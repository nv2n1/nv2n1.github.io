---
title: "nl(1)"
name: "nl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nl/"
description: "nl – number lines of files"
---

<h2 class="name">NAME</h2>
<p> nl &#8211; number lines of files </p>
<h2>SYNOPSIS</h2>
<p> <code>nl</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Write each FILE to standard output, with line numbers added. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;body-numbering</code>=<i>,STYLE/</i></p>
<dd> use STYLE for numbering body lines</p>
<dt><code>-d</code>, <code>&#8211;section-delimiter</code>=<i>,CC/</i></p>
<dd> use CC for logical page delimiters</p>
<dt><code>-f</code>, <code>&#8211;footer-numbering</code>=<i>,STYLE/</i></p>
<dd> use STYLE for numbering footer lines</p>
<dt><code>-h</code>, <code>&#8211;header-numbering</code>=<i>,STYLE/</i></p>
<dd> use STYLE for numbering header lines</p>
<dt><code>-i</code>, <code>&#8211;line-increment</code>=<i>,NUMBER/</i></p>
<dd> line number increment at each line</p>
<dt><code>-l</code>, <code>&#8211;join-blank-lines</code>=<i>,NUMBER/</i></p>
<dd> group of NUMBER empty lines counted as one</p>
<dt><code>-n</code>, <code>&#8211;number-format</code>=<i>,FORMAT/</i></p>
<dd> insert line numbers according to FORMAT</p>
<dt><code>-p</code>, <code>&#8211;no-renumber</code></p>
<dd> do not reset line numbers for each section</p>
<dt><code>-s</code>, <code>&#8211;number-separator</code>=<i>,STRING/</i></p>
<dd> add STRING after (possible) line number</p>
<dt><code>-v</code>, <code>&#8211;starting-line-number</code>=<i>,NUMBER/</i></p>
<dd> first line number for each section</p>
<dt><code>-w</code>, <code>&#8211;number-width</code>=<i>,NUMBER/</i></p>
<dd> use NUMBER columns for line numbers</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Default options are: <code>-bt</code> <code>-d</code>&#8216;\:&#8217; <code>-fn</code> <code>-hn</code> <code>-i1</code> <code>-l1</code> <code>-n</code>&#8216;rn&#8217; <code>-s</code>&lt;TAB&gt; <code>-v1</code> <code>-w6</code> </p>
<p> CC are two delimiter characters used to construct logical page delimiters; a missing second character implies &#8216;:&#8217;. </p>
<p> STYLE is one of:</p>
<dl>
<dt>a</p>
<dd> number all lines</p>
<dt>t</p>
<dd> number only nonempty lines</p>
<dt>n</p>
<dd> number no lines</p>
<dt>pBRE</p>
<dd> number only lines that contain a match for the basic regular expression, BRE</dl>
<p> FORMAT is one of:</p>
<dl>
<dt>ln</p>
<dd> left justified, no leading zeros</p>
<dt>rn</p>
<dd> right justified, no leading zeros</p>
<dt>rz</p>
<dd> right justified, leading zeros</dl>
<h2>AUTHOR</h2>
<p> Written by Scott Bartram and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/nl">https://www.gnu.org/software/coreutils/nl</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) nl invocation&#8217; </p>
<h2>Index</h2>
