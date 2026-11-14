---
title: "byobu-prompt(1)"
name: "byobu-prompt"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-prompt/"
description: "byobu-prompt, byobu-enable-prompt, byobu-disable-prompt – add and remove a nice color prompt to your shell configuration"
---

<h2>NAME</h2>
<p> byobu-prompt, byobu-enable-prompt, byobu-disable-prompt &#8211; add and remove a nice color prompt to your shell configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>byobu-prompt</code></p>
<dl>
<dt><code>byobu-enable-prompt</code></p>
<dd>
<dt><code>byobu-disable-prompt</code></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> Byobu provides a special PS1 prompt command, compatible with Bash shells. It will display the previous command&#8217;s exit code, if it&#8217;s not zero. It will use 3 separate colors for the local username, hostname, and the current working directory. </p>
<p> <code>byobu-enable-prompt</code> will add one line to your <i>~/.bashrc</i>. </p>
<p> You can safely remove the line from your <i>~/.bashrc</i>, which ends in <code>#byobu-prompt</code>. </p>
<p> <code>byobu-disable-prompt</code> will remove its color configuration from <i>~/.bashrc</i>. </p>
<p> <code>byobu-prompt</code> is an interactive wrapper of the previous two tools. </p>
<h2>BUGS</h2>
<p> This is currently only compatible with <code><a href="/docs/linux/man/1-bash/">bash</a>(1)</code>. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1)</p>
<dd>
<dt><code><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></code></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
