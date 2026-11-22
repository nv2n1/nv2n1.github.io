---

title: "tput(1)"
name: "tput"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tput/"
description: "tput, reset – initialize a terminal or query terminfo database"
---

<p> <code>tput</code>, <code>reset</code> - initialize a terminal or query terminfo database </p>
<h2>SYNOPSIS</h2>
<p> <code>tput</code> [<code>-T</code><i>type</i>] <i>capname</i> [<i>parameters</i>] <br/>
 <code>tput</code> [<code>-T</code><i>type</i>] [<code>-x</code>] <code>clear</code> <br/>
 <code>tput</code> [<code>-T</code><i>type</i>] <code>init</code> <br/>
 <code>tput</code> [<code>-T</code><i>type</i>] <code>reset</code> <br/>
 <code>tput</code> [<code>-T</code><i>type</i>] <code>longname</code> <br/>
 <code>tput -S</code> <code>&lt;&lt;</code> <br/>
 <code>tput -V</code> <br/>
  </p>
<h2>DESCRIPTION</h2>
<p> The <code>tput</code> utility uses the <code>terminfo</code> database to make the values of terminal-dependent capabilities and information available to the shell (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)), to initialize or reset the terminal, or return the long name of the requested terminal type. The result depends upon the capability&#8217;s type: </p>
<dl>
<dd>  </dd>
<dl>
<dt>string</dt>
<dd> <p> <code>tput</code> writes the string to the standard output. No trailing newline is supplied. </p>
 </dd>
<dt>integer</dt>
<dd> <p> <code>tput</code> writes the decimal value to the standard output, with a trailing newline. </p>
 </dd>
<dt>boolean</dt>
<dd> <p> <code>tput</code> simply sets the exit code (<code>0</code> for TRUE if the terminal has the capability, <code>1</code> for FALSE if it does not), and writes nothing to the standard output. </p>
 </dd></dl>
</dl>
<p> Before using a value returned on the standard output, the application should test the exit code (e.g., <code>$?</code>, see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) to be sure it is <code>0</code>. (See the <code>EXIT CODES</code> and <code>DIAGNOSTICS</code> sections.) For a complete list of capabilities and the <i>capname</i> associated with each, see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5).  </p>
<h3>Options</h3>
<dl>
<dt><code>-S</code></dt>
<dd> <p> allows more than one capability per invocation of <code>tput</code>. The capabilities must be passed to <code>tput</code> from the standard input instead of from the command line (see example). Only one <i>capname</i> is allowed per line. The <code>-S</code> option changes the meaning of the <code>0</code> and <code>1</code> boolean and string exit codes (see the EXIT CODES section). </p>
 </dd>
<dd> <p> Because some capabilities may use <i>string</i> parameters rather than <i>numbers</i>, <code>tput</code> uses a table and the presence of parameters in its input to decide whether to use <code>tparm</code>(3X), and how to interpret the parameters. </p>
 </dd>
<dt><code>-T</code><i>type</i></dt>
<dd> <p> indicates the <i>type</i> of terminal. Normally this option is unnecessary, because the default is taken from the environment variable <code>TERM</code>. If <code>-T</code> is specified, then the shell variables <code>LINES</code> and <code>COLUMNS</code> will also be ignored. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> reports the version of ncurses which was used in this program, and exits. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> do not attempt to clear the terminal&#8217;s scrollback buffer using the extended ``E3&#8217;&#8216; capability. </p>
 </dd></dl>
<h3>Commands</h3>
<p> A few commands (<code>init</code>, <code>reset</code> and <code>longname</code>) are special; they are defined by the <code>tput</code> program. The others are the names of <i>capabilities</i> from the terminal database (see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) for a list). Although <code>init</code> and <code>reset</code> resemble capability names, <code>tput</code> uses several capabilities to perform these special functions. </p>
<dl>
<dt><i>capname</i></dt>
<dd> <p> indicates the capability from the terminal database. </p>
 </dd>
<dd> <p> If the capability is a string that takes parameters, the arguments following the capability will be used as parameters for the string. </p>
 </dd>
<dd> <p> Most parameters are numbers. Only a few terminal capabilities require string parameters; <code>tput</code> uses a table to decide which to pass as strings. Normally <code>tput</code> uses <code>tparm</code>(3X) to perform the substitution. If no parameters are given for the capability, <code>tput</code> writes the string without performing the substitution. </p>
 </dd>
<dt><code>init</code></dt>
<dd> <p> If the terminal database is present and an entry for the user&#8217;s terminal exists (see <code>-T</code><i>type</i>, above), the following will occur: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>(1)</dt>
<dd> <p> first, <code>tput</code> retrieves the current terminal mode settings for your terminal. It does this by successively testing </p>
 </dd>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 the standard error, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard output, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard input and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 ultimately ``/dev/tty&#8217;&#8216; </p>
 </dd></dl>
<dd> <p> to obtain terminal settings. Having retrieved these settings, <code>tput</code> remembers which file descriptor to use when updating settings. </p>
 </dd>
<dt>(2)</dt>
<dd> <p> if the window size cannot be obtained from the operating system, but the terminal description (or environment, e.g., <code>LINES</code> and <code>COLUMNS</code> variables specify this), update the operating system&#8217;s notion of the window size. </p>
 </dd>
<dt>(3)</dt>
<dd> <p> the terminal modes will be updated: </p>
 </dd>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 any delays (e.g., newline) specified in the entry will be set in the tty driver, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 tabs expansion will be turned on or off according to the specification in the entry, and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 if tabs are not expanded, standard tabs will be set (every 8 spaces). </p>
 </dd></dl>
<dt>(4)</dt>
<dd> <p> if present, the terminal&#8217;s initialization strings will be output as detailed in the <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) section on <i>Tabs and Initialization</i>, </p>
 </dd>
<dt>(5)</dt>
<dd> <p> output is flushed. </p>
 </dd></dl>
</dl>
<dd> <p> If an entry does not contain the information needed for any of these activities, that activity will silently be skipped. </p>
 </dd>
<dt><code>reset</code></dt>
<dd> <p> This is similar to <code>init</code>, with two differences: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>(1)</dt>
<dd> <p> before any other initialization, the terminal modes will be reset to a ``sane&#8217;&#8216; state: </p>
 </dd>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 set cooked and echo modes, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 turn off cbreak and raw modes, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 turn on newline translation and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 reset any unset special characters to their default values </p>
 </dd></dl>
<dt>(2)</dt>
<dd> <p> Instead of putting out <i>initialization</i> strings, the terminal&#8217;s <i>reset</i> strings will be output if present (<code>rs1</code>, <code>rs2</code>, <code>rs3</code>, <code>rf</code>). If the <i>reset</i> strings are not present, but <i>initialization</i> strings are, the <i>initialization</i> strings will be output. </p>
 </dd></dl>
</dl>
<dd> <p> Otherwise, <code>reset</code> acts identically to <code>init</code>. </p>
 </dd>
<dt><code>longname</code></dt>
<dd> <p> If the terminal database is present and an entry for the user&#8217;s terminal exists (see <code>-T</code><i>type</i> above), then the long name of the terminal will be put out. The long name is the last name in the first line of the terminal&#8217;s description in the <code>terminfo</code> database [see <code><a href="/docs/linux/man/5-term/">term</a></code>(5)]. </p>
 </dd></dl>
<h3>Aliases</h3>
<p> <code>tput</code> handles the <code>clear</code>, <code>init</code> and <code>reset</code> commands specially: it allows for the possibility that it is invoked by a link with those names. </p>
<p> If <code>tput</code> is invoked by a link named <code>reset</code>, this has the same effect as <code>tput reset</code>. The <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1) utility also treats a link named <code>reset</code> specially. </p>
<p> Before ncurses 6.1, the two utilities were different from each other: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>tset</code> utility reset the terminal modes and special characters (not done with <code>tput</code>). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 On the other hand, <code>tset</code>&#8216;s repertoire of terminal capabilities for resetting the terminal was more limited, i.e., only <code>reset_1string</code>, <code>reset_2string</code> and <code>reset_file</code> in contrast to the tab-stops and margins which are set by this utility. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>reset</code> program is usually an alias for <code>tset</code>, because of this difference with resetting terminal modes and special characters. </p>
<p> With the changes made for ncurses 6.1, the <i>reset</i> feature of the two programs is (mostly) the same. A few differences remain: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>tset</code> program waits one second when resetting, in case it happens to be a hardware terminal. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The two programs write the terminal initialization strings to different streams (i.e., the standard error for <code>tset</code> and the standard output for <code>tput</code>). </p>
<dl>
<dd> <p> <code>Note:</code> although these programs write to different streams, redirecting their output to a file will capture only part of their actions. The changes to the terminal modes are not affected by redirecting the output. </p>
 </dd></dl>
<p> If <code>tput</code> is invoked by a link named <code>init</code>, this has the same effect as <code>tput init</code>. Again, you are less likely to use that link because another program named <code>init</code> has a more well-established use.  </p>
<h3>Terminal Size</h3>
<p> Besides the special commands (e.g., <code>clear</code>), tput treats certain terminfo capabilities specially: <code>lines</code> and <code>cols</code>. tput calls <code>setupterm</code>(3X) to obtain the terminal size: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 first, it gets the size from the terminal database (which generally is not provided for terminal emulators which do not have a fixed window size) <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 then it asks the operating system for the terminal&#8217;s size (which generally works, unless connecting via a serial line which does not support <i>NAWS</i>: negotiations about window size). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 finally, it inspects the environment variables <code>LINES</code> and <code>COLUMNS</code> which may override the terminal size. </p>
<p> If the <code>-T</code> option is given tput ignores the environment variables by calling <code>use_tioctl(TRUE)</code>, relying upon the operating system (or finally, the terminal database).  </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>tput init</code></dt>
<dd> <p> Initialize the terminal according to the type of terminal in the environmental variable <code>TERM</code>. This command should be included in everyone&#8217;s .profile after the environmental variable <code>TERM</code> has been exported, as illustrated on the <code>profile</code>(5) manual page. </p>
 </dd>
<dt><code>tput -T5620 reset</code></dt>
<dd> <p> Reset an AT&amp;T 5620 terminal, overriding the type of terminal in the environmental variable <code>TERM</code>. </p>
 </dd>
<dt><code>tput cup 0 0</code></dt>
<dd> <p> Send the sequence to move the cursor to row <code>0</code>, column <code>0</code> (the upper left corner of the screen, usually known as the ``home&#8217;&#8216; cursor position). </p>
 </dd>
<dt><code>tput clear</code></dt>
<dd> <p> Echo the clear-screen sequence for the current terminal. </p>
 </dd>
<dt><code>tput cols</code></dt>
<dd> <p> Print the number of columns for the current terminal. </p>
 </dd>
<dt><code>tput -T450 cols</code></dt>
<dd> <p> Print the number of columns for the 450 terminal. </p>
 </dd>
<dt><code>bold=`tput smso` offbold=`tput rmso`</code></dt>
<dd> <p> Set the shell variables <code>bold</code>, to begin stand-out mode sequence, and <code>offbold</code>, to end standout mode sequence, for the current terminal. This might be followed by a prompt: <code>echo &quot;${bold}Please type in your name: ${offbold}\c&quot;</code> </p>
 </dd>
<dt><code>tput hc</code></dt>
<dd> <p> Set exit code to indicate if the current terminal is a hard copy terminal. </p>
 </dd>
<dt><code>tput cup 23 4</code></dt>
<dd> <p> Send the sequence to move the cursor to row 23, column 4. </p>
 </dd>
<dt><code>tput cup</code></dt>
<dd> <p> Send the terminfo string for cursor-movement, with no parameters substituted. </p>
 </dd>
<dt><code>tput longname</code></dt>
<dd> <p> Print the long name from the <code>terminfo</code> database for the type of terminal specified in the environmental variable <code>TERM</code>. </p>
 </dd></dl>
<dl>
<dd> <p> <code>tput -S &lt;&lt;!</code> <br/>
 <code>&gt; clear</code> <br/>
 <code>&gt; cup 10 10</code> <br/>
 <code>&gt; bold</code> <br/>
 <code>&gt; !</code> </p>
 </dd></dl>
<dl>
<dd> <p> This example shows <code>tput</code> processing several capabilities in one invocation. It clears the screen, moves the cursor to position 10, 10 and turns on bold (extra bright) mode. The list is terminated by an exclamation mark (<code>!</code>) on a line by itself. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/terminfo</code></dt>
<dd> <p> compiled terminal description database </p>
 </dd>
<dt><code>/usr/share/tabset/*</code></dt>
<dd> <p> tab settings for some terminals, in a format appropriate to be output to the terminal (escape sequences that set margins and tabs); for more information, see the <i>Tabs and Initialization</i>, section of <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) </p>
 </dd></dl>
<h2>EXIT CODES</h2>
<p> If the <code>-S</code> option is used, <code>tput</code> checks for errors from each line, and if any errors are found, will set the exit code to 4 plus the number of lines with errors. If no errors are found, the exit code is <code>0</code>. No indication of which line failed can be given so exit code <code>1</code> will never appear. Exit codes <code>2</code>, <code>3</code>, and <code>4</code> retain their usual interpretation. If the <code>-S</code> option is not used, the exit code depends on the type of <i>capname</i>: </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>boolean</i></dt>
<dd> <p> a value of <code>0</code> is set for TRUE and <code>1</code> for FALSE. </p>
 </dd>
<dt><i>string</i></dt>
<dd> <p> a value of <code>0</code> is set if the <i>capname</i> is defined for this terminal <i>type</i> (the value of <i>capname</i> is returned on standard output); a value of <code>1</code> is set if <i>capname</i> is not defined for this terminal <i>type</i> (nothing is written to standard output). </p>
 </dd>
<dt><i>integer</i></dt>
<dd> <p> a value of <code>0</code> is always set, whether or not <i>capname</i> is defined for this terminal <i>type</i>. To determine if <i>capname</i> is defined for this terminal <i>type</i>, the user must test the value written to standard output. A value of <code>-1</code> means that <i>capname</i> is not defined for this terminal <i>type</i>. </p>
 </dd>
<dt><i>other</i></dt>
<dd> <p> <code>reset</code> or <code>init</code> may fail to find their respective files. In that case, the exit code is set to 4 + <code>errno</code>. </p>
 </dd></dl>
</dl>
<p> Any other exit code indicates an error; see the DIAGNOSTICS section.  </p>
<h2>DIAGNOSTICS</h2>
<p> <code>tput</code> prints the following error messages and sets the corresponding exit codes. </p>
<table>
<tr VALIGN=top>
<td>exit code</td>
<td>error message
</td>
</tr>
<tr VALIGN=top>
<td><hr />
<hr />
</td>
</tr>
<tr VALIGN=top>
<td><code>0</code></td>
<td> (<i>capname</i> is a numeric variable that is not specified in the <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) database for this terminal type, e.g. <code>tput -T450 lines</code> and <code>tput -Thp2621 xmc</code>) 
</td>
</tr>
<tr VALIGN=top>
<td><code>1</code></td>
<td>no error message is printed, see the <code>EXIT CODES</code> section.
</td>
</tr>
<tr VALIGN=top>
<td><code>2</code></td>
<td>usage error
</td>
</tr>
<tr VALIGN=top>
<td><code>3</code></td>
<td>unknown terminal <i>type</i> or no <code>terminfo</code> database
</td>
</tr>
<tr VALIGN=top>
<td><code>4</code></td>
<td>unknown <code>terminfo</code> capability <i>capname</i>
</td>
</tr>
<tr VALIGN=top>
<td><code>&gt;4</code></td>
<td>error occurred in -S
</td>
</tr>
<tr VALIGN=top>
<td><hr />
<hr />
</td>
</tr>
</table>
<h2>HISTORY</h2>
<p> The <code>tput</code> command was begun by Bill Joy in 1980. The initial version only cleared the screen. </p>
<p> AT&amp;T System V provided a different <code>tput</code> command: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr2 provided a rudimentary <code>tput</code> which checked the parameter against each predefined capability and returned the corresponding value. This version of <code>tput</code> did not use <code>tparm</code>(3X) for the capabilities which are parameterized. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr3 replaced that, a year later, by a more extensive program whose <code>init</code> and <code>reset</code> subcommands (more than half the program) were incorporated from the <code>reset</code> feature of BSD <code>tset</code> written by Eric Allman. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr4 added color initialization using the <i>orig_colors</i> and <i>orig_pairs</i> capabilities in the <code>init</code> subcommand. </p>
<p> Keith Bostic replaced the BSD <code>tput</code> command in 1989 with a new implementation based on the AT&amp;T System V program <code>tput</code>. Like the AT&amp;T program, Bostic&#8217;s version accepted some parameters named for <i>terminfo capabilities</i> (<code>clear</code>, <code>init</code>, <code>longname</code> and <code>reset</code>). However (because he had only termcap available), it accepted <i>termcap names</i> for other capabilities. Also, Bostic&#8217;s BSD <code>tput</code> did not modify the terminal I/O modes as the earlier BSD <code>tset</code> had done. </p>
<p> At the same time, Bostic added a shell script named ``clear&#8217;&#8216;, which used <code>tput</code> to clear the screen. </p>
<p> Both of these appeared in 4.4BSD, becoming the ``modern&#8217;&#8216; BSD implementation of <code>tput</code>. </p>
<p> This implementation of <code>tput</code> began from a different source than AT&amp;T or BSD: Ross Ridge&#8217;s <i>mytinfo</i> package, published on <i>comp.sources.unix</i> in December 1992. Ridge&#8217;s program made more sophisticated use of the terminal capabilities than the BSD program. Eric Raymond used that <code>tput</code> program (and other parts of <i>mytinfo</i>) in ncurses in June 1995. Using the portions dealing with terminal capabilities almost without change, Raymond made improvements to the way the command-line parameters were handled.  </p>
<h2>PORTABILITY</h2>
<p> This implementation of <code>tput</code> differs from AT&amp;T <code>tput</code> in two important areas: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>tput</code> <i>capname</i> writes to the standard output. That need not be a regular terminal. However, the subcommands which manipulate terminal modes may not use the standard output. </p>
<dl>
<dd> <p> The AT&amp;T implementation&#8217;s <code>init</code> and <code>reset</code> commands use the BSD (4.1c) <code>tset</code> source, which manipulates terminal modes. It successively tries standard output, standard error, standard input before falling back to ``/dev/tty&#8217;&#8216; and finally just assumes a 1200Bd terminal. When updating terminal modes, it ignores errors. </p>
 </dd>
<dd> <p> Until changes made after ncurses 6.0, <code>tput</code> did not modify terminal modes. <code>tput</code> now uses a similar scheme, using functions shared with <code>tset</code> (and ultimately based on the 4.4BSD <code>tset</code>). If it is not able to open a terminal, e.g., when running in <code>cron</code>, <code>tput</code> will return an error. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 AT&amp;T <code>tput</code> guesses the type of its <i>capname</i> operands by seeing if all of the characters are numeric, or not. </p>
 </dd>
<dd> <p> Most implementations which provide support for <i>capname</i> operands use the <i>tparm</i> function to expand parameters in it. That function expects a mixture of numeric and string parameters, requiring <code>tput</code> to know which type to use. </p>
 </dd>
<dd> <p> This implementation uses a table to determine the parameter types for the standard <i>capname</i> operands, and an internal library function to analyze nonstandard <i>capname</i> operands. </p>
 </dd>
<dd> <p> Besides providing more reliable operation than AT&amp;T&#8217;s utility, a portability problem is introduced by this analysis: An OpenBSD developer adapted the internal library function from ncurses to port NetBSD&#8217;s termcap-based <code>tput</code> to terminfo. That had been modified to interpret multiple commands on a line. Portable applications should not rely upon this feature; ncurses provides it to support applications written specifically for OpenBSD. </p>
 </dd></dl>
<p> This implementation (unlike others) can accept both <i>termcap</i> and <i>terminfo</i> names for the <i>capname</i> feature, if <i>termcap</i> support is compiled in. However, the predefined <i>termcap</i> and <i>terminfo</i> names have two ambiguities in this case (and the <i>terminfo</i> name is assumed): <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <i>termcap</i> name <code>dl</code> corresponds to the <i>terminfo</i> name <code>dl1</code> (delete one line). <br/>
 The <i>terminfo</i> name <code>dl</code> corresponds to the <i>termcap</i> name <code>DL</code> (delete a given number of lines). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <i>termcap</i> name <code>ed</code> corresponds to the <i>terminfo</i> name <code>rmdc</code> (end delete mode). <br/>
 The <i>terminfo</i> name <code>ed</code> corresponds to the <i>termcap</i> name <code>cd</code> (clear to end of screen). </p>
<p> The <code>longname</code> and <code>-S</code> options, and the parameter-substitution features used in the <code>cup</code> example, were not supported in BSD curses before 4.3reno (1989) or in AT&amp;T/USL curses before SVr4 (1988). </p>
<p> IEEE Std 1003.1/The Open Group Base Specifications Issue 7 (POSIX.1-2008) documents only the operands for <code>clear</code>, <code>init</code> and <code>reset</code>. There are a few interesting observations to make regarding that: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 In this implementation, <code>clear</code> is part of the <i>capname</i> support. The others (<code>init</code> and <code>longname</code>) do not correspond to terminal capabilities. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Other implementations of <code>tput</code> on SVr4-based systems such as Solaris, IRIX64 and HPUX as well as others such as AIX and Tru64 provide support for <i>capname</i> operands. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 A few platforms such as FreeBSD recognize termcap names rather than terminfo capability names in their respective <code>tput</code> commands. Since 2010, NetBSD&#8217;s <code>tput</code> uses terminfo names. Before that, it (like FreeBSD) recognized termcap names. </p>
<dl>
<dd> <p> Beginning in 2021, FreeBSD uses the ncurses <code>tput</code>, configured for both terminfo (tested first) and termcap (as a fallback). </p>
 </dd></dl>
<p> Because (apparently) <i>all</i> of the certified Unix systems support the full set of capability names, the reasoning for documenting only a few may not be apparent. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 X/Open Curses Issue 7 documents <code>tput</code> differently, with <i>capname</i> and the other features used in this implementation. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 That is, there are two standards for <code>tput</code>: POSIX (a subset) and X/Open Curses (the full implementation). POSIX documents a subset to avoid the complication of including X/Open Curses and the terminal capabilities database. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 While it is certainly possible to write a <code>tput</code> program without using curses, none of the systems which have a curses implementation provide a <code>tput</code> utility which does not provide the <i>capname</i> feature. </p>
<p> X/Open Curses Issue 7 (2009) is the first version to document utilities. However that part of X/Open Curses does not follow existing practice (i.e., Unix features documented in SVID 3): <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 It assigns exit code 4 to ``invalid operand&#8217;&#8216;, which may be the same as <i>unknown capability</i>. For instance, the source code for Solaris&#8217; xcurses uses the term ``invalid&#8217;&#8216; in this case. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 It assigns exit code 255 to a numeric variable that is not specified in the terminfo database. That likely is a documentation error, confusing the <code>-1</code> written to the standard output for an absent or cancelled numeric value versus an (unsigned) exit code. </p>
<p> The various Unix systems (AIX, HPUX, Solaris) use the same exit-codes as ncurses. </p>
<p> NetBSD curses documents different exit codes which do not correspond to either ncurses or X/Open.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/1-tabs/">tabs</a></code>(1), <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1), <code>termcap</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5). </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
