---
title: "nice(1)"
name: "nice"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nice/"
description: "nice – run a program with modified scheduling priority"
---

<h2 class="name">NAME</h2>
<p> nice &#8211; run a program with modified scheduling priority </p>
<h2>SYNOPSIS</h2>
<p> <code>nice</code> [<i>,OPTION/</i>] [<i>,COMMAND /</i>[<i>,ARG/</i>]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Run COMMAND with an adjusted niceness, which affects process scheduling. With no COMMAND, print the current niceness. Niceness values range from <code>-20</code> (most favorable to the process) to 19 (least favorable to the process). </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;adjustment</code>=<i>,N/</i></p>
<dd> add integer N to the niceness (default 10)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> NOTE: your shell may have its own version of nice, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-nice/">nice</a>(2), <a href="/docs/linux/man/1-renice/">renice</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/nice">https://www.gnu.org/software/coreutils/nice</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) nice invocation&#8217; </p>
<h2>Index</h2>
