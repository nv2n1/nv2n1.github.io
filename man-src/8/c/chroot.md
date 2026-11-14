---
title: "chroot(8)"
name: "chroot"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chroot/"
description: "chroot – run command or interactive shell with special root directory"
---

<p>chroot &#8211; run command or interactive shell with special root directory</p>
<h2>Synopsis</h2>
<p><code>chroot</code> [<i>,OPTION/</i>] <i>,NEWROOT /</i>[<i>,COMMAND /</i>[<i>,ARG/</i>]&#8230;]<br />
 <code>chroot</code> <i>,OPTION/</i></p>
<h2>Description</h2>
<p>Run COMMAND with root directory set to NEWROOT.</p>
<dl>
<dt><code>&#8211;groups</code>=<i>,G_LIST/</i></p>
<dd>specify supplementary groups as g1,g2,..,gN</p>
<dt><code>&#8211;userspec</code>=<i>,USER/</i>:GROUP</p>
<dd>specify user and group (ID or name) to use</p>
<dt><code>&#8211;skip-chdir</code></p>
<dd>do not change working directory to &#8216;/&#8217;</p>
<dt><code>&#8211;help</code></p>
<dd>display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</dl>
<p> If no command is given, run &#8216;&quot;$SHELL&quot; <code>-i</code>&#8216; (default: &#8216;/bin/sh <code>-i</code>&#8216;).</p>
<h2>Author</h2>
<p>Written by Roland McGrath.</p>
<h2>Reporting Bugs</h2>
<p>GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-chroot/">chroot</a>(2)<br />
 Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/chroot">https://www.gnu.org/software/coreutils/chroot</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) chroot invocation&#8217; </p>
