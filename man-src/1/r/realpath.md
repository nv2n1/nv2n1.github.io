---
title: "realpath(1)"
name: "realpath"
section: "1"
letter: "r"
url: "/docs/linux/man/1-realpath/"
description: "realpath – print the resolved path"
---

<h2 class="name">NAME</h2>
<p> realpath &#8211; print the resolved path </p>
<h2>SYNOPSIS</h2>
<p> <code>realpath</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print the resolved absolute file name; all but the last component must exist</p>
<dl>
<dt><code>-e</code>, <code>&#8211;canonicalize-existing</code></p>
<dd> all components of the path must exist</p>
<dt><code>-m</code>, <code>&#8211;canonicalize-missing</code></p>
<dd> no path components need exist or be a directory</p>
<dt><code>-L</code>, <code>&#8211;logical</code></p>
<dd> resolve &#8216;..&#8217; components before symlinks</p>
<dt><code>-P</code>, <code>&#8211;physical</code></p>
<dd> resolve symlinks as encountered (default)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress most error messages</p>
<dt><code>&#8211;relative-to</code>=<i>,DIR/</i></p>
<dd> print the resolved path relative to DIR</p>
<dt><code>&#8211;relative-base</code>=<i>,DIR/</i></p>
<dd> print absolute paths unless paths below DIR</p>
<dt><code>-s</code>, <code>&#8211;strip</code>, <code>&#8211;no-symlinks</code></p>
<dd> don&#8217;t expand symlinks</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> end each output line with NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-readlink/">readlink</a>(1), <a href="/docs/linux/man/2-readlink/">readlink</a>(2), <a href="/docs/linux/man/3-realpath/">realpath</a>(3) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/realpath">https://www.gnu.org/software/coreutils/realpath</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) realpath invocation&#8217; </p>
<h2>Index</h2>
