---
title: "agetty(8)"
name: "agetty"
section: "8"
letter: "a"
url: "/docs/linux/man/8-agetty/"
description: "agetty – alternative Linux getty"
---

<p>agetty &#8211; alternative Linux getty</p>
<h2>Synopsis</h2>
<p><code>agetty</code> [options] <i>port</i> [<i>baud_rate</i>&#8230;] [<i>term</i>]</p>
<h2>Description</h2>
<p><code>agetty</code> opens a tty port, prompts for a login name and invokes the /bin/login command. It is normally invoked by <code><a href="/docs/linux/man/8-init/">init</a></code>(8). </p>
<p> <code>agetty</code> has several <i>non-standard</i> features that are useful for hardwired and for dial-in lines: </p>
<dl>
<dd>&bull; Adapts the tty settings to parity bits and to erase, kill, end-of-line and uppercase characters when it reads a login name. The program can handle 7-bit characters with even, odd, none or space parity, and 8-bit characters with no parity. The following special characters are recognized: Control-U (kill); DEL and backspace (erase); carriage return and line feed (end of line). See also the <code>&#8211;erase-chars</code> and <code>&#8211;kill-chars</code> options.</dl>
<dl>
<dd>&bull; Optionally deduces the baud rate from the CONNECT messages produced by Hayes(tm)-compatible modems.</dl>
<dl>
<dd>&bull; Optionally does not hang up when it is given an already opened line (useful for call-back applications).</dl>
<dl>
<dd>&bull; Optionally does not display the contents of the <i>/etc/issue</i> file.</dl>
<dl>
<dd>&bull; Optionally displays an alternative issue files or directories instead of <i>/etc/issue</i> or <i>/etc/issue.d</i>.</dl>
<dl>
<dd>&bull; Optionally does not ask for a login name.</dl>
<dl>
<dd>&bull; Optionally invokes a non-standard login program instead of <i>/bin/login</i>.</dl>
<dl>
<dd>&bull; Optionally turns on hardware flow control.</dl>
<dl>
<dd>&bull; Optionally forces the line to be local with no need for carrier detect.</dl>
<p> This program does not use the <i>/etc/gettydefs</i> (System V) or <i>/etc/gettytab</i> (SunOS 4) files.</p>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>A path name relative to the <i>/dev</i> directory. If a &quot;-&quot; is specified, <code>agetty</code> assumes that its standard input is already connected to a tty port and that a connection to a remote user has already been established. </p>
<p> Under System V, a &quot;-&quot; <i>port</i> argument should be preceded by a &quot;&#8211;&quot;.</dl>
<p> <i>baud_rate</i>,&#8230;</p>
<dl>
<dd>A comma-separated list of one or more baud rates. Each time <code>agetty</code> receives a BREAK character it advances through the list, which is treated as if it were circular. </p>
<p> Baud rates should be specified in descending order, so that the null character (Ctrl-@) can also be used for baud-rate switching. </p>
<p> This argument is optional and unnecessary for <code>virtual terminals</code>. </p>
<p> The default for <code>serial terminals</code> is keep the current baud rate (see <code>&#8211;keep-baud</code>) and if unsuccessful then default to &#8216;9600&#8217;.</dl>
<p> <i>term</i></p>
<dl>
<dd>The value to be used for the <code>TERM</code> environment variable. This overrides whatever <code><a href="/docs/linux/man/1-init/">init</a></code>(1) may have set, and is inherited by login and the shell. </p>
<p> The default is &#8216;vt100&#8217;, or &#8216;linux&#8217; for Linux on a virtual terminal, or &#8216;hurd&#8217; for GNU Hurd on a virtual terminal.</dl>
<h2>Options</h2>
<p><code>-8</code>, <code>&#8211;8bits</code></p>
<dl>
<dd>Assume that the tty is 8-bit clean, hence disable parity detection.</dl>
<p> <code>-a</code>, <code>&#8211;autologin</code> <i>username</i></p>
<dl>
<dd>Automatically log in the specified user without asking for a username or password. Using this option causes an <code>-f</code> <i>username</i> option and argument to be added to the <code>/bin/login</code> command line. See <code>&#8211;login-options</code>, which can be used to modify this option&#8217;s behavior. </p>
<p> Note that <code>&#8211;autologin</code> may affect the way in which <code>getty</code> initializes the serial line, because on auto-login <code>agetty</code> does not read from the line and it has no opportunity optimize the line setting.</dl>
<p> <code>-c</code>, <code>&#8211;noreset</code></p>
<dl>
<dd>Do not reset terminal cflags (control modes). See <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) for more details.</dl>
<p> <code>-E</code>, <code>&#8211;remote</code></p>
<dl>
<dd>Typically the <code><a href="/docs/linux/man/1-login/">login</a></code>(1) command is given a remote hostname when called by something such as <code><a href="/docs/linux/man/8-telnetd/">telnetd</a></code>(8). This option allows <code>agetty</code> to pass what it is using for a hostname to <code><a href="/docs/linux/man/1-login/">login</a></code>(1) for use in <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). See <code>&#8211;host</code>, <code><a href="/docs/linux/man/1-login/">login</a></code>(1), and <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). </p>
<p> If the <code>&#8211;host</code> <i>fakehost</i> option is given, then an <code>-h</code> <i>fakehost</i> option and argument are added to the <i>/bin/login</i> command line. </p>
<p> If the <code>&#8211;nohostname</code> option is given, then an <code>-H</code> option is added to the <code>/bin/login</code> command line. </p>
<p> See <code>&#8211;login-options</code>.</dl>
<p> <code>-f</code>, <code>&#8211;issue-file</code> <i>path</i></p>
<dl>
<dd>Specifies a &quot;:&quot; delimited list of files and directories to be displayed instead of <i>/etc/issue</i> (or other). All specified files and directories are displayed, missing or empty files are silently ignored. If the specified path is a directory then display all files with .issue file extension in version-sort order from the directory. This allows custom messages to be displayed on different terminals. The <code>&#8211;noissue</code> option will override this option.</dl>
<p> <code>&#8211;show-issue</code></p>
<dl>
<dd>Display the current issue file (or other) on the current terminal and exit. Use this option to review the current setting, it is not designed for any other purpose. Note that output may use some default or incomplete information as proper output depends on terminal and agetty command line.</dl>
<p> <code>-h, &#8211;flow-control</code></p>
<dl>
<dd>Enable hardware (RTS/CTS) flow control. It is left up to the application to disable software (XON/XOFF) flow protocol where appropriate.</dl>
<p> <code>-H</code>, <code>&#8211;host</code> <i>fakehost</i></p>
<dl>
<dd>Write the specified <i>fakehost</i> into the utmp file. Normally, no login host is given, since <code>agetty</code> is used for local hardwired connections and consoles. However, this option can be useful for identifying terminal concentrators and the like.</dl>
<p> <code>-i</code>, <code>&#8211;noissue</code></p>
<dl>
<dd>Do not display the contents of <i>/etc/issue</i> (or other) before writing the login prompt. Terminals or communications hardware may become confused when receiving lots of text at the wrong baud rate; dial-up scripts may fail if the login prompt is preceded by too much text.</dl>
<p> <code>-I</code>, <code>&#8211;init-string</code> <i>initstring</i></p>
<dl>
<dd>Set an initial string to be sent to the tty or modem before sending anything else. This may be used to initialize a modem. Non-printable characters may be sent by writing their octal code preceded by a backslash (\). For example, to send a linefeed character (ASCII 10, octal 012), write \12.</dl>
<p> <code>-J</code>, <code>&#8211;noclear</code></p>
<dl>
<dd>Do not clear the screen before prompting for the login name. By default the screen is cleared.</dl>
<p> <code>-l</code>, <code>&#8211;login-program</code> <i>login_program</i></p>
<dl>
<dd>Invoke the specified <i>login_program</i> instead of /bin/login. This allows the use of a non-standard login program. Such a program could, for example, ask for a dial-up password or use a different password file. See <code>&#8211;login-options</code>.</dl>
<p> <code>-L</code>, <code>&#8211;local-line</code>[=<i>mode</i>]</p>
<dl>
<dd>Control the CLOCAL line flag. The optional <i>mode</i> argument is &#8216;auto&#8217;, &#8216;always&#8217; or &#8216;never&#8217;. If the <i>mode</i> argument is omitted, then the default is &#8216;always&#8217;. If the <code>&#8211;local-line</code> option is not given at all, then the default is &#8216;auto&#8217;. </p>
<p> <i>always</i></p>
<dl>
<dd>Forces the line to be a local line with no need for carrier detect. This can be useful when you have a locally attached terminal where the serial line does not set the carrier-detect signal.</dl>
<p> <i>never</i></p>
<dl>
<dd>Explicitly clears the CLOCAL flag from the line setting and the carrier-detect signal is expected on the line.</dl>
<p> <i>auto</i></p>
<dl>
<dd>The <code>agetty</code> default. Does not modify the CLOCAL setting and follows the setting enabled by the kernel.</dl>
</dl>
<p> <code>-m</code>, <code>&#8211;extract-baud</code></p>
<dl>
<dd>Try to extract the baud rate from the CONNECT status message produced by Hayes(tm)-compatible modems. These status messages are of the form: &quot;&lt;junk&gt;&lt;speed&gt;&lt;junk&gt;&quot;. <code>agetty</code> assumes that the modem emits its status message at the same speed as specified with (the first) <i>baud_rate</i> value on the command line. </p>
<p> Since the <code>&#8211;extract-baud</code> feature may fail on heavily-loaded systems, you still should enable BREAK processing by enumerating all expected baud rates on the command line.</dl>
<p> <code>&#8211;list-speeds</code></p>
<dl>
<dd>Display supported baud rates. These are determined at compilation time.</dl>
<p> <code>-n</code>, <code>&#8211;skip-login</code></p>
<dl>
<dd>Do not prompt the user for a login name. This can be used in connection with the <code>&#8211;login-program</code> option to invoke a non-standard login process such as a BBS system. Note that with the <code>&#8211;skip-login</code> option, <code>agetty</code> gets no input from the user who logs in and therefore will not be able to figure out parity, character size, and newline processing of the connection. It defaults to space parity, 7 bit characters, and ASCII CR (13) end-of-line character. Beware that the program that <code>agetty</code> starts (usually /bin/login) is run as root.</dl>
<p> <code>-N</code>, <code>&#8211;nonewline</code></p>
<dl>
<dd>Do not print a newline before writing out <i>/etc/issue</i>.</dl>
<p> <code>-o</code>, <code>&#8211;login-options</code> <i>login_options</i></p>
<dl>
<dd>Options and arguments that are passed to <code><a href="/docs/linux/man/1-login/">login</a></code>(1). Where 
