---
title: "reptyr(1)"
name: "reptyr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reptyr/"
description: "reptyr – Reparent a running program to a new terminal"
---

<h2>NAME</h2>
<p> reptyr &#8211; Reparent a running program to a new terminal</p>
<h2>SYNOPSIS</h2>
<p> <code>reptyr</code> <i>PID</i> </p>
<p> <code>reptyr -l|-L [COMMAND [ARGS]]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>reptyr</code> is a utility for taking an existing running program and attaching it to a new terminal. Started a long-running process over ssh, but have to leave and don&#8217;t want to interrupt it? Just start a screen, use <code>reptyr</code> to grab it, and then kill the ssh session and head on home. </p>
<p> <code>reptyr</code> works by attaching to the target program using <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), redirecting relevant file descriptors, and changing the program&#8217;s controlling terminal (See <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)) It is this last detail that makes <code>reptyr</code> work much better than alternatives such as <code><a href="/docs/linux/man/1-retty/">retty</a></code>(1). </p>
<p> After attaching a program, the program will appear to be either backgrounded or suspended to the shell it was launched from (depending on the shell). For maximal safety you can run</p>
<dl>
<dt>
<dd> bg; disown</dl>
<p> in the old shell to remove the association with the program, but <code>reptyr</code> will attempt to ensure that the target program remains running even if you close the shell without doing so. </p>
<h2>OPTIONS</h2>
<p> <code>-l, -L [COMMAND [ARGS]]</code></p>
<dl>
<dt>
<dd> Instead of attaching to a new process, create a new pty pair, proxy the master end to the current terminal, and then print the name of the slave pty. This can be passed to e.g. <code>gdb&#8217;s</code> <i>set inferior-tty</i> option. </p>
<p> If an optional <code>COMMAND</code> and <code>ARGS</code> are passed in conjunction with <code>-l,</code> that command will be executed as a child of <code>reptyr</code> with the <code>REPTYR_PTY</code> environment variable set to the name of the slave pty. If <code>-L</code> is used instead of <code>-l,</code> then fds 0-2 of the child will also be redirected to point to the slave, and the child will be run in a fresh session with the slave as its controlling terminal.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd>
<p> By default, reptyr will move any file descriptors in the target that were connected to the target&#8217;s controlling terminal to point to the new terminal. The <code>-s</code> option will cause reptyr to unconditionally attach file descriptors 0, 1, and 2 in the target, even if the target has no controlling terminal or they are not connected to a terminal.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Print the version of <code>reptyr</code> and exit.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print a usage message and exit.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Print verbose debug output while running.</dl>
<h2>NOTES</h2>
<p> <code>reptyr</code> depends on the <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) system call to attach to the remote program. On Ubuntu Maverick and higher, this ability is disabled by default for security reasons. You can enable it temporarily by doing</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>echo 0&nbsp;<wbr>&gt;&nbsp;<wbr>/proc/sys/kernel/yama/ptrace_scope</dl>
<p> as root, or permanently by editing the file <i>/etc/sysctl.d/10-ptrace.conf</i>, which also contains more information about this setting. </p>
<h2>BUGS</h2>
<p> When attaching to some curses programs, they will not redraw the screen right away, and a <code>^L</code> or similar will be needed to force a redraw. </p>
<p> Similarly, after attaching to certain programs, the old terminal will be left in an odd state, and a <code>clear</code> or even <code>reset</code> may be required before the old terminal is usable again. </p>
<p> Attaching to rtorrent (and probably some other apps) doesn&#8217;t work right (rtorrent stops accepting input) (The problem is that rtorrent is using epoll to poll stdin, and we don&#8217;t update the internal reference that the epoll fd has to the old tty). </p>
<p> Attaching to a process with children doesn&#8217;t work right. This should be possible to fix &#8212; I just need to ptrace each child individually and do the same games to it. </p>
<p> Attaching a <code><a href="/docs/linux/man/1-less/">less</a></code>(1) process doesn&#8217;t work if you have a <i>.lessfilter</i> file, as <code>less</code> leaves around a zombie child in this case. This could be worked around. </p>
<p> Bugs should be reported to the author (see below) or via the issue tracker on GitHub. </p>
<h2>AUTHORS</h2>
<p> reptyr was written by Nelson Elhage &lt;nelhage [at] nelhage.com&gt;. </p>
<h2>HOMEPAGE</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-neercs/">neercs</a></code>(1), <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1) </p>
<h2>Index</h2>
