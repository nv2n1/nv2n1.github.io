---
title: "in-telnetd(8)"
name: "in-telnetd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-telnetd/"
description: "telnetd – DARPA telnet protocol server"
---

<p><code>telnetd</code> &#8211; DARPA <code>telnet</code> protocol server</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/in.telnetd</code> [-<code>ihn</code>[-<code>a </code><i>authmode</i> ] ] [-<code>D </code><i>debugmode</i> ] [-<code>L </code><i>loginprg</i> ] [-<code>S </code><i>tos</i> ] [-<code>X </code><i>authtype</i> ] [-<code>edebug</code> ] [-<code>debug </code><i>port</i> ]</p>
<h2>Description</h2>
<p>The <code>telnetd</code> program is a server which supports the <code>DARPA</code> <code>telnet</code> interactive communication protocol. <code>Telnetd</code> is normally invoked by the internet server (see <a href="/docs/linux/man/8-inetd/">inetd</a>(8)) for requests to connect to the <code>telnet</code> port as indicated by the /etc/services file (see <a href="/docs/linux/man/5-services/">services</a>(5)). The &#8211;<code>debug</code> option may be used to start up <code>telnetd</code> manually, instead of through <a href="/docs/linux/man/8-inetd/">inetd</a>(8). If started up this way, <i>port</i> may be specified to run <code>telnetd</code> on an alternate <code>TCP </code> port number. </p>
<p> The <code>telnetd</code> program accepts the following options:</p>
<dl>
<dt><code>-a </code><i>authmode</i></p>
<dd>This option may be used for specifying what mode should be used for authentication. Note that this option is only useful if <code>telnetd</code> has been compiled with support for authentication, which is not available in the current version. The following values of <i>authmode </i> are understood:</p>
<dl>
<dt><code>debug</code></p>
<dd>Turns on authentication debugging code.</p>
<dt><code>user</code></p>
<dd>Only allow connections when the remote user can provide valid authentication information to identify the remote user, and is allowed access to the specified account without providing a password.</p>
<dt><code>valid</code></p>
<dd>Only allow connections when the remote user can provide valid authentication information to identify the remote user. The <a href="/docs/linux/man/1-login/">login</a>(1) command will provide any additional user verification needed if the remote user is not allowed automatic access to the specified account.</p>
<dt><code>other</code></p>
<dd>Only allow connections that supply some authentication information. This option is currently not supported by any of the existing authentication mechanisms, and is thus the same as specifying <code>valid</code></p>
<dt><code>none</code></p>
<dd>This is the default state. Authentication information is not required. If no or insufficient authentication information is provided, then the <a href="/docs/linux/man/1-login/">login</a>(1) program will provide the necessary user verification.</p>
<dt><code>off</code></p>
<dd>This disables the authentication code. All user verification will happen through the <a href="/docs/linux/man/1-login/">login</a>(1) program.</dl>
<dt><code>-D </code><i>debugmode</i></p>
<dd>This option may be used for debugging purposes. This allows <code>telnetd</code> to print out debugging information to the connection, allowing the user to see what <code>telnetd</code> is doing. There are several possible values for <i>debugmode:</i></p>
<dl>
<dt><code>options</code></p>
<dd>Prints information about the negotiation of <code>telnet</code> options.</p>
<dt><code>report</code></p>
<dd>Prints the <code>options</code> information, plus some additional information about what processing is going on.</p>
<dt><code>netdata</code></p>
<dd>Displays the data stream received by <code>telnetd.</code></p>
<dt><code>ptydata</code></p>
<dd>Displays data written to the pty.</p>
<dt><code>exercise</code></p>
<dd>Has not been implemented yet.</dl>
<dt><code>-edebug</code></p>
<dd>If <code>telnetd</code> has been compiled with support for encryption, then the &#8211;<code>edebug</code> option may be used to enable encryption debugging code.</p>
<dt><code>-h</code></p>
<dd>Disables the printing of host-specific information before login has been completed.</p>
<dt><code>-i</code></p>
<dd>Disable reverse DNS lookups and use the numeric IP address in logs and REMOTEHOST environment variable. (-i switch corresponds to utilities like last)</p>
<dt><code>-L </code><i>loginprg</i></p>
<dd>This option may be used to specify a different login program. By default, /bin/login is used.</p>
<dt><code>-n</code></p>
<dd>Disable <code>TCP</code> keep-alives. Normally <code>telnetd</code> enables the <code>TCP</code> keep-alive mechanism to probe connections that have been idle for some period of time to determine if the client is still there, so that idle connections from machines that have crashed or can no longer be reached may be cleaned up.</p>
<dt><code>-N</code></p>
<dd>Do not use DNS to canonicalize the local hostname; Fn gethostname 2 returns a fully qualified name.</p>
<dt><code>-s</code></p>
<dd>This option is only enabled if <code>telnetd</code> is compiled with support for <code>SecurID</code> cards. It causes the &#8211;<code>s</code> option to be passed on to <a href="/docs/linux/man/1-login/">login</a>(1), and thus is only useful if <a href="/docs/linux/man/1-login/">login</a>(1) supports the &#8211;<code>s</code> flag to indicate that only <code>SecurID</code> validated logins are allowed. This is usually useful for controlling remote logins from outside of a firewall.</p>
<dt><code>-S </code><i>tos</i></p>
<dd>Sets the IP type-of-service (TOS) option for the telnet connection to the value <i>tos</i></p>
<dt><code>-X </code><i>authtype</i></p>
<dd>This option is only valid if <code>telnetd</code> has been built with support for the authentication option. It disables the use of <i>authtype</i> authentication, and can be used to temporarily disable a specific authentication type without having to recompile <code>telnetd</code></dl>
<p> If the file /etc/issue.net is present, <code>telnetd</code> will display its contents before the login prompt of a telnet session (see issue.net5). </p>
<p> <code>Telnetd</code> operates by allocating a pseudo-terminal device (see <a href="/docs/linux/man/4-pty/">pty</a>(4)) for a client, then creating a login process which has the slave side of the pseudo-terminal as <code>stdin</code> <code>stdout</code> and <code>stderr</code> <code>Telnetd</code> manipulates the master side of the pseudo-terminal, implementing the <code>telnet</code> protocol and passing characters between the remote client and the login process. </p>
<p> When a <code>telnet</code> session is started up, <code>telnetd</code> sends <code>telnet</code> options to the client side indicating a willingness to do the following <code>telnet</code> options, which are described in more detail below: </p>
<blockquote>
<pre>DO AUTHENTICATION
WILL ENCRYPT
DO TERMINAL TYPE
DO TSPEED
DO XDISPLOC
DO NEW-ENVIRON
DO ENVIRON
WILL SUPPRESS GO AHEAD
DO ECHO
DO LINEMODE
DO NAWS
WILL STATUS
DO LFLOW
DO TIMING-MARK</pre>
</blockquote>
<p> The pseudo-terminal allocated to the client is configured to operate in &#8220;cooked&#8221; mode, and with <code>XTABS</code> <code>CRMOD</code> enabled (see <a href="/docs/linux/man/4-tty/">tty</a>(4)). </p>
<p> <code>Telnetd</code> has support for enabling locally the following <code>telnet</code> options:</p>
<dl>
<dt><code>&quot;WILL ECHO&quot;</code></p>
<dd>When the <code>LINEMODE</code> option is enabled, a <code>WILL ECHO</code> or <code>WONT ECHO</code> will be sent to the client to indicate the current state of terminal echoing. When terminal echo is not desired, a <code>WILL ECHO</code> is sent to indicate that <code>telnetd</code> will take care of echoing any data that needs to be echoed to the terminal, and then nothing is echoed. When terminal echo is desired, a <code>WONT ECHO</code> is sent to indicate that <code>telnetd</code> will not be doing any terminal echoing, so the client should do any terminal echoing that is needed.</p>
<dt><code>&quot;WILL BINARY&quot;</code></p>
<dd>Indicates that the client is willing to send a 8 bits of data, rather than the normal 7 bits of the Network Virtual Terminal.</p>
<dt><code>&quot;WILL SGA&quot;</code></p>
<dd>Indicates that it will not be sending <code>IAC GA,</code> go ahead, commands.</p>
<dt><code>&quot;WILL STATUS&quot;</code></p>
<dd>Indicates a willingness to send the client, upon request, of the current status of all <code>TELNET</code> options.</p>
<dt><code>&quot;WILL TIMING-MARK&quot;</code></p>
<dd>Whenever a <code>DO TIMING-MARK</code> command is received, it is always responded to with a <code>WILL TIMING-MARK</code></p>
<dt><code>&quot;WILL LOGOUT&quot;</code></p>
<dd>When a <code>DO LOGOUT</code> is received, a <code>WILL LOGOUT</code> is sent in response, and the <code>TELNET</code> session is shut down.</p>
<dt><code>&quot;WILL ENCRYPT&quot;</code></p>
<dd>Only sent if <code>telnetd</code> is compiled with support for data encryption, and indicates a willingness to decrypt the data stream.</dl>
<p> <code>Telnetd</code> has support for enabling remotely the following <code>TELNET</code> options:</p>
<dl>
<dt><code>&quot;DO BINARY&quot;</code></p>
<dd>Sent to indicate that <code>telnetd</code> is willing to receive an 8 bit data stream.</p>
<dt><code>&quot;DO LFLOW&quot;</code></p>
<dd>Requests that the client handle flow control characters remotely.</p>
<dt><code>&quot;DO ECHO&quot;</code></p>
<dd>This is not really supported, but is sent to identify a 4.2BSD <a href="/docs/linux/man/1-telnet/">telnet</a>(1) client, which will improperly respond with <code>WILL ECHO.</code> If a <code>WILL ECHO</code> is received, a <code>DONT ECHO</code> will be sent in response.</p>
<dt><code>&quot;DO TERMINAL-TYPE&quot;</code></p>
<dd>Indicates a desire to be able to request the name of the type of terminal that is attached to the client side of the connection.</p>
<dt><code>&quot;DO SGA&quot;</code></p>
<dd>Indicates that it does not need to receive <code>IAC GA,</code> the go ahead command.</p>
<dt><code>&quot;DO NAWS&quot;</code></p>
<dd>Requests that the client inform the server when the window (display) size changes.</p>
<dt><code>&quot;DO TERMINAL-SPEED&quot;</code></p>
<dd>Indicates a desire to be able to request information about the speed of the serial line to which the client is attached.</p>
<dt><code>&quot;DO XDISPLOC&quot;</code></p>
<dd>Indicates a desire to be able to request the name of the X windows display that is associated with the telnet client.</p>
<dt><code>&quot;DO NEW-ENVIRON&quot;</code></p>
<dd>Indicates a desire to be able to request environment variable information, as described in RFC 1572.</p>
<dt><code>&quot;DO ENVIRON&quot;</code></p>
<dd>Indicates a desire to be able to request environment variable information, as described in RFC 1408.</p>
<dt><code>&quot;DO LINEMODE&quot;</code></p>
<dd>Only sent if <code>telnetd</code> is compiled with support for linemode, and requests that the client do line by line processing.</p>
<dt><code>&quot;DO TIMING-MARK&quot;</code></p>
<dd>Only sent if <code>telnetd</code> is compiled with support for both linemode and kludge linemode, and the client responded with <code>WONT LINEMODE.</code> If the client responds with <code>WILL TM,</code> the it is assumed that the client supports kludge linemode. Note that the [-<code>k</code> ] option can be used to disable this.</p>
<dt><code>&quot;DO AUTHENTICATION&quot;</code></p>
<dd>Only sent if <code>telnetd</code> is compiled with support for authentication, and indicates a willingness to receive authentication information for automatic login.</p>
<dt><code>&quot;DO ENCRYPT&quot;</code></p>
<dd>Only sent if <code>telnetd</code> is compiled with support for data encryption, and indicates a willingness to decrypt the data stream. issue.net5).</dl>
</dl>
<h2>Files</h2>
<p>/etc/services /etc/issue.net</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-telnet/">telnet</a>(1), <a href="/docs/linux/man/1-login/">login</a>(1), issue.net5,</p>
<h2>Standards</h2>
<dl>
<dt><code>RFC-854</code></p>
<dd><code>TELNET</code> PROTOCOL SPECIFICATION</p>
<dt><code>RFC-855</code></p>
<dd>TELNET OPTION SPECIFICATIONS</p>
<dt><code>RFC-856</code></p>
<dd>TELNET BINARY TRANSMISSION</p>
<dt><code>RFC-857</code></p>
<dd>TELNET ECHO OPTION</p>
<dt><code>RFC-858</code></p>
<dd>TELNET SUPPRESS GO AHEAD OPTION</p>
<dt><code>RFC-859</code></p>
<dd>TELNET STATUS OPTION</p>
<dt><code>RFC-860</code></p>
<dd>TELNET TIMING MARK OPTION</p>
<dt><code>RFC-861</code></p>
<dd>TELNET EXTENDED OPTIONS &#8211; LIST OPTION</p>
<dt><code>RFC-885</code></p>
<dd>TELNET END OF RECORD OPTION</p>
<dt><code>RFC-1073</code></p>
<dd>Telnet Window Size Option</p>
<dt><code>RFC-1079</code></p>
<dd>Telnet Terminal Speed Option</p>
<dt><code>RFC-1091</code></p>
<dd>Telnet Terminal-Type Option</p>
<dt><code>RFC-1096</code></p>
<dd>Telnet X Display Location Option</p>
<dt><code>RFC-1123</code></p>
<dd>Requirements for Internet Hosts &#8212; Application and Support</p>
<dt><code>RFC-1184</code></p>
<dd>Telnet Linemode Option</p>
<dt><code>RFC-1372</code></p>
<dd>Telnet Remote Flow Control Option</p>
<dt><code>RFC-1416</code></p>
<dd>Telnet Authentication Option</p>
<dt><code>RFC-1411</code></p>
<dd>Telnet Authentication: Kerberos Version 4</p>
<dt><code>RFC-1412</code></p>
<dd>Telnet Authentication: SPX</p>
<dt><code>RFC-1571</code></p>
<dd>Telnet Environment Option Interoperability Issues</p>
<dt><code>RFC-1572</code></p>
<dd>Telnet Environment Option</dl>
</dl>
<h2>Bugs</h2>
<p>Some <code>TELNET</code> commands are only partially implemented. Because of bugs in the original 4.2 BSD <a href="/docs/linux/man/1-telnet/">telnet</a>(1), <code>telnetd</code> performs some dubious protocol exchanges to try to discover if the remote client is, in fact, a 4.2 BSD <a href="/docs/linux/man/1-telnet/">telnet</a>(1). Binary mode has no common interpretation except between similar operating systems (Unix in this case). The terminal type name received from the remote client is converted to lower case. <code>Telnetd</code> never sends <code>TELNET</code> <code>IAC GA</code> (go ahead) commands. The source code is not comprehensible. </p>
