---
title: "dirname(1)"
name: "dirname"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dirname/"
description: "dirname – strip last component from file name"
---

<h2 class="name">NAME</h2>
<p> dirname &#8211; strip last component from file name </p>
<h2>SYNOPSIS</h2>
<p> <code>dirname</code> [<i>,OPTION/</i>] <i>,NAME/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Output each NAME with its last non-slash component and trailing slashes removed; if NAME contains no /&#8217;s, output &#8216;.&#8217; (meaning the current directory).</p>
<dl>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> end each output line with NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>dirname /usr/bin/</p>
<dd> -&gt; &quot;/usr&quot;</p>
<dt>dirname dir1/str dir2/str</p>
<dd> -&gt; &quot;dir1&quot; followed by &quot;dir2&quot;</p>
<dt>dirname stdio.h</p>
<dd> -&gt; &quot;.&quot;</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-basename/">basename</a>(1), <a href="/docs/linux/man/1-readlink/">readlink</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/dirname">https://www.gnu.org/software/coreutils/dirname</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) dirname invocation&#8217; </p>
<h2>Index</h2>
