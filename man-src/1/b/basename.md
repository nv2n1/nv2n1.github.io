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
<dt><code>-a</code>, <code>&#8211;multiple</code></dt>
<dd> support multiple arguments and treat each as a NAME</dd>
<dt><code>-s</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></dt>
<dd> remove a trailing SUFFIX; implies <code>-a</code></dd>
<dt><code>-z</code>, <code>&#8211;zero</code></dt>
<dd> end each output line with NUL, not newline</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>basename /usr/bin/sort</dt>
<dd> -&gt; &quot;sort&quot;</dd>
<dt>basename include/stdio.h .h</dt>
<dd> -&gt; &quot;stdio&quot;</dd>
<dt>basename -s .h include/stdio.h</dt>
<dd> -&gt; &quot;stdio&quot;</dd>
<dt>basename -a any/str1 any/str2</dt>
<dd> -&gt; &quot;str1&quot; followed by &quot;str2&quot;</dd></dl>
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
