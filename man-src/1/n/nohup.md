---
title: "nohup(1)"
name: "nohup"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nohup/"
description: "nohup – run a command immune to hangups, with output to a non-tty"
---

<h2 class="name">NAME</h2>
<p> nohup &#8211; run a command immune to hangups, with output to a non-tty </p>
<h2>SYNOPSIS</h2>
<p> <code>nohup</code> <i>,COMMAND /</i>[<i>,ARG/</i>]&#8230;<br />
 <code>nohup</code> <i>,OPTION/</i></p>
<h2>DESCRIPTION</h2>
<p> Run COMMAND, ignoring hangup signals.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If standard input is a terminal, redirect it from an unreadable file. If standard output is a terminal, append output to &#8216;nohup.out&#8217; if possible, &#8216;$HOME/nohup.out&#8217; otherwise. If standard error is a terminal, redirect it to standard output. To save output to FILE, use &#8216;nohup COMMAND &gt; FILE&#8217;. </p>
<p> NOTE: your shell may have its own version of nohup, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/nohup">https://www.gnu.org/software/coreutils/nohup</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) nohup invocation&#8217; </p>
<h2>Index</h2>
