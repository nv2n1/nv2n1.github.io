---
title: "basename(1)"
name: "basename"
section: "1"
letter: "b"
url: "/docs/linux/man/1-basename/"
description: "basename – strip directory and suffix from filenames"
---

<h2 class="name">NAME</h2>
<p> basename &#8211; strip directory and suffix from filenames </p>
<h2>SYNOPSIS</h2>
<p> <code>basename</code> <i>,NAME /</i>[<i>,SUFFIX/</i>]<br />
 <code>basename</code> <i>,OPTION/</i>&#8230; <i>,NAME/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print NAME with any leading directory components removed. If specified, also remove a trailing SUFFIX. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;multiple</code></p>
<dd> support multiple arguments and treat each as a NAME</p>
<dt><code>-s</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></p>
<dd> remove a trailing SUFFIX; implies <code>-a</code></p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> end each output line with NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>basename /usr/bin/sort</p>
<dd> -&gt; &quot;sort&quot;</p>
<dt>basename include/stdio.h .h</p>
<dd> -&gt; &quot;stdio&quot;</p>
<dt>basename -s .h include/stdio.h</p>
<dd> -&gt; &quot;stdio&quot;</p>
<dt>basename -a any/str1 any/str2</p>
<dd> -&gt; &quot;str1&quot; followed by &quot;str2&quot;</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dirname/">dirname</a>(1), <a href="/docs/linux/man/1-readlink/">readlink</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/basename">https://www.gnu.org/software/coreutils/basename</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) basename invocation&#8217; </p>
<h2>Index</h2>
