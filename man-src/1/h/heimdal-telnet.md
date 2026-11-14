---
title: "heimdal-telnet(1)"
name: "heimdal-telnet"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-telnet/"
description: "telnet – user interface to the TELNET protocol"
---

<h2 class="name">NAME</h2>
<p> <code>telnet</code> &#8211; user interface to the <code>TELNET</code> protocol </p>
<h2>SYNOPSIS</h2>
<p> <code>telnet</code> [-<code>78EFKLacdfrx</code> ] [-<code>S </code><i>tos</i> ] [-<code>X </code><i>authtype</i> ] [-<code>e </code><i>escapechar</i> ] [-<code>k </code><i>realm</i> ] [-<code>l </code><i>user</i> ] [-<code>n </code><i>tracefile</i> ] [<i>host</i> [port] ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>telnet</code> command is used to communicate with another host using the <code>TELNET</code> protocol. If <code>telnet</code> is invoked without the <i>host</i> argument, it enters command mode, indicated by its prompt (<code>telnet&gt;</code> ) In this mode, it accepts and executes the commands listed below. If it is invoked with arguments, it performs an <code>open</code> command with those arguments. </p>
<p> Options:</p>
<dl>
<dt><code>-8</code></p>
<dd> Specifies an 8-bit data path. This causes an attempt to negotiate the <code>TELNET BINARY</code> option on both input and output.</p>
<dt><code>-7</code></p>
<dd> Do not try to negotiate <code>TELNET BINARY</code> option.</p>
<dt><code>-E</code></p>
<dd> Stops any character from being recognized as an escape character.</p>
<dt><code>-F</code></p>
<dd> If Kerberos V5 authentication is being used, the &#8211;<code>F</code> option allows the local credentials to be forwarded to the remote system, including any credentials that have already been forwarded into the local environment.</p>
<dt><code>-K</code></p>
<dd> Specifies no automatic login to the remote system.</p>
<dt><code>-L</code></p>
<dd> Specifies an 8-bit data path on output. This causes the BINARY option to be negotiated on output.</p>
<dt><code>-S </code><i>tos</i></p>
<dd> Sets the IP type-of-service (TOS) option for the telnet connection to the value <i>tos</i> which can be a numeric TOS value or, on systems that support it, a symbolic TOS name found in the /etc/iptos file.</p>
<dt><code>-X </code><i>atype</i></p>
<dd> Disables the <i>atype</i> type of authentication.</p>
<dt><code>-a</code></p>
<dd> Attempt automatic login. Currently, this sends the user name via the <code>USER</code> variable of the <code>ENVIRON</code> option if supported by the remote system. The name used is that of the current user as returned by <a href="/docs/linux/man/2-getlogin/">getlogin</a>(2) if it agrees with the current user ID, otherwise it is the name associated with the user ID.</p>
<dt><code>-c</code></p>
<dd> Disables the reading of the user&#8217;s .telnetrc file. (See the <code>toggle skiprc</code> command on this man page.)</p>
<dt><code>-d</code></p>
<dd> Sets the initial value of the <code>debug</code> toggle to <code>TRUE</code></p>
<dt><code>-e </code><i>escape char</i></p>
<dd> Sets the initial <code>telnet</code> <code>telnet</code> escape character to <i>escape char</i> If <i>escape char</i> is omitted, then there will be no escape character.</p>
<dt><code>-f</code></p>
<dd> If Kerberos V5 authentication is being used, the &#8211;<code>f</code> option allows the local credentials to be forwarded to the remote system.</p>
<dt><code>-k </code><i>realm</i></p>
<dd> If Kerberos authentication is being used, the &#8211;<code>k</code> option requests that telnet obtain tickets for the remote host in realm realm instead of the remote host&#8217;s realm, as determined by krb_realmofhost3.</p>
<dt><code>-l </code><i>user</i></p>
<dd> When connecting to the remote system, if the remote system understands the <code>ENVIRON</code> option, then <i>user</i> will be sent to the remote system as the value for the variable USER. This option implies the &#8211;<code>a</code> option. This option may also be used with the <code>open</code> command.</p>
<dt><code>-n </code><i>tracefile</i></p>
<dd> Opens <i>tracefile</i> for recording trace information. See the <code>set tracefile</code> command below.</p>
<dt><code>-r</code></p>
<dd> Specifies a user interface similar to <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1). In this mode, the escape character is set to the tilde (~) character, unless modified by the -e option.</p>
<dt><code>-x</code></p>
<dd> Turn on encryption of the data stream. When this option is turned on, <code>telnet</code> will exit with an error if authentication cannot be negotiated or if encryption cannot be turned on.</p>
<dt><i>host</i></p>
<dd> Indicates the official name, an alias, or the Internet address of a remote host.</p>
<dt><i>port</i></p>
<dd> Indicates a port number (address of an application). If a number is not specified, the default <code>telnet</code> port is used.</dl>
<p> When in rlogin mode, a line of the form ~. disconnects from the remote host; ~ is the telnet escape character. Similarly, the line ~^Z suspends the telnet session. The line ~^] escapes to the normal telnet escape prompt. </p>
<p> Once a connection has been opened, <code>telnet</code> will attempt to enable the <code>TELNET LINEMODE</code> option. If this fails, then <code>telnet</code> will revert to one of two input modes: either &ldquo;character at a time&rdquo; or &ldquo;old line by line&rdquo; depending on what the remote system supports. </p>
<p> When <code>LINEMODE</code> is enabled, character processing is done on the local system, under the control of the remote system. When input editing or character echoing is to be disabled, the remote system will relay that information. The remote system will also relay changes to any special characters that happen on the remote system, so that they can take effect on the local system. </p>
<p> In &ldquo;character at a time&rdquo; mode, most text typed is immediately sent to the remote host for processing. </p>
<p> In &ldquo;old line by line&rdquo; mode, all text is echoed locally, and (normally) only completed lines are sent to the remote host. The &ldquo;local echo character&rdquo; (initially &ldquo;^E&rdquo;) may be used to turn off and on the local echo (this would mostly be used to enter passwords without the password being echoed). </p>
<p> If the <code>LINEMODE</code> option is enabled, or if the <code>localchars</code> toggle is <code>TRUE</code> (the default for &ldquo;old line by line&ldquo;; see below), the user&#8217;s <code>quit </code> <code>intr</code> and <code>flush</code> characters are trapped locally, and sent as <code>TELNET</code> protocol sequences to the remote side. If <code>LINEMODE</code> has ever been enabled, then the user&#8217;s <code>susp</code> and <code>eof</code> are also sent as <code>TELNET</code> protocol sequences, and <code>quit</code> is sent as a <code>TELNET ABORT</code> instead of <code>BREAK</code> There are options (see <code>toggle</code> <code>autoflush</code> and <code>toggle</code> <code>autosynch</code> below) which cause this action to flush subsequent output to the terminal (until the remote host acknowledges the <code>TELNET</code> sequence) and flush previous terminal input (in the case of <code>quit</code> and <code>intr )</code> </p>
<p> While connected to a remote host, <code>telnet</code> command mode may be entered by typing the <code>telnet</code> &ldquo;escape character&rdquo; (initially &ldquo;^]&rdquo;). When in command mode, the normal terminal editing conventions are available. </p>
<p> The following <code>telnet</code> commands are available. Only enough of each command to uniquely identify it need be typed (this is also true for arguments to the <code>mode </code> <code>set</code> <code>toggle </code> <code>unset</code> <code>slc </code> <code>environ</code> and <code>display</code> commands). </p>
<dl>
<dt><code>auth </code><i>argument &#8230;</i></p>
<dd> The auth command manipulates the information sent through the <code>TELNET AUTHENTICATE</code> option. Valid arguments for the auth command are as follows:</p>
<dl>
<dt><code>disable </code><i>type</i></p>
<dd> Disables the specified type of authentication. To obtain a list of available types, use the <code>auth disable ?</code> command.</p>
<dt><code>enable </code><i>type</i></p>
<dd> Enables the specified type of authentication. To obtain a list of available types, use the <code>auth enable ?</code> command.</p>
<dt><code>status</code></p>
<dd> Lists the current status of the various types of authentication.</dl>
<dt><code>close</code></p>
<dd> Close a <code>TELNET</code> session and return to command mode.</p>
<dt><code>display </code><i>argument &#8230;</i></p>
<dd> Displays all, or some, of the <code>set</code> and <code>toggle</code> values (see below).</p>
<dt><code>encrypt </code><i>argument &#8230;</i></p>
<dd> The encrypt command manipulates the information sent through the <code>TELNET ENCRYPT</code> option. </p>
<p> Note: Because of export controls, the <code>TELNET ENCRYPT</code> option is not supported outside of the United States and Canada. </p>
<p> Valid arguments for the encrypt command are as follows:</p>
<dl>
<dt><code>disable </code><i>type </i> [<code>input | output</code> ]</p>
<dd>
<dd>Disables the specified type of encryption. If you omit the input and output, both input and output are disabled. To obtain a list of available types, use the <code>encrypt disable ?</code> command.</p>
<dt><code>enable </code><i>type </i> [<code>input | output</code> ]</p>
<dd>
<dd>Enables the specified type of encryption. If you omit input and output, both input and output are enabled. To obtain a list of available types, use the <code>encrypt enable ?</code> command.</p>
<dt><code>input</code></p>
<dd> This is the same as the <code>encrypt start input</code> command.</p>
<dt><code>-input</code></p>
<dd> This is the same as the <code>encrypt stop input</code> command.</p>
<dt><code>output</code></p>
<dd> This is the same as the <code>encrypt start output</code> command.</p>
<dt><code>-output</code></p>
<dd> This is the same as the <code>encrypt stop output</code> command.</p>
<dt><code>start </code>[<code>input | output</code> ]</p>
<dd> Attempts to start encryption. If you omit <code>input</code> and <code>output</code> both input and output are enabled. To obtain a list of available types, use the <code>encrypt enable ?</code> command.</p>
<dt><code>status</code></p>
<dd> Lists the current status of encryption.</p>
<dt><code>stop </code>[<code>input | output</code> ]</p>
<dd> Stops encryption. If you omit input and output, encryption is on both input and output.</p>
<dt><code>type </code><i>type</i></p>
<dd> Sets the default type of encryption to be used with later <code>encrypt start</code> or <code>encrypt stop</code> commands.</dl>
<dt><code>environ </code><i>arguments &#8230;</i></p>
<dd> The <code>environ</code> command is used to manipulate the the variables that my be sent through the <code>TELNET ENVIRON</code> option. The initial set of variables is taken from the users environment, with only the <code>DISPLAY</code> and <code>PRINTER</code> variables being exported by default. The <code>USER</code> variable is also exported if the &#8211;<code>a</code> or &#8211;<code>l</code> options are used. </p>
<p> Valid arguments for the <code>environ</code> command are:</p>
<dl>
<dt><code>define </code><i>variable value</i></p>
<dd> Define the variable <i>variable</i> to have a value of <i>value</i> Any variables defined by this command are automatically exported. The <i>value</i> may be enclosed in single or double quotes so that tabs and spaces may be included.</p>
<dt><code>undefine </code><i>variable</i></p>
<dd> Remove <i>variable</i> from the list of environment variables.</p>
<dt><code>export </code><i>variable</i></p>
<dd> Mark the variable <i>variable</i> to be exported to the remote side.</p>
<dt><code>unexport </code><i>variable</i></p>
<dd> Mark the variable <i>variable</i> to not be exported unless explicitly asked for by the remote side.</p>
<dt><code>list</code></p>
<dd> List the current set of environment variables. Those marked with a <code>*</code> will be sent automatically, other variables will only be sent if explicitly requested.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>environ</code> command.</dl>
<dt><code>logout</code></p>
<dd> Sends the <code>TELNET LOGOUT</code> option to the remote side. This command is similar to a <code>close</code> command; however, if the remote side does not support the <code>LOGOUT</code> option, nothing happens. If, however, the remote side does support the <code>LOGOUT</code> option, this command should cause the remote side to close the <code>TELNET</code> connection. If the remote side also supports the concept of suspending a user&#8217;s session for later reattachment, the logout argument indicates that you should terminate the session immediately.</p>
<dt><code>mode </code><i>type</i></p>
<dd> <i>Type</i> is one of several options, depending on the state of the <code>TELNET</code> session. The remote host is asked for permission to go into the requested mode. If the remote host is capable of entering that mode, the requested mode will be entered.</p>
<dl>
<dt><code>character</code></p>
<dd> Disable the <code>TELNET LINEMODE</code> option, or, if the remote side does not understand the <code>LINEMODE</code> option, then enter &ldquo;character at a time&ldquo; mode.</p>
<dt><code>line</code></p>
<dd> Enable the <code>TELNET LINEMODE</code> option, or, if the remote side does not understand the <code>LINEMODE</code> option, then attempt to enter &ldquo;old-line-by-line&ldquo; mode.</p>
<dt><code>isig (-isig</code> )</p>
<dd> Attempt to enable (disable) the <code>TRAPSIG</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>edit (-edit</code> )</p>
<dd> Attempt to enable (disable) the <code>EDIT</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>softtabs (-softtabs</code> )</p>
<dd> Attempt to enable (disable) the <code>SOFT_TAB</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>litecho (-litecho</code> )</p>
<dd> Attempt to enable (disable) the <code>LIT_ECHO</code> mode of the <code>LINEMODE</code> option. This requires that the <code>LINEMODE</code> option be enabled.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>mode</code> command.</dl>
<dt> <code>open </code><i>host</i> [-<code>l </code><i>user</i> ] [[-<i>port</i> ] ]</p>
<dd>
<dd>Open a connection to the named host. If no port number is specified, <code>telnet</code> will attempt to contact a <code>TELNET</code> server at the default port. The host specification may be either a host name (see <a href="/docs/linux/man/5-hosts/">hosts</a>(5)) or an Internet address specified in the &ldquo;dot notation&rdquo; (see <a href="/docs/linux/man/3-inet/">inet</a>(3)). The [-<code>l</code> ] option may be used to specify the user name to be passed to the remote system via the <code>ENVIRON</code> option. When connecting to a non-standard port, <code>telnet</code> omits any automatic initiation of <code>TELNET</code> options. When the port number is preceded by a minus sign, the initial option negotiation is done. After establishing a connection, the file .telnetrc in the users home directory is opened. Lines beginning with a # are comment lines. Blank lines are ignored. Lines that begin without white space are the start of a machine entry. The first thing on the line is the name of the machine that is being connected to. The rest of the line, and successive lines that begin with white space are assumed to be <code>telnet</code> commands and are processed as if they had been typed in manually to the <code>telnet</code> command prompt.</p>
<dt><code>quit</code></p>
<dd> Close any open <code>TELNET</code> session and exit <code>telnet </code> An end of file (in command mode) will also close a session and exit.</p>
<dt><code>send </code><i>arguments</i></p>
<dd> Sends one or more special character sequences to the remote host. The following are the arguments which may be specified (more than one argument may be specified at a time): </p>
<dl>
<dt><code>abort</code></p>
<dd> Sends the <code>TELNET ABORT</code> (Abort processes) sequence.</p>
<dt><code>ao</code></p>
<dd> Sends the <code>TELNET AO</code> (Abort Output) sequence, which should cause the remote system to flush all output <i>from</i> the remote system <i>to</i> the user&#8217;s terminal.</p>
<dt><code>ayt</code></p>
<dd> Sends the <code>TELNET AYT</code> (Are You There) sequence, to which the remote system may or may not choose to respond.</p>
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
<dd> Sends the current <code>telnet</code> escape character (initially &ldquo;^&rdquo;).</p>
<dt><code>ga</code></p>
<dd> Sends the <code>TELNET GA</code> (Go Ahead) sequence, which likely has no significance to the remote system.</p>
<dt><code>getstatus</code></p>
<dd> If the remote side supports the <code>TELNET STATUS</code> command, <code>getstatus</code> will send the subnegotiation to request that the server send its current option status.</p>
<dt><code>ip</code></p>
<dd> Sends the <code>TELNET IP</code> (Interrupt Process) sequence, which should cause the remote system to abort the currently running process.</p>
<dt><code>nop</code></p>
<dd> Sends the <code>TELNET NOP</code> (No OPeration) sequence.</p>
<dt><code>susp</code></p>
<dd> Sends the <code>TELNET SUSP</code> (SUSPend process) sequence.</p>
<dt><code>synch</code></p>
<dd> Sends the <code>TELNET SYNCH</code> sequence. This sequence causes the remote system to discard all previously typed (but not yet read) input. This sequence is sent as <code>TCP</code> urgent data (and may not work if the remote system is a BSD 4.2 system &#8212; if it doesn&#8217;t work, a lower case &ldquo;r&rdquo; may be echoed on the terminal).</p>
<dt><code>do </code><i>cmd</i></p>
<dd>
<dt><code>dont </code><i>cmd</i></p>
<dd>
<dt><code>will </code><i>cmd</i></p>
<dd>
<dt><code>wont </code><i>cmd</i></p>
<dd> Sends the <code>TELNET DO</code> <i>cmd</i> sequence. <i>Cmd</i> can be either a decimal number between 0 and 255, or a symbolic name for a specific <code>TELNET</code> command. <i>Cmd</i> can also be either <code>help</code> or <code>?</code> to print out help information, including a list of known symbolic names.</p>
<dt><code>?</code></p>
<dd> Prints out help information for the <code>send</code> command.</dl>
<dt><code>set </code><i>argument value</i></p>
<dd>
<dt><code>unset </code><i>argument value</i></p>
<dd> The <code>set</code> command will set any one of a number of <code>telnet</code> variables to a specific value or to <code>TRUE</code> The special value <code>off</code> turns off the function associated with the variable, this is equivalent to using the <code>unset</code> command. The <code>unset</code> command will disable or set to <code>FALSE</code> any of the specified functions. The values of variables may be interrogated with the <code>display</code> command. The variables which may be set or unset, but not toggled, are listed here. In addition, any of the variables for the <code>toggle</code> command may be explicitly set or unset using the <code>set</code> and <code>unset</code> commands.</p>
<dl>
<dt><code>ayt</code></p>
<dd> If <code>TELNET</code> is in localchars mode, or <code>LINEMODE</code> is enabled, and the status character is typed, a <code>TELNET AYT</code> sequence (see <code>send ayt</code> preceding) is sent to the remote host. The initial value for the &quot;Are You There&quot; character is the terminal&#8217;s status character.</p>
<dt><code>echo</code></p>
<dd> This is the value (initially &ldquo;^E&rdquo;) which, when in &ldquo;line by line&rdquo; mode, toggles between doing local echoing of entered characters (for normal processing), and suppressing echoing of entered characters (for entering, say, a password).</p>
<dt><code>eof</code></p>
<dd> If <code>telnet</code> is operating in <code>LINEMODE</code> or &ldquo;old line by line&rdquo; mode, entering this character as the first character on a line will cause this character to be sent to the remote system. The initial value of the eof character is taken to be the terminal&#8217;s <code>eof</code> character.</p>
<dt><code>erase</code></p>
<dd> If <code>telnet</code> is in <code>localchars</code> mode (see <code>toggle</code> <code>localchars</code> below), <code>and</code> if <code>telnet</code> is operating in &ldquo;character at a time&rdquo; mode, then when this character is typed, a <code>TELNET EC</code> sequence (see <code>send</code> <code>ec</code> above) is sent to the remote system. The initial value for the erase character is taken to be the terminal&#8217;s <code>erase</code> character.</p>
<dt><code>escape</code></p>
<dd> This is the <code>telnet</code> escape character (initially &ldquo;^[&rdquo;) which causes entry into <code>telnet</code> command mode (when connected to a remote system).</p>
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
<dd> This is the rlogin escape character. If set, the normal <code>TELNET</code> escape character is ignored unless it is preceded by this character at the beginning of a line. This character, at the beginning of a line followed by a &quot;.&quot; closes the connection; when followed by a ^Z it suspends the telnet command. The initial state is to disable the rlogin escape character.</p>
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
<dt><code>slc </code><i>state</i></p>
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
<dd> Show the current status of <code>telnet </code> This includes the peer one is connected to, as well as the current mode.</p>
<dt><code>toggle </code><i>arguments &#8230;</i></p>
<dd> Toggle (between <code>TRUE</code> and <code>FALSE</code> various flags that control how <code>telnet</code> responds to events. These flags may be set explicitly to <code>TRUE</code> or <code>FALSE</code> using the <code>set</code> and <code>unset</code> commands listed above. More than one argument may be specified. The state of these flags may be interrogated with the <code>display</code> command. Valid arguments are:</p>
<dl>
<dt><code>authdebug</code></p>
<dd> Turns on debugging information for the authentication code.</p>
<dt><code>autoflush</code></p>
<dd> If <code>autoflush</code> and <code>localchars</code> are both <code>TRUE</code> then when the <code>ao </code> or <code>quit</code> characters are recognized (and transformed into <code>TELNET</code> sequences; see <code>set</code> above for details), <code>telnet</code> refuses to display any data on the user&#8217;s terminal until the remote system acknowledges (via a <code>TELNET TIMING MARK</code> option) that it has processed those <code>TELNET</code> sequences. The initial value for this toggle is <code>TRUE</code> if the terminal user had not done an &quot;stty noflsh&quot;, otherwise <code>FALSE</code> (see <a href="/docs/linux/man/1-stty/">stty</a>(1)).</p>
<dt><code>autodecrypt</code></p>
<dd> When the <code>TELNET ENCRYPT</code> option is negotiated, by default the actual encryption (decryption) of the data stream does not start automatically. The autoencrypt (autodecrypt) command states that encryption of the output (input) stream should be enabled as soon as possible. </p>
<p> Note: Because of export controls, the <code>TELNET ENCRYPT</code> option is not supported outside the United States and Canada.</p>
<dt><code>autologin</code></p>
<dd> If the remote side supports the <code>TELNET AUTHENTICATION</code> option <code>TELNET</code> attempts to use it to perform automatic authentication. If the <code>AUTHENTICATION</code> option is not supported, the user&#8217;s login name are propagated through the <code>TELNET ENVIRON</code> option. This command is the same as specifying <i>a</i> option on the <code>open</code> command.</p>
<dt><code>autosynch</code></p>
<dd> If <code>autosynch</code> and <code>localchars</code> are both <code>TRUE</code> then when either the <code>intr</code> or <code>quit</code> characters is typed (see <code>set</code> above for descriptions of the <code>intr</code> and <code>quit</code> characters), the resulting <code>TELNET</code> sequence sent is followed by the <code>TELNET SYNCH</code> sequence. This procedure <code>should</code> cause the remote system to begin throwing away all previously typed input until both of the <code>TELNET</code> sequences have been read and acted upon. The initial value of this toggle is <code>FALSE</code></p>
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
<dd> Turns on debugging information for the encryption code.</p>
<dt><code>localchars</code></p>
<dd> If this is <code>TRUE</code> then the <code>flush </code> <code>interrupt</code> <code>quit </code> <code>erase</code> and <code>kill</code> characters (see <code>set</code> above) are recognized locally, and transformed into (hopefully) appropriate <code>TELNET</code> control sequences (respectively <code>ao </code> <code>ip</code> <code>brk </code> <code>ec</code> and <code>el </code> see <code>send</code> above). The initial value for this toggle is <code>TRUE</code> in &ldquo;old line by line&rdquo; mode, and <code>FALSE</code> in &ldquo;character at a time&rdquo; mode. When the <code>LINEMODE</code> option is enabled, the value of <code>localchars</code> is ignored, and assumed to always be <code>TRUE</code> If <code>LINEMODE</code> has ever been enabled, then <code>quit</code> is sent as <code>abort </code> and <code>eof</code> and <code>suspend</code> are sent as <code>eof</code> and <code>susp</code> see <code>send</code> above).</p>
<dt><code>netdata</code></p>
<dd> Toggles the display of all network data (in hexadecimal format). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>options</code></p>
<dd> Toggles the display of some internal <code>telnet</code> protocol processing (having to do with <code>TELNET</code> options). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>prettydump</code></p>
<dd> When the <code>netdata</code> toggle is enabled, if <code>prettydump</code> is enabled the output from the <code>netdata</code> command will be formatted in a more user readable format. Spaces are put between each character in the output, and the beginning of any <code>TELNET</code> escape sequence is preceded by a &#8216;*&#8217; to aid in locating them.</p>
<dt><code>skiprc</code></p>
<dd> When the skiprc toggle is <code>TRUE</code> <code>TELNET</code> skips the reading of the .telnetrc file in the users home directory when connections are opened. The initial value for this toggle is <code>FALSE</code></p>
<dt><code>termdata</code></p>
<dd> Toggles the display of all terminal data (in hexadecimal format). The initial value for this toggle is <code>FALSE</code></p>
<dt><code>verbose_encrypt</code></p>
<dd> When the <code>verbose_encrypt</code> toggle is <code>TRUE</code> <code>TELNET</code> prints out a message each time encryption is enabled or disabled. The initial value for this toggle is <code>FALSE</code> Note: Because of export controls, data encryption is not supported outside of the United States and Canada.</p>
<dt><code>?</code></p>
<dd> Displays the legal <code>toggle</code> commands.</dl>
<dt><code>z</code></p>
<dd> Suspend <code>telnet </code> This command only works when the user is using the <a href="/docs/linux/man/1-csh/">csh</a>(1).</p>
<dt><code>! </code>[<i>command</i> ]</p>
<dd> Execute a single command in a subshell on the local system. If <code>command</code> is omitted, then an interactive subshell is invoked.</p>
<dt><code>? </code>[<i>command</i> ]</p>
<dd> Get help. With no arguments, <code>telnet</code> prints a help summary. If a command is specified, <code>telnet</code> will print the help information for just that command.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>Telnet</code> uses at least the <code>HOME</code> <code>SHELL</code> <code>DISPLAY</code> and <code>TERM</code> environment variables. Other environment variables may be propagated to the other side via the <code>TELNET ENVIRON</code> option.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.telnetrc </code></p>
<dd> user customized telnet startup values</dl>
<h2>HISTORY</h2>
<p> The <code>Telnet</code> command appeared in BSD 4.2</p>
<h2>NOTES</h2>
<p> On some remote systems, echo has to be turned off manually when in &ldquo;old line by line&rdquo; mode. </p>
<p> In &ldquo;old line by line&rdquo; mode or <code>LINEMODE</code> the terminal&#8217;s <code>eof</code> character is only recognized (and sent to the remote system) when it is the first character on a line. </p>
<h2>Index</h2>
