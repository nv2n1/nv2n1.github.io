---
title: "pts(4)"
name: "pts"
section: "4"
letter: "p"
url: "/docs/linux/man/4-pts/"
description: "ptmx, pts – pseudoterminal master and slave"
---

<p>ptmx, pts &#8211; pseudoterminal master and slave</p>
<h2>Description</h2>
<p>The file <i>/dev/ptmx</i> (the pseudoterminal multiplexor device) is a character file with major number 5 and minor number 2, usually with mode 0666 and ownership root:root. It is used to create a pseudoterminal master and slave pair. </p>
<p> When a process opens <i>/dev/ptmx</i>, it gets a file descriptor for a pseudoterminal master and a pseudoterminal slave device is created in the <i>/dev/pts</i> directory. Each file descriptor obtained by opening <i>/dev/ptmx</i> is an independent pseudoterminal master with its own associated slave, whose path can be found by passing the file descriptor to <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3). </p>
<p> Before opening the pseudoterminal slave, you must pass the master&#8217;s file descriptor to <code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3) and <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3). </p>
<p> Once both the pseudoterminal master and slave are open, the slave provides processes with an interface that is identical to that of a real terminal. </p>
<p> Data written to the slave is presented on the master file descriptor as input. Data written to the master is presented to the slave as input. </p>
<p> In practice, pseudoterminals are used for implementing terminal emulators such as <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), in which data read from the pseudoterminal master is interpreted by the application in the same way a real terminal would interpret the data, and for implementing remote-login programs such as <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8), in which data read from the pseudoterminal master is sent across the network to a client program that is connected to a terminal or terminal emulator. </p>
<p> Pseudoterminals can also be used to send input to programs that normally refuse to read input from pipes (such as <code><a href="/docs/linux/man/1-su/">su</a></code>(1), and <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1)).</p>
<h2>Files</h2>
<p><i>/dev/ptmx</i>, <i>/dev/pts/*</i></p>
<h2>Notes</h2>
<p>The Linux support for the above (known as UNIX 98 pseudoterminal naming) is done using the <i>devpts</i> filesystem, which should be mounted on <i>/dev/pts</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getpt/">getpt</a></code>(3), <code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
