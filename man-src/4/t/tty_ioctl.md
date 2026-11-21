---

title: "tty_ioctl(4)"
name: "tty_ioctl"
section: "4"
letter: "t"
url: "/docs/linux/man/4-tty_ioctl/"
description: "ioctl_tty – ioctls for terminals and serial lines"
---

<p>ioctl_tty &#8211; ioctls for terminals and serial lines </p>

<p> <code>#include &lt;termios.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>fd</i><code>, int </code><i>cmd</i><code>, ...);</code>  </p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) call for terminals and serial ports accepts many possible command arguments. Most require a third argument, of varying type, here called <i>argp</i> or <i>arg</i>. </p>
<p>Use of <i>ioctl</i> makes for nonportable programs. Use the POSIX interface described in <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) whenever possible.  </p>
<h3>Get and set terminal attributes</h3>
<dl>
<dt><code>TCGETS <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>struct termios *</code><i>argp</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcgetattr(fd, argp)</i>. </p>
 </dd>
<dd> <p> Get the current serial port settings. </p>
 </dd>
<dt><code>TCSETS <code>&nbsp;</code>const struct termios *</code><i>argp</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcsetattr(fd, TCSANOW, argp)</i>. </p>
 </dd>
<dd> <p> Set the current serial port settings. </p>
 </dd>
<dt><code>TCSETSW <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct termios *</code><i>argp</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcsetattr(fd, TCSADRAIN, argp)</i>. </p>
 </dd>
<dd> <p> Allow the output buffer to drain, and set the current serial port settings. </p>
 </dd>
<dt><code>TCSETSF <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct termios *</code><i>argp</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcsetattr(fd, TCSAFLUSH, argp)</i>. </p>
 </dd>
<dd> <p> Allow the output buffer to drain, discard pending input, and set the current serial port settings. </p>
 </dd></dl>
<p>The following four ioctls are just like <code>TCGETS</code>, <code>TCSETS</code>, <code>TCSETSW</code>, <code>TCSETSF</code>, except that they take a <i>struct termio&nbsp;*</i> instead of a <i>struct termios&nbsp;*</i>. </p>
<dl>
<dd> <p> <code>TCGETA <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>struct termio *</code><i>argp</i> </p>
 </dd>
<dd> <p> <code>TCSETA <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct termio *</code><i>argp</i> </p>
 </dd>
<dd> <p> <code>TCSETAW <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct termio *</code><i>argp</i> </p>
 </dd>
<dd> <p> <code>TCSETAF <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct termio *</code><i>argp</i> </p>
 </dd></dl>
<h3>Locking the termios structure</h3>
<p> The<br />
 <i>termios</i> structure of a terminal can be locked. The lock is itself a <i>termios</i> structure, with nonzero bits or fields indicating a locked value. </p>
<dl>
<dt><code>TIOCGLCKTRMIOS <code>&nbsp;</code>struct termios *</code><i>argp</i></dt>
<dd> <p> Gets the locking status of the<br />
 <i>termios</i> structure of the terminal. </p>
 </dd>
<dt><code>TIOCSLCKTRMIOS <code>&nbsp;</code>const struct termios *</code><i>argp</i></dt>
<dd> <p> Sets the locking status of the<br />
 <i>termios</i> structure of the terminal. Only a process with the <code>CAP_SYS_ADMIN</code> capability can do this. </p>
 </dd></dl>
<h3>Get and set window size</h3>
<p> Window sizes are kept in the kernel, but not used by the kernel (except in the case of virtual consoles, where the kernel will update the window size when the size of the virtual console changes, for example, by loading a new font). </p>
<p>The following constants and structure are defined in <i>&lt;sys/ioctl.h&gt;</i>. </p>
<dl>
<dt><code>TIOCGWINSZ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>struct winsize *</code><i>argp</i></dt>
<dd> <p> Get window size.<br />
 </p>
 </dd>
<dt><code>TIOCSWINSZ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const struct winsize *</code><i>argp</i></dt>
<dd> <p> Set window size.<br />
 </p>
 </dd></dl>
<p>The struct used by these ioctls is defined as </p>
<p>struct winsize { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short ws_row; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short ws_col; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short ws_xpixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short ws_ypixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;*/ }; </p>
<p>When the window size changes, a <code>SIGWINCH</code> signal is sent to the foreground process group.  </p>
<h3>Sending a break</h3>
<dl>
<dt><code>TCSBRK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int </code><i>arg</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcsendbreak(fd, arg)</i>. </p>
 </dd>
<dd> <p> If the terminal is using asynchronous serial data transmission, and <i>arg</i> is zero, then send a break (a stream of zero bits) for between 0.25 and 0.5 seconds. If the terminal is not using asynchronous serial data transmission, then either a break is sent, or the function returns without doing anything. When <i>arg</i> is nonzero, nobody knows what will happen. </p>
 </dd>
<dd> <p> (SVr4, UnixWare, Solaris, Linux treat <i>tcsendbreak(fd,arg)</i> with nonzero <i>arg</i> like <i>tcdrain(fd)</i>. SunOS treats <i>arg</i> as a multiplier, and sends a stream of bits <i>arg</i> times as long as done for zero <i>arg</i>. DG/UX and AIX treat <i>arg</i> (when nonzero) as a time interval measured in milliseconds. HP-UX ignores <i>arg</i>.) </p>
 </dd>
<dt><code>TCSBRKP <code>&nbsp;</code>int </code><i>arg</i></dt>
<dd> <p> So-called &quot;POSIX version&quot; of<br />
 <code>TCSBRK</code>. It treats nonzero <i>arg</i> as a time interval measured in deciseconds, and does nothing when the driver does not support breaks. </p>
 </dd>
<dt><code>TIOCSBRK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> Turn break on, that is, start sending zero bits.<br />
 </p>
 </dd>
<dt><code>TIOCCBRK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> Turn break off, that is, stop sending zero bits.<br />
 </p>
 </dd></dl>
<h3>Software flow control</h3>
<dl>
<dt><code>TCXONC <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int </code><i>arg</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcflow(fd, arg)</i>. </p>
 </dd>
<dd> <p> See <code><a href="/docs/linux/man/3-tcflow/">tcflow</a></code>(3) for the argument values <code>TCOOFF</code>, <code>TCOON</code>, <code>TCIOFF</code>, <code>TCION</code>. </p>
 </dd></dl>
<h3>Buffer count and flushing</h3>
<dl>
<dt><code>FIONREAD <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Get the number of bytes in the input buffer.<br />
 </p>
 </dd>
<dt><code>TIOCINQ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Same as<br />
 <code>FIONREAD</code>. </p>
 </dd>
<dt><code>TIOCOUTQ <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Get the number of bytes in the output buffer.<br />
 </p>
 </dd>
<dt><code>TCFLSH <code>&nbsp;</code>int </code><i>arg</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcflush(fd, arg)</i>. </p>
 </dd>
<dd> <p> See <code><a href="/docs/linux/man/3-tcflush/">tcflush</a></code>(3) for the argument values <code>TCIFLUSH</code>, <code>TCOFLUSH</code>, <code>TCIOFLUSH</code>. </p>
 </dd></dl>
<h3>Faking input</h3>
<dl>
<dt><code>TIOCSTI <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const char *</code><i>argp</i></dt>
<dd> <p> Insert the given byte in the input queue.<br />
 </p>
 </dd></dl>
<h3>Redirecting console output</h3>
<dl>
<dt><code>TIOCCONS <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> Redirect output that would have gone to<br />
 <i>/dev/console</i> or <i>/dev/tty0</i> to the given terminal. If that was a pseudoterminal master, send it to the slave. In Linux before version 2.6.10, anybody can do this as long as the output was not redirected yet; since version 2.6.10, only a process with the <code>CAP_SYS_ADMIN</code> capability may do this. If output was redirected already, then <code>EBUSY</code> is returned, but redirection can be stopped by using this ioctl with <i>fd</i> pointing at <i>/dev/console</i> or <i>/dev/tty0</i>. </p>
 </dd></dl>
<h3>Controlling terminal</h3>
<dl>
<dt><code>TIOCSCTTY <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int </code><i>arg</i></dt>
<dd> <p> Make the given terminal the controlling terminal of the calling process.<br />
 The calling process must be a session leader and not have a controlling terminal already. For this case, <i>arg</i> should be specified as zero. </p>
 </dd>
<dd> <p> If this terminal is already the controlling terminal of a different session group, then the ioctl fails with <code>EPERM</code>, unless the caller has the <code>CAP_SYS_ADMIN</code> capability and <i>arg</i> equals 1, in which case the terminal is stolen, and all processes that had it as controlling terminal lose it. </p>
 </dd>
<dt><code>TIOCNOTTY <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> If the given terminal was the controlling terminal of the calling process,<br />
 give up this controlling terminal. If the process was session leader, then send <code>SIGHUP</code> and <code>SIGCONT</code> to the foreground process group and all processes in the current session lose their controlling terminal. </p>
 </dd></dl>
<h3>Process group and session ID</h3>
<dl>
<dt><code>TIOCGPGRP <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>pid_t *</code><i>argp</i></dt>
<dd> <p> When successful, equivalent to<br />
 <i>*argp = tcgetpgrp(fd)</i>. </p>
 </dd>
<dd> <p> Get the process group ID of the foreground process group on this terminal. </p>
 </dd>
<dt><code>TIOCSPGRP <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const pid_t *</code><i>argp</i></dt>
<dd> <p> Equivalent to<br />
 <i>tcsetpgrp(fd, *argp)</i>. </p>
 </dd>
<dd> <p> Set the foreground process group ID of this terminal. </p>
 </dd>
<dt><code>TIOCGSID <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>pid_t *</code><i>argp</i></dt>
<dd> <p> Get the session ID of the given terminal.<br />
 This fails with the error <code>ENOTTY</code> if the terminal is not a master pseudoterminal and not our controlling terminal. Strange. </p>
 </dd></dl>
<h3>Exclusive mode</h3>
<dl>
<dt><code>TIOCEXCL <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> Put the terminal into exclusive mode.<br />
 No further <code><a href="/docs/linux/man/2-open/">open</a></code>(2) operations on the terminal are permitted. (They fail with <code>EBUSY</code>, except for a process with the <code>CAP_SYS_ADMIN</code> capability.) </p>
 </dd>
<dt><code>TIOCGEXCL <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> (since Linux 3.8)<br />
 If the terminal is currently in exclusive mode, place a nonzero value in the location pointed to by <i>argp</i>; otherwise, place zero in <i>*argp</i>. </p>
 </dd>
<dt><code>TIOCNXCL <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>void</code></dt>
<dd> <p> Disable exclusive mode.<br />
 </p>
 </dd></dl>
<h3>Line discipline</h3>
<dl>
<dt><code>TIOCGETD <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Get the line discipline of the terminal.<br />
 </p>
 </dd>
<dt><code>TIOCSETD <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> Set the line discipline of the terminal.<br />
 </p>
 </dd></dl>
<h3>Pseudoterminal ioctls</h3>
<dl>
<dt><code>TIOCPKT <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> Enable (when<br />
 *<i>argp</i> is nonzero) or disable packet mode. Can be applied to the master side of a pseudoterminal only (and will return <code>ENOTTY</code> otherwise). In packet mode, each subsequent <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will return a packet that either contains a single nonzero control byte, or has a single byte containing zero (&#8216;\0&#8217;) followed by data written on the slave side of the pseudoterminal. If the first byte is not <code>TIOCPKT_DATA</code> (0), it is an OR of one or more of the following bits: </p>
 </dd>
<dd> <table>
<tr VALIGN=top>
<td><code>TIOCPKT_FLUSHREAD</code></td>
<td>The read queue for the terminal is flushed.
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCPKT_FLUSHWRITE</code></td>
<td>The write queue for the terminal is flushed.
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCPKT_STOP</code></td>
<td>Output to the terminal is stopped.
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCPKT_START</code></td>
<td>Output to the terminal is restarted.
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCPKT_DOSTOP</code></td>
<td>The start and stop characters are <code>haS</code>/<code>haQ</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCPKT_NOSTOP</code></td>
<td>The start and stop characters are not <code>haS</code>/<code>haQ</code>.
</td>
</tr>
</table>
 </dd>
<dd> <p> While packet mode is in use, the presence of control status information to be read from the master side may be detected by a <code><a href="/docs/linux/man/2-select/">select</a></code>(2) for exceptional conditions or a <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) for the <code>POLLPRI</code> event. </p>
 </dd>
<dd> <p> This mode is used by <code><a href="/docs/linux/man/1-rlogin/">rlogin</a></code>(1) and <code>rlogind</code>(8) to implement a remote-echoed, locally <code>haS</code>/<code>haQ</code> flow-controlled remote login. </p>
 </dd>
<dt><code>TIOCGPKT <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> (since Linux 3.8)<br />
 Return the current packet mode setting in the integer pointed to by <i>argp</i>. </p>
 </dd>
<dt><code>TIOCSPTLCK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Set (if<br />
 <i>*argp</i> is nonzero) or remove (if <i>*argp</i> is zero) the lock on the pseudoterminal slave device. (See also <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3).) </p>
 </dd>
<dt><code>TIOCGPTLCK <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> (since Linux 3.8)<br />
 Place the current lock state of the pseudoterminal slave device in the location pointed to by <i>argp</i>. </p>
 </dd>
<dt><code>TIOCGPTPEER <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int </code><i>flags</i></dt>
<dd> <p> (since Linux 4.13)<br />
 Given a file descriptor in <i>fd</i> that refers to a pseudoterminal master, open (with the given <code><a href="/docs/linux/man/2-open/">open</a></code>(2)-style <i>flags</i>) and return a new file descriptor that refers to the peer pseudoterminal slave device. This operation can be performed regardless of whether the pathname of the slave device is accessible through the calling process&#8217;s mount namespace. </p>
 </dd>
<dd> <p> Security-conscious programs interacting with namespaces may wish to use this operation rather than <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the pathname returned by <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), and similar library functions that have insecure APIs. (For example, confusion can occur in some cases using <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3) with a pathname where a devpts filesystem has been mounted in a different mount namespace.) </p>
 </dd></dl>
<p>The BSD ioctls <code>TIOCSTOP</code>, <code>TIOCSTART</code>, <code>TIOCUCNTL</code>, <code>TIOCREMOTE</code> have not been implemented under Linux.  </p>
<h3>Modem control</h3>
<dl>
<dt><code>TIOCMGET <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> Get the status of modem bits.<br />
 </p>
 </dd>
<dt><code>TIOCMSET <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> Set the status of modem bits.<br />
 </p>
 </dd>
<dt><code>TIOCMBIC <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> Clear the indicated modem bits.<br />
 </p>
 </dd>
<dt><code>TIOCMBIS <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> Set the indicated modem bits.<br />
 </p>
 </dd></dl>
<p>The following bits are used by the above ioctls: </p>
<table>
<tr VALIGN=top>
<td><code>TIOCM_LE</code></td>
<td>DSR (data set ready/line enable)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_DTR</code></td>
<td>DTR (data terminal ready)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_RTS</code></td>
<td>RTS (request to send)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_ST</code></td>
<td>Secondary TXD (transmit)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_SR</code></td>
<td>Secondary RXD (receive)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_CTS</code></td>
<td>CTS (clear to send)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_CAR</code></td>
<td>DCD (data carrier detect)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_CD</code></td>
<td>see TIOCM_CAR
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_RNG</code></td>
<td>RNG (ring)
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_RI</code></td>
<td>see TIOCM_RNG
</td>
</tr>
<tr VALIGN=top>
<td><code>TIOCM_DSR</code></td>
<td>DSR (data set ready)
</td>
</tr>
</table>
<dl>
<dt><code>TIOCMIWAITint </code><i>arg</i></dt>
<dd> <p> Wait for any of the 4 modem bits (DCD, RI, DSR, CTS) to change.<br />
 The bits of interest are specified as a bit mask in <i>arg</i>, by ORing together any of the bit values, <code>TIOCM_RNG</code>, <code>TIOCM_DSR</code>, <code>TIOCM_CD</code>, and <code>TIOCM_CTS</code>. The caller should use <code>TIOCGICOUNT</code> to see which bit has changed. </p>
 </dd>
<dt><code>TIOCGICOUNT <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>struct serial_icounter_struct *</code><i>argp</i></dt>
<dd> <p> Get counts of input serial line interrupts (DCD, RI, DSR, CTS).<br />
 The counts are written to the <i>serial_icounter_struct</i> structure pointed to by <i>argp</i>. </p>
 </dd>
<dd> <p> Note: both 1-&gt;0 and 0-&gt;1 transitions are counted, except for RI, where only 0-&gt;1 transitions are counted. </p>
 </dd></dl>
<h3>Marking a line as local</h3>
<dl>
<dt><code>TIOCGSOFTCAR <code>&nbsp;<wbr>&nbsp;</code>int *</code><i>argp</i></dt>
<dd> <p> (&quot;Get software carrier flag&quot;)<br />
 Get the status of the CLOCAL flag in the c_cflag field of the <i>termios</i> structure. </p>
 </dd>
<dt><code>TIOCSSOFTCAR <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>const int *</code><i>argp</i></dt>
<dd> <p> (&quot;Set software carrier flag&quot;)<br />
 Set the CLOCAL flag in the <i>termios</i> structure when *<i>argp</i> is nonzero, and clear it otherwise. </p>
 </dd></dl>
<p>If the <code>CLOCAL</code> flag for a line is off, the hardware carrier detect (DCD) signal is significant, and an <code><a href="/docs/linux/man/2-open/">open</a></code>(2) of the corresponding terminal will block until DCD is asserted, unless the <code>O_NONBLOCK</code> flag is given. If <code>CLOCAL</code> is set, the line behaves as if DCD is always asserted. The software carrier flag is usually turned on for local devices, and is off for lines with modems.  </p>
<h3>Linux-specific</h3>
<p> For the <code>TIOCLINUX</code> ioctl, see <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2).  </p>
<h3>Kernel debugging</h3>
<p> <code>#include &lt;linux/tty.h&gt;</code> </p>
<dl>
<dt><code>TIOCTTYGSTRUCT <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>struct tty_struct *</code><i>argp</i></dt>
<dd> <p> Get the<br />
 <i>tty_struct</i> corresponding to <i>fd</i>. This command was removed in Linux 2.5.67. </p>
 </dd></dl>
<h2>RETURN VALUE</h2>
<p> The <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) system call returns 0 on success. On error, it returns -1 and sets <i>errno</i> appropriately.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> <p> Invalid command parameter. </p>
 </dd>
<dt><code>ENOIOCTLCMD</code></dt>
<dd> <p> Unknown command. </p>
 </dd>
<dt><code>ENOTTY</code></dt>
<dd> <p> Inappropriate <i>fd</i>. </p>
 </dd>
<dt><code>EPERM</code></dt>
<dd> <p> Insufficient permission. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> Check the condition of DTR on the serial port. </p>
<p>#include &lt;termios.h&gt; #include &lt;fcntl.h&gt; #include &lt;sys/ioctl.h&gt; </p>
<p>int main(void) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd, serial; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(&quot;/dev/ttyS0&quot;, O_RDONLY); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ioctl(fd, TIOCMGET,&nbsp;&amp;serial); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(serial&nbsp;&amp;&nbsp;TIOCM_DTR) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts(&quot;TIOCM_DTR is set&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts(&quot;TIOCM_DTR is not set&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); }  </p>
<h2>SEE ALSO</h2>
<p> <code>ldattach</code>(1), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
