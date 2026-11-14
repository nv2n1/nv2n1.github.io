---
title: "cat(1)"
name: "cat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cat/"
description: "cat – concatenate files and print on the standard output"
---

<h2 class="name">NAME</h2>
<p> cat &#8211; concatenate files and print on the standard output </p>
<h2>SYNOPSIS</h2>
<p> <code>cat</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Concatenate FILE(s) to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;show-all</code></p>
<dd> equivalent to <code>-vET</code></p>
<dt><code>-b</code>, <code>&#8211;number-nonblank</code></p>
<dd> number nonempty output lines, overrides <code>-n</code></p>
<dt><code>-e</code></p>
<dd> equivalent to <code>-vE</code></p>
<dt><code>-E</code>, <code>&#8211;show-ends</code></p>
<dd> display $ at end of each line</p>
<dt><code>-n</code>, <code>&#8211;number</code></p>
<dd> number all output lines</p>
<dt><code>-s</code>, <code>&#8211;squeeze-blank</code></p>
<dd> suppress repeated empty output lines</p>
<dt><code>-t</code></p>
<dd> equivalent to <code>-vT</code></p>
<dt><code>-T</code>, <code>&#8211;show-tabs</code></p>
<dd> display TAB characters as ^I</p>
<dt><code>-u</code></p>
<dd> (ignored)</p>
<dt><code>-v</code>, <code>&#8211;show-nonprinting</code></p>
<dd> use ^ and M- notation, except for LFD and TAB</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>cat f &#8211; g</p>
<dd> Output f&#8217;s contents, then standard input, then g&#8217;s contents.</p>
<dt>cat</p>
<dd> Copy standard input to standard output.</dl>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund and Richard M. Stallman.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tac/">tac</a></code>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/cat">https://www.gnu.org/software/coreutils/cat</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) cat invocation&#8217; </p>
<h2>Index</h2>
