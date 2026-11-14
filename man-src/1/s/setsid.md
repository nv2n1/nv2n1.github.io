---
title: "setsid(1)"
name: "setsid"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setsid/"
description: "setsid – run a program in a new session"
---

<h2 class="name">NAME</h2>
<p> setsid &#8211; run a program in a new session </p>
<h2>SYNOPSIS</h2>
<p> <code>setsid</code> [options] <i>program</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>setsid</code> runs a program in a new session. The command calls <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) if already a process group leader. Otherwise, it executes a program in the current process. This default behavior is possible to override by the <code>&#8211;fork</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;ctty</code></p>
<dl>
<dt>
<dd> Set the controlling terminal to the current one.</dl>
<p> <code>-f</code>, <code>&#8211;fork</code></p>
<dl>
<dt>
<dd> Always create a new process.</dl>
<p> <code>-w</code>, <code>&#8211;wait</code></p>
<dl>
<dt>
<dd> Wait for the execution of the program to end, and return the exit status of this program as the exit status of <code>setsid</code>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>setsid</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
