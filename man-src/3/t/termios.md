---
title: "termios(3)"
name: "termios"
section: "3"
letter: "t"
url: "/docs/linux/man/3-termios/"
description: "termios, tcgetattr, tcsetattr, tcsendbreak, tcdrain, tcflush, tcflow, cfmakeraw, cfgetospeed, cfgetispeed, cfsetispeed, cfsetospeed, cfsetspeed – get and set terminal attributes, line control, get ..."
---
<p>termios, tcgetattr, tcsetattr, tcsendbreak, tcdrain, tcflush, tcflow, cfmakeraw, cfgetospeed, cfgetispeed, cfsetispeed, cfsetospeed, cfsetspeed &#8211; get and set terminal attributes, line control, get and set baud rate </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;termios.h&gt; 
 #include &lt;unistd.h&gt; 
 int tcgetattr(int  fd  , struct termios *  termios_p  ); 
 int tcsetattr(int  fd  , int  optional_actions  , 
               const struct termios *  termios_p  ); 
 int tcsendbreak(int  fd  , int  duration  ); 
 int tcdrain(int  fd  ); 
 int tcflush(int  fd  , int  queue_selector  ); 
 int tcflow(int  fd  , int  action  ); 
 void cfmakeraw(struct termios *  termios_p  ); 
 speed_t cfgetispeed(const struct termios *  termios_p  ); 
 speed_t cfgetospeed(const struct termios *  termios_p  ); 
 int cfsetispeed(struct termios *  termios_p  , speed_t  speed  ); 
 int cfsetospeed(struct termios *  termios_p  , speed_t  speed  ); 
 int cfsetspeed(struct termios *  termios_p  , speed_t  speed  ); 
</code></pre>
<p>Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>cfsetspeed</code>(), <code>cfmakeraw</code>(): <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier: <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE  </p>
<h2>DESCRIPTION</h2>
<p> The termios functions describe a general terminal interface that is provided to control asynchronous communications ports.  </p>
<h3>The termios structure</h3>
<p> Many of the functions described here have a <i>termios_p</i> argument that is a pointer to a <i>termios</i> structure. This structure contains at least the following members: </p>
<p>tcflag_t c_iflag; /* input modes */ tcflag_t c_oflag; /* output modes */ tcflag_t c_cflag; /* control modes */ tcflag_t c_lflag; /* local modes */ cc_t c_cc[NCCS]; /* special characters */ </p>
<p>The values that may be assigned to these fields are described below. In the case of the first four bit-mask fields, the definitions of some of the associated flags that may be set are exposed only if a specific feature test macro (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)) is defined, as noted in brackets (&quot;[]&quot;). </p>
<p>In the descriptions below, &quot;not in POSIX&quot; means that the value is not specified in POSIX.1-2001, and &quot;XSI&quot; means that the value is specified in POSIX.1-2001 as part of the XSI extension. </p>
<p> <i>c_iflag</i> flag constants: </p>
<dl>
<dt><code>IGNBRK</code></dt>
<dd> <p> Ignore BREAK condition on input. </p>
 </dd>
<dt><code>BRKINT</code></dt>
<dd> <p> If <code>IGNBRK</code> is set, a BREAK is ignored. If it is not set but <code>BRKINT</code> is set, then a BREAK causes the input and output queues to be flushed, and if the terminal is the controlling terminal of a foreground process group, it will cause a <code>SIGINT</code> to be sent to this foreground process group. When neither <code>IGNBRK</code> nor <code>BRKINT</code> are set, a BREAK reads as a null byte (&#8216;\0&#8217;), except when <code>PARMRK</code> is set, in which case it reads as the sequence \377 \0 \0. </p>
 </dd>
<dt><code>IGNPAR</code></dt>
<dd> <p> Ignore framing errors and parity errors. </p>
 </dd>
<dt><code>PARMRK</code></dt>
<dd> <p> If this bit is set, input bytes with parity or framing errors are marked when passed to the program. This bit is meaningful only when <code>INPCK</code> is set and <code>IGNPAR</code> is not set. The way erroneous bytes are marked is with two preceding bytes, \377 and \0. Thus, the program actually reads three bytes for one erroneous byte received from the terminal. If a valid byte has the value \377, and <code>ISTRIP</code> (see below) is not set, the program might confuse it with the prefix that marks a parity error. Therefore, a valid byte \377 is passed to the program as two bytes, \377 \377, in this case. </p>
 </dd>
<dd> <p> If neither <code>IGNPAR</code> nor <code>PARMRK</code> is set, read a character with a parity error or framing error as \0. </p>
 </dd>
<dt><code>INPCK</code></dt>
<dd> <p> Enable input parity checking. </p>
 </dd>
<dt><code>ISTRIP</code></dt>
<dd> <p> Strip off eighth bit. </p>
 </dd>
<dt><code>INLCR</code></dt>
<dd> <p> Translate NL to CR on input. </p>
 </dd>
<dt><code>IGNCR</code></dt>
<dd> <p> Ignore carriage return on input. </p>
 </dd>
<dt><code>ICRNL</code></dt>
<dd> <p> Translate carriage return to newline on input (unless <code>IGNCR</code> is set). </p>
 </dd>
<dt><code>IUCLC</code></dt>
<dd> <p> (not in POSIX) Map uppercase characters to lowercase on input. </p>
 </dd>
<dt><code>IXON</code></dt>
<dd> <p> Enable XON/XOFF flow control on output. </p>
 </dd>
<dt><code>IXANY</code></dt>
<dd> <p> (XSI) Typing any character will restart stopped output. (The default is to allow just the START character to restart output.) </p>
 </dd>
<dt><code>IXOFF</code></dt>
<dd> <p> Enable XON/XOFF flow control on input. </p>
 </dd>
<dt><code>IMAXBEL</code></dt>
<dd> <p> (not in POSIX) Ring bell when input queue is full. Linux does not implement this bit, and acts as if it is always set. </p>
 </dd>
<dt><code>IUTF8</code> (since Linux 2.6.4) </dt>
<dd> <p> (not in POSIX) Input is UTF8; this allows character-erase to be correctly performed in cooked mode. </p>
 </dd></dl>
<p> <i>c_oflag</i> flag constants: </p>
<dl>
<dt><code>OPOST</code></dt>
<dd> <p> Enable implementation-defined output processing. </p>
 </dd>
<dt><code>OLCUC</code></dt>
<dd> <p> (not in POSIX) Map lowercase characters to uppercase on output. </p>
 </dd>
<dt><code>ONLCR</code></dt>
<dd> <p> (XSI) Map NL to CR-NL on output. </p>
 </dd>
<dt><code>OCRNL</code></dt>
<dd> <p> Map CR to NL on output. </p>
 </dd>
<dt><code>ONOCR</code></dt>
<dd> <p> Don&#8217;t output CR at column 0. </p>
 </dd>
<dt><code>ONLRET</code></dt>
<dd> <p> Don&#8217;t output CR. </p>
 </dd>
<dt><code>OFILL</code></dt>
<dd> <p> Send fill characters for a delay, rather than using a timed delay. </p>
 </dd>
<dt><code>OFDEL</code></dt>
<dd> <p> Fill character is ASCII DEL (0177). If unset, fill character is ASCII NUL (&#8216;\0&#8217;). (Not implemented on Linux.) </p>
 </dd>
<dt><code>NLDLY</code></dt>
<dd> <p> Newline delay mask. Values are <code>NL0</code> and <code>NL1</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd>
<dt><code>CRDLY</code></dt>
<dd> <p> Carriage return delay mask. Values are <code>CR0</code>, <code>CR1</code>, <code>CR2</code>, or <code>CR3</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd>
<dt><code>TABDLY</code></dt>
<dd> <p> Horizontal tab delay mask. Values are <code>TAB0</code>, <code>TAB1</code>, <code>TAB2</code>, <code>TAB3</code> (or <code>XTABS</code>, but see the <code>BUGS</code> section). A value of TAB3, that is, XTABS, expands tabs to spaces (with tab stops every eight columns). [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd>
<dt><code>BSDLY</code></dt>
<dd> <p> Backspace delay mask. Values are <code>BS0</code> or <code>BS1</code>. (Has never been implemented.) [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd>
<dt><code>VTDLY</code></dt>
<dd> <p> Vertical tab delay mask. Values are <code>VT0</code> or <code>VT1</code>. </p>
 </dd>
<dt><code>FFDLY</code></dt>
<dd> <p> Form feed delay mask. Values are <code>FF0</code> or <code>FF1</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd></dl>
<p> <i>c_cflag</i> flag constants: </p>
<dl>
<dt><code>CBAUD</code></dt>
<dd> <p> (not in POSIX) Baud speed mask (4+1 bits). [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>CBAUDEX</code></dt>
<dd> <p> (not in POSIX) Extra baud speed mask (1 bit), included in <code>CBAUD</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dd> <p> (POSIX says that the baud speed is stored in the <i>termios</i> structure without specifying where precisely, and provides <code>cfgetispeed</code>() and <code>cfsetispeed</code>() for getting at it. Some systems use bits selected by <code>CBAUD</code> in <i>c_cflag</i>, other systems use separate fields, for example, <i>sg_ispeed</i> and <i>sg_ospeed</i>.) </p>
 </dd>
<dt><code>CSIZE</code></dt>
<dd> <p> Character size mask. Values are <code>CS5</code>, <code>CS6</code>, <code>CS7</code>, or <code>CS8</code>. </p>
 </dd>
<dt><code>CSTOPB</code></dt>
<dd> <p> Set two stop bits, rather than one. </p>
 </dd>
<dt><code>CREAD</code></dt>
<dd> <p> Enable receiver. </p>
 </dd>
<dt><code>PARENB</code></dt>
<dd> <p> Enable parity generation on output and parity checking for input. </p>
 </dd>
<dt><code>PARODD</code></dt>
<dd> <p> If set, then parity for input and output is odd; otherwise even parity is used. </p>
 </dd>
<dt><code>HUPCL</code></dt>
<dd> <p> Lower modem control lines after last process closes the device (hang up). </p>
 </dd>
<dt><code>CLOCAL</code></dt>
<dd> <p> Ignore modem control lines. </p>
 </dd>
<dt><code>LOBLK</code></dt>
<dd> <p> (not in POSIX) Block output from a noncurrent shell layer. For use by <code>shl</code> (shell layers). (Not implemented on Linux.) </p>
 </dd>
<dt><code>CIBAUD</code></dt>
<dd> <p> (not in POSIX) Mask for input speeds. The values for the <code>CIBAUD</code> bits are the same as the values for the <code>CBAUD</code> bits, shifted left <code>IBSHIFT</code> bits. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] (Not implemented on Linux.) </p>
 </dd>
<dt><code>CMSPAR</code></dt>
<dd> <p> (not in POSIX) Use &quot;stick&quot; (mark/space) parity (supported on certain serial devices): if <code>PARODD</code> is set, the parity bit is always 1; if <code>PARODD</code> is not set, then the parity bit is always 0. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>CRTSCTS</code></dt>
<dd> <p> (not in POSIX) Enable RTS/CTS (hardware) flow control. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd></dl>
<p> <i>c_lflag</i> flag constants: </p>
<dl>
<dt><code>ISIG</code></dt>
<dd> <p> When any of the characters INTR, QUIT, SUSP, or DSUSP are received, generate the corresponding signal. </p>
 </dd>
<dt><code>ICANON</code></dt>
<dd> <p> Enable canonical mode (described below). </p>
 </dd>
<dt><code>XCASE</code></dt>
<dd> <p> (not in POSIX; not supported under Linux) If <code>ICANON</code> is also set, terminal is uppercase only. Input is converted to lowercase, except for characters preceded by \. On output, uppercase characters are preceded by \ and lowercase characters are converted to uppercase. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> or <code>_XOPEN_SOURCE</code>] </p>
 </dd>
<dt><code>ECHO</code></dt>
<dd> <p> Echo input characters. </p>
 </dd>
<dt><code>ECHOE</code></dt>
<dd> <p> If <code>ICANON</code> is also set, the ERASE character erases the preceding input character, and WERASE erases the preceding word. </p>
 </dd>
<dt><code>ECHOK</code></dt>
<dd> <p> If <code>ICANON</code> is also set, the KILL character erases the current line. </p>
 </dd>
<dt><code>ECHONL</code></dt>
<dd> <p> If <code>ICANON</code> is also set, echo the NL character even if ECHO is not set. </p>
 </dd>
<dt><code>ECHOCTL</code></dt>
<dd> <p> (not in POSIX) If <code>ECHO</code> is also set, terminal special characters other than TAB, NL, START, and STOP are echoed as <code>haX</code>, where X is the character with ASCII code 0x40 greater than the special character. For example, character 0x08 (BS) is echoed as <code>haH</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>ECHOPRT</code></dt>
<dd> <p> (not in POSIX) If <code>ICANON</code> and <code>ECHO</code> are also set, characters are printed as they are being erased. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>ECHOKE</code></dt>
<dd> <p> (not in POSIX) If <code>ICANON</code> is also set, KILL is echoed by erasing each character on the line, as specified by <code>ECHOE</code> and <code>ECHOPRT</code>. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>DEFECHO</code></dt>
<dd> <p> (not in POSIX) Echo only when a process is reading. (Not implemented on Linux.) </p>
 </dd>
<dt><code>FLUSHO</code></dt>
<dd> <p> (not in POSIX; not supported under Linux) Output is being flushed. This flag is toggled by typing the DISCARD character. [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>NOFLSH</code></dt>
<dd> <p> Disable flushing the input and output queues when generating signals for the INT, QUIT, and SUSP characters. </p>
 </dd>
<dt><code>TOSTOP</code></dt>
<dd> <p> Send the <code>SIGTTOU</code> signal to the process group of a background process which tries to write to its controlling terminal. </p>
 </dd>
<dt><code>PENDIN</code></dt>
<dd> <p> (not in POSIX; not supported under Linux) All characters in the input queue are reprinted when the next character is read. (<code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) handles typeahead this way.) [requires <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code>] </p>
 </dd>
<dt><code>IEXTEN</code></dt>
<dd> <p> Enable implementation-defined input processing. This flag, as well as <code>ICANON</code> must be enabled for the special characters EOL2, LNEXT, REPRINT, WERASE to be interpreted, and for the <code>IUCLC</code> flag to be effective. </p>
 </dd></dl>
<p>The <i>c_cc</i> array defines the terminal special characters. The symbolic indices (initial values) and meaning are: </p>
<dl>
<dt><code>VDISCARD</code></dt>
<dd> <p> (not in POSIX; not supported under Linux; 017, SI, Ctrl-O) Toggle: start/stop discarding pending output. Recognized when <code>IEXTEN</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VDSUSP</code></dt>
<dd> <p> (not in POSIX; not supported under Linux; 031, EM, Ctrl-Y) Delayed suspend character (DSUSP): send <code>SIGTSTP</code> signal when the character is read by the user program. Recognized when <code>IEXTEN</code> and <code>ISIG</code> are set, and the system supports job control, and then not passed as input. </p>
 </dd>
<dt><code>VEOF</code></dt>
<dd> <p> (004, EOT, Ctrl-D) End-of-file character (EOF). More precisely: this character causes the pending tty buffer to be sent to the waiting user program without waiting for end-of-line. If it is the first character of the line, the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) in the user program returns 0, which signifies end-of-file. Recognized when <code>ICANON</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VEOL</code></dt>
<dd> <p> (0, NUL) Additional end-of-line character (EOL). Recognized when <code>ICANON</code> is set. </p>
 </dd>
<dt><code>VEOL2</code></dt>
<dd> <p> (not in POSIX; 0, NUL) Yet another end-of-line character (EOL2). Recognized when <code>ICANON</code> is set. </p>
 </dd>
<dt><code>VERASE</code></dt>
<dd> <p> (0177, DEL, rubout, or 010, BS, Ctrl-H, or also #) Erase character (ERASE). This erases the previous not-yet-erased character, but does not erase past EOF or beginning-of-line. Recognized when <code>ICANON</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VINTR</code></dt>
<dd> <p> (003, ETX, Ctrl-C, or also 0177, DEL, rubout) Interrupt character (INTR). Send a <code>SIGINT</code> signal. Recognized when <code>ISIG</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VKILL</code></dt>
<dd> <p> (025, NAK, Ctrl-U, or Ctrl-X, or also @) Kill character (KILL). This erases the input since the last EOF or beginning-of-line. Recognized when <code>ICANON</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VLNEXT</code></dt>
<dd> <p> (not in POSIX; 026, SYN, Ctrl-V) Literal next (LNEXT). Quotes the next input character, depriving it of a possible special meaning. Recognized when <code>IEXTEN</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VMIN</code></dt>
<dd> <p> Minimum number of characters for noncanonical read (MIN). </p>
 </dd>
<dt><code>VQUIT</code></dt>
<dd> <p> (034, FS, Ctrl-\) Quit character (QUIT). Send <code>SIGQUIT</code> signal. Recognized when <code>ISIG</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VREPRINT</code></dt>
<dd> <p> (not in POSIX; 022, DC2, Ctrl-R) Reprint unread characters (REPRINT). Recognized when <code>ICANON</code> and <code>IEXTEN</code> are set, and then not passed as input. </p>
 </dd>
<dt><code>VSTART</code></dt>
<dd> <p> (021, DC1, Ctrl-Q) Start character (START). Restarts output stopped by the Stop character. Recognized when <code>IXON</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VSTATUS</code></dt>
<dd> <p> (not in POSIX; not supported under Linux; status request: 024, DC4, Ctrl-T). Status character (STATUS). Display status information at terminal, including state of foreground process and amount of CPU time it has consumed. Also sends a <code>SIGINFO</code> signal (not supported on Linux) to the foreground process group. </p>
 </dd>
<dt><code>VSTOP</code></dt>
<dd> <p> (023, DC3, Ctrl-S) Stop character (STOP). Stop output until Start character typed. Recognized when <code>IXON</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VSUSP</code></dt>
<dd> <p> (032, SUB, Ctrl-Z) Suspend character (SUSP). Send <code>SIGTSTP</code> signal. Recognized when <code>ISIG</code> is set, and then not passed as input. </p>
 </dd>
<dt><code>VSWTCH</code></dt>
<dd> <p> (not in POSIX; not supported under Linux; 0, NUL) Switch character (SWTCH). Used in System V to switch shells in <i>shell layers</i>, a predecessor to shell job control. </p>
 </dd>
<dt><code>VTIME</code></dt>
<dd> <p> Timeout in deciseconds for noncanonical read (TIME). </p>
 </dd>
<dt><code>VWERASE</code></dt>
<dd> <p> (not in POSIX; 027, ETB, Ctrl-W) Word erase (WERASE). Recognized when <code>ICANON</code> and <code>IEXTEN</code> are set, and then not passed as input. </p>
 </dd></dl>
<p>An individual terminal special character can be disabled by setting the value of the corresponding <i>c_cc</i> element to <code>_POSIX_VDISABLE</code>. </p>
<p>The above symbolic subscript values are all different, except that <code>VTIME</code>, <code>VMIN</code> may have the same value as <code>VEOL</code>, <code>VEOF</code>, respectively. In noncanonical mode the special character meaning is replaced by the timeout meaning. For an explanation of <code>VMIN</code> and <code>VTIME</code>, see the description of noncanonical mode below.  </p>
<h3>Retrieving and changing terminal settings</h3>
<p> <code>tcgetattr</code>() gets the parameters associated with the object referred by <i>fd</i> and stores them in the <i>termios</i> structure referenced by <i>termios_p</i>. This function may be invoked from a background process; however, the terminal attributes may be subsequently changed by a foreground process. </p>
<p> <code>tcsetattr</code>() sets the parameters associated with the terminal (unless support is required from the underlying hardware that is not available) from the <i>termios</i> structure referred to by <i>termios_p</i>. <i>optional_actions</i> specifies when the changes take effect: </p>
<dl>
<dt><code>TCSANOW</code></dt>
<dd> <p> the change occurs immediately. </p>
 </dd>
<dt><code>TCSADRAIN</code></dt>
<dd> <p> the change occurs after all output written to <i>fd</i> has been transmitted. This option should be used when changing parameters that affect output. </p>
 </dd>
<dt><code>TCSAFLUSH</code></dt>
<dd> <p> the change occurs after all output written to the object referred by <i>fd</i> has been transmitted, and all input that has been received but not read will be discarded before the change is made. </p>
 </dd></dl>
<h3>Canonical and noncanonical mode</h3>
<p> The setting of the <code>ICANON</code> canon flag in <i>c_lflag</i> determines whether the terminal is operating in canonical mode (<code>ICANON</code> set) or noncanonical mode (<code>ICANON</code> unset). By default, <code>ICANON</code> is set. </p>
<p>In canonical mode: </p>
<dl>
<dt>*</dt>
<dd> <p> Input is made available line by line. An input line is available when one of the line delimiters is typed (NL, EOL, EOL2; or EOF at the start of line). Except in the case of EOF, the line delimiter is included in the buffer returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2). </p>
 </dd>
<dt>*</dt>
<dd> <p> Line editing is enabled (ERASE, KILL; and if the <code>IEXTEN</code> flag is set: WERASE, REPRINT, LNEXT). A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns at most one line of input; if the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) requested fewer bytes than are available in the current line of input, then only as many bytes as requested are read, and the remaining characters will be available for a future <code><a href="/docs/linux/man/2-read/">read</a></code>(2). </p>
 </dd>
<dt>*</dt>
<dd> <p> The maximum line length is 4096 chars (including the terminating newline character); lines longer than 4096 chars are truncated. After 4095 characters, input processing (e.g., <code>ISIG</code> and <code>ECHO*</code> processing) continues, but any input data after 4095 characters up to (but not including) any terminating newline is discarded. This ensures that the terminal can always receive more input until at least one line can be read. </p>
 </dd></dl>
<p>In noncanonical mode input is available immediately (without the user having to type a line-delimiter character), no input processing is performed, and line editing is disabled. The read buffer will only accept 4095 chars; this provides the necessary space for a newline char if the input mode is switched to canonical. The settings of MIN (<i>c_cc[VMIN]</i>) and TIME (<i>c_cc[VTIME]</i>) determine the circumstances in which a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) completes; there are four distinct cases: </p>
<dl>
<dt>MIN == 0, TIME == 0 (polling read)</dt>
<dd> <p> If data is available, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns immediately, with the lesser of the number of bytes available, or the number of bytes requested. If no data is available, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0. </p>
 </dd>
<dt>MIN &gt; 0, TIME == 0 (blocking read)</dt>
<dd> <p> <code><a href="/docs/linux/man/2-read/">read</a></code>(2) blocks until MIN bytes are available, and returns up to the number of bytes requested. </p>
 </dd>
<dt>MIN == 0, TIME &gt; 0 (read with timeout)</dt>
<dd> <p> TIME specifies the limit for a timer in tenths of a second. The timer is started when <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is called. <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns either when at least one byte of data is available, or when the timer expires. If the timer expires without any input becoming available, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0. If data is already available at the time of the call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2), the call behaves as though the data was received immediately after the call. </p>
 </dd>
<dt>MIN &gt; 0, TIME &gt; 0 (read with interbyte timeout)</dt>
<dd> <p> TIME specifies the limit for a timer in tenths of a second. Once an initial byte of input becomes available, the timer is restarted after each further byte is received. <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns when any of the following conditions is met: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>*</dt>
<dd> <p> MIN bytes have been received. </p>
 </dd>
<dt>*</dt>
<dd> <p> The interbyte timer expires. </p>
 </dd>
<dt>*</dt>
<dd> <p> The number of bytes requested by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) has been received. (POSIX does not specify this termination condition, and on some other implementations <code><a href="/docs/linux/man/2-read/">read</a></code>(2) does not return in this case.) </p>
 </dd></dl>
</dl>
<dd> <p> Because the timer is started only after the initial byte becomes available, at least one byte will be read. If data is already available at the time of the call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2), the call behaves as though the data was received immediately after the call. </p>
 </dd></dl>
<p>POSIX does not specify whether the setting of the <code>O_NONBLOCK</code> file status flag takes precedence over the MIN and TIME settings. If <code>O_NONBLOCK</code> is set, a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) in noncanonical mode may return immediately, regardless of the setting of MIN or TIME. Furthermore, if no data is available, POSIX permits a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) in noncanonical mode to return either 0, or -1 with <i>errno</i> set to <code>EAGAIN</code>.  </p>
<h3>Raw mode</h3>
<p> <code>cfmakeraw</code>() sets the terminal to something like the &quot;raw&quot; mode of the old Version 7 terminal driver: input is available character by character, echoing is disabled, and all special processing of terminal input and output characters is disabled. The terminal attributes are set as follows: </p>
<p>termios_p-&gt;c_iflag &amp;= ~(IGNBRK | BRKINT | PARMRK | ISTRIP <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;| INLCR | IGNCR | ICRNL | IXON); termios_p-&gt;c_oflag &amp;= ~OPOST; termios_p-&gt;c_lflag &amp;= ~(ECHO | ECHONL | ICANON | ISIG | IEXTEN); termios_p-&gt;c_cflag &amp;= ~(CSIZE | PARENB); termios_p-&gt;c_cflag |= CS8;  </p>
<h3>Line control</h3>
<p> <code>tcsendbreak</code>() transmits a continuous stream of zero-valued bits for a specific duration, if the terminal is using asynchronous serial data transmission. If <i>duration</i> is zero, it transmits zero-valued bits for at least 0.25 seconds, and not more than 0.5 seconds. If <i>duration</i> is not zero, it sends zero-valued bits for some implementation-defined length of time. </p>
<p>If the terminal is not using asynchronous serial data transmission, <code>tcsendbreak</code>() returns without taking any action. </p>
<p> <code>tcdrain</code>() waits until all output written to the object referred to by <i>fd</i> has been transmitted. </p>
<p> <code>tcflush</code>() discards data written to the object referred to by <i>fd</i> but not transmitted, or data received but not read, depending on the value of <i>queue_selector</i>: </p>
<dl>
<dt><code>TCIFLUSH</code></dt>
<dd> <p> flushes data received but not read. </p>
 </dd>
<dt><code>TCOFLUSH</code></dt>
<dd> <p> flushes data written but not transmitted. </p>
 </dd>
<dt><code>TCIOFLUSH</code></dt>
<dd> <p> flushes both data received but not read, and data written but not transmitted. </p>
 </dd></dl>
<p> <code>tcflow</code>() suspends transmission or reception of data on the object referred to by <i>fd</i>, depending on the value of <i>action</i>: </p>
<dl>
<dt><code>TCOOFF</code></dt>
<dd> <p> suspends output. </p>
 </dd>
<dt><code>TCOON</code></dt>
<dd> <p> restarts suspended output. </p>
 </dd>
<dt><code>TCIOFF</code></dt>
<dd> <p> transmits a STOP character, which stops the terminal device from transmitting data to the system. </p>
 </dd>
<dt><code>TCION</code></dt>
<dd> <p> transmits a START character, which starts the terminal device transmitting data to the system. </p>
 </dd></dl>
<p>The default on open of a terminal file is that neither its input nor its output is suspended.  </p>
<h3>Line speed</h3>
<p> The baud rate functions are provided for getting and setting the values of the input and output baud rates in the <i>termios</i> structure. The new values do not take effect until <code>tcsetattr</code>() is successfully called. </p>
<p>Setting the speed to <code>B0</code> instructs the modem to &quot;hang up&quot;. The actual bit rate corresponding to <code>B38400</code> may be altered with <code><a href="/docs/linux/man/8-setserial/">setserial</a></code>(8). </p>
<p>The input and output baud rates are stored in the <i>termios</i> structure. </p>
<p> <code>cfgetospeed</code>() returns the output baud rate stored in the <i>termios</i> structure pointed to by <i>termios_p</i>. </p>
<p> <code>cfsetospeed</code>() sets the output baud rate stored in the <i>termios</i> structure pointed to by <i>termios_p</i> to <i>speed</i>, which must be one of these constants: </p>
<pre><code>
         B0
        B50
        B75
        B110
        B134
        B150
        B200
        B300
        B600
        B1200
        B1800
        B2400
        B4800
        B9600
        B19200
        B38400
        B57600
        B115200
        B230400
 </code></pre>
<p>The zero baud rate, <code>B0</code>, is used to terminate the connection. If B0 is specified, the modem control lines shall no longer be asserted. Normally, this will disconnect the line. <code>CBAUDEX</code> is a mask for the speeds beyond those defined in POSIX.1 (57600 and above). Thus, <code>B57600</code> &amp; <code>CBAUDEX</code> is nonzero. </p>
<p> <code>cfgetispeed</code>() returns the input baud rate stored in the <i>termios</i> structure. </p>
<p> <code>cfsetispeed</code>() sets the input baud rate stored in the <i>termios</i> structure to <i>speed</i>, which must be specified as one of the <code>Bnnn</code> constants listed above for <code>cfsetospeed</code>(). If the input baud rate is set to zero, the input baud rate will be equal to the output baud rate. </p>
<p> <code>cfsetspeed</code>() is a 4.4BSD extension. It takes the same arguments as <code>cfsetispeed</code>(), and sets both input and output speed.  </p>
<h2>RETURN VALUE</h2>
<p> <code>cfgetispeed</code>() returns the input baud rate stored in the <i>termios</i> structure. </p>
<p> <code>cfgetospeed</code>() returns the output baud rate stored in the <i>termios</i> structure. </p>
<p>All other functions return: </p>
<dl>
<dt>0</dt>
<dd> <p> on success. </p>
 </dd>
<dt>-1</dt>
<dd> <p> on failure and set <i>errno</i> to indicate the error. </p>
 </dd></dl>
<p>Note that <code>tcsetattr</code>() returns success if <i>any</i> of the requested changes could be successfully carried out. Therefore, when making multiple changes it may be necessary to follow this call with a further call to <code>tcgetattr</code>() to check that all changes have been performed successfully.  </p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>tcgetattr</code>(), <code>tcsetattr</code>(), <code>tcdrain</code>(), <code>tcflush</code>(), <code>tcflow</code>(), <code>tcsendbreak</code>(), <code>cfmakeraw</code>(), <code>cfgetispeed</code>(), <code>cfgetospeed</code>(), <code>cfsetispeed</code>(), <code>cfsetospeed</code>(), <code>cfsetspeed</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>tcgetattr</code>(), <code>tcsetattr</code>(), <code>tcsendbreak</code>(), <code>tcdrain</code>(), <code>tcflush</code>(), <code>tcflow</code>(), <code>cfgetispeed</code>(), <code>cfgetospeed</code>(), <code>cfsetispeed</code>(), and <code>cfsetospeed</code>() are specified in POSIX.1-2001. </p>
<p> <code>cfmakeraw</code>() and <code>cfsetspeed</code>() are nonstandard, but available on the BSDs.  </p>
<h2>NOTES</h2>
<p> UNIX V7 and several later systems have a list of baud rates where after the fourteen values B0, ..., B9600 one finds the two constants EXTA, EXTB (&quot;External A&quot; and &quot;External B&quot;). Many systems extend the list with much higher baud rates. </p>
<p>The effect of a nonzero <i>duration</i> with <code>tcsendbreak</code>() varies. SunOS specifies a break of <i>duration&nbsp;*&nbsp;N</i> seconds, where <i>N</i> is at least 0.25, and not more than 0.5. Linux, AIX, DU, Tru64 send a break of <i>duration</i> milliseconds. FreeBSD and NetBSD and HP-UX and MacOS ignore the value of <i>duration</i>. Under Solaris and UnixWare, <code>tcsendbreak</code>() with nonzero <i>duration</i> behaves like <code>tcdrain</code>().  </p>
<h2>BUGS</h2>
<p> On the Alpha architecture before Linux 4.16 (and glibc before 2.28), the <code>XTABS</code> value was different from <code>TAB3</code> and it was ignored by the <code>N_TTY</code> line discipline code of the terminal driver as a result (because as it wasn&#8217;t part of the <code>TABDLY</code> mask).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reset/">reset</a></code>(1), <code><a href="/docs/linux/man/1-setterm/">setterm</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/1-tput/">tput</a></code>(1), <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1), <code><a href="/docs/linux/man/1-tty/">tty</a></code>(1), <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/8-setserial/">setserial</a></code>(8)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAE">The termios structure</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Retrieving and changing terminal settings</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Canonical and noncanonical mode</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Raw mode</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">Line control</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">Line speed</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAK">RETURN VALUE</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">ATTRIBUTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">CONFORMING TO</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">NOTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">COLOPHON</a></dt>
<dd>  </dd></dl>
