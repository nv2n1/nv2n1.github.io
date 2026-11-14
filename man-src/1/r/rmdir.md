---
title: "rmdir(1)"
name: "rmdir"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmdir/"
description: "rmdir – remove empty directories"
---

<h2 class="name">NAME</h2>
<p> rmdir &#8211; remove empty directories </p>
<h2>SYNOPSIS</h2>
<p> <code>rmdir</code> [<i>,OPTION/</i>]&#8230; <i>,DIRECTORY/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Remove the DIRECTORY(ies), if they are empty.</p>
<dl>
<dt> <code>&#8211;ignore-fail-on-non-empty</code></p>
<dt>
<dd>
<dd>ignore each failure that is solely because a directory</p>
<dt>
<dd> is non-empty</p>
<dt><code>-p</code>, <code>&#8211;parents</code></p>
<dd> remove DIRECTORY and its ancestors; e.g., &#8216;rmdir <code>-p</code> a/b/c&#8217; is similar to &#8216;rmdir a/b/c a/b a&#8217;</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output a diagnostic for every directory processed</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-rmdir/">rmdir</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/rmdir">https://www.gnu.org/software/coreutils/rmdir</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) rmdir invocation&#8217; </p>
<h2>Index</h2>
