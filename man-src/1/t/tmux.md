---

title: "tmux(1)"
name: "tmux"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tmux/"
description: "tmux – terminal multiplexer"
---

<h2>NAME</h2>
<p> <code>tmux</code> - terminal multiplexer  </p>
<p> <code>tmux</code> -words [-<code>28lCquvV</code> ] [-<code>c </code><i>shell-command</i> ] [-<code>f </code><i>file</i> ] [-<code>L </code><i>socket-name</i> ] [-<code>S </code><i>socket-path</i> ] [<i>command </i>[<i>flags</i> ] ]  </p>
<p> <code>tmux</code> is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. <code>tmux</code> may be detached from a screen and continue running in the background, then later reattached. </p>
<p> When <code>tmux</code> is started it creates a new <i>session</i> with a single <i>window</i> and displays it on screen. A status line at the bottom of the screen shows information on the current session and is used to enter interactive commands. </p>
<p> A session is a single collection of <i>pseudo terminals</i> under the management of <code>.</code> Each session has one or more windows linked to it. A window occupies the entire screen and may be split into rectangular panes, each of which is a separate pseudo terminal (the pty(4) manual page documents the technical details of pseudo terminals). Any number of <code>tmux</code> instances may connect to the same session, and any number of windows may be present in the same session. Once all sessions are killed, <code>tmux</code> exits. </p>
<p> Each session is persistent and will survive accidental disconnection (such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1) connection timeout) or intentional detaching (with the `C-b&#8217; d key strokes). <code>tmux</code> may be reattached using: </p>
<blockquote><p> <code>$ tmux attach</code> </p>
</blockquote>
<p> In <code>,</code> a session is displayed on screen by a <i>client</i> and all sessions are managed by a single <i>server</i> The server and each client are separate processes which communicate through a socket in /tmp </p>
<p> The options are as follows: </p>
<dl>
<dt><code>-2</code></dt>
<dd> <p> Force <code>tmux</code> to assume the terminal supports 256 colours. </p>
 </dd>
<dt><code>-8</code></dt>
<dd> <p> Like -<code>2</code> but indicates that the terminal supports 88 colours. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Start in control mode. Given twice ( Fl CC ) Xc disables echo. </p>
 </dd>
<dt><code>-c </code><i>shell-command</i></dt>
<dd> <p> Execute <i>shell-command</i> using the default shell. If necessary, the <code>tmux</code> server will be started to retrieve the <code>default-shell</code> option. This option is for compatibility with <a href="/docs/linux/man/1-sh/">sh</a>(1) when <code>tmux</code> is used as a login shell. </p>
 </dd>
<dt><code>-f </code><i>file</i></dt>
<dd> <p> Specify an alternative configuration file. By default, <code>tmux</code> loads the system configuration file from /etc/tmux.conf if present, then looks for a user configuration file at ~/.tmux.conf </p>
<p> The configuration file is a set of <code>tmux</code> commands which are executed in sequence when the server is first started. <code>tmux</code> loads configuration files once when the server process has started. The <code>source-file</code> command may be used to load a file later. </p>
<p> <code>tmux</code> shows any error messages from commands in configuration files in the first session created, and continues to process the rest of the configuration file. </p>
 </dd>
<dt><code>-L </code><i>socket-name</i><code>tmux</code></dt>
<dd> <p> stores the server socket in a directory under /tmp (or <code>TMPDIR</code> if set); the default socket is named <i>default</i> This option allows a different socket name to be specified, allowing several independent <code>tmux</code> servers to be run. Unlike -<code>S</code> a full path is not necessary: the sockets are all created in the same directory. </p>
<p> If the socket is accidentally removed, the <code>SIGUSR1</code> signal may be sent to the <code>tmux</code> server process to recreate it. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Behave as a login shell. This flag currently has no effect and is for compatibility with other shells when using tmux as a login shell. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Set the <code>quiet</code> server option to prevent the server sending various informational messages. </p>
 </dd>
<dt><code>-S </code><i>socket-path</i></dt>
<dd> <p> Specify a full alternative path to the server socket. If -<code>S</code> is specified, the default socket directory is not used and any -<code>L</code> flag is ignored. </p>
 </dd>
<dt><code>-u</code><code>tmux</code></dt>
<dd> <p> attempts to guess if the terminal is likely to support UTF-8 by checking the first of the <code>LC_ALL</code> <code>LC_CTYPE</code> and <code>LANG</code> environment variables to be set for the string &quot;UTF-8&quot;. This is not always correct: the -<code>u</code> flag explicitly informs <code>tmux</code> that UTF-8 is supported. </p>
<p> If the server is started from a client passed -<code>u</code> or where UTF-8 is detected, the <code>utf8</code> and <code>status-utf8</code> options are enabled in the global window and session options respectively. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Request verbose logging. This option may be specified multiple times for increasing verbosity. Log messages will be saved into tmux-client-PID.log and tmux-server-PID.log files in the current directory, where <i>PID</i> is the PID of the server or client process. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Report the <code>tmux</code> version. </p>
 </dd>
<dt><i>command </i>[<i>flags</i> ] </dt>
<dd> <p> This specifies one of a set of commands used to control <code>,</code> as described in the following sections. If no commands are specified, the <code>new-session</code> command is assumed. </p>
 </dd></dl>
<h2>KEY BINDINGS</h2>
<p> <code>tmux</code> may be controlled from an attached client by using a key combination of a prefix key, `C-b&#8217; (Ctrl-b) by default, followed by a command key. </p>
<p> The default command key bindings are: </p>
<dl>
<dt><code>C-b</code></dt>
<dd> <p> Send the prefix key (C-b) through to the application. </p>
 </dd>
<dt><code>C-o</code></dt>
<dd> <p> Rotate the panes in the current window forwards. </p>
 </dd>
<dt><code>C-z</code></dt>
<dd> <p> Suspend the <code>tmux</code> client. </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Break the current pane out of the window. </p>
 </dd>
<dt><code>&quot;</code></dt>
<dd> <p> Split the current pane into two, top and bottom. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> List all paste buffers. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Rename the current session. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Split the current pane into two, left and right. </p>
 </dd>
<dt><code>&amp;</code></dt>
<dd> <p> Kill the current window. </p>
 </dd>
<dt><code>&#8216;</code></dt>
<dd> <p> Prompt for a window index to select. </p>
 </dd>
<dt><code>,</code></dt>
<dd> <p> Rename the current window. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Delete the most recently copied buffer of text. </p>
 </dd>
<dt><code>.</code></dt>
<dd> <p> Prompt for an index to move the current window. </p>
 </dd>
<dt><code>0 to 9</code></dt>
<dd> <p> Select windows 0 to 9. </p>
 </dd>
<dt><code>:</code></dt>
<dd> <p> Enter the <code>tmux</code> command prompt. </p>
 </dd>
<dt><code>;</code></dt>
<dd> <p> Move to the previously active pane. </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> Choose which buffer to paste interactively from a list. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> List all key bindings. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Choose a client to detach. </p>
 </dd>
<dt><code>[</code></dt>
<dd> <p> Enter copy mode to copy text or view the history. </p>
 </dd>
<dt><code>]</code></dt>
<dd> <p> Paste the most recently copied buffer of text. </p>
 </dd>
<dt><code>c</code></dt>
<dd> <p> Create a new window. </p>
 </dd>
<dt><code>d</code></dt>
<dd> <p> Detach the current client. </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Prompt to search for text in open windows. </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Display some information about the current window. </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Move to the previously selected window. </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Change to the next window. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Select the next pane in the current window. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Change to the previous window. </p>
 </dd>
<dt><code>q</code></dt>
<dd> <p> Briefly display pane indexes. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Force redraw of the attached client. </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> Select a new session for the attached client interactively. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Switch the attached client back to the last session. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Show the time. </p>
 </dd>
<dt><code>w</code></dt>
<dd> <p> Choose the current window interactively. </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Kill the current pane. </p>
 </dd>
<dt><code>{</code></dt>
<dd> <p> Swap the current pane with the previous pane. </p>
 </dd>
<dt><code>}</code></dt>
<dd> <p> Swap the current pane with the next pane. </p>
 </dd>
<dt><code>~</code></dt>
<dd> <p> Show previous messages from <code>,</code> if any. </p>
 </dd>
<dt><code>Page Up </code>Enter copy mode and scroll one page up. </dt>
<dt><code>Up, Down</code></dt>
<dt><code>Left, Right</code></dt>
<dd> <p> Change to the pane above, below, to the left, or to the right of the current pane. </p>
 </dd>
<dt><code>M-1 to M-5</code></dt>
<dd> <p> Arrange panes in one of the five preset layouts: even-horizontal, even-vertical, main-horizontal, main-vertical, or tiled. </p>
 </dd>
<dt><code>M-n</code></dt>
<dd> <p> Move to the next window with a bell or activity marker. </p>
 </dd>
<dt><code>M-o</code></dt>
<dd> <p> Rotate the panes in the current window backwards. </p>
 </dd>
<dt><code>M-p</code></dt>
<dd> <p> Move to the previous window with a bell or activity marker. </p>
 </dd>
<dt><code>C-Up, C-Down</code></dt>
<dt><code>C-Left, C-Right</code></dt>
<dd> <p> Resize the current pane in steps of one cell. </p>
 </dd>
<dt><code>M-Up, M-Down</code></dt>
<dt><code>M-Left, M-Right</code></dt>
<dd> <p> Resize the current pane in steps of five cells. </p>
 </dd></dl>
<p> Key bindings may be changed with the <code>bind-key</code> and <code>unbind-key</code> commands.  </p>
<h2>COMMANDS</h2>
<p> This section contains a list of the commands supported by <code>.</code> Most commands accept the optional -<code>t</code> argument with one of <i>target-client</i> <i>target-session</i> <i>target-window</i> or <i>target-pane</i> These specify the client, session, window or pane which a command should affect. <i>target-client</i> is the name of the pty(4) file to which the client is connected, for example either of /dev/ttyp1 or ttyp1 for the client attached to /dev/ttyp1 If no client is specified, the current client is chosen, if possible, or an error is reported. Clients may be listed with the <code>list-clients</code> command. </p>
<p> <i>target-session</i> is the session id prefixed with a $, the name of a session (as listed by the <code>list-sessions</code> command), or the name of a client with the same syntax as <i>target-client</i> in which case the session attached to the client is used. When looking for the session name, <code>tmux</code> initially searches for an exact match; if none is found, the session names are checked for any for which <i>target-session</i> is a prefix or for which it matches as an <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern. If a single match is found, it is used as the target session; multiple matches produce an error. If a session is omitted, the current session is used if available; if no current session is available, the most recently used is chosen. </p>
<p> <i>target-window</i> specifies a window in the form <i>session </i><code>: </code><i>window</i> <i>session</i> follows the same rules as for <i>target-session</i> and <i>window</i> is looked for in order: as a window index, for example mysession:1; as a window ID, such as @1; as an exact window name, such as mysession:mywindow; then as an <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern or the start of a window name, such as mysession:mywin* or mysession:mywin. An empty window name specifies the next unused index if appropriate (for example the <code>new-window</code> and <code>link-window</code> commands) otherwise the current window in <i>session</i> is chosen. The special character `!&#8216; uses the last (previously current) window, `^&#8216; selects the highest numbered window, `$&#8216; selects the lowest numbered window, and `+&#8216; and `-&#8216; select the next window or the previous window by number. When the argument does not contain a colon, <code>tmux</code> first attempts to parse it as window; if that fails, an attempt is made to match a session. </p>
<p> <i>target-pane</i> takes a similar form to <i>target-window</i> but with the optional addition of a period followed by a pane index, for example: mysession:mywindow.1. If the pane index is omitted, the currently active pane in the specified window is used. If neither a colon nor period appears, <code>tmux</code> first attempts to use the argument as a pane index; if that fails, it is looked up as for <i>target-window</i> A `+&#8216; or `-&#8216; indicate the next or previous pane index, respectively. One of the strings <i>top</i> <i>bottom</i> <i>left</i> <i>right</i> <i>top-left</i> <i>top-right</i> <i>bottom-left</i> or <i>bottom-right</i> may be used instead of a pane index. </p>
<p> The special characters `+&#8216; and `-&#8216; may be followed by an offset, for example: </p>
<blockquote><pre><code>select-window -t:+2
</code></pre>
</blockquote>
<p> When dealing with a session that doesn&#8217;t contain sequential window indexes, they will be correctly skipped. </p>
<p> <code>tmux</code> also gives each pane created in a server an identifier consisting of a `%&#8216; and a number, starting from zero. A pane&#8217;s identifier is unique for the life of the <code>tmux</code> server and is passed to the child process of the pane in the <code>TMUX_PANE</code> environment variable. It may be used alone to target a pane or the window containing it. </p>
<p> <i>shell-command</i> arguments are <a href="/docs/linux/man/1-sh/">sh</a>(1) commands. These must be passed as a single item, which typically means quoting them, for example: </p>
<blockquote><pre><code>new-window 'vi /etc/passwd'
</code></pre>
</blockquote>
<p> <i>command</i> [<i>arguments</i> ] refers to a <code>tmux</code> command, passed with the command and arguments separately, for example: </p>
<blockquote><pre><code>bind-key F1 set-window-option force-width 81
</code></pre>
</blockquote>
<p> Or if using <a href="/docs/linux/man/1-sh/">sh</a>(1): </p>
<blockquote><pre><code>$ tmux bind-key F1 set-window-option force-width 81
</code></pre>
</blockquote>
<p> Multiple commands may be specified together as part of a <i>command sequence</i> Each command should be separated by spaces and a semicolon; commands are executed sequentially from left to right and lines ending with a backslash continue on to the next line, except when escaped by another backslash. A literal semicolon may be included by escaping it with a backslash (for example, when specifying a command sequence to <code>bind-key )</code> </p>
<p> Example <code>tmux</code> commands include: </p>
<blockquote><pre><code>refresh-client -t/dev/ttyp2
rename-session -tfirst newname
set-window-option -t:0 monitor-activity on
new-window ; split-window -d
bind-key R source-file ~/.tmux.conf \; \
        display-message &quot;source-file done&quot;
</code></pre>
</blockquote>
<p> Or from <a href="/docs/linux/man/1-sh/">sh</a>(1): </p>
<blockquote><pre><code>$ tmux kill-window -t :1
$ tmux new-window \; split-window -d
$ tmux new-session -d 'vi /etc/passwd' \; split-window -d \; attach
</code></pre>
</blockquote>
<h2>CLIENTS AND SESSIONS</h2>
<p> The <code>tmux</code> server manages clients, sessions, windows and panes. Clients are attached to sessions to interact with them, either when they are created with the <code>new-session</code> command, or later with the <code>attach-session</code> command. Each session has one or more windows <i>linked</i> into it. Windows may be linked to multiple sessions and are made up of one or more panes, each of which contains a pseudo terminal. Commands for creating, linking and otherwise manipulating windows are covered in the Sx WINDOWS AND PANES section. </p>
<p> The following commands are available to manage clients and sessions: </p>
<dl>
<dt><code> attach-session</code> [-<code>dr</code> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> If run from outside <code>,</code> create a new client in the current terminal and attach it to <i>target-session</i> If used from inside, switch the current client. If -<code>d</code> is specified, any other clients attached to the session are detached. -<code>r</code> signifies the client is read-only (only keys bound to the <code>detach-client</code> or <code>switch-client</code> commands have any effect) </p>
<p> If no server is started, <code>attach-session</code> will attempt to start it; this will fail unless sessions are created in the configuration file. </p>
<p> The <i>target-session</i> rules for <code>attach-session</code> are slightly adjusted: if <code>tmux</code> needs to select the most recently used session, it will prefer the most recently used <i>unattached</i> session. </p>
 </dd>
<dt><code> detach-client</code> [-<code>P</code> ] [-<code>a</code> ] [-<code>s </code><i>target-session</i> ] [-<code>t </code><i>target-client</i> ] </dt>
<dd>  </dd>
<dd> <p> Detach the current client if bound to a key, the client specified with -<code>t</code> or all clients currently attached to the session specified by -<code>s</code> The -<code>a</code> option kills all but the client given with -<code>t</code> If -<code>P</code> is given, send SIGHUP to the parent process of the client, typically causing it to exit. </p>
 </dd>
<dt><code>has-session </code>[-<code>t </code><i>target-session</i> ] </dt>
<dd> <p> Report an error and exit with 1 if the specified session does not exist. If it does exist, exit with 0. </p>
 </dd>
<dt><code>kill-server</code></dt>
<dd> <p> Kill the <code>tmux</code> server and clients and destroy all sessions. </p>
 </dd>
<dt><code>kill-session</code></dt>
<dd> <p> [-<code>a</code> ] [-<code>t </code><i>target-session</i> ] Destroy the given session, closing any windows linked to it and no other sessions, and detaching all clients attached to it. If -<code>a</code> is given, all sessions but the specified one is killed. </p>
 </dd>
<dt><code> list-clients</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> List all clients attached to the server. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. If <i>target-session</i> is specified, list only clients connected to that session. </p>
 </dd>
<dt><code>list-commands</code></dt>
<dd> <p> List the syntax of all commands supported by <code>.</code> </p>
 </dd>
<dt><code>list-sessions </code>[-<code>F </code><i>format</i> ] </dt>
<dd> <p> List all sessions managed by the server. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. </p>
 </dd>
<dt><code>lock-client </code>[-<code>t </code><i>target-client</i> ] </dt>
<dd> <p> Lock <i>target-client</i> see the <code>lock-server</code> command. </p>
 </dd>
<dt><code>lock-session </code>[-<code>t </code><i>target-session</i> ] </dt>
<dd> <p> Lock all clients attached to <i>target-session</i> </p>
 </dd>
<dt><code> new-session</code> [-<code>AdDP</code> ] [-<code>F </code><i>format</i> ] [-<code>n </code><i>window-name</i> ] [-<code>s </code><i>session-name</i> ] [-<code>t </code><i>target-session</i> ] [-<code>x </code><i>width</i> ] [-<code>y </code><i>height</i> ] [<i>shell-command</i> ] </dt>
<dd>  </dd>
<dd> <p> Create a new session with name <i>session-name</i> </p>
<p> The new session is attached to the current terminal unless -<code>d</code> is given. <i>window-name</i> and <i>shell-command</i> are the name of and shell command to execute in the initial window. If -<code>d</code> is used, -<code>x</code> and -<code>y</code> specify the size of the initial window (80 by 24 if not given). </p>
<p> If run from a terminal, any termios(4) special characters are saved and used for new windows in the new session. </p>
<p> The -<code>A</code> flag makes <code>new-session</code> behave like <code>attach-session</code> if <i>session-name</i> already exists; in the case, -<code>D</code> behaves like -<code>d</code> to <code>attach-session</code> </p>
<p> If -<code>t</code> is given, the new session is <i>grouped</i> with <i>target-session</i> This means they share the same set of windows - all windows from <i>target-session</i> are linked to the new session and any subsequent new windows or windows being closed are applied to both sessions. The current and previous window and any session options remain independent and either session may be killed without affecting the other. Giving -<code>n</code> or <i>shell-command</i> are invalid if -<code>t</code> is used. </p>
<p> The -<code>P</code> option prints information about the new session after it has been created. By default, it uses the format `#{session_name}:&#8216; but a different format may be specified with -<code>F</code> </p>
 </dd>
<dt><code> refresh-client</code> [-<code>S</code> ] [-<code>t </code><i>target-client</i> ] </dt>
<dd>  </dd>
<dd> <p> Refresh the current client if bound to a key, or a single client if one is given with -<code>t</code> If -<code>S</code> is specified, only update the client&#8217;s status bar. </p>
 </dd>
<dt><code> rename-session</code> [-<code>t </code><i>target-session</i> ] <i>new-name</i></dt>
<dd>  </dd>
<dd> <p> Rename the session to <i>new-name</i> </p>
 </dd>
<dt><code> show-messages</code> [-<code>t </code><i>target-client</i> ] </dt>
<dd>  </dd>
<dd> <p> Any messages displayed on the status line are saved in a per-client message log, up to a maximum of the limit set by the <i>message-limit</i> session option for the session attached to that client. This command displays the log for <i>target-client</i> </p>
 </dd>
<dt><code>source-file </code><i>path</i></dt>
<dd> <p> Execute commands from <i>path</i> </p>
 </dd>
<dt><code>start-server</code></dt>
<dd> <p> Start the <code>tmux</code> server, if not already running, without creating any sessions. </p>
 </dd>
<dt><code> suspend-client</code> [-<code>t </code><i>target-client</i> ] </dt>
<dd>  </dd>
<dd> <p> Suspend a client by sending <code>SIGTSTP</code> (tty stop). </p>
 </dd>
<dt><code> switch-client</code> [-<code>lnpr</code> ] [-<code>c </code><i>target-client</i> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> Switch the current session for client <i>target-client</i> to <i>target-session</i> If -<code>l</code> -<code>n</code> or -<code>p</code> is used, the client is moved to the last, next or previous session respectively. -<code>r</code> toggles whether a client is read-only (see the <code>attach-session</code> command). </p>
 </dd></dl>
<h2>WINDOWS AND PANES</h2>
<p> A <code>tmux</code> window may be in one of several modes. The default permits direct access to the terminal attached to the window. The other is copy mode, which permits a section of a window or its history to be copied to a <i>paste buffer</i> for later insertion into another window. This mode is entered with the <code>copy-mode</code> command, bound to `[&#8216; by default. It is also entered when a command that produces output, such as <code>list-keys</code> is executed from a key binding. </p>
<p> The keys available depend on whether emacs or vi mode is selected (see the <code>mode-keys</code> option). The following keys are supported as appropriate for the mode: </p>
<dl>
<dt><code>Function Ta </code><code>vi Ta </code><code>emacs</code></dt>
<dd>  </dd>
<dt><code>Back to indentation Ta </code>^ Ta M-m </dt>
<dd>  </dd>
<dt><code>Bottom of history Ta </code>G Ta M-&lt; </dt>
<dd>  </dd>
<dt><code>Clear selection Ta </code>Escape Ta C-g </dt>
<dd>  </dd>
<dt><code>Copy selection Ta </code>Enter Ta M-w </dt>
<dd>  </dd>
<dt><code>Cursor down Ta </code>j Ta Down </dt>
<dd>  </dd>
<dt><code>Cursor left Ta </code>h Ta Left </dt>
<dd>  </dd>
<dt><code>Cursor right Ta </code>l Ta Right </dt>
<dd>  </dd>
<dt><code>Cursor to bottom line Ta </code>L Ta </dt>
<dd>  </dd>
<dt><code>Cursor to middle line Ta </code>M Ta M-r </dt>
<dd>  </dd>
<dt><code>Cursor to top line Ta </code>H Ta M-R </dt>
<dd>  </dd>
<dt><code>Cursor up Ta </code>k Ta Up </dt>
<dd>  </dd>
<dt><code>Delete entire line Ta </code>d Ta C-u </dt>
<dd>  </dd>
<dt><code>Delete/Copy to end of line Ta </code>D Ta C-k </dt>
<dd>  </dd>
<dt><code>End of line Ta </code>$ Ta C-e </dt>
<dd>  </dd>
<dt><code>Go </code>to line Ta : Ta g </dt>
<dd>  </dd>
<dt><code>Half page down Ta </code>C-d Ta M-Down </dt>
<dd>  </dd>
<dt><code>Half page up Ta </code>C-u Ta M-Up </dt>
<dd>  </dd>
<dt><code>Jump forward Ta </code>f Ta f </dt>
<dd>  </dd>
<dt><code>Jump to forward Ta </code>t Ta </dt>
<dd>  </dd>
<dt><code>Jump backward Ta </code>F Ta F </dt>
<dd>  </dd>
<dt><code>Jump to backward Ta </code>T Ta </dt>
<dd>  </dd>
<dt><code>Jump again Ta </code>; Ta ; </dt>
<dd>  </dd>
<dt><code>Jump again in reverse Ta </code>, Ta , </dt>
<dd>  </dd>
<dt><code>Next page Ta </code>C-f Ta Page down </dt>
<dd>  </dd>
<dt><code>Next space Ta </code>W Ta </dt>
<dd>  </dd>
<dt><code>Next space, end of word Ta </code>E Ta </dt>
<dd>  </dd>
<dt><code>Next word Ta </code>w Ta </dt>
<dd>  </dd>
<dt><code>Next word end Ta </code>e Ta M-f </dt>
<dd>  </dd>
<dt><code>Paste buffer Ta </code>p Ta C-y </dt>
<dd>  </dd>
<dt><code>Previous page Ta </code>C-b Ta Page up </dt>
<dd>  </dd>
<dt><code>Previous word Ta </code>b Ta M-b </dt>
<dd>  </dd>
<dt><code>Previous space Ta </code>B Ta </dt>
<dd>  </dd>
<dt><code>Quit mode Ta </code>q Ta Escape </dt>
<dd>  </dd>
<dt><code>Rectangle toggle Ta </code>v Ta R </dt>
<dd>  </dd>
<dt><code>Scroll down Ta </code>C-Down or C-e Ta C-Down </dt>
<dd>  </dd>
<dt><code>Scroll up Ta </code>C-Up or C-y Ta C-Up </dt>
<dd>  </dd>
<dt><code>Search again Ta </code>n Ta n </dt>
<dd>  </dd>
<dt><code>Search again in reverse Ta </code>N Ta N </dt>
<dd>  </dd>
<dt><code>Search backward Ta </code>? Ta C-r </dt>
<dd>  </dd>
<dt><code>Search forward Ta </code>/ Ta C-s </dt>
<dd>  </dd>
<dt><code>Start of line Ta </code>0 Ta C-a </dt>
<dd>  </dd>
<dt><code>Start selection Ta </code>Space Ta C-Space </dt>
<dd>  </dd>
<dt><code>Top of history Ta </code>g Ta M-&gt; </dt>
<dd>  </dd>
<dt><code>Transpose characters Ta </code> Ta C-t </dt>
<dd>  </dd></dl>
<p> The next and previous word keys use space and the `-&#8216; , `_&#8216; and `@&#8216; characters as word delimiters by default, but this can be adjusted by setting the <i>word-separators</i> session option. Next word moves to the start of the next word, next word end to the end of the next word and previous word to the start of the previous word. The three next and previous space keys work similarly but use a space alone as the word separator. </p>
<p> The jump commands enable quick movement within a line. For instance, typing `f&#8217; followed by `/&#8216; will move the cursor to the next `/&#8216; character on the current line. A `;&#8216; will then jump to the next occurrence. </p>
<p> Commands in copy mode may be prefaced by an optional repeat count. With vi key bindings, a prefix is entered using the number keys; with emacs, the Alt (meta) key and a number begins prefix entry. For example, to move the cursor forward by ten words, use `M-1&#8217; 0 M-f in emacs mode, and `10w&#8217; in vi. </p>
<p> When copying the selection, the repeat count indicates the buffer index to replace, if used. </p>
<p> Mode key bindings are defined in a set of named tables: <i>vi-edit</i> and <i>emacs-edit</i> for keys used when line editing at the command prompt; <i>vi-choice</i> and <i>emacs-choice</i> for keys used when choosing from lists (such as produced by the <code>choose-window</code> command); and <i>vi-copy</i> and <i>emacs-copy</i> used in copy mode. The tables may be viewed with the <code>list-keys</code> command and keys modified or removed with <code>bind-key</code> and <code>unbind-key</code> One command accepts an argument, <code>copy-pipe</code> which copies the selection and pipes it to a command. For example the following will bind `C-q&#8217; to copy the selection into /tmp as well as the paste buffer: </p>
<blockquote><pre><code>bind-key -temacs-copy C-q copy-pipe &quot;cat &gt;/tmp/out&quot;
</code></pre>
</blockquote>
<p> The paste buffer key pastes the first line from the top paste buffer on the stack. </p>
<p> The synopsis for the <code>copy-mode</code> command is: </p>
<dl>
<dt><code> copy-mode</code> [-<code>u</code> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Enter copy mode. The -<code>u</code> option scrolls one page up. </p>
 </dd></dl>
<p> Each window displayed by <code>tmux</code> may be split into one or more <i>panes</i> each pane takes up a certain area of the display and is a separate terminal. A window may be split into panes using the <code>split-window</code> command. Windows may be split horizontally (with the -<code>h</code> flag) or vertically. Panes may be resized with the <code>resize-pane</code> command (bound to `C-up&#8217; , `C-down&#8217; `C-left&#8217; and `C-right&#8217; by default), the current pane may be changed with the <code>select-pane</code> command and the <code>rotate-window</code> and <code>swap-pane</code> commands may be used to swap panes without changing their position. Panes are numbered beginning from zero in the order they are created. </p>
<p> A number of preset <i>layouts</i> are available. These may be selected with the <code>select-layout</code> command or cycled with <code>next-layout</code> (bound to `Space&#8217; by default); once a layout is chosen, panes within it may be moved and resized as normal. </p>
<p> The following layouts are supported: </p>
<dl>
<dt><code>even-horizontal</code></dt>
<dd> <p> Panes are spread out evenly from left to right across the window. </p>
 </dd>
<dt><code>even-vertical</code></dt>
<dd> <p> Panes are spread evenly from top to bottom. </p>
 </dd>
<dt><code>main-horizontal</code></dt>
<dd> <p> A large (main) pane is shown at the top of the window and the remaining panes are spread from left to right in the leftover space at the bottom. Use the <i>main-pane-height</i> window option to specify the height of the top pane. </p>
 </dd>
<dt><code>main-vertical</code></dt>
<dd> <p> Similar to <code>main-horizontal</code> but the large pane is placed on the left and the others spread from top to bottom along the right. See the <i>main-pane-width</i> window option. </p>
 </dd>
<dt><code>tiled</code></dt>
<dd> <p> Panes are spread out as evenly as possible over the window in both rows and columns. </p>
 </dd></dl>
<p> In addition, <code>select-layout</code> may be used to apply a previously used layout - the <code>list-windows</code> command displays the layout of each window in a form suitable for use with <code>select-layout</code> For example: </p>
<blockquote><pre><code>$ tmux list-windows
0: ksh [159x48]
    layout: bb62,159x48,0,0{79x48,0,0,79x48,80,0}
$ tmux select-layout bb62,159x48,0,0{79x48,0,0,79x48,80,0}
</code></pre>
</blockquote>
<p> <code>tmux</code> automatically adjusts the size of the layout for the current window size. Note that a layout cannot be applied to a window with more panes than that from which the layout was originally defined. </p>
<p> Commands related to windows and panes are as follows: </p>
<dl>
<dt><code> break-pane</code> [-<code>dP</code> ] [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Break <i>target-pane</i> off from its containing window to make it the only pane in a new window. If -<code>d</code> is given, the new window does not become the current window. The -<code>P</code> option prints information about the new window after it has been created. By default, it uses the format `#{session_name}:#{window_index}&#8216; but a different format may be specified with -<code>F</code> </p>
 </dd>
<dt><code> capture-pane</code> [-<code>aep(</code>[-<code>b </code><i>buffer-index</i> ] ) ] [-<code>E </code><i>end-line</i> ] [-<code>S </code><i>start-line</i> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Capture the contents of a pane. If -<code>p</code> is given, the output goes to stdout, otherwise to the buffer specified with -<code>b</code> or a new buffer if omitted. If -<code>a</code> is given, the alternate screen is used, and the history is not accessible. If no alternate screen exists, an error will be returned unless -<code>q</code> is given. If -<code>e</code> is given, the output includes escape sequences for text and background attributes. -<code>C</code> also escapes non-printable characters as octal \xxx. -<code>J</code> joins wrapped lines and preserves trailing spaces at each line&#8217;s end. -<code>P</code> captures only any output that the pane has received that is the beginning of an as-yet incomplete escape sequence. </p>
<p> -<code>S</code> and -<code>E</code> specify the starting and ending line numbers, zero is the first line of the visible pane and negative numbers are lines in the history. The default is to capture only the visible contents of the pane. </p>
 </dd>
<dt><code>choose-client</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into client choice mode, allowing a client to be selected interactively from a list. After a client is chosen, `%%&#8216; is replaced by the client pty(4) path in <i>template</i> and the result executed as a command. If <i>template</i> is not given, &quot;detach-client -t &#8216;%%&#8216;&quot; is used. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code>choose-list</code> [-<code>l </code><i>items</i> ] [-<code>t </code><i>target-window</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into list choice mode, allowing <i>items</i> to be selected. <i>items</i> can be a comma-separated list to display more than one item. If an item has spaces, that entry must be quoted. After an item is chosen, `%%&#8216; is replaced by the chosen item in the <i>template</i> and the result is executed as a command. If <i>template</i> is not given, &quot;run-shell &#8216;%%&#8216;&quot; is used. <i>items</i> also accepts format specifiers. For the meaning of this see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code>choose-session</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into session choice mode, where a session may be selected interactively from a list. When one is chosen, `%%&#8216; is replaced by the session name in <i>template</i> and the result executed as a command. If <i>template</i> is not given, &quot;switch-client -t &#8216;%%&#8216;&quot; is used. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code>choose-tree</code> [-<code>suw</code> ] [-<code>b </code><i>session-template</i> ] [-<code>c </code><i>window-template</i> ] [-<code>S </code><i>format</i> ] [-<code>W </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into tree choice mode, where either sessions or windows may be selected interactively from a list. By default, windows belonging to a session are indented to show their relationship to a session. </p>
<p> Note that the <code>choose-window</code> and <code>choose-session</code> commands are wrappers around <code>choose-tree</code> </p>
<p> If -<code>s</code> is given, will show sessions. If -<code>w</code> is given, will show windows. </p>
<p> By default, the tree is collapsed and sessions must be expanded to windows with the right arrow key. The -<code>u</code> option will start with all sessions expanded instead. </p>
<p> If -<code>b</code> is given, will override the default session command. Note that `%%&#8216; can be used and will be replaced with the session name. The default option if not specified is &quot;switch-client -t &#8216;%%&#8216;&quot;. If -<code>c</code> is given, will override the default window command. Like -<code>b</code> `%%&#8216; can be used and will be replaced with the session name and window index. When a window is chosen from the list, the session command is run before the window command. </p>
<p> If -<code>S</code> is given will display the specified format instead of the default session format. If -<code>W</code> is given will display the specified format instead of the default window format. For the meaning of the -<code>s</code> and -<code>w</code> options, see the Sx FORMATS section. </p>
<p> This command works only if at least one client is attached. </p>
 </dd>
<dt><code>choose-window</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into window choice mode, where a window may be chosen interactively from a list. After a window is selected, `%%&#8216; is replaced by the session name and window index in <i>template</i> and the result executed as a command. If <i>template</i> is not given, &quot;select-window -t &#8216;%%&#8216;&quot; is used. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code>display-panes </code>[-<code>t </code><i>target-client</i> ] </dt>
<dd> <p> Display a visible indicator of each pane shown by <i>target-client</i> See the <code>display-panes-time</code> <code>display-panes-colour</code> and <code>display-panes-active-colour</code> session options. While the indicator is on screen, a pane may be selected with the `0&#8217; to `9&#8217; keys. </p>
 </dd>
<dt><code> find-window</code> [-<code>CNT</code> ] [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] <i>match-string</i></dt>
<dd>  </dd>
<dd> <p> Search for the <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern <i>match-string</i> in window names, titles, and visible content (but not history). The flags control matching behavior: -<code>C</code> matches only visible window contents, -<code>N</code> matches only the window name and -<code>T</code> matches only the window title. The default is -<code>CNT</code> If only one window is matched, it&#8217;ll be automatically selected, otherwise a choice list is shown. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code> join-pane</code> [-<code>bdhv</code> ] [-<code>l</code><i>size</i> -<code>p </code><i>percentage </i>] [-<code>s </code><i>src-pane</i> ] [-<code>t </code><i>dst-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Like <code>split-window</code> but instead of splitting <i>dst-pane</i> and creating a new pane, split it and move <i>src-pane</i> into the space. This can be used to reverse <code>break-pane</code> The -<code>b</code> option causes <i>src-pane</i> to be joined to left of or above <i>dst-pane</i> </p>
 </dd>
<dt><code> kill-pane</code> [-<code>a</code> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Destroy the given pane. If no panes remain in the containing window, it is also destroyed. The -<code>a</code> option kills all but the pane given with -<code>t</code> </p>
 </dd>
<dt><code> kill-window</code> [-<code>a</code> ] [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Kill the current window or the window at <i>target-window</i> removing it from any sessions to which it is linked. The -<code>a</code> option kills all but the window given with -<code>t</code> </p>
 </dd>
<dt><code>last-pane </code>[-<code>t </code><i>target-window</i> ] </dt>
<dd> <p> Select the last (previously selected) pane. </p>
 </dd>
<dt><code>last-window </code>[-<code>t </code><i>target-session</i> ] </dt>
<dd> <p> Select the last (previously selected) window. If no <i>target-session</i> is specified, select the last window of the current session. </p>
 </dd>
<dt><code> link-window</code> [-<code>dk</code> ] [-<code>s </code><i>src-window</i> ] [-<code>t </code><i>dst-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Link the window at <i>src-window</i> to the specified <i>dst-window</i> If <i>dst-window</i> is specified and no such window exists, the <i>src-window</i> is linked there. If -<code>k</code> is given and <i>dst-window</i> exists, it is killed, otherwise an error is generated. If -<code>d</code> is given, the newly linked window is not selected. </p>
 </dd>
<dt><code> list-panes</code> [-<code>as</code> ] [-<code>F </code><i>format</i> ] [-<code>t </code><i>target</i> ] </dt>
<dd>  </dd>
<dd> <p> If -<code>a</code> is given, <i>target</i> is ignored and all panes on the server are listed. If -<code>s</code> is given, <i>target</i> is a session (or the current session). If neither is given, <i>target</i> is a window (or the current window). For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. </p>
 </dd>
<dt><code> list-windows</code> [-<code>a</code> ] [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> If -<code>a</code> is given, list all windows on the server. Otherwise, list windows in the current session or in <i>target-session</i> For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. </p>
 </dd>
<dt><code> move-pane</code> [-<code>bdhv</code> ] [-<code>l</code><i>size</i> -<code>p </code><i>percentage </i>] [-<code>s </code><i>src-pane</i> ] [-<code>t </code><i>dst-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Like <code>join-pane</code> but <i>src-pane</i> and <i>dst-pane</i> may belong to the same window. </p>
 </dd>
<dt><code> move-window</code> [-<code>rdk</code> ] [-<code>s </code><i>src-window</i> ] [-<code>t </code><i>dst-window</i> ] </dt>
<dd>  </dd>
<dd> <p> This is similar to <code>link-window</code> except the window at <i>src-window</i> is moved to <i>dst-window</i> With -<code>r</code> all windows in the session are renumbered in sequential order, respecting the <code>base-index</code> option. </p>
 </dd>
<dt><code> new-window</code> [-<code>adkP</code> ] [-<code>c </code><i>start-directory</i> ] [-<code>F </code><i>format</i> ] [-<code>n </code><i>window-name</i> ] [-<code>t </code><i>target-window</i> ] [<i>shell-command</i> ] </dt>
<dd>  </dd>
<dd> <p> Create a new window. With -<code>a</code> the new window is inserted at the next index up from the specified <i>target-window</i> moving windows up if necessary, otherwise <i>target-window</i> is the new window location. </p>
<p> If -<code>d</code> is given, the session does not make the new window the current window. <i>target-window</i> represents the window to be created; if the target already exists an error is shown, unless the -<code>k</code> flag is used, in which case it is destroyed. <i>shell-command</i> is the command to execute. If <i>shell-command</i> is not specified, the value of the <code>default-command</code> option is used. -<code>c</code> specifies the working directory in which the new window is created. It may have an absolute path or one of the following values (or a subdirectory): </p>
 </dd>
<dl>
<dt><code>Empty string Ta </code>Current pane&#8217;s directory </dt>
<dd>  </dd>
<dt><code>~ Ta </code>User&#8217;s home directory </dt>
<dd>  </dd>
<dt><code>- Ta </code>Where session was started </dt>
<dd>  </dd>
<dt><code>. Ta </code>Where server was started </dt>
<dd>  </dd></dl>
<p> When the shell command completes, the window closes. See the <code>remain-on-exit</code> option to change this behaviour. </p>
<p> The <code>TERM</code> environment variable must be set to ``screen&#8217;&#8216; for all programs running <i>inside</i> <code>.</code> New windows will automatically have ``TERM=screen&#8217;&#8216; added to their environment, but care must be taken not to reset this in shell start-up files. </p>
<p> The -<code>P</code> option prints information about the new window after it has been created. By default, it uses the format `#{session_name}:#{window_index}&#8216; but a different format may be specified with -<code>F</code> </p>
<dt><code>next-layout </code>[-<code>t </code><i>target-window</i> ] </dt>
<dd> <p> Move a window to the next layout and rearrange the panes to fit. </p>
 </dd>
<dt><code> next-window</code> [-<code>a</code> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> Move to the next window in the session. If -<code>a</code> is used, move to the next window with an alert. </p>
 </dd>
<dt><code> pipe-pane</code> [-<code>o</code> ] [-<code>t </code><i>target-pane</i> ] [<i>shell-command</i> ] </dt>
<dd>  </dd>
<dd> <p> Pipe any output sent by the program in <i>target-pane</i> to a shell command. A pane may only be piped to one command at a time, any existing pipe is closed before <i>shell-command</i> is executed. The <i>shell-command</i> string may contain the special character sequences supported by the <code>status-left</code> option. If no <i>shell-command</i> is given, the current pipe (if any) is closed. </p>
<p> The -<code>o</code> option only opens a new pipe if no previous pipe exists, allowing a pipe to be toggled with a single key, for example: </p>
<blockquote><pre><code>bind-key C-p pipe-pane -o 'cat &gt;&gt;~/output.#I-#P'
</code></pre>
</blockquote>
 </dd>
<dt><code> previous-layout</code> [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Move to the previous layout in the session. </p>
 </dd>
<dt><code> previous-window</code> [-<code>a</code> ] [-<code>t </code><i>target-session</i> ] </dt>
<dd>  </dd>
<dd> <p> Move to the previous window in the session. With -<code>a</code> move to the previous window with an alert. </p>
 </dd>
<dt><code> rename-window</code> [-<code>t </code><i>target-window</i> ] <i>new-name</i></dt>
<dd>  </dd>
<dd> <p> Rename the current window, or the window at <i>target-window</i> if specified, to <i>new-name</i> </p>
 </dd>
<dt><code> resize-pane</code> [-<code>DLRUZ</code> ] [-<code>t </code><i>target-pane</i> ] [-<code>x </code><i>width</i> ] [-<code>y </code><i>height</i> ] [<i>adjustment</i> ] </dt>
<dd>  </dd>
<dd> <p> Resize a pane, up, down, left or right by <i>adjustment</i> with -<code>U</code> -<code>D</code> -<code>L</code> or -<code>R</code> or to an absolute size with -<code>x</code> or -<code>y</code> The <i>adjustment</i> is given in lines or cells (the default is 1). </p>
<p> With -<code>Z</code> the active pane is toggled between zoomed (occupying the whole of the window) and unzoomed (its normal position in the layout). </p>
 </dd>
<dt><code> respawn-pane</code> [-<code>k</code> ] [-<code>t </code><i>target-pane</i> ] [<i>shell-command</i> ] </dt>
<dd>  </dd>
<dd> <p> Reactivate a pane in which the command has exited (see the <code>remain-on-exit</code> window option). If <i>shell-command</i> is not given, the command used when the pane was created is executed. The pane must be already inactive, unless -<code>k</code> is given, in which case any existing command is killed. </p>
 </dd>
<dt><code> respawn-window</code> [-<code>k</code> ] [-<code>t </code><i>target-window</i> ] [<i>shell-command</i> ] </dt>
<dd>  </dd>
<dd> <p> Reactivate a window in which the command has exited (see the <code>remain-on-exit</code> window option). If <i>shell-command</i> is not given, the command used when the window was created is executed. The window must be already inactive, unless -<code>k</code> is given, in which case any existing command is killed. </p>
 </dd>
<dt><code> rotate-window</code> [-<code>DU</code> ] [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Rotate the positions of the panes within a window, either upward (numerically lower) with -<code>U</code> or downward (numerically higher). </p>
 </dd>
<dt><code> select-layout</code> [-<code>np</code> ] [-<code>t </code><i>target-window</i> ] [<i>layout-name</i> ] </dt>
<dd>  </dd>
<dd> <p> Choose a specific layout for a window. If <i>layout-name</i> is not given, the last preset layout used (if any) is reapplied. -<code>n</code> and -<code>p</code> are equivalent to the <code>next-layout</code> and <code>previous-layout</code> commands. </p>
 </dd>
<dt><code> select-pane</code> [-<code>lDLRU</code> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Make pane <i>target-pane</i> the active pane in window <i>target-window</i> If one of -<code>D</code> -<code>L</code> -<code>R</code> or -<code>U</code> is used, respectively the pane below, to the left, to the right, or above the target pane is used. -<code>l</code> is the same as using the <code>last-pane</code> command. </p>
 </dd>
<dt><code> select-window</code> [-<code>lnpT</code> ] [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Select the window at <i>target-window</i> -<code>l</code> -<code>n</code> and -<code>p</code> are equivalent to the <code>last-window</code> <code>next-window</code> and <code>previous-window</code> commands. If -<code>T</code> is given and the selected window is already the current window, the command behaves like <code>last-window</code> </p>
 </dd>
<dt><code> split-window</code> [-<code>dhvP</code> ] [-<code>c </code><i>start-directory</i> ] [-<code>l</code><i>size</i> -<code>p </code><i>percentage </i>] [-<code>t </code><i>target-pane</i> ] [<i>shell-command</i> ] [-<code>F </code><i>format</i> ] </dt>
<dd>  </dd>
<dd> <p> Create a new pane by splitting <i>target-pane</i> -<code>h</code> does a horizontal split and -<code>v</code> a vertical split; if neither is specified, -<code>v</code> is assumed. The -<code>l</code> and -<code>p</code> options specify the size of the new pane in lines (for vertical split) or in cells (for horizontal split), or as a percentage, respectively. All other options have the same meaning as for the <code>new-window</code> command. </p>
 </dd>
<dt><code> swap-pane</code> [-<code>dDU</code> ] [-<code>s </code><i>src-pane</i> ] [-<code>t </code><i>dst-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Swap two panes. If -<code>U</code> is used and no source pane is specified with -<code>s</code> <i>dst-pane</i> is swapped with the previous pane (before it numerically); -<code>D</code> swaps with the next pane (after it numerically). -<code>d</code> instructs <code>tmux</code> not to change the active pane. </p>
 </dd>
<dt><code> swap-window</code> [-<code>d</code> ] [-<code>s </code><i>src-window</i> ] [-<code>t </code><i>dst-window</i> ] </dt>
<dd>  </dd>
<dd> <p> This is similar to <code>link-window</code> except the source and destination windows are swapped. It is an error if no window exists at <i>src-window</i> </p>
 </dd>
<dt><code> unlink-window</code> [-<code>k</code> ] [-<code>t </code><i>target-window</i> ] </dt>
<dd>  </dd>
<dd> <p> Unlink <i>target-window</i> Unless -<code>k</code> is given, a window may be unlinked only if it is linked to multiple sessions - windows may not be linked to no sessions; if -<code>k</code> is specified and the window is linked to only one session, it is unlinked and destroyed. </p>
 </dd></dl>
<h2>KEY BINDINGS</h2>
<p> <code>tmux</code> allows a command to be bound to most keys, with or without a prefix key. When specifying keys, most represent themselves (for example `A&#8217; to `Z&#8217; ) . Ctrl keys may be prefixed with `C-&#8216; or `^&#8216; , and Alt (meta) with `M-&#8216; In addition, the following special key names are accepted: <i>Up </i>, <i>Down</i> <i>Left</i> <i>Right</i> <i>BSpace</i> <i>BTab</i> <i>DC</i> (Delete), <i>End</i> <i>Enter</i> <i>Escape</i> <i>F1</i> to <i>F20</i> <i>Home</i> <i>IC</i> (Insert), <i>NPage/PageDown/PgDn </i>, <i>PPage/PageUp/PgUp </i>, <i>Space</i> and <i>Tab</i> Note that to bind the `&#8216; or `&#8216;&#8216; keys, quotation marks are necessary, for example: </p>
<blockquote><pre><code>bind-key '&quot;' split-window
bind-key &quot;'&quot; new-window
</code></pre>
</blockquote>
<p> Commands related to key bindings are as follows: </p>
<dl>
<dt><code> bind-key</code> [-<code>cnr</code> ] [-<code>t </code><i>key-table</i> ] <i>key command </i>[<i>arguments</i> ] </dt>
<dd>  </dd>
<dd> <p> Bind key <i>key</i> to <i>command</i> By default (without -<code>t</code> the primary key bindings are modified (those normally activated with the prefix key); in this case, if -<code>n</code> is specified, it is not necessary to use the prefix key, <i>command</i> is bound to <i>key</i> alone. The -<code>r</code> flag indicates this key may repeat, see the <code>repeat-time</code> option. </p>
<p> If -<code>t</code> is present, <i>key</i> is bound in <i>key-table</i> the binding for command mode with -<code>c</code> or for normal mode without. To view the default bindings and possible commands, see the <code>list-keys</code> command. </p>
 </dd>
<dt><code>list-keys </code>[-<code>t </code><i>key-table</i> ] </dt>
<dd> <p> List all key bindings. Without -<code>t</code> the primary key bindings - those executed when preceded by the prefix key - are printed. </p>
<p> With -<code>t</code> the key bindings in <i>key-table</i> are listed; this may be one of: <i>vi-edit</i> <i>emacs-edit</i> <i>vi-choice</i> <i>emacs-choice</i> <i>vi-copy</i> or <i>emacs-copy</i> </p>
 </dd>
<dt><code> send-keys</code> [-<code>lR</code> ] [-<code>t </code><i>target-pane</i> ] <i>key ...</i></dt>
<dd>  </dd>
<dd> <p> Send a key or keys to a window. Each argument <i>key</i> is the name of the key (such as `C-a&#8217; or `npage&#8217; ) to send; if the string is not recognised as a key, it is sent as a series of characters. The -<code>l</code> flag disables key name lookup and sends the keys literally. All arguments are sent sequentially from first to last. The -<code>R</code> flag causes the terminal state to be reset. </p>
 </dd>
<dt><code> send-prefix</code> [-<code>2</code> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Send the prefix key, or with -<code>2</code> the secondary prefix key, to a window as if it was pressed. </p>
 </dd>
<dt><code> unbind-key</code> [-<code>acn</code> ] [-<code>t </code><i>key-table</i> ] <i>key</i></dt>
<dd>  </dd>
<dd> <p> Unbind the command bound to <i>key</i> Without -<code>t</code> the primary key bindings are modified; in this case, if -<code>n</code> is specified, the command bound to <i>key</i> without a prefix (if any) is removed. If -<code>a</code> is present, all key bindings are removed. </p>
<p> If -<code>t</code> is present, <i>key</i> in <i>key-table</i> is unbound: the binding for command mode with -<code>c</code> or for normal mode without. </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> The appearance and behaviour of <code>tmux</code> may be modified by changing the value of various options. There are three types of option: <i>server options</i> <i>session options</i> and <i>window options</i> </p>
<p> The <code>tmux</code> server has a set of global options which do not apply to any particular window or session. These are altered with the <code>set-option</code> -<code>s</code> command, or displayed with the <code>show-options</code> -<code>s</code> command. </p>
<p> In addition, each individual session may have a set of session options, and there is a separate set of global session options. Sessions which do not have a particular option configured inherit the value from the global session options. Session options are set or unset with the <code>set-option</code> command and may be listed with the <code>show-options</code> command. The available server and session options are listed under the <code>set-option</code> command. </p>
<p> Similarly, a set of window options is attached to each window, and there is a set of global window options from which any unset options are inherited. Window options are altered with the <code>set-window-option</code> command and can be listed with the <code>show-window-options</code> command. All window options are documented with the <code>set-window-option</code> command. </p>
<p> <code>tmux</code> also supports user options which are prefixed with a `@&#8216; User options may have any name, so long as they are prefixed with `@&#8216; , and be set to any string. For example </p>
<blockquote><pre><code>$ tmux setw -q @foo &quot;abc123&quot;
$ tmux showw -v @foo
abc123
</code></pre>
</blockquote>
<p> Commands which set options are as follows: </p>
<dl>
<dt><code> set-option</code> [-<code>agoqsuw</code> ] [-<code>t </code><i>target-session | target-window</i> ] <i>option value</i></dt>
<dd>  </dd>
<dd> <p> Set a window option with -<code>w</code> (equivalent to the <code>set-window-option</code> command), a server option with -<code>s</code> otherwise a session option. </p>
<p> If -<code>g</code> is specified, the global session or window option is set. With -<code>a</code> and if the option expects a string, <i>value</i> is appended to the existing setting. The -<code>u</code> flag unsets an option, so a session inherits the option from the global options. It is not possible to unset a global option. </p>
<p> The -<code>o</code> flag prevents setting an option that is already set. </p>
<p> The -<code>q</code> flag suppresses the informational message (as if the <code>quiet</code> server option was set). </p>
<p> Available window options are listed under <code>set-window-option</code> </p>
<p> <i>value</i> depends on the option and may be a number, a string, or a flag (on, off, or omitted to toggle). </p>
<p> Available server options are: </p>
 </dd>
<dl>
<dt><code>buffer-limit </code><i>number</i></dt>
<dd> <p> Set the number of buffers; as new buffers are added to the top of the stack, old ones are removed from the bottom if necessary to maintain this maximum length. </p>
 </dd>
<dt><code>escape-time </code><i>time</i></dt>
<dd> <p> Set the time in milliseconds for which <code>tmux</code> waits after an escape is input to determine if it is part of a function or meta key sequences. The default is 500 milliseconds. </p>
 </dd>
<dt><code> exit-unattached</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If enabled, the server will exit when there are no attached clients. </p>
 </dd>
<dt><code> quiet</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Enable or disable the display of various informational messages (see also the -<code>q</code> command line flag). </p>
 </dd>
<dt><code> set-clipboard</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Attempt to set the terminal clipboard content using the \e]52;...\007 <a href="/docs/linux/man/1-xterm/">xterm</a>(1) escape sequences. This option is on by default if there is an <i></i><code>entry in the</code> <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) description for the client terminal. Note that this feature needs to be enabled in <a href="/docs/linux/man/1-xterm/">xterm</a>(1) by setting the resource: </p>
<blockquote><pre><code>disallowedWindowOps: 20,21,SetXprop
</code></pre>
</blockquote>
<p> Or changing this property from the <a href="/docs/linux/man/1-xterm/">xterm</a>(1) interactive menu when required. </p>
 </dd></dl>
<p> Available session options are: </p>
<dl>
<dt><code>assume-paste-time </code><i>milliseconds</i></dt>
<dd> <p> If keys are entered faster than one in <i>milliseconds</i> they are assumed to have been pasted rather than typed and <code>tmux</code> key bindings are not processed. The default is one millisecond and zero disables. </p>
 </dd>
<dt><code>base-index </code><i>index</i></dt>
<dd> <p> Set the base index from which an unused index should be searched when a new window is created. The default is zero. </p>
 </dd>
<dt><code> bell-action</code> [<code>any | none | current</code> ] </dt>
<dd>  </dd>
<dd> <p> Set action on window bell. <code>any</code> means a bell in any window linked to a session causes a bell in the current window of that session, <code>none</code> means all bells are ignored and <code>current</code> means only bells in windows other than the current window are ignored. </p>
 </dd>
<dt><code> bell-on-alert</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, ring the terminal bell when an alert occurs. </p>
 </dd>
<dt><code>default-command </code><i>shell-command</i></dt>
<dd> <p> Set the command used for new windows (if not specified when the window is created) to <i>shell-command</i> which may be any <a href="/docs/linux/man/1-sh/">sh</a>(1) command. The default is an empty string, which instructs <code>tmux</code> to create a login shell using the value of the <code>default-shell</code> option. </p>
 </dd>
<dt><code>default-path </code><i>path</i></dt>
<dd> <p> Set the default working directory for new panes. If empty (the default), the working directory is determined from the process running in the active pane, from the command line environment or from the working directory where the session was created. Otherwise the same options are available as for the -<code>c</code> flag to <code>new-window</code> </p>
 </dd>
<dt><code>default-shell </code><i>path</i></dt>
<dd> <p> Specify the default shell. This is used as the login shell for new windows when the <code>default-command</code> option is set to empty, and must be the full path of the executable. When started <code>tmux</code> tries to set a default value from the first suitable of the <code>SHELL</code> environment variable, the shell returned by <a href="/docs/linux/man/3-getpwuid/">getpwuid</a>(3), or /bin/sh This option should be configured when <code>tmux</code> is used as a login shell. </p>
 </dd>
<dt><code>default-terminal </code><i>terminal</i></dt>
<dd> <p> Set the default terminal for new windows created in this session - the default value of the <code>TERM</code> environment variable. For <code>tmux</code> to work correctly, this <i>must</i> be set to `screen&#8217; or a derivative of it. </p>
 </dd>
<dt><code> destroy-unattached</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If enabled and the session is no longer attached to any clients, it is destroyed. </p>
 </dd>
<dt><code> detach-on-destroy</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on (the default), the client is detached when the session it is attached to is destroyed. If off, the client is switched to the most recently active of the remaining sessions. </p>
 </dd>
<dt><code>display-panes-active-colour </code><i>colour</i></dt>
<dd> <p> Set the colour used by the <code>display-panes</code> command to show the indicator for the active pane. </p>
 </dd>
<dt><code>display-panes-colour </code><i>colour</i></dt>
<dd> <p> Set the colour used by the <code>display-panes</code> command to show the indicators for inactive panes. </p>
 </dd>
<dt><code>display-panes-time </code><i>time</i></dt>
<dd> <p> Set the time in milliseconds for which the indicators shown by the <code>display-panes</code> command appear. </p>
 </dd>
<dt><code>display-time </code><i>time</i></dt>
<dd> <p> Set the amount of time for which status line messages and other on-screen indicators are displayed. <i>time</i> is in milliseconds. </p>
 </dd>
<dt><code>history-limit </code><i>lines</i></dt>
<dd> <p> Set the maximum number of lines held in window history. This setting applies only to new windows - existing window histories are not resized and retain the limit at the point they were created. </p>
 </dd>
<dt><code>lock-after-time </code><i>number</i></dt>
<dd> <p> Lock the session (like the <code>lock-session</code> command) after <i>number</i> seconds of inactivity, or the entire server (all sessions) if the <code>lock-server</code> option is set. The default is not to lock (set to 0). </p>
 </dd>
<dt><code>lock-command </code><i>shell-command</i></dt>
<dd> <p> Command to run when locking each client. The default is to run lock(1) with -<code>np</code> </p>
 </dd>
<dt><code> lock-server</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If this option is <code>on</code> (the default), instead of each session locking individually as each has been idle for <code>lock-after-time</code> the entire server will lock after <i>all</i> sessions would have locked. This has no effect as a session option; it must be set as a global option. </p>
 </dd>
<dt><code>message-attr </code><i>attributes</i></dt>
<dd> <p> Set status line message attributes, where <i>attributes</i> is either <code>none</code> or a comma-delimited list of one or more of: <code>bright</code> (or <code>bold )</code> <code>dim</code> <code>underscore</code> <code>blink</code> <code>reverse</code> <code>hidden</code> or <code>italics</code> </p>
 </dd>
<dt><code>message-bg </code><i>colour</i></dt>
<dd> <p> Set status line message background colour, where <i>colour</i> is one of: <code>black</code> <code>red</code> <code>green</code> <code>yellow</code> <code>blue</code> <code>magenta</code> <code>cyan</code> <code>white</code> aixterm bright variants (if supported: <code>brightred</code> <code>brightgreen</code> and so on), <code>colour0</code> to <code>colour255</code> from the 256-colour set, <code>default</code> or a hexadecimal RGB string such as `#ffffff&#8217; , which chooses the closest match from the default 256-colour set. </p>
 </dd>
<dt><code>message-command-attr </code><i>attributes</i></dt>
<dd> <p> Set status line message attributes when in command mode. </p>
 </dd>
<dt><code>message-command-bg </code><i>colour</i></dt>
<dd> <p> Set status line message background colour when in command mode. </p>
 </dd>
<dt><code>message-command-fg </code><i>colour</i></dt>
<dd> <p> Set status line message foreground colour when in command mode. </p>
 </dd>
<dt><code>message-fg </code><i>colour</i></dt>
<dd> <p> Set status line message foreground colour. </p>
 </dd>
<dt><code>message-limit </code><i>number</i></dt>
<dd> <p> Set the number of error or information messages to save in the message log for each client. The default is 20. </p>
 </dd>
<dt><code> mouse-resize-pane</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, <code>tmux</code> captures the mouse and allows panes to be resized by dragging on their borders. </p>
 </dd>
<dt><code> mouse-select-pane</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, <code>tmux</code> captures the mouse and when a window is split into multiple panes the mouse may be used to select the current pane. The mouse click is also passed through to the application as normal. </p>
 </dd>
<dt><code> mouse-select-window</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, clicking the mouse on a window name in the status line will select that window. </p>
 </dd>
<dt><code> mouse-utf8</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If enabled, request mouse input as UTF-8 on UTF-8 terminals. </p>
 </dd>
<dt><code>pane-active-border-bg </code><i>colour</i></dt>
<dd>  </dd>
<dt><code>pane-active-border-fg </code><i>colour</i></dt>
<dd> <p> Set the pane border colour for the currently active pane. </p>
 </dd>
<dt><code>pane-border-bg </code><i>colour</i></dt>
<dd>  </dd>
<dt><code>pane-border-fg </code><i>colour</i></dt>
<dd> <p> Set the pane border colour for panes aside from the active pane. </p>
 </dd>
<dt><code>prefix </code><i>key</i></dt>
<dd> <p> Set the key accepted as a prefix key. </p>
 </dd>
<dt><code>prefix2 </code><i>key</i></dt>
<dd> <p> Set a secondary key accepted as a prefix key. </p>
 </dd>
<dt><code> renumber-windows</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, when a window is closed in a session, automatically renumber the other windows in numerical order. This respects the <code>base-index</code> option if it has been set. If off, do not renumber the windows. </p>
 </dd>
<dt><code>repeat-time </code><i>time</i></dt>
<dd> <p> Allow multiple commands to be entered without pressing the prefix-key again in the specified <i>time</i> milliseconds (the default is 500). Whether a key repeats may be set when it is bound using the -<code>r</code> flag to <code>bind-key</code> Repeat is enabled for the default keys bound to the <code>resize-pane</code> command. </p>
 </dd>
<dt><code> set-remain-on-exit</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Set the <code>remain-on-exit</code> window option for any windows first created in this session. When this option is true, windows in which the running program has exited do not close, instead remaining open but inactivate. Use the <code>respawn-window</code> command to reactivate such a window, or the <code>kill-window</code> command to destroy it. </p>
 </dd>
<dt><code> set-titles</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Attempt to set the client terminal title using the <i>tsl</i> and <i>fsl</i> <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) entries if they exist. <code>tmux</code> automatically sets these to the \e]2;...\007 sequence if the terminal appears to be an xterm. This option is off by default. Note that elinks will only attempt to set the window title if the STY environment variable is set. </p>
 </dd>
<dt><code>set-titles-string </code><i>string</i></dt>
<dd> <p> String used to set the window title if <code>set-titles</code> is on. Character sequences are replaced as for the <code>status-left</code> option. </p>
 </dd>
<dt><code> status</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Show or hide the status line. </p>
 </dd>
<dt><code>status-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes. </p>
 </dd>
<dt><code>status-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour. </p>
 </dd>
<dt><code>status-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour. </p>
 </dd>
<dt><code>status-interval </code><i>interval</i></dt>
<dd> <p> Update the status bar every <i>interval</i> seconds. By default, updates will occur every 15 seconds. A setting of zero disables redrawing at interval. </p>
 </dd>
<dt><code> status-justify</code> [<code>left | centre | right</code> ] </dt>
<dd>  </dd>
<dd> <p> Set the position of the window list component of the status line: left, centre or right justified. </p>
 </dd>
<dt><code> status-keys</code> [<code>vi | emacs</code> ] </dt>
<dd>  </dd>
<dd> <p> Use vi or emacs-style key bindings in the status line, for example at the command prompt. The default is emacs, unless the <code>VISUAL</code> or <code>EDITOR</code> environment variables are set and contain the string `vi&#8217; </p>
 </dd>
<dt><code>status-left </code><i>string</i></dt>
<dd> <p> Display <i>string</i> to the left of the status bar. <i>string</i> will be passed through <a href="/docs/linux/man/3-strftime/">strftime</a>(3) before being used. By default, the session name is shown. <i>string</i> may contain any of the following special character sequences: </p>
 </dd>
<dl>
<dt><code>Character pair Ta </code><code>Replaced with</code></dt>
<dd>  </dd>
<dt><code>#(shell-command) Ta </code>First line of the command&#8217;s output </dt>
<dd>  </dd>
<dt><code>#[attributes] Ta </code>Colour or attribute change </dt>
<dd>  </dd>
<dt><code>#H Ta </code>Hostname of local host </dt>
<dd>  </dd>
<dt><code>#h Ta </code>Hostname of local host without the domain name </dt>
<dd>  </dd>
<dt><code>#F Ta </code>Current window flag </dt>
<dd>  </dd>
<dt><code>#I Ta </code>Current window index </dt>
<dd>  </dd>
<dt><code>#D Ta </code>Current pane unique identifier </dt>
<dd>  </dd>
<dt><code>#P Ta </code>Current pane index </dt>
<dd>  </dd>
<dt><code>#S Ta </code>Session name </dt>
<dd>  </dd>
<dt><code>#T Ta </code>Current pane title </dt>
<dd>  </dd>
<dt><code>#W Ta </code>Current window name </dt>
<dd>  </dd>
<dt><code>## Ta </code>A literal `#&#8216; </dt>
<dd>  </dd></dl>
<p> The #(shell-command) form executes `shell-command&#8217; and inserts the first line of its output. Note that shell commands are only executed once at the interval specified by the <code>status-interval</code> option: if the status line is redrawn in the meantime, the previous result is used. Shell commands are executed with the <code>tmux</code> global environment set (see the Sx ENVIRONMENT section). </p>
<p> For details on how the names and titles can be set see the Sx NAMES AND TITLES section. </p>
<p> #[attributes] allows a comma-separated list of attributes to be specified, these may be `fg=colour&#8217; to set the foreground colour, `bg=colour&#8217; to set the background colour, the name of one of the attributes (listed under the <code>message-attr</code> option) to turn an attribute on, or an attribute prefixed with `no&#8217; to turn one off, for example <code>nobright</code> Examples are: </p>
<blockquote><pre><code>#(sysctl vm.loadavg)
#[fg=yellow,bold]#(apm -l)%%#[default] [#S]
</code></pre>
</blockquote>
<p> Where appropriate, special character sequences may be prefixed with a number to specify the maximum length, for example `#24T&#8217; </p>
<p> By default, UTF-8 in <i>string</i> is not interpreted, to enable UTF-8, use the <code>status-utf8</code> option. </p>
<dt><code>status-left-attr </code><i>attributes</i></dt>
<dd> <p> Set the attribute of the left part of the status line. </p>
 </dd>
<dt><code>status-left-bg </code><i>colour</i></dt>
<dd> <p> Set the background colour of the left part of the status line. </p>
 </dd>
<dt><code>status-left-fg </code><i>colour</i></dt>
<dd> <p> Set the foreground colour of the left part of the status line. </p>
 </dd>
<dt><code>status-left-length </code><i>length</i></dt>
<dd> <p> Set the maximum <i>length</i> of the left component of the status bar. The default is 10. </p>
 </dd>
<dt><code> status-position</code> [<code>top | bottom</code> ] </dt>
<dd>  </dd>
<dd> <p> Set the position of the status line. </p>
 </dd>
<dt><code>status-right </code><i>string</i></dt>
<dd> <p> Display <i>string</i> to the right of the status bar. By default, the current window title in double quotes, the date and the time are shown. As with <code>status-left</code> <i>string</i> will be passed to <a href="/docs/linux/man/3-strftime/">strftime</a>(3), character pairs are replaced, and UTF-8 is dependent on the <code>status-utf8</code> option. </p>
 </dd>
<dt><code>status-right-attr </code><i>attributes</i></dt>
<dd> <p> Set the attribute of the right part of the status line. </p>
 </dd>
<dt><code>status-right-bg </code><i>colour</i></dt>
<dd> <p> Set the background colour of the right part of the status line. </p>
 </dd>
<dt><code>status-right-fg </code><i>colour</i></dt>
<dd> <p> Set the foreground colour of the right part of the status line. </p>
 </dd>
<dt><code>status-right-length </code><i>length</i></dt>
<dd> <p> Set the maximum <i>length</i> of the right component of the status bar. The default is 40. </p>
 </dd>
<dt><code> status-utf8</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Instruct <code>tmux</code> to treat top-bit-set characters in the <code>status-left</code> and <code>status-right</code> strings as UTF-8; notably, this is important for wide characters. This option defaults to off. </p>
 </dd>
<dt><code>terminal-overrides </code><i>string</i></dt>
<dd> <p> Contains a list of entries which override terminal descriptions read using <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5). <i>string</i> is a comma-separated list of items each a colon-separated string made up of a terminal type pattern (matched using <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3)) and a set of <i>name=value</i> entries. </p>
<p> For example, to set the `clear&#8217; <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) entry to `\e[H\e[2J&#8217; for all terminal types and the `dch1&#8217; entry to `\e[P&#8217; for the `rxvt&#8217; terminal type, the option could be set to the string: </p>
<blockquote><pre><code>&quot;*:clear=\e[H\e[2J,rxvt:dch1=\e[P&quot;
</code></pre>
</blockquote>
<p> The terminal entry value is passed through strunvis(3) before interpretation. The default value forcibly corrects the `colors&#8217; entry for terminals which support 88 or 256 colours: </p>
<blockquote><pre><code>&quot;*88col*:colors=88,*256col*:colors=256,xterm*:XT&quot;
</code></pre>
</blockquote>
 </dd>
<dt><code>update-environment </code><i>variables</i></dt>
<dd> <p> Set a space-separated string containing a list of environment variables to be copied into the session environment when a new session is created or an existing session is attached. Any variables that do not exist in the source environment are set to be removed from the session environment (as if -<code>r</code> was given to the <code>set-environment</code> command). The default is &quot;DISPLAY SSH_ASKPASS SSH_AUTH_SOCK SSH_AGENT_PID SSH_CONNECTION WINDOWID XAUTHORITY&quot;. </p>
 </dd>
<dt><code> visual-activity</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If on, display a status line message when activity occurs in a window for which the <code>monitor-activity</code> window option is enabled. </p>
 </dd>
<dt><code> visual-bell</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If this option is on, a message is shown on a bell instead of it being passed through to the terminal (which normally makes a sound). Also see the <code>bell-action</code> option. </p>
 </dd>
<dt><code> visual-content</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Like <code>visual-activity</code> display a message when content is present in a window for which the <code>monitor-content</code> window option is enabled. </p>
 </dd>
<dt><code> visual-silence</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If <code>monitor-silence</code> is enabled, prints a message after the interval has expired on a given window. </p>
 </dd>
<dt><code>word-separators </code><i>string</i></dt>
<dd> <p> Sets the session&#8217;s conception of what characters are considered word separators, for the purposes of the next and previous word commands in copy mode. The default is `-_@ .&#8216; </p>
 </dd></dl>
<dt><code> set-window-option</code> [-<code>agqu</code> ] [-<code>t </code><i>target-window</i> ] <i>option value</i></dt>
<dd>  </dd>
<dd> <p> Set a window option. The -<code>a</code> -<code>g</code> -<code>q</code> and -<code>u</code> flags work similarly to the <code>set-option</code> command. </p>
<p> Supported window options are: </p>
 </dd>
<dl>
<dt><code> aggressive-resize</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Aggressively resize the chosen window. This means that <code>tmux</code> will resize the window to the size of the smallest session for which it is the current window, rather than the smallest session to which it is attached. The window may resize when the current window is changed on another sessions; this option is good for full-screen programs which support <code>SIGWINCH</code> and poor for interactive programs such as shells. </p>
 </dd>
<dt><code> allow-rename</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Allow programs to change the window name using a terminal escape sequence (\033k...\033\\). The default is on. </p>
 </dd>
<dt><code> alternate-screen</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> This option configures whether programs running inside <code>tmux</code> may use the terminal alternate screen feature, which allows the <i>smcup</i> and <i>rmcup</i> <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) capabilities. The alternate screen feature preserves the contents of the window when an interactive application starts and restores it on exit, so that any output visible before the application starts reappears unchanged after it exits. The default is on. </p>
 </dd>
<dt><code> automatic-rename</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Control automatic window renaming. When this setting is enabled, <code>tmux</code> will attempt - on supported platforms - to rename the window to reflect the command currently running in it. This flag is automatically disabled for an individual window when a name is specified at creation with <code>new-window</code> or <code>new-session</code> or later with <code>rename-window</code> or with a terminal escape sequence. It may be switched off globally with: </p>
<blockquote><pre><code>set-window-option -g automatic-rename off
</code></pre>
</blockquote>
 </dd>
<dt><code>c0-change-interval </code><i>interval</i></dt>
<dd>  </dd>
<dt><code>c0-change-trigger </code><i>trigger</i></dt>
<dd> <p> These two options configure a simple form of rate limiting for a pane. If <code>tmux</code> sees more than <i>trigger</i> C0 sequences that modify the screen (for example, carriage returns, linefeeds or backspaces) in one millisecond, it will stop updating the pane immediately and instead redraw it entirely every <i>interval</i> milliseconds. This helps to prevent fast output (such as <a href="/docs/linux/man/1-yes/">yes</a>(1) overwhelming the terminal). The default is a trigger of 250 and an interval of 100. A trigger of zero disables the rate limiting. </p>
 </dd>
<dt><code>clock-mode-colour </code><i>colour</i></dt>
<dd> <p> Set clock colour. </p>
 </dd>
<dt><code> clock-mode-style</code> [<code>12 | 24</code> ] </dt>
<dd>  </dd>
<dd> <p> Set clock hour format. </p>
 </dd>
<dt><code>force-height </code><i>height</i></dt>
<dd>  </dd>
<dt><code>force-width </code><i>width</i></dt>
<dd> <p> Prevent <code>tmux</code> from resizing a window to greater than <i>width</i> or <i>height</i> A value of zero restores the default unlimited setting. </p>
 </dd>
<dt><code>main-pane-height </code><i>height</i></dt>
<dd>  </dd>
<dt><code>main-pane-width </code><i>width</i></dt>
<dd> <p> Set the width or height of the main (left or top) pane in the <code>main-horizontal</code> or <code>main-vertical</code> layouts. </p>
 </dd>
<dt><code>mode-attr </code><i>attributes</i></dt>
<dd> <p> Set window modes attributes. </p>
 </dd>
<dt><code>mode-bg </code><i>colour</i></dt>
<dd> <p> Set window modes background colour. </p>
 </dd>
<dt><code>mode-fg </code><i>colour</i></dt>
<dd> <p> Set window modes foreground colour. </p>
 </dd>
<dt><code> mode-keys</code> [<code>vi | emacs</code> ] </dt>
<dd>  </dd>
<dd> <p> Use vi or emacs-style key bindings in copy and choice modes. As with the <code>status-keys</code> option, the default is emacs, unless <code>VISUAL</code> or <code>EDITOR</code> contains `vi&#8217; </p>
 </dd>
<dt><code> mode-mouse</code> [<code>on | off | copy-mode</code> ] </dt>
<dd>  </dd>
<dd> <p> Mouse state in modes. If on, the mouse may be used to enter copy mode and copy a selection by dragging, to enter copy mode and scroll with the mouse wheel, or to select an option in choice mode. If set to <i>copy-mode</i> the mouse behaves as set to on, but cannot be used to enter copy mode. </p>
 </dd>
<dt><code> monitor-activity</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Monitor for activity in the window. Windows with activity are highlighted in the status line. </p>
 </dd>
<dt><code>monitor-content </code><i>match-string</i></dt>
<dd> <p> Monitor content in the window. When <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) pattern <i>match-string</i> appears in the window, it is highlighted in the status line. </p>
 </dd>
<dt><code> monitor-silence</code> [<code>interval</code> ] </dt>
<dd>  </dd>
<dd> <p> Monitor for silence (no activity) in the window within <code>interval</code> seconds. Windows that have been silent for the interval are highlighted in the status line. An interval of zero disables the monitoring. </p>
 </dd>
<dt><code>other-pane-height </code><i>height</i></dt>
<dd> <p> Set the height of the other panes (not the main pane) in the <code>main-horizontal</code> layout. If this option is set to 0 (the default), it will have no effect. If both the <code>main-pane-height</code> and <code>other-pane-height</code> options are set, the main pane will grow taller to make the other panes the specified height, but will never shrink to do so. </p>
 </dd>
<dt><code>other-pane-width </code><i>width</i></dt>
<dd> <p> Like <code>other-pane-height</code> but set the width of other panes in the <code>main-vertical</code> layout. </p>
 </dd>
<dt><code>pane-base-index </code><i>index</i></dt>
<dd> <p> Like <code>base-index</code> but set the starting index for pane numbers. </p>
 </dd>
<dt><code> remain-on-exit</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> A window with this flag set is not destroyed when the program running in it exits. The window may be reactivated with the <code>respawn-window</code> command. </p>
 </dd>
<dt><code> synchronize-panes</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Duplicate input to any pane to all other panes in the same window (only for panes that are not in any special mode). </p>
 </dd>
<dt><code> utf8</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> Instructs <code>tmux</code> to expect UTF-8 sequences to appear in this window. </p>
 </dd>
<dt><code>window-status-bell-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for windows which have a bell alert. </p>
 </dd>
<dt><code>window-status-bell-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for windows with a bell alert. </p>
 </dd>
<dt><code>window-status-bell-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for windows with a bell alert. </p>
 </dd>
<dt><code>window-status-content-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for windows which have a content alert. </p>
 </dd>
<dt><code>window-status-content-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for windows with a content alert. </p>
 </dd>
<dt><code>window-status-content-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for windows with a content alert. </p>
 </dd>
<dt><code>window-status-activity-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for windows which have an activity (or silence) alert. </p>
 </dd>
<dt><code>window-status-activity-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for windows with an activity alert. </p>
 </dd>
<dt><code>window-status-activity-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for windows with an activity alert. </p>
 </dd>
<dt><code>window-status-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for a single window. </p>
 </dd>
<dt><code>window-status-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for a single window. </p>
 </dd>
<dt><code>window-status-current-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for the currently active window. </p>
 </dd>
<dt><code>window-status-current-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for the currently active window. </p>
 </dd>
<dt><code>window-status-current-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for the currently active window. </p>
 </dd>
<dt><code>window-status-current-format </code><i>string</i></dt>
<dd> <p> Like <i>window-status-format</i> but is the format used when the window is the current window. </p>
 </dd>
<dt><code>window-status-last-attr </code><i>attributes</i></dt>
<dd> <p> Set status line attributes for the last active window. </p>
 </dd>
<dt><code>window-status-last-bg </code><i>colour</i></dt>
<dd> <p> Set status line background colour for the last active window. </p>
 </dd>
<dt><code>window-status-last-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for the last active window. </p>
 </dd>
<dt><code>window-status-fg </code><i>colour</i></dt>
<dd> <p> Set status line foreground colour for a single window. </p>
 </dd>
<dt><code>window-status-format </code><i>string</i></dt>
<dd> <p> Set the format in which the window is displayed in the status line window list. See the <i>status-left</i> option for details of special character sequences available. The default is `#I:#W#F&#8217; </p>
 </dd>
<dt><code>window-status-separator </code><i>string</i></dt>
<dd> <p> Sets the separator drawn between windows in the status line. The default is a single space character. </p>
 </dd>
<dt><code> xterm-keys</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If this option is set, <code>tmux</code> will generate <a href="/docs/linux/man/1-xterm/">xterm</a>(1)-style function key sequences; these have a number included to indicate modifiers such as Shift, Alt or Ctrl. The default is off. </p>
 </dd>
<dt><code> wrap-search</code> [<code>on | off</code> ] </dt>
<dd>  </dd>
<dd> <p> If this option is set, searches will wrap around the end of the pane contents. The default is on. </p>
 </dd></dl>
<dt><code> show-options</code> [-<code>gqsvw</code> ] [-<code>t </code><i>target-session | target-window</i> ] [<i>option</i> ] </dt>
<dd>  </dd>
<dd> <p> Show the window options (or a single window option if given) with -<code>w</code> (equivalent to <code>show-window-options )</code> the server options with -<code>s</code> otherwise the session options for <i>target session</i> Global session or window options are listed if -<code>g</code> is used. -<code>v</code> shows only the option value, not the name. If -<code>q</code> is set, no error will be returned if <i>option</i> is unset. </p>
 </dd>
<dt><code> show-window-options</code> [-<code>gv</code> ] [-<code>t </code><i>target-window</i> ] [<i>option</i> ] </dt>
<dd>  </dd>
<dd> <p> List the window options or a single option for <i>target-window</i> or the global window options if -<code>g</code> is used. -<code>v</code> shows only the option value, not the name. </p>
 </dd></dl>
<h2>FORMATS</h2>
<p> Certain commands accept the -<code>F</code> flag with a <i>format</i> argument. This is a string which controls the output format of the command. Special character sequences are replaced as documented under the <code>status-left</code> option and an additional long form is accepted. Replacement variables are enclosed in `#{&#8216; and `}&#8216; , for example `#{session_name}&#8216; is equivalent to `#S&#8217; Conditionals are also accepted by prefixing with `?&#8216; and separating two alternatives with a comma; if the specified variable exists and is not zero, the first alternative is chosen, otherwise the second is used. For example `#{?session_attached,attached,not&#8217; attached} will include the string `attached&#8217; if the session is attached and the string `not&#8217; attached if it is unattached. </p>
<p> The following variables are available, where appropriate: </p>
<dl>
<dt><code>Variable name Ta </code><code>Replaced with</code></dt>
<dd>  </dd>
<dt><code>alternate_on Ta </code>If pane is in alternate screen </dt>
<dd>  </dd>
<dt><code>alternate_saved_x Ta </code>Saved cursor X in alternate screen </dt>
<dd>  </dd>
<dt><code>alternate_saved_y Ta </code>Saved cursor Y in alternate screen </dt>
<dd>  </dd>
<dt><code>buffer_sample Ta </code>First 50 characters from the specified buffer </dt>
<dd>  </dd>
<dt><code>buffer_size Ta </code>Size of the specified buffer in bytes </dt>
<dd>  </dd>
<dt><code>client_activity Ta </code>Integer time client last had activity </dt>
<dd>  </dd>
<dt><code>client_activity_string Ta </code>String time client last had activity </dt>
<dd>  </dd>
<dt><code>client_created Ta </code>Integer time client created </dt>
<dd>  </dd>
<dt><code>client_created_string Ta </code>String time client created </dt>
<dd>  </dd>
<dt><code>client_cwd Ta </code>Working directory of client </dt>
<dd>  </dd>
<dt><code>client_height Ta </code>Height of client </dt>
<dd>  </dd>
<dt><code>client_last_session Ta </code>Name of the client&#8217;s last session </dt>
<dd>  </dd>
<dt><code>client_prefix Ta </code>1 if prefix key has been pressed </dt>
<dd>  </dd>
<dt><code>client_readonly Ta </code>1 if client is readonly </dt>
<dd>  </dd>
<dt><code>client_session Ta </code>Name of the client&#8217;s session </dt>
<dd>  </dd>
<dt><code>client_termname Ta </code>Terminal name of client </dt>
<dd>  </dd>
<dt><code>client_tty Ta </code>Pseudo terminal of client </dt>
<dd>  </dd>
<dt><code>client_utf8 Ta </code>1 if client supports utf8 </dt>
<dd>  </dd>
<dt><code>client_width Ta </code>Width of client </dt>
<dd>  </dd>
<dt><code>cursor_flag Ta </code>Pane cursor flag </dt>
<dd>  </dd>
<dt><code>cursor_x Ta </code>Cursor X position in pane </dt>
<dd>  </dd>
<dt><code>cursor_y Ta </code>Cursor Y position in pane </dt>
<dd>  </dd>
<dt><code>history_bytes Ta </code>Number of bytes in window history </dt>
<dd>  </dd>
<dt><code>history_limit Ta </code>Maximum window history lines </dt>
<dd>  </dd>
<dt><code>history_size Ta </code>Size of history in bytes </dt>
<dd>  </dd>
<dt><code>host Ta </code>Hostname of local host </dt>
<dd>  </dd>
<dt><code>insert_flag Ta </code>Pane insert flag </dt>
<dd>  </dd>
<dt><code>keypad_cursor_flag Ta </code>Pane keypad cursor flag </dt>
<dd>  </dd>
<dt><code>keypad_flag Ta </code>Pane keypad flag </dt>
<dd>  </dd>
<dt><code>line Ta </code>Line number in the list </dt>
<dd>  </dd>
<dt><code>mouse_any_flag Ta </code>Pane mouse any flag </dt>
<dd>  </dd>
<dt><code>mouse_button_flag Ta </code>Pane mouse button flag </dt>
<dd>  </dd>
<dt><code>mouse_standard_flag Ta </code>Pane mouse standard flag </dt>
<dd>  </dd>
<dt><code>mouse_utf8_flag Ta </code>Pane mouse UTF-8 flag </dt>
<dd>  </dd>
<dt><code>pane_active Ta </code>1 if active pane </dt>
<dd>  </dd>
<dt><code>pane_current_command Ta </code>Current command if available </dt>
<dd>  </dd>
<dt><code>pane_current_path Ta </code>Current path if available </dt>
<dd>  </dd>
<dt><code>pane_dead Ta </code>1 if pane is dead </dt>
<dd>  </dd>
<dt><code>pane_height Ta </code>Height of pane </dt>
<dd>  </dd>
<dt><code>pane_id Ta </code>Unique pane ID </dt>
<dd>  </dd>
<dt><code>pane_in_mode Ta </code>If pane is in a mode </dt>
<dd>  </dd>
<dt><code>pane_index Ta </code>Index of pane </dt>
<dd>  </dd>
<dt><code>pane_pid Ta </code>PID of first process in pane </dt>
<dd>  </dd>
<dt><code>pane_start_command Ta </code>Command pane started with </dt>
<dd>  </dd>
<dt><code>pane_start_path Ta </code>Path pane started with </dt>
<dd>  </dd>
<dt><code>pane_tabs Ta </code>Pane tab positions </dt>
<dd>  </dd>
<dt><code>pane_title Ta </code>Title of pane </dt>
<dd>  </dd>
<dt><code>pane_tty Ta </code>Pseudo terminal of pane </dt>
<dd>  </dd>
<dt><code>pane_width Ta </code>Width of pane </dt>
<dd>  </dd>
<dt><code>saved_cursor_x Ta </code>Saved cursor X in pane </dt>
<dd>  </dd>
<dt><code>saved_cursor_y Ta </code>Saved cursor Y in pane </dt>
<dd>  </dd>
<dt><code>scroll_region_lower Ta </code>Bottom of scroll region in pane </dt>
<dd>  </dd>
<dt><code>scroll_region_upper Ta </code>Top of scroll region in pane </dt>
<dd>  </dd>
<dt><code>session_attached Ta </code>1 if session attached </dt>
<dd>  </dd>
<dt><code>session_created Ta </code>Integer time session created </dt>
<dd>  </dd>
<dt><code>session_created_string Ta </code>String time session created </dt>
<dd>  </dd>
<dt><code>session_group Ta </code>Number of session group </dt>
<dd>  </dd>
<dt><code>session_grouped Ta </code>1 if session in a group </dt>
<dd>  </dd>
<dt><code>session_height Ta </code>Height of session </dt>
<dd>  </dd>
<dt><code>session_id Ta </code>Unique session ID </dt>
<dd>  </dd>
<dt><code>session_name Ta </code>Name of session </dt>
<dd>  </dd>
<dt><code>session_width Ta </code>Width of session </dt>
<dd>  </dd>
<dt><code>session_windows Ta </code>Number of windows in session </dt>
<dd>  </dd>
<dt><code>window_active Ta </code>1 if window active </dt>
<dd>  </dd>
<dt><code>window_find_matches Ta </code>Matched data from the find-window command if available </dt>
<dd>  </dd>
<dt><code>window_flags Ta </code>Window flags </dt>
<dd>  </dd>
<dt><code>window_height Ta </code>Height of window </dt>
<dd>  </dd>
<dt><code>window_id Ta </code>Unique window ID </dt>
<dd>  </dd>
<dt><code>window_index Ta </code>Index of window </dt>
<dd>  </dd>
<dt><code>window_layout Ta </code>Window layout description </dt>
<dd>  </dd>
<dt><code>window_name Ta </code>Name of window </dt>
<dd>  </dd>
<dt><code>window_panes Ta </code>Number of panes in window </dt>
<dd>  </dd>
<dt><code>window_width Ta </code>Width of window </dt>
<dd>  </dd>
<dt><code>wrap_flag Ta </code>Pane wrap flag </dt>
<dd>  </dd></dl>
<h2>NAMES AND TITLES</h2>
<p> <code>tmux</code> distinguishes between names and titles. Windows and sessions have names, which may be used to specify them in targets and are displayed in the status line and various lists: the name is the <code>tmux</code> identifier for a window or session. Only panes have titles. A pane&#8217;s title is typically set by the program running inside the pane and is not modified by <code>.</code> It is the same mechanism used to set for example the <a href="/docs/linux/man/1-xterm/">xterm</a>(1) window title in an <a href="/docs/linux/man/7-X/">X</a>(7) window manager. Windows themselves do not have titles - a window&#8217;s title is the title of its active pane. <code>tmux</code> itself may set the title of the terminal in which the client is running, see the <code>set-titles</code> option. </p>
<p> A session&#8217;s name is set with the <code>new-session</code> and <code>rename-session</code> commands. A window&#8217;s name is set with one of: </p>
<ol>
<li> <p> A command argument (such as -<code>n</code> for <code>new-window</code> or <code>new-session )</code>  </li>
<li>  An escape sequence: </p>
<blockquote><pre><code>$ printf '\033kWINDOW_NAME\033\\'
</code></pre>
</blockquote>
 </li>
<li> <p> Automatic renaming, which sets the name to the active command in the window&#8217;s active pane. See the <code>automatic-rename</code> option.  </li>
</ol>
 </p>
<p> When a pane is first created, its title is the hostname. A pane&#8217;s title can be set via the OSC title setting sequence, for example: </p>
<blockquote><pre><code>$ printf '\033]2;My Title\033\\'
</code></pre>
</blockquote>
<h2>ENVIRONMENT</h2>
<p> When the server is started, <code>tmux</code> copies the environment into the <i>global environment</i> in addition, each session has a <i>session environment</i> When a window is created, the session and global environments are merged. If a variable exists in both, the value from the session environment is used. The result is the initial environment passed to the new process. </p>
<p> The <code>update-environment</code> session option may be used to update the session environment from the client when a new session is created or an old reattached. <code>tmux</code> also initialises the <code>TMUX</code> variable with some internal information to allow commands to be executed from inside, and the <code>TERM</code> variable with the correct terminal setting of `screen&#8217; </p>
<p> Commands to alter and view the environment are: </p>
<dl>
<dt><code> set-environment</code> [-<code>gru</code> ] [-<code>t </code><i>target-session</i> ] <i>name </i>[<i>value</i> ] </dt>
<dd>  </dd>
<dd> <p> Set or unset an environment variable. If -<code>g</code> is used, the change is made in the global environment; otherwise, it is applied to the session environment for <i>target-session</i> The -<code>u</code> flag unsets a variable. -<code>r</code> indicates the variable is to be removed from the environment before starting a new process. </p>
 </dd>
<dt><code> show-environment</code> [-<code>g</code> ] [-<code>t </code><i>target-session</i> ] [<i>variable</i> ] </dt>
<dd>  </dd>
<dd> <p> Display the environment for <i>target-session</i> or the global environment with -<code>g</code> If <i>variable</i> is omitted, all variables are shown. Variables removed from the environment are prefixed with `-&#8216; </p>
 </dd></dl>
<h2>STATUS LINE</h2>
<p> <code>tmux</code> includes an optional status line which is displayed in the bottom line of each terminal. By default, the status line is enabled (it may be disabled with the <code>status</code> session option) and contains, from left-to-right: the name of the current session in square brackets; the window list; the title of the active pane in double quotes; and the time and date. </p>
<p> The status line is made of three parts: configurable left and right sections (which may contain dynamic content such as the time or output from a shell command, see the <code>status-left</code> <code>status-left-length</code> <code>status-right</code> and <code>status-right-length</code> options below), and a central window list. By default, the window list shows the index, name and (if any) flag of the windows present in the current session in ascending numerical order. It may be customised with the <i>window-status-format</i> and <i>window-status-current-format</i> options. The flag is one of the following symbols appended to the window name: </p>
<dl>
<dt><code>Symbol Ta </code><code>Meaning</code></dt>
<dd>  </dd>
<dt><code>* Ta </code>Denotes the current window. </dt>
<dd>  </dd>
<dt><code>- Ta </code>Marks the last window (previously selected). </dt>
<dd>  </dd>
<dt><code># Ta </code>Window is monitored and activity has been detected. </dt>
<dd>  </dd>
<dt><code>! Ta </code>A bell has occurred in the window. </dt>
<dd>  </dd>
<dt><code>+ Ta </code>Window is monitored for content and it has appeared. </dt>
<dd>  </dd>
<dt><code>~ Ta </code>The window has been silent for the monitor-silence interval. </dt>
<dd>  </dd>
<dt><code>Z Ta </code>The window&#8217;s active pane is zoomed. </dt>
<dd>  </dd></dl>
<p> The # symbol relates to the <code>monitor-activity</code> and + to the <code>monitor-content</code> window options. The window name is printed in inverted colours if an alert (bell, activity or content) is present. </p>
<p> The colour and attributes of the status line may be configured, the entire status line using the <code>status-attr</code> <code>status-fg</code> and <code>status-bg</code> session options and individual windows using the <code>window-status-attr</code> <code>window-status-fg</code> and <code>window-status-bg</code> window options. </p>
<p> The status line is automatically refreshed at interval if it has changed, the interval may be controlled with the <code>status-interval</code> session option. </p>
<p> Commands related to the status line are as follows: </p>
<dl>
<dt><code> command-prompt</code> [-<code>I </code><i>inputs</i> ] [-<code>p </code><i>prompts</i> ] [-<code>t </code><i>target-client</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Open the command prompt in a client. This may be used from inside <code>tmux</code> to execute commands interactively. </p>
<p> If <i>template</i> is specified, it is used as the command. If present, -<code>I</code> is a comma-separated list of the initial text for each prompt. If -<code>p</code> is given, <i>prompts</i> is a comma-separated list of prompts which are displayed in order; otherwise a single prompt is displayed, constructed from <i>template</i> if it is present, or `:&#8216; if not. </p>
<p> Both <i>inputs</i> and <i>prompts</i> may contain the special character sequences supported by the <code>status-left</code> option. </p>
<p> Before the command is executed, the first occurrence of the string `%%&#8216; and all occurrences of `%1&#8217; are replaced by the response to the first prompt, the second `%%&#8216; and all `%2&#8217; are replaced with the response to the second prompt, and so on for further prompts. Up to nine prompt responses may be replaced Po `%1&#8217; to `%9&#8217; Pc . </p>
 </dd>
<dt><code> confirm-before</code> [-<code>p </code><i>prompt</i> ] [-<code>t </code><i>target-client</i> ] <i>command</i></dt>
<dd>  </dd>
<dd> <p> Ask for confirmation before executing <i>command</i> If -<code>p</code> is given, <i>prompt</i> is the prompt to display; otherwise a prompt is constructed from <i>command</i> It may contain the special character sequences supported by the <code>status-left</code> option. </p>
<p> This command works only from inside <code>.</code> </p>
 </dd>
<dt><code> display-message</code> [-<code>p</code> ] [-<code>c </code><i>target-client</i> ] [-<code>t </code><i>target-pane</i> ] [<i>message</i> ] </dt>
<dd>  </dd>
<dd> <p> Display a message. If -<code>p</code> is given, the output is printed to stdout, otherwise it is displayed in the <i>target-client</i> status line. The format of <i>message</i> is described in the Sx FORMATS section; information is taken from <i>target-pane</i> if -<code>t</code> is given, otherwise the active pane for the session attached to <i>target-client</i> </p>
 </dd></dl>
<h2>BUFFERS</h2>
<p> <code>tmux</code> maintains a stack of <i>paste buffers</i> Up to the value of the <code>buffer-limit</code> option are kept; when a new buffer is added, the buffer at the bottom of the stack is removed. Buffers may be added using <code>copy-mode</code> or the <code>set-buffer</code> command, and pasted into a window using the <code>paste-buffer</code> command. </p>
<p> A configurable history buffer is also maintained for each window. By default, up to 2000 lines are kept; this can be altered with the <code>history-limit</code> option (see the <code>set-option</code> command above). </p>
<p> The buffer commands are as follows: </p>
<dl>
<dt><code>choose-buffer</code> [-<code>F </code><i>format</i> ] [-<code>t </code><i>target-window</i> ] [<i>template</i> ] </dt>
<dd>  </dd>
<dd> <p> Put a window into buffer choice mode, where a buffer may be chosen interactively from a list. After a buffer is selected, `%%&#8216; is replaced by the buffer index in <i>template</i> and the result executed as a command. If <i>template</i> is not given, &quot;paste-buffer -b &#8216;%%&#8216;&quot; is used. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. This command works only if at least one client is attached. </p>
 </dd>
<dt><code>clear-history </code>[-<code>t </code><i>target-pane</i> ] </dt>
<dd> <p> Remove and free the history for the specified pane. </p>
 </dd>
<dt><code>delete-buffer </code>[-<code>b </code><i>buffer-index</i> ] </dt>
<dd> <p> Delete the buffer at <i>buffer-index</i> or the top buffer if not specified. </p>
 </dd>
<dt><code> list-buffers</code> [-<code>F </code><i>format</i> ] </dt>
<dd>  </dd>
<dd> <p> List the global buffers. For the meaning of the -<code>F</code> flag, see the Sx FORMATS section. </p>
 </dd>
<dt><code> load-buffer</code> [-<code>b </code><i>buffer-index</i> ] <i>path</i></dt>
<dd>  </dd>
<dd> <p> Load the contents of the specified paste buffer from <i>path</i> </p>
 </dd>
<dt><code> paste-buffer</code> [-<code>dpr</code> ] [-<code>b </code><i>buffer-index</i> ] [-<code>s </code><i>separator</i> ] [-<code>t </code><i>target-pane</i> ] </dt>
<dd>  </dd>
<dd> <p> Insert the contents of a paste buffer into the specified pane. If not specified, paste into the current one. With -<code>d</code> also delete the paste buffer from the stack. When output, any linefeed (LF) characters in the paste buffer are replaced with a separator, by default carriage return (CR). A custom separator may be specified using the -<code>s</code> flag. The -<code>r</code> flag means to do no replacement (equivalent to a separator of LF). If -<code>p</code> is specified, paste bracket control codes are inserted around the buffer if the application has requested bracketed paste mode. </p>
 </dd>
<dt><code> save-buffer</code> [-<code>a</code> ] [-<code>b </code><i>buffer-index</i> ] <i>path</i></dt>
<dd>  </dd>
<dd> <p> Save the contents of the specified paste buffer to <i>path</i> The -<code>a</code> option appends to rather than overwriting the file. </p>
 </dd>
<dt><code> set-buffer</code> [-<code>b </code><i>buffer-index</i> ] <i>data</i></dt>
<dd>  </dd>
<dd> <p> Set the contents of the specified buffer to <i>data</i> </p>
 </dd>
<dt><code> show-buffer</code> [-<code>b </code><i>buffer-index</i> ] </dt>
<dd>  </dd>
<dd> <p> Display the contents of the specified buffer. </p>
 </dd></dl>
<h2>MISCELLANEOUS</h2>
<p> Miscellaneous commands are as follows: </p>
<dl>
<dt><code>clock-mode </code>[-<code>t </code><i>target-pane</i> ] </dt>
<dd> <p> Display a large clock. </p>
 </dd>
<dt><code> if-shell</code> [-<code>b</code> ] [-<code>t </code><i>target-pane</i> ] <i>shell-command command</i> [<i>command</i> ] </dt>
<dd>  </dd>
<dd> <p> Execute the first <i>command</i> if <i>shell-command</i> returns success or the second <i>command</i> otherwise. Before being executed, shell-command is expanded using the rules specified in the Sx FORMATS section, including those relevant to <i>target-pane</i> With -<code>b</code> <i>shell-command</i> is run in the background. </p>
 </dd>
<dt><code>lock-server</code></dt>
<dd> <p> Lock each client individually by running the command specified by the <code>lock-command</code> option. </p>
 </dd>
<dt><code> run-shell</code> -<code>b</code> [-<code>t </code><i>target-pane</i> ] <i>shell-command</i></dt>
<dd>  </dd>
<dd> <p> Execute <i>shell-command</i> in the background without creating a window. Before being executed, shell-command is expanded using the rules specified in the Sx FORMATS section. With -<code>b</code> the command is run in the background. After it finishes, any output to stdout is displayed in copy mode (in the pane specified by -<code>t</code> or the current pane if omitted). If the command doesn&#8217;t return success, the exit status is also displayed. </p>
 </dd>
<dt><code>server-info</code></dt>
<dd> <p> Show server information and terminal details. </p>
 </dd>
<dt><code> wait-for</code> -<code>LSU</code><i>channel</i></dt>
<dd>  </dd>
<dd> <p> When used without options, prevents the client from exiting until woken using <code>wait-for</code> -<code>S</code> with the same channel. When -<code>L</code> is used, the channel is locked and any clients that try to lock the same channel are made to wait until the channel is unlocked with <code>wait-for</code> -<code>U</code> This command only works from outside <code>.</code> </p>
 </dd></dl>
<h2>TERMINFO EXTENSIONS</h2>
<p> <code>tmux</code> understands some extensions to <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5): </p>
<dl>
<dt><i>Cc </i>, Cr Set the cursor colour. </dt>
<dd> <p> The first takes a single string argument and is used to set the colour; the second takes no arguments and restores the default cursor colour. If set, a sequence such as this may be used to change the cursor colour from inside <code>:</code> </p>
<blockquote><pre><code>$ printf '\033]12;red\033\\'
</code></pre>
</blockquote>
 </dd>
<dt><i>Cs </i>, Csr </dt>
<dd> <p> Change the cursor style. If set, a sequence such as this may be used to change the cursor to an underline: </p>
<blockquote><pre><code>$ printf '\033[4 q'
</code></pre>
</blockquote>
<p> If <i>Csr</i> is set, it will be used to reset the cursor style instead of <i>Cs </i> </p>
 </dd>
<dt><i></i><code>This sequence can be used by</code></dt>
<dd> <p> <code>tmux</code> to store the current buffer in the host terminal&#8217;s selection (clipboard). See the <i>set-clipboard</i> option above and the <a href="/docs/linux/man/1-xterm/">xterm</a>(1) man page. </p>
 </dd></dl>
<h2>CONTROL MODE</h2>
<p> <code>tmux</code> offers a textual interface called <i>control mode</i> This allows applications to communicate with <code>tmux</code> using a simple text-only protocol. </p>
<p> In control mode, a client sends <code>tmux</code> commands or command sequences terminated by newlines on standard input. Each command will produce one block of output on standard output. An output block consists of a <i>%begin</i> line followed by the output (which may be empty). The output block ends with a <i>%end</i> or <i>%error</i> <i>%begin</i> and matching <i>%end</i> or <i>%error</i> have two arguments: an integer time (as seconds from epoch) and command number. For example: </p>
<blockquote><pre><code>%begin 1363006971 2
0: ksh* (1 panes) [80x24] [layout b25f,80x24,0,0,2] @2 (active)
%end 1363006971 2
</code></pre>
</blockquote>
<p> In control mode, <code>tmux</code> outputs notifications. A notification will never occur inside an output block. </p>
<p> The following notifications are defined: </p>
<dl>
<dt><code>%exit </code>[<i>reason</i> ] </dt>
<dd> <p> The <code>tmux</code> client is exiting immediately, either because it is not attached to any session or an error occurred. If present, <i>reason</i> describes why the client exited. </p>
 </dd>
<dt><code>%layout-change </code><i>window-id window-layout</i></dt>
<dd> <p> The layout of a window with ID <i>window-id</i> changed. The new layout is <i>window-layout</i> </p>
 </dd>
<dt><code>%output </code><i>pane-id value</i></dt>
<dd> <p> A window pane produced output. <i>value</i> escapes non-printable characters and backslash as octal \xxx. </p>
 </dd>
<dt><code>%session-changed </code><i>session-id name</i></dt>
<dd> <p> The client is now attached to the session with ID <i>session-id</i> which is named <i>name</i> </p>
 </dd>
<dt><code>%session-renamed </code><i>name</i></dt>
<dd> <p> The current session was renamed to <i>name</i> </p>
 </dd>
<dt><code>%sessions-changed</code></dt>
<dd> <p> A session was created or destroyed. </p>
 </dd>
<dt><code>%unlinked-window-add </code><i>window-id</i></dt>
<dd> <p> The window with ID <i>window-id</i> was created but is not linked to the current session. </p>
 </dd>
<dt><code>%window-add </code><i>window-id</i></dt>
<dd> <p> The window with ID <i>window-id</i> was linked to the current session. </p>
 </dd>
<dt><code>%window-close </code><i>window-id</i></dt>
<dd> <p> The window with ID <i>window-id</i> closed. </p>
 </dd>
<dt><code>%window-renamed </code><i>window-id name</i></dt>
<dd> <p> The window with ID <i>window-id</i> was renamed to <i>name</i> </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.tmux.conf </code></dt>
<dd> <p> Default <code>tmux</code> configuration file. </p>
 </dd>
<dt><code>/etc/tmux.conf </code></dt>
<dd> <p> System-wide configuration file. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> To create a new <code>tmux</code> session running <a href="/docs/linux/man/1-vi/">vi</a>(1): </p>
<blockquote><p> <code>$ tmux new-session vi</code> </p>
</blockquote>
<p> Most commands have a shorter form, known as an alias. For new-session, this is <code>new</code> </p>
<blockquote><p> <code>$ tmux new vi</code> </p>
</blockquote>
<p> Alternatively, the shortest unambiguous form of a command is accepted. If there are several options, they are listed: </p>
<blockquote><pre><code>$ tmux n
ambiguous command: n, could be: new-session, new-window, next-window
</code></pre>
</blockquote>
<p> Within an active session, a new window may be created by typing `C-b&#8217; c (Ctrl followed by the `b&#8217; key followed by the `c&#8217; key). </p>
<p> Windows may be navigated with: `C-b&#8217; 0 (to select window 0), `C-b&#8217; 1 (to select window 1), and so on; `C-b&#8217; n to select the next window; and `C-b&#8217; p to select the previous window. </p>
<p> A session may be detached using `C-b&#8217; d (or by an external event such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1) disconnection) and reattached with: </p>
<blockquote><p> <code>$ tmux attach-session</code> </p>
</blockquote>
<p> Typing `C-b&#8217; ? lists the current key bindings in the current window; up and down may be used to navigate the list or `q&#8217; to exit from it. </p>
<p> Commands to be run when the <code>tmux</code> server is started may be placed in the ~/.tmux.conf configuration file. Common examples include: </p>
<p> Changing the default prefix key: </p>
<blockquote><pre><code>set-option -g prefix C-a
unbind-key C-b
bind-key C-a send-prefix
</code></pre>
</blockquote>
<p> Turning the status line off, or changing its colour: </p>
<blockquote><pre><code>set-option -g status off
set-option -g status-bg blue
</code></pre>
</blockquote>
<p> Setting other options, such as the default command, or locking after 30 minutes of inactivity: </p>
<blockquote><pre><code>set-option -g default-command &quot;exec /bin/ksh&quot;
set-option -g lock-after-time 1800
</code></pre>
</blockquote>
<p> Creating new key bindings: </p>
<blockquote><pre><code>bind-key b set-option status
bind-key / command-prompt &quot;split-window 'exec man %%'&quot;
bind-key S command-prompt &quot;new-window -n %1 'ssh %1'&quot;
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> pty(4)  </p>
<h2>AUTHORS</h2>
<p> An Nicholas Marriott Aq nicm [at] users.sourceforge.net </p>
