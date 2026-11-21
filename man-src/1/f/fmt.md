---
title: "fmt(1)"
name: "fmt"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fmt/"
description: "fmt – simple optimal text formatter"
---

<h2 class="name">NAME</h2>
<p> fmt &#8211; simple optimal text formatter </p>
<h2>SYNOPSIS</h2>
<p> <code>fmt</code> [<i>,-WIDTH/</i>] [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Reformat each paragraph in the FILE(s), writing to standard output. The option <code>-WIDTH</code> is an abbreviated form of <code>&#8211;width</code>=<i>,DIGITS/</i>. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;crown-margin</code></dt>
<dd> preserve indentation of first two lines</dd>
<dt><code>-p</code>, <code>&#8211;prefix</code>=<i>,STRING/</i></dt>
<dd> reformat only lines beginning with STRING, reattaching the prefix to reformatted lines</dd>
<dt><code>-s</code>, <code>&#8211;split-only</code></dt>
<dd> split long lines, but do not refill</dd>
<dt><code>-t</code>, <code>&#8211;tagged-paragraph</code></dt>
<dd> indentation of first line different from second</dd>
<dt><code>-u</code>, <code>&#8211;uniform-spacing</code></dt>
<dd> one space between words, two after sentences</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,WIDTH/</i></dt>
<dd> maximum line width (default of 75 columns)</dd>
<dt><code>-g</code>, <code>&#8211;goal</code>=<i>,WIDTH/</i></dt>
<dd> goal width (default of 93% of width)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Ross Paterson.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/fmt">https://www.gnu.org/software/coreutils/fmt</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) fmt invocation&#8217; </p>
