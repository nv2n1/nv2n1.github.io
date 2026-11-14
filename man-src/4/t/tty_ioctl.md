---
title: "tty_ioctl(4)"
name: "tty_ioctl"
section: "4"
letter: "t"
url: "/docs/linux/man/4-tty_ioctl/"
description: "ioctl_tty – ioctls for terminals and serial lines"
---

<p>ioctl_tty &#8211; ioctls for terminals and serial lines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;termios.h&gt;
int ioctl(int fd, int cmd, ...);</code></pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) call for terminals and serial ports accepts many possible command arguments. Most require a third argument, of varying type, here called <i>argp</i> or <i>arg</i>. Use of <i>ioctl</i> makes for nonportable programs. Use the POSIX interface described in <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) whenever possible.</p>
<h3>Get and set terminal attributes</h3>
<dl>
<dt><code>TCGETS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>struct termios *</code><i>argp</i></p>
<dd>Equivalent to<br />
 <i>tcgetattr(fd, argp)</i>.</p>
<dd>Get the current serial port settings.</p>
<dt><code>TCSETS<tt>&nbsp;</tt>const struct termios *</code><i>argp</i></p>
<dd>Equivalent to<br />
 <i>tcsetattr(fd, TCSANOW, argp)</i>.</p>
<dd>Set the current serial port settings.</p>
<dt><code>TCSETSW<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct termios *</code><i>argp</i></p>
<dd>Equivalent to<br />
 <i>tcsetattr(fd, TCSADRAIN, argp)</i>.</p>
<dd>Allow the output buffer to drain, and set the current serial port settings.</p>
<dt><code>TCSETSF<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct termios *</code><i>argp</i></p>
<dd>Equivalent to<br />
 <i>tcsetattr(fd, TCSAFLUSH, argp)</i>.</p>
<dd>Allow the output buffer to drain, discard pending input, and set the current serial port settings.</dl>
<p> The following four ioctls are just like <code>TCGETS</code>, <code>TCSETS</code>, <code>TCSETSW</code>, <code>TCSETSF</code>, except that they take a <i>struct termio&nbsp;*</i> instead of a <i>struct termios&nbsp;*</i>.</p>
<dl>
<dd><code>TCGETA<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>struct termio *</code><i>argp</i></p>
<dd><code>TCSETA<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct termio *</code><i>argp</i></p>
<dd><code>TCSETAW<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct termio *</code><i>argp</i></p>
<dd><code>TCSETAF<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct termio *</code><i>argp</i></dl>
<h3>Locking the termios structure</h3>
<p>The<br />
 <i>termios</i> structure of a terminal can be locked. The lock is itself a <i>termios</i> structure, with nonzero bits or fields indicating a locked value.</p>
<dl>
<dt><code>TIOCGLCKTRMIOS<tt>&nbsp;</tt>struct termios *</code><i>argp</i></p>
<dd>Gets the locking status of the<br />
 <i>termios</i> structure of the terminal.</p>
<dt><code>TIOCSLCKTRMIOS<tt>&nbsp;</tt>const struct termios *</code><i>argp</i></p>
<dd>Sets the locking status of the<br />
 <i>termios</i> structure of the terminal. Only a process with the <code>CAP_SYS_ADMIN</code> capability can do this.</dl>
<h3>Get and set window size</h3>
<p>Window sizes are kept in the kernel, but not used by the kernel (except in the case of virtual consoles, where the kernel will update the window size when the size of the virtual console changes, for example, by loading a new font). The following constants and structure are defined in <i>&lt;sys/ioctl.h&gt;</i>.</p>
<dl>
<dt><code>TIOCGWINSZ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>struct winsize *</code><i>argp</i></p>
<dd>Get window size.</p>
<dt><code>TIOCSWINSZ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const struct winsize *</code><i>argp</i></p>
<dd>Set window size.
</dl>
<p> The struct used by these ioctls is defined as struct winsize {<br />
    unsigned short ws_row;<br />
    unsigned short ws_col;<br />
    unsigned short ws_xpixel; /* unused */<br />
    unsigned short ws_ypixel; /* unused */<br />
}; When the window size changes, a <code>SIGWINCH</code> signal is sent to the foreground process group.</p>
<h3>Sending a break</h3>
<dl>
<dt><code>TCSBRK<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int </code><i>arg</i></p>
<dd>Equivalent to<br />
 <i>tcsendbreak(fd, arg)</i>.</p>
<dd>If the terminal is using asynchronous serial data transmission, and <i>arg</i> is zero, then send a break (a stream of zero bits) for between 0.25 and 0.5 seconds. If the terminal is not using asynchronous serial data transmission, then either a break is sent, or the function returns without doing anything. When <i>arg</i> is nonzero, nobody knows what will happen.</p>
<dd>(SVr4, UnixWare, Solaris, Linux treat <i>tcsendbreak(fd,arg)</i> with nonzero <i>arg</i> like <i>tcdrain(fd)</i>. SunOS treats <i>arg</i> as a multiplier, and sends a stream of bits <i>arg</i> times as long as done for zero <i>arg</i>. DG/UX and AIX treat <i>arg</i> (when nonzero) as a time interval measured in milliseconds. HP-UX ignores <i>arg</i>.)</p>
<dt><code>TCSBRKP<tt>&nbsp;</tt>int </code><i>arg</i></p>
<dd>So-called &quot;POSIX version&quot; of<br />
 <code>TCSBRK</code>. It treats nonzero <i>arg</i> as a time interval measured in deciseconds, and does nothing when the driver does not support breaks.</p>
<dt><code>TIOCSBRK<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>Turn break on, that is, start sending zero bits.</p>
<dt><code>TIOCCBRK<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>Turn break off, that is, stop sending zero bits.
</dl>
<h3>Software flow control</h3>
<dl>
<dt><code>TCXONC<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int </code><i>arg</i></p>
<dd>Equivalent to<br />
 <i>tcflow(fd, arg)</i>.</p>
<dd>See <code><a href="/docs/linux/man/3-tcflow/">tcflow</a></code>(3) for the argument values <code>TCOOFF</code>, <code>TCOON</code>, <code>TCIOFF</code>, <code>TCION</code>.</dl>
<h3>Buffer count and flushing</h3>
<dl>
<dt><code>FIONREAD<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int *</code><i>argp</i></p>
<dd>Get the number of bytes in the input buffer.</p>
<dt><code>TIOCINQ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int *</code><i>argp</i></p>
<dd>Same as<br />
 <code>FIONREAD</code>.</p>
<dt><code>TIOCOUTQ<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int *</code><i>argp</i></p>
<dd>Get the number of bytes in the output buffer.</p>
<dt><code>TCFLSH<tt>&nbsp;</tt>int </code><i>arg</i></p>
<dd>Equivalent to<br />
 <i>tcflush(fd, arg)</i>.</p>
<dd>See <code><a href="/docs/linux/man/3-tcflush/">tcflush</a></code>(3) for the argument values <code>TCIFLUSH</code>, <code>TCOFLUSH</code>, <code>TCIOFLUSH</code>.</dl>
<h3>Faking input</h3>
<dl>
<dt><code>TIOCSTI<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const char *</code><i>argp</i></p>
<dd>Insert the given byte in the input queue.
</dl>
<h3>Redirecting console output</h3>
<dl>
<dt><code>TIOCCONS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>Redirect output that would have gone to<br />
 <i>/dev/console</i> or <i>/dev/tty0</i> to the given terminal. If that was a pseudoterminal master, send it to the slave. In Linux before version 2.6.10, anybody can do this as long as the output was not redirected yet; since version 2.6.10, only a process with the <code>CAP_SYS_ADMIN</code> capability may do this. If output was redirected already, then <code>EBUSY</code> is returned, but redirection can be stopped by using this ioctl with <i>fd</i> pointing at <i>/dev/console</i> or <i>/dev/tty0</i>.</dl>
<h3>Controlling terminal</h3>
<dl>
<dt><code>TIOCSCTTY<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int </code><i>arg</i></p>
<dd>Make the given terminal the controlling terminal of the calling process.<br />
 The calling process must be a session leader and not have a controlling terminal already. For this case, <i>arg</i> should be specified as zero.</p>
<dd>If this terminal is already the controlling terminal of a different session group, then the ioctl fails with <code>EPERM</code>, unless the caller has the <code>CAP_SYS_ADMIN</code> capability and <i>arg</i> equals 1, in which case the terminal is stolen, and all processes that had it as controlling terminal lose it.</p>
<dt><code>TIOCNOTTY<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>If the given terminal was the controlling terminal of the calling process,<br />
 give up this controlling terminal. If the process was session leader, then send <code>SIGHUP</code> and <code>SIGCONT</code> to the foreground process group and all processes in the current session lose their controlling terminal.</dl>
<h3>Process group and session ID</h3>
<dl>
<dt><code>TIOCGPGRP<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pid_t *</code><i>argp</i></p>
<dd>When successful, equivalent to<br />
 <i>*argp = tcgetpgrp(fd)</i>.</p>
<dd>Get the process group ID of the foreground process group on this terminal.</p>
<dt><code>TIOCSPGRP<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const pid_t *</code><i>argp</i></p>
<dd>Equivalent to<br />
 <i>tcsetpgrp(fd, *argp)</i>.</p>
<dd>Set the foreground process group ID of this terminal.</p>
<dt><code>TIOCGSID<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pid_t *</code><i>argp</i></p>
<dd>Get the session ID of the given terminal.<br />
 This fails with the error <code>ENOTTY</code> if the terminal is not a master pseudoterminal and not our controlling terminal. Strange.</dl>
<h3>Exclusive mode</h3>
<dl>
<dt><code>TIOCEXCL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>Put the terminal into exclusive mode.<br />
 No further <code><a href="/docs/linux/man/2-open/">open</a></code>(2) operations on the terminal are permitted. (They fail with <code>EBUSY</code>, except for a process with the <code>CAP_SYS_ADMIN</code> capability.)</p>
<dt><code>TIOCGEXCL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int *</code><i>argp</i></p>
<dd>(since Linux 3.8)<br />
 If the terminal is currently in exclusive mode, place a nonzero value in the location pointed to by <i>argp</i>; otherwise, place zero in <i>*argp</i>.</p>
<dt><code>TIOCNXCL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>void</code></p>
<dd>Disable exclusive mode.
</dl>
<h3>Line discipline</h3>
<dl>
<dt><code>TIOCGETD<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>int *</code><i>argp</i></p>
<dd>Get the line discipline of the terminal.</p>
<dt><code>TIOCSETD<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const int *</code><i>argp</i></p>
<dd>Set the line discipline of the terminal.
</dl>
<h3>Pseudoterminal ioctls</h3>
<dl>
<dt><code>TIOCPKT<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>const int *</code><i>argp</i></p>
<dd>Enable (when<br />
 *<i>argp</i> is nonzero) or disable packet mode. Can be applied to the master side of a pseudoterminal only (and will return <code>ENOTTY</code> otherwise). In packet mode, each subsequent <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will return a packet that either contains a single nonzero control byte, or has a single byte containing zero (&#8216;
