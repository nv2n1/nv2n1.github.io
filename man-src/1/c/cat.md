---
title: "cat(1)"
name: "cat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cat/"
description: "cat – concatenate files and print on the standard output"
---

<h2>SYNOPSIS</h2>
<p> <code>cat</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Concatenate FILE(s) to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;show-all</code></dt>
<dd> equivalent to <code>-vET</code></dd>
<dt><code>-b</code>, <code>&#8211;number-nonblank</code></dt>
<dd> number nonempty output lines, overrides <code>-n</code></dd>
<dt><code>-e</code></dt>
<dd> equivalent to <code>-vE</code></dd>
<dt><code>-E</code>, <code>&#8211;show-ends</code></dt>
<dd> display $ at end of each line</dd>
<dt><code>-n</code>, <code>&#8211;number</code></dt>
<dd> number all output lines</dd>
<dt><code>-s</code>, <code>&#8211;squeeze-blank</code></dt>
<dd> suppress repeated empty output lines</dd>
<dt><code>-t</code></dt>
<dd> equivalent to <code>-vT</code></dd>
<dt><code>-T</code>, <code>&#8211;show-tabs</code></dt>
<dd> display TAB characters as ^I</dd>
<dt><code>-u</code></dt>
<dd> (ignored)</dd>
<dt><code>-v</code>, <code>&#8211;show-nonprinting</code></dt>
<dd> use ^ and M- notation, except for LFD and TAB</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>cat f &#8211; g</dt>
<dd> Output f&#8217;s contents, then standard input, then g&#8217;s contents.</dd>
<dt>cat</dt>
<dd> Copy standard input to standard output.</dd></dl>
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
