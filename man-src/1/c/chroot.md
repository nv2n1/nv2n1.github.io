---
title: "chroot(1)"
name: "chroot"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chroot/"
description: "chroot – run command or interactive shell with special root directory"
---

<h2>NAME</h2>
<p> chroot &#8211; run command or interactive shell with special root directory</p>
<h2>SYNOPSIS</h2>
<p> <code>chroot</code> [<i>OPTION</i>] <i>NEWROOT </i>[<i>COMMAND </i>[<i>ARG</i>]&#8230;]<br />
 <code>chroot</code> <i>OPTION</i></p>
<h2>DESCRIPTION</h2>
<p> Run COMMAND with root directory set to NEWROOT.</p>
<dl>
<dt><code>&#8211;userspec</code>=<i>USER</i>:GROUP</p>
<dd> specify user and group (ID or name) to use</p>
<dt><code>&#8211;groups</code>=<i>G_LIST</i></p>
<dd> specify supplementary groups as g1,g2,..,gN</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If no command is given, run &#8216;${SHELL} <code>-i</code>&#8216; (default: &#8216;/bin/sh <code>-i</code>&#8216;). </p>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="http://www.gnu.org/software/coreutils/">http://www.gnu.org/software/coreutils/</a>&gt; Report chroot translation bugs to &lt;<a rel="nofollow" href="http://translationproject.org/team/">http://translationproject.org/team/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Written by Roland McGrath.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-chroot/">chroot</a>(2) </p>
<p> The full documentation for <code>chroot</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>chroot</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info coreutils &#8216;chroot invocation&#8217;</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
