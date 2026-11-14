---
title: "pwd(1)"
name: "pwd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwd/"
description: "pwd – print name of current/working directory"
---

<h2 class="name">NAME</h2>
<p> pwd &#8211; print name of current/working directory </p>
<h2>SYNOPSIS</h2>
<p> <code>pwd</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print the full filename of the current working directory.</p>
<dl>
<dt><code>-L</code>, <code>&#8211;logical</code></p>
<dd> use PWD from environment, even if it contains symlinks</p>
<dt><code>-P</code>, <code>&#8211;physical</code></p>
<dd> avoid all symlinks</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If no option is specified, <code>-P</code> is assumed. </p>
<p> NOTE: your shell may have its own version of pwd, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/pwd">https://www.gnu.org/software/coreutils/pwd</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) pwd invocation&#8217; </p>
<h2>Index</h2>
