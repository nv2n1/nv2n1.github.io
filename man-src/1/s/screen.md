---
title: "screen(1)"
name: "screen"
section: "1"
letter: "s"
url: "/docs/linux/man/1-screen/"
description: "screen – screen manager with VT100/ANSI terminal emulation"
---

<h2 class="name">NAME</h2>
<p> screen &#8211; screen manager with VT100/ANSI terminal emulation </p>
<h2>SYNOPSIS</h2>
<p> <code>screen</code> [ <code>&#8211;</code><i>options</i> ] [ <i>cmd</i> [ <i>args</i> ] ]<br />
 <code>screen -r</code> [[<i>pid</i><code>.</code>]<i>tty</i>[<code>.</code><i>host</i>]]<br />
 <code>screen -r</code> <i>sessionowner</i><code>/</code>[[<i>pid</i><code>.</code>]<i>tty</i>[<code>.</code><i>host</i>]] </p>
<h2>DESCRIPTION</h2>
<p> <i>Screen</i> is a full-screen window manager that multiplexes a physical terminal between several processes (typically interactive shells). Each virtual terminal provides the functions of a DEC VT100 terminal and, in addition, several control functions from the ISO 6429 (ECMA 48, ANSI X3.64) and ISO 2022 standards (e.g. insert/delete line and support for multiple character sets). There is a scrollback history buffer for each virtual terminal and a copy-and-paste mechanism that allows moving text regions between windows. </p>
<p> When <i>screen</i> is called, it creates a single window with a shell in it (or the specified command) and then gets out of your way so that you can use the program as you normally would. Then, at any time, you can create new (full-screen) windows with other programs in them (including more shells), kill existing windows, view a list of windows, turn output logging on and off, copy-and-paste text between windows, view the scrollback history, switch between windows in whatever manner you wish, etc. All windows run their programs completely independent of each other. Programs continue to run when their window is currently not visible and even when the whole <i>screen </i> session is detached from the user&#8217;s terminal. When a program terminates, <i>screen</i> (per default) kills the window that contained it. If this window was in the foreground, the display switches to the previous window; if none are left, <i>screen</i> exits. Shells usually distinguish between running as login-shell or sub-shell. Screen runs them as sub-shells, unless told otherwise (See shell .screenrc command). </p>
<p> Everything you type is sent to the program running in the current window. The only exception to this is the one keystroke that is used to initiate a command to the window manager. By default, each command begins with a control-a (abbreviated C-a from now on), and is followed by one other keystroke. The command character and all the key bindings can be fully customized to be anything you like, though they are always two characters in length. </p>
<p> <i>Screen</i> does not understand the prefix C- to mean control, although this notation is used in this manual for readability. Please use the caret notation (^A instead of C-a) as arguments to e.g. the <i>escape</i> command or the <i>-e</i> option. <i>Screen</i> will also print out control characters in caret notation. </p>
<p> The standard way to create a new window is to type <code>C-a c</code>. This creates a new window running a shell and switches to that window immediately, regardless of the state of the process running in the current window. Similarly, you can create a new window with a custom command in it by first binding the command to a keystroke (in your .screenrc file or at the <code>C-a :</code> command line) and then using it just like the <code>C-a c</code> command. In addition, new windows can be created by running a command like:</p>
<dl>
<dt>
<dd> screen emacs prog.c</dl>
<p> from a shell prompt within a previously created window. This will not run another copy of <i>screen</i>, but will instead supply the command name and its arguments to the window manager (specified in the $STY environment variable) who will use it to create the new window. The above example would start the emacs editor (editing prog.c) and switch to its window. &#8211; Note that you cannot transport environment variables from the invoking shell to the application (emacs in this case), because it is forked from the parent screen process, not from the invoking shell. </p>
<p> If /run/utmp is writable by <i>screen</i>, an appropriate record will be written to this file for each window, and removed when the window is terminated. This is useful for working with talk, script, shutdown, rsend, sccs and other similar programs that use the utmp file to determine who you are. As long as <i>screen</i> is active on your terminal, the terminal&#8217;s own record is removed from the utmp file. See also C-a L. </p>
<h2>GETTING STARTED</h2>
<p> Before you begin to use <i>screen</i> you&#8217;ll need to make sure you have correctly selected your terminal type, just as you would for any other termcap/terminfo program. (You can do this by using <i>test</i> for example.) </p>
<p> If you&#8217;re impatient and want to get started without doing a lot more reading, you should remember this one command: <code>C-a ?</code>. Typing these two characters will display a list of the available <i>screen</i> commands and their bindings. Each keystroke is discussed in the section DEFAULT KEY BINDINGS. The manual section CUSTOMIZATION deals with the contents of your .screenrc. </p>
<p> If your terminal is a true auto-margin terminal (it doesn&#8217;t allow the last position on the screen to be updated without scrolling the screen) consider using a version of your terminal&#8217;s termcap that has automatic margins turned <i>off</i>. This will ensure an accurate and optimal update of the screen in all circumstances. Most terminals nowadays have magic margins (automatic margins plus usable last column). This is the VT100 style type and perfectly suited for <i>screen</i>. If all you&#8217;ve got is a true auto-margin terminal <i>screen</i> will be content to use it, but updating a character put into the last position on the screen may not be possible until the screen scrolls or the character is moved into a safe position in some other way. This delay can be shortened by using a terminal with insert-character capability. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> Screen has the following command-line options:</p>
<dl>
<dt><code>-a</code></p>
<dd> include <i>all</i> capabilities (with some minor exceptions) in each window&#8217;s termcap, even if <i>screen</i> must redraw parts of the display in order to implement a function.</p>
<dt><code>-A</code></p>
<dd> Adapt the sizes of all windows to the size of the current terminal. By default, <i>screen</i> tries to restore its old window sizes when attaching to resizable terminals (those with WS in its description, e.g. suncmd or some xterm).</p>
<dt><code>-c </code><i>file</i></p>
<dd> override the default configuration file from $HOME/.screenrc to <i>file</i>.</p>
<dt><code>-d</code>|<code>-D</code> [<i>pid.tty.host</i>]</p>
<dd> does not start <i>screen</i>, but detaches the elsewhere running <i>screen</i> session. It has the same effect as typing C-a d from <i>screen</i>&#8216;s controlling terminal. <code>-D</code> is the equivalent to the power detach key. If no session can be detached, this option is ignored. In combination with the <code>-r</code>/<code>-R</code> option more powerful effects can be achieved:</p>
<dt><code>-d -r</code></p>
<dd> Reattach a session and if necessary detach it first.</p>
<dt><code>-d -R</code></p>
<dd> Reattach a session and if necessary detach or even create it first.</p>
<dt><code>-d -RR</code></p>
<dd> Reattach a session and if necessary detach or create it. Use the first session if more than one session is available.</p>
<dt><code>-D -r</code></p>
<dd> Reattach a session. If necessary detach and logout remotely first.</p>
<dt><code>-D -R</code></p>
<dd> Attach here and now. In detail this means: If a session is running, then reattach. If necessary detach and logout remotely first. If it was not running create it and notify the user. This is the author&#8217;s favorite.</p>
<dt><code>-D -RR</code></p>
<dd> Attach here and now. Whatever that means, just do it.</p>
<dt>
<dd> Note: It is always a good idea to check the status of your sessions by means of screen -list.</p>
<dt><code>-e </code><i>xy</i></p>
<dd> specifies the command character to be <i>x</i> and the character generating a literal command character to <i>y</i> (when typed after the command character). The default is C-a and `a&#8217;, which can be specified as -e^Aa. When creating a <i>screen</i> session, this option sets the default command character. In a multiuser session all users added will start off with this command character. But when attaching to an already running session, this option changes only the command character of the attaching user. This option is equivalent to either the commands defescape or escape respectively.</p>
<dt><code>-f</code>, <code>-fn</code>, and <code>-fa</code></p>
<dd> turns flow-control on, off, or automatic switching mode. This can also be defined through the defflow .screenrc command.</p>
<dt><code>-h </code><i>num</i></p>
<dd> Specifies the history scrollback buffer to be <i>num</i> lines high.</p>
<dt><code>-i</code></p>
<dd> will cause the interrupt key (usually C-c) to interrupt the display immediately when flow-control is on. See the defflow .screenrc command for details. The use of this option is discouraged.</p>
<dt><code>-l</code> and <code>-ln</code></p>
<dd> turns login mode on or off (for /run/utmp updating). This can also be defined through the deflogin .screenrc command.</p>
<dt><code>-ls</code> [<i>match</i>]</p>
<dd>
<dt><code>-list</code> [<i>match</i>]</p>
<dd> does not start <i>screen</i>, but prints a list of <i>pid.tty.host</i> strings and creation timestamps identifying your <i>screen</i> sessions. Sessions marked `detached&#8217; can be resumed with screen -r. Those marked `attached&#8217; are running and have a controlling terminal. If the session runs in multiuser mode, it is marked `multi&#8217;. Sessions marked as `unreachable&#8217; either live on a different host or are `dead&#8217;. An unreachable session is considered dead, when its name matches either the name of the local host, or the specified parameter, if any. See the <code>-r</code> flag for a description how to construct matches. Sessions marked as `dead&#8217; should be thoroughly checked and removed. Ask your system administrator if you are not sure. Remove sessions with the <code>-wipe</code> option.</p>
<dt><code>-L</code></p>
<dd> tells <i>screen</i> to turn on automatic output logging for the windows.</p>
<dt><code>-Logfile </code><i>file</i></p>
<dd> By default logfile name is screenlog.0. You can set new logfile name with the -Logfile option.</p>
<dt><code>-m</code></p>
<dd> causes <i>screen</i> to ignore the $STY environment variable. With screen -m creation of a new session is enforced, regardless whether <i>screen</i> is called from within another <i>screen</i> session or not. This flag has a special meaning in connection with the `-d&#8217; option:</p>
<dt><code>-d -m</code></p>
<dd> Start <i>screen</i> in detached mode. This creates a new session but doesn&#8217;t attach to it. This is useful for system startup scripts.</p>
<dt><code>-D -m</code></p>
<dd> This also starts screen in detached mode, but doesn&#8217;t fork a new process. The command exits if the session terminates.</p>
<dt><code>-O</code></p>
<dd> selects an optimal output mode for your terminal rather than true VT100 emulation (only affects auto-margin terminals without `LP&#8217;). This can also be set in your .screenrc by specifying `OP&#8217; in a termcap command.</p>
<dt><code>-p </code><i>number_or_name|-|=|+</i></p>
<dd> Preselect a window. This is useful when you want to reattach to a specific window or you want to send a command via the -X option to a specific window. As with screen&#8217;s select command, &#8211; selects the blank window. As a special case for reattach, = brings up the windowlist on the blank window, while a + will create a new window. The command will not be executed if the specified window could not be found.</p>
<dt><code>-q</code></p>
<dd> Suppress printing of error messages. In combination with -ls the exit value is as follows: 9 indicates a directory without sessions. 10 indicates a directory with running but not attachable sessions. 11 (or more) indicates 1 (or more) usable sessions. In combination with -r the exit value is as follows: 10 indicates that there is no session to resume. 12 (or more) indicates that there are 2 (or more) sessions to resume and you should specify which one to choose. In all other cases -q has no effect.</p>
<dt><code>-Q</code></p>
<dd> Some commands now can be queried from a remote session using this flag, e.g. screen -Q windows. The commands will send the response to the stdout of the querying process. If there was an error in the command, then the querying process will exit with a non-zero status. </p>
<p> The commands that can be queried now are:<br />
&nbsp;<code>echo</code><br />
&nbsp;<code>info</code><br />
&nbsp;<code>lastmsg</code><br />
&nbsp;<code>number</code><br />
&nbsp;<code>select</code><br />
&nbsp;<code>time</code><br />
&nbsp;<code>title</code><br />
&nbsp;<code>windows</code></p>
<dt><code>-r</code> [<i>pid.tty.host</i>]</p>
<dd>
<dt><code>-r</code> <i>sessionowner/[</i><i>pid.tty.host</i>]</p>
<dd> resumes a detached <i>screen</i> session. No other options (except combinations with <code>-d</code>/<code>-D</code>) may be specified, though an optional prefix of [<i>pid.</i>]<i>tty.host</i> may be needed to distinguish between multiple detached <i>screen</i> sessions. The second form is used to connect to another user&#8217;s screen session which runs in multiuser mode. This indicates that screen should look for sessions in another user&#8217;s directory. This requires setuid-root.</p>
<dt><code>-R</code></p>
<dd> resumes screen only when it&#8217;s unambiguous which one to attach, usually when only one <i>screen</i> is detached. Otherwise lists available sessions. <code>-RR</code> attempts to resume the youngest (in terms of creation time) detached <i>screen</i> session it finds. If successful, all other command-line options are ignored. If no detached session exists, starts a new session using the specified options, just as if <code>-R</code> had not been specified. The option is set by default if <i>screen</i> is run as a login-shell (actually screen uses -xRR in that case). For combinations with the <code>-d</code>/<code>-D</code> option see there. <code>Note:</code> Time-based session selection is a Debian addition.</p>
<dt><code>-s </code><i>program</i></p>
<dd> sets the default shell to the program specified, instead of the value in the environment variable $SHELL (or /bin/sh if not defined). This can also be defined through the shell .screenrc command. See also there.</p>
<dt><code>-S </code><i>sessionname</i></p>
<dd> When creating a new session, this option can be used to specify a meaningful name for the session. This name identifies the session for screen -list and screen -r actions. It substitutes the default [<i>tty.host</i>] suffix. This name should not be longer then 80 symbols.</p>
<dt><code>-t </code><i>name</i></p>
<dd> sets the title (a.k.a.) for the default shell or specified program. See also the shelltitle .screenrc command.</p>
<dt><code>-T </code><i>term</i></p>
<dd> Set the $TERM environment variable using the specified term as opposed to the default setting of <code>screen</code>.</p>
<dt><code>-U</code></p>
<dd> Run screen in UTF-8 mode. This option tells screen that your terminal sends and understands UTF-8 encoded characters. It also sets the default encoding for new windows to `utf8&#8242;.</p>
<dt><code>-v</code></p>
<dd> Print version number.</p>
<dt><code>-wipe</code> [<i>match</i>]</p>
<dd> does the same as screen -ls, but removes destroyed sessions instead of marking them as `dead&#8217;. An unreachable session is considered dead, when its name matches either the name of the local host, or the explicitly given parameter, if any. See the <code>-r</code> flag for a description how to construct matches.</p>
<dt><code>-x</code></p>
<dd> Attach to a not detached <i>screen</i> session. (Multi display mode). <i>Screen</i> refuses to attach from within itself. But when cascading multiple screens, loops are not detected; take care.</p>
<dt><code>-X</code></p>
<dd> Send the specified command to a running screen session. You may use the <code>-S</code> option to specify the screen session if you have several screen sessions running. You can use the <code>-d</code> or <code>-r</code> option to tell screen to look only for attached or detached screen sessions. Note that this command doesn&#8217;t work if the session is password protected. </p>
<dt><code>-4</code></p>
<dd> Resolve hostnames only to IPv4 addresses.</p>
<dt><code>-6</code></p>
<dd> Resolve hostnames only to IPv6 addresses.</dl>
<h2>DEFAULT KEY BINDINGS</h2>
<p> As mentioned, each <i>screen</i> command consists of a C-a followed by one other character. For your convenience, all commands that are bound to lower-case letters are also bound to their control character counterparts (with the exception of C-a a; see below), thus, C-a c as well as C-a C-c can be used to create a window. See section CUSTOMIZATION for a description of the command. </p>
<p> The following table shows the default key bindings. The trailing commas in boxes with multiple keystroke entries are separators, not part of the bindings. </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a &#8216;</code></td>
<td>(select)</td>
<td> Prompt for a window name or number to switch to.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a &quot;</code></td>
<td>(windowlist -b)</td>
<td> Present a list of all windows for selection.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a <i>digit</i></code></td>
<td>(select 0-9)</td>
<td> Switch to window number 0 &#8211; 9
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a &#8211;</code></td>
<td>(select -)</td>
<td> Switch to window number 0 &#8211; 9, or to the blank window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a tab</code></td>
<td>(focus)</td>
<td> Switch the input focus to the next region. See also <i>split, remove, only</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a C-a</code></td>
<td>(other)</td>
<td> Toggle to the window displayed previously. Note that this binding defaults to the command character typed twice, unless overridden. For instance, if you use the option <code>-e]x</code>, this command becomes ]].
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a a </code></td>
<td>(meta)</td>
<td> Send the command character (C-a) to window. See <i>escape</i> command.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a A</code></td>
<td>(title)</td>
<td> Allow the user to enter a name for the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a b,<br />
 C-a C-b </code></td>
<td>(break)</td>
<td> Send a break to window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a B</code></td>
<td>(pow_break)</td>
<td> Reopen the terminal line and send a break.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a c,<br />
 C-a C-c </code></td>
<td>(screen)</td>
<td> Create a new window with a shell and switch to that window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a C</code></td>
<td>(clear)</td>
<td> Clear the screen.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a d,<br />
 C-a C-d </code></td>
<td>(detach)</td>
<td> Detach <i>screen</i> from this terminal.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a D D</code></td>
<td>(pow_detach)</td>
<td> Detach and logout.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a f,<br />
 C-a C-f </code></td>
<td>(flow)</td>
<td> Toggle flow <i>on</i>, <i>off</i> or <i>auto</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a F</code></td>
<td>(fit)</td>
<td> Resize the window to the current region size.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a C-g</code></td>
<td>(vbell)</td>
<td> Toggles <i>screen&#8217;s</i> visual bell mode.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a h</code></td>
<td>(hardcopy)</td>
<td> Write a hardcopy of the current window to the file hardcopy.<i>n</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a H</code></td>
<td>(log)</td>
<td> Begins/ends logging of the current window to the file screenlog.<i>n</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a i,<br />
 C-a C-i </code></td>
<td>(info)</td>
<td> Show info about this window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a k,<br />
 C-a C-k </code></td>
<td>(kill)</td>
<td> Destroy current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a l,<br />
 C-a C-l </code></td>
<td>(redisplay)</td>
<td> Fully refresh current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a L</code></td>
<td>(login)</td>
<td> Toggle this windows login slot. Available only if <i>screen</i> is configured to update the utmp database.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a m,<br />
 C-a C-m </code></td>
<td>(lastmsg)</td>
<td> Repeat the last message displayed in the message line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a M</code></td>
<td>(monitor)</td>
<td> Toggles monitoring of the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a space,<br />
 C-a n,<br />
 C-a C-n </code></td>
<td>(next)</td>
<td> Switch to the next window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a N</code></td>
<td>(number)</td>
<td> Show the number (and title) of the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a backspace,<br />
 C-a C-h,<br />
 C-a p,<br />
 C-a C-p </code></td>
<td>(prev)</td>
<td> Switch to the previous window (opposite of <code>C-a n</code>).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a q,<br />
 C-a C-q </code></td>
<td>(xon)</td>
<td> Send a control-q to the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a Q</code></td>
<td>(only)</td>
<td> Delete all regions but the current one. See also <i>split, remove, focus</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a r,<br />
 C-a C-r </code></td>
<td>(wrap)</td>
<td> Toggle the current window&#8217;s line-wrap setting (turn the current window&#8217;s automatic margins on and off).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a s,<br />
 C-a C-s; </code></td>
<td>(xoff)</td>
<td> Send a control-s to the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a S</code></td>
<td>(split)</td>
<td> Split the current region horizontally into two new ones. See also <i>only, remove, focus</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a t,<br />
 C-a C-t </code></td>
<td>(time)</td>
<td> Show system information.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a v</code></td>
<td>(version)</td>
<td> Display the version and compilation date.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a C-v</code></td>
<td>(digraph)</td>
<td> Enter digraph.
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a w,<br />
 C-a C-w </code></td>
<td>(windows)</td>
<td> Show a list of window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a W</code></td>
<td>(width)</td>
<td> Toggle 80/132 columns.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a x or C-a C-x</code></td>
<td>(lockscreen)</td>
<td> Lock this terminal.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a X </code></td>
<td>(remove)</td>
<td> Kill the current region. See also <i>split, only, focus</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a z,<br />
 C-a C-z </code></td>
<td>(suspend)</td>
<td> Suspend <i>screen</i>. Your system must support BSD-style job-control.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a Z</code></td>
<td>(reset)</td>
<td> Reset the virtual terminal to its power-on values.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a .</code></td>
<td>(dumptermcap)</td>
<td> Write out a .termcap file.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a ?</code></td>
<td>(help)</td>
<td> Show key bindings.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a \</code></td>
<td>(quit)</td>
<td> Kill all windows and terminate <i>screen</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a :</code></td>
<td>(colon)</td>
<td> Enter command line mode.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a [,<br />
 C-a C-[,<br />
 C-a esc </code></td>
<td>(copy)</td>
<td> Enter copy/scrollback mode.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a C-],<br />
 C-a ] </code></td>
<td>(paste .)</td>
<td> Write the contents of the paste buffer to the stdin queue of the current window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> C-a {,<br />
 C-a } </code></td>
<td>(history)</td>
<td> Copy and paste a previous (command) line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a &gt;</code></td>
<td>(writebuf)</td>
<td> Write paste buffer to a file.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a &lt;</code></td>
<td>(readbuf)</td>
<td> Reads the screen-exchange file into the paste buffer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a =</code></td>
<td>(removebuf)</td>
<td> Removes the file used by <code>C-a &lt;</code> and C-a &gt;.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a ,</code></td>
<td>(license)</td>
<td> Shows where <i>screen</i> comes from, where it went to and why you can use it.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a _</code></td>
<td>(silence)</td>
<td> Start/stop monitoring the current window for inactivity.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a |</code></td>
<td>(split -v)</td>
<td> Split the current region vertically into two new ones.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a *</code></td>
<td>(displays)</td>
<td> Show a listing of all currently attached displays.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<h2>CUSTOMIZATION</h2>
<p> The socket directory defaults either to $HOME/.screen or simply to /tmp/screens or preferably to /run/screen chosen at compile-time. If <i>screen</i> is installed setuid-root, then the administrator should compile <i>screen</i> with an adequate (not NFS mounted) socket directory. If <i>screen</i> is not running setuid-root, the user can specify any mode 700 directory in the environment variable $SCREENDIR. </p>
<p> When <i>screen</i> is invoked, it executes initialization commands from the files /etc/screenrc and .screenrc in the user&#8217;s home directory. These are the programmer&#8217;s defaults that can be overridden in the following ways: for the global screenrc file <i>screen</i> searches for the environment variable $SYSSCREENRC (this override feature may be disabled at compile-time). The user specific screenrc file is searched in $SCREENRC, then $HOME/.screenrc. The command line option <code>-c</code> takes precedence over the above user screenrc files. </p>
<p> Commands in these files are used to set options, bind functions to keys, and to automatically establish one or more windows at the beginning of your <i>screen</i> session. Commands are listed one per line, with empty lines being ignored. A command&#8217;s arguments are separated by tabs or spaces, and may be surrounded by single or double quotes. A `#&#8217; turns the rest of the line into a comment, except in quotes. Unintelligible lines are warned about and ignored. Commands may contain references to environment variables. The syntax is the shell-like &quot;$VAR &quot; or &quot;${VAR}&quot;. Note that this causes incompatibility with previous <i>screen</i> versions, as now the &#8216;$&#8217;-character has to be protected with &#8216;\&#8217; if no variable substitution shall be performed. A string in single-quotes is also protected from variable substitution. </p>
<p> Two configuration files are shipped as examples with your screen distribution: etc/screenrc and etc/etcscreenrc. They contain a number of useful examples for various commands. </p>
<p> Customization can also be done &#8216;on-line&#8217;. To enter the command mode type `C-a :&#8217;. Note that commands starting with def change default values, while others change current settings. </p>
<p> The following commands are available:</p>
<dl>
<dt><code>acladd</code><i> usernames </i>[<i>crypted-pw</i>]</p>
<dd>
<dt><code>addacl</code><i> usernames</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Enable users to fully access this screen session. <i>Usernames</i> can be one user or a comma separated list of users. This command enables to attach to the <i>screen</i> session and performs the equivalent of `aclchg <i>usernames</i> +rwx &quot;#?&quot;&#8217;. executed. To add a user with restricted access, use the `aclchg&#8217; command below. If an optional second parameter is supplied, it should be a crypted password for the named user(s). `Addacl&#8217; is a synonym to `acladd&#8217;. Multi user mode only.</dl>
<dt><code>aclchg</code><i> usernames permbits list</i></p>
<dd>
<dt><code>chacl</code><i> usernames permbits list</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Change permissions for a comma separated list of users. Permission bits are represented as `r&#8217;, `w&#8217; and `x&#8217;. Prefixing `+&#8217; grants the permission, `-&#8216; removes it. The third parameter is a comma separated list of commands and/or windows (specified either by number or title). The special list `#&#8217; refers to all windows, `?&#8217; to all commands. if <i>usernames</i> consists of a single `*&#8217;, all known users are affected. </p>
<p> A command can be executed when the user has the `x&#8217; bit for it. The user can type input to a window when he has its `w&#8217; bit set and no other user obtains a writelock for this window. Other bits are currently ignored. To withdraw the writelock from another user in window 2: `aclchg <i>username</i> -w+w 2&#8242;. To allow read-only access to the session: `aclchg <i>username</i> -w &quot;#&quot;&#8217;. As soon as a user&#8217;s name is known to <i>screen </i> he can attach to the session and (per default) has full permissions for all command and windows. Execution permission for the acl commands, `at&#8217; and others should also be removed or the user may be able to regain write permission. Rights of the special username <code>nobody</code> cannot be changed (see the su command). `Chacl&#8217; is a synonym to `aclchg&#8217;. Multi user mode only.</dl>
<dt><code>acldel</code><i> username</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Remove a user from <i>screen</i>&#8216;s access control list. If currently attached, all the user&#8217;s displays are detached from the session. He cannot attach again. Multi user mode only.</dl>
<dt><code>aclgrp</code><i> username </i>[<i>groupname</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Creates groups of users that share common access rights. The name of the group is the username of the group leader. Each member of the group inherits the permissions that are granted to the group leader. That means, if a user fails an access check, another check is made for the group leader. A user is removed from all groups the special value none is used for <i>groupname</i>. If the second parameter is omitted all groups the user is in are listed.</dl>
<dt><code>aclumask</code> [[ <i>users</i> ] <i>+bits</i> | [ <i>users</i> ] <i>-bits&#8230;</i> ]</p>
<dd>
<dt><code>umask</code> [[ <i>users</i> ] <i>+bits</i> | [ <i>users</i> ] <i>-bits&#8230;</i> ]</p>
<dd>
<dl>
<dt>
<dd>
<p> This specifies the access other users have to windows that will be created by the caller of the command. <i>Users</i> may be no, one or a comma separated list of known usernames. If no users are specified, a list of all currently known users is assumed. <i>Bits</i> is any combination of access control bits allowed defined with the aclchg command. The special username ? predefines the access that not yet known users will be granted to any window initially. The special username ?? predefines the access that not yet known users are granted to any command. Rights of the special username <code>nobody</code> cannot be changed (see the su command). `Umask&#8217; is a synonym to `aclumask&#8217;.</dl>
<dt><code>activity</code><i> message</i></p>
<dd>
<dl>
<dt>
<dd>
<p> When any activity occurs in a background window that is being monitored, <i>screen</i> displays a notification in the message line. The notification message can be re-defined by means of the activity command. Each occurrence of `%&#8217; in <i>message</i> is replaced by the number of the window in which activity has occurred, and each occurrence of `^G&#8217; is replaced by the definition for bell in your termcap (usually an audible bell). The default message is </p>
<pre>
            'Activity in window %n'
</pre>
<p> Note that monitoring is off for all windows by default, but can be altered by use of the monitor command (C-a M).</dl>
<dt><code>allpartial [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> If set to on, only the current cursor line is refreshed on window change. This affects all windows and is useful for slow terminal lines. The previous setting of full/partial refresh for each window is restored with allpartial off. This is a global flag that immediately takes effect on all windows overriding the partial settings. It does not change the default redraw behavior of newly created windows.</dl>
<dt><code>altscreen [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> If set to on, &quot;alternate screen&quot; support is enabled in virtual terminals, just like in xterm. Initial setting is `off&#8217;.</dl>
<dt><code>at </code>[<i>identifier</i>][<code>#</code>|*|%] command <code>[</code><i>args</i><code> &#8230; ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Execute a command at other displays or windows as if it had been entered there. At changes the context (the `current window&#8217; or `current display&#8217; setting) of the command. If the first parameter describes a non-unique context, the command will be executed multiple times. If the first parameter is of the form `<i>identifier</i>*&#8217; then identifier is matched against user names. The command is executed once for each display of the selected user(s). If the first parameter is of the form `<i>identifier</i>%&#8217; identifier is matched against displays. Displays are named after the ttys they attach. The prefix `/dev/&#8217; or `/dev/tty&#8217; may be omitted from the identifier. If <i>identifier</i> has a `#&#8217; or nothing appended it is matched against window numbers and titles. Omitting an identifier in front of the `#&#8217;, `*&#8217; or `%&#8217;-character selects all users, displays or windows because a prefix-match is performed. Note that on the affected display(s) a short message will describe what happened. Permission is checked for initiator of the at command, not for the owners of the affected display(s). Note that the &#8216;#&#8217; character works as a comment introducer when it is preceded by whitespace. This can be escaped by prefixing a &#8216;\&#8217;. Permission is checked for the initiator of the at command, not for the owners of the affected display(s). </p>
<p> Caveat: When matching against windows, the command is executed at least once per window. Commands that change the internal arrangement of windows (like other) may be called again. In shared windows the command will be repeated for each attached display. Beware, when issuing toggle commands like login! Some commands (e.g. process) require that a display is associated with the target windows. These commands may not work correctly under at looping over windows.</dl>
<dt><code>attrcolor </code><i>attrib </i>[<i>attribute/color-modifier</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command can be used to highlight attributes by changing the color of the text. If the attribute <i>attrib</i> is in use, the specified attribute/color modifier is also applied. If no modifier is given, the current one is deleted. See the STRING ESCAPES chapter for the syntax of the modifier. Screen understands two pseudo-attributes, i stands for high-intensity foreground color and I for high-intensity background color. </p>
<p> Examples:</p>
<dl>
<dt>
<dd> attrcolor b &quot;R&quot;</dl>
<p> Change the color to bright red if bold text is to be printed.</p>
<dl>
<dt>
<dd> attrcolor u &quot;-u b&quot;</dl>
<p> Use blue text instead of underline.</p>
<dl>
<dt>
<dd> attrcolor b &quot;.I&quot;</dl>
<p> Use bright colors for bold text. Most terminal emulators do this already.</p>
<dl>
<dt>
<dd> attrcolor i &quot;+b&quot;</dl>
<p> Make bright colored text also bold.</dl>
<dt><code>autodetach [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sets whether <i>screen</i> will automatically detach upon hangup, which saves all your running programs until they are resumed with a <code>screen -r</code> command. When turned off, a hangup signal will terminate <i>screen</i> and all the processes it contains. Autodetach is on by default.</dl>
<dt><code>autonuke [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sets whether a clear screen sequence should nuke all the output that has not been written to the terminal. See also obuflimit.</dl>
<dt><code>backtick </code><i>id lifespan autorefresh cmd args&#8230;</i></p>
<dd>
<dt><code>backtick </code><i>id</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Program the backtick command with the numerical id <i>id</i>. The output of such a command is used for substitution of the %` string escape. The specified <i>lifespan</i> is the number of seconds the output is considered valid. After this time, the command is run again if a corresponding string escape is encountered. The <i>autorefresh</i> parameter triggers an automatic refresh for caption and hardstatus strings after the specified number of seconds. Only the last line of output is used for substitution. </p>
<p> If both the <i>lifespan</i> and the <i>autorefresh</i> parameters are zero, the backtick program is expected to stay in the background and generate output once in a while. In this case, the command is executed right away and screen stores the last line of output. If a new line gets printed screen will automatically refresh the hardstatus or the captions. </p>
<p> The second form of the command deletes the backtick command with the numerical id <i>id</i>.</dl>
<dt><code>bce [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change background-color-erase setting. If bce is set to on, all characters cleared by an erase/insert/scroll/clear operation will be displayed in the current background color. Otherwise the default background color is used.</dl>
<dt><code>bell_msg </code>[<i>message</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> When a bell character is sent to a background window, <i>screen</i> displays a notification in the message line. The notification message can be re-defined by this command. Each occurrence of `%&#8217; in <i>message</i> is replaced by the number of the window to which a bell has been sent, and each occurrence of `^G&#8217; is replaced by the definition for bell in your termcap (usually an audible bell). The default message is </p>
<pre>
            'Bell in window %n'
</pre>
<p> An empty message can be supplied to the bell_msg command to suppress output of a message line (bell_msg &quot;&quot;). Without parameter, the current message is shown.</dl>
<dt><code>bind </code>[<i>class</i>]<i>key</i> [<i>command</i> [<i>args</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Bind a command to a key. By default, most of the commands provided by <i>screen</i> are bound to one or more keys as indicated in the DEFAULT KEY BINDINGS section, e.g. the command to create a new window is bound to C-c and c. The bind command can be used to redefine the key bindings and to define new bindings. The <i>key</i> argument is either a single character, a two-character sequence of the form ^x (meaning C-x), a backslash followed by an octal number (specifying the ASCII code of the character), or a backslash followed by a second character, such as \^ or \. The argument can also be quoted, if you like. If no further argument is given, any previously established binding for this key is removed. The <i>command</i> argument can be any command listed in this section. </p>
<p> If a command class is specified via the -c option, the key is bound for the specified class. Use the command command to activate a class. Command classes can be used to create multiple command keys or multi-character bindings. </p>
<p> Some examples: </p>
<pre>
            bind ' ' windows
            bind ^k
            bind k
            bind K kill
            bind ^f screen telnet foobar
            bind  screen -ln -t root -h 1000 9 su
</pre>
<p> would bind the space key to the command that displays a list of windows (so that the command usually invoked by C-a C-w would also be available as C-a space). The next three lines remove the default kill binding from C-a C-k and C-a k. C-a K is then bound to the kill command. Then it binds C-f to the command create a window with a TELNET connection to foobar, and bind escape to the command that creates an non-login window with a.k.a. root in slot #9, with a superuser shell and a scrollback buffer of 1000 lines. </p>
<pre>
            bind -c demo1 0 select 10
            bind -c demo1 1 select 11
            bind -c demo1 2 select 12
            bindkey &quot;^B&quot; command -c demo1
</pre>
<p> makes C-b 0 select window 10, C-b 1 window 11, etc. </p>
<pre>
            bind -c demo2 0 select 10
            bind -c demo2 1 select 11
            bind -c demo2 2 select 12
            bind - command -c demo2
</pre>
<p> makes C-a &#8211; 0 select window 10, C-a &#8211; 1 window 11, etc.</dl>
<dt><code>bindkey </code>[<code>-d</code>] [<code>-m</code>] [<code>-a</code>] [[<code>-k</code>|<code>-t</code>]<i>string</i> [<i>cmd-args</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command manages screen&#8217;s input translation tables. Every entry in one of the tables tells screen how to react if a certain sequence of characters is encountered. There are three tables: one that should contain actions programmed by the user, one for the default actions used for terminal emulation and one for screen&#8217;s copy mode to do cursor movement. See section INPUT TRANSLATION for a list of default key bindings. </p>
<p> If the <code>-d</code> option is given, bindkey modifies the default table, <code>-m</code> changes the copy mode table and with neither option the user table is selected. The argument <i>string</i> is the sequence of characters to which an action is bound. This can either be a fixed string or a termcap keyboard capability name (selectable with the <code>-k</code> option). </p>
<p> Some keys on a VT100 terminal can send a different string if application mode is turned on (e.g the cursor keys). Such keys have two entries in the translation table. You can select the application mode entry by specifying the <code>-a</code> option. </p>
<p> The <code>-t</code> option tells screen not to do inter-character timing. One cannot turn off the timing if a termcap capability is used. </p>
<p> <i>Cmd</i> can be any of screen&#8217;s commands with an arbitrary number of <i>args</i>. If <i>cmd</i> is omitted the key-binding is removed from the table. </p>
<p> Here are some examples of keyboard bindings: </p>
<pre>
        bindkey -d
</pre>
<p> Show all of the default key bindings. The application mode entries are marked with [A]. </p>
<pre>
        bindkey -k k1 select 1
</pre>
<p> Make the &quot;F1&quot; key switch to window one. </p>
<pre>
        bindkey -t foo stuff barfoo
</pre>
<p> Make &quot;foo&quot; an abbreviation of the word &quot;barfoo&quot;. Timeout is disabled so that users can type slowly. </p>
<pre>
        bindkey &quot;&quot; mapdefault
</pre>
<p> This key-binding makes ^T an escape character for key-bindings. If you did the above stuff barfoo binding, you can enter the word foo by typing ^Tfoo. If you want to insert a ^T you have to press the key twice (i.e., escape the escape binding). </p>
<pre>
        bindkey -k F1 command
</pre>
<p> Make the F11 (not F1!) key an alternative screen escape (besides ^A).</dl>
<dt><code>break </code>[<i>duration</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Send a break signal for <i>duration</i>*0.25 seconds to this window. For non-Posix systems the time interval may be rounded up to full seconds. Most useful if a character device is attached to the window rather than a shell process (See also chapter WINDOW TYPES). The maximum duration of a break signal is limited to 15 seconds.</dl>
<dt><code>blanker</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Activate the screen blanker. First the screen is cleared. If no blanker program is defined, the cursor is turned off, otherwise, the program is started and it&#8217;s output is written to the screen. The screen blanker is killed with the first keypress, the read key is discarded. </p>
<p> This command is normally used together with the idle command.</dl>
<dt><i></i><code>blankerprg</code> [<i>program-args</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Defines a blanker program. Disables the blanker program if an empty argument is given. Shows the currently set blanker program if no arguments are given.</dl>
<dt><i></i><code>breaktype</code> [<i>tcsendbreak</i>|<i>TIOCSBRK</i>|<i>TCSBRK</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Choose one of the available methods of generating a break signal for terminal devices. This command should affect the current window only. But it still behaves identical to defbreaktype. This will be changed in the future. Calling breaktype with no parameter displays the break method for the current window.</dl>
<dt><i></i><code>bufferfile</code> [<i>exchange-file</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change the filename used for reading and writing with the paste buffer. If the optional argument to the bufferfile command is omitted, the default setting (/tmp/screen-exchange) is reactivated. The following example will paste the system&#8217;s password file into the <i>screen</i> window (using the paste buffer, where a copy remains): </p>
<pre>
            C-a : bufferfile /etc/passwd
            C-a &lt; C-a ]
            C-a : bufferfile
</pre>
<p> <code>bumpleft</code> </p>
<p> Swaps window with previous one on window list.</dl>
<dt><code>bumpright</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Swaps window with next one on window list.</dl>
<dt><code>c1 [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change c1 code processing. <code>C1 on</code> tells screen to treat the input characters between 128 and 159 as control functions. Such an 8-bit code is normally the same as ESC followed by the corresponding 7-bit code. The default setting is to process c1 codes and can be changed with the defc1 command. Users with fonts that have usable characters in the c1 positions may want to turn this off.</dl>
<dt><code>caption [ top | bottom ] always</code>|<code>splitonly</code>[<code>string</code>]</p>
<dd>
<dt><i></i><code>caption string</code> [<i>string</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command controls the display of the window captions. Normally a caption is only used if more than one window is shown on the display (split screen mode). But if the type is set to <code>always</code> screen shows a caption even if only one window is displayed. The default is <code>splitonly</code>. </p>
<p> The second form changes the text used for the caption. You can use all escapes from the STRING ESCAPES chapter. Screen uses a default of `%3n %t&#8217;. </p>
<p> You can mix both forms by providing a string as an additional argument. </p>
<p> You can have the caption displayed either at the top or bottom of the window. The default is <code>bottom</code>.</dl>
<dt><code>charset </code><i>set</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Change the current character set slot designation and charset mapping. The first four character of <i>set</i> are treated as charset designators while the fifth and sixth character must be in range &#8216;0&#8217; to &#8216;3&#8217; and set the GL/GR charset mapping. On every position a &#8216;.&#8217; may be used to indicate that the corresponding charset/mapping should not be changed (<i>set</i> is padded to six characters internally by appending &#8216;.&#8217; chars). New windows have &quot;BBBB02&quot; as default charset, unless a encoding command is active.<br />
 The current setting can be viewed with the info command.</dl>
<dt><i></i><code>chdir</code> [<i>directory</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change the <i>current directory</i> of <i>screen</i> to the specified directory or, if called without an argument, to your home directory (the value of the environment variable $HOME). All windows that are created by means of the screen command from within .screenrc or by means of C-a : screen &#8230; or C-a c use this as their default directory. Without a chdir command, this would be the directory from which <i>screen</i> was invoked. </p>
<p> Hardcopy and log files are always written to the <i>window&#8217;s</i> default directory, <i>not</i> the current directory of the process running in the window. You can use this command multiple times in your .screenrc to start various windows in different default directories, but the last chdir value will affect all the windows you create interactively.</dl>
<dt><code>cjkwidth [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Treat ambiguous width characters as full/half width.</dl>
<dt><code>clear</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Clears the current window and saves its image to the scrollback buffer.</dl>
<dt><code>collapse</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Reorders window on window list, removing number gaps between them.</dl>
<dt><i></i><code>colon </code>[<i>prefix</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Allows you to enter .screenrc command lines. Useful for on-the-fly modification of key bindings, specific window creation and changing settings. Note that the set keyword no longer exists! Usually commands affect the current window rather than default settings for future windows. Change defaults with commands starting with &#8216;def&#8230;&#8217;. </p>
<p> If you consider this as the `Ex command mode&#8217; of <i>screen</i>, you may regard C-a esc (copy mode) as its `Vi command mode&#8217;.</dl>
<dt><code>command [ -c </code><i>class</i> ]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command has the same effect as typing the screen escape character (^A). It is probably only useful for key bindings. If the -c option is given, select the specified command class. See also bind and bindkey.</dl>
<dt><code>compacthist [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> This tells screen whether to suppress trailing blank lines when scrolling up text into the history buffer.</dl>
<dt><code>console [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Grabs or un-grabs the machines console output to a window. <i>Note</i>: Only the owner of /dev/console can grab the console output. This command is only available if the machine supports the ioctl TIOCCONS.</dl>
<dt><code>copy</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Enter copy/scrollback mode. This allows you to copy text from the current window and its history into the paste buffer. In this mode a vi-like `full screen editor&#8217; is active:<br />
 The editor&#8217;s movement keys are: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>h</code>, <code>C-h</code>,<br />
 <code>left arrow</code> </td>
<td>move the cursor left.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>j</code>, <code>C-n</code>,<br />
 <code>down arrow</code> </td>
<td>move the cursor down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>k</code>, <code>C-p</code>,<br />
 <code>up arrow</code> </td>
<td>move the cursor up.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>l</code> (&#8216;el&#8217;),<br />
 <code>right arrow</code> </td>
<td>move the cursor right.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>0</code> (zero) <code>C-a</code></td>
<td>move to the leftmost column.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>+</code> and <code>&#8211;</code></td>
<td>positions one line up and down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>H</code>, <code>M</code> and <code>L</code></td>
<td> move the cursor to the leftmost column of the top, center or bottom line of the window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>|</code></td>
<td>moves to the specified absolute column.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>g</code> or <code>home</code></td>
<td>moves to the beginning of the buffer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>G</code> or <code>end</code></td>
<td> moves to the specified absolute line (default: end of buffer).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>%</code></td>
<td>jumps to the specified percentage of the buffer.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>^</code> or <code>$</code></td>
<td> move to the leftmost column, to the first or last non-whitespace character on the line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>w</code>, <code>b</code>, and <code>e</code></td>
<td>move the cursor word by word.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>B</code>, <code>E</code></td>
<td>move the cursor WORD by WORD (as in vi).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>f/F</code>, <code>t/T</code></td>
<td> move the cursor forward/backward to the next occurrence of the target. (eg, &#8216;3fy&#8217; will move the cursor to the 3rd &#8216;y&#8217; to the right.)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>;</code> and <code>,</code></td>
<td> Repeat the last f/F/t/T command in the same/opposite direction.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-e</code> and <code>C-y</code></td>
<td> scroll the display up/down by one line while preserving the cursor position.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-u</code> and <code>C-d</code></td>
<td> scroll the display up/down by the specified amount of lines while preserving the cursor position. (Default: half screen-full).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-b</code> and <code>C-f</code></td>
<td>scroll the display up/down a full screen.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p> Note: Emacs style movement keys can be customized by a .screenrc command. (E.g. markkeys &quot;h=^B:l=^F:$=^E&quot;) There is no simple method for a full emacs-style keymap, as this involves multi-character codes. </p>
<p> Some keys are defined to do mark and replace operations. </p>
<p> The copy range is specified by setting two marks. The text between these marks will be highlighted. Press:</p>
<dl>
<dt>
<dd> <code>space</code> or <code>enter</code> to set the first or second mark respectively. If <code>mousetrack</code> is set to `on&#8217;, marks can also be set using left mouse click.</dl>
<dl>
<dt>
<dd> <code>Y</code> and <code>y</code> used to mark one whole line or to mark from start of line.</p>
<dt>
<dd> <code>W</code> marks exactly one word.</dl>
<p> Any of these commands can be prefixed with a repeat count number by pressing digits</p>
<dl>
<dt>
<dd> <code>0</code>..<code>9</code> which is taken as a repeat count.</dl>
<p> Example: C-a C-[ H 10 j 5 Y will copy lines 11 to 15 into the paste buffer. </p>
<p> The following search keys are defined:</p>
<dl>
<dt>
<dd> <code>/</code> <i>Vi</i>-like search forward.</p>
<dt>
<dd> <code>?</code> <i>Vi</i>-like search backward.</p>
<dt>
<dd> <code>C-a s</code> <i>Emacs</i> style incremental search forward.</p>
<dt>
<dd> <code>C-r</code> <i>Emacs</i> style reverse i-search.</p>
<dt>
<dd> <code>n</code> Find next search pattern.</p>
<dt>
<dd> <code>N</code> Find previous search pattern. </p>
</dl>
<p> There are however some keys that act differently than in <i>vi</i>. <i>Vi</i> does not allow one to yank rectangular blocks of text, but <i>screen</i> does. Press: <code>c</code> or <code>C</code> to set the left or right margin respectively. If no repeat count is given, both default to the current cursor position. </p>
<p> Example: Try this on a rather full text screen: </p>
<dl>
<dt>
<dd> C-a [ M 20 l SPACE c 10 l 5 j C SPACE.</dl>
<p> This moves one to the middle line of the screen, moves in 20 columns left, marks the beginning of the paste buffer, sets the left column, moves 5 columns down, sets the right column, and then marks the end of the paste buffer. Now try: </p>
<dl>
<dt>
<dd> C-a [ M 20 l SPACE 10 l 5 j SPACE</dl>
<p> and notice the difference in the amount of text copied. </p>
<p> <code>J</code> joins lines. It toggles between 4 modes: lines separated by a newline character (012), lines glued seamless, lines separated by a single whitespace and comma separated lines. Note that you can prepend the newline character with a carriage return character, by issuing a crlf on. </p>
<p> <code>v</code> or <code>V</code> is for all the <i>vi </i> users with :set numbers &#8211; it toggles the left margin between column 9 and 1. Press </p>
<p> <code>a</code> before the final space key to toggle in append mode. Thus the contents of the paste buffer will not be overwritten, but is appended to. </p>
<p> <code>A</code> toggles in append mode and sets a (second) mark. </p>
<p> <code>&gt;</code> sets the (second) mark and writes the contents of the paste buffer to the screen-exchange file (/tmp/screen-exchange per default) once copy-mode is finished. </p>
<p> This example demonstrates how to dump the whole scrollback buffer to that file: C-A [ g SPACE G $ &gt;. </p>
<p> <code>C-g</code> gives information about the current line and column. </p>
<p> <code>x</code> or <code>o</code> exchanges the first mark and the current cursor position. You can use this to adjust an already placed mark. </p>
<p> <code>C-l</code> (&#8216;el&#8217;) will redraw the screen. </p>
<p> <code>@</code> does nothing. Does not even exit copy mode. </p>
<p> All keys not described here exit copy mode.</dl>
<dt><i></i><code>copy_reg </code>[<i>key</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> No longer exists, use readreg instead.</dl>
<dt><code>crlf [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> This affects the copying of text regions with the `C-a [&#8216; command. If it is set to `on&#8217;, lines will be separated by the two character sequence `CR&#8217; &#8211; `LF&#8217;. Otherwise (default) only `LF&#8217; is used. When no parameter is given, the state is toggled.</dl>
<dt><code>debug [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Turns runtime debugging on or off. If <i>screen</i> has been compiled with option -DDEBUG debugging available and is turned on per default. Note that this command only affects debugging output from the main SCREEN process correctly. Debug output from attacher processes can only be turned off once and forever.</dl>
<dt><code>defc1 [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>c1</code> command except that the default setting for new windows is changed. Initial setting is `on&#8217;.</dl>
<dt><code>defautonuke [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>autonuke</code> command except that the default setting for new displays is changed. Initial setting is `off&#8217;. Note that you can use the special `AN&#8217; terminal capability if you want to have a dependency on the terminal type.</dl>
<dt><code>defbce [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>bce</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><i></i><code>defbreaktype</code> [<i>tcsendbreak</i>|<i>TIOCSBRK</i>|<i>TCSBRK</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Choose one of the available methods of generating a break signal for terminal devices. The preferred methods are <i>tcsendbreak</i> and <i>TIOCSBRK</i>. The third, <i>TCSBRK</i>, blocks the complete <i>screen</i> session for the duration of the break, but it may be the only way to generate long breaks. <i>Tcsendbreak</i> and <i>TIOCSBRK</i> may or may not produce long breaks with spikes (e.g. 4 per second). This is not only system-dependent, this also differs between serial board drivers. Calling defbreaktype with no parameter displays the current setting.</dl>
<dt><code>defcharset </code>[<i>set</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Like the <code>charset</code> command except that the default setting for new windows is changed. Shows current default if called without argument.</dl>
<dt><code>defdynamictitle [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Set default behaviour for new windows regarding if screen should change window title when seeing proper escape sequence. See also &quot;TITLES (naming windows)&quot; section.</dl>
<dt><code>defescape </code><i>xy</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the default command characters. This is equivalent to the escape except that it is useful multiuser sessions only. In a multiuser session escape changes the command character of the calling user, where defescape changes the default command characters for users that will be added later.</dl>
<dt><code>defflow [ on | off | auto [ interrupt ]]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>flow</code> command except that the default setting for new windows is changed. Initial setting is `auto&#8217;. Specifying <code>defflow auto interrupt</code> is the same as the command-line options <code>-fa</code> and <code>-i</code>.</dl>
<dt><code>defgr [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>gr</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><code>defhstatus </code>[<i>status</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> The hardstatus line that all new windows will get is set to <i>status</i>. This command is useful to make the hardstatus of every window display the window number or title or the like. <i>Status</i> may contain the same directives as in the window messages, but the directive escape character is &#8216;^E&#8217; (octal 005) instead of &#8216;%&#8217;. This was done to make a misinterpretation of program generated hardstatus lines impossible. If the parameter <i>status</i> is omitted, the current default string is displayed. Per default the hardstatus line of new windows is empty.</dl>
<dt><code>defencoding </code><i>enc</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>encoding</code> command except that the default setting for new windows is changed. Initial setting is the encoding taken from the terminal.</dl>
<dt><code>deflog [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>log</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><code>deflogin [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>login</code> command except that the default setting for new windows is changed. This is initialized with `on&#8217; as distributed (see config.h.in).</dl>
<dt><code>defmode </code><i>mode</i></p>
<dd>
<dl>
<dt>
<dd>
<p> The mode of each newly allocated pseudo-tty is set to <i>mode</i>. <i>Mode</i> is an octal number. When no defmode command is given, mode 0622 is used.</dl>
<dt><code>defmonitor [ on | off]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>monitor</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><code>defmousetrack [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>mousetrack</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><code>defnonblock [ on | off | </code><i>numsecs</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>nonblock</code> command except that the default setting for displays is changed. Initial setting is `off&#8217;.</dl>
<dt><code>defobuflimit </code><i>limit</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>obuflimit</code> command except that the default setting for new displays is changed. Initial setting is 256 bytes. Note that you can use the special &#8216;OL&#8217; terminal capability if you want to have a dependency on the terminal type.</dl>
<dt><code>defscrollback </code><i>num</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>scrollback</code> command except that the default setting for new windows is changed. Initial setting is 100.</dl>
<dt><code>defshell </code><i>command</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Synonym to the <code>shell</code> .screenrc command. See there.</dl>
<dt><code>defsilence [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>silence</code> command except that the default setting for new windows is changed. Initial setting is `off&#8217;.</dl>
<dt><code>defslowpaste </code><i>msec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>slowpaste</code> command except that the default setting for new windows is changed. Initial setting is 0 milliseconds, meaning `off&#8217;.</dl>
<dt><code>defutf8 [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>utf8</code> command except that the default setting for new windows is changed. Initial setting is `on&#8217; if screen was started with -U, otherwise `off&#8217;.</dl>
<dt><code>defwrap [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>wrap</code> command except that the default setting for new windows is changed. Initially line-wrap is on and can be toggled with the wrap command (C-a r) or by means of &quot;C-a : wrap on|off&quot;.</dl>
<dt><code>defwritelock [ on | off | auto ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Same as the <code>writelock</code> command except that the default setting for new windows is changed. Initially writelocks will off.</dl>
<dt><code>detach </code>[<code>-h</code>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Detach the <i>screen</i> session (disconnect it from the terminal and put it into the background). This returns you to the shell where you invoked <i>screen</i>. A detached <i>screen</i> can be resumed by invoking <i>screen</i> with the <code>-r</code> option (see also section COMMAND-LINE OPTIONS). The <code>-h</code> option tells screen to immediately close the connection to the terminal (hangup).</dl>
<dt><code>dinfo</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Show what screen thinks about your terminal. Useful if you want to know why features like color or the alternate charset don&#8217;t work.</dl>
<dt><code>displays</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Shows a tabular listing of all currently connected user front-ends (displays). This is most useful for multiuser sessions. The following keys can be used in displays list: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>k</code>, <code>C-p</code>, or <code>up</code></td>
<td>Move up one line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>j</code>, <code>C-n</code>, or <code>down</code></td>
<td>Move down one line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a</code> or <code>home</code></td>
<td>Move to the first line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-e</code> or <code>end</code></td>
<td>Move to the last line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-u</code> or <code>C-d</code></td>
<td>Move one half page up or down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-b</code> or <code>C-f</code></td>
<td>Move one full page up or down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>mouseclick</code></td>
<td> Move to the selected line. Available when mousetrack is set to on.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>space</code></td>
<td>Refresh the list
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>d</code></td>
<td>Detach that display
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>D</code></td>
<td>Power detach that display
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-g</code>, <code>enter</code>, or <code>escape</code></td>
<td>Exit the list
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p> The following is an example of what displays could look like:</p>
<dl>
<dt>
<dd>
<pre>
xterm 80x42 jnweiger@/dev/ttyp4     0(m11)   &amp;rWx
facit 80x24 mlschroe@/dev/ttyhf nb 11(tcsh)   rwx
xterm 80x42 jnhollma@/dev/ttyp5     0(m11)   &amp;R.x
 (A)   (B)     (C)     (D)     (E) (F)(G)   (H)(I)
</pre>
</dl>
<p> The legend is as follows:</p>
<dl>
<dt>
<dd> (A) The terminal type known by screen for this display.</p>
<dt>
<dd> (B) Displays geometry as width x height.</p>
<dt>
<dd> (C) Username who is logged in at the display.</p>
<dt>
<dd> (D) Device name of the display or the attached device</p>
<dt>
<dd> (E) Display is in blocking or nonblocking mode. The available modes are &quot;nb&quot;, &quot;NB&quot;, &quot;Z&lt;&quot;, &quot;Z&gt;&quot;, and &quot;BL&quot;.</p>
<dt>
<dd> (F) Number of the window</p>
<dt>
<dd> (G) Name/title of window</p>
<dt>
<dd> (H) Whether the window is shared</p>
<dt>
<dd> (I) Window permissions. Made up of three characters. </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=6>Window permissions indicators
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>1st character</td>
<td ALIGN=center COLSPAN=2>2nd character</td>
<td ALIGN=center>3rd character</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;</code></td>
<td>no read</td>
<td><code>&#8211;</code></td>
<td>no write</td>
<td><code>&#8211;</code></td>
<td>no execute
</td>
</tr>
<tr VALIGN=top>
<td><code>r</code></td>
<td>read</td>
<td><code>w</code></td>
<td>write</td>
<td><code>x</code></td>
<td>execute
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td><code>W</code></td>
<td>own wlock</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>Indicators of permissions suppressed by a foreign wlock
</td>
</tr>
<tr VALIGN=top>
<td><code>R</code></td>
<td>read only</td>
<td><code>.</code></td>
<td>no write</td>
<td></td>
<td>
</td>
</tr>
</table>
</dl>
<dl>
<dt>
<dd> displays needs a region size of at least 10 characters wide and 5 characters high in order to display.</dl>
<dl>
<dt><i></i><code>digraph</code> [<i>preset</i>[<i>unicode-value</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command prompts the user for a digraph sequence. The next two characters typed are looked up in a builtin table and the resulting character is inserted in the input stream. For example, if the user enters &#8216;a&quot;&#8217;, an a-umlaut will be inserted. If the first character entered is a 0 (zero), <i>screen</i> will treat the following characters (up to three) as an octal number instead. The optional argument <i>preset</i> is treated as user input, thus one can create an umlaut key. For example the command &quot;bindkey ^K digraph &#8216;&quot;&#8217;&quot; enables the user to generate an a-umlaut by typing CTRL-K a. When a non-zero <i>unicode-value</i> is specified, a new digraph is created with the specified preset. The digraph is unset if a zero value is provided for the <i>unicode-value.</i></dl>
<dt><code>dumptermcap</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Write the termcap entry for the virtual terminal optimized for the currently active window to the file .termcap in the user&#8217;s $HOME/.screen directory (or wherever <i>screen</i> stores its sockets. See the FILES section below). This termcap entry is identical to the value of the environment variable $TERMCAP that is set up by <i>screen</i> for each window. For terminfo based systems you will need to run a converter like <i>captoinfo</i> and then compile the entry with <i>tic</i>.</dl>
<dt><code>dynamictitle [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change behaviour for windows regarding if screen should change window title when seeing proper escape sequence. See also &quot;TITLES (naming windows)&quot; section.</dl>
<dt><code>echo </code>[<code>-n</code>]<i>message</i></p>
<dd>
<dl>
<dt>
<dd>
<p> The echo command may be used to annoy <i>screen</i> users with a &#8216;message of the day&#8217;. Typically installed in a global /etc/screenrc. The option -n may be used to suppress the line feed. See also sleep. Echo is also useful for online checking of environment variables.</dl>
<dt><code>encoding </code><i>enc </i>[<i>enc</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Tell <i>screen </i> how to interpret the input/output. The first argument sets the encoding of the current window. Each window can emulate a different encoding. The optional second parameter overwrites the encoding of the connected terminal. It should never be needed as screen uses the locale setting to detect the encoding. There is also a way to select a terminal encoding depending on the terminal type by using the KJ termcap entry. </p>
<p> Supported encodings are eucJP, SJIS, eucKR, eucCN, Big5, GBK, KOI8-R, KOI8-U, CP1251, UTF-8, ISO8859-2, ISO8859-3, ISO8859-4, ISO8859-5, ISO8859-6, ISO8859-7, ISO8859-8, ISO8859-9, ISO8859-10, ISO8859-15, jis. </p>
<p> See also defencoding, which changes the default setting of a new window.</dl>
<dt><code>escape </code><i>xy</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the command character to <i>x</i> and the character generating a literal command character (by triggering the meta command) to <i>y</i> (similar to the -e option). Each argument is either a single character, a two-character sequence of the form ^x (meaning C-x), a backslash followed by an octal number (specifying the ASCII code of the character), or a backslash followed by a second character, such as \^ or \. The default is ^Aa.</dl>
<dt><code>eval</code> <i>command1</i>[<i>command2 &#8230;</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Parses and executes each argument as separate command.</dl>
<dt><i></i><code>exec</code> [[<i>fdpat</i>]<i>newcommand </i>[<i>args &#8230;</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Run a unix subprocess (specified by an executable path <i>newcommand</i> and its optional arguments) in the current window. The flow of data between newcommands stdin/stdout/stderr, the process originally started in the window (let us call it &quot;application-process&quot;) and screen itself (window) is controlled by the file descriptor pattern fdpat. This pattern is basically a three character sequence representing stdin, stdout and stderr of newcommand. A dot (.) connects the file descriptor to <i>screen</i>. An exclamation mark (!) causes the file descriptor to be connected to the application-process. A colon (:) combines both. User input will go to newcommand unless newcommand receives the application-process&#8217; output (fdpats first character is `!&#8217; or `:&#8217;) or a pipe symbol (|) is added (as a fourth character) to the end of fdpat. </p>
<p> Invoking `exec&#8217; without arguments shows name and arguments of the currently running subprocess in this window. Only one subprocess a time can be running in each window. </p>
<p> When a subprocess is running the `kill&#8217; command will affect it instead of the windows process. </p>
<p> Refer to the postscript file `doc/fdpat.ps&#8217; for a confusing illustration of all 21 possible combinations. Each drawing shows the digits 2,1,0 representing the three file descriptors of newcommand. The box marked `W&#8217; is the usual pty that has the application-process on its slave side. The box marked `P&#8217; is the secondary pty that now has <i>screen</i> at its master side. </p>
<p> Abbreviations: Whitespace between the word `exec&#8217; and fdpat and the command can be omitted. Trailing dots and a fdpat consisting only of dots can be omitted. A simple `|&#8217; is synonymous for the pattern `!..|&#8217;; the word exec can be omitted here and can always be replaced by `!&#8217;. </p>
<p> Examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>exec &#8230; /bin/sh</p>
<dd>
<dt>exec /bin/sh</p>
<dd>
<dt>!/bin/sh</p>
<dd>
<p> Creates another shell in the same window, while the original shell is still running. Output of both shells is displayed and user input is sent to the new /bin/sh.</p>
<dt>exec !.. stty 19200</p>
<dd>
<dt>exec ! stty 19200</p>
<dd>
<dt>!!stty 19200</p>
<dd>
<p> Set the speed of the window&#8217;s tty. If your stty command operates on stdout, then add another `!&#8217;.</p>
<dt>exec !..| less</p>
<dd>
<dt>|less</p>
<dd>
<p> This adds a pager to the window output. The special character `|&#8217; is needed to give the user control over the pager although it gets its input from the window&#8217;s process. This works, because <i>less</i> listens on stderr (a behavior that <i>screen</i> would not expect without the `|&#8217;) when its stdin is not a tty. <i>Less </i> versions newer than 177 fail miserably here; good old <i>pg</i> still works.</p>
<dt>!:sed -n s/.*Error.*//p</p>
<dd>
<p> Sends window output to both, the user and the sed command. The sed inserts an additional bell character (oct. 007) to the window output seen by <i>screen</i>. This will cause &quot;Bell in window x&quot; messages, whenever the string &quot;Error&quot; appears in the window.</dl>
</dl>
</dl>
<dt><code>fit</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change the window size to the size of the current region. This command is needed because screen doesn&#8217;t adapt the window size automatically if the window is displayed more than once.</dl>
<dt><code>flow [ on | off | auto]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sets the flow-control mode for this window. Without parameters it cycles the current window&#8217;s flow-control setting from &quot;automatic&quot; to &quot;on&quot; to &quot;off&quot;. See the discussion on FLOW-CONTROL later on in this document for full details and note, that this is subject to change in future releases. Default is set by `defflow&#8217;.</dl>
<dt><code>focus [ next | prev | up | down | left | right | top | bottom ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Move the input focus to the next region. This is done in a cyclic way so that the top left region is selected after the bottom right one. If no option is given it defaults to `next&#8217;. The next region to be selected is determined by how the regions are layered. Normally, the next region in the same layer would be selected. However, if that next region contains one or more layers, the first region in the highest layer is selected first. If you are at the last region of the current layer, `next&#8217; will move the focus to the next region in the lower layer (if there is a lower layer). `Prev&#8217; cycles in the opposite order. See split for more information about layers. </p>
<p> The rest of the options (`up&#8217;, `down&#8217;, `left&#8217;, `right&#8217;, `top&#8217;, and `bottom&#8217;) are more indifferent to layers. The option `up&#8217; will move the focus upward to the region that is touching the upper left corner of the current region. `Down&#8217; will move downward to the region that is touching the lower left corner of the current region. The option `left&#8217; will move the focus leftward to the region that is touching the upper left corner of the current region, while `right&#8217; will move rightward to the region that is touching the upper right corner of the current region. Moving left from a left most region or moving right from a right most region will result in no action. </p>
<p> The option `top&#8217; will move the focus to the very first region in the upper list corner of the screen, and `bottom&#8217; will move to the region in the bottom right corner of the screen. Moving up from a top most region or moving down from a bottom most region will result in no action. </p>
<p> Useful bindings are (h, j, k, and l as in vi) </p>
<pre>
    bind h focus left
    bind j focus down
    bind k focus up
    bind l focus right
    bind t focus top
    bind b focus bottom
</pre>
<p> Note that <code>k</code> is traditionally bound to the <i>kill</i> command.</dl>
<dt><code>focusminsize [ ( </code><i>width</i><code>|max|_ ) ( </code><i>height</i><code>|max|_ ) ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> This forces any currently selected region to be automatically resized at least a certain <i>width</i> and <i>height</i>. All other surrounding regions will be resized in order to accommodate. This constraint follows every time the focus command is used. The resize command can be used to increase either dimension of a region, but never below what is set with focusminsize. The underscore `_&#8217; is a synonym for <code>max</code>. Setting a <i>width</i> and <i>height</i> of `0 0&#8242; (zero zero) will undo any constraints and allow for manual resizing. Without any parameters, the minimum width and height is shown.</dl>
<dt><code>gr [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Turn GR charset switching on/off. Whenever screen sees an input character with the 8th bit set, it will use the charset stored in the GR slot and print the character with the 8th bit stripped. The default (see also defgr) is not to process GR switching because otherwise the ISO88591 charset would not work.</dl>
<dt><i></i><code>group</code> [<i>grouptitle</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change or show the group the current window belongs to. Windows can be moved around between different groups by specifying the name of the destination group. Without specifying a group, the title of the current group is displayed.</dl>
<dt><i></i><code>hardcopy</code> [<i>-h</i>] [<i>file</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Writes out the currently displayed image to the file <i>file</i>, or, if no filename is specified, to <i>hardcopy.n</i> in the default directory, where <i>n</i> is the number of the current window. This either appends or overwrites the file if it exists. See below. If the option <code>-h</code> is specified, dump also the contents of the scrollback buffer.</dl>
<dt><code>hardcopy_append [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> If set to &quot;on&quot;, <i>screen</i> will append to the &quot;hardcopy.n&quot; files created by the command C-a h, otherwise these files are overwritten each time. Default is `off&#8217;.</dl>
<dt><code>hardcopydir directory</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Defines a directory where hardcopy files will be placed. If unset, hardcopys are dumped in <i>screen</i>&#8216;s current working directory.</dl>
<dt><code>hardstatus [ on | off ]</code></p>
<dd>
<dt><code>hardstatus [ always ] firstline | lastline | message | ignore [ string ]</code></p>
<dd>
<dt><code>hardstatus string [ string ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> This command configures the use and emulation of the terminal&#8217;s hardstatus line. The first form toggles whether <i>screen</i> will use the hardware status line to display messages. If the flag is set to `off&#8217;, these messages are overlaid in reverse video mode at the display line. The default setting is `on&#8217;. </p>
<p> The second form tells <i>screen </i> what to do if the terminal doesn&#8217;t have a hardstatus line (i.e. the termcap/terminfo capabilities &quot;hs&quot;, &quot;ts&quot;, &quot;fs&quot; and &quot;ds&quot; are not set). When firstline/lastline is used, <i>screen </i> will reserve the first/last line of the display for the hardstatus. message uses <i>screen&#8217;s</i> message mechanism and ignore tells <i>screen </i> never to display the hardstatus. If you prepend the word always to the type (e.g., alwayslastline), <i>screen </i> will use the type even if the terminal supports a hardstatus. </p>
<p> The third form specifies the contents of the hardstatus line. &#8216;%h&#8217; is used as default string, i.e., the stored hardstatus of the current window (settable via ESC]0;&lt;string&gt;^G or ESC_&lt;string&gt;ESC\) is displayed. You can customize this to any string you like including the escapes from the STRING ESCAPES chapter. If you leave out the argument <i>string</i>, the current string is displayed. </p>
<p> You can mix the second and third form by providing the string as additional argument.</dl>
<dt><code>height </code>[<code>-w</code>|<code>-d</code>] [<i>lines</i> [<i>cols</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Set the display height to a specified number of lines. When no argument is given it toggles between 24 and 42 lines display. You can also specify a width if you want to change both values. The <code>-w</code> option tells screen to leave the display size unchanged and just set the window size, <code>-d</code> vice versa.</dl>
<dt><code>help</code>[<i>class</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Not really a online help, but displays a help <i>screen </i> showing you all the key bindings. The first pages list all the internal commands followed by their current bindings. Subsequent pages will display the custom commands, one command per key. Press space when you&#8217;re done reading each page, or return to exit early. All other characters are ignored. If the -c option is given, display all bound commands for the specified command class. See also DEFAULT KEY BINDINGS section.</dl>
<dt><code>history</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Usually users work with a shell that allows easy access to previous commands. For example csh has the command !! to repeat the last command executed. <i>Screen</i> allows you to have a primitive way of re-calling the command that started &#8230;: You just type the first letter of that command, then hit `C-a {&#8216; and <i>screen</i> tries to find a previous line that matches with the `prompt character&#8217; to the left of the cursor. This line is pasted into this window&#8217;s input queue. Thus you have a crude command history (made up by the visible window and its scrollback buffer).</dl>
<dt><code>hstatus </code><i>status</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Change the window&#8217;s hardstatus line to the string <i>status</i>.</dl>
<dt><i></i><code>idle</code> [<i>timeout</i>[<i>cmd-args</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Sets a command that is run after the specified number of seconds inactivity is reached. This command will normally be the blanker command to create a screen blanker, but it can be any screen command. If no command is specified, only the timeout is set. A timeout of zero (or the special timeout <code>off</code>) disables the timer. If no arguments are given, the current settings are displayed.</dl>
<dt><code>ignorecase [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Tell screen to ignore the case of characters in searches. Default is `off&#8217;. Without any options, the state of ignorecase is toggled.</dl>
<dt><code>info</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Uses the message line to display some information about the current window: the cursor position in the form (column,row) starting with (1,1), the terminal width and height plus the size of the scrollback buffer in lines, like in (80,24)+50, the current state of window XON/XOFF flow control is shown like this (See also section FLOW CONTROL): </p>
<table BORDER>
<tr VALIGN=top>
<td>+flow</td>
<td>automatic flow control, currently on.
</td>
</tr>
<tr VALIGN=top>
<td>-flow</td>
<td>automatic flow control, currently off.
</td>
</tr>
<tr VALIGN=top>
<td>+(+)flow</td>
<td>flow control enabled. Agrees with automatic control.
</td>
</tr>
<tr VALIGN=top>
<td>-(+)flow</td>
<td>flow control disabled. Disagrees with automatic control.
</td>
</tr>
<tr VALIGN=top>
<td>+(-)flow</td>
<td>flow control enabled. Disagrees with automatic control.
</td>
</tr>
<tr VALIGN=top>
<td>-(-)flow</td>
<td>flow control disabled. Agrees with automatic control.
</td>
</tr>
</table>
<p> The current line wrap setting (`+wrap&#8217; indicates enabled, `-wrap&#8217; not) is also shown. The flags `ins&#8217;, `org&#8217;, `app&#8217;, `log&#8217;, `mon&#8217; or `nored&#8217; are displayed when the window is in insert mode, origin mode, application-keypad mode, has output logging, activity monitoring or partial redraw enabled. </p>
<p> The currently active character set (<i>G0</i>, <i>G1</i>, <i>G2</i>, or <i>G3</i>) and in square brackets the terminal character sets that are currently designated as <i>G0</i> through <i>G3</i> is shown. If the window is in UTF-8 mode, the string UTF-8 is shown instead. </p>
<p> Additional modes depending on the type of the window are displayed at the end of the status line (See also chapter WINDOW TYPES). </p>
<p> If the state machine of the terminal emulator is in a non-default state, the info line is started with a string identifying the current state. </p>
<p> For system information use the time command.</dl>
<dt><code>ins_reg</code> [<i>key</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> No longer exists, use paste instead.</dl>
<dt><code>kill</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Kill current window. </p>
<p> If there is an `exec&#8217; command running then it is killed. Otherwise the process (shell) running in the window receives a HANGUP condition, the window structure is removed and <i>screen </i> (your display) switches to another window. When the last window is destroyed, <i>screen</i> exits. After a kill <i>screen </i> switches to the previously displayed window. </p>
<p> Note: <i>Emacs</i> users should keep this command in mind, when killing a line. It is recommended not to use C-a as the <i>screen</i> escape key or to rebind kill to C-a K.</dl>
<dt><code>lastmsg</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Redisplay the last contents of the message/status line. Useful if you&#8217;re typing when a message appears, because the message goes away when you press a key (unless your terminal has a hardware status line). Refer to the commands msgwait and msgminwait for fine tuning.</dl>
<dt><code>layout new </code>[<i>title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Create a new layout. The screen will change to one whole region and be switched to the blank window. From here, you build the regions and the windows they show as you desire. The new layout will be numbered with the smallest available integer, starting with zero. You can optionally give a title to your new layout. Otherwise, it will have a default title of layout. You can always change the title later by using the command <code>layout title</code>.</dl>
<dt><code>layout remove </code>[<i>n|title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Remove, or in other words, delete the specified layout. Either the number or the title can be specified. Without either specification, <i>screen</i> will remove the current layout. </p>
<p> Removing a layout does not affect your set windows or regions.</dl>
<dt><code>layout next</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the next layout available</dl>
<dt><code>layout prev</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the previous layout available</dl>
<dt><code>layout select </code>[<i>n|title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Select the desired layout. Either the number or the title can be specified. Without either specification, <i>screen</i> will prompt and ask which screen is desired. To see which layouts are available, use the <code>layout show</code> command.</dl>
<dt><code>layout show</code></p>
<dd>
<dl>
<dt>
<dd>
<p> List on the message line the number(s) and title(s) of the available layout(s). The current layout is flagged.</dl>
<dt><code>layout title </code>[<i>title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change or display the title of the current layout. A string given will be used to name the layout. Without any options, the current title and number is displayed on the message line.</dl>
<dt><code>layout number </code>[<i>n</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change or display the number of the current layout. An integer given will be used to number the layout. Without any options, the current number and title is displayed on the message line.</dl>
<dt><code>layout attach </code>[<i>title</i>|<code>:last</code>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change or display which layout to reattach back to. The default is <code>:last</code>, which tells <i>screen</i> to reattach back to the last used layout just before detachment. By supplying a title, You can instruct <i>screen</i> to reattach to a particular layout regardless which one was used at the time of detachment. Without any options, the layout to reattach to will be shown in the message line.</dl>
<dt><code>layout save </code>[<i>n|title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Remember the current arrangement of regions. When used, <i>screen</i> will remember the arrangement of vertically and horizontally split regions. This arrangement is restored when a <i>screen</i> session is reattached or switched back from a different layout. If the session ends or the <i>screen</i> process dies, the layout arrangements are lost. The <code>layout dump</code> command should help in this siutation. If a number or title is supplied, <i>screen</i> will remember the arrangement of that particular layout. Without any options, <i>screen</i> will remember the current layout. </p>
<p> Saving your regions can be done automatically by using the <code>layout autosave</code> command.</dl>
<dt><code>layout autosave [ on | off]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change or display the status of automatcally saving layouts. The default is <code>on</code>, meaning when <i>screen</i> is detached or changed to a different layout, the arrangement of regions and windows will be remembered at the time of change and restored upon return. If autosave is set to <code>off</code>, that arrangement will only be restored to either to the last manual save, using <code>layout save</code>, or to when the layout was first created, to a single region with a single window. Without either an <code>on</code> or <code>off</code>, the current status is displayed on the message line.</dl>
<dt><code>layout dump </code>[<i>filename</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Write to a file the order of splits made in the current layout. This is useful to recreate the order of your regions used in your current layout. Only the current layout is recorded. While the order of the regions are recorded, the sizes of those regions and which windows correspond to which regions are not. If no filename is specified, the default is <i>layout-dump</i>, saved in the directory that the <i>screen</i> process was started in. If the file already exists, <code>layout dump</code> will append to that file. As an example: </p>
<pre>
            C-a : layout dump /home/user/.screenrc
</pre>
<p> will save or append the layout to the user&#8217;s <i>.screenrc</i> file.</dl>
<dt><code>license</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Display the disclaimer page. This is done whenever <i>screen</i> is started without options, which should be often enough. See also the <code>startup_message</code> command.</dl>
<dt><code>lockscreen</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Lock this display. Call a screenlock program (/local/bin/lck or /usr/bin/lock or a builtin if no other is available). Screen does not accept any command keys until this program terminates. Meanwhile processes in the windows may continue, as the windows are in the `detached&#8217; state. The screenlock program may be changed through the environment variable $LOCKPRG (which must be set in the shell from which <i>screen</i> is started) and is executed with the user&#8217;s uid and gid. </p>
<p> Warning: When you leave other shells unlocked and you have no password set on <i>screen</i>, the lock is void: One could easily re-attach from an unlocked shell. This feature should rather be called `lockterminal&#8217;.</dl>
<dt><code>log [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Start/stop writing output of the current window to a file screenlog.<i>n</i> in the window&#8217;s default directory, where <i>n</i> is the number of the current window. This filename can be changed with the `logfile&#8217; command. If no parameter is given, the state of logging is toggled. The session log is appended to the previous contents of the file if it already exists. The current contents and the contents of the scrollback history are not included in the session log. Default is `off&#8217;.</dl>
<dt><code>logfile </code><i>filename</i></p>
<dd>
<dt><code>logfile flush </code><i>secs</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Defines the name the log files will get. The default is screenlog.%n. The second form changes the number of seconds <i>screen</i> will wait before flushing the logfile buffer to the file-system. The default value is 10 seconds.</dl>
<dt><code>login [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Adds or removes the entry in the utmp database file for the current window. This controls if the window is `logged in&#8217;. When no parameter is given, the login state of the window is toggled. Additionally to that toggle, it is convenient having a `log in&#8217; and a `log out&#8217; key. E.g. `bind I login on&#8217; and `bind O login off&#8217; will map these keys to be C-a I and C-a O. The default setting (in config.h.in) should be on for a <i>screen</i> that runs under suid-root. Use the deflogin command to change the default login state for new windows. Both commands are only present when <i>screen</i> has been compiled with utmp support.</dl>
<dt><code>logtstamp </code>[<code>on</code>|<code>off</code>]</p>
<dd>
<dt><i></i><code>logtstamp after</code> [<i>secs</i>]</p>
<dd>
<dt><code>logtstamp string</code></p>
<dd>
<dl>
<dt>
<dd> [<i>string</i>] </p>
<p> This command controls logfile time-stamp mechanism of <i>screen.</i> If time-stamps are turned on, <i>screen </i> adds a string containing the current time to the logfile after two minutes of inactivity. When output continues and more than another two minutes have passed, a second time-stamp is added to document the restart of the output. You can change this timeout with the second form of the command. The third form is used for customizing the time-stamp string (`&#8211; %n:%t &#8212; time-stamp &#8212; %M/%d/%y %c:%s &#8211;
&#8217; by default).</dl>
<dt><code>mapdefault</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Tell <i>screen </i> that the next input character should only be looked up in the default bindkey table. See also bindkey.</dl>
<dt><code>mapnotnext</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Like mapdefault, but don&#8217;t even look in the default bindkey table.</dl>
<dt><i>maptimeout</i> [<i>timeout</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Set the inter-character timer for input sequence detection to a timeout of <i>timeout</i> ms. The default timeout is 300ms. Maptimeout with no arguments shows the current setting. See also bindkey.</dl>
<dt><code>markkeys </code><i>string</i></p>
<dd>
<dl>
<dt>
<dd>
<p> This is a method of changing the keymap used for copy/history mode. The string is made up of <i>oldchar</i>=<i>newchar</i> pairs which are separated by `:&#8217;. Example: The string B=^B:F=^F will change the keys `C-b&#8217; and `C-f&#8217; to the vi style binding (scroll up/down fill page). This happens to be the default binding for `B&#8217; and `F&#8217;. The command markkeys h=^B:l=^F:$=^E would set the mode for an emacs-style binding. If your terminal sends characters, that cause you to abort copy mode, then this command may help by binding these characters to do nothing. The no-op character is `@&#8217; and is used like this: markkeys @=L=H if you do not want to use the `H&#8217; or `L&#8217; commands any longer. As shown in this example, multiple keys can be assigned to one function in a single statement.</dl>
<dt><code>maxwin </code><i>num</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the maximum window number screen will create. Doesn&#8217;t affect already existing windows. The number can be increased only when there are no existing windows.</dl>
<dt><code>meta</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Insert the command character (C-a) in the current window&#8217;s input stream.</dl>
<dt><code>monitor [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Toggles activity monitoring of windows. When monitoring is turned on and an affected window is switched into the background, you will receive the activity notification message in the status line at the first sign of output and the window will also be marked with an `@&#8217; in the window-status display. Monitoring is initially off for all windows.</dl>
<dt><code>mousetrack [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> This command determines whether <i>screen</i> will watch for mouse clicks. When this command is enabled, regions that have been split in various ways can be selected by pointing to them with a mouse and left-clicking them. Without specifying <code>on</code> or <code>off</code>, the current state is displayed. The default state is determined by the <code>defmousetrack</code> command.</dl>
<dt><code>msgminwait </code><i>sec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Defines the time <i>screen </i> delays a new message when one message is currently displayed. The default is 1 second.</dl>
<dt><code>msgwait </code><i>sec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Defines the time a message is displayed if <i>screen</i> is not disturbed by other activity. The default is 5 seconds.</dl>
<dt><code>multiuser [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch between singleuser and multiuser mode. Standard <i>screen</i> operation is singleuser. In multiuser mode the commands `acladd&#8217;, `aclchg&#8217;, `aclgrp&#8217; and `acldel&#8217; can be used to enable (and disable) other users accessing this <i>screen</i> session.</dl>
<dt><code>nethack [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Changes the kind of error messages used by <i>screen</i>. When you are familiar with the game nethack, you may enjoy the nethack-style messages which will often blur the facts a little, but are much funnier to read. Anyway, standard messages often tend to be unclear as well.<br />
 This option is only available if <i>screen</i> was compiled with the NETHACK flag defined. The default setting is then determined by the presence of the environment variable $NETHACKOPTIONS and the file ~/.nethackrc &#8211; if either one is present, the default is <code>on</code>.</dl>
<dt><code>next</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the next window. This command can be used repeatedly to cycle through the list of windows.</dl>
</dl>
<p> <code>nonblock [ on | off | numsecs ]</code></p>
<dl>
<dt>
<dd>
<p> Tell screen how to deal with user interfaces (displays) that cease to accept output. This can happen if a user presses ^S or a TCP/modem connection gets cut but no hangup is received. If nonblock is <code>off</code> (this is the default) screen waits until the display restarts to accept the output. If nonblock is <code>on</code>, screen waits until the timeout is reached (<code>on</code> is treated as 1s). If the display still doesn&#8217;t receive characters, screen will consider it blocked and stop sending characters to it. If at some time it restarts to accept characters, screen will unblock the display and redisplay the updated window contents.</dl>
<dl>
<dt><code>number </code>[[+|-]<i>n</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Change the current window&#8217;s number. If the given number <i>n</i> is already used by another window, both windows exchange their numbers. If no argument is specified, the current window number (and title) is shown. Using `+&#8217; or `-&#8216; will change the window&#8217;s number by the relative amount specified.</dl>
<dt><code>obuflimit </code>[<i>limit</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> If the output buffer contains more bytes than the specified limit, no more data will be read from the windows. The default value is 256. If you have a fast display (like xterm), you can set it to some higher value. If no argument is specified, the current setting is displayed.</dl>
<dt><code>only</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Kill all regions but the current one.</dl>
<dt><code>other</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the window displayed previously. If this window does no longer exist, <i>other</i> has the same effect as <i>next</i>.</dl>
<dt><code>partial [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Defines whether the display should be refreshed (as with <i>redisplay</i>) after switching to the current window. This command only affects the current window. To immediately affect all windows use the <i>allpartial</i> command. Default is `off&#8217;, of course. This default is fixed, as there is currently no <i>defpartial</i> command.</dl>
<dt><code>password </code>[<i>crypted_pw</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Present a crypted password in your .screenrc file and <i>screen</i> will ask for it, whenever someone attempts to resume a detached. This is useful if you have privileged programs running under <i>screen</i> and you want to protect your session from reattach attempts by another user masquerading as your uid (i.e. any superuser.) If no crypted password is specified, <i>screen</i> prompts twice for typing a password and places its encryption in the paste buffer. Default is `none&#8217;, this disables password checking.</dl>
<dt><i></i><code>paste</code> [<i>registers</i> [<i>dest_reg</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Write the (concatenated) contents of the specified registers to the stdin queue of the current window. The register &#8216;.&#8217; is treated as the paste buffer. If no parameter is given the user is prompted for a single register to paste. The paste buffer can be filled with the <code>copy</code>, <code>history</code> and <code>readbuf</code> commands. Other registers can be filled with the <code>register</code>, <code>readreg</code> and <code>paste</code> commands. If <code>paste</code> is called with a second argument, the contents of the specified registers is pasted into the named destination register rather than the window. If &#8216;.&#8217; is used as the second argument, the displays paste buffer is the destination. Note, that <code>paste</code> uses a wide variety of resources: Whenever a second argument is specified no current window is needed. When the source specification only contains registers (not the paste buffer) then there need not be a current display (terminal attached), as the registers are a global resource. The paste buffer exists once for every user.</dl>
<dt><code>pastefont [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Tell <i>screen </i> to include font information in the paste buffer. The default is not to do so. This command is especially useful for multi character fonts like kanji.</dl>
<dt><code>pow_break</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Reopen the window&#8217;s terminal line and send a break condition. See `break&#8217;.</dl>
<dt><code>pow_detach</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Power detach. Mainly the same as <i>detach</i>, but also sends a HANGUP signal to the parent process of <i>screen</i>. CAUTION: This will result in a logout, when <i>screen</i> was started from your login-shell.</dl>
<dt><i></i><code>pow_detach_msg</code> [<i>message</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> The <i>message</i> specified here is output whenever a `Power detach&#8217; was performed. It may be used as a replacement for a logout message or to reset baud rate, etc. Without parameter, the current message is shown.</dl>
<dt><code>prev</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the window with the next lower number. This command can be used repeatedly to cycle through the list of windows.</dl>
<dt><i></i><code>printcmd</code> [<i>cmd</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> If <i>cmd</i> is not an empty string, <i>screen </i> will not use the terminal capabilities po/pf if it detects an ansi print sequence <code>ESC [ 5 i</code>, but pipe the output into <i>cmd</i>. This should normally be a command like lpr or &#8216;cat &gt; /tmp/scrprint&#8217;. <code>printcmd</code> without a command displays the current setting. The ansi sequence <code>ESC \</code> ends printing and closes the pipe. </p>
<p> Warning: Be careful with this command! If other user have write access to your terminal, they will be able to fire off print commands.</dl>
<dt><code>process</code> [<i>key</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Stuff the contents of the specified register into <i>screen</i>&#8216;s input queue. If no argument is given you are prompted for a register name. The text is parsed as if it had been typed in from the user&#8217;s keyboard. This command can be used to bind multiple actions to a single key.</dl>
<dt><code>quit</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Kill all windows and terminate <i>screen</i>. Note that on VT100-style terminals the keys C-4 and C-\ are identical. This makes the default bindings dangerous: Be careful not to type C-a C-4 when selecting window no. 4. Use the empty bind command (as in bind &#8216;^\&#8217;) to remove a key binding.</dl>
<dt><i></i><code>readbuf</code> [<i>encoding</i>] [<i>filename</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Reads the contents of the specified file into the paste buffer. You can tell screen the encoding of the file via the <code>-e</code> option. If no file is specified, the screen-exchange filename is used. See also <code>bufferfile</code> command.</dl>
<dt><i></i><code>readreg</code> [<i>encoding</i>] [<i>register</i> [<i>filename</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Does one of two things, dependent on number of arguments: with zero or one arguments it duplicates the paste buffer contents into the register specified or entered at the prompt. With two arguments it reads the contents of the named file into the register, just as <i>readbuf</i> reads the screen-exchange file into the paste buffer. You can tell screen the encoding of the file via the <code>-e</code> option. The following example will paste the system&#8217;s password file into the <i>screen </i> window (using register p, where a copy remains): </p>
<pre>
            C-a : readreg p /etc/passwd
            C-a : paste p
</pre>
</dl>
<dt><code>redisplay</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Redisplay the current window. Needed to get a full redisplay when in partial redraw mode.</dl>
<dt><code>register</code> <i></i>[<code>-e</code><i>encoding</i>]<i>key-string</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Save the specified <i>string</i> to the register <i>key</i>. The encoding of the string can be specified via the <code>-e</code> option. See also the paste command.</dl>
<dt><code>remove</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Kill the current region. This is a no-op if there is only one region.</dl>
<dt><code>removebuf</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Unlinks the screen-exchange file used by the commands <code>writebuf</code> and <code>readbuf</code>.</dl>
<dt><code>rendition [ bell | monitor | silence | so ] attr [ color ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change the way <i>screen</i> renders the titles of windows that have monitor or bell flags set in caption or hardstatus or windowlist. See the STRING ESCAPES chapter for the syntax of the modifiers. The default for monitor is currently =b (bold, active colors), for bell =ub (underline, bold and active colors), and =u for silence.</dl>
<dt><code>reset</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Reset the virtual terminal to its power-on values. Useful when strange settings (like scroll regions or graphics character set) are left over from an application.</dl>
<dt><code>resize</code></p>
<dd> [<code>-h</code>|<code>-v</code>|<code>-b</code>|<code>-l</code>|<code>-p</code>] [[<code>+</code>|<code>&#8211;</code>] <i>n</i>[%] |<code>=</code>|<code>max</code>|<code>min</code>|<code>_</code>|<code>0</code>]</p>
<dl>
<dt>
<dd>
<p> Resize the current region. The space will be removed from or added to the surrounding regions depending on the order of the splits. The available options for resizing are `-h'(horizontal), `-v'(vertical), `-b'(both), `-l'(local to layer), and `-p'(perpendicular). Horizontal resizes will add or remove width to a region, vertical will add or remove height, and both will add or remove size from both dimensions. Local and perpendicular are similar to horizontal and vertical, but they take in account of how a region was split. If a region&#8217;s last split was horizontal, a local resize will work like a vertical resize. If a region&#8217;s last split was vertical, a local resize will work like a horizontal resize. Perpendicular resizes work in opposite of local resizes. If no option is specified, local is the default. </p>
<p> The amount of lines to add or remove can be expressed a couple of different ways. By specifying a number <i>n</i> by itself will resize the region by that absolute amount. You can specify a relative amount by prefixing a plus `+&#8217; or minus `-&#8216; to the amount, such as adding +<i>n</i> lines or removing &#8211;<i>n</i> lines. Resizing can also be expressed as an absolute or relative percentage by postfixing a percent sign `%&#8217;. Using zero `0&#8242; is a synonym for `min&#8217; and using an underscore `_&#8217; is a synonym for `max&#8217;. </p>
<p> Some examples are:</p>
<dl>
<dt>resize +N</p>
<dd> increase current region by N</p>
<dt>resize -N</p>
<dd> decrease current region by N</p>
<dt>resize N</p>
<dd> set current region to N</p>
<dt>resize 20%</p>
<dd> set current region to 20% of original size</p>
<dt>resize +20%</p>
<dd> increase current region by 20%</p>
<dt>resize -b =</p>
<dd> make all windows equally</p>
<dt>resize max</p>
<dd> maximize current region</p>
<dt>resize min</p>
<dd> minimize current region</dl>
<p> Without any arguments, <i>screen</i> will prompt for how you would like to resize the current region. </p>
<p> See focusminsize if you want to restrict the minimum size a region can have.</dl>
</dl>
</dl>
<dt><code>screen </code>[<i>-opts</i>] [<i>n</i>] [<i>cmd</i> [<i>args</i>]|<code>//group</code>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Establish a new window. The flow-control options (<code>-f</code>, <code>-fn</code> and <code>-fa</code>), title (a.k.a.) option (<code>-t</code>), login options (<code>-l</code> and <code>-ln</code>) , terminal type option (<code>-T</code> &lt;term&gt;), the all-capability-flag (<code>-a</code>) and scrollback option (<code>-h</code> &lt;num&gt;) may be specified with each command. The option (<code>-M</code>) turns monitoring on for this window. The option (<code>-L</code>) turns output logging on for this window. If an optional number <i>n</i> in the range 0..MAXWIN-1 is given, the window number <i>n</i> is assigned to the newly created window (or, if this number is already in-use, the next available number). If a command is specified after screen, this command (with the given arguments) is started in the window; otherwise, a shell is created. If <code>//group</code> is supplied, a container-type window is created in which other windows may be created inside it. </p>
<p> Thus, if your .screenrc contains the lines </p>
<pre>
            # example for .screenrc:
            screen 1
            screen -fn -t foobar -L 2 telnet foobar
</pre>
<p> <i>screen</i> creates a shell window (in window #1) and a window with a TELNET connection to the machine foobar (with no flow-control using the title foobar in window #2) and will write a logfile (screenlog.2) of the telnet session. Note, that unlike previous versions of <i>screen</i> no additional default window is created when screen commands are included in your .screenrc file. When the initialization is completed, <i>screen</i> switches to the last window specified in your .screenrc file or, if none, opens a default window #0. </p>
<p> Screen has built in some functionality of cu and telnet. See also chapter WINDOW TYPES.</dl>
<dt><code>scrollback </code><i>num</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the size of the scrollback buffer for the current windows to <i>num</i> lines. The default scrollback is 100 lines. See also the defscrollback command and use info to view the current setting. To access and use the contents in the scrollback buffer, use the copy command.</dl>
<dt><code>select </code>[<i>WindowID</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Switch to the window identified by <i>WindowID</i>. This can be a prefix of a window title (alphanumeric window name) or a window number. The parameter is optional and if omitted, you get prompted for an identifier. When a new window is established, the first available number is assigned to this window. Thus, the first window can be activated by select 0. The number of windows is limited at compile-time by the MAXWIN configuration parameter (which defaults to 40). There are two special WindowIDs, &#8211; selects the internal blank window and . selects the current window. The latter is useful if used with screen&#8217;s -X option.</dl>
<dt><code>sessionname </code>[<i>name</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Rename the current session. Note, that for screen -list the name shows up with the process-id prepended. If the argument name is omitted, the name of this session is displayed. Caution: The $STY environment variables will still reflect the old name in pre-existing shells. This may result in confusion. Use of this command is generally discouraged. Use the -S command-line option if you want to name a new session. The default is constructed from the tty and host names.</dl>
<dt><i></i><code>setenv</code> [<i>var</i> [<i>string</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Set the environment variable <i>var</i> to value <i>string</i>. If only <i>var</i> is specified, the user will be prompted to enter a value. If no parameters are specified, the user will be prompted for both variable and value. The environment is inherited by all subsequently forked shells.</dl>
<dt><code>setsid [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Normally screen uses different sessions and process groups for the windows. If setsid is turned <i>off</i>, this is not done anymore and all windows will be in the same process group as the screen backend process. This also breaks job-control, so be careful. The default is <i>on</i>, of course. This command is probably useful only in rare circumstances.</dl>
<dt><code>shell </code><i>command</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the command to be used to create a new shell. This overrides the value of the environment variable $SHELL. This is useful if you&#8217;d like to run a tty-enhancer which is expecting to execute the program specified in $SHELL. If the command begins with a &#8216;-&#8216; character, the shell will be started as a login-shell. Typical shells do only minimal initialization when not started as a login-shell. E.g. Bash will not read your ~/.bashrc unless it is a login-shell.</dl>
<dt><code>shelltitle </code><i>title</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Set the title for all shells created during startup or by the C-A C-c command. For details about what a title is, see the discussion entitled TITLES (naming windows).</dl>
<dt><code>silence [ on | off | sec ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Toggles silence monitoring of windows. When silence is turned on and an affected window is switched into the background, you will receive the silence notification message in the status line after a specified period of inactivity (silence). The default timeout can be changed with the `silencewait&#8217; command or by specifying a number of seconds instead of `on&#8217; or `off&#8217;. Silence is initially off for all windows.</dl>
<dt><code>silencewait </code><i>sec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Define the time that all windows monitored for silence should wait before displaying a message. Default 30 seconds. </p>
<p> <code>sleep </code><i>num</i></p>
<dl>
<dt>
<dd>
<p> This command will pause the execution of a .screenrc file for <i>num</i> seconds. Keyboard activity will end the sleep. It may be used to give users a chance to read the messages output by echo.</dl>
<dl>
<dt><code>slowpaste </code><i>msec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Define the speed at which text is inserted into the current window by the paste (&quot;C-a ]&quot;) command. If the slowpaste value is nonzero text is written character by character. <i>screen</i> will make a pause of <i>msec</i> milliseconds after each single character write to allow the application to process its input. Only use slowpaste if your underlying system exposes flow control problems while pasting large amounts of text.</dl>
<dt><code>sort</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sort the windows in alphabetical order of the window tiles.</dl>
<dt><code>source </code><i>file</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Read and execute commands from file <i>file</i>. Source commands may be nested to a maximum recursion level of ten. If file is not an absolute path and screen is already processing a source command, the parent directory of the running source command file is used to search for the new command file before screen&#8217;s current directory. </p>
<p> Note that termcap/terminfo/termcapinfo commands only work at startup and reattach time, so they must be reached via the default screenrc files to have an effect.</dl>
<dt><i></i><code>sorendition</code> [<i>attr</i>[<i>color</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> This command is deprecated. See &quot;rendition so&quot; instead.</dl>
<dt><code>split</code>[<code>-v</code>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Split the current region into two new ones. All regions on the display are resized to make room for the new region. The blank window is displayed in the new region. The default is to create a horizontal split, putting the new regions on the top and bottom of each other. Using `-v&#8217; will create a vertical split, causing the new regions to appear side by side of each other. Use the remove or the only command to delete regions. Use focus to toggle between regions. </p>
<p> When a region is split opposite of how it was previously split (that is, vertical then horizontal or horizontal then vertical), a new layer is created. The layer is used to group together the regions that are split the same. Normally, as a user, you should not see nor have to worry about layers, but they will affect how some commands (focus and resize) behave. </p>
<p> With this current implementation of screen, scrolling data will appear much slower in a vertically split region than one that is not. This should be taken into consideration if you need to use system commands such as <code>cat</code> or <code>tail -f</code>.</dl>
<dt><code>startup_message [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Select whether you want to see the copyright notice during startup. Default is `on&#8217;, as you probably noticed.</dl>
</dl>
<p> <code>status [ top | up | down | bottom ] [ left | right ]</code></p>
<dl>
<dt>
<dd>
<p> The status window by default is in bottom-left corner. This command can move status messages to any corner of the screen. <code>top</code> is the same as <code>up</code>, <code>down</code> is the same as <code>bottom</code>.</dl>
<dl>
<dt><code>stuff </code>[<i>string</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Stuff the string <i>string</i> in the input buffer of the current window. This is like the paste command but with much less overhead. Without a parameter, screen will prompt for a string to stuff. You cannot paste large buffers with the stuff command. It is most useful for key bindings. See also bindkey.</dl>
<dt><i></i><code>su </code>[<i>username</i> [<i>password</i> [<i>password2</i>]]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Substitute the user of a display. The command prompts for all parameters that are omitted. If passwords are specified as parameters, they have to be specified un-crypted. The first password is matched against the systems passwd database, the second password is matched against the <i>screen</i> password as set with the commands acladd or password. Su may be useful for the <i>screen</i> administrator to test multiuser setups. When the identification fails, the user has access to the commands available for user <code>nobody</code>. These are detach, license, version, help and displays.</dl>
<dt><code>suspend</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Suspend <i>screen</i>. The windows are in the `detached&#8217; state, while <i>screen</i> is suspended. This feature relies on the shell being able to do job control.</dl>
<dt><code>term </code><i>term</i></p>
<dd>
<dl>
<dt>
<dd>
<p> In each window&#8217;s environment <i>screen</i> opens, the $TERM variable is set to screen by default. But when no description for screen is installed in the local termcap or terminfo data base, you set $TERM to &#8211; say &#8211; vt100. This won&#8217;t do much harm, as <i>screen</i> is VT100/ANSI compatible. The use of the term command is discouraged for non-default purpose. That is, one may want to specify special $TERM settings (e.g. vt100) for the next screen rlogin othermachine command. Use the command screen -T vt100 rlogin othermachine rather than setting and resetting the default.</dl>
<dt><code>termcap</code><i> term terminal-tweaks</i>[<i>window-tweaks</i><i>]</i></p>
<dd>
<dt><code>terminfo</code><i> term terminal-tweaks</i>[<i>window-tweaks</i><i>]</i></p>
<dd>
<dt><code>termcapinfo</code><i> term terminal-tweaks</i>[<i>window-tweaks</i><i>]</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Use this command to modify your terminal&#8217;s termcap entry without going through all the hassles involved in creating a custom termcap entry. Plus, you can optionally customize the termcap generated for the windows. You have to place these commands in one of the screenrc startup files, as they are meaningless once the terminal emulator is booted. </p>
<p> If your system uses the terminfo database rather than termcap, <i>screen </i> will understand the `terminfo&#8217; command, which has the same effects as the `termcap&#8217; command. Two separate commands are provided, as there are subtle syntactic differences, e.g. when parameter interpolation (using `%&#8217;) is required. Note that termcap names of the capabilities have to be used with the `terminfo&#8217; command. </p>
<p> In many cases, where the arguments are valid in both terminfo and termcap syntax, you can use the command `termcapinfo&#8217;, which is just a shorthand for a pair of `termcap&#8217; and `terminfo&#8217; commands with identical arguments. </p>
<p> The first argument specifies which terminal(s) should be affected by this definition. You can specify multiple terminal names by separating them with `|&#8217;s. Use `*&#8217; to match all terminals and `vt*&#8217; to match all terminals that begin with vt. </p>
<p> Each <i>tweak</i> argument contains one or more termcap defines (separated by `:&#8217;s) to be inserted at the start of the appropriate termcap entry, enhancing it or overriding existing values. The first tweak modifies your terminal&#8217;s termcap, and contains definitions that your terminal uses to perform certain functions. Specify a null string to leave this unchanged (e.g. &#8221;). The second (optional) tweak modifies all the window termcaps, and should contain definitions that <i>screen</i> understands (see the VIRTUAL TERMINAL section). </p>
<p> Some examples:</p>
<dl>
<dt>
<dd> termcap xterm* LP:hs@</dl>
<p> Informs <i>screen</i> that all terminals that begin with `xterm&#8217; have firm auto-margins that allow the last position on the screen to be updated (LP), but they don&#8217;t really have a status line (no &#8216;hs&#8217; &#8211; append `@&#8217; to turn entries off). Note that we assume `LP&#8217; for all terminal names that start with vt, but only if you don&#8217;t specify a termcap command for that terminal.</p>
<dl>
<dt>
<dd>
<pre>
termcap vt*  LP
</pre>
</dl>
<p> termcap vt102|vt220 Z0=\E[?3h:Z1=\E[?3l </p>
<p> Specifies the firm-margined `LP&#8217; capability for all terminals that begin with `vt&#8217;, and the second line will also add the escape-sequences to switch into (Z0) and back out of (Z1) 132-character-per-line mode if this is a VT102 or VT220. (You must specify Z0 and Z1 in your termcap to use the width-changing commands.)</p>
<dl>
<dt>
<dd> termcap vt100 &quot;&quot; l0=PF1:l1=PF2:l2=PF3:l3=PF4</dl>
<p> This leaves your vt100 termcap alone and adds the function key labels to each window&#8217;s termcap entry.</p>
<dl>
<dt>
<dd> termcap h19|z19 am@:im=\E@:ei=\EO dc=\E[P</dl>
<p> Takes a h19 or z19 termcap and turns off auto-margins (am@) and enables the insert mode (im) and end-insert (ei) capabilities (the `@&#8217; in the `im&#8217; string is after the `=&#8217;, so it is part of the string). Having the `im&#8217; and `ei&#8217; definitions put into your terminal&#8217;s termcap will cause <i>screen</i> to automatically advertise the character-insert capability in each window&#8217;s termcap. Each window will also get the delete-character capability (dc) added to its termcap, which <i>screen</i> will translate into a line-update for the terminal (we&#8217;re pretending it doesn&#8217;t support character deletion). </p>
<p> If you would like to fully specify each window&#8217;s termcap entry, you should instead set the $SCREENCAP variable prior to running <i>screen</i>. See the discussion on the VIRTUAL TERMINAL in this manual, and the <a href="/docs/linux/man/5-termcap/">termcap</a>(5) man page for more information on termcap definitions.</dl>
<dt><code>time</code></p>
<dd> [<i>string</i>]</p>
<dl>
<dt>
<dd>
<p> Uses the message line to display the time of day, the host name, and the load averages over 1, 5, and 15 minutes (if this is available on your system). For window specific information, use info. </p>
<p> If a string is specified, it changes the format of the time report like it is described in the STRING ESCAPES chapter. Screen uses a default of &quot;%c:%s %M %d %H%? %l%?&quot;.</dl>
<dt><code>title </code>[<i>windowtitle</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Set the name of the current window to <i>windowtitle</i>. If no name is specified, <i>screen</i> prompts for one. This command was known as `aka&#8217; in previous releases.</dl>
<dt><code>unbindall </code></p>
<dd>
<dl>
<dt>
<dd>
<p> Unbind all the bindings. This can be useful when screen is used solely for its detaching abilities, such as when letting a console application run as a daemon. If, for some reason, it is necessary to bind commands after this, use &#8216;screen -X&#8217;.</dl>
<dt><code>unsetenv </code><i>var</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Unset an environment variable.</dl>
<dt><code>utf8 [ on | off [ on | off ]]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Change the encoding used in the current window. If utf8 is enabled, the strings sent to the window will be UTF-8 encoded and vice versa. Omitting the parameter toggles the setting. If a second parameter is given, the display&#8217;s encoding is also changed (this should rather be done with screen&#8217;s -U option). See also defutf8, which changes the default setting of a new window.</dl>
<dt><code>vbell [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sets the visual bell setting for this window. Omitting the parameter toggles the setting. If vbell is switched on, but your terminal does not support a visual bell, a `vbell-message&#8217; is displayed in the status line when the bell character (^G) is received. Visual bell support of a terminal is defined by the termcap variable `vb&#8217; (terminfo: &#8216;flash&#8217;). </p>
<p> Per default, vbell is off, thus the audible bell is used. See also `bell_msg&#8217;.</dl>
<dt><i></i><code>vbell_msg</code> [<i>message</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Sets the visual bell message. <i>message</i> is printed to the status line if the window receives a bell character (^G), vbell is set to on, but the terminal does not support a visual bell. The default message is Wuff, Wuff!!. Without a parameter, the current message is shown.</dl>
<dt><code>vbellwait </code><i>sec</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Define a delay in seconds after each display of <i>screen</i>&#8216;s visual bell message. The default is 1 second.</dl>
<dt><code>verbose [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> If verbose is switched on, the command name is echoed, whenever a window is created (or resurrected from zombie state). Default is off. Without a parameter, the current setting is shown.</dl>
<dt><code>version</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Print the current version and the compile date in the status line.</dl>
<dt><code>wall </code><i>message</i></p>
<dd>
<dl>
<dt>
<dd>
<p> Write a message to all displays. The message will appear in the terminal&#8217;s status line.</dl>
<dt><code>width </code>[<code>-w</code>|<code>-d</code>] [<i>cols</i> [<i>lines</i>]]</p>
<dd>
<dl>
<dt>
<dd>
<p> Toggle the window width between 80 and 132 columns or set it to <i>cols</i> columns if an argument is specified. This requires a capable terminal and the termcap entries Z0 and Z1. See the termcap command for more information. You can also specify a new height if you want to change both values. The <code>-w</code> option tells screen to leave the display size unchanged and just set the window size, <code>-d</code> vice versa.</dl>
<dt><code>windowlist [ -b ] [ -m ] [ -g ]</code></p>
<dd>
<dt><i></i><code>windowlist string</code> [<i>string</i>]</p>
<dd>
<dt><i></i><code>windowlist title</code> [<i>title</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Display all windows in a table for visual window selection. If screen was in a window group, screen will back out of the group and then display the windows in that group. If the <code>-b</code> option is given, screen will switch to the blank window before presenting the list, so that the current window is also selectable. The <code>-m</code> option changes the order of the windows, instead of sorting by window numbers screen uses its internal most-recently-used list. The <code>-g</code> option will show the windows inside any groups in that level and downwards. </p>
<p> The following keys are used to navigate in windowlist: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>k</code>, <code>C-p</code>, or <code>up</code></td>
<td>Move up one line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>j</code>, <code>C-n</code>, or <code>down</code></td>
<td>Move down one line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-g</code> or <code>escape</code></td>
<td>Exit windowlist.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-a</code> or <code>home</code></td>
<td>Move to the first line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-e</code> or <code>end</code></td>
<td>Move to the last line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-u</code> or <code>C-d</code></td>
<td>Move one half page up or down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-b</code> or <code>C-f</code></td>
<td>Move one full page up or down.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>0..9</code></td>
<td>Using the number keys, move to the selected line.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>mouseclick</code></td>
<td> Move to the selected line. Available when mousetrack is set to on
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>/</code></td>
<td>Search.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>n</code></td>
<td>Repeat search in the forward direction.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>N</code></td>
<td>Repeat search in the backward direction.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>m</code></td>
<td>Toggle MRU.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>g</code></td>
<td>Toggle group nesting.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>a</code></td>
<td>All window view.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>C-h</code> or backspace</td>
<td>Back out the group.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>,</code></td>
<td>Switch numbers with the previous window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>.</code></td>
<td>Switch numbers with the next window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>K</code></td>
<td>Kill that window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>space</code> or <code>enter</code></td>
<td>Select that window.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p> The table format can be changed with the <code>string</code> and <code>title</code> option, the title is displayed as table heading, while the lines are made by using the string setting. The default setting is Num Name%=Flags for the title and %3n %t%=%f for the lines. See the STRING ESCAPES chapter for more codes (e.g. color settings). </p>
<p> Windowlist needs a region size of at least 10 characters wide and 6 characters high in order to display.</dl>
<dt><code>windows [ string ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Uses the message line to display a list of all the windows. Each window is listed by number with the name of process that has been started in the window (or its title); the current window is marked with a `*&#8217;; the previous window is marked with a `-&#8216;; all the windows that are logged in are marked with a `$&#8217;; a background window that has received a bell is marked with a `!&#8217;; a background window that is being monitored and has had activity occur is marked with an `@&#8217;; a window which has output logging turned on is marked with `(L)&#8217;; windows occupied by other users are marked with `&amp;&#8217;; windows in the zombie state are marked with `Z&#8217;. If this list is too long to fit on the terminal&#8217;s status line only the portion around the current window is displayed. The optional string parameter follows the STRING ESCAPES format. If string parameter is passed, the output size is unlimited. The default command without any parameter is limited to a size of 1024 bytes.</dl>
<dt><code>wrap [ on | off ]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Sets the line-wrap setting for the current window. When line-wrap is on, the second consecutive printable character output at the last column of a line will wrap to the start of the following line. As an added feature, backspace (^H) will also wrap through the left margin to the previous line. Default is `on&#8217;. Without any options, the state of wrap is toggled.</dl>
<dt><code>writebuf </code>[<code>-e</code> <i>encoding</i>] [<i>filename</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Writes the contents of the paste buffer to the specified file, or the public accessible screen-exchange file if no filename is given. This is thought of as a primitive means of communication between <i>screen</i> users on the same host. If an encoding is specified the paste buffer is recoded on the fly to match the encoding. The filename can be set with the <i>bufferfile</i> command and defaults to /tmp/screen-exchange.</dl>
<dt><code>writelock [ on | off | auto]</code></p>
<dd>
<dl>
<dt>
<dd>
<p> In addition to access control lists, not all users may be able to write to the same window at once. Per default, writelock is in `auto&#8217; mode and grants exclusive input permission to the user who is the first to switch to the particular window. When he leaves the window, other users may obtain the writelock (automatically). The writelock of the current window is disabled by the command writelock off. If the user issues the command writelock on he keeps the exclusive write permission while switching to other windows.</dl>
<dt><code>xoff</code></p>
<dd>
<dt><code>xon</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Insert a CTRL-s / CTRL-q character to the stdin queue of the current window.</dl>
<dt><code>zmodem [ off | auto | catch | pass ]</code></p>
<dd>
<dt><i></i><code>zmodem sendcmd</code> [<i>string</i>]</p>
<dd>
<dt><i></i><code>zmodem recvcmd</code> [<i>string</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Define zmodem support for screen. Screen understands two different modes when it detects a zmodem request: pass and catch. If the mode is set to pass, screen will relay all data to the attacher until the end of the transmission is reached. In catch mode screen acts as a zmodem endpoint and starts the corresponding rz/sz commands. If the mode is set to auto, screen will use catch if the window is a tty (e.g. a serial line), otherwise it will use pass. </p>
<p> You can define the templates screen uses in catch mode via the second and the third form. </p>
<p> Note also that this is an experimental feature.</dl>
<dt><code>zombie </code>[<i>keys</i><code>[</code>onerror<code>]</code>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Per default <i>screen </i> windows are removed from the window list as soon as the windows process (e.g. shell) exits. When a string of two keys is specified to the zombie command, `dead&#8217; windows will remain in the list. The <code>kill</code> command may be used to remove such a window. Pressing the first key in the dead window has the same effect. When pressing the second key, <i>screen </i> will attempt to resurrect the window. The process that was initially running in the window will be launched again. Calling <code>zombie</code> without parameters will clear the zombie setting, thus making windows disappear when their process exits. </p>
<p> As the zombie-setting is manipulated globally for all windows, this command should probably be called <code>defzombie</code>, but it isn&#8217;t. </p>
<p> Optionally you can put the word onerror after the keys. This will cause screen to monitor exit status of the process running in the window. If it exits normally (&#8216;0&#8217;), the window disappears. Any other exit value causes the window to become a zombie.</dl>
<dt><code>zombie_timeout</code>[<i>seconds</i>]</p>
<dd>
<dl>
<dt>
<dd>
<p> Per default <i>screen</i> windows are removed from the window list as soon as the windows process (e.g. shell) exits. If <code>zombie</code> keys are defined (compare with above <code>zombie</code> command), it is possible to also set a timeout when screen tries to automatically reconnect a dead screen window.</dl>
</dl>
</dl>
</dl>
<h2>THE MESSAGE LINE</h2>
<p> <i>Screen</i> displays informational messages and other diagnostics in a <i>message line</i>. While this line is distributed to appear at the bottom of the screen, it can be defined to appear at the top of the screen during compilation. If your terminal has a status line defined in its termcap, <i>screen</i> will use this for displaying its messages, otherwise a line of the current screen will be temporarily overwritten and output will be momentarily interrupted. The message line is automatically removed after a few seconds delay, but it can also be removed early (on terminals without a status line) by beginning to type. </p>
<p> The message line facility can be used by an application running in the current window by means of the ANSI <i>Privacy message</i> control sequence. For instance, from within the shell, try something like:</p>
<dl>
<dt>
<dd> echo &#8216;&lt;esc&gt;^Hello world from window &#8216;$WINDOW'&lt;esc&gt;\&#8217;</dl>
<p> where &#8216;&lt;esc&gt;&#8217; is an <i>escape</i>, &#8216;^&#8217; is a literal up-arrow, and &#8216;\&#8217; turns into a single backslash. </p>
<h2>WINDOW TYPES</h2>
<p> Screen provides three different window types. New windows are created with <i>screen</i>&#8216;s <code>screen</code> command (see also the entry in chapter CUSTOMIZATION). The first parameter to the <code>screen</code> command defines which type of window is created. The different window types are all special cases of the normal type. They have been added in order to allow <i>screen </i> to be used efficiently as a console multiplexer with 100 or more windows. </p>
<dl>
<dt>&bull;</p>
<dd> The normal window contains a shell (default, if no parameter is given) or any other system command that could be executed from a shell (e.g. <code>slogin</code>, etc&#8230;) </p>
<dt>&bull;</p>
<dd> If a tty (character special device) name (e.g. /dev/ttya) is specified as the first parameter, then the window is directly connected to this device. This window type is similar to screen cu -l /dev/ttya. Read and write access is required on the device node, an exclusive open is attempted on the node to mark the connection line as busy. An optional parameter is allowed consisting of a comma separated list of flags in the notation used by <a href="/docs/linux/man/1-stty/">stty</a>(1):</p>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;baud_rate&gt;</p>
<dd> Usually 300, 1200, 9600 or 19200. This affects transmission as well as receive speed.</p>
<dt>cs8 or cs7</p>
<dd> Specify the transmission of eight (or seven) bits per byte.</p>
<dt>ixon or -ixon</p>
<dd> Enables (or disables) software flow-control (CTRL-S/CTRL-Q) for sending data.</p>
<dt>ixoff or -ixoff</p>
<dd> Enables (or disables) software flow-control for receiving data.</p>
<dt>istrip or -istrip</p>
<dd> Clear (or keep) the eight bit in each received byte.</dl>
<p> You may want to specify as many of these options as applicable. Unspecified options cause the terminal driver to make up the parameter values of the connection. These values are system dependent and may be in defaults or values saved from a previous connection. </p>
<p> For tty windows, the <code>info</code> command shows some of the modem control lines in the status line. These may include `RTS&#8217;, `CTS&#8217;, &#8216;DTR&#8217;, `DSR&#8217;, `CD&#8217; and more. This depends on the available ioctl()&#8217;s and system header files as well as the on the physical capabilities of the serial board. Signals that are logical low (inactive) have their name preceded by an exclamation mark (!), otherwise the signal is logical high (active). Signals not supported by the hardware but available to the ioctl() interface are usually shown low. </p>
<p> When the CLOCAL status bit is true, the whole set of modem signals is placed inside curly braces ({ and }). When the CRTSCTS or TIOCSOFTCAR bit is set, the signals `CTS&#8217; or `CD&#8217; are shown in parenthesis, respectively. </p>
<p> For tty windows, the command <code>break</code> causes the Data transmission line (TxD) to go low for a specified period of time. This is expected to be interpreted as break signal on the other side. No data is sent and no modem control line is changed when a <code>break</code> is issued.</dl>
<dt>&bull;</p>
<dd> If the first parameter is //telnet, the second parameter is expected to be a host name, and an optional third parameter may specify a TCP port number (default decimal 23). Screen will connect to a server listening on the remote host and use the telnet protocol to communicate with that server.</dl>
<p> For telnet windows, the command <code>info</code> shows details about the connection in square brackets ([ and ]) at the end of the status line.</p>
<dl>
<dt>
<dd>
<dl>
<dt>b</p>
<dd> BINARY. The connection is in binary mode.</p>
<dt>e</p>
<dd> ECHO. Local echo is disabled.</p>
<dt>c</p>
<dd> SGA. The connection is in `character mode&#8217; (default: `line mode&#8217;).</p>
<dt>t</p>
<dd> TTYPE. The terminal type has been requested by the remote host. Screen sends the name screen unless instructed otherwise (see also the command `term&#8217;).</p>
<dt>w</p>
<dd> NAWS. The remote site is notified about window size changes.</p>
<dt>f</p>
<dd> LFLOW. The remote host will send flow control information. (Ignored at the moment.)</dl>
<p> Additional flags for debugging are x, t and n (XDISPLOC, TSPEED and NEWENV). </p>
<p> For telnet windows, the command <code>break</code> sends the telnet code IAC BREAK (decimal 243) to the remote host. </p>
<p> This window type is only available if <i>screen</i> was compiled with the ENABLE_TELNET option defined.</dl>
<h2>STRING ESCAPES</h2>
<p> Screen provides an escape mechanism to insert information like the current time into messages or file names. The escape character is &#8216;%&#8217; with one exception: inside of a window&#8217;s hardstatus &#8216;^%&#8217; (&#8216;^E&#8217;) is used instead. </p>
<p> Here is the full list of supported escapes:</p>
<dl>
<dt>%</p>
<dd> the escape character itself</p>
<dt>E</p>
<dd> sets %? to true if the escape character has been pressed.</p>
<dt>e</p>
<dd> encoding</p>
<dt>f</p>
<dd> flags of the window, see windows for meanings of the various flags</p>
<dt>F</p>
<dd> sets %? to true if the window has the focus</p>
<dt>h</p>
<dd> hardstatus of the window</p>
<dt>H</p>
<dd> hostname of the system</p>
<dt>n</p>
<dd> window number</p>
<dt>P</p>
<dd> sets %? to true if the current region is in copy/paste mode</p>
<dt>S</p>
<dd> session name</p>
<dt>s</p>
<dd> window size</p>
<dt>t</p>
<dd> window title</p>
<dt>u</p>
<dd> all other users on this window</p>
<dt>w</p>
<dd> all window numbers and names. With &#8216;-&#8216; qualifier: up to the current window; with &#8216;+&#8217; qualifier: starting with the window after the current one.</p>
<dt>W</p>
<dd> all window numbers and names except the current one</p>
<dt>x</p>
<dd> the executed command including arguments running in this windows</p>
<dt>X</p>
<dd> the executed command without arguments running in this windows</p>
<dt>?</p>
<dd> the part to the next &#8216;%?&#8217; is displayed only if a &#8216;%&#8217; escape inside the part expands to a non-empty string</p>
<dt>:</p>
<dd> else part of &#8216;%?&#8217;</p>
<dt>=</p>
<dd> pad the string to the display&#8217;s width (like TeX&#8217;s hfill). If a number is specified, pad to the percentage of the window&#8217;s width. A &#8216;0&#8217; qualifier tells screen to treat the number as absolute position. You can specify to pad relative to the last absolute pad position by adding a &#8216;+&#8217; qualifier or to pad relative to the right margin by using &#8216;-&#8216;. The padding truncates the string if the specified position lies before the current position. Add the &#8216;L&#8217; qualifier to change this.</p>
<dt>&lt;</p>
<dd> same as &#8216;%=&#8217; but just do truncation, do not fill with spaces</p>
<dt>&gt;</p>
<dd> mark the current text position for the next truncation. When screen needs to do truncation, it tries to do it in a way that the marked position gets moved to the specified percentage of the output area. (The area starts from the last absolute pad position and ends with the position specified by the truncation operator.) The &#8216;L&#8217; qualifier tells screen to mark the truncated parts with &#8216;&#8230;&#8217;.</p>
<dt>{</p>
<dd> attribute/color modifier string terminated by the next }</p>
<dt>`</p>
<dd> Substitute with the output of a &#8216;backtick&#8217; command. The length qualifier is misused to identify one of the commands.</dl>
<p> The &#8216;c&#8217; and &#8216;C&#8217; escape may be qualified with a &#8216;0&#8217; to make <i>screen </i> use zero instead of space as fill character. The &#8216;0&#8217; qualifier also makes the &#8216;=&#8217; escape use absolute positions. The &#8216;n&#8217; and &#8216;=&#8217; escapes understand a length qualifier (e.g. &#8216;%3n&#8217;), &#8216;D&#8217; and &#8216;M&#8217; can be prefixed with &#8216;L&#8217; to generate long names, &#8216;w&#8217; and &#8216;W&#8217; also show the window flags if &#8216;L&#8217; is given. </p>
<p> An attribute/color modifier is used to change the attributes or the color settings. Its format is [attribute modifier] [color description]. The attribute modifier must be prefixed by a change type indicator if it can be confused with a color description. The following change types are known:</p>
<dl>
<dt>+</p>
<dd> add the specified set to the current attributes</p>
<dt>&#8211;</p>
<dd> remove the set from the current attributes</p>
<dt>!</p>
<dd> invert the set in the current attributes</p>
<dt>=</p>
<dd> change the current attributes to the specified set</dl>
<p> The attribute set can either be specified as a hexadecimal number or a combination of the following letters:</p>
<dl>
<dt>d</p>
<dd> dim</p>
<dt>u</p>
<dd> underline</p>
<dt>b</p>
<dd> bold</p>
<dt>r</p>
<dd> reverse</p>
<dt>s</p>
<dd> /standout</p>
<dt>B</p>
<dd> blinking</dl>
<p> Colors are coded either as a hexadecimal number or two letters specifying the desired background and foreground color (in that order). The following colors are known:</p>
<dl>
<dt>k</p>
<dd> black</p>
<dt>r</p>
<dd> red</p>
<dt>g</p>
<dd> green</p>
<dt>y</p>
<dd> yellow</p>
<dt>b</p>
<dd> blue</p>
<dt>m</p>
<dd> magenta</p>
<dt>c</p>
<dd> cyan</p>
<dt>w</p>
<dd> white</p>
<dt>d</p>
<dd> default color</p>
<dt>.</p>
<dd> leave color unchanged</dl>
<p> The capitalized versions of the letter specify bright colors. You can also use the pseudo-color &#8216;i&#8217; to set just the brightness and leave the color unchanged.<br />
 A one digit/letter color description is treated as foreground or background color dependent on the current attributes: if reverse mode is set, the background color is changed instead of the foreground color. If you don&#8217;t like this, prefix the color with a .. If you want the same behavior for two-letter color descriptions, also prefix them with a ..<br />
 As a special case, %{-} restores the attributes and colors that were set before the last change was made (i.e., pops one level of the color-change stack). </p>
<p> Examples:</p>
<dl>
<dt>G</p>
<dd> set color to bright green</p>
<dt>+b r</p>
<dd> use bold red</p>
<dt>= yd</p>
<dd> clear all attributes, write in default color on yellow background.</p>
<dt>%-Lw%{= BW}%50&gt;%n%f* %t%{-}%+Lw%&lt;</p>
<dd> The available windows centered at the current window and truncated to the available width. The current window is displayed white on blue. This can be used with hardstatus alwayslastline.</p>
<dt>%?%F%{.R.}%?%3n %t%? [%h]%?</p>
<dd> The window number and title and the window&#8217;s hardstatus, if one is set. Also use a red background if this is the active focus. Useful for caption string.</dl>
<h2>FLOW-CONTROL</h2>
<p> Each window has a flow-control setting that determines how <i>screen</i> deals with the XON and XOFF characters (and perhaps the interrupt character). When flow-control is turned off, <i>screen</i> ignores the XON and XOFF characters, which allows the user to send them to the current program by simply typing them (useful for the <i>emacs</i> editor, for instance). The trade-off is that it will take longer for output from a normal program to pause in response to an XOFF. With flow-control turned on, XON and XOFF characters are used to immediately pause the output of the current window. You can still send these characters to the current program, but you must use the appropriate two-character <i>screen</i> commands (typically C-a q (xon) and C-a s (xoff)). The xon/xoff commands are also useful for typing C-s and C-q past a terminal that intercepts these characters. </p>
<p> Each window has an initial flow-control value set with either the <code>-f</code> option or the defflow .screenrc command. Per default the windows are set to automatic flow-switching. It can then be toggled between the three states &#8216;fixed on&#8217;, &#8216;fixed off&#8217; and &#8216;automatic&#8217; interactively with the flow command bound to &quot;C-a f&quot;. </p>
<p> The automatic flow-switching mode deals with flow control using the TIOCPKT mode (like rlogin does). If the tty driver does not support TIOCPKT, <i>screen</i> tries to find out the right mode based on the current setting of the application keypad &#8211; when it is enabled, flow-control is turned off and visa versa. Of course, you can still manipulate flow-control manually when needed. </p>
<p> If you&#8217;re running with flow-control enabled and find that pressing the interrupt key (usually C-c) does not interrupt the display until another 6-8 lines have scrolled by, try running <i>screen</i> with the interrupt option (add the interrupt flag to the flow command in your .screenrc, or use the <code>-i</code> command-line option). This causes the output that <i>screen</i> has accumulated from the interrupted program to be flushed. One disadvantage is that the virtual terminal&#8217;s memory contains the non-flushed version of the output, which in rare cases can cause minor inaccuracies in the output. For example, if you switch screens and return, or update the screen with C-a l you would see the version of the output you would have gotten without interrupt being on. Also, you might need to turn off flow-control (or use auto-flow mode to turn it off automatically) when running a program that expects you to type the interrupt character as input, as it is possible to interrupt the output of the virtual terminal to your physical terminal when flow-control is enabled. If this happens, a simple refresh of the screen with C-a l will restore it. Give each mode a try, and use whichever mode you find more comfortable. </p>
<h2>TITLES (naming windows)</h2>
<p> You can customize each window&#8217;s name in the window display (viewed with the windows command (C-a w)) by setting it with one of the title commands. Normally the name displayed is the actual command name of the program created in the window. However, it is sometimes useful to distinguish various programs of the same name or to change the name on-the-fly to reflect the current state of the window. </p>
<p> The default name for all shell windows can be set with the shelltitle command in the .screenrc file, while all other windows are created with a screen command and thus can have their name set with the <code>-t</code> option. Interactively, there is the title-string escape-sequence (&lt;esc&gt;k<i>name</i>&lt;esc&gt;\) and the title command (C-a A). The former can be output from an application to control the window&#8217;s name under software control, and the latter will prompt for a name when typed. You can also bind pre-defined names to keys with the title command to set things quickly without prompting. Changing title by this escape sequence can be controlled by <code>defdynamictitle</code> and <code>dynamictitle</code> commands. </p>
<p> Finally, <i>screen</i> has a shell-specific heuristic that is enabled by setting the window&#8217;s name to <i>search|name</i> and arranging to have a null title escape-sequence output as a part of your prompt. The <i>search</i> portion specifies an end-of-prompt search string, while the <i>name</i> portion specifies the default shell name for the window. If the <i>name</i> ends in a `:&#8217; <i>screen</i> will add what it believes to be the current command running in the window to the end of the window&#8217;s shell name (e.g. <i>name:cmd</i>). Otherwise the current command name supersedes the shell name while it is running. </p>
<p> Here&#8217;s how it works: you must modify your shell prompt to output a null title-escape-sequence (&lt;esc&gt;k&lt;esc&gt;\) as a part of your prompt. The last part of your prompt must be the same as the string you specified for the <i>search</i> portion of the title. Once this is set up, <i>screen</i> will use the title-escape-sequence to clear the previous command name and get ready for the next command. Then, when a newline is received from the shell, a search is made for the end of the prompt. If found, it will grab the first word after the matched string and use it as the command name. If the command name begins with either &#8216;!&#8217;, &#8216;%&#8217;, or &#8216;^&#8217; <i>screen</i> will use the first word on the following line (if found) in preference to the just-found name. This helps csh users get better command names when using job control or history recall commands. </p>
<p> Here&#8217;s some .screenrc examples: </p>
<pre>
            screen -t top 2 nice top
</pre>
<p> Adding this line to your .screenrc would start a nice-d version of the top command in window 2 named top rather than nice. </p>
<pre>
            shelltitle '&gt; |csh'
            screen 1
</pre>
<p> These commands would start a shell with the given shelltitle. The title specified is an auto-title that would expect the prompt and the typed command to look something like the following: </p>
<pre>
            /usr/joe/src/dir&gt; trn
</pre>
<p> (it looks after the &#8216;&gt; &#8216; for the command name). The window status would show the name trn while the command was running, and revert to csh upon completion. </p>
<pre>
            bind R screen -t '% |root:' su
</pre>
<p> Having this command in your .screenrc would bind the key sequence C-a R to the su command and give it an auto-title name of root:. For this auto-title to work, the screen could look something like this: </p>
<pre>
            % !em
            emacs file.c
</pre>
<p> Here the user typed the csh history command !em which ran the previously entered emacs command. The window status would show root:emacs during the execution of the command, and revert to simply root: at its completion. </p>
<pre>
            bind o title
            bind E title &quot;&quot;
            bind u title (unknown)
</pre>
<p> The first binding doesn&#8217;t have any arguments, so it would prompt you for a title when you type C-a o. The second binding would clear an auto-title&#8217;s current setting (C-a E). The third binding would set the current window&#8217;s title to (unknown) (C-a u). </p>
<p> One thing to keep in mind when adding a null title-escape-sequence to your prompt is that some shells (like the csh) count all the non-control characters as part of the prompt&#8217;s length. If these invisible characters aren&#8217;t a multiple of 8 then backspacing over a tab will result in an incorrect display. One way to get around this is to use a prompt like this: </p>
<pre><code>
set prompt = '^[[0000m^[k^[\% '
</code></pre>
<p> The escape-sequence &lt;esc&gt;[0000m not only normalizes the character attributes, but all the zeros round the length of the invisible characters up to 8. Bash users will probably want to echo the escape sequence in the PROMPT_COMMAND: </p>
<pre>
            PROMPT_COMMAND='printf &quot;k\134&quot;'
</pre>
<p> (I used \134 to output a `\&#8217; because of a bug in bash v1.04). </p>
<h2>THE VIRTUAL TERMINAL</h2>
<p> Each window in a <i>screen</i> session emulates a VT100 terminal, with some extra functions added. The VT100 emulator is hard-coded, no other terminal types can be emulated.<br />
 Usually <i>screen</i> tries to emulate as much of the VT100/ANSI standard as possible. But if your terminal lacks certain capabilities, the emulation may not be complete. In these cases <i>screen</i> has to tell the applications that some of the features are missing. This is no problem on machines using termcap, because <i>screen</i> can use the $TERMCAP variable to customize the standard <i>screen</i> termcap. </p>
<p> But if you do a rlogin on another machine or your machine supports only terminfo this method fails. Because of this, <i>screen</i> offers a way to deal with these cases. Here is how it works: </p>
<p> When <i>screen</i> tries to figure out a terminal name for itself, it first looks for an entry named screen.&lt;term&gt;, where &lt;term&gt; is the contents of your $TERM variable. If no such entry exists, <i>screen</i> tries screen (or screen-w if the terminal is wide (132 cols or more)). If even this entry cannot be found, vt100 is used as a substitute. </p>
<p> The idea is that if you have a terminal which doesn&#8217;t support an important feature (e.g. delete char or clear to EOS) you can build a new termcap/terminfo entry for <i>screen</i> (named screen.&lt;dumbterm&gt;) in which this capability has been disabled. If this entry is installed on your machines you are able to do a rlogin and still keep the correct termcap/terminfo entry. The terminal name is put in the $TERM variable of all new windows. <i>Screen</i> also sets the $TERMCAP variable reflecting the capabilities of the virtual terminal emulated. Notice that, however, on machines using the terminfo database this variable has no effect. Furthermore, the variable $WINDOW is set to the window number of each window. </p>
<p> The actual set of capabilities supported by the virtual terminal depends on the capabilities supported by the physical terminal. If, for instance, the physical terminal does not support underscore mode, <i>screen</i> does not put the `us&#8217; and `ue&#8217; capabilities into the window&#8217;s $TERMCAP variable, accordingly. However, a minimum number of capabilities must be supported by a terminal in order to run <i>screen</i>; namely scrolling, clear screen, and direct cursor addressing (in addition, <i>screen</i> does not run on hardcopy terminals or on terminals that over-strike). </p>
<p> Also, you can customize the $TERMCAP value used by <i>screen</i> by using the termcap .screenrc command, or by defining the variable $SCREENCAP prior to startup. When the latter is defined, its value will be copied verbatim into each window&#8217;s $TERMCAP variable. This can either be the full terminal definition, or a filename where the terminal screen (and/or screen-w) is defined. </p>
<p> Note that <i>screen</i> honors the terminfo .screenrc command if the system uses the terminfo database rather than termcap. </p>
<p> When the boolean `G0&#8242; capability is present in the termcap entry for the terminal on which <i>screen</i> has been called, the terminal emulation of <i>screen</i> supports multiple character sets. This allows an application to make use of, for instance, the VT100 graphics character set or national character sets. The following control functions from ISO 2022 are supported: <i>lock shift G0</i> (<i>SI</i>), <i>lock shift G1</i> (<i>SO</i>), <i>lock shift G2</i>, <i>lock shift G3</i>, <i>single shift G2</i>, and <i>single shift G3</i>. When a virtual terminal is created or reset, the ASCII character set is designated as <i>G0</i> through <i>G3</i>. When the `G0&#8242; capability is present, <i>screen</i> evaluates the capabilities `S0&#8242;, `E0&#8242;, and `C0&#8242; if present. `S0&#8242; is the sequence the terminal uses to enable and start the graphics character set rather than <i>SI</i>. `E0&#8242; is the corresponding replacement for <i>SO</i>. `C0&#8242; gives a character by character translation string that is used during semi-graphics mode. This string is built like the `acsc&#8217; terminfo capability. </p>
<p> When the `po&#8217; and `pf&#8217; capabilities are present in the terminal&#8217;s termcap entry, applications running in a <i>screen</i> window can send output to the printer port of the terminal. This allows a user to have an application in one window sending output to a printer connected to the terminal, while all other windows are still active (the printer port is enabled and disabled again for each chunk of output). As a side-effect, programs running in different windows can send output to the printer simultaneously. Data sent to the printer is not displayed in the window. The <i>info</i> command displays a line starting `PRIN&#8217; while the printer is active. </p>
<p> <i>Screen</i> maintains a hardstatus line for every window. If a window gets selected, the display&#8217;s hardstatus will be updated to match the window&#8217;s hardstatus line. If the display has no hardstatus the line will be displayed as a standard <i>screen </i> message. The hardstatus line can be changed with the ANSI Application Program Command (APC): ESC_&lt;string&gt;ESC\. As a convenience for xterm users the sequence ESC]0..2;&lt;string&gt;^G is also accepted. </p>
<p> Some capabilities are only put into the $TERMCAP variable of the virtual terminal if they can be efficiently implemented by the physical terminal. For instance, `dl&#8217; (delete line) is only put into the $TERMCAP variable if the terminal supports either delete line itself or scrolling regions. Note that this may provoke confusion, when the session is reattached on a different terminal, as the value of $TERMCAP cannot be modified by parent processes. </p>
<p> The &quot;alternate screen&quot; capability is not enabled by default. Set the <code>altscreen</code> .screenrc command to enable it. </p>
<p> The following is a list of control sequences recognized by <i>screen</i>. (V) and (A) indicate VT100-specific and ANSI- or ISO-specific functions, respectively. </p>
<dl>
<dt><code>ESC E</code></p>
<dd> Next Line</p>
<dt><code>ESC D</code></p>
<dd> Index</p>
<dt><code>ESC M</code></p>
<dd> Reverse Index</p>
<dt><code>ESC H</code></p>
<dd> Horizontal Tab Set</p>
<dt><code>ESC Z</code></p>
<dd> Send VT100 Identification String</p>
<dt><code>ESC 7</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Save Cursor and Attributes</p>
<dt><code>ESC 8</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Restore Cursor and Attributes</p>
<dt><code>ESC [s</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Save Cursor and Attributes</p>
<dt><code>ESC [u</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Restore Cursor and Attributes</p>
<dt><code>ESC c</code></p>
<dd> Reset to Initial State</p>
<dt><code>ESC g</code></p>
<dd> Visual Bell</p>
<dt><code>ESC </code>Pn<code> p</code></p>
<dd> Cursor Visibility (97801)</p>
<dl>
<dt>
<dd>
<dl>
<dt>Pn = <code>6</code></p>
<dd> Invisible</p>
<dt>Pn = <code>7</code></p>
<dd> Visible</dl>
</dl>
<dt><code>ESC =</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Application Keypad Mode</p>
<dt><code>ESC &gt;</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Numeric Keypad Mode</p>
<dt><code>ESC # 8</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Fill Screen with E&#8217;s</p>
<dt><code>ESC \</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> String Terminator</p>
<dt><code>ESC ^</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Privacy Message String (Message Line)</p>
<dt><code>ESC !</code></p>
<dd> Global Message String (Message Line)</p>
<dt><code>ESC k</code></p>
<dd> A.k.a. Definition String</p>
<dt><code>ESC P</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Device Control String.<br />
 Outputs a string directly to the host terminal without interpretation.</p>
<dt><code>ESC _</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Application Program Command (Hardstatus)</p>
<dt><code>ESC ] 0 ; string ^G</code>(A)</p>
<dd> Operating System Command (Hardstatus, xterm title hack)</p>
<dt><code>ESC ] 83 ; cmd ^G</code><tt>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Execute screen command. This only works if multi-user support is<br />
 compiled into screen. The pseudo-user :window: is used to check the access control list. Use addacl :window: -rwx #? to create a user with no rights and allow only the needed commands.</p>
<dt><code>Control-N</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Lock Shift G1 (SO)</p>
<dt><code>Control-O</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Lock Shift G0 (SI)</p>
<dt><code>ESC n</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Lock Shift G2</p>
<dt><code>ESC o</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Lock Shift G3</p>
<dt><code>ESC N</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Single Shift G2</p>
<dt><code>ESC O</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Single Shift G3</p>
<dt><code>ESC ( </code>Pcs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Designate character set as G0</p>
<dt><code>ESC ) </code>Pcs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Designate character set as G1</p>
<dt><code>ESC * </code>Pcs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Designate character set as G2</p>
<dt><code>ESC + </code>Pcs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Designate character set as G3</p>
<dt><code>ESC [ </code>Pn<code> ; </code>Pn<code> H</code></p>
<dd> Direct Cursor Addressing</p>
<dt><code>ESC [ </code>Pn<code> ; </code>Pn<code> f</code></p>
<dd> same as above</p>
<dt><code>ESC [ </code>Pn<code> J</code></p>
<dd> Erase in Display</p>
<dl>
<dt>
<dd>
<dl>
<dt>Pn = None or <code>0</code></p>
<dd> From Cursor to End of Screen</p>
<dt>Pn = <code>1</code></p>
<dd> From Beginning of Screen to Cursor</p>
<dt>Pn = <code>2</code></p>
<dd> Entire Screen</dl>
</dl>
<dt><code>ESC [ </code>Pn<code> K</code></p>
<dd> Erase in Line</p>
<dl>
<dt>
<dd>
<dl>
<dt>Pn = None or <code>0</code></p>
<dd> From Cursor to End of Line</p>
<dt>Pn = <code>1</code></p>
<dd> From Beginning of Line to Cursor</p>
<dt>Pn = <code>2</code></p>
<dd> Entire Line</dl>
</dl>
<dt><code>ESC [ </code>Pn<code> X</code></p>
<dd> Erase character</p>
<dt><code>ESC [ </code>Pn<code> A</code></p>
<dd> Cursor Up</p>
<dt><code>ESC [ </code>Pn<code> B</code></p>
<dd> Cursor Down</p>
<dt><code>ESC [ </code>Pn<code> C</code></p>
<dd> Cursor Right</p>
<dt><code>ESC [ </code>Pn<code> D</code></p>
<dd> Cursor Left</p>
<dt><code>ESC [ </code>Pn<code> E</code></p>
<dd> Cursor next line</p>
<dt><code>ESC [ </code>Pn<code> F</code></p>
<dd> Cursor previous line</p>
<dt><code>ESC [ </code>Pn<code> G</code></p>
<dd> Cursor horizontal position</p>
<dt><code>ESC [ </code>Pn<code> `</code></p>
<dd> same as above</p>
<dt><code>ESC [ </code>Pn<code> d</code></p>
<dd> Cursor vertical position</p>
<dt><code>ESC [ </code>Ps<code> ;</code>&#8230;<code>; </code>Ps<code> m</code></p>
<dd> Select Graphic Rendition</p>
<dl>
<dt>
<dd>
<dl>
<dt>Ps = None or <code>0</code></p>
<dd> Default Rendition</p>
<dt>Ps = <code>1</code></p>
<dd> Bold</p>
<dt>Ps = <code>2</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Faint</p>
<dt>Ps = <code>3</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> <i>Standout</i> Mode (ANSI: Italicized)</p>
<dt>Ps = <code>4</code></p>
<dd> Underlined</p>
<dt>Ps = <code>5</code></p>
<dd> Blinking</p>
<dt>Ps = <code>7</code></p>
<dd> Negative Image</p>
<dt>Ps = <code>22</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Normal Intensity</p>
<dt>Ps = <code>23</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> <i>Standout</i> Mode off (ANSI: Italicized off)</p>
<dt>Ps = <code>24</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Not Underlined</p>
<dt>Ps = <code>25</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Not Blinking</p>
<dt>Ps = <code>27</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Positive Image</p>
<dt>Ps = <code>30</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Black</p>
<dt>Ps = <code>31</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Red</p>
<dt>Ps = <code>32</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Green</p>
<dt>Ps = <code>33</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Yellow</p>
<dt>Ps = <code>34</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Blue</p>
<dt>Ps = <code>35</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Magenta</p>
<dt>Ps = <code>36</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Cyan</p>
<dt>Ps = <code>37</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground White</p>
<dt>Ps = <code>39</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Foreground Default</p>
<dt>Ps = <code>40</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Background Black</p>
<dt>Ps = <code>&#8230;</code></p>
<dd>
<dt>Ps = <code>49</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Background Default
</dl>
</dl>
<dt><code>ESC [ </code>Pn<code> g</code></p>
<dd> Tab Clear</p>
<dl>
<dt>
<dd>
<dl>
<dt>Pn = None or <code>0</code></p>
<dd> Clear Tab at Current Position</p>
<dt>Pn = <code>3</code></p>
<dd> Clear All Tabs</dl>
</dl>
<dt><code>ESC [ </code>Pn<code> ; </code>Pn<code> r</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Set Scrolling Region</p>
<dt><code>ESC [ </code>Pn<code> I</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Horizontal Tab</p>
<dt><code>ESC [ </code>Pn<code> Z</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Backward Tab</p>
<dt><code>ESC [ </code>Pn<code> L</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Insert Line</p>
<dt><code>ESC [ </code>Pn<code> M</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Delete Line</p>
<dt><code>ESC [ </code>Pn<code> @</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Insert Character</p>
<dt><code>ESC [ </code>Pn<code> P</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Delete Character</p>
<dt><code>ESC [ </code>Pn<code> S</code></p>
<dd> Scroll Scrolling Region Up</p>
<dt><code>ESC [ </code>Pn<code> T</code></p>
<dd> Scroll Scrolling Region Down</p>
<dt><code>ESC [ </code>Pn<code> ^</code></p>
<dd> same as above</p>
<dt><code>ESC [ </code>Ps<code> ;</code>&#8230;<code>; </code>Ps<code> h</code></p>
<dd> Set Mode</p>
<dt><code>ESC [ </code>Ps<code> ;</code>&#8230;<code>; </code>Ps<code> l</code></p>
<dd> Reset Mode</p>
<dl>
<dt>
<dd>
<dl>
<dt>Ps = <code>4</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Insert Mode</p>
<dt>Ps = <code>20</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> <i>Automatic Linefeed</i> Mode</p>
<dt>Ps = <code>34</code></p>
<dd> Normal Cursor Visibility</p>
<dt>Ps = <code>?1</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Application Cursor Keys</p>
<dt>Ps = <code>?3</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Change Terminal Width to 132 columns</p>
<dt>Ps = <code>?5</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Reverse Video</p>
<dt>Ps = <code>?6</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> <i>Origin</i> Mode</p>
<dt>Ps = <code>?7</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> <i>Wrap</i> Mode</p>
<dt>Ps = <code>?9</code></p>
<dd> X10 mouse tracking</p>
<dt>Ps = <code>?25</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> Visible Cursor</p>
<dt>Ps = <code>?47</code></p>
<dd> Alternate Screen (old xterm code)</p>
<dt>Ps = <code>?1000</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(V)</p>
<dd> VT200 mouse tracking</p>
<dt>Ps = <code>?1047</code></p>
<dd> Alternate Screen (new xterm code)</p>
<dt>Ps = <code>?1049</code></p>
<dd> Alternate Screen (new xterm code)</dl>
</dl>
<dt><code>ESC [ 5 i</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Start relay to printer (ANSI Media Copy)</p>
<dt><code>ESC [ 4 i</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(A)</p>
<dd> Stop relay to printer (ANSI Media Copy)</p>
<dt><code>ESC [ 8 ; </code>Ph<code> ; </code>Pw<code> t</code></p>
<dd> Resize the window to `Ph&#8217; lines and `Pw&#8217; columns (SunView special)</p>
<dt><code>ESC [ c</code></p>
<dd> Send VT100 Identification String</p>
<dt><code>ESC [ x</code></p>
<dd> Send Terminal Parameter Report</p>
<dt><code>ESC [ &gt; c</code></p>
<dd> Send VT220 Secondary Device Attributes String</p>
<dt><code>ESC [ 6 n</code></p>
<dd> Send Cursor Position Report </p>
</dl>
<h2>INPUT TRANSLATION</h2>
<p> In order to do a full VT100 emulation <i>screen</i> has to detect that a sequence of characters in the input stream was generated by a keypress on the user&#8217;s keyboard and insert the VT100 style escape sequence. <i>Screen</i> has a very flexible way of doing this by making it possible to map arbitrary commands on arbitrary sequences of characters. For standard VT100 emulation the command will always insert a string in the input buffer of the window (see also command <code>stuff</code> in the command table). Because the sequences generated by a keypress can change after a reattach from a different terminal type, it is possible to bind commands to the termcap name of the keys. <i>Screen</i> will insert the correct binding after each reattach. See the <code>bindkey</code> command for further details on the syntax and examples. </p>
<p> Here is the table of the default key bindings. The fourth is what command is executed if the keyboard is switched into application mode. </p>
<table BORDER>
<tr VALIGN=top>
<td>Key name</td>
<td>Termcap name</td>
<td>Command</td>
<td>App mode
</td>
</tr>
<tr VALIGN=top>
<td>Cursor up</td>
<td>ku</td>
<td>[A</td>
<td>OA
</td>
</tr>
<tr VALIGN=top>
<td>Cursor down</td>
<td>kd</td>
<td>[B</td>
<td>OB
</td>
</tr>
<tr VALIGN=top>
<td>Cursor right</td>
<td>kr</td>
<td>[C</td>
<td>OC
</td>
</tr>
<tr VALIGN=top>
<td>Cursor left</td>
<td>kl</td>
<td>[D</td>
<td>OD
</td>
</tr>
<tr VALIGN=top>
<td>Function key 0</td>
<td>k0</td>
<td>[10~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 1</td>
<td>k1</td>
<td>OP</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 2</td>
<td>k2</td>
<td>OQ</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 3</td>
<td>k3</td>
<td>OR</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 4</td>
<td>k4</td>
<td>OS</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 5</td>
<td>k5</td>
<td>[15~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 6</td>
<td>k6</td>
<td>[17~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 7</td>
<td>k7</td>
<td>[18~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 8</td>
<td>k8</td>
<td>[19~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 9</td>
<td>k9</td>
<td>[20~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 10</td>
<td>k;</td>
<td>[21~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 11</td>
<td>F1</td>
<td>[23~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Function key 12</td>
<td>F2</td>
<td>[24~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>kh</td>
<td>[1~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>kH</td>
<td>[4~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Insert</td>
<td>kI</td>
<td>[2~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Delete</td>
<td>kD</td>
<td>[3~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Page up</td>
<td>kP</td>
<td>[5~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Page down</td>
<td>kN</td>
<td>[6~</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 0</td>
<td>f0</td>
<td>0</td>
<td>Op
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 1</td>
<td>f1</td>
<td>1</td>
<td>Oq
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 2</td>
<td>f2</td>
<td>2</td>
<td>Or
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 3</td>
<td>f3</td>
<td>3</td>
<td>Os
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 4</td>
<td>f4</td>
<td>4</td>
<td>Ot
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 5</td>
<td>f5</td>
<td>5</td>
<td>Ou
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 6</td>
<td>f6</td>
<td>6</td>
<td>Ov
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 7</td>
<td>f7</td>
<td>7</td>
<td>Ow
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 8</td>
<td>f8</td>
<td>8</td>
<td>Ox
</td>
</tr>
<tr VALIGN=top>
<td>Keypad 9</td>
<td>f9</td>
<td>9</td>
<td>Oy
</td>
</tr>
<tr VALIGN=top>
<td>Keypad +</td>
<td>f+</td>
<td>+</td>
<td>Ok
</td>
</tr>
<tr VALIGN=top>
<td>Keypad &#8211;</td>
<td>f-</td>
<td>&#8211;</td>
<td>Om
</td>
</tr>
<tr VALIGN=top>
<td>Keypad *</td>
<td>f*</td>
<td>*</td>
<td>Oj
</td>
</tr>
<tr VALIGN=top>
<td>Keypad /</td>
<td>f/</td>
<td>/</td>
<td>Oo
</td>
</tr>
<tr VALIGN=top>
<td>Keypad =</td>
<td>fq</td>
<td>=</td>
<td>OX
</td>
</tr>
<tr VALIGN=top>
<td>Keypad .</td>
<td>f.</td>
<td>.</td>
<td>On
</td>
</tr>
<tr VALIGN=top>
<td>Keypad ,</td>
<td>f,</td>
<td>,</td>
<td>Ol
</td>
</tr>
<tr VALIGN=top>
<td>Keypad enter</td>
<td>fe</td>
<td></td>
<td>OM
</td>
</tr>
</table>
<h2>SPECIAL TERMINAL CAPABILITIES</h2>
<p> The following table describes all terminal capabilities that are recognized by <i>screen</i> and are not in the <a href="/docs/linux/man/5-termcap/">termcap</a>(5) manual. You can place these capabilities in your termcap entries (in `/etc/termcap&#8217;) or use them with the commands `termcap&#8217;, `terminfo&#8217; and `termcapinfo&#8217; in your screenrc files. It is often not possible to place these capabilities in the terminfo database. </p>
<dl>
<dt><code>LP</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Terminal has VT100 style margins (`magic margins&#8217;). Note that<br />
 this capability is obsolete because <i>screen</i> uses the standard &#8216;xn&#8217; instead.</p>
<dt><code>Z0</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Change width to 132 columns.</p>
<dt><code>Z1</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Change width to 80 columns.</p>
<dt><code>WS</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Resize display. This capability has the desired width and height as<br />
 arguments. <i>SunView(tm)</i> example: &#8216;\E[8;%d;%dt&#8217;.</p>
<dt><code>NF</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Terminal doesn&#8217;t need flow control. Send ^S and ^Q direct to<br />
 the application. Same as &#8216;flow off&#8217;. The opposite of this capability is &#8216;nx&#8217;.</p>
<dt><code>G0</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Terminal can deal with ISO 2022 font selection sequences.</p>
<dt><code>S0</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Switch charset &#8216;G0&#8217; to the specified charset. Default<br />
 is &#8216;\E(%.&#8217;.</p>
<dt><code>E0</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Switch charset &#8216;G0&#8217; back to standard charset. Default<br />
 is &#8216;\E(B&#8217;.</p>
<dt><code>C0</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Use the string as a conversion table for font &#8216;0&#8217;. See<br />
 the &#8216;ac&#8217; capability for more details.</p>
<dt><code>CS</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Switch cursor-keys to application mode.</p>
<dt><code>CE</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Switch cursor-keys back to normal mode.</p>
<dt><code>AN</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Turn on autonuke. See the &#8216;autonuke&#8217; command for more details.</p>
<dt><code>OL</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(num)</i></p>
<dd> Set the output buffer limit. See the &#8216;obuflimit&#8217; command for more details.</p>
<dt><code>KJ</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Set the encoding of the terminal. See the &#8216;encoding&#8217; command for<br />
 valid encodings.</p>
<dt><code>AF</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Change character foreground color in an ANSI conform way. This<br />
 capability will almost always be set to &#8216;\E[3%dm&#8217; (&#8216;\E[3%p1%dm&#8217; on terminfo machines).</p>
<dt><code>AB</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Same as &#8216;AF&#8217;, but change background color.</p>
<dt><code>AX</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Does understand ANSI set default fg/bg color (\E[39m / \E[49m).</p>
<dt><code>XC</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(str)</i></p>
<dd> Describe a translation of characters to strings depending on the<br />
 current font. More details follow in the next section.</p>
<dt><code>XT</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Terminal understands special xterm sequences (OSC, mouse tracking).</p>
<dt><code>C8</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Terminal needs bold to display high-intensity colors (e.g. Eterm).</p>
<dt><code>TF</code><i><tt>&nbsp;<wbr>&nbsp;</tt>(bool)</i></p>
<dd> Add missing capabilities to the termcap/info entry. (Set by default).</p>
</dl>
<h2>CHARACTER TRANSLATION</h2>
<p> <i>Screen</i> has a powerful mechanism to translate characters to arbitrary strings depending on the current font and terminal type. Use this feature if you want to work with a common standard character set (say ISO8851-latin1) even on terminals that scatter the more unusual characters over several national language font pages. </p>
<p> Syntax:<br />
XC = &lt;charset &#8211; mapping&gt;{, , &lt;charset &#8211; mapping&gt;}&lt;charset &#8211; mapping&gt; : = &lt;designator&gt;&lt;template&gt;{, &lt;mapping&gt;}&lt;mapping&gt; : = &lt;char &#8211; to &#8211; be &#8211; mapped&gt;&lt;template &#8211; arg&gt;</p>
<p> The things in braces may be repeated any number of times. </p>
<p> A <i>&lt;charset-mapping&gt;</i> tells <i>screen</i> how to map characters in font <i>&lt;designator&gt;</i> (&#8216;B&#8217;: Ascii, &#8216;A&#8217;: UK, &#8216;K&#8217;: German, etc.) to strings. Every <i>&lt;mapping&gt;</i> describes to what string a single character will be translated. A template mechanism is used, as most of the time the codes have a lot in common (for example strings to switch to and from another charset). Each occurrence of &#8216;%&#8217; in <i>&lt;template&gt;</i> gets substituted with the <i>&lt;template-arg&gt;</i> specified together with the character. If your strings are not similar at all, then use &#8216;%&#8217; as a template and place the full string in <i>&lt;template-arg&gt;</i>. A quoting mechanism was added to make it possible to use a real &#8216;%&#8217;. The &#8216;\&#8217; character quotes the special characters &#8216;\&#8217;, &#8216;%&#8217;, and &#8216;,&#8217;. </p>
<p> Here is an example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;termcap hp700&nbsp;&#8216;XC=B\E(K%\E(B,\304[,\326\\,\334]&#8217; </p>
<p> This tells <i>screen</i> how to translate ISOlatin1 (charset &#8216;B&#8217;) upper case umlaut characters on a hp700 terminal that has a German charset. &#8216;\304&#8217; gets translated to &#8216;\E(K[\E(B&#8217; and so on. Note that this line gets parsed *three* times before the internal lookup table is built, therefore a lot of quoting is needed to create a single &#8216;\&#8217;. </p>
<p> Another extension was added to allow more emulation: If a mapping translates the unquoted &#8216;%&#8217; char, it will be sent to the terminal whenever <i>screen</i> switches to the corresponding <i>&lt;designator&gt;</i>. In this special case the template is assumed to be just &#8216;%&#8217; because the charset switch sequence and the character mappings normally haven&#8217;t much in common. </p>
<p> This example shows one use of the extension: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;termcap xterm&nbsp;&#8216;XC=K%,%\E(B,[\304,\\\326,]\334&#8217; </p>
<p> Here, a part of the German (&#8216;K&#8217;) charset is emulated on an xterm. If <i>screen</i> has to change to the &#8216;K&#8217; charset, &#8216;\E(B&#8217; will be sent to the terminal, i.e. the ASCII charset is used instead. The template is just &#8216;%&#8217;, so the mapping is straightforward: &#8216;[&#8216; to &#8216;\304&#8217;, &#8216;\&#8217; to &#8216;\326&#8217;, and &#8216;]&#8217; to &#8216;\334&#8217;. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>COLUMNS</p>
<dd> Number of columns on the terminal (overrides termcap entry).</p>
<dt>HOME</p>
<dd> Directory in which to look for .screenrc.</p>
<dt>LINES</p>
<dd> Number of lines on the terminal (overrides termcap entry).</p>
<dt>LOCKPRG</p>
<dd> Screen lock program.</p>
<dt>NETHACKOPTIONS</p>
<dd> Turns on nethack option.</p>
<dt>PATH</p>
<dd> Used for locating programs to run.</p>
<dt>SCREENCAP</p>
<dd> For customizing a terminal&#8217;s TERMCAP value.</p>
<dt>SCREENDIR</p>
<dd> Alternate socket directory.</p>
<dt>SCREENRC</p>
<dd> Alternate user screenrc file.</p>
<dt>SHELL</p>
<dd> Default shell program for opening windows (default /bin/sh). See also shell .screenrc command.</p>
<dt>STY</p>
<dd> Alternate socket name.</p>
<dt>SYSSCREENRC</p>
<dd> Alternate system screenrc file.</p>
<dt>TERM</p>
<dd> Terminal name.</p>
<dt>TERMCAP</p>
<dd> Terminal description.</p>
<dt>WINDOW</p>
<dd> Window number of a window (at creation time). </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>&#8230;/screen-4.?.??/etc/screenrc</p>
<dd>
<dt>&#8230;/screen-4.?.??/etc/etcscreenrc</p>
<dd> Examples in the <i>screen</i> distribution package for private and global initialization files.</p>
<dt>$SYSSCREENRC</p>
<dd>
<dt>/etc/screenrc</p>
<dd> <i>screen</i> initialization commands</p>
<dt>$SCREENRC</p>
<dd>
<dt>$HOME/.screenrc</p>
<dd> Read in after /etc/screenrc</p>
<dt>$SCREENDIR/S-&lt;login&gt;</p>
<dd>
<dt>/run/screen/S-&lt;login&gt;</p>
<dd> Socket directories (default)</p>
<dt>/usr/tmp/screens/S-&lt;login&gt;</p>
<dd> Alternate socket directories.</p>
<dt>&lt;socket directory&gt;/.termcap</p>
<dd> Written by the &quot;termcap&quot; output function</p>
<dt>/usr/tmp/screens/screen-exchange</p>
<dd> or</p>
<dt>/tmp/screen-exchange</p>
<dd> <i>screen</i> `interprocess communication buffer&#8217;</p>
<dt>hardcopy.[0-9]</p>
<dd> Screen images created by the hardcopy function</p>
<dt>screenlog.[0-9]</p>
<dd> Output log files created by the log function</p>
<dt>/usr/lib/terminfo/?/*</p>
<dd> or</p>
<dt>/etc/termcap</p>
<dd> Terminal capability databases</p>
<dt>/run/utmp</p>
<dd> Login records</p>
<dt>$LOCKPRG</p>
<dd> Program that locks a terminal. </p>
</dl>
<h2>AUTHORS</h2>
<p> Originally created by Oliver Laumann. For a long time maintained and developed by Juergen Weigert, Michael Schroeder, Micah Cowan and Sadrul Habib Chowdhury. Since 2015 maintained and developed by Amadeusz Slawinski &lt;amade [at] asmblr.net&gt; and Alexander Naumov &lt;alexander_naumov [at] opensuse.org&gt;. </p>
<h2>COPYLEFT</h2>
<p>Copyright(c) 2018 &#8211; 2022 Alexander Naumov&lt;alexander_naumov[at] opensuse.org&gt; Amadeusz Slawinski&lt;amade[at] asmblr.net&gt; Copyright(c) 2015 &#8211; 2017 Juergen Weigert&lt;jnweiger[at] immd4.informatik.uni &#8211; erlangen.de&gt; Alexander Naumov&lt;alexander_naumov[at] opensuse.org&gt; Amadeusz Slawinski&lt;amade[at] asmblr.net&gt; Copyright(c) 2010 &#8211; 2015 Juergen Weigert&lt;jnweiger[at] immd4.informatik.uni &#8211; erlangen.de&gt; Sadrul Habib Chowdhury&lt;sadrul[at] users.sourceforge.net&gt; Copyright(c) 2008, 2009 Juergen Weigert&lt;jnweiger[at] immd4.informatik.uni &#8211; erlangen.de&gt; Michael Schroeder&lt;mlschroe[at] immd4.informatik.uni &#8211; erlangen.de&gt; Micah Cowan&lt;micah[at] cowan.name&gt; Sadrul Habib Chowdhury&lt;sadrul[at] users.sourceforge.net&gt; Copyright(C) 1993 &#8211; 2003 Juergen Weigert&lt;jnweiger[at] immd4.informatik.uni &#8211; erlangen.de&gt; Michael Schroeder&lt;mlschroe[at] immd4.informatik.uni &#8211; erlangen.de&gt; Copyright(C) 1987 Oliver Laumann</p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program (see the file COPYING); if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA </p>
<h2>CONTRIBUTORS</h2>
<pre><code>
Maarten ter Huurne&lt;maarten[at] treewalker.org&gt;,
    Jussi Kukkonen&lt;jussi.kukkonen[at] intel.com&gt;,
    Eric S.Raymond&lt;esr[at] thyrsus.com&gt;,
    Thomas Renninger&lt;treen[at] suse.com&gt;,
    Axel Beckert&lt;abe[at] deuxchevaux.org&gt;,
    Ken Beal&lt;kbeal[at] amber.ssd.csd.harris.com&gt;,
    Rudolf Koenig&lt;rfkoenig[at] immd4.informatik.uni - erlangen.de&gt;,
    Toerless Eckert&lt;eckert[at] immd4.informatik.uni - erlangen.de&gt;,
    Wayne Davison&lt;davison[at] borland.com&gt;,
    Patrick Wolfe&lt;pat[at] kai.com, kailand !pat&gt;,
    Bart Schaefer&lt;schaefer[at] cse.ogi.edu&gt;,
    Nathan Glasser&lt;nathan[at] brokaw.lcs.mit.edu&gt;,
    Larry W.Virden&lt;lvirden[at] cas.org&gt;,
    Howard Chu&lt;hyc[at] hanauma.jpl.nasa.gov&gt;,
    Tim MacKenzie&lt;tym[at] dibbler.cs.monash.edu.au&gt;,
    Markku Jarvinen&lt;mta @{cc, cs, ee}.tut.fi&gt;,
    Marc Boucher&lt;marc[at] CAM.ORG&gt;,
    Doug Siebert&lt;dsiebert[at] isca.uiowa.edu&gt;,
    Ken Stillson&lt;stillson[at] tsfsrv.mitre.org&gt;,
    Ian Frechett&lt;frechett[at] spot.Colorado.EDU&gt;,
    Brian Koehmstedt&lt;bpk[at] gnu.ai.mit.edu&gt;,
    Don Smith&lt;djs6015[at] ultb.isc.rit.edu&gt;,
    Frank van der Linden&lt;vdlinden[at] fwi.uva.nl&gt;,
    Martin Schweikert&lt;schweik[at] cpp.ob.open.de&gt;,
    David Vrona&lt;dave[at] sashimi.lcu.com&gt;,
    E.Tye McQueen&lt;tye % spillman.UUCP[at] uunet.uu.net&gt;,
    Matthew Green&lt;mrg[at] eterna.com.au&gt;,
    Christopher Williams&lt;cgw[at] pobox.com&gt;,
    Matt Mosley&lt;mattm[at] access.digex.net&gt;,
    Gregory Neil Shapiro&lt;gshapiro[at] wpi.WPI.EDU&gt;,
    Johannes Zellner&lt;johannes[at] zellner.org&gt;,
    Pablo Averbuj&lt;pablo[at] averbuj.com&gt;.
</code></pre>
<h2>AVAILABILITY</h2>
<p> The latest official release of <i>screen</i> available via anonymous ftp from <a href="ftp://ftp.gnu.org">ftp.gnu.org</a>/gnu/screen/ or any other <i>GNU </i> distribution site. The home page of <i>screen</i> is <a rel="nofollow" href="https://savannah.gnu.org/projects/screen/">https://savannah.gnu.org/projects/screen/</a> and the git repo is <a rel="nofollow" href="https://git.savannah.gnu.org/cgit/screen.git.">https://git.savannah.gnu.org/cgit/screen.git.</a> If you want to help, send a note to <code>screen-devel [at] gnu.org.</code> </p>
<h2>BUGS</h2>
<dl>
<dt>&bull;</p>
<dd> `dm&#8217; (delete mode) and `xs&#8217; are not handled correctly (they are ignored). `xn&#8217; is treated as a magic-margin indicator.</p>
<dt>&bull;</p>
<dd> <i>Screen</i> has no clue about double-high or double-wide characters. But this is the only area where <i>vttest</i> is allowed to fail.</p>
<dt>&bull;</p>
<dd> It is not possible to change the environment variable $TERMCAP when reattaching under a different terminal type.</p>
<dt>&bull;</p>
<dd> The support of terminfo based systems is very limited. Adding extra capabilities to $TERMCAP may not have any effects.</p>
<dt>&bull;</p>
<dd> <i>Screen</i> does not make use of hardware tabs.</p>
<dt>&bull;</p>
<dd> <i>Screen</i> must be installed as set-uid with owner root on most systems in order to be able to correctly change the owner of the tty device file for each window. Special permission may also be required to write the file /run/utmp.</p>
<dt>&bull;</p>
<dd> Entries in /run/utmp are not removed when <i>screen</i> is killed with SIGKILL. This will cause some programs (like &quot;w&quot; or &quot;rwho&quot;) to advertise that a user is logged on who really isn&#8217;t.</p>
<dt>&bull;</p>
<dd> <i>Screen</i> may give a strange warning when your tty has no utmp entry.</p>
<dt>&bull;</p>
<dd> When the modem line was hung up, <i>screen</i> may not automatically detach (or quit) unless the device driver is configured to send a HANGUP signal. To detach a <i>screen</i> session use the -D or -d command line option.</p>
<dt>&bull;</p>
<dd> If a password is set, the command line options -d and -D still detach a session without asking.</p>
<dt>&bull;</p>
<dd> Both breaktype and defbreaktype change the break generating method used by all terminal devices. The first should change a window specific setting, where the latter should change only the default for new windows.</p>
<dt>&bull;</p>
<dd> When attaching to a multiuser session, the user&#8217;s .screenrc file is not sourced. Each user&#8217;s personal settings have to be included in the .screenrc file from which the session is booted, or have to be changed manually.</p>
<dt>&bull;</p>
<dd> A weird imagination is most useful to gain full advantage of all the features.</dl>
<p> Send bug-reports, fixes, enhancements, t-shirts, money, beer &amp; pizza to <code>screen-devel [at] gnu.org</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-termcap/">termcap</a>(5),</code> <code><a href="/docs/linux/man/5-utmp/">utmp</a>(5),</code> <code><a href="/docs/linux/man/1-vi/">vi</a>(1),</code> <code><a href="/docs/linux/man/1-captoinfo/">captoinfo</a>(1),</code> <code><a href="/docs/linux/man/1-tic/">tic</a>(1),</code> <code><a href="/docs/linux/man/4-tty/">tty</a>(4),</code> <code><a href="/docs/linux/man/7-pty/">pty</a>(7)</code> </p>
<h2>Index</h2>
