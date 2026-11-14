---
title: "wc(1)"
name: "wc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wc/"
description: "wc – print newline, word, and byte counts for each file"
---

<h2 class="name">NAME</h2>
<p> wc &#8211; print newline, word, and byte counts for each file </p>
<h2>SYNOPSIS</h2>
<p> <code>wc</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;<br />
 <code>wc</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;files0-from=F/</i></p>
<h2>DESCRIPTION</h2>
<p> Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified. A word is a non-zero-length sequence of characters delimited by white space. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> The options below may be used to select which counts are printed, always in the following order: newline, word, character, byte, maximum line length.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;bytes</code></p>
<dd> print the byte counts</p>
<dt><code>-m</code>, <code>&#8211;chars</code></p>
<dd> print the character counts</p>
<dt><code>-l</code>, <code>&#8211;lines</code></p>
<dd> print the newline counts</p>
<dt><code>&#8211;files0-from</code>=<i>,F/</i></p>
<dd> read input from the files specified by NUL-terminated names in file F; If F is &#8211; then read names from standard input</p>
<dt><code>-L</code>, <code>&#8211;max-line-length</code></p>
<dd> print the maximum display width</p>
<dt><code>-w</code>, <code>&#8211;words</code></p>
<dd> print the word counts</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Paul Rubin and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/wc">https://www.gnu.org/software/coreutils/wc</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) wc invocation&#8217; </p>
<h2>Index</h2>
