---
title: "pty(7)"
name: "pty"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pty/"
description: "pty – pseudoterminal interfaces"
---

<p>pty &#8211; pseudoterminal interfaces</p>
<h2>Description</h2>
<p>A pseudoterminal (sometimes abbreviated &quot;pty&quot;) is a pair of virtual character devices that provide a bidirectional communication channel. One end of the channel is called the <i>master</i>; the other end is called the <i>slave</i>. </p>
<p> The slave end of the pseudoterminal provides an interface that behaves exactly like a classical terminal. A process that expects to be connected to a terminal, can open the slave end of a pseudoterminal and then be driven by a program that has opened the master end. Anything that is written on the master end is provided to the process on the slave end as though it was input typed on a terminal. For example, writing the interrupt character (usually control-C) to the master device would cause an interrupt signal (<code>SIGINT</code>) to be generated for the foreground process group that is connected to the slave. Conversely, anything that is written to the slave end of the pseudoterminal can be read by the process that is connected to the master end. </p>
<p> Data flow between master and slave is handled asynchronously, much like data flow with a physical terminal. Data written to the slave will be available at the master promptly, but may not be available immediately. Similarly, there may be a small processing delay between a write to the master, and the effect being visible at the slave. </p>
<p> Historically, two pseudoterminal APIs have evolved: BSD and System V. SUSv1 standardized a pseudoterminal API based on the System V API, and this API should be employed in all new programs that use pseudoterminals. </p>
<p> Linux provides both BSD-style and (standardized) System V-style pseudoterminals. System V-style terminals are commonly called UNIX 98 pseudoterminals on Linux systems. </p>
<p> Since kernel 2.6.4, BSD-style pseudoterminals are considered deprecated: support can be disabled when building the kernel by disabling the <code>CONFIG_LEGACY_PTYS</code> option. (Starting with Linux 2.6.30, that option is disabled by default in the mainline kernel.) UNIX 98 pseudoterminals should be used in new applications.</p>
<h3>UNIX 98 pseudoterminals</h3>
<p>An unused UNIX 98 pseudoterminal master is opened by calling <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3). (This function opens the master clone device, <i>/dev/ptmx</i>; see <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4).) After performing any program-specific initializations, changing the ownership and permissions of the slave device using <code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), and unlocking the slave using <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3)), the corresponding slave device can be opened by passing the name returned by <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3) in a call to <code><a href="/docs/linux/man/2-open/">open</a></code>(2). </p>
<p> The Linux kernel imposes a limit on the number of available UNIX 98 pseudoterminals. In kernels up to and including 2.6.3, this limit is configured at kernel compilation time (<code>CONFIG_UNIX98_PTYS</code>), and the permitted number of pseudoterminals can be up to 2048, with a default setting of 256. Since kernel 2.6.4, the limit is dynamically adjustable via <i>/proc/sys/kernel/pty/max</i>, and a corresponding file, <i>/proc/sys/kernel/pty/nr</i>, indicates how many pseudoterminals are currently in use. For further details on these two files, see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<h3>BSD pseudoterminals</h3>
<p>BSD-style pseudoterminals are provided as precreated pairs, with names of the form <i>/dev/ptyXY</i> (master) and <i>/dev/ttyXY</i> (slave), where X is a letter from the 16-character set [p-za-e], and Y is a letter from the 16-character set [0-9a-f]. (The precise range of letters in these two sets varies across UNIX implementations.) For example, <i>/dev/ptyp1</i> and <i>/dev/ttyp1</i> constitute a BSD pseudoterminal pair. A process finds an unused pseudoterminal pair by trying to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) each pseudoterminal master until an open succeeds. The corresponding pseudoterminal slave (substitute &quot;tty&quot; for &quot;pty&quot; in the name of the master) can then be opened.</p>
<h2>Files</h2>
<dl>
<dt><i>/dev/ptmx</i></p>
<dd>UNIX 98 master clone device</p>
<dt><i>/dev/pts/*</i></p>
<dd>UNIX 98 slave devices</p>
<dt><i>/dev/pty[p-za-e][0-9a-f]</i></p>
<dd>BSD master devices</p>
<dt><i>/dev/tty[p-za-e][0-9a-f]</i></p>
<dd>BSD slave devices</dl>
<h2>Notes</h2>
<p>Pseudoterminals are used by applications such as network login services (<code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/1-rlogin/">rlogin</a></code>(1), <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1)), terminal emulators such as <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), <code><a href="/docs/linux/man/1-script/">script</a></code>(1), <code><a href="/docs/linux/man/1-screen/">screen</a></code>(1), <code><a href="/docs/linux/man/1-tmux/">tmux</a></code>(1), <code><a href="/docs/linux/man/1-unbuffer/">unbuffer</a></code>(1), and <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1). </p>
<p> A description of the <code>TIOCPKT</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), which controls packet mode operation, can be found in <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2). </p>
<p> The BSD <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations <code>TIOCSTOP</code>, <code>TIOCSTART</code>, <code>TIOCUCNTL</code>, and <code>TIOCREMOTE</code> have not been implemented under Linux.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/3-forkpty/">forkpty</a></code>(3), <code><a href="/docs/linux/man/3-openpty/">openpty</a></code>(3), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
