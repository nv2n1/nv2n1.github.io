---
title: "tty(4)"
name: "tty"
section: "4"
letter: "t"
url: "/docs/linux/man/4-tty/"
description: "tty – controlling terminal"
---

<p>tty &#8211; controlling terminal</p>
<h2>Description</h2>
<p>The file <i>/dev/tty</i> is a character file with major number 5 and minor number 0, usually with mode 0666 and ownership root:tty. It is a synonym for the controlling terminal of a process, if any. </p>
<p> In addition to the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests supported by the device that <code>tty</code> refers to, the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) request <code>TIOCNOTTY</code> is supported.</p>
<h3>Tiocnotty</h3>
<p>Detach the calling process from its controlling terminal. </p>
<p> If the process is the session leader, then <code>SIGHUP</code> and <code>SIGCONT</code> signals are sent to the foreground process group and all processes in the current session lose their controlling tty. </p>
<p> This <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) call works only on file descriptors connected to <i>/dev/tty</i>. It is used by daemon processes when they are invoked by a user at a terminal. The process attempts to open <i>/dev/tty</i>. If the open succeeds, it detaches itself from the terminal by using <code>TIOCNOTTY</code>, while if the open fails, it is obviously not attached to a terminal and does not need to detach itself.</p>
<h2>Files</h2>
<p><i>/dev/tty</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4), <code><a href="/docs/linux/man/4-vcs/">vcs</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
