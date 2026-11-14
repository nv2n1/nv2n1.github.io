---
title: "resize(1)"
name: "resize"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resize/"
description: "resize – set environment and terminal settings to current xterm window size"
---

<h2 class="name">NAME</h2>
<p> resize &#8211; set environment and terminal settings to current xterm window size </p>
<h2>SYNOPSIS</h2>
<p> <code>resize</code> [ <code>-v</code> | <code>-u</code> | <code>-c</code> ] [ <code>-s</code> [ <i>row col</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Resize</i> prints a shell command for setting the appropriate environment variables to indicate the current size of <i>xterm</i> window from which the command is run. </p>
<p> <i>Resize</i> determines the command through several steps:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 first, it finds the name of the user&#8217;s shell program. It uses the <code>SHELL</code> variable if set, otherwise it uses the user&#8217;s data from /etc/passwd.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 then it decides whether to use Bourne shell syntax or C-Shell syntax. It uses a built-in table of known shells, which can be overridden by the <code>-u</code> and <code>-c</code> options.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 then <i>resize</i> asks the operating system for the terminal settings. This is the same information which can be manipulated using <i>stty</i>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 then <i>resize</i> asks the terminal for its size in characters. Depending on whether the &quot;<code>-s</code> option is given, <i>resize</i> uses a different escape sequence to ask for this information.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 at this point, <i>resize</i> attempts to update the terminal settings to reflect the terminal window&#8217;s size in pixels:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the <code>-s</code> option is used, <i>resize</i> then asks the terminal for its size in pixels.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 otherwise, <i>resize</i> asks the operating system for the information and updates that after ensuring that the window&#8217;s dimensions are a multiple of the character height and width.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 in either case, the updated terminal settings are done using a different system call than used for <i>stty</i>.</dl>
<p>&nbsp;.IP&nbsp;&bull;&nbsp;4 then <i>resize</i> updates the terminal settings to reflect any altered values such as its size in rows or columns. This affects the values shown by <i>stty</i>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 finally, <i>resize</i> generates shell commands for setting the environment variables, and writes that to the standard output.</p>
<h2>EXAMPLES</h2>
<p> For <i>resize</i>&#8216;s output to take effect, <i>resize</i> must either be evaluated as part of the command line (usually done with a shell alias or function) or else redirected to a file which can then be read in. From the C shell (usually known as <i>/bin/csh</i>), the following alias could be defined in the user&#8217;s <i>.cshrc</i>: </p>
<pre>
        %  alias rs 'set noglob; eval `resize`'
</pre>
<p> After resizing the window, the user would type: </p>
<pre>
        %  rs
</pre>
<p> Users of versions of the Bourne shell (usually known as <i>/bin/sh</i>) that don&#8217;t have command functions will need to send the output to a temporary file and then read it back in with the &#8220;.&#8221; command: </p>
<pre>
        $  resize &gt; /tmp/out
        $  .&nbsp;/tmp/out
</pre>
<h2>OPTIONS</h2>
<p> The following options may be used with <i>resize</i>:</p>
<dl>
<dt><code>-c</code></p>
<dd> This option indicates that C shell commands should be generated even if the user&#8217;s current shell does not appear to use C shell syntax.</p>
<dt><code>-s </code>[<i>rows columns</i>]</p>
<dd> This option indicates that Sun console escape sequences will be used instead of the VT100-style <i>xterm</i> escape codes. If <i>rows</i> and <i>columns</i> are given, <i>resize</i> will ask the <i>xterm</i> to resize itself using those values.</p>
<dt>
<dd> Both of the escape sequences used for this option (first to obtain the window size and second to modify it) are subject to <i>xterm</i>&#8216;s <code>allowWindowOps</code> resource setting. The window manager may also choose to disallow the change.</p>
<dt>
<dd> The VT100-style escape sequence used to determine the screen size always works for VT100-compatible terminals. VT100s have no corresponding way to modify the screensize.</p>
<dt><code>-u</code></p>
<dd> This option indicates that Bourne shell commands should be generated even if the user&#8217;s current shell does not appear to use Bourne shell syntax.</p>
<dt><code>-v</code></p>
<dd> This causes <i>resize</i> to print a version number to the standard output, and then exit.</dl>
<p> Note that the Sun console escape sequences are recognized by XFree86 <i>xterm</i> and by <i>dtterm</i>. The <i>resize</i> program may be installed as <i>sunsize</i>, which causes makes it assume the <code>-s</code> option. </p>
<p> The <i>rows</i> and <i>columns</i> arguments must appear last; though they are normally associated with the <code>-s</code> option, they are parsed separately.</p>
<h2>FILES</h2>
<dl>
<dt>/etc/termcap</p>
<dd> for the base termcap entry to modify.</p>
<dt>~/.cshrc</p>
<dd> user&#8217;s alias for the command.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>SHELL</p>
<dd> Unless overridden by the <code>-c</code> option, <i>resize</i> determines the user&#8217;s current shell by</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 first checking if <code>$SHELL</code> is set, and using that,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 otherwise <i>resize</i> looks in the password file (/etc/passwd).</dl>
<dt>
<dd> Generally Bourne-shell variants (including <i>ksh</i>) do not modify <code>$SHELL</code>, so it is possible for <i>resize</i> to be confused if one runs <i>resize</i> from a Bourne shell spawned from a C shell.</p>
<dt>
<dd> After determining the user&#8217;s shell, <i>resize</i> checks the shell&#8217;s name against a table of known shell names. If it does not find the name in its table, <i>resize</i> will use C shell syntax for the generated commands to set environment variables.</p>
<dt>TERM</p>
<dd> <i>Resize</i>&#8216;s generated shell command sets this to &quot;xterm&quot; if not already set.</p>
<dt>TERMCAP</p>
<dd> <i>Resize</i>&#8216;s generated shell command sets this variable on systems using termcap, e.g., when <i>resize</i> is linked with the <i>termcap</i> library rather than a <i>terminfo</i> library. The latter does not provide the complete text for a termcap entry.</p>
<dt>COLUMNS, LINES</p>
<dd> <i>Resize</i>&#8216;s generated shell command sets these variables on systems using terminfo. Many applications (including the curses library) use those variables when set to override their screensize.</dl>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/3x-use_env/">use_env</a>(3x)<br />
 <a href="/docs/linux/man/1-csh/">csh</a>(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/1-tset/">tset</a>(1)<br />
 <a href="/docs/linux/man/1-xterm/">xterm</a>(1)</p>
<h2>AUTHORS</h2>
<p> Mark Vandevoorde (MIT-Athena), Edward Moy (Berkeley)<br />
 Thomas Dickey (invisible-island.net).<br />
 Copyright (c) 1984, 1985 by X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a></i>(7) for a complete copyright notice. </p>
<h2>Index</h2>
