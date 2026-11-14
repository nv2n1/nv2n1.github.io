---
title: "reset(1)"
name: "reset"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reset/"
description: "tset, reset – terminal initialization"
---

<h2 class="name">NAME</h2>
<p> <code>tset</code>, <code>reset</code> &#8211; terminal initialization </p>
<h2>SYNOPSIS</h2>
<p> <code>tset</code> [<code>-IQVcqrsw</code>] [<code>&#8211;</code>] [<code>-e</code> <i>ch</i>] [<code>-i</code> <i>ch</i>] [<code>-k</code> <i>ch</i>] [<code>-m</code> <i>mapping</i>] [<i>terminal</i>]<br />
 <code>reset</code> [<code>-IQVcqrsw</code>] [<code>&#8211;</code>] [<code>-e</code> <i>ch</i>] [<code>-i</code> <i>ch</i>] [<code>-k</code> <i>ch</i>] [<code>-m</code> <i>mapping</i>] [<i>terminal</i>]</p>
<h2>DESCRIPTION</h2>
<h3>tset &#8211; initialization</h3>
<p> This program initializes terminals. </p>
<p> First, <code>tset</code> retrieves the current terminal mode settings for your terminal. It does this by successively testing<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the standard error,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard output,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard input and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 ultimately &#8220;/dev/tty&#8221; </p>
<p> to obtain terminal settings. Having retrieved these settings, <code>tset</code> remembers which file descriptor to use when updating settings. </p>
<p> Next, <code>tset</code> determines the type of terminal that you are using. This determination is done as follows, using the first terminal type found. </p>
<p> 1. The <code>terminal</code> argument specified on the command line. </p>
<p> 2. The value of the <code>TERM</code> environmental variable. </p>
<p> 3. (BSD systems only.) The terminal type associated with the standard error output device in the <i>/etc/ttys</i> file. (On System-V-like UNIXes and systems using that convention, <i>getty</i> does this job by setting <code>TERM</code> according to the type passed to it by <i>/etc/inittab</i>.) </p>
<p> 4. The default terminal type, &#8220;unknown&#8221;. </p>
<p> If the terminal type was not specified on the command-line, the <code>-m</code> option mappings are then applied (see the section <code>TERMINAL TYPE MAPPING</code> for more information). Then, if the terminal type begins with a question mark (&#8220;?&#8221;), the user is prompted for confirmation of the terminal type. An empty response confirms the type, or, another type can be entered to specify a new type. Once the terminal type has been determined, the terminal description for the terminal is retrieved. If no terminal description is found for the type, the user is prompted for another terminal type. </p>
<p> Once the terminal description is retrieved,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the &#8220;<code>-w</code>&#8221; option is enabled, <code>tset</code> may update the terminal&#8217;s window size.</p>
<dl>
<dt>
<dd> If the window size cannot be obtained from the operating system, but the terminal description (or environment, e.g., <code>LINES</code> and <code>COLUMNS</code> variables specify this), use this to set the operating system&#8217;s notion of the window size.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the &#8220;<code>-c</code>&#8221; option is enabled, the backspace, interrupt and line kill characters (among many other things) are set<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 unless the &#8220;<code>-I</code>&#8221; option is enabled, the terminal and tab <i>initialization</i> strings are sent to the standard error output, and <code>tset</code> waits one second (in case a hardware reset was issued).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Finally, if the erase, interrupt and line kill characters have changed, or are not set to their default values, their values are displayed to the standard error output.</dl>
<h3>reset &#8211; reinitialization</h3>
<p> When invoked as <code>reset</code>, <code>tset</code> sets the terminal modes to &#8220;sane&#8221; values:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 sets cooked and echo modes,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 turns off cbreak and raw modes,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 turns on newline translation and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 resets any unset special characters to their default values </p>
<p> before doing the terminal initialization described above. Also, rather than using the terminal <i>initialization</i> strings, it uses the terminal <i>reset</i> strings. </p>
<p> The <code>reset</code> command is useful after a program dies leaving a terminal in an abnormal state:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 you may have to type </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>&lt;LF&gt;</i><code>reset</code><i>&lt;LF&gt;</i> </p>
<p> (the line-feed character is normally control-J) to get the terminal to work, as carriage-return may no longer work in the abnormal state.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Also, the terminal will often not echo the command.</p>
<h2>OPTIONS</h2>
<p> The options are as follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> Set control characters and modes.</p>
<dt><code>-e&nbsp;</code><i>ch</i></p>
<dd> Set the erase character to <i>ch</i>.</p>
<dt><code>-I</code></p>
<dd> Do not send the terminal or tab initialization strings to the terminal.</p>
<dt><code>-i&nbsp;</code><i>ch</i></p>
<dd> Set the interrupt character to <i>ch</i>.</p>
<dt><code>-k&nbsp;</code><i>ch</i></p>
<dd> Set the line kill character to <i>ch</i>.</p>
<dt><code>-m&nbsp;</code><i>mapping</i></p>
<dd> Specify a mapping from a port type to a terminal. See the section <code>TERMINAL TYPE MAPPING</code> for more information.</p>
<dt><code>-Q</code></p>
<dd> Do not display any values for the erase, interrupt and line kill characters. Normally <code>tset</code> displays the values for control characters which differ from the system&#8217;s default values.</p>
<dt><code>-q</code></p>
<dd> The terminal type is displayed to the standard output, and the terminal is not initialized in any way. The option &#8220;-&#8221; by itself is equivalent but archaic.</p>
<dt><code>-r</code></p>
<dd> Print the terminal type to the standard error output.</p>
<dt><code>-s</code></p>
<dd> Print the sequence of shell commands to initialize the environment variable <code>TERM</code> to the standard output. See the section <code>SETTING THE ENVIRONMENT</code> for details.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits.</p>
<dt><code>-w</code></p>
<dd> Resize the window to match the size deduced via <code><a href="//www.systutorials.com/docs/linux/man/3X-setupterm/">setupterm</a></code>(3X). Normally this has no effect, unless <code>setupterm</code> is not able to detect the window size.</dl>
<p> The arguments for the <code>-e</code>, <code>-i</code>, and <code>-k</code> options may either be entered as actual characters or by using the &#8220;hat&#8221; notation, i.e., control-h may be specified as &#8220;^H&#8221; or &#8220;^h&#8221;. </p>
<p> If neither <code>-c</code> or <code>-w</code> is given, both options are assumed.</p>
<h2>SETTING THE ENVIRONMENT</h2>
<p> It is often desirable to enter the terminal type and information about the terminal&#8217;s capabilities into the shell&#8217;s environment. This is done using the <code>-s</code> option. </p>
<p> When the <code>-s</code> option is specified, the commands to enter the information into the shell&#8217;s environment are written to the standard output. If the <code>SHELL</code> environmental variable ends in &#8220;csh&#8221;, the commands are for <code>csh</code>, otherwise, they are for <code>sh</code>. Note, the <code>csh</code> commands set and unset the shell variable <code>noglob</code>, leaving it unset. The following line in the <code>.login</code> or <code>.profile</code> files will initialize the environment correctly: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;eval&nbsp;`tset -s options &#8230;&nbsp;`</p>
<h2>TERMINAL TYPE MAPPING</h2>
<p> When the terminal is not hardwired into the system (or the current system information is incorrect) the terminal type derived from the <i>/etc/ttys</i> file or the <code>TERM</code> environmental variable is often something generic like <code>network</code>, <code>dialup</code>, or <code>unknown</code>. When <code>tset</code> is used in a startup script it is often desirable to provide information about the type of terminal used on such ports. </p>
<p> The <code>-m</code> options maps from some set of conditions to a terminal type, that is, to tell <code>tset</code> &#8220;If I&#8217;m on this port at a particular speed, guess that I&#8217;m on that kind of terminal&#8221;. </p>
<p> The argument to the <code>-m</code> option consists of an optional port type, an optional operator, an optional baud rate specification, an optional colon (&#8220;:&#8221;) character and a terminal type. The port type is a string (delimited by either the operator or the colon character). The operator may be any combination of &#8220;&gt;&#8221;, &#8220;&lt;&#8221;, &#8220;@&#8221;, and &#8220;!&#8221;; &#8220;&gt;&#8221; means greater than, &#8220;&lt;&#8221; means less than, &#8220;@&#8221; means equal to and &#8220;!&#8221; inverts the sense of the test. The baud rate is specified as a number and is compared with the speed of the standard error output (which should be the control terminal). The terminal type is a string. </p>
<p> If the terminal type is not specified on the command line, the <code>-m</code> mappings are applied to the terminal type. If the port type and baud rate match the mapping, the terminal type specified in the mapping replaces the current type. If more than one mapping is specified, the first applicable mapping is used. </p>
<p> For example, consider the following mapping: <code>dialup&gt;9600:vt100</code>. The port type is dialup , the operator is &gt;, the baud rate specification is 9600, and the terminal type is vt100. The result of this mapping is to specify that if the terminal type is <code>dialup</code>, and the baud rate is greater than 9600 baud, a terminal type of <code>vt100</code> will be used. </p>
<p> If no baud rate is specified, the terminal type will match any baud rate. If no port type is specified, the terminal type will match any port type. For example, <code>-m dialup:vt100 -m :?xterm</code> will cause any dialup port, regardless of baud rate, to match the terminal type vt100, and any non-dialup port type to match the terminal type ?xterm. Note, because of the leading question mark, the user will be queried on a default port as to whether they are actually using an xterm terminal. </p>
<p> No whitespace characters are permitted in the <code>-m</code> option argument. Also, to avoid problems with meta-characters, it is suggested that the entire <code>-m</code> option argument be placed within single quote characters, and that <code>csh</code> users insert a backslash character (&#8220;\&#8221;) before any exclamation marks (&#8220;!&#8221;).</p>
<h2>HISTORY</h2>
<p> A <code>reset</code> command appeared in 1BSD (March 1978), written by Kurt Shoens. This program set the <i>erase</i> and <i>kill</i> characters to <code>^H</code> (backspace) and <code>@</code> respectively. Mark Horton improved that in 3BSD (October 1979), adding <i>intr</i>, <i>quit</i>, <i>start</i>/<i>stop</i> and <i>eof</i> characters as well as changing the program to avoid modifying any user settings. That version of <code>reset</code> did not use the termcap database. </p>
<p> A separate <code>tset</code> command was provided in 1BSD by Eric Allman, using the termcap database. Allman&#8217;s comments in the source code indicate that he began work in October 1977, continuing development over the next few years. </p>
<p> According to comments in the source code, the <code>tset</code> program was modified in September 1980, to use logic copied from the 3BSD &#8220;reset&#8221; when it was invoked as <code>reset</code>. This version appeared in 4.1cBSD, late in 1982. </p>
<p> Other developers (e.g., Keith Bostic and Jim Bloom) continued to modify <code>tset</code> until 4.4BSD was released in 1993. </p>
<p> The <code>ncurses</code> implementation was lightly adapted from the 4.4BSD sources for a terminfo environment by Eric S. Raymond &lt;esr [at] snark.thyrsus.com&gt;.</p>
<h2>COMPATIBILITY</h2>
<p> Neither IEEE Std 1003.1/The Open Group Base Specifications Issue 7 (POSIX.1-2008) nor X/Open Curses Issue 7 documents <code>tset</code> or <code>reset</code>. </p>
<p> The AT&amp;T <code>tput</code> utility (AIX, HPUX, Solaris) incorporated the terminal-mode manipulation as well as termcap-based features such as resetting tabstops from <code>tset</code> in BSD (4.1c), presumably with the intention of making <code>tset</code> obsolete. However, each of those systems still provides <code>tset</code>. In fact, the commonly-used <code>reset</code> utility is always an alias for <code>tset</code>. </p>
<p> The <code>tset</code> utility provides for backward-compatibility with BSD environments (under most modern UNIXes, <code>/etc/inittab</code> and <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) can set <code>TERM</code> appropriately for each dial-up line; this obviates what was <code>tset</code>&#8216;s most important use). This implementation behaves like 4.4BSD <code>tset</code>, with a few exceptions specified here. </p>
<p> A few options are different because the <code>TERMCAP</code> variable is no longer supported under terminfo-based <code>ncurses</code>:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>-S</code> option of BSD <code>tset</code> no longer works; it prints an error message to the standard error and dies.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>-s</code> option only sets <code>TERM</code>, not <code>TERMCAP</code>. </p>
<p> There was an undocumented 4.4BSD feature that invoking <code>tset</code> via a link named &#8220;TSET&#8221; (or via any other name beginning with an upper-case letter) set the terminal to use upper-case only. This feature has been omitted. </p>
<p> The <code>-A</code>, <code>-E</code>, <code>-h</code>, <code>-u</code> and <code>-v</code> options were deleted from the <code>tset</code> utility in 4.4BSD. None of them were documented in 4.3BSD and all are of limited utility at best. The <code>-a</code>, <code>-d</code>, and <code>-p</code> options are similarly not documented or useful, but were retained as they appear to be in widespread use. It is strongly recommended that any usage of these three options be changed to use the <code>-m</code> option instead. The <code>-a</code>, <code>-d</code>, and <code>-p</code> options are therefore omitted from the usage summary above. </p>
<p> Very old systems, e.g., 3BSD, used a different terminal driver which was replaced in 4BSD in the early 1980s. To accommodate these older systems, the 4BSD <code>tset</code> provided a <code>-n</code> option to specify that the new terminal driver should be used. This implementation does not provide that choice. </p>
<p> It is still permissible to specify the <code>-e</code>, <code>-i</code>, and <code>-k</code> options without arguments, although it is strongly recommended that such usage be fixed to explicitly specify the character. </p>
<p> As of 4.4BSD, executing <code>tset</code> as <code>reset</code> no longer implies the <code>-Q</code> option. Also, the interaction between the &#8211; option and the <i>terminal</i> argument in some historic implementations of <code>tset</code> has been removed. </p>
<p> The <code>-c</code> and <code>-w</code> options are not found in earlier implementations. However, a different window size-change feature was provided in 4.4BSD.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In 4.4BSD, <code>tset</code> uses the window size from the termcap description to set the window size if <code>tset</code> is not able to obtain the window size from the operating system.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In ncurses, <code>tset</code> obtains the window size using <code>setupterm</code>, which may be from the operating system, the <code>LINES</code> and <code>COLUMNS</code> environment variables or the terminal description. </p>
<p> Obtaining the window size from the terminal description is common to both implementations, but considered obsolescent. Its only practical use is for hardware terminals. Generally speaking, a window size would be unset only if there were some problem obtaining the value from the operating system (and <code>setupterm</code> would still fail). For that reason, the <code>LINES</code> and <code>COLUMNS</code> environment variables may be useful for working around window-size problems. Those have the drawback that if the window is resized, those variables must be recomputed and reassigned. To do this more easily, use the <code><a href="/docs/linux/man/1-resize/">resize</a></code>(1) program.</p>
<h2>ENVIRONMENT</h2>
<p> The <code>tset</code> command uses these environment variables:</p>
<dl>
<dt>SHELL</p>
<dd> tells <code>tset</code> whether to initialize <code>TERM</code> using <code>sh</code> or <code>csh</code> syntax.</p>
<dt>TERM</p>
<dd> Denotes your terminal type. Each terminal type is distinct, though many are similar.</p>
<dt>TERMCAP</p>
<dd> may denote the location of a termcap database. If it is not an absolute pathname, e.g., begins with a &#8220;/&#8221;, <code>tset</code> removes the variable from the environment before looking for the terminal description.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/ttys</p>
<dd> system port name to terminal type mapping database (BSD versions only).</p>
<dt>/etc/terminfo</p>
<dd> terminal capability database</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3X-curs_terminfo/">curs_terminfo</a></code>(3X), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code><a href="/docs/linux/man/5-ttys/">ttys</a></code>(5), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
