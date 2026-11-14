---
title: "byobu-launcher-install(1)"
name: "byobu-launcher-install"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-launcher-install/"
description: "byobu-launcher-install – Byobu Launcher installation utility"
---

<h2>NAME</h2>
<p> byobu-launcher-install &#8211; Byobu Launcher installation utility </p>
<h2>SYNOPSIS</h2>
<p> byobu-launcher-install [-n|&#8211;no-logout] </p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-byobu-launcher-install/">byobu-launcher-install</a></code>(1) is a simple utilty that will add a line to your <i>$HOME/.profile</i> file which launches <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) any time you login through <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) or on a <code><a href="/docs/linux/man/4-console/">console</a></code>(4). </p>
<p> By default, when users detach from the <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) session they will also logout. Users can change this behavior by adding the [-n|&#8211;no-logout] option when they run <code><a href="/docs/linux/man/1-byobu-launcher-install/">byobu-launcher-install</a></code>(1). </p>
<p> You can disable this behavior entirely at any time with the <code><a href="/docs/linux/man/1-byobu-launcher-uninstall/">byobu-launcher-uninstall</a>(1) utility. </p>
<p> </code></p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-screen/">screen</a></code>(1), <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/4-console/">console</a></code>(4), <code><a href="/docs/linux/man/1-byobu-launcher-uninstall/">byobu-launcher-uninstall</a></code>(1)</p>
<dd>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
