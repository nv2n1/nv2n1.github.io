---
title: "mesg(1)"
name: "mesg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mesg/"
description: "mesg – display (or do not display) messages from other users"
---

<h2 class="name">NAME</h2>
<p> mesg &#8211; display (or do not display) messages from other users </p>
<h2>SYNOPSIS</h2>
<p> <code>mesg</code> [<i>option</i>] [<code>n</code>|<code>y</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mesg</code> utility is invoked by a user to control write access others have to the terminal device associated with standard error output. If write access is allowed, then programs such as <code><a href="/docs/linux/man/1-talk/">talk</a></code>(1) and <code><a href="/docs/linux/man/1-write/">write</a></code>(1) may display messages on the terminal. </p>
<p> Traditionally, write access is allowed by default. However, as users become more conscious of various security risks, there is a trend to remove write access by default, at least for the primary login shell. To make sure your ttys are set the way you want them to be set, <code>mesg</code> should be executed in your login scripts. </p>
<p> The <code>mesg</code> utility silently exits with error status 2 if not executed on terminal. In this case execute <code>mesg</code> is pointless. The command line option <code>&#8211;verbose</code> forces mesg to print a warning in this situation. This behaviour has been introduced in version 2.33.</p>
<h2>ARGUMENTS</h2>
<p> <code>n</code></p>
<dl>
<dt>
<dd> Disallow messages.</dl>
<p> <code>y</code></p>
<dl>
<dt>
<dd> Allow messages to be displayed.</dl>
<p> If no arguments are given, <code>mesg</code> shows the current message status on standard error output.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Explain what is being done.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>mesg</code> utility exits with one of the following values: </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Messages are allowed.</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Messages are not allowed.</dl>
<p> <code>&gt;1</code></p>
<dl>
<dt>
<dd> An error has occurred.</dl>
<h2>FILES</h2>
<p> <i>/dev/[pt]ty[pq]?</i></p>
<h2>HISTORY</h2>
<p> A <code>mesg</code> command appeared in Version 6 AT&amp;T UNIX.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-talk/">talk</a></code>(1), <code><a href="/docs/linux/man/1-write/">write</a></code>(1), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>mesg</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
