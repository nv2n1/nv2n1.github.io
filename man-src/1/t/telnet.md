---
title: "telnet(1)"
name: "telnet"
section: "1"
letter: "t"
url: "/docs/linux/man/1-telnet/"
description: "telnet – user interface to the TELNET protocol"
---

<p>Linux NetKit (0.17)</p>
<h2 class="name">NAME</h2>
<p> <code>telnet</code> &#8211; user interface to the <code>TELNET</code> protocol </p>
<h2>SYNOPSIS</h2>
<p> <code>telnet</code> [-<code>468ELadr</code> ] [-<code>S </code><i>tos</i> ] [-<code>b </code><i>address</i> ] [-<code>e </code><i>escapechar</i> ] [-<code>l </code><i>user</i> ] [-<code>n </code><i>tracefile</i> ] [<i>host</i> [<i>port</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>telnet</code> command is used for interactive communication with another host using the <code>TELNET</code> protocol. It begins in command mode, where it prints a telnet prompt (&quot;telnet&gt; &quot;). If <code>telnet</code> is invoked with a <i>host</i> argument, it performs an <code>open</code> command implicitly; see the description below. </p>
<p> Options:</p>
<dl>
<dt><code>-4</code></p>
<dd> Force IPv4 address resolution.</p>
<dt><code>-6</code></p>
<dd> Force IPv6 address resolution.</p>
<dt><code>-8</code></p>
<dd> Request 8-bit operation. This causes an attempt to negotiate the <code>TELNET BINARY</code> option for both input and output. By default telnet is not 8-bit clean.</p>
<dt><code>-E</code></p>
<dd> Disables the escape character functionality; that is, sets the escape character to &#8220;no character&#8221;.</p>
<dt><code>-L</code></p>
<dd> Specifies an 8-bit data path on output. This causes the <code>TELNET BINARY </code> option to be negotiated on just output.</p>
<dt><code>-a</code></p>
<dd> Attempt automatic login. Currently, this sends the user name via the <code>USER</code> variable of the <code>NEW-ENVIRON</code> option if supported by the remote system. The username is retrieved via <a href="/docs/linux/man/3-getlogin/">getlogin</a>(3).</p>
<dt><code>-b </code><i>address</i></p>
<dd> Use <a href="/docs/linux/man/2-bind/">bind</a>(2) on the local socket to bind it to a specific local address.</p>
<dt><code>-d</code></p>
<dd> Sets the initial value of the <code>debug</code> toggle to <code>TRUE.</code></p>
<dt><code>-r</code></p>
<dd> Emulate <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1). In this mode, the default escape character is a tilde. Also, the interpretation of the escape character is changed: an escape character followed by a dot causes <code>telnet </code> to disconnect from the remote host. A ^Z instead of a dot suspends <code>telnet</code> and a ^] (the default <code>telnet</code> escape character) generates a normal telnet prompt. These codes are accepted only at the beginning of a line.</p>
<dt><code>-S </code><i>tos</i></p>
<dd> Sets the IP type-of-service (TOS) option for the telnet connection to the value <i>tos</i></p>
<dt><code>-e </code><i>escapechar</i></p>
<dd> Sets the escape character to <i>escapechar.</i> If no character is supplied, no escape character will be used. Entering the escape character while connected causes telnet to drop to command mode.</p>
<dt><code>-l </code><i>user</i></p>
<dd> Specify <i>user</i> as the user to log in as on the remote system. This is accomplished by sending the specified name as the <code>USER</code> environment variable, so it requires that the remote system support the <code>TELNET NEW-ENVIRON</code> option. This option implies the &#8211;<code>a</code> option, and may also be used with the <code>open</code> command.</p>
<dt><code>-n </code><i>tracefile</i></p>
<dd> Opens <i>tracefile</i> for recording trace information. See the <code>set tracefile</code> command below.</p>
<dt><i>host</i></p>
<dd> Specifies a host to contact over the network.</p>
<dt><i>port</i></p>
<dd> Specifies a port number or service name to contact. If not specified, the <code>telnet</code> port (23) is used.</dl>
<p> Protocol: </p>
<p> Once a connection has been opened, <code>telnet</code> will attempt to enable the <code>TELNET LINEMODE</code> option. If this fails, then <code>telnet</code> will revert to one of two input modes: either &ldquo;character at a time&rdquo; or &ldquo;old line by line&rdquo; depending on what the remote system supports. </p>
<p> When <code>LINEMODE</code> is enabled, character processing is done on the local system, under the control of the remote system. When input editing or character echoing is to be disabled, the remote system will relay that information. The remote system will also relay changes to any special characters that happen on the remote system, so that they can take effect on the local system. </p>
<p> In &ldquo;character at a time&rdquo; mode, most text typed is immediately sent to the remote host for processing. </p>
<p> In &ldquo;old line by line&rdquo; mode, all text is echoed locally, and (normally) only completed lines are sent to the remote host. The &ldquo;local echo character&rdquo; (initially &ldquo;^E&rdquo;) may be used to turn off and on the local echo (this would mostly be used to enter passwords without the password being echoed). </p>
<p> If the <code>LINEMODE</code> option is enabled, or if the <code>localchars</code> toggle is <code>TRUE</code> (the default for &ldquo;old line by line&ldquo;; see below), the user&#8217;s <code>quit </code> <code>intr</code> and <code>flush</code> characters are trapped locally, and sent as <code>TELNET</code> protocol sequences to the remote side. If <code>LINEMODE</code> has ever been enabled, then the user&#8217;s <code>susp</code> and <code>eof</code> are also sent as <code>TELNET</code> protocol sequences, and <code>quit</code> is sent as a <code>TELNET ABORT</code> instead of <code>BREAK</code> There are options (see <code>toggle</code> <code>autoflush</code> and <code>toggle</code> <code>autosynch</code> below) which cause this action to flush subsequent output to the terminal (until the remote host acknowledges the <code>TELNET</code> sequence) and flush previous terminal input (in the case of <code>quit</code> and <code>intr )</code> </p>
<p> Commands: </p>
<p> The following <code>telnet</code> commands are available. Unique prefixes are understood as abbreviations. </p>
<dl>
<dt><code>auth </code><i>argument &#8230; </i></p>
<dd> The <code>auth</code> command controls the <code>TELNET AUTHENTICATE</code> protocol option. If <code>telnet</code> was compiled without authentication, the <code>auth</code> command will not be supported. Valid arguments are as follows:</p>
<dl>
<dt><code>disable </code><i>type</i></p>
<dd> Disable the specified type of authentication. To obtain a list of available types, use the <code>auth disable ?</code> command.</p>
<dt><code>enable </code><i>type</i></p>
<dd> Enable the specified type of authentication. To obtain a list of available types, use the <code>auth enable ?</code> command.</p>
<dt><code>status</code></p>
<dd> List the current status of the various types of authentication.</dl>
<p> Note that the current version of <code>telnet</code> does not support authentication.</p>
<dt><code>close</code></p>
<dd> Close the connection to the remote host, if any, and return to command mode.</p>
<dt><code>display </code><i>argument &#8230; </i></p>
<dd> Display all, or some, of the <code>set</code> and <code>toggle</code> values (see below).</p>
<dt><code>encrypt </code><i>argument &#8230;</i></p>
<dd> The encrypt command controls the <code>TELNET ENCRYPT</code> protocol option. If <code>telnet</code> was compiled without encryption, the <code>encrypt</code> command will not be supported. </p>
<p> Valid arguments are as follows:</p>
<dl>
<dt><code>disable </code><i>type </i><code>[input|output]</code></p>
<dd> Disable the specified type of encryption. If you do not specify input or output, encryption of both is disabled. To obtain a list of available types, use &#8220;encrypt disable ?&#8221;.</p>
<dt><code>enable </code><i>type </i><code>[input|output]</code></p>
<dd> Enable the specified type of encryption. If you do not specify input or output, encryption of both is enabled. To obtain a list of available types, use &#8220;encrypt enable ?&#8221;.</p>
<dt><code>input</code></p>
<dd> This is the same as &#8220;encrypt start input&#8221;.</p>
<dt><code>-input</code></p>
<dd> This is the same as &#8220;encrypt stop input&#8221;.</p>
<dt><code>output</code></p>
<dd> This is the same as &#8220;encrypt start output&#8221;.</p>
<dt><code>-output</code></p>
<dd> This is the same as &#8220;encrypt stop output&#8221;.</p>
<dt><code>start [input|output]</code></p>
<dd> Attempt to begin encrypting. If you do not specify input or output, encryption of both input and output is started.</p>
<dt><code>status</code></p>
<dd> Display the current status of the encryption module.</p>
<dt><code>stop [input|output]</code></p>
<dd> Stop encrypting. If you do not specify input or output, encryption of both is stopped.</p>
<dt><code>type </code><i>type</i></p>
<dd> Sets the default type of encryption to be used with later &#8220;encrypt start&#8221; or &#8220;encrypt stop&#8221; commands.</dl>
<p> Note that the current version of <code>telnet</code> does not support encryption.</p>
<dt><code>environ </code><i>arguments&#8230; </i></p>
<dd> The <code>environ</code> command is used to propagate environment variables across the <code>telnet</code> link using the <code>TELNET NEW-ENVIRON</code> protocol option. All variables exported from the shell are defined, but only the <code>DISPLAY</code> and <code>PRINTER</code> variables are marked to be sent by default. The <code>USER</code> variable is marked to be sent if the &#8211;<code>a</code> or &#8211;<code>l</code> command-line options were used. </p>
<p> Valid arguments for the <code>environ</code> command are:</p>
<dl>
<dt><code>define </code><i>variable value </i></p>
<dd> Define the variable <i>variable</i> to have a value of <i>value.</i> Any variables defined by this command are automatically marked for propagation (&#8220;exported&#8221;). The <i>value</i> may be enclosed in single or double quotes so that tabs and spaces may be included.</p>
<dt><code>undefine </code><i>variable </i></p>
<dd> Remove any existing definition of <i>variable</i></p>
<dt><code>export </code><i>variable </i></p>
<dd> Mark the specified variable for propagation to the remote host.</p>
<dt><code>unexport </code><i>variable </i></p>
<dd> Do not mark the specified variable for propagation to the remote host. The remote host may still ask explicitly for variables that are not exported.</p>
<dt><code>list</code></p>
<dd> List the current set of environment variables. Those marked with a <code>*</code> will be propagated to the remote host. The remote host may still ask explicitly for the rest.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>environ</code> command.</dl>
<dt><code>logout</code></p>
<dd> Send the <code>TELNET LOGOUT</code> protocol option to the remote host. This command is similar to a <code>close</code> command. If the remote host does not support the <code>LOGOUT</code> option, nothing happens. But if it does, this command should cause it to close the connection. If the remote side also supports the concept of suspending a user&#8217;s session for later reattachment, the logout command indicates that the session should be terminated immediately.</p>
<dt><code>mode </code><i>type </i></p>
<dd> <i>Type</i> is one of several options, depending on the state of the session. <code>Telnet</code> asks the remote host to go into the requested mode. If the remote host says it can, that mode takes effect.</p>
<dl>
<dt><code>character</code></p>
<dd> Disable the <code>TELNET LINEMODE</code> option, or, if the remote side does not understand the <code>LINEMODE</code> option, then enter &ldquo;character at a time&ldquo; mode.</p>
<dt><code>line</code></p>
<dd> Enable the <code>TELNET LINEMODE</code> option, or, if the remote side does not understand the <code>LINEMODE</code> option, then attempt to enter &ldquo;old-line-by-line&ldquo; mode.</p>
<dt><code>isig (-isig </code> )</p>
<dd> Attempt to enable (disable) the <code>TRAPSIG</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>edit (-edit </code> )</p>
<dd> Attempt to enable (disable) the <code>EDIT</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>softtabs (-softtabs </code> )</p>
<dd> Attempt to enable (disable) the <code>SOFT_TAB</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>litecho (-litecho </code> )</p>
<dd> Attempt to enable (disable) the <code>LIT_ECHO</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>mode</code> command.</dl>
<dt> <code>open </code><i>host</i> [[-<code>l</code> ] <i>user</i> [- ] <i>port </i>]</p>
<dd>
<dd>Open a connection to the named host. If no port number is specified, <code>telnet</code> will attempt to contact a <code>telnet</code> daemon at the standard port (23). The host specification may be a host name or IP address. The &#8211;<code>l</code> option may be used to specify a user name to be passed to the remote system, like the &#8211;<code>l</code> command-line option. </p>
<p> When connecting to ports other than the <code>telnet</code> port, <code>telnet</code> does not attempt <code>telnet</code> protocol negotiations. This makes it possible to connect to services that do not support the <code>telnet</code> protocol without making a mess. Protocol negotiation can be forced by placing a dash before the port number. </p>
<p> After establishing a connection, any commands associated with the remote host in /etc/telnetrc and the user&#8217;s .telnetrc file are executed, in that order. </p>
<p> The format of the telnetrc files is as follows: Lines beginning with a #, and blank lines, are ignored. The rest of the file should consist of hostnames and sequences of <code>telnet</code> commands to use with that host. Commands should be one per line, indented by whitespace; lines beginning without whitespace are interpreted as hostnames. Lines beginning with the special hostname `DEFAULT&#8217; will apply to all hosts. Hostnames including `DEFAULT&#8217; may be followed immediately by a colon and a port number or string. If a port is specified it must match exactly with what is specified on the command line. If no port was specified on the command line, then the value `telnet&#8217; is used. Upon connecting to a particular host, the commands associated with that host are executed.</p>
<dt><code>quit</code></p>
<dd> Close any open session and exit <code>telnet</code> An end of file condition on input, when in command mode, will trigger this operation as well.</p>
<dt><code>send </code><i>arguments </i></p>
<dd> Send one or more special <code>telnet</code> protocol character sequences to the remote host. The following are the codes which may be specified (more than one may be used in one command): </p>
<dl>
<dt><code>abort</code></p>
<dd> Sends the <code>TELNET ABORT</code> (Abort Processes) sequence.</p>
<dt><code>ao</code></p>
<dd> Sends the <code>TELNET AO</code> (Abort Output) sequence, which should cause the remote system to flush all output <i>from</i> the remote system <i>to</i> the user&#8217;s terminal.</p>
<dt><code>ayt</code></p>
<dd> Sends the <code>TELNET AYT</code> (Are You There?) sequence, to which the remote system may or may not choose to respond.</p>
<dt><code>brk</code></p>
<dd> Sends the <code>TELNET BRK</code> (Break) sequence, which may have significance to the remote system.</p>
<dt><code>ec</code></p>
<dd> Sends the <code>TELNET EC</code> (Erase Character) sequence, which should cause the remote system to erase the last character entered.</p>
<dt><code>el</code></p>
<dd> Sends the <code>TELNET EL</code> (Erase Line) sequence, which should cause the remote system to erase the line currently being entered.</p>
<dt><code>eof</code></p>
<dd> Sends the <code>TELNET EOF</code> (End Of File) sequence.</p>
<dt><code>eor</code></p>
<dd> Sends the <code>TELNET EOR</code> (End of Record) sequence.</p>
<dt><code>escape</code></p>
<dd> Sends the current <code>telnet</code> escape character.</p>
<dt><code>ga</code></p>
<dd> Sends the <code>TELNET GA</code> (Go Ahead) sequence, which likely has no significance to the remote system.</p>
<dt><code>getstatus</code></p>
<dd> If the remote side supports the <code>TELNET STATUS</code> command, <code>getstatus</code> will send the subnegotiation to request that the server send its current option status.</p>
<dt><code>ip</code></p>
<dd> Sends the <code>TELNET IP</code> (Interrupt Process) sequence, which should cause the remote system to abort the currently running process.</p>
<dt><code>nop</code></p>
<dd> Sends the <code>TELNET NOP</code> (No Operation) sequence.</p>
<dt><code>susp</code></p>
<dd> Sends the <code>TELNET SUSP</code> (Suspend Process) sequence.</p>
<dt><code>synch</code></p>
<dd> Sends the <code>TELNET SYNCH</code> sequence. This sequence causes the remote system to discard all previously typed (but not yet read) input. This sequence is sent as <code>TCP</code> urgent data (and may not work if the remote system is a BSD 4.2 system &#8212; if it doesn&#8217;t work, a lower case &ldquo;r&rdquo; may be echoed on the terminal).</p>
<dt><code>do </code><i>cmd</i></p>
<dd>
<dt><code>dont </code><i>cmd</i></p>
<dd>
<dt><code>will </code><i>cmd</i></p>
<dd>
<dt><code>wont </code><i>cmd</i></p>
<dd> Sends the <code>TELNET DO</code> <i>cmd</i> sequence. <i>cmd</i> can be either a decimal number between 0 and 255, or a symbolic name for a specific <code>TELNET</code> command. <i>cmd</i> can also be either <code>help</code> or <code>?</code> to print out help information, including a list of known symbolic names.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>send</code> command.</dl>
<dt><code>set </code><i>argument value </i></p>
<dd>
<dt><code>unset </code><i>argument value </i></p>
<dd> The <code>set</code> command will set any one of a number of <code>telnet</code> variables to a specific value or to <code>TRUE</code> The special value <code>off</code> turns off the function associated with the variable. This is equivalent to using the <code>unset</code> command. The <code>unset</code> command will disable or set to <code>FALSE</code> any of the specified variables. The values of variables may be interrogated with the <code>display</code> command. The variables which may be set or unset, but not toggled, are listed here. In addition, any of the variables for the <code>toggle</code> command may be explicitly set or unset.</p>
<dl>
<dt><code>ayt</code></p>
<dd> If <code>telnet</code> is in localchars mode, or <code>LINEMODE</code> is enabled, and the status character is typed, a <code>TELNET AYT</code> sequence is sent to the remote host. The initial value for the &quot;Are You There&quot; character is the terminal&#8217;s status character.</p>
<dt><code>echo</code></p>
<dd> This is the value (initially &ldquo;^E&rdquo;) which, when in &ldquo;line by line&rdquo; mode, toggles between doing local echoing of entered characters (for normal processing), and suppressing echoing of entered characters (for entering, say, a password).</p>
<dt><code>eof</code></p>
<dd> If <code>telnet</code> is operating in <code>LINEMODE</code> or &ldquo;old line by line&rdquo; mode, entering this character as the first character on a line will cause this character to be sent to the remote system. The initial value of the eof character is taken to be the terminal&#8217;s <code>eof</code> character.</p>
<dt><code>erase</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below), <code>and</code> if <code>telnet</code> is operating in &ldquo;character at a time&rdquo; mode, then when this character is typed, a <code>TELNET EC</code> sequence (see <code>send</code> <code>ec</code> above) is sent to the remote system. The initial value for the erase character is taken to be the terminal&#8217;s <code>erase</code> character.</p>
<dt><code>escape</code></p>
<dd> This is the <code>telnet</code> escape character (initially &ldquo;^]&rdquo;) which causes entry into <code>telnet</code> command mode (when connected to a remote system).</p>
<dt><code>flushoutput</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below) and the <code>flushoutput</code> character is typed, a <code>TELNET AO</code> sequence (see <code>send</code> <code>ao</code> above) is sent to the remote host. The initial value for the flush character is taken to be the terminal&#8217;s <code>flush</code> character.</p>
<dt><code>forw1</code></p>
<dd>
<dt><code>forw2</code></p>
<dd> If <code>TELNET</code> is operating in <code>LINEMODE</code> these are the characters that, when typed, cause partial lines to be forwarded to the remote system. The initial value for the forwarding characters are taken from the terminal&#8217;s eol and eol2 characters.</p>
<dt><code>interrupt</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below) and the <code>interrupt</code> character is typed, a <code>TELNET IP</code> sequence (see <code>send</code> <code>ip</code> above) is sent to the remote host. The initial value for the interrupt character is taken to be the terminal&#8217;s <code>intr</code> character.</p>
<dt><code>kill</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below), <code>and</code> if <code>telnet</code> is operating in &ldquo;character at a time&rdquo; mode, then when this character is typed, a <code>TELNET EL</code> sequence (see <code>send</code> <code>el</code> above) is sent to the remote system. The initial value for the kill character is taken to be the terminal&#8217;s <code>kill</code> character.</p>
<dt><code>lnext</code></p>
<dd> If <code>telnet</code> is operating in <code>LINEMODE</code> or &ldquo;old line by line&ldquo; mode, then this character is taken to be the terminal&#8217;s <code>lnext</code> character. The initial value for the lnext character is taken to be the terminal&#8217;s <code>lnext</code> character.</p>
<dt><code>quit</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below) and the <code>quit</code> character is typed, a <code>TELNET BRK</code> sequence (see <code>send</code> <code>brk</code> above) is sent to the remote host. The initial value for the quit character is taken to be the terminal&#8217;s <code>quit</code> character.</p>
<dt><code>reprint</code></p>
<dd> If <code>telnet</code> is operating in <code>LINEMODE</code> or &ldquo;old line by line&ldquo; mode, then this character is taken to be the terminal&#8217;s <code>reprint</code> character. The initial value for the reprint character is taken to be the terminal&#8217;s <code>reprint</code> character.</p>
<dt><code>rlogin</code></p>
<dd> This is the rlogin mode escape character. Setting it enables rlogin mode, as with the <i>r</i> command-line option (q.v.)</p>
<dt><code>start</code></p>
<dd> If the <code>TELNET TOGGLE-FLOW-CONTROL</code> option has been enabled, then this character is taken to be the terminal&#8217;s <code>start</code> character. The initial value for the kill character is taken to be the terminal&#8217;s <code>start</code> character.</p>
<dt><code>stop</code></p>
<dd> If the <code>TELNET TOGGLE-FLOW-CONTROL</code> option has been enabled, then this character is taken to be the terminal&#8217;s <code>stop</code> character. The initial value for the kill character is taken to be the terminal&#8217;s <code>stop</code> character.</p>
<dt><code>susp</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode, or <code>LINEMODE</code> is enabled, and the <code>suspend</code> character is typed, a <code>TELNET SUSP</code> sequence (see <code>send</code> <code>susp</code> above) is sent to the remote host. The initial value for the suspend character is taken to be the terminal&#8217;s <code>suspend</code> character.</p>
<dt><code>tracefile</code></p>
<dd> This is the file to which the output, caused by <code>netdata</code> or <code>option</code> tracing being <code>TRUE</code> will be written. If it is set to &#8220;- &#8221; then tracing information will be written to standard output (the default).</p>
<dt><code>worderase</code></p>
<dd> If <code>telnet</code> is operating in <code>LINEMODE</code> or &ldquo;old line by line&ldquo; mode, then this character is taken to be the terminal&#8217;s <code>worderase</code> character. The initial value for the worderase character is taken to be the terminal&#8217;s <code>worderase</code> character.</p>
<dt><code>?</code></p>
<dd> Displays the legal <code>set</code> (<code>unset</code> ) commands.</dl>
<dt><code>slc </code><i>state </i></p>
<dd> The <code>slc</code> command (Set Local Characters) is used to set or change the state of the the special characters when the <code>TELNET LINEMODE</code> option has been enabled. Special characters are characters that get mapped to <code>TELNET</code> commands sequences (like <code>ip</code> or <code>quit </code> or line editing characters (like <code>erase</code> and <code>kill )</code> By default, the local special characters are exported.</p>
<dl>
<dt><code>check</code></p>
<dd> Verify the current settings for the current special characters. The remote side is requested to send all the current special character settings, and if there are any discrepancies with the local side, the local side will switch to the remote value.</p>
<dt><code>export</code></p>
<dd> Switch to the local defaults for the special characters. The local default characters are those of the local terminal at the time when <code>telnet</code> was started.</p>
<dt><code>import</code></p>
<dd> Switch to the remote defaults for the special characters. The remote default characters are those of the remote system at the time when the <code>TELNET</code> connection was established.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>slc</code> command.</dl>
<dt><code>status</code></p>
<dd> Show the current status of <code>telnet</code> This includes the name of the remote host, if any, as well as the current mode.</p>
<dt><code>toggle </code><i>arguments &#8230; </i></p>
<dd> Toggle (between <code>TRUE</code> and <code>FALSE</code> various flags that control how <code>telnet</code> responds to events. These flags may be set explicitly to <code>TRUE</code> or <code>FALSE</code> using the <code>set</code> and <code>unset</code> commands. More than one flag may be toggled at once. The state of these flags may be examined with the <code>display</code> command. Valid flags are:</p>
<dl>
<dt><code>authdebug</code></p>
<dd> Turns on debugging for the authentication code. This flag only exists if authentication support is enabled.</p>
<dt><code>autoflush</code></p>
<dd> If <code>autoflush</code> and <code>localchars</code> are both <code>TRUE</code> then when the <code>ao </code> or <code>quit</code> characters are recognized (and transformed into <code>TELNET</code> sequences; see <code>set</code> above for details), <code>telnet</code> refuses to display any data on the user&#8217;s terminal until the remote system acknowledges (via a <code>TELNET TIMING MARK</code> option) that it has processed those <code>TELNET</code> sequences. The initial value for this toggle is <code>TRUE</code> if the terminal user had not done an &quot;stty noflsh&quot;, otherwise <code>FALSE</code> (see <a href="/docs/linux/man/1-stty/">stty</a>(1)).</p>
<dt><code>autodecrypt</code></p>
<dd> When the <code>TELNET ENCRYPT</code> option is negotiated, by default the actual encryption (decryption) of the data stream does not start automatically. The autoencrypt (autodecrypt) command states that encryption of the output (input) stream should be enabled as soon as possible. </p>
<p> Note that this flag exists only if encryption support is enabled.</p>
<dt><code>autologin</code></p>
<dd> If the remote side supports the <code>TELNET AUTHENTICATION</code> option, <code>telnet</code> attempts to use it to perform automatic authentication. If the <code>TELNET AUTHENTICATION</code> option is not supported, the user&#8217;s login name is propagated using the <code>TELNET NEW-ENVIRON</code> option. Setting this flag is the same as specifying the <i>a</i> option to the <code>open</code> command or on the command line.</p>
<dt><code>autosynch</code></p>
<dd> If <code>autosynch</code> and <code>localchars</code> are both <code>TRUE</code> then when either the <code>intr</code> or <code>quit</code> characters is typed (see <code>set</code> above for descriptions of the <code>intr</code> and <code>quit</code> characters), the resulting <code>telnet</code> sequence sent is followed by the <code>TELNET SYNCH</code> sequence. This procedure <code>should</code> cause the remote system to begin throwing away all previously typed input until both of the <code>telnet</code> sequences have been read and acted upon. The initial value of this toggle is <code>FALSE</code></p>
<dt><code>binary</code></p>
<dd> Enable or disable the <code>TELNET BINARY</code> option on both input and output.</p>
<dt><code>inbinary</code></p>
<dd> Enable or disable the <code>TELNET BINARY</code> option on input.</p>
<dt><code>outbinary</code></p>
<dd> Enable or disable the <code>TELNET BINARY</code> option on output.</p>
<dt><code>crlf</code></p>
<dd> If this is <code>TRUE</code> then carriage returns will be sent as <code>&lt;CR&gt;&lt;LF&gt;</code> If this is <code>FALSE</code> then carriage returns will be send as <code>&lt;CR&gt;&lt;NUL&gt;</code> The initial value for this toggle is <code>FALSE</code></p>
<dt><code>crmod</code></p>
<dd> Toggle carriage return mode. When this mode is enabled, most carriage return characters received from the remote host will be mapped into a carriage return followed by a line feed. This mode does not affect those characters typed by the user, only those received from the remote host. This mode is not very useful unless the remote host only sends carriage return, but never line feed. The initial value for this toggle is <code>FALSE</code></p>
<dt><code>debug</code></p>
<dd> Toggles socket level debugging (useful only to the <code>super user )</code> The initial value for this toggle is <code>FALSE</code></p>
<dt><code>encdebug</code></p>
<dd> Turns on debugging information for the encryption code. Note that this flag only exists if encryption support is available.</p>
<dt><code>localchars</code></p>
<dd> If this is <code>TRUE</code> then the <code>flush </code> <code>interrupt</code> <code>quit </code> <code>erase</code> and <code>kill</code> characters (see <code>set</code> above) are recognized locally, and transformed into (hopefully) appropriate <code>TELNET</code> control sequences (respectively <code>ao </code> <code>ip</code> <code>brk </code> <code>ec</code> and <code>el </code> see <code>send</code> above). The initial value for this toggle is <code>TRUE</code> in &ldquo;old line by line&rdquo; mode, and <code>FALSE</code> in &ldquo;character at a time&rdquo; mode. When the <code>LINEMODE</code> option is enabled, the value of <code>localchars</code> is ignored, and assumed to always be <code>TRUE</code> If <code>LINEMODE</code> has ever been enabled, then <code>quit</code> is sent as <code>abort </code> and <code>eof</code> and <code>suspend</code> are sent as <code>eof</code> and <code>susp</code> see <code>send</code> above).</p>
<dt><code>netdata</code></p>
<dd> Toggles the display of all network data (in hexadecimal format). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>options</code></p>
<dd> Toggles the display of some internal <code>telnet</code> protocol processing (having to do with <code>telnet</code> options). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>prettydump</code></p>
<dd> When the <code>netdata</code> toggle is enabled, if <code>prettydump</code> is enabled the output from the <code>netdata</code> command will be formatted in a more user-readable format. Spaces are put between each character in the output, and the beginning of <code>telnet</code> escape sequences are preceded by a &#8216;*&#8217; to aid in locating them.</p>
<dt><code>skiprc</code></p>
<dd> When the skiprc toggle is <code>TRUE</code> <code>telnet</code> does not read the telnetrc files. The initial value for this toggle is <code>FALSE.</code></p>
<dt><code>termdata</code></p>
<dd> Toggles the display of all terminal data (in hexadecimal format). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>verbose_encrypt</code></p>
<dd> When the <code>verbose_encrypt</code> toggle is <code>TRUE</code> <code>TELNET</code> prints out a message each time encryption is enabled or disabled. The initial value for this toggle is <code>FALSE.</code> This flag only exists if encryption support is available.</p>
<dt><code>?</code></p>
<dd> Displays the legal <code>toggle</code> commands.</dl>
<dt><code>z</code></p>
<dd> Suspend <code>telnet </code> This command only works when the user is using the <a href="/docs/linux/man/1-csh/">csh</a>(1).</p>
<dt><code>! </code>[<i>command </i> ]</p>
<dd> Execute a single command in a subshell on the local system. If <code>command</code> is omitted, then an interactive subshell is invoked.</p>
<dt><code>? </code>[<i>command </i> ]</p>
<dd> Get help. With no arguments, <code>telnet</code> prints a help summary. If a command is specified, <code>telnet</code> will print the help information for just that command.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>Telnet</code> uses at least the <code>HOME</code> <code>SHELL</code> <code>DISPLAY</code> and <code>TERM</code> environment variables. Other environment variables may be propagated to the other side via the <code>TELNET NEW-ENVIRON</code> option.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/telnetrc </code></p>
<dd> global telnet startup values</p>
<dt><code>~/.telnetrc </code></p>
<dd> user customized telnet startup values</dl>
<h2>HISTORY</h2>
<p> The <code>Telnet</code> command appeared in BSD 4.2</p>
<h2>NOTES</h2>
<p> On some remote systems, echo has to be turned off manually when in &ldquo;old line by line&rdquo; mode. </p>
<p> In &ldquo;old line by line&rdquo; mode or <code>LINEMODE</code> the terminal&#8217;s <code>eof</code> character is only recognized (and sent to the remote system) when it is the first character on a line.</p>
<h2>BUGS</h2>
<p> The source code is not comprehensible. </p>
<h2>Index</h2>
