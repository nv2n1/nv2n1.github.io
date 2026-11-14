---
title: "tput(1)"
name: "tput"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tput/"
description: "tput, reset – initialize a terminal or query terminfo database"
---

<h2 class="name">NAME</h2>
<p> <code>tput</code>, <code>reset</code> &#8211; initialize a terminal or query terminfo database </p>
<h2>SYNOPSIS</h2>
<p> <code>tput</code> [<code>-T</code><i>type</i>] <i>capname</i> [<i>parameters</i>]<br />
 <code>tput</code> [<code>-T</code><i>type</i>] [<code>-x</code>] <code>clear</code><br />
 <code>tput</code> [<code>-T</code><i>type</i>] <code>init</code><br />
 <code>tput</code> [<code>-T</code><i>type</i>] <code>reset</code><br />
 <code>tput</code> [<code>-T</code><i>type</i>] <code>longname</code><br />
 <code>tput -S</code> <code>&lt;&lt;</code><br />
 <code>tput -V</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>tput</code> utility uses the <code>terminfo</code> database to make the values of terminal-dependent capabilities and information available to the shell (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)), to initialize or reset the terminal, or return the long name of the requested terminal type. The result depends upon the capability&#8217;s type:</p>
<dl>
<dt>
<dd>
<dl>
<dt>string</p>
<dd> <code>tput</code> writes the string to the standard output. No trailing newline is supplied.</p>
<dt>integer</p>
<dd> <code>tput</code> writes the decimal value to the standard output, with a trailing newline.</p>
<dt>boolean</p>
<dd> <code>tput</code> simply sets the exit code (<code>0</code> for TRUE if the terminal has the capability, <code>1</code> for FALSE if it does not), and writes nothing to the standard output.</dl>
</dl>
<p> Before using a value returned on the standard output, the application should test the exit code (e.g., <code>$?</code>, see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) to be sure it is <code>0</code>. (See the <code>EXIT CODES</code> and <code>DIAGNOSTICS</code> sections.) For a complete list of capabilities and the <i>capname</i> associated with each, see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5).</p>
<h3>Options</h3>
<dl>
<dt><code>-S</code></p>
<dd> allows more than one capability per invocation of <code>tput</code>. The capabilities must be passed to <code>tput</code> from the standard input instead of from the command line (see example). Only one <i>capname</i> is allowed per line. The <code>-S</code> option changes the meaning of the <code>0</code> and <code>1</code> boolean and string exit codes (see the EXIT CODES section).</p>
<dt>
<dd> Because some capabilities may use <i>string</i> parameters rather than <i>numbers</i>, <code>tput</code> uses a table and the presence of parameters in its input to decide whether to use <code><a href="//www.systutorials.com/docs/linux/man/3X-tparm/">tparm</a></code>(3X), and how to interpret the parameters.</p>
<dt><code>-T</code><i>type</i></p>
<dd> indicates the <i>type</i> of terminal. Normally this option is unnecessary, because the default is taken from the environment variable <code>TERM</code>. If <code>-T</code> is specified, then the shell variables <code>LINES</code> and <code>COLUMNS</code> will also be ignored.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits.</p>
<dt><code>-x</code></p>
<dd> do not attempt to clear the terminal&#8217;s scrollback buffer using the extended &#8220;E3&#8221; capability.</dl>
<h3>Commands</h3>
<p> A few commands (<code>init</code>, <code>reset</code> and <code>longname</code>) are special; they are defined by the <code>tput</code> program. The others are the names of <i>capabilities</i> from the terminal database (see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) for a list). Although <code>init</code> and <code>reset</code> resemble capability names, <code>tput</code> uses several capabilities to perform these special functions.</p>
<dl>
<dt><i>capname</i></p>
<dd> indicates the capability from the terminal database.</p>
<dt>
<dd> If the capability is a string that takes parameters, the arguments following the capability will be used as parameters for the string.</p>
<dt>
<dd> Most parameters are numbers. Only a few terminal capabilities require string parameters; <code>tput</code> uses a table to decide which to pass as strings. Normally <code>tput</code> uses <code><a href="//www.systutorials.com/docs/linux/man/3X-tparm/">tparm</a></code>(3X) to perform the substitution. If no parameters are given for the capability, <code>tput</code> writes the string without performing the substitution.</p>
<dt><code>init</code></p>
<dd> If the terminal database is present and an entry for the user&#8217;s terminal exists (see <code>-T</code><i>type</i>, above), the following will occur:</p>
<dl>
<dt>
<dd>
<dl>
<dt>(1)</p>
<dd> first, <code>tput</code> retrieves the current terminal mode settings for your terminal. It does this by successively testing</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 the standard error,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard output,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 standard input and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 ultimately &#8220;/dev/tty&#8221;</dl>
<dt>
<dd> to obtain terminal settings. Having retrieved these settings, <code>tput</code> remembers which file descriptor to use when updating settings.</p>
<dt>(2)</p>
<dd> if the window size cannot be obtained from the operating system, but the terminal description (or environment, e.g., <code>LINES</code> and <code>COLUMNS</code> variables specify this), update the operating system&#8217;s notion of the window size.</p>
<dt>(3)</p>
<dd> the terminal modes will be updated:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 any delays (e.g., newline) specified in the entry will be set in the tty driver,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 tabs expansion will be turned on or off according to the specification in the entry, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if tabs are not expanded, standard tabs will be set (every 8 spaces).</dl>
<dt>(4)</p>
<dd> if present, the terminal&#8217;s initialization strings will be output as detailed in the <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) section on <i>Tabs and Initialization</i>,</p>
<dt>(5)</p>
<dd> output is flushed.</dl>
</dl>
<dt>
<dd> If an entry does not contain the information needed for any of these activities, that activity will silently be skipped.</p>
<dt><code>reset</code></p>
<dd> This is similar to <code>init</code>, with two differences:</p>
<dl>
<dt>
<dd>
<dl>
<dt>(1)</p>
<dd> before any other initialization, the terminal modes will be reset to a &#8220;sane&#8221; state:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 set cooked and echo modes,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 turn off cbreak and raw modes,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 turn on newline translation and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 reset any unset special characters to their default values</dl>
<dt>(2)</p>
<dd> Instead of putting out <i>initialization</i> strings, the terminal&#8217;s <i>reset</i> strings will be output if present (<code>rs1</code>, <code>rs2</code>, <code>rs3</code>, <code>rf</code>). If the <i>reset</i> strings are not present, but <i>initialization</i> strings are, the <i>initialization</i> strings will be output.</dl>
</dl>
<dt>
<dd> Otherwise, <code>reset</code> acts identically to <code>init</code>.</p>
<dt><code>longname</code></p>
<dd> If the terminal database is present and an entry for the user&#8217;s terminal exists (see <code>-T</code><i>type</i> above), then the long name of the terminal will be put out. The long name is the last name in the first line of the terminal&#8217;s description in the <code>terminfo</code> database [see <code><a href="/docs/linux/man/5-term/">term</a></code>(5)].</dl>
<h3>Aliases</h3>
<p> <code>tput</code> handles the <code>clear</code>, <code>init</code> and <code>reset</code> commands specially: it allows for the possibility that it is invoked by a link with those names. </p>
<p> If <code>tput</code> is invoked by a link named <code>reset</code>, this has the same effect as <code>tput reset</code>. The <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1) utility also treats a link named <code>reset</code> specially. </p>
<p> Before ncurses 6.1, the two utilities were different from each other:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>tset</code> utility reset the terminal modes and special characters (not done with <code>tput</code>).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 On the other hand, <code>tset</code>&#8216;s repertoire of terminal capabilities for resetting the terminal was more limited, i.e., only <code>reset_1string</code>, <code>reset_2string</code> and <code>reset_file</code> in contrast to the tab-stops and margins which are set by this utility.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>reset</code> program is usually an alias for <code>tset</code>, because of this difference with resetting terminal modes and special characters. </p>
<p> With the changes made for ncurses 6.1, the <i>reset</i> feature of the two programs is (mostly) the same. A few differences remain:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>tset</code> program waits one second when resetting, in case it happens to be a hardware terminal.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The two programs write the terminal initialization strings to different streams (i.e., the standard error for <code>tset</code> and the standard output for <code>tput</code>).</p>
<dl>
<dt>
<dd> <code>Note:</code> although these programs write to different streams, redirecting their output to a file will capture only part of their actions. The changes to the terminal modes are not affected by redirecting the output.</dl>
<p> If <code>tput</code> is invoked by a link named <code>init</code>, this has the same effect as <code>tput init</code>. Again, you are less likely to use that link because another program named <code>init</code> has a more well-established use.</p>
<h3>Terminal Size</h3>
<p> Besides the special commands (e.g., <code>clear</code>), tput treats certain terminfo capabilities specially: <code>lines</code> and <code>cols</code>. tput calls <code><a href="//www.systutorials.com/docs/linux/man/3X-setupterm/">setupterm</a></code>(3X) to obtain the terminal size:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 first, it gets the size from the terminal database (which generally is not provided for terminal emulators which do not have a fixed window size)<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 then it asks the operating system for the terminal&#8217;s size (which generally works, unless connecting via a serial line which does not support <i>NAWS</i>: negotiations about window size).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 finally, it inspects the environment variables <code>LINES</code> and <code>COLUMNS</code> which may override the terminal size. </p>
<p> If the <code>-T</code> option is given tput ignores the environment variables by calling <code>use_tioctl(TRUE)</code>, relying upon the operating system (or finally, the terminal database).</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>tput init</code></p>
<dd> Initialize the terminal according to the type of terminal in the environmental variable <code>TERM</code>. This command should be included in everyone&#8217;s .profile after the environmental variable <code>TERM</code> has been exported, as illustrated on the <code><a href="/docs/linux/man/5-profile/">profile</a></code>(5) manual page.</p>
<dt><code>tput -T5620 reset</code></p>
<dd> Reset an AT&amp;T 5620 terminal, overriding the type of terminal in the environmental variable <code>TERM</code>.</p>
<dt><code>tput cup 0 0</code></p>
<dd> Send the sequence to move the cursor to row <code>0</code>, column <code>0</code> (the upper left corner of the screen, usually known as the &#8220;home&#8221; cursor position).</p>
<dt><code>tput clear</code></p>
<dd> Echo the clear-screen sequence for the current terminal.</p>
<dt><code>tput cols</code></p>
<dd> Print the number of columns for the current terminal.</p>
<dt><code>tput -T450 cols</code></p>
<dd> Print the number of columns for the 450 terminal.</p>
<dt><code>bold=`tput smso` offbold=`tput rmso`</code></p>
<dd> Set the shell variables <code>bold</code>, to begin stand-out mode sequence, and <code>offbold</code>, to end standout mode sequence, for the current terminal. This might be followed by a prompt: <code>echo &quot;${bold}Please type in your name: ${offbold}
