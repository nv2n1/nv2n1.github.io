---
title: "zshtcpsys(1)"
name: "zshtcpsys"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshtcpsys/"
description: "zshtcpsys – zsh tcp system"
---

<h2 class="name">NAME</h2>
<p> zshtcpsys &#8211; zsh tcp system </p>
<h2>DESCRIPTION</h2>
<p> A module <code>zsh/net/tcp</code> is provided to provide network I/O over TCP/IP from within the shell; see its description in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). This manual page describes a function suite based on the module. If the module is installed, the functions are usually installed at the same time, in which case they will be available for autoloading in the default function search path. In addition to the <code>zsh/net/tcp</code> module, the <code>zsh/zselect</code> module is used to implement timeouts on read operations. For troubleshooting tips, consult the corresponding advice for the <code>zftp</code> functions described in <i><a href="/docs/linux/man/1-zshzftpsys/">zshzftpsys</a></i>(1). </p>
<p> There are functions corresponding to the basic I/O operations open, close, read and send, named <code>tcp_open</code> etc., as well as a function <code>tcp_expect</code> for pattern match analysis of data read as input. The system makes it easy to receive data from and send data to multiple named sessions at once. In addition, it can be linked with the shell&#8217;s line editor in such a way that input data is automatically shown at the terminal. Other facilities available including logging, filtering and configurable output prompts. </p>
<p> To use the system where it is available, it should be enough to `<code>autoload -U tcp_open</code>&#8216; and run <code>tcp_open</code> as documented below to start a session. The <code>tcp_open</code> function will autoload the remaining functions. </p>
<h2>TCP USER FUNCTIONS</h2>
<h3>Basic I/O</h3>
<dl>
<dt>
<dd> <code>tcp_open</code> [ <code>-qz</code> ] <i>host port</i> [ <i>sess</i> ]</p>
<dt>
<dd> <code>tcp_open</code> [ <code>-qz</code> ] [ <code>-s</code> <i>sess</i> | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] ] &#8230;</p>
<dt>
<dd> <code>tcp_open</code> [ <code>-qz</code> ] [ <code>-a</code> <i>fd</i> | <code>-f</code> <i>fd</i> ] [ <i>sess</i> ] Open a new session. In the first and simplest form, open a TCP connection to host <i>host</i> at port <i>port</i>; numeric and symbolic forms are understood for both.</p>
<dl>
<dt>
<dd>
<p> If <i>sess</i> is given, this becomes the name of the session which can be used to refer to multiple different TCP connections. If <i>sess</i> is not given, the function will invent a numeric name value (note this is <i>not</i> the same as the file descriptor to which the session is attached). It is recommended that session names not include `funny&#8217; characters, where funny characters are not well-defined but certainly do not include alphanumerics or underscores, and certainly do include whitespace. </p>
<p> In the second case, one or more sessions to be opened are given by name. A single session name is given after <code>-s</code> and a comma-separated list after <code>-l</code>; both options may be repeated as many times as necessary. A failure to open any session causes <code>tcp_open</code> to abort. The host and port are read from the file <code>.ztcp_sessions</code> in the same directory as the user&#8217;s zsh initialisation files, i.e. usually the home directory, but <code>$ZDOTDIR</code> if that is set. The file consists of lines each giving a session name and the corresponding host and port, in that order (note the session name comes first, not last), separated by whitespace. </p>
<p> The third form allows passive and fake TCP connections. If the option <code>-a</code> is used, its argument is a file descriptor open for listening for connections. No function front-end is provided to open such a file descriptor, but a call to `<code>ztcp -l</code> <i>port</i>&#8216; will create one with the file descriptor stored in the parameter <code>$REPLY</code>. The listening port can be closed with `<code>ztcp -c</code> <i>fd</i>&#8216;. A call to `<code>tcp_open -a</code> <i>fd</i>&#8216; will block until a remote TCP connection is made to <i>port</i> on the local machine. At this point, a session is created in the usual way and is largely indistinguishable from an active connection created with one of the first two forms. </p>
<p> If the option <code>-f</code> is used, its argument is a file descriptor which is used directly as if it were a TCP session. How well the remainder of the TCP function system copes with this depends on what actually underlies this file descriptor. A regular file is likely to be unusable; a FIFO (pipe) of some sort will work better, but note that it is not a good idea for two different sessions to attempt to read from the same FIFO at once. </p>
<p> If the option <code>-q</code> is given with any of the three forms, <code>tcp_open</code> will not print informational messages, although it will in any case exit with an appropriate status. </p>
<p> If the line editor (zle) is in use, which is typically the case if the shell is interactive, <code>tcp_open</code> installs a handler inside zle which will check for new data at the same time as it checks for keyboard input. This is convenient as the shell consumes no CPU time while waiting; the test is performed by the operating system. Giving the option <code>-z</code> to any of the forms of <code>tcp_open</code> prevents the handler from being installed, so data must be read explicitly. Note, however, this is not necessary for executing complete sets of send and read commands from a function, as zle is not active at this point. Generally speaking, the handler is only active when the shell is waiting for input at a command prompt or in the <code>vared</code> builtin. The option has no effect if zle is not active; `<code>[[ -o zle]]</code>&#8216; will test for this. </p>
<p> The first session to be opened becomes the current session and subsequent calls to <code>tcp_open</code> do not change it. The current session is stored in the parameter <code>$TCP_SESS</code>; see below for more detail about the parameters used by the system. </p>
<p> The function <code>tcp_on_open</code>, if defined, is called when a session is opened. See the description below.</dl>
<dt><code>tcp_close</code> [ <code>-qn</code> ] [ <code>-a</code> | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] | <i>sess</i> &#8230; ]</p>
<dd> Close the named sessions, or the current session if none is given, or all open sessions if <code>-a</code> is given. The options <code>-l</code> and <code>-s</code> are both handled for consistency with <code>tcp_open</code>, although the latter is redundant.</p>
<dl>
<dt>
<dd>
<p> If the session being closed is the current one, <code>$TCP_SESS</code> is unset, leaving no current session, even if there are other sessions still open. </p>
<p> If the session was opened with <code>tcp_open -f</code>, the file descriptor is closed so long as it is in the range 0 to 9 accessible directly from the command line. If the option <code>-n</code> is given, no attempt will be made to close file descriptors in this case. The <code>-n</code> option is not used for genuine <code>ztcp</code> session; the file descriptors are always closed with the session. </p>
<p> If the option <code>-q</code> is given, no informational messages will be printed.</dl>
<dt>
<dd> <code>tcp_read </code>[ <code>-bdq</code> ] [ <code>-t</code> <i>TO</i> ] [ <code>-T</code> <i>TO</i> ]</p>
<dt>
<dd> [ <code>-a</code> | <code>-u</code> <i>fd</i>[<code>,</code>&#8230;] | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] | <code>-s</code> <i>sess</i> &#8230; ] Perform a read operation on the current session, or on a list of sessions if any are given with <code>-u</code>, <code>-l</code> or <code>-s</code>, or all open sessions if the option <code>-a</code> is given. Any of the <code>-u</code>, <code>-l</code> or <code>-s</code> options may be repeated or mixed together. The <code>-u</code> option specifies a file descriptor directly (only those managed by this system are useful), the other two specify sessions as described for <code>tcp_open</code> above.</p>
<dl>
<dt>
<dd>
<p> The function checks for new data available on all the sessions listed. Unless the <code>-b</code> option is given, it will not block waiting for new data. Any one line of data from any of the available sessions will be read, stored in the parameter <code>$TCP_LINE</code>, and displayed to standard output unless <code>$TCP_SILENT</code> contains a non-empty string. When printed to standard output the string <code>$TCP_PROMPT</code> will be shown at the start of the line; the default form for this includes the name of the session being read. See below for more information on these parameters. In this mode, <code>tcp_read</code> can be called repeatedly until it returns status 2 which indicates all pending input from all specified sessions has been handled. </p>
<p> With the option <code>-b</code>, equivalent to an infinite timeout, the function will block until a line is available to read from one of the specified sessions. However, only a single line is returned. </p>
<p> The option <code>-d</code> indicates that all pending input should be drained. In this case <code>tcp_read</code> may process multiple lines in the manner given above; only the last is stored in <code>$TCP_LINE</code>, but the complete set is stored in the array <code>$tcp_lines</code>. This is cleared at the start of each call to <code>tcp_read</code>. </p>
<p> The options <code>-t</code> and <code>-T</code> specify a timeout in seconds, which may be a floating point number for increased accuracy. With <code>-t</code> the timeout is applied before each line read. With <code>-T</code>, the timeout applies to the overall operation, possibly including multiple read operations if the option <code>-d</code> is present; without this option, there is no distinction between <code>-t</code> and <code>-T</code>. </p>
<p> The function does not print informational messages, but if the option <code>-q</code> is given, no error message is printed for a non-existent session. </p>
<p> A return status of 2 indicates a timeout or no data to read. Any other non-zero return status indicates some error condition. </p>
<p> See <code>tcp_log</code> for how to control where data is sent by <code>tcp_read</code>.</dl>
<dt>
<dd> <code>tcp_send</code> [ <code>-cnq</code> ] [ <code>-s</code> <i>sess</i> | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] ] <i>data</i> &#8230;</p>
<dt>
<dd> <code>tcp_send</code> [ <code>-cnq</code> ] <code>-a</code> <i>data</i> &#8230; Send the supplied data strings to all the specified sessions in turn. The underlying operation differs little from a `<code>print -r</code>&#8216; to the session&#8217;s file descriptor, although it attempts to prevent the shell from dying owing to a <code>SIGPIPE</code> caused by an attempt to write to a defunct session.</p>
<dl>
<dt>
<dd>
<p> The option <code>-c</code> causes <code>tcp_send</code> to behave like <code>cat</code>. It reads lines from standard input until end of input and sends them in turn to the specified session(s) exactly as if they were given as <i>data</i> arguments to individual <code>tcp_send</code> commands. </p>
<p> The option <code>-n</code> prevents <code>tcp_send</code> from putting a newline at the end of the data strings. </p>
<p> The remaining options all behave as for <code>tcp_read</code>. </p>
<p> The data arguments are not further processed once they have been passed to <code>tcp_send</code>; they are simply passed down to <code>print -r</code>. </p>
<p> If the parameter <code>$TCP_OUTPUT</code> is a non-empty string and logging is enabled then the data sent to each session will be echoed to the log file(s) with <code>$TCP_OUTPUT</code> in front where appropriate, much in the manner of <code>$TCP_PROMPT</code>.</dl>
</dl>
<h3>Session Management</h3>
<dl>
<dt>
<dd> <code>tcp_alias</code> [ <code>-q</code> ] <i>alias</i><code>=</code><i>sess</i> &#8230;</p>
<dt>
<dd> <code>tcp_alias</code> [ <code>-q</code> ] [ <i>alias</i> &#8230; ]</p>
<dt>
<dd> <code>tcp_alias</code> <code>-d</code> [ <code>-q</code> ] <i>alias</i> &#8230; This function is not particularly well tested.</p>
<dl>
<dt>
<dd>
<p> The first form creates an alias for a session name; <i>alias</i> can then be used to refer to the existing session <i>sess</i>. As many aliases may be listed as required. </p>
<p> The second form lists any aliases specified, or all aliases if none. </p>
<p> The third form deletes all the aliases listed. The underlying sessions are not affected. </p>
<p> The option <code>-q</code> suppresses an inconsistently chosen subset of error messages.</dl>
<dt><code>tcp_log</code> [ <code>-asc</code> ] [ <code>-n</code> | <code>-N</code> ] [ <i>logfile</i> ]</p>
<dd> With an argument <i>logfile</i>, all future input from <code>tcp_read</code> will be logged to the named file. Unless <code>-a</code> (append) is given, this file will first be truncated or created empty. With no arguments, show the current status of logging.</p>
<dl>
<dt>
<dd>
<p> With the option <code>-s</code>, per-session logging is enabled. Input from <code>tcp_read</code> is output to the file <i>logfile</i><code>.</code><i>sess</i>. As the session is automatically discriminated by the filename, the contents are raw (no <code>$TCP_PROMPT</code>). The option <code>-a</code> applies as above. Per-session logging and logging of all data in one file are not mutually exclusive. </p>
<p> The option <code>-c</code> closes all logging, both complete and per-session logs. </p>
<p> The options <code>-n</code> and <code>-N</code> respectively turn off or restore output of data read by <code>tcp_read</code> to standard output; hence `<code>tcp_log -cn</code>&#8216; turns off all output by <code>tcp_read</code>. </p>
<p> The function is purely a convenient front end to setting the parameters <code>$TCP_LOG</code>, <code>$TCP_LOG_SESS</code>, <code>$TCP_SILENT</code>, which are described below.</dl>
<dt><code>tcp_rename</code> <i>old</i> <i>new</i></p>
<dd> Rename session <i>old</i> to session <i>new</i>. The old name becomes invalid.</p>
<dt><code>tcp_sess</code> [ <i>sess</i> [ <i>command</i> [ <i>arg</i> &#8230; ] ] ]</p>
<dd> With no arguments, list all the open sessions and associated file descriptors. The current session is marked with a star. For use in functions, direct access to the parameters <code>$tcp_by_name</code>, <code>$tcp_by_fd</code> and <code>$TCP_SESS</code> is probably more convenient; see below.</p>
<dl>
<dt>
<dd>
<p> With a <i>sess</i> argument, set the current session to <i>sess</i>. This is equivalent to changing <code>$TCP_SESS</code> directly. </p>
<p> With additional arguments, temporarily set the current session while executing `<i>command</i> <i>arg</i> &#8230;&#8217;. <i>command</i> is re-evaluated so as to expand aliases etc., but the remaining <i>arg</i>s are passed through as that appear to <code>tcp_sess</code>. The original session is restored when <code>tcp_sess</code> exits.</dl>
</dl>
<h3>Advanced I/O</h3>
<dl>
<dt>
<dd> <code>tcp_command</code> <i>send-option</i> &#8230; <i>send-argument</i> &#8230; This is a convenient front-end to <code>tcp_send</code>. All arguments are passed to <code>tcp_send</code>, then the function pauses waiting for data. While data is arriving at least every <code>$TCP_TIMEOUT</code> (default 0.3) seconds, data is handled and printed out according to the current settings. Status 0 is always returned.</p>
<dl>
<dt>
<dd>
<p> This is generally only useful for interactive use, to prevent the display becoming fragmented by output returned from the connection. Within a programme or function it is generally better to handle reading data by a more explicit method.</dl>
<dt>
<dd> <code>tcp_expect </code>[ <code>-q</code> ] [ <code>-p</code> <i>var</i> | <code>-P</code> <i>var</i> ] [ <code>-t</code> <i>TO</i> | <code>-T</code> <i>TO</i> ]</p>
<dt>
<dd> [ <code>-a</code> | <code>-s</code> <i>sess</i> | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] ] <i>pattern</i> &#8230; Wait for input matching any of the given <i>pattern</i>s from any of the specified sessions. Input is ignored until an input line matches one of the given patterns; at this point status zero is returned, the matching line is stored in <code>$TCP_LINE</code>, and the full set of lines read during the call to <code>tcp_expect</code> is stored in the array <code>$tcp_expect_lines</code>.</p>
<dl>
<dt>
<dd>
<p> Sessions are specified in the same way as <code>tcp_read</code>: the default is to use the current session, otherwise the sessions specified by <code>-a</code>, <code>-s</code>, or <code>-l</code> are used. </p>
<p> Each <i>pattern</i> is a standard zsh extended-globbing pattern; note that it needs to be quoted to avoid it being expanded immediately by filename generation. It must match the full line, so to match a substring there must be a `<code>*</code>&#8216; at the start and end. The line matched against includes the <code>$TCP_PROMPT</code> added by <code>tcp_read</code>. It is possible to include the globbing flags `<code>#b</code>&#8216; or `<code>#m</code>&#8216; in the patterns to make backreferences available in the parameters <code>$MATCH</code>, <code>$match</code>, etc., as described in the base zsh documentation on pattern matching. </p>
<p> Unlike <code>tcp_read</code>, the default behaviour of <code>tcp_expect</code> is to block indefinitely until the required input is found. This can be modified by specifying a timeout with <code>-t</code> or <code>-T</code>; these function as in <code>tcp_read</code>, specifying a per-read or overall timeout, respectively, in seconds, as an integer or floating-point number. As <code>tcp_read</code>, the function returns status 2 if a timeout occurs. </p>
<p> The function returns as soon as any one of the patterns given match. If the caller needs to know which of the patterns matched, the option <code>-p</code> <i>var</i> can be used; on return, <code>$var</code> is set to the number of the pattern using ordinary zsh indexing, i.e. the first is 1, and so on. Note the absence of a `<code>$</code>&#8216; in front of <i>var</i>. To avoid clashes, the parameter cannot begin with `<code>_expect</code>&#8216;. The index -1 is used if there is a timeout and 0 if there is no match. </p>
<p> The option <code>-P</code> <i>var</i> works similarly to <code>-p</code>, but instead of numerical indexes the regular arguments must begin with a prefix followed by a colon: that prefix is then used as a tag to which <i>var</i> is set when the argument matches. The tag <code>timeout</code> is used if there is a timeout and the empty string if there is no match. Note it is acceptable for different arguments to start with the same prefix if the matches do not need to be distinguished. </p>
<p> The option <code>-q</code> is passed directly down to <code>tcp_read</code>. </p>
<p> As all input is done via <code>tcp_read</code>, all the usual rules about output of lines read apply. One exception is that the parameter <code>$tcp_lines</code> will only reflect the line actually matched by <code>tcp_expect</code>; use <code>$tcp_expect_lines</code> for the full set of lines read during the function call.</dl>
<dt><code>tcp_proxy</code></p>
<dd> This is a simple-minded function to accept a TCP connection and execute a command with I/O redirected to the connection. Extreme caution should be taken as there is no security whatsoever and this can leave your computer open to the world. Ideally, it should only be used behind a firewall.</p>
<dl>
<dt>
<dd>
<p> The first argument is a TCP port on which the function will listen. </p>
<p> The remaining arguments give a command and its arguments to execute with standard input, standard output and standard error redirected to the file descriptor on which the TCP session has been accepted. If no command is given, a new zsh is started. This gives everyone on your network direct access to your account, which in many cases will be a bad thing. </p>
<p> The command is run in the background, so <code>tcp_proxy</code> can then accept new connections. It continues to accept new connections until interrupted.</dl>
<dt><code>tcp_spam</code> [ <code>-ertv</code> ] [ <code>-a</code> | <code>-s</code> <i>sess</i> | <code>-l</code> <i>sess</i>[<code>,</code>&#8230;] ] <i>cmd</i> [ <i>arg</i> &#8230; ]</p>
<dd> Execute `<i>cmd</i> [ <i>arg</i> &#8230; ]&#8217; for each session in turn. Note this executes the command and arguments; it does not send the command line as data unless the <code>-t</code> (transmit) option is given.</p>
<dl>
<dt>
<dd>
<p> The sessions may be selected explicitly with the standard <code>-a</code>, <code>-s</code> or <code>-l</code> options, or may be chosen implicitly. If none of the three options is given the rules are: first, if the array <code>$tcp_spam_list</code> is set, this is taken as the list of sessions, otherwise all sessions are taken. Second, any sessions given in the array <code>$tcp_no_spam_list</code> are removed from the list of sessions. </p>
<p> Normally, any sessions added by the `<code>-a</code>&#8216; flag or when all sessions are chosen implicitly are spammed in alphabetic order; sessions given by the <code>$tcp_spam_list</code> array or on the command line are spammed in the order given. The <code>-r</code> flag reverses the order however it was arrived it. </p>
<p> The <code>-v</code> flag specifies that a <code>$TCP_PROMPT</code> will be output before each session. This is output after any modification to <code>TCP_SESS</code> by the user-defined <code>tcp_on_spam</code> function described below. (Obviously that function is able to generate its own output.) </p>
<p> If the option <code>-e</code> is present, the line given as `<i>cmd</i> [ <i>arg</i> &#8230; ]&#8217; is executed using <code>eval</code>, otherwise it is executed without any further processing.</dl>
<dt><code>tcp_talk</code></p>
<dd> This is a fairly simple-minded attempt to force input to the line editor to go straight to the default <code>TCP_SESS</code>.</p>
<dl>
<dt>
<dd>
<p> An escape string, <code>$TCP_TALK_ESCAPE</code>, default `<code>:</code>&#8216;, is used to allow access to normal shell operation. If it is on its own at the start of the line, or followed only by whitespace, the line editor returns to normal operation. Otherwise, the string and any following whitespace are skipped and the remainder of the line executed as shell input without any change of the line editor&#8217;s operating mode. </p>
<p> The current implementation is somewhat deficient in terms of use of the command history. For this reason, many users will prefer to use some form of alternative approach for sending data easily to the current session. One simple approach is to alias some special character (such as `<code>%</code>&#8216;) to `<code>tcp_command &#8211;</code><code>&#8211;</code>&#8216;.</dl>
<dt><code>tcp_wait</code></p>
<dd> The sole argument is an integer or floating point number which gives the seconds to delay. The shell will do nothing for that period except wait for input on all TCP sessions by calling <code>tcp_read -a</code>. This is similar to the interactive behaviour at the command prompt when zle handlers are installed.</dl>
<h3>`One-shot&#8217; file transfer</h3>
<dl>
<dt>
<dd> <code>tcp_point</code> <i>port</i></p>
<dt>
<dd> <code>tcp_shoot</code> <i>host</i> <i>port</i> This pair of functions provide a simple way to transfer a file between two hosts within the shell. Note, however, that bulk data transfer is currently done using <code>cat</code>. <code>tcp_point</code> reads any data arriving at <i>port</i> and sends it to standard output; <code>tcp_shoot</code> connects to <i>port</i> on <i>host</i> and sends its standard input. Any unused <i>port</i> may be used; the standard mechanism for picking a port is to think of a random four-digit number above 1024 until one works.</p>
<dl>
<dt>
<dd>
<p> To transfer a file from host <code>woodcock</code> to host <code>springes</code>, on <code>springes</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_point 8091 &gt;output_file</code>
</pre>
</dl>
<p> and on <code>woodcock</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_shoot springes 8091 &lt;input_file</code>
</pre>
</dl>
<p> As these two functions do not require <code>tcp_open</code> to set up a TCP connection first, they may need to be autoloaded separately.</dl>
</dl>
<h2>TCP USER-DEFINED FUNCTIONS</h2>
<p> Certain functions, if defined by the user, will be called by the function system in certain contexts. This facility depends on the module <code>zsh/parameter</code>, which is usually available in interactive shells as the completion system depends on it. None of the functions need be defined; they simply provide convenient hooks when necessary. </p>
<p> Typically, these are called after the requested action has been taken, so that the various parameters will reflect the new state. </p>
<dl>
<dt>
<dd> <code>tcp_on_alias</code> <i>alias</i> <i>fd</i> When an alias is defined, this function will be called with two arguments: the name of the alias, and the file descriptor of the corresponding session.</p>
<dt><code>tcp_on_awol</code> <i>sess</i> <i>fd</i></p>
<dd> If the function <code>tcp_fd_handler</code> is handling input from the line editor and detects that the file descriptor is no longer reusable, by default it removes it from the list of file descriptors handled by this method and prints a message. If the function <code>tcp_on_awol</code> is defined it is called immediately before this point. It may return status 100, which indicates that the normal handling should still be performed; any other return status indicates that no further action should be taken and the <code>tcp_fd_handler</code> should return immediately with the given status. Typically the action of <code>tcp_on_awol</code> will be to close the session.</p>
<dl>
<dt>
<dd>
<p> The variable <code>TCP_INVALIDATE_ZLE</code> will be a non-empty string if it is necessary to invalidate the line editor display using `<code>zle -I</code>&#8216; before printing output from the function. </p>
<p> (`AWOL&#8217; is military jargon for `absent without leave&#8217; or some variation. It has no pre-existing technical meaning known to the author.)</dl>
<dt><code>tcp_on_close</code> <i>sess</i> <i>fd</i></p>
<dd> This is called with the name of a session being closed and the file descriptor which corresponded to that session. Both will be invalid by the time the function is called.</p>
<dt><code>tcp_on_open</code> <i>sess</i> <i>fd</i></p>
<dd> This is called after a new session has been defined with the session name and file descriptor as arguments. If it returns a non-zero status, opening the session is assumed to fail and the session is closed again; however, <code>tcp_open</code> will continue to attempt to open any remaining sessions given on the command line.</p>
<dt><code>tcp_on_rename</code> <i>oldsess</i> <i>fd</i> <i>newsess</i></p>
<dd> This is called after a session has been renamed with the three arguments old session name, file descriptor, new session name.</p>
<dt><code>tcp_on_spam</code> <i>sess</i> <i>command &#8230;</i></p>
<dd> This is called once for each session spammed, just <i>before</i> a command is executed for a session by <code>tcp_spam</code>. The arguments are the session name followed by the command list to be executed. If <code>tcp_spam</code> was called with the option <code>-t</code>, the first command will be <code>tcp_send</code>.</p>
<dl>
<dt>
<dd>
<p> This function is called after <code>$TCP_SESS</code> is set to reflect the session to be spammed, but before any use of it is made. Hence it is possible to alter the value of <code>$TCP_SESS</code> within this function. For example, the session arguments to <code>tcp_spam</code> could include extra information to be stripped off and processed in <code>tcp_on_spam</code>. </p>
<p> If the function sets the parameter <code>$REPLY</code> to `<code>done</code>&#8216;, the command line is not executed; in addition, no prompt is printed for the <code>-v</code> option to <code>tcp_spam</code>.</dl>
<dt><code>tcp_on_unalias</code> <i>alias</i> <i>fd</i></p>
<dd> This is called with the name of an alias and the corresponding session&#8217;s file descriptor after an alias has been deleted.</dl>
<h2>TCP UTILITY FUNCTIONS</h2>
<p> The following functions are used by the TCP function system but will rarely if ever need to be called directly. </p>
<dl>
<dt>
<dd> <code>tcp_fd_handler</code> This is the function installed by <code>tcp_open</code> for handling input from within the line editor, if that is required. It is in the format documented for the builtin `<code>zle -F</code>&#8216; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1) .</p>
<dl>
<dt>
<dd>
<p> While active, the function sets the parameter <code>TCP_HANDLER_ACTIVE</code> to 1. This allows shell code called internally (for example, by setting <code>tcp_on_read</code>) to tell if is being called when the shell is otherwise idle at the editor prompt.</dl>
<dt><code>tcp_output</code> [ <code>-q</code> ] <code>-P</code> <i>prompt</i> <code>-F</code> <i>fd</i> <code>-S</code> <i>sess</i></p>
<dd> This function is used for both logging and handling output to standard output, from within <code>tcp_read</code> and (if <code>$TCP_OUTPUT</code> is set) <code>tcp_send</code>.</p>
<dl>
<dt>
<dd>
<p> The <i>prompt</i> to use is specified by <code>-P</code>; the default is the empty string. It can contain:</p>
<dl>
<dt>
<dd> <code>%c</code> Expands to 1 if the session is the current session, otherwise 0. Used with ternary expressions such as `<code>%(c.-.+)</code>&#8216; to output `<code>+</code>&#8216; for the current session and `<code>&#8211;</code>&#8216; otherwise.</p>
<dt><code>%f</code></p>
<dd> Replaced by the session&#8217;s file descriptor.</p>
<dt><code>%s</code></p>
<dd> Replaced by the session name.</p>
<dt><code>%%</code></p>
<dd> Replaced by a single `<code>%</code>&#8216;.</dl>
<p> The option <code>-q</code> suppresses output to standard output, but not to any log files which are configured. </p>
<p> The <code>-S</code> and <code>-F</code> options are used to pass in the session name and file descriptor for possible replacement in the prompt.</dl>
</dl>
<h2>TCP USER PARAMETERS</h2>
<p> Parameters follow the usual convention that uppercase is used for scalars and integers, while lowercase is used for normal and associative array. It is always safe for user code to read these parameters. Some parameters may also be set; these are noted explicitly. Others are included in this group as they are set by the function system for the user&#8217;s benefit, i.e. setting them is typically not useful but is benign. </p>
<p> It is often also useful to make settable parameters local to a function. For example, `<code>local TCP_SILENT=1</code>&#8216; specifies that data read during the function call will not be printed to standard output, regardless of the setting outside the function. Likewise, `<code>local TCP_SESS=</code><i>sess</i>&#8216; sets a session for the duration of a function, and `<code>local TCP_PROMPT=</code>&#8216; specifies that no prompt is used for input during the function. </p>
<dl>
<dt>
<dd> <code>tcp_expect_lines</code> Array. The set of lines read during the last call to <code>tcp_expect</code>, including the last (<code>$TCP_LINE</code>).</p>
<dt><code>tcp_filter</code></p>
<dd> Array. May be set directly. A set of extended globbing patterns which, if matched in <code>tcp_output</code>, will cause the line not to be printed to standard output. The patterns should be defined as described for the arguments to <code>tcp_expect</code>. Output of line to log files is not affected.</p>
<dt><code>TCP_HANDLER_ACTIVE</code></p>
<dd> Scalar. Set to 1 within <code>tcp_fd_handler</code> to indicate to functions called recursively that they have been called during an editor session. Otherwise unset.</p>
<dt><code>TCP_LINE</code></p>
<dd> The last line read by <code>tcp_read</code>, and hence also <code>tcp_expect</code>.</p>
<dt><code>TCP_LINE_FD</code></p>
<dd> The file descriptor from which <code>$TCP_LINE</code> was read. <code>${tcp_by_fd[$TCP_LINE_FD]}</code> will give the corresponding session name.</p>
<dt><code>tcp_lines</code></p>
<dd> Array. The set of lines read during the last call to <code>tcp_read</code>, including the last (<code>$TCP_LINE</code>).</p>
<dt><code>TCP_LOG</code></p>
<dd> May be set directly, although it is also controlled by <code>tcp_log</code>. The name of a file to which output from all sessions will be sent. The output is proceeded by the usual <code>$TCP_PROMPT</code>. If it is not an absolute path name, it will follow the user&#8217;s current directory.</p>
<dt><code>TCP_LOG_SESS</code></p>
<dd> May be set directly, although it is also controlled by <code>tcp_log</code>. The prefix for a set of files to which output from each session separately will be sent; the full filename is <code>${TCP_LOG_SESS}.</code><i>sess</i>. Output to each file is raw; no prompt is added. If it is not an absolute path name, it will follow the user&#8217;s current directory.</p>
<dt><code>tcp_no_spam_list</code></p>
<dd> Array. May be set directly. See <code>tcp_spam</code> for how this is used.</p>
<dt><code>TCP_OUTPUT</code></p>
<dd> May be set directly. If a non-empty string, any data sent to a session by <code>tcp_send</code> will be logged. This parameter gives the prompt to be used in a file specified by <code>$TCP_LOG</code> but not in a file generated from <code>$TCP_LOG_SESS</code>. The prompt string has the same format as <code>TCP_PROMPT</code> and the same rules for its use apply.</p>
<dt><code>TCP_PROMPT</code></p>
<dd> May be set directly. Used as the prefix for data read by <code>tcp_read</code> which is printed to standard output or to the log file given by <code>$TCP_LOG</code>, if any. Any `<code>%s</code>&#8216;, `<code>%f</code>&#8216; or `<code>%%</code>&#8216; occurring in the string will be replaced by the name of the session, the session&#8217;s underlying file descriptor, or a single `<code>%</code>&#8216;, respectively. The expression `<code>%c</code>&#8216; expands to 1 if the session being read is the current session, else 0; this is most useful in ternary expressions such as `<code>%(c.-.+)</code>&#8216; which outputs `<code>+</code>&#8216; if the session is the current one, else `<code>&#8211;</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> If the prompt starts with <code>%P</code>, this is stripped and the complete result of the previous stage is passed through standard prompt <code>%</code>-style formatting before being output.</dl>
<dt><code>TCP_READ_DEBUG</code></p>
<dd> May be set directly. If this has non-zero length, <code>tcp_read</code> will give some limited diagnostics about data being read.</p>
<dt><code>TCP_SECONDS_START</code></p>
<dd> This value is created and initialised to zero by tcp_open.</p>
<dl>
<dt>
<dd>
<p> The functions <code>tcp_read</code> and <code>tcp_expect</code> use the shell&#8217;s <code>SECONDS</code> parameter for their own timing purposes. If that parameter is not of floating point type on entry to one of the functions, it will create a local parameter <code>SECONDS</code> which is floating point and set the parameter <code>TCP_SECONDS_START</code> to the previous value of <code>$SECONDS</code>. If the parameter is already floating point, it is used without a local copy being created and <code>TCP_SECONDS_START</code> is not set. As the global value is zero, the shell elapsed time is guaranteed to be the sum of <code>$SECONDS</code> and <code>$TCP_SECONDS_START</code>. </p>
<p> This can be avoided by setting <code>SECONDS</code> globally to a floating point value using `<code>typeset -F SECONDS</code>&#8216;; then the TCP functions will never make a local copy and never set <code>TCP_SECONDS_START</code> to a non-zero value.</dl>
<dt><code>TCP_SESS</code></p>
<dd> May be set directly. The current session; must refer to one of the sessions established by <code>tcp_open</code>.</p>
<dt><code>TCP_SILENT</code></p>
<dd> May be set directly, although it is also controlled by <code>tcp_log</code>. If of non-zero length, data read by <code>tcp_read</code> will not be written to standard output, though may still be written to a log file.</p>
<dt><code>tcp_spam_list</code></p>
<dd> Array. May be set directly. See the description of the function <code>tcp_spam</code> for how this is used.</p>
<dt><code>TCP_TALK_ESCAPE</code></p>
<dd> May be set directly. See the description of the function <code>tcp_talk</code> for how this is used.</p>
<dt><code>TCP_TIMEOUT</code></p>
<dd> May be set directly. Currently this is only used by the function <code>tcp_command</code>, see above.</dl>
<h2>TCP USER-DEFINED PARAMETERS</h2>
<p> The following parameters are not set by the function system, but have a special effect if set by the user. </p>
<dl>
<dt>
<dd> <code>tcp_on_read</code> This should be an associative array; if it is not, the behaviour is undefined. Each key is the name of a shell function or other command, and the corresponding value is a shell pattern (using <code>EXTENDED_GLOB</code>). Every line read from a TCP session directly or indirectly using <code>tcp_read</code> (which includes lines read by <code>tcp_expect</code>) is compared against the pattern. If the line matches, the command given in the key is called with two arguments: the name of the session from which the line was read, and the line itself.</p>
<dl>
<dt>
<dd>
<p> If any function called to handle a line returns a non-zero status, the line is not output. Thus a <code>tcp_on_read</code> handler containing only the instruction `<code>return 1</code>&#8216; can be used to suppress output of particular lines (see, however, <code>tcp_filter</code> above). However, the line is still stored in <code>TCP_LINE</code> and <code>tcp_lines</code>; this occurs after all <code>tcp_on_read</code> processing.</dl>
</dl>
<h2>TCP UTILITY PARAMETERS</h2>
<p> These parameters are controlled by the function system; they may be read directly, but should not usually be set by user code. </p>
<dl>
<dt>
<dd> <code>tcp_aliases</code> Associative array. The keys are the names of sessions established with <code>tcp_open</code>; each value is a space-separated list of aliases which refer to that session.</p>
<dt><code>tcp_by_fd</code></p>
<dd> Associative array. The keys are session file descriptors; each value is the name of that session.</p>
<dt><code>tcp_by_name</code></p>
<dd> Associative array. The keys are the names of sessions; each value is the file descriptor associated with that session.</dl>
<h2>TCP EXAMPLES</h2>
<p> Here is a trivial example using a remote calculator. </p>
<p> To create a calculator server on port 7337 (see the <code>dc</code> manual page for quite how infuriating the underlying command is): </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_proxy 7337 dc</code>
</pre>
</dl>
<p> To connect to this from the same host with a session also named `<code>dc</code>&#8216;: </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_open localhost 7337 dc</code>
</pre>
</dl>
<p> To send a command to the remote session and wait a short while for output (assuming <code>dc</code> is the current session): </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_command 2 4 + p</code>
</pre>
</dl>
<p> To close the session: </p>
<dl>
<dt>
<dd>
<pre>
<code>tcp_close</code>
</pre>
</dl>
<p> The <code>tcp_proxy</code> needs to be killed to be stopped. Note this will not usually kill any connections which have already been accepted, and also that the port is not immediately available for reuse. </p>
<p> The following chunk of code puts a list of sessions into an xterm header, with the current session followed by a star. </p>
<dl>
<dt>
<dd>
<pre><code>
print - n "]2;TCP:" $
{
    (k) tcp_by_name : / $TCP_SESS / $TCP_SESS\*
}
""
</code></pre>
</dl>
<h2>TCP BUGS</h2>
<p> The function <code>tcp_read</code> uses the shell&#8217;s normal <code>read</code> builtin. As this reads a complete line at once, data arriving without a terminating newline can cause the function to block indefinitely. </p>
<p> Though the function suite works well for interactive use and for data arriving in small amounts, the performance when large amounts of data are being exchanged is likely to be extremely poor. </p>
<h2>Index</h2>
