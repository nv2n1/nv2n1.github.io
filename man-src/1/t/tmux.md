---
title: "tmux(1)"
name: "tmux"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tmux/"
description: "tmux – terminal multiplexer"
---

<h2>NAME</h2>
<p> <code>tmux</code> &#8211; terminal multiplexer</p>
<h2>SYNOPSIS</h2>
<p> <code>tmux</code> -words [-<code>28lCquvV</code> ] [-<code>c </code><i>shell-command</i> ] [-<code>f </code><i>file</i> ] [-<code>L </code><i>socket-name</i> ] [-<code>S </code><i>socket-path</i> ] [<i>command </i>[<i>flags</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>tmux</code> is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. <code>tmux</code> may be detached from a screen and continue running in the background, then later reattached. </p>
<p> When <code>tmux</code> is started it creates a new <i>session</i> with a single <i>window</i> and displays it on screen. A status line at the bottom of the screen shows information on the current session and is used to enter interactive commands. </p>
<p> A session is a single collection of <i>pseudo terminals</i> under the management of <code>.</code> Each session has one or more windows linked to it. A window occupies the entire screen and may be split into rectangular panes, each of which is a separate pseudo terminal (the <a href="/docs/linux/man/4-pty/">pty</a>(4) manual page documents the technical details of pseudo terminals). Any number of <code>tmux</code> instances may connect to the same session, and any number of windows may be present in the same session. Once all sessions are killed, <code>tmux</code> exits. </p>
<p> Each session is persistent and will survive accidental disconnection (such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1) connection timeout) or intentional detaching (with the `C-b&#8217; d key strokes). <code>tmux</code> may be reattached using: </p>
<blockquote><p><tt>$ tmux attach</tt></p></blockquote>
<p> In <code>,</code> a session is displayed on screen by a <i>client</i> and all sessions are managed by a single <i>server</i> The server and each client are separate processes which communicate through a socket in /tmp </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-2</code></p>
<dd> Force <code>tmux</code> to assume the terminal supports 256 colours.</p>
<dt><code>-8</code></p>
<dd> Like &#8211;<code>2</code> but indicates that the terminal supports 88 colours.</p>
<dt><code>-C</code></p>
<dd> Start in control mode. Given twice ( Fl CC ) Xc disables echo.</p>
<dt><code>-c </code><i>shell-command</i></p>
<dd>Execute <i>shell-command</i> using the default shell. If necessary, the <code>tmux</code> server will be started to retrieve the <code>default-shell</code> option. This option is for compatibility with <a href="/docs/linux/man/1-sh/">sh</a>(1) when <code>tmux</code> is used as a login shell.</p>
<dt><code>-f </code><i>file</i></p>
<dd>Specify an alternative configuration file. By default, <code>tmux</code> loads the system configuration file from /etc/tmux.conf if present, then looks for a user configuration file at ~/.tmux.conf </p>
<p> The configuration file is a set of <code>tmux</code> commands which are executed in sequence when the server is first started. <code>tmux</code> loads configuration files once when the server process has started. The <code>source-file</code> command may be used to load a file later. </p>
<p> <code>tmux</code> shows any error messages from commands in configuration files in the first session created, and continues to process the rest of the configuration file.</p>
<dt><code>-L </code><i>socket-name</i> <code>tmux</code></p>
<dd>stores the server socket in a directory under /tmp (or <code>TMPDIR</code> if set); the default socket is named <i>default</i> This option allows a different socket name to be specified, allowing several independent <code>tmux</code> servers to be run. Unlike &#8211;<code>S</code> a full path is not necessary: the sockets are all created in the same directory. </p>
<p> If the socket is accidentally removed, the <code>SIGUSR1</code> signal may be sent to the <code>tmux</code> server process to recreate it.</p>
<dt><code>-l</code></p>
<dd>Behave as a login shell. This flag currently has no effect and is for compatibility with other shells when using tmux as a login shell.</p>
<dt><code>-q</code></p>
<dd>Set the <code>quiet</code> server option to prevent the server sending various informational messages.</p>
<dt><code>-S </code><i>socket-path</i></p>
<dd>Specify a full alternative path to the server socket. If &#8211;<code>S</code> is specified, the default socket directory is not used and any &#8211;<code>L</code> flag is ignored.</p>
<dt><code>-u</code> <code>tmux</code></p>
<dd>attempts to guess if the terminal is likely to support UTF-8 by checking the first of the <code>LC_ALL</code> <code>LC_CTYPE</code> and <code>LANG</code> environment variables to be set for the string &quot;UTF-8&quot;. This is not always correct: the &#8211;<code>u</code> flag explicitly informs <code>tmux</code> that UTF-8 is supported. </p>
<p> If the server is started from a client passed &#8211;<code>u</code> or where UTF-8 is detected, the <code>utf8</code> and <code>status-utf8</code> options are enabled in the global window and session options respectively.</p>
<dt><code>-v</code></p>
<dd>Request verbose logging. This option may be specified multiple times for increasing verbosity. Log messages will be saved into tmux-client-PID.log and tmux-server-PID.log files in the current directory, where <i>PID</i> is the PID of the server or client process.</p>
<dt><code>-V</code></p>
<dd>Report the <code>tmux</code> version.</p>
<dt><i>command </i>[<i>flags</i> ]</p>
<dd>This specifies one of a set of commands used to control <code>,</code> as described in the following sections. If no commands are specified, the <code>new-session</code> command is assumed.</dl>
<h2>KEY BINDINGS</h2>
<p> <code>tmux</code> may be controlled from an attached client by using a key combination of a prefix key, `C-b&#8217; (Ctrl-b) by default, followed by a command key. </p>
<p> The default command key bindings are: </p>
<dl>
<dt><code>C-b</code></p>
<dd>Send the prefix key (C-b) through to the application.</p>
<dt><code>C-o</code></p>
<dd>Rotate the panes in the current window forwards.</p>
<dt><code>C-z</code></p>
<dd>Suspend the <code>tmux</code> client.</p>
<dt><code>!</code></p>
<dd>Break the current pane out of the window.</p>
<dt><code>&quot;</code></p>
<dd>Split the current pane into two, top and bottom.</p>
<dt><code>#</code></p>
<dd>List all paste buffers.</p>
<dt><code>$</code></p>
<dd>Rename the current session.</p>
<dt><code>%</code></p>
<dd>Split the current pane into two, left and right.</p>
<dt><code>&amp;</code></p>
<dd>Kill the current window.</p>
<dt><code>&#8216;</code></p>
<dd>Prompt for a window index to select.</p>
<dt><code>,</code></p>
<dd>Rename the current window.</p>
<dt><code>&#8211;</code></p>
<dd>Delete the most recently copied buffer of text.</p>
<dt><code>.</code></p>
<dd>Prompt for an index to move the current window.</p>
<dt><code>0 to 9</code></p>
<dd>Select windows 0 to 9.</p>
<dt><code>:</code></p>
<dd>Enter the <code>tmux</code> command prompt.</p>
<dt><code>;</code></p>
<dd>Move to the previously active pane.</p>
<dt><code>=</code></p>
<dd>Choose which buffer to paste interactively from a list.</p>
<dt><code>?</code></p>
<dd>List all key bindings.</p>
<dt><code>D</code></p>
<dd>Choose a client to detach.</p>
<dt><code>[</code></p>
<dd>Enter copy mode to copy text or view the history.</p>
<dt><code>]</code></p>
<dd>Paste the most recently copied buffer of text.</p>
<dt><code>c</code></p>
<dd>Create a new window.</p>
<dt><code>d</code></p>
<dd>Detach the current client.</p>
<dt><code>f</code></p>
<dd>Prompt to search for text in open windows.</p>
<dt><code>i</code></p>
<dd>Display some information about the current window.</p>
<dt><code>l</code></p>
<dd>Move to the previously selected window.</p>
<dt><code>n</code></p>
<dd>Change to the next window.</p>
<dt><code>o</code></p>
<dd>Select the next pane in the current window.</p>
<dt><code>p</code></p>
<dd>Change to the previous window.</p>
<dt><code>q</code></p>
<dd>Briefly display pane indexes.</p>
<dt><code>r</code></p>
<dd>Force redraw of the attached client.</p>
<dt><code>s</code></p>
<dd>Select a new session for the attached client interactively.</p>
<dt><code>L</code></p>
<dd>Switch the attached client back to the last session.</p>
<dt><code>t</code></p>
<dd>Show the time.</p>
<dt><code>w</code></p>
<dd>Choose the current window interactively.</p>
<dt><code>x</code></p>
<dd>Kill the current pane.</p>
<dt><code>{</code></p>
<dd>Swap the current pane with the previous pane.</p>
<dt><code>}</code></p>
<dd>Swap the current pane with the next pane.</p>
<dt><code>~</code></p>
<dd>Show previous messages from <code>,</code> if any.</p>
<dt><code>Page Up </code>Enter copy mode and scroll one page up.</p>
<dt><code>Up, Down</code></p>
<dt><code>Left, Right</code></p>
<dd>Change to the pane above, below, to the left, or to the right of the current pane.</p>
<dt><code>M-1 to M-5</code></p>
<dd>Arrange panes in one of the five preset layouts: even-horizontal, even-vertical, main-horizontal, main-vertical, or tiled.</p>
<dt><code>M-n</code></p>
<dd>Move to the next window with a bell or activity marker.</p>
<dt><code>M-o</code></p>
<dd>Rotate the panes in the current window backwards.</p>
<dt><code>M-p</code></p>
<dd>Move to the previous window with a bell or activity marker.</p>
<dt><code>C-Up, C-Down</code></p>
<dt><code>C-Left, C-Right</code></p>
<dd>Resize the current pane in steps of one cell.</p>
<dt><code>M-Up, M-Down</code></p>
<dt><code>M-Left, M-Right</code></p>
<dd>Resize the current pane in steps of five cells.</dl>
<p> Key bindings may be changed with the <code>bind-key</code> and <code>unbind-key</code> commands.</p>
<h2>COMMANDS</h2>
<p> This section contains a list of the commands supported by <code>.</code> Most commands accept the optional &#8211;<code>t</code> argument with one of <i>target-client</i> <i>target-session</i> <i>target-window</i> or <i>target-pane</i> These specify the client, session, window or pane which a command should affect. <i>target-client</i> is the name of the <a href="/docs/linux/man/4-pty/">pty</a>(4) file to which the client is connected, for example either of /dev/ttyp1 or ttyp1 for the client attached to /dev/ttyp1 If no client is specified, the current client is chosen, if possible, or an error is reported. Clients may be listed with the <code>list-clients</code> command. </p>
<p> <i>target-session</i> is the session id prefixed with a $, the name of a session (as listed by the <code>list-sessions</code> command), or the name of a client with the same syntax as <i>target-client</i> in which case the session attached to the client is used. When looking for the session name, <code>tmux</code> initially searches for an exact match; if none is found, the session names are checked for any for which <i>target-session</i> is a prefix or for which it matches as an <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern. If a single match is found, it is used as the target session; multiple matches produce an error. If a session is omitted, the current session is used if available; if no current session is available, the most recently used is chosen. </p>
<p> <i>target-window</i> specifies a window in the form <i>session </i><code>: </code><i>window</i> <i>session</i> follows the same rules as for <i>target-session</i> and <i>window</i> is looked for in order: as a window index, for example mysession:1; as a window ID, such as @1; as an exact window name, such as mysession:mywindow; then as an <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern or the start of a window name, such as mysession:mywin* or mysession:mywin. An empty window name specifies the next unused index if appropriate (for example the <code>new-window</code> and <code>link-window</code> commands) otherwise the current window in <i>session</i> is chosen. The special character `!&#8217; uses the last (previously current) window, `^&#8217; selects the highest numbered window, `$&#8217; selects the lowest numbered window, and `+&#8217; and `-&#8216; select the next window or the previous window by number. When the argument does not contain a colon, <code>tmux</code> first attempts to parse it as window; if that fails, an attempt is made to match a session. </p>
<p> <i>target-pane</i> takes a similar form to <i>target-window</i> but with the optional addition of a period followed by a pane index, for example: mysession:mywindow.1. If the pane index is omitted, the currently active pane in the specified window is used. If neither a colon nor period appears, <code>tmux</code> first attempts to use the argument as a pane index; if that fails, it is looked up as for <i>target-window</i> A `+&#8217; or `-&#8216; indicate the next or previous pane index, respectively. One of the strings <i>top</i> <i>bottom</i> <i>left</i> <i>right</i> <i>top-left</i> <i>top-right</i> <i>bottom-left</i> or <i>bottom-right</i> may be used instead of a pane index. </p>
<p> The special characters `+&#8217; and `-&#8216; may be followed by an offset, for example: </p>
<blockquote>
<pre>
select-window -t:+2
</pre>
</blockquote>
<p> When dealing with a session that doesn&#8217;t contain sequential window indexes, they will be correctly skipped. </p>
<p> <code>tmux</code> also gives each pane created in a server an identifier consisting of a `%&#8217; and a number, starting from zero. A pane&#8217;s identifier is unique for the life of the <code>tmux</code> server and is passed to the child process of the pane in the <code>TMUX_PANE</code> environment variable. It may be used alone to target a pane or the window containing it. </p>
<p> <i>shell-command</i> arguments are <a href="/docs/linux/man/1-sh/">sh</a>(1) commands. These must be passed as a single item, which typically means quoting them, for example: </p>
<blockquote>
<pre>
new-window 'vi /etc/passwd'
</pre>
</blockquote>
<p> <i>command</i> [<i>arguments</i> ] refers to a <code>tmux</code> command, passed with the command and arguments separately, for example: </p>
<blockquote>
<pre>
bind-key F1 set-window-option force-width 81
</pre>
</blockquote>
<p> Or if using <a href="/docs/linux/man/1-sh/">sh</a>(1): </p>
<blockquote>
<pre>
$ tmux bind-key F1 set-window-option force-width 81
</pre>
</blockquote>
<p> Multiple commands may be specified together as part of a <i>command sequence</i> Each command should be separated by spaces and a semicolon; commands are executed sequentially from left to right and lines ending with a backslash continue on to the next line, except when escaped by another backslash. A literal semicolon may be included by escaping it with a backslash (for example, when specifying a command sequence to <code>bind-key )</code> </p>
<p> Example <code>tmux</code> commands include: </p>
<blockquote>
<pre>
refresh-client -t/dev/ttyp2
rename-session -tfirst newname
set-window-option -t:0 monitor-activity on
new-window ; split-window -d
bind-key R source-file ~/.tmux.conf \; \
        display-message &quot;source-file done&quot;
</pre>
</blockquote>
<p> Or from <a href="/docs/linux/man/1-sh/">sh</a>(1): </p>
<blockquote>
<pre>
$ tmux kill-window -t :1
$ tmux new-window \; split-window -d
$ tmux new-session -d 'vi /etc/passwd' \; split-window -d \; attach
</pre>
</blockquote>
<h2>CLIENTS AND SESSIONS</h2>
<p> The <code>tmux</code> server manages clients, sessions, windows and panes. Clients are attached to sessions to interact with them, either when they are created with the <code>new-session</code> command, or later with the <code>attach-session</code> command. Each session has one or more windows <i>linked</i> into it. Windows may be linked to multiple sessions and are made up of one or more panes, each of which contains a pseudo terminal. Commands for creating, linking and otherwise manipulating windows are covered in the Sx WINDOWS AND PANES section. </p>
<p> The following commands are available to manage clients and sessions:</p>
<dl>
<dt><code> attach-session</code> [-<code>dr</code> ] [-<code>t </code><i>target-session</i> ]</p>
<dd>
<dd>If run from outside <code>,</code> create a new client in the current terminal and attach it to <i>target-session</i> If used from inside, switch the current client. If &#8211;<code>d</code> is specified, any other clients attached to the session are detached. &#8211;<code>r</code> signifies the client is read-only (only keys bound to the <code>detach-client</code> or <code>switch-client</code> commands have any effect) </p>
<p> If no server is started, <code>attach-session</code> will attempt to start it; this will fail unless sessions are created in the configuration file. </p>
<p> The <i>target-session</i> rules for <code>attach-session</code> are slightly adjusted: if <code>tmux</code> needs to select the most recently used session, it will prefer the most recently used <i>unattached</i> session.</p>
<dt><code> detach-client</code> [-<code>P</code> ] [-<code>a</code> ] [-<code>s </code><i>target-session</i> ] [-<code>t </code><i>target-client</i> ]</p>
<dd>
<dd>Detach the current client if bound to a key, the client specified with &#8211;<code>t</code> or all clients currently attached to the session specified by &#8211;<code>s</code> The &#8211;<code>a</code> option kills all but the client given with &#8211;<code>t</code> If &#8211;<code>P</code> is given, send SIGHUP to the parent process of the client, typically causing it to exit.</p>
<dt><code>has-session </code>[-<code>t </code><i>target-session</i> ]</p>
<dd> Report an error and exit with 1 if the specified session does not exist. If it does exist, exit with 0.</p>
<dt><code>kill-server</code></p>
<dd> Kill the <code>tmux</code> server and clients and destroy all sessions.</p>
<dt><code>kill-session</code></p>
<dd> [-<code>a</code> ] [-<code>t </code><i>target-session</i> ] Destroy the given session, closing any windows linked to it and no other sessions, and detaching all clients attached to it. If &#8211;<code>a</code> is given, all sessions but the specified one is killed.</p>
<dt><code> list-clients</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-session</i> ]</p>
<dd>
<dd>List all clients attached to the server. For the meaning of the &#8211;<code>F</code> flag, see the Sx FORMATS section. If <i>target-session</i> is specified, list only clients connected to that session.</p>
<dt><code>list-commands</code></p>
<dd> List the syntax of all commands supported by <code>.</code></p>
<dt><code>list-sessions </code>[-<code>F </code><i>format</i> ]</p>
<dd> List all sessions managed by the server. For the meaning of the &#8211;<code>F</code> flag, see the Sx FORMATS section.</p>
<dt><code>lock-client </code>[-<code>t </code><i>target-client</i> ]</p>
<dd> Lock <i>target-client</i> see the <code>lock-server</code> command.</p>
<dt><code>lock-session </code>[-<code>t </code><i>target-session</i> ]</p>
<dd> Lock all clients attached to <i>target-session</i></p>
<dt><code> new-session</code> [-<code>AdDP</code> ] [-<code>F </code><i>format</i> ] [-<code>n </code><i>window-name</i> ] [-<code>s </code><i>session-name</i> ] [-<code>t </code><i>target-session</i> ] [-<code>x </code><i>width</i> ] [-<code>y </code><i>height</i> ] [<i>shell-command</i> ]</p>
<dd>
<dd>Create a new session with name <i>session-name</i> </p>
<p> The new session is attached to the current terminal unless &#8211;<code>d</code> is given. <i>window-name</i> and <i>shell-command</i> are the name of and shell command to execute in the initial window. If &#8211;<code>d</code> is used, &#8211;<code>x</code> and &#8211;<code>y</code> specify the size of the initial window (80 by 24 if not given). </p>
<p> If run from a terminal, any <a href="/docs/linux/man/4-termios/">termios</a>(4) special characters are saved and used for new windows in the new session. </p>
<p> The &#8211;<code>A</code> flag makes <code>new-session</code> behave like <code>attach-session</code> if <i>session-name</i> already exists; in the case, &#8211;<code>D</code> behaves like &#8211;<code>d</code> to <code>attach-session</code> </p>
<p> If &#8211;<code>t</code> is given, the new session is <i>grouped</i> with <i>target-session</i> This means they share the same set of windows &#8211; all windows from <i>target-session</i> are linked to the new session and any subsequent new windows or windows being closed are applied to both sessions. The current and previous window and any session options remain independent and either session may be killed without affecting the other. Giving &#8211;<code>n</code> or <i>shell-command</i> are invalid if &#8211;<code>t</code> is used. </p>
<p> The &#8211;<code>P</code> option prints information about the new session after it has been created. By default, it uses the format `#{session_name}:&#8217; but a different format may be specified with &#8211;<code>F</code></p>
<dt><code> refresh-client</code> [-<code>S</code> ] [-<code>t </code><i>target-client</i> ]</p>
<dd>
<dd>Refresh the current client if bound to a key, or a single client if one is given with &#8211;<code>t</code> If &#8211;<code>S</code> is specified, only update the client&#8217;s status bar.</p>
<dt><code> rename-session</code> [-<code>t </code><i>target-session</i> ] <i>new-name</i></p>
<dd>
<dd>Rename the session to <i>new-name</i></p>
<dt><code> show-messages</code> [-<code>t </code><i>target-client</i> ]</p>
<dd>
<dd>Any messages displayed on the status line are saved in a per-client message log, up to a maximum of the limit set by the <i>message-limit</i> session option for the session attached to that client. This command displays the log for <i>target-client</i></p>
<dt><code>source-file </code><i>path</i></p>
<dd> Execute commands from <i>path</i></p>
<dt><code>start-server</code></p>
<dd> Start the <code>tmux</code> server, if not already running, without creating any sessions.</p>
<dt><code> suspend-client</code> [-<code>t </code><i>target-client</i> ]</p>
<dd>
<dd>Suspend a client by sending <code>SIGTSTP</code> (tty stop).</p>
<dt><code> switch-client</code> [-<code>lnpr</code> ] [-<code>c </code><i>target-client</i> ] [-<code>t </code><i>target-session</i> ]</p>
<dd>
<dd>Switch the current session for client <i>target-client</i> to <i>target-session</i> If &#8211;<code>l</code> &#8211;<code>n</code> or &#8211;<code>p</code> is used, the client is moved to the last, next or previous session respectively. &#8211;<code>r</code> toggles whether a client is read-only (see the <code>attach-session</code> command).</dl>
<h2>WINDOWS AND PANES</h2>
<p> A <code>tmux</code> window may be in one of several modes. The default permits direct access to the terminal attached to the window. The other is copy mode, which permits a section of a window or its history to be copied to a <i>paste buffer</i> for later insertion into another window. This mode is entered with the <code>copy-mode</code> command, bound to `[&#8216; by default. It is also entered when a command that produces output, such as <code>list-keys</code> is executed from a key binding. </p>
<p> The keys available depend on whether emacs or vi mode is selected (see the <code>mode-keys</code> option). The following keys are supported as appropriate for the mode:</p>
<dl>
<dt><code>Function Ta </code><code>vi Ta </code><code>emacs</code></p>
<dd>
<dt><code>Back to indentation Ta </code>^ Ta M-m</p>
<dd>
<dt><code>Bottom of history Ta </code>G Ta M-&lt;</p>
<dd>
<dt><code>Clear selection Ta </code>Escape Ta C-g</p>
<dd>
<dt><code>Copy selection Ta </code>Enter Ta M-w</p>
<dd>
<dt><code>Cursor down Ta </code>j Ta Down</p>
<dd>
<dt><code>Cursor left Ta </code>h Ta Left</p>
<dd>
<dt><code>Cursor right Ta </code>l Ta Right</p>
<dd>
<dt><code>Cursor to bottom line Ta </code>L Ta</p>
<dd>
<dt><code>Cursor to middle line Ta </code>M Ta M-r</p>
<dd>
<dt><code>Cursor to top line Ta </code>H Ta M-R</p>
<dd>
<dt><code>Cursor up Ta </code>k Ta Up</p>
<dd>
<dt><code>Delete entire line Ta </code>d Ta C-u</p>
<dd>
<dt><code>Delete/Copy to end of line Ta </code>D Ta C-k</p>
<dd>
<dt><code>End of line Ta </code>$ Ta C-e</p>
<dd>
<dt><code>Go </code>to line Ta : Ta g</p>
<dd>
<dt><code>Half page down Ta </code>C-d Ta M-Down</p>
<dd>
<dt><code>Half page up Ta </code>C-u Ta M-Up</p>
<dd>
<dt><code>Jump forward Ta </code>f Ta f</p>
<dd>
<dt><code>Jump to forward Ta </code>t Ta</p>
<dd>
<dt><code>Jump backward Ta </code>F Ta F</p>
<dd>
<dt><code>Jump to backward Ta </code>T Ta</p>
<dd>
<dt><code>Jump again Ta </code>; Ta ;</p>
<dd>
<dt><code>Jump again in reverse Ta </code>, Ta ,</p>
<dd>
<dt><code>Next page Ta </code>C-f Ta Page down</p>
<dd>
<dt><code>Next space Ta </code>W Ta</p>
<dd>
<dt><code>Next space, end of word Ta </code>E Ta</p>
<dd>
<dt><code>Next word Ta </code>w Ta</p>
<dd>
<dt><code>Next word end Ta </code>e Ta M-f</p>
<dd>
<dt><code>Paste buffer Ta </code>p Ta C-y</p>
<dd>
<dt><code>Previous page Ta </code>C-b Ta Page up</p>
<dd>
<dt><code>Previous word Ta </code>b Ta M-b</p>
<dd>
<dt><code>Previous space Ta </code>B Ta</p>
<dd>
<dt><code>Quit mode Ta </code>q Ta Escape</p>
<dd>
<dt><code>Rectangle toggle Ta </code>v Ta R</p>
<dd>
<dt><code>Scroll down Ta </code>C-Down or C-e Ta C-Down</p>
<dd>
<dt><code>Scroll up Ta </code>C-Up or C-y Ta C-Up</p>
<dd>
<dt><code>Search again Ta </code>n Ta n</p>
<dd>
<dt><code>Search again in reverse Ta </code>N Ta N</p>
<dd>
<dt><code>Search backward Ta </code>? Ta C-r</p>
<dd>
<dt><code>Search forward Ta </code>/ Ta C-s</p>
<dd>
<dt><code>Start of line Ta </code>0 Ta C-a</p>
<dd>
<dt><code>Start selection Ta </code>Space Ta C-Space</p>
<dd>
<dt><code>Top of history Ta </code>g Ta M-&gt;</p>
<dd>
<dt><code>Transpose characters Ta </code> Ta C-t</p>
<dd></dl>
<p> The next and previous word keys use space and the `-&#8216; , `_&#8217; and `@&#8217; characters as word delimiters by default, but this can be adjusted by setting the <i>word-separators</i> session option. Next word moves to the start of the next word, next word end to the end of the next word and previous word to the start of the previous word. The three next and previous space keys work similarly but use a space alone as the word separator. </p>
<p> The jump commands enable quick movement within a line. For instance, typing `f&#8217; followed by `/&#8217; will move the cursor to the next `/&#8217; character on the current line. A `;&#8217; will then jump to the next occurrence. </p>
<p> Commands in copy mode may be prefaced by an optional repeat count. With vi key bindings, a prefix is entered using the number keys; with emacs, the Alt (meta) key and a number begins prefix entry. For example, to move the cursor forward by ten words, use `M-1&#8242; 0 M-f in emacs mode, and `10w&#8217; in vi. </p>
<p> When copying the selection, the repeat count indicates the buffer index to replace, if used. </p>
<p> Mode key bindings are defined in a set of named tables: <i>vi-edit</i> and <i>emacs-edit</i> for keys used when line editing at the command prompt; <i>vi-choice</i> and <i>emacs-choice</i> for keys used when choosing from lists (such as produced by the <code>choose-window</code> command); and <i>vi-copy</i> and <i>emacs-copy</i> used in copy mode. The tables may be viewed with the <code>list-keys</code> command and keys modified or removed with <code>bind-key</code> and <code>unbind-key</code> One command accepts an argument, <code>copy-pipe</code> which copies the selection and pipes it to a command. For example the following will bind `C-q&#8217; to copy the selection into /tmp as well as the paste buffer: </p>
<blockquote>
<pre>
bind-key -temacs-copy C-q copy-pipe &quot;cat &gt;/tmp/out&quot;
</pre>
</blockquote>
<p> The paste buffer key pastes the first line from the top paste buffer on the stack. </p>
<p> The synopsis for the <code>copy-mode</code> command is:</p>
<dl>
<dt><code> copy-mode</code> [-<code>u</code> ] [-<code>t </code><i>target-pane</i> ]</p>
<dd>
<dd>Enter copy mode. The &#8211;<code>u</code> option scrolls one page up.</dl>
<p> Each window displayed by <code>tmux</code> may be split into one or more <i>panes</i> each pane takes up a certain area of the display and is a separate terminal. A window may be split into panes using the <code>split-window</code> command. Windows may be split horizontally (with the &#8211;<code>h</code> flag) or vertically. Panes may be resized with the <code>resize-pane</code> command (bound to `C-up&#8217; , `C-down&#8217; `C-left&#8217; and `C-right&#8217; by default), the current pane may be changed with the <code>select-pane</code> command and the <code>rotate-window</code> and <code>swap-pane</code> commands may be used to swap panes without changing their position. Panes are numbered beginning from zero in the order they are created. </p>
<p> A number of preset <i>layouts</i> are available. These may be selected with the <code>select-layout</code> command or cycled with <code>next-layout</code> (bound to `Space&#8217; by default); once a layout is chosen, panes within it may be moved and resized as normal. </p>
<p> The following layouts are supported:</p>
<dl>
<dt><code>even-horizontal</code></p>
<dd> Panes are spread out evenly from left to right across the window.</p>
<dt><code>even-vertical</code></p>
<dd> Panes are spread evenly from top to bottom.</p>
<dt><code>main-horizontal</code></p>
<dd> A large (main) pane is shown at the top of the window and the remaining panes are spread from left to right in the leftover space at the bottom. Use the <i>main-pane-height</i> window option to specify the height of the top pane.</p>
<dt><code>main-vertical</code></p>
<dd> Similar to <code>main-horizontal</code> but the large pane is placed on the left and the others spread from top to bottom along the right. See the <i>main-pane-width</i> window option.</p>
<dt><code>tiled</code></p>
<dd> Panes are spread out as evenly as possible over the window in both rows and columns.</dl>
<p> In addition, <code>select-layout</code> may be used to apply a previously used layout &#8211; the <code>list-windows</code> command displays the layout of each window in a form suitable for use with <code>select-layout</code> For example: </p>
<blockquote>
<pre><code>
$ tmux list - windows 0 : ksh[159x48] layout : bb62, 159x48, 0, 0 {79x48, 0, 0, 79x48, 80, 0} $ tmux select - layout bb62, 159x48, 0, 0
{
    79x48, 0, 0, 79x48, 80, 0
}
</code></pre>
</blockquote>
<p> <code>tmux</code> automatically adjusts the size of the layout for the current window size. Note that a layout cannot be applied to a window with more panes than that from which the layout was originally defined. </p>
<p> Commands related to windows and panes are as follows:</p>
<dl>
<dt><code> break-pane</code> [-<code>dP</code> ] [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-pane</i> ]</p>
<dd>
<dd>Break <i>target-pane</i> off from its containing window to make it the only pane in a new window. If &#8211;<code>d</code> is given, the new window does not become the current window. The &#8211;<code>P</code> option prints information about the new window after it has been created. By default, it uses the format `#{session_name}:#{window_index}&#8217; but a different format may be specified with &#8211;<code>F</code></p>
<dt><code> capture-pane</code> [-<code>aep(</code>[-<code>b </code><i>buffer-index</i> ] ) ] [-<code>E </code><i>end-line</i> ] [-<code>S </code><i>start-line</i> ] [-<code>t </code><i>target-pane</i> ]</p>
<dd>
<dd>Capture the contents of a pane. If &#8211;<code>p</code> is given, the output goes to stdout, otherwise to the buffer specified with &#8211;<code>b</code> or a new buffer if omitted. If &#8211;<code>a</code> is given, the alternate screen is used, and the history is not accessible. If no alternate screen exists, an error will be returned unless &#8211;<code>q</code> is given. If &#8211;<code>e</code> is given, the output includes escape sequences for text and background attributes. &#8211;<code>C</code> also escapes non-printable characters as octal 
