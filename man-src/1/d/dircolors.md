---
title: "dircolors(1)"
name: "dircolors"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dircolors/"
description: "dircolors – color setup for ls"
---

<h2 class="name">NAME</h2>
<p> dircolors &#8211; color setup for ls </p>
<h2>SYNOPSIS</h2>
<p> <code>dircolors</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Output commands to set the LS_COLORS environment variable.</p>
<h3>Determine format of output:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;sh</code>, <code>&#8211;bourne-shell</code></p>
<dd> output Bourne shell code to set LS_COLORS</p>
<dt><code>-c</code>, <code>&#8211;csh</code>, <code>&#8211;c-shell</code></p>
<dd> output C shell code to set LS_COLORS</p>
<dt><code>-p</code>, <code>&#8211;print-database</code></p>
<dd> output defaults</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If FILE is specified, read it to determine which colors to use for which file types and extensions. Otherwise, a precompiled database is used. For details on the format of these files, run &#8216;dircolors <code>&#8211;print-database</code>&#8216;.</p>
<h2>AUTHOR</h2>
<p> Written by H. Peter Anvin.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/dircolors">https://www.gnu.org/software/coreutils/dircolors</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) dircolors invocation&#8217; </p>
<h2>Index</h2>
