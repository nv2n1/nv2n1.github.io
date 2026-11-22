---

title: "getty(8)"
name: "getty"
section: "8"
letter: "g"
url: "/docs/linux/man/8-getty/"
description: "agetty – alternative Linux getty"
---

<p>agetty &#8211; alternative Linux getty </p>

<p> <code>agetty</code> [options] <i>port</i> [<i>baud_rate</i>...] [<i>term</i>]  </p>
<h2>DESCRIPTION</h2>
<p> <code>agetty</code> opens a tty port, prompts for a login name and invokes the /bin/login command. It is normally invoked by <code><a href="/docs/linux/man/8-init/">init</a></code>(8). </p>
<p> <code>agetty</code> has several <i>non-standard</i> features that are useful for hardwired and for dial-in lines: </p>
<dl>
<dd> <p> &bull; Adapts the tty settings to parity bits and to erase, kill, end-of-line and uppercase characters when it reads a login name. The program can handle 7-bit characters with even, odd, none or space parity, and 8-bit characters with no parity. The following special characters are recognized: Control-U (kill); DEL and backspace (erase); carriage return and line feed (end of line). See also the <code>--erase-chars</code> and <code>--kill-chars</code> options. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally deduces the baud rate from the CONNECT messages produced by Hayes(tm)-compatible modems. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally does not hang up when it is given an already opened line (useful for call-back applications). </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally does not display the contents of the <i>/etc/issue</i> file. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally displays an alternative issue files or directories instead of <i>/etc/issue</i> or <i>/etc/issue.d</i>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally does not ask for a login name. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally invokes a non-standard login program instead of <i>/bin/login</i>. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally turns on hardware flow control. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; Optionally forces the line to be local with no need for carrier detect. </p>
 </dd></dl>
<p>This program does not use the <i>/etc/gettydefs</i> (System V) or <i>/etc/gettytab</i> (SunOS 4) files.  </p>
<h2>ARGUMENTS</h2>
<p> <i>port</i> </p>
<dl>
<dd> <p> A path name relative to the <i>/dev</i> directory. If a &quot;-&quot; is specified, <code>agetty</code> assumes that its standard input is already connected to a tty port and that a connection to a remote user has already been established. </p>
<p>Under System V, a &quot;-&quot; <i>port</i> argument should be preceded by a &quot;--&quot;. </p>
 </dd></dl>
<p> <i>baud_rate</i>,... </p>
<dl>
<dd> <p> A comma-separated list of one or more baud rates. Each time <code>agetty</code> receives a BREAK character it advances through the list, which is treated as if it were circular. </p>
<p>Baud rates should be specified in descending order, so that the null character (Ctrl-@) can also be used for baud-rate switching. </p>
<p>This argument is optional and unnecessary for <code>virtual terminals</code>. </p>
<p>The default for <code>serial terminals</code> is keep the current baud rate (see <code>--keep-baud</code>) and if unsuccessful then default to &#8216;9600&#8217;. </p>
 </dd></dl>
<p> <i>term</i> </p>
<dl>
<dd> <p> The value to be used for the <code>TERM</code> environment variable. This overrides whatever <code><a href="/docs/linux/man/1-init/">init</a></code>(1) may have set, and is inherited by login and the shell. </p>
<p>The default is &#8216;vt100&#8217;, or &#8216;linux&#8217; for Linux on a virtual terminal, or &#8216;hurd&#8217; for GNU Hurd on a virtual terminal. </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> <code>-8</code>, <code>--8bits</code> </p>
<dl>
<dd> <p> Assume that the tty is 8-bit clean, hence disable parity detection. </p>
 </dd></dl>
<p> <code>-a</code>, <code>--autologin</code> <i>username</i> </p>
<dl>
<dd> <p> Automatically log in the specified user without asking for a username or password. Using this option causes an <code>-f</code> <i>username</i> option and argument to be added to the <code>/bin/login</code> command line. See <code>--login-options</code>, which can be used to modify this option&#8217;s behavior. </p>
<p>Note that <code>--autologin</code> may affect the way in which <code>getty</code> initializes the serial line, because on auto-login <code>agetty</code> does not read from the line and it has no opportunity optimize the line setting. </p>
 </dd></dl>
<p> <code>-c</code>, <code>--noreset</code> </p>
<dl>
<dd> <p> Do not reset terminal cflags (control modes). See <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) for more details. </p>
 </dd></dl>
<p> <code>-E</code>, <code>--remote</code> </p>
<dl>
<dd> <p> Typically the <code><a href="/docs/linux/man/1-login/">login</a></code>(1) command is given a remote hostname when called by something such as <code>telnetd</code>(8). This option allows <code>agetty</code> to pass what it is using for a hostname to <code><a href="/docs/linux/man/1-login/">login</a></code>(1) for use in <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). See <code>--host</code>, <code><a href="/docs/linux/man/1-login/">login</a></code>(1), and <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5). </p>
<p>If the <code>--host</code> <i>fakehost</i> option is given, then an <code>-h</code> <i>fakehost</i> option and argument are added to the <i>/bin/login</i> command line. </p>
<p>If the <code>--nohostname</code> option is given, then an <code>-H</code> option is added to the <code>/bin/login</code> command line. </p>
<p>See <code>--login-options</code>. </p>
 </dd></dl>
<p> <code>-f</code>, <code>--issue-file</code> <i>path</i> </p>
<dl>
<dd> <p> Specifies a &quot;:&quot; delimited list of files and directories to be displayed instead of <i>/etc/issue</i> (or other). All specified files and directories are displayed, missing or empty files are silently ignored. If the specified path is a directory then display all files with .issue file extension in version-sort order from the directory. This allows custom messages to be displayed on different terminals. The <code>--noissue</code> option will override this option. </p>
 </dd></dl>
<p> <code>--show-issue</code> </p>
<dl>
<dd> <p> Display the current issue file (or other) on the current terminal and exit. Use this option to review the current setting, it is not designed for any other purpose. Note that output may use some default or incomplete information as proper output depends on terminal and agetty command line. </p>
 </dd></dl>
<p> <code>-h, --flow-control</code> </p>
<dl>
<dd> <p> Enable hardware (RTS/CTS) flow control. It is left up to the application to disable software (XON/XOFF) flow protocol where appropriate. </p>
 </dd></dl>
<p> <code>-H</code>, <code>--host</code> <i>fakehost</i> </p>
<dl>
<dd> <p> Write the specified <i>fakehost</i> into the utmp file. Normally, no login host is given, since <code>agetty</code> is used for local hardwired connections and consoles. However, this option can be useful for identifying terminal concentrators and the like. </p>
 </dd></dl>
<p> <code>-i</code>, <code>--noissue</code> </p>
<dl>
<dd> <p> Do not display the contents of <i>/etc/issue</i> (or other) before writing the login prompt. Terminals or communications hardware may become confused when receiving lots of text at the wrong baud rate; dial-up scripts may fail if the login prompt is preceded by too much text. </p>
 </dd></dl>
<p> <code>-I</code>, <code>--init-string</code> <i>initstring</i> </p>
<dl>
<dd> <p> Set an initial string to be sent to the tty or modem before sending anything else. This may be used to initialize a modem. Non-printable characters may be sent by writing their octal code preceded by a backslash (\). For example, to send a linefeed character (ASCII 10, octal 012), write \12. </p>
 </dd></dl>
<p> <code>-J</code>, <code>--noclear</code> </p>
<dl>
<dd> <p> Do not clear the screen before prompting for the login name. By default the screen is cleared. </p>
 </dd></dl>
<p> <code>-l</code>, <code>--login-program</code> <i>login_program</i> </p>
<dl>
<dd> <p> Invoke the specified <i>login_program</i> instead of /bin/login. This allows the use of a non-standard login program. Such a program could, for example, ask for a dial-up password or use a different password file. See <code>--login-options</code>. </p>
 </dd></dl>
<p> <code>-L</code>, <code>--local-line</code>[=<i>mode</i>] </p>
<dl>
<dd> <p> Control the CLOCAL line flag. The optional <i>mode</i> argument is &#8216;auto&#8217;, &#8216;always&#8217; or &#8216;never&#8217;. If the <i>mode</i> argument is omitted, then the default is &#8216;always&#8217;. If the <code>--local-line</code> option is not given at all, then the default is &#8216;auto&#8217;. </p>
<p> <i>always</i> </p>
 </dd>
<dl>
<dd> <p> Forces the line to be a local line with no need for carrier detect. This can be useful when you have a locally attached terminal where the serial line does not set the carrier-detect signal. </p>
 </dd></dl>
<p> <i>never</i> </p>
<dl>
<dd> <p> Explicitly clears the CLOCAL flag from the line setting and the carrier-detect signal is expected on the line. </p>
 </dd></dl>
<p> <i>auto</i> </p>
<dl>
<dd> <p> The <code>agetty</code> default. Does not modify the CLOCAL setting and follows the setting enabled by the kernel. </p>
 </dd></dl>
</dl>
<p> <code>-m</code>, <code>--extract-baud</code> </p>
<dl>
<dd> <p> Try to extract the baud rate from the CONNECT status message produced by Hayes(tm)-compatible modems. These status messages are of the form: &quot;&lt;junk&gt;&lt;speed&gt;&lt;junk&gt;&quot;. <code>agetty</code> assumes that the modem emits its status message at the same speed as specified with (the first) <i>baud_rate</i> value on the command line. </p>
<p>Since the <code>--extract-baud</code> feature may fail on heavily-loaded systems, you still should enable BREAK processing by enumerating all expected baud rates on the command line. </p>
 </dd></dl>
<p> <code>--list-speeds</code> </p>
<dl>
<dd> <p> Display supported baud rates. These are determined at compilation time. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--skip-login</code> </p>
<dl>
<dd> <p> Do not prompt the user for a login name. This can be used in connection with the <code>--login-program</code> option to invoke a non-standard login process such as a BBS system. Note that with the <code>--skip-login</code> option, <code>agetty</code> gets no input from the user who logs in and therefore will not be able to figure out parity, character size, and newline processing of the connection. It defaults to space parity, 7 bit characters, and ASCII CR (13) end-of-line character. Beware that the program that <code>agetty</code> starts (usually /bin/login) is run as root. </p>
 </dd></dl>
<p> <code>-N</code>, <code>--nonewline</code> </p>
<dl>
<dd> <p> Do not print a newline before writing out <i>/etc/issue</i>. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--login-options</code> <i>login_options</i> </p>
<dl>
<dd> <p> Options and arguments that are passed to <code><a href="/docs/linux/man/1-login/">login</a></code>(1). Where \u is replaced by the login name. For example: </p>
<p> <code>--login-options &#8216;-h darkstar --- \u&#8217;</code> </p>
<p>See <code>--autologin</code>, <code>--login-program</code> and <code>--remote</code>. </p>
<p>Please read the SECURITY NOTICE below before using this option. </p>
 </dd></dl>
<p> <code>-p</code>, <code>--login-pause</code> </p>
<dl>
<dd> <p> Wait for any key before dropping to the login prompt. Can be combined with <code>--autologin</code> to save memory by lazily spawning shells. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--chroot</code> <i>directory</i> </p>
<dl>
<dd> <p> Change root to the specified directory. </p>
 </dd></dl>
<p> <code>-R</code>, <code>--hangup</code> </p>
<dl>
<dd> <p> Call <code><a href="/docs/linux/man/2-vhangup/">vhangup</a></code>(2) to do a virtual hangup of the specified terminal. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--keep-baud</code> </p>
<dl>
<dd> <p> Try to keep the existing baud rate. The baud rates from the command line are used when <code>agetty</code> receives a BREAK character. If another baud rates specified then the original baud rate is also saved to the end of the wanted baud rates list. This can be used to return to the original baud rate after unexpected BREAKs. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--timeout</code> <i>timeout</i> </p>
<dl>
<dd> <p> Terminate if no user name could be read within <i>timeout</i> seconds. Use of this option with hardwired terminal lines is not recommended. </p>
 </dd></dl>
<p> <code>-U</code>, <code>--detect-case</code> </p>
<dl>
<dd> <p> Turn on support for detecting an uppercase-only terminal. This setting will detect a login name containing only capitals as indicating an uppercase-only terminal and turn on some upper-to-lower case conversions. Note that this has no support for any Unicode characters. </p>
 </dd></dl>
<p> <code>-w</code>, <code>--wait-cr</code> </p>
<dl>
<dd> <p> Wait for the user or the modem to send a carriage-return or a linefeed character before sending the <i>/etc/issue</i> file (or others) and the login prompt. This is useful with the <code>--init-string</code> option. </p>
 </dd></dl>
<p> <code>--nohints</code> </p>
<dl>
<dd> <p> Do not print hints about Num, Caps and Scroll Locks. </p>
 </dd></dl>
<p> <code>--nohostname</code> </p>
<dl>
<dd> <p> By default the hostname will be printed. With this option enabled, no hostname at all will be shown. </p>
 </dd></dl>
<p> <code>--long-hostname</code> </p>
<dl>
<dd> <p> By default the hostname is only printed until the first dot. With this option enabled, the fully qualified hostname by <code>gethostname</code>(3P) or (if not found) by <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) is shown. </p>
 </dd></dl>
<p> <code>--erase-chars</code> <i>string</i> </p>
<dl>
<dd> <p> This option specifies additional characters that should be interpreted as a backspace (&quot;ignore the previous character&quot;) when the user types the login name. The default additional &#8216;erase&#8217; has been &#8216;#&#8216;, but since util-linux 2.23 no additional erase characters are enabled by default. </p>
 </dd></dl>
<p> <code>--kill-chars</code> <i>string</i> </p>
<dl>
<dd> <p> This option specifies additional characters that should be interpreted as a kill (&quot;ignore all previous characters&quot;) when the user types the login name. The default additional &#8216;kill&#8217; has been &#8216;@&#8216;, but since util-linux 2.23 no additional kill characters are enabled by default. </p>
 </dd></dl>
<p> <code>--chdir</code> <i>directory</i> </p>
<dl>
<dd> <p> Change directory before the login. </p>
 </dd></dl>
<p> <code>--delay</code> <i>number</i> </p>
<dl>
<dd> <p> Sleep seconds before open tty. </p>
 </dd></dl>
<p> <code>--nice</code> <i>number</i> </p>
<dl>
<dd> <p> Run login with this priority. </p>
 </dd></dl>
<p> <code>--reload</code> </p>
<dl>
<dd> <p> Ask all running agetty instances to reload and update their displayed prompts, if the user has not yet commenced logging in. After doing so the command will exit. This feature might be unsupported on systems without Linux <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7). </p>
 </dd></dl>
<p> <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<h2>EXAMPLE</h2>
<p>This section shows examples for the process field of an entry in the <i>/etc/inittab</i> file. You&#8217;ll have to prepend appropriate values for the other fields. See <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5) for more details. </p>
<p>For a hardwired line or a console tty: </p>
<dl>
<dd> <p> <code>/sbin/agetty 9600 ttyS1</code> <br/>
 </p>
 </dd></dl>
<p>For a directly connected terminal without proper carrier-detect wiring (try this if your terminal just sleeps instead of giving you a password: prompt): </p>
<dl>
<dd> <p> <code>/sbin/agetty --local-line 9600 ttyS1 vt100</code> <br/>
 </p>
 </dd></dl>
<p>For an old-style dial-in line with a 9600/2400/1200 baud modem: </p>
<dl>
<dd> <p> <code>/sbin/agetty --extract-baud --timeout 60 ttyS1 9600,2400,1200</code> <br/>
 </p>
 </dd></dl>
<p>For a Hayes modem with a fixed 115200 bps interface to the machine (the example init string turns off modem echo and result codes, makes modem/computer DCD track modem/modem DCD, makes a DTR drop cause a disconnection, and turns on auto-answer after 1 ring): </p>
<dl>
<dd> <p> <code>/sbin/agetty --wait-cr --init-string &#8216;ATE0Q1&amp;D2&amp;C1S0=1\015&#8217; 115200 ttyS1</code> <br/>
 </p>
 </dd></dl>
<h2>SECURITY NOTICE</h2>
<p>If you use the <code>--login-program</code> and <code>--login-options</code> options, be aware that a malicious user may try to enter lognames with embedded options, which then get passed to the used login program. Agetty does check for a leading &quot;-&quot; and makes sure the logname gets passed as one parameter (so embedded spaces will not create yet another parameter), but depending on how the login binary parses the command line that might not be sufficient. Check that the used login program cannot be abused this way. </p>
<p>Some programs use &quot;--&quot; to indicate that the rest of the command line should not be interpreted as options. Use this feature if available by passing &quot;--&quot; before the username gets passed by \u.  </p>
<h2>ISSUE FILES</h2>
<p>The default issue file is <i>/etc/issue</i>. If the file exists, then <code>agetty</code> also checks for <i>/etc/issue.d</i> directory. The directory is optional extension to the default issue file and content of the directory is printed after <i>/etc/issue</i> content. If the <i>/etc/issue</i> does not exist, then the directory is ignored. All files <code>with .issue extension</code> from the directory are printed in version-sort order. The directory can be used to maintain 3rd-party messages independently on the primary system <i>/etc/issue</i> file. </p>
<p>Since version 2.35 additional locations for issue file and directory are supported. If the default <i>/etc/issue</i> does not exist, then <code>agetty</code> checks for <i>/run/issue</i> and <i>/run/issue.d</i>, thereafter for <i>/usr/lib/issue</i> and <i>/usr/lib/issue.d</i>. The directory <i>/etc</i> is expected for host specific configuration, <i>/run</i> is expected for generated stuff and <i>/usr/lib</i> for static distribution maintained configuration. </p>
<p>The default path maybe overridden by <code>--issue-file</code> option. In this case specified path has to be file or directory and all the default issue file and directory locations are ignored. </p>
<p>The issue file feature can be completely disabled by <code>--noissue</code> option. </p>
<p>It is possible to review the current issue file by <code>agetty --show-issue</code> on the current terminal. </p>
<p>The issue files may contain certain escape codes to display the system name, date, time et cetera. All escape codes consist of a backslash (\) immediately followed by one of the characters listed below. </p>
<p>4 or 4{<i>interface</i>} </p>
<dl>
<dd> <p> Insert the IPv4 address of the specified network interface (for example: \4{eth0}). If the <i>interface</i> argument is not specified, then select the first fully configured (UP, non-LOCALBACK, RUNNING) interface. If not any configured interface is found, fall back to the IP address of the machine&#8217;s hostname. </p>
 </dd></dl>
<p>6 or 6{<i>interface</i>} </p>
<dl>
<dd> <p> The same as \4 but for IPv6. </p>
 </dd></dl>
<p>b </p>
<dl>
<dd> <p> Insert the baudrate of the current line. </p>
 </dd></dl>
<p>d </p>
<dl>
<dd> <p> Insert the current date. </p>
 </dd></dl>
<p>e or e{<i>name</i>} </p>
<dl>
<dd> <p> Translate the human-readable <i>name</i> to an escape sequence and insert it (for example: \e{red}Alert text.\e{reset}). If the <i>name</i> argument is not specified, then insert \033. The currently supported names are: black, blink, blue, bold, brown, cyan, darkgray, gray, green, halfbright, lightblue, lightcyan, lightgray, lightgreen, lightmagenta, lightred, magenta, red, reset, reverse, yellow and white. All unknown names are silently ignored. </p>
 </dd></dl>
<p>s </p>
<dl>
<dd> <p> Insert the system name (the name of the operating system). Same as &#8216;uname -s&#8217;. See also the \S escape code. </p>
 </dd></dl>
<p>S or S{VARIABLE} </p>
<dl>
<dd> <p> Insert the VARIABLE data from <i>/etc/os-release</i>. If this file does not exist then fall back to <i>/usr/lib/os-release</i>. If the VARIABLE argument is not specified, then use PRETTY_NAME from the file or the system name (see \s). This escape code can be used to keep <i>/etc/issue</i> distribution and release independent. Note that \S{ANSI_COLOR} is converted to the real terminal escape sequence. </p>
 </dd></dl>
<p>l </p>
<dl>
<dd> <p> Insert the name of the current tty line. </p>
 </dd></dl>
<p>m </p>
<dl>
<dd> <p> Insert the architecture identifier of the machine. Same as <code>uname -m</code>. </p>
 </dd></dl>
<p>n </p>
<dl>
<dd> <p> Insert the nodename of the machine, also known as the hostname. Same as <code>uname -n</code>. </p>
 </dd></dl>
<p>o </p>
<dl>
<dd> <p> Insert the NIS domainname of the machine. Same as <code>hostname -d</code>. </p>
 </dd></dl>
<p>O </p>
<dl>
<dd> <p> Insert the DNS domainname of the machine. </p>
 </dd></dl>
<p>r </p>
<dl>
<dd> <p> Insert the release number of the OS. Same as <code>uname -r</code>. </p>
 </dd></dl>
<p>t </p>
<dl>
<dd> <p> Insert the current time. </p>
 </dd></dl>
<p>u </p>
<dl>
<dd> <p> Insert the number of current users logged in. </p>
 </dd></dl>
<p>U </p>
<dl>
<dd> <p> Insert the string &quot;1 user&quot; or &quot;&lt;n&gt; users&quot; where &lt;n&gt; is the number of current users logged in. </p>
 </dd></dl>
<p>v </p>
<dl>
<dd> <p> Insert the version of the OS, that is, the build-date and such. </p>
 </dd></dl>
<p>An example. On my system, the following <i>/etc/issue</i> file: </p>
<dl>
<dd> <pre><code>This is \n.\o (\s \m \r) \t
</code></pre>
 </dd></dl>
<p>displays as: </p>
<dl>
<dd> <pre><code>This is thingol.orcan.dk (Linux i386 1.1.9) 18:29:30
</code></pre>
 </dd></dl>
<h2>FILES</h2>
<p> <i>/var/run/utmp</i> </p>
<dl>
<dd> <p> the system status file. </p>
 </dd></dl>
<p> <i>/etc/issue</i> </p>
<dl>
<dd> <p> printed before the login prompt. </p>
 </dd></dl>
<p> <i>/etc/os-release /usr/lib/os-release</i> </p>
<dl>
<dd> <p> operating system identification data. </p>
 </dd></dl>
<p> <i>/dev/console</i> </p>
<dl>
<dd> <p> problem reports (if <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) is not used). </p>
 </dd></dl>
<p> <i>/etc/inittab</i> </p>
<dl>
<dd> <p> <code><a href="/docs/linux/man/8-init/">init</a></code>(8) configuration file for SysV-style init daemon. </p>
 </dd></dl>
<h2>BUGS</h2>
<p>The baud-rate detection feature (the <code>--extract-baud</code> option) requires that <code>agetty</code> be scheduled soon enough after completion of a dial-in call (within 30 ms with modems that talk at 2400 baud). For robustness, always use the <code>--extract-baud</code> option in combination with a multiple baud rate command-line argument, so that BREAK processing is enabled. </p>
<p>The text in the <i>/etc/issue</i> file (or other) and the login prompt are always output with 7-bit characters and space parity. </p>
<p>The baud-rate detection feature (the <code>--extract-baud</code> option) requires that the modem emits its status message <i>after</i> raising the DCD line.  </p>
<h2>DIAGNOSTICS</h2>
<p>Depending on how the program was configured, all diagnostics are written to the console device or reported via the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility. Error messages are produced if the <i>port</i> argument does not specify a terminal device; if there is no utmp entry for the current process (System V only); and so on.  </p>
<h2>AUTHORS</h2>
<p>The original <code>agetty</code> for serial terminals was written by and ported to Linux by  </p>
<h2>REPORTING BUGS</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p>The <code>agetty</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
