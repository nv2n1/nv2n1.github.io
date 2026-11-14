---
title: "byobu-select-session(1)"
name: "byobu-select-session"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-select-session/"
description: "byobu-select-session – select and connect to a byobu session"
---

<h2>NAME</h2>
<p> byobu-select-session &#8211; select and connect to a byobu session </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu-select-session</code> is an application that lists the available screen sessions running on the system, and prompts the user to select one. The user also has the option to create a new Byobu session, or launch the default shell without Byobu. </p>
<p> If an invalid selection is chosen 3 times in a row, the user is connected to the youngest session. </p>
<p> By default, if only one session exists, the user is connected to that session, and if no sessions exist, a new session is created &#8212; such that there is no interactive prompt in the normal behavior. However, some users may choose to always be prompted, by touching the file $BYOBU_CONFIG_DIR/.always-select. </p>
<p> Note that BYOBU_CONFIG_DIR=$HOME/.byobu. </p>
<p> Named sessions that begin with a &quot;.&quot; are &quot;hidden&quot; from <code><a href="/docs/linux/man/1-byobu-select-session/">byobu-select-session</a></code>(1). This is useful, for instance, if you do not want a session to be automatically selected at login. Example:<br />
&nbsp;<wbr>&nbsp;<wbr>byobu -S .hidden </p>
<h2>FILES</h2>
<p> <i>$BYOBU_CONFIG_DIR/.always-select</i> </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1), <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1)</p>
<dd>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
