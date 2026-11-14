---
title: "byobu-select-backend(1)"
name: "byobu-select-backend"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-select-backend/"
description: "byobu-select-backend – select your default Byobu backend window manager"
---

<h2>NAME</h2>
<p> byobu-select-backend &#8211; select your default Byobu backend window manager </p>
<h2>SYNOPSIS</h2>
<p> <code>byobu-select-backend</code> [screen|tmux] </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu-select-backend</code> is an application that lists the available Byobu backends and allows you to select your default. </p>
<p> You can select one of either <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) or <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1) on the command line, or giving no command line parameters, the utility will run interactively. </p>
<p> This utility will only affect which backend is used by default when simply running, <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1). Note that at any time, you can force the backend of a particular session by running the helpers, <code><a href="/docs/linux/man/1-byobu-screen/">byobu-screen</a></code>(1) or <code><a href="/docs/linux/man/1-byobu-tmux/">byobu-tmux</a></code>(1). </p>
<h2>FILES</h2>
<p> <i>~/.byobu/backend</i> </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1), <code><a href="/docs/linux/man/1-byobu-screen/">byobu-screen</a></code>(1), <code><a href="/docs/linux/man/1-byobu-tmux/">byobu-tmux</a></code>(1), <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1), <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1)</p>
<dd>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
