---
title: "im-launch(1)"
name: "im-launch"
section: "1"
letter: "i"
url: "/docs/linux/man/1-im-launch/"
description: "im-launch – launch input method and execute session program"
---

<h2 class="name">NAME</h2>
<p> im-launch &#8211; launch input method and execute session program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>im-launch </code><i>SESSION-PROGRAM</i></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>im-launch</code> command is used to start a input method framework server daemon such as <code>ibus-daemon</code>, set up the appropriate environment variables for the client programs, and execute <i>SESSION-PROGRAM</i> such as <code>x-session-manager</code>. </p>
<p> This command is usually not invoked from the console of a normal user but is normally invoked by the <code>/etc/X11/Xsession.d/70im-config_launch</code>. </p>
<h2>TROUBLESHOOT</h2>
<p> If you have any problem, see the first part of <code>~/.xsession-errors</code> and look for the cause. If you are running <code>im-config</code> while Debian (sid) system is undergoing a major library transition, you may need to manually set up <code>~/.xinputrc</code> with adjusted library version number etc. Please file a bug report to the im-config package using <a href="/docs/linux/man/1-reportbug/">reportbug</a>(1) describing your resolution experience. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-im-config/">im-config</a>(8),</code> <code>/usr/share/doc/im-config/README.Debian.gz</code></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Aron Xu &lt;aron [at] debian.org&gt;, and Osamu Aoki &lt;osamu [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
