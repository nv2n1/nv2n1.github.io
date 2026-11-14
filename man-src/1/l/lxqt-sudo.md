---
title: "lxqt-sudo(1)"
name: "lxqt-sudo"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxqt-sudo/"
description: "lxqt-sudo, lxsu – execute a command as privileged user"
---

<h2>NAME</h2>
<p> <code>lxqt-sudo</code>, <code>lxsu</code> &#8211; execute a command as privileged user</p>
<h2>SYNOPSIS</h2>
<p> <code>lxqt-sudo</code> <i>option</i> [<i>command</i> [<i>arguments</i>]]<br />
 <code>lxsu</code> [<i>option</i>] [<i>command</i> [<i>arguments</i>]]<br />
 <code>lxsudo</code> [<i>option</i>] [<i>command</i> [<i>arguments</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxqt-sudo</code> (and symlinks <code>lxsu</code>, <code>lxsudo</code>) is a graphical QT frontend for plain <code><a href="/docs/linux/man/8-sudo/">sudo</a>(8)</code> or <code><a href="/docs/linux/man/1-su/">su</a>(1)</code> (for requesting optional password in GUI fashion).<br />
 When invoked it simply spawns child <i>sudo</i> or <i>su</i> process with requested <i>command</i> (and optional <i>arguments</i>). If <i>sudo</i>/<i>su</i> requests user&#8217;s password, the GUI password dialog is shown and (after submit) the password is provided to backend. </p>
<h2>OPTIONS</h2>
<p> <code>option</code> is one of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-h|&#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print help. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-v|&#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print version information. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-s|&#8211;su&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use&nbsp;<wbr><i>su</i>&nbsp;<wbr>as backend&nbsp;<wbr>(default for&nbsp;<wbr><code>lxqt-sudo</code>&nbsp;<wbr>&amp;&nbsp;<wbr><code>lxsudo</code>&nbsp;<wbr>is&nbsp;<wbr><i>sudo</i>, for&nbsp;<wbr><code>lxsu</code>&nbsp;<wbr>is&nbsp;<wbr><i>su</i>). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d|&#8211;sudo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use&nbsp;<wbr><i>sudo</i>&nbsp;<wbr>as backend&nbsp;<wbr>(default for&nbsp;<wbr><code>lxqt-sudo</code>&nbsp;<wbr>&amp;&nbsp;<wbr><code>lxsudo</code>&nbsp;<wbr>is&nbsp;<wbr><i>sudo</i>, for&nbsp;<wbr><code>lxsu</code>&nbsp;<wbr>is&nbsp;<wbr><i>su</i>).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/lxde/lxqt/issues">https://github.com/lxde/lxqt/issues</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-sudo/">sudo</a>(8)</code> <code><a href="/docs/linux/man/1-su/">su</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> This manual page was created by <code>Palo Kisa</code> <i>&lt;palo.kisa [at] gmail.com&gt;</i> for <code>LXQt</code> project. </p>
<h2>Index</h2>
