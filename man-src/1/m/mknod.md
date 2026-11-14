---
title: "mknod(1)"
name: "mknod"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mknod/"
description: "mknod – make block or character special files"
---

<h2 class="name">NAME</h2>
<p> mknod &#8211; make block or character special files </p>
<h2>SYNOPSIS</h2>
<p> <code>mknod</code> [<i>,OPTION/</i>]&#8230; <i>,NAME TYPE /</i>[<i>,MAJOR MINOR/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Create the special file NAME of the given TYPE. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>,MODE/</i></p>
<dd> set file permission bits to MODE, not a=rw &#8211; umask</p>
<dt><code>-Z</code></p>
<dd> set the SELinux security context to default type</p>
<dt><code>&#8211;context</code>[=<i>,CTX/</i>]</p>
<dd> like <code>-Z</code>, or if CTX is specified then set the SELinux or SMACK security context to CTX</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Both MAJOR and MINOR must be specified when TYPE is b, c, or u, and they must be omitted when TYPE is p. If MAJOR or MINOR begins with 0x or 0X, it is interpreted as hexadecimal; otherwise, if it begins with 0, as octal; otherwise, as decimal. TYPE may be:</p>
<dl>
<dt>b</p>
<dd> create a block (buffered) special file</p>
<dt>c, u</p>
<dd> create a character (unbuffered) special file</p>
<dt>p</p>
<dd> create a FIFO</dl>
<p> NOTE: your shell may have its own version of mknod, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-mknod/">mknod</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/mknod">https://www.gnu.org/software/coreutils/mknod</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) mknod invocation&#8217; </p>
<h2>Index</h2>
