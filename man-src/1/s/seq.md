---
title: "seq(1)"
name: "seq"
section: "1"
letter: "s"
url: "/docs/linux/man/1-seq/"
description: "seq – print a sequence of numbers"
---

<h2 class="name">NAME</h2>
<p> seq &#8211; print a sequence of numbers </p>
<h2>SYNOPSIS</h2>
<p> <code>seq</code> [<i>,OPTION/</i>]&#8230; <i>,LAST/</i><br />
 <code>seq</code> [<i>,OPTION/</i>]&#8230; <i>,FIRST LAST/</i><br />
 <code>seq</code> [<i>,OPTION/</i>]&#8230; <i>,FIRST INCREMENT LAST/</i></p>
<h2>DESCRIPTION</h2>
<p> Print numbers from FIRST to LAST, in steps of INCREMENT. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>,FORMAT/</i></p>
<dd> use printf style floating-point FORMAT</p>
<dt><code>-s</code>, <code>&#8211;separator</code>=<i>,STRING/</i></p>
<dd> use STRING to separate numbers (default: 
)</p>
<dt><code>-w</code>, <code>&#8211;equal-width</code></p>
<dd> equalize width by padding with leading zeroes</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If FIRST or INCREMENT is omitted, it defaults to 1. That is, an omitted INCREMENT defaults to 1 even when LAST is smaller than FIRST. The sequence of numbers ends when the sum of the current number and INCREMENT would become greater than LAST. FIRST, INCREMENT, and LAST are interpreted as floating point values. INCREMENT is usually positive if FIRST is smaller than LAST, and INCREMENT is usually negative if FIRST is greater than LAST. INCREMENT must not be 0; none of FIRST, INCREMENT and LAST may be NaN. FORMAT must be suitable for printing one argument of type &#8216;double&#8217;; it defaults to %.PRECf if FIRST, INCREMENT, and LAST are all fixed point decimal numbers with maximum precision PREC, and to %g otherwise.</p>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/seq">https://www.gnu.org/software/coreutils/seq</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) seq invocation&#8217; </p>
<h2>Index</h2>
