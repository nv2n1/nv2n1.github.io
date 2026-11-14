---
title: "dbclient(1)"
name: "dbclient"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbclient/"
description: "dbclient – lightweight SSH client"
---

<h2>NAME</h2>
<p> dbclient &#8211; lightweight SSH client</p>
<h2>SYNOPSIS</h2>
<p> <code>dbclient</code> [<i>flag arguments</i>] [-p <i>port</i>] [-i <i>id</i>] [-L <i>l</i>:<i>h</i>:<i>p</i>] [-R <i>l</i>:<i>h</i>:<i>p</i>] [-l <i>user</i>] <i>host</i> [<i>more flags</i>] [<i>command</i>] </p>
<p> <code>dbclient</code> [<i>args</i>] [<i>user1</i>]@<i>host1</i>[^<i>port1</i>],[<i>user2</i>]@<i>host2</i>[^<i>port2</i>],&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>dbclient</code> is a small SSH client</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>command</code></p>
<dd>
<dd> A command to run on the remote host. This will normally be run by the remote host using the user&#8217;s shell. The command begins at the first hyphen argument after the host argument. If no command is specified an interactive terminal will be opened (see -t and -T).</p>
<dt><code>-p </code><i>port</i></p>
<dd> Connect to <i>port</i> on the remote host. Alternatively a port can be specified as hostname^port. Default is 22.</p>
<dt><code>-i </code><i>idfile</i></p>
<dd> Identity file. Read the identity key from file <i>idfile</i> (multiple allowed). This file is created with <a href="/docs/linux/man/1-dropbearkey/">dropbearkey</a>(1) or converted from OpenSSH with <a href="/docs/linux/man/1-dropbearconvert/">dropbearconvert</a>(1). The default path ~/.ssh/id_dropbear is used</p>
<dt><code>-L</code> [<i>listenaddress</i>]:<i>listenport</i>:<i>host</i>:<i>port</i></p>
<dd> Local port forwarding. Forward the port <i>listenport</i> on the local host through the SSH connection to port <i>port</i> on the host <i>host</i>.</p>
<dt><code>-R</code> [<i>listenaddress</i>]:<i>listenport</i>:<i>host</i>:<i>port</i></p>
<dd> Remote port forwarding. Forward the port <i>listenport</i> on the remote host through the SSH connection to port <i>port</i> on the host <i>host</i>.</p>
<dt><code>-l </code><i>user</i></p>
<dd> Username. Login as <i>user</i> on the remote host.</p>
<dt><code>-t</code></p>
<dd> Allocate a PTY. This is the default when no command is given, it gives a full interactive remote session. The main effect is that keystrokes are sent remotely immediately as opposed to local line-based editing.</p>
<dt><code>-T</code></p>
<dd> Don&#8217;t allocate a PTY. This is the default a command is given. See -t.</p>
<dt><code>-N</code></p>
<dd> Don&#8217;t request a remote shell or run any commands. Any command arguments are ignored.</p>
<dt><code>-f</code></p>
<dd> Fork into the background after authentication. A command argument (or -N) is required. This is useful when using password authentication.</p>
<dt><code>-g</code></p>
<dd> Allow non-local hosts to connect to forwarded ports. Applies to -L and -R forwarded ports, though remote connections to -R forwarded ports may be limited by the ssh server.</p>
<dt><code>-y</code></p>
<dd> Always accept hostkeys if they are unknown. If a hostkey mismatch occurs the connection will abort as normal. If specified a second time no host key checking is performed at all, this is usually undesirable.</p>
<dt><code>-A</code></p>
<dd> Forward agent connections to the remote host. dbclient will use any OpenSSH-style agent program if available ($SSH_AUTH_SOCK will be set) for public key authentication. Forwarding is only enabled if -A is specified.</p>
<dt><code>-W </code><i>windowsize</i></p>
<dd> Specify the per-channel receive window buffer size. Increasing this may improve network performance at the expense of memory use. Use -h to see the default buffer size.</p>
<dt><code>-K </code><i>timeout_seconds</i></p>
<dd> Ensure that traffic is transmitted at a certain interval in seconds. This is useful for working around firewalls or routers that drop connections after a certain period of inactivity. The trade-off is that a session may be closed if there is a temporary lapse of network connectivity. A setting if 0 disables keepalives. If no response is received for 3 consecutive keepalives the connection will be closed.</p>
<dt><code>-I </code><i>idle_timeout</i></p>
<dd> Disconnect the session if no traffic is transmitted or received for <i>idle_timeout</i> seconds.</p>
<dt><code>-J </code><i>proxy_command</i></p>
<dd> Use the standard input/output of the program <i>proxy_command</i> rather than using a normal TCP connection. A hostname should be still be provided, as this is used for comparing saved hostkeys. This command will be executed as &quot;exec proxy_command &#8230;&quot; with the default shell.</p>
<dt><code>-B </code><i>endhost:endport</i></p>
<dd> &quot;Netcat-alike&quot; mode, where Dropbear will connect to the given host, then create a forwarded connection to <i>endhost</i>. This will then be presented as dbclient&#8217;s standard input/output.</p>
<dt><code>-c </code><i>cipherlist</i></p>
<dd> Specify a comma separated list of ciphers to enable. Use <i>-c help</i> to list possibilities.</p>
<dt><code>-m </code><i>MAClist</i></p>
<dd> Specify a comma separated list of authentication MACs to enable. Use <i>-m help</i> to list possibilities.</p>
<dt><code>-o </code><i>option</i></p>
<dd> Can be used to give options in the format used by OpenSSH config file. This is useful for specifying options for which there is no separate command-line flag. For full details of the options listed below, and their possible values, see <a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5). </p>
<p> For now following options have been implemented:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ExitOnForwardFailure</code></p>
<dd> Specifies whether dbclient should terminate the connection if it cannot set up all requested local and remote port forwardings. The argument must be “yes” or “no”. The default is “no”.</p>
<dt><code>UseSyslog</code></p>
<dd> Send dbclient log messages to syslog in addition to stderr.</dl>
</dl>
<dt><code>-s </code></p>
<dd> The specified command will be requested as a subsystem, used for sftp. Dropbear doesn&#8217;t implement sftp itself but the OpenSSH sftp client can be used eg <i>sftp -S dbclient user [at] host</i></p>
<dt><code>-V</code></p>
<dd> Print the version </p>
</dl>
<h2>MULTI-HOP</h2>
<p> Dropbear will also allow multiple &quot;hops&quot; to be specified, separated by commas. In this case a connection will be made to the first host, then a TCP forwarded connection will be made through that to the second host, and so on. Hosts other than the final destination will not see anything other than the encrypted SSH stream. A port for a host can be specified with a caret (eg matt [at] martello^44 ). This syntax can also be used with scp or rsync (specifying dbclient as the ssh/rsh command). A file can be &quot;bounced&quot; through multiple SSH hops, eg </p>
<p> scp -S dbclient matt [at] martello,root@wrt,canyons:/tmp/dump . </p>
<p> Note that hostnames are resolved by the prior hop (so &quot;canyons&quot; would be resolved by the host &quot;wrt&quot;) in the example above, the same way as other -L TCP forwarded hosts are. Host keys are checked locally based on the given hostname. </p>
<h2>ESCAPE CHARACTERS</h2>
<p> Typing a newline followed by the key sequence <i>~.</i> (tilde, dot) will terminate a connection. The sequence <i>~^Z</i> (tilde, ctrl-z) will background the connection. This behaviour only applies when a PTY is used. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DROPBEAR_PASSWORD</code></p>
<dd> A password to use for remote authentication can be specified in the environment variable DROPBEAR_PASSWORD. Care should be taken that the password is not exposed to other users on a multi-user system, or stored in accessible files.</p>
<dt><code>SSH_ASKPASS</code></p>
<dd> dbclient can use an external program to request a password from a user. SSH_ASKPASS should be set to the path of a program that will return a password on standard output. This program will only be used if either DISPLAY is set and standard input is not a TTY, or the environment variable SSH_ASKPASS_ALWAYS is set.</dl>
<h2>NOTES</h2>
<p> If compiled with zlib support and if the server supports it, dbclient will always use compression. </p>
<h2>AUTHOR</h2>
<p> Matt Johnston (matt [at] ucc.asn.au).<br />
 Mihnea Stoenescu wrote initial Dropbear client support<br />
 Gerrit Pape (pape [at] smarden.org) wrote this manual page.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-dropbear/">dropbear</a>(8), <a href="/docs/linux/man/1-dropbearkey/">dropbearkey</a>(1) </p>
<p> <a rel="nofollow" href="https://matt.ucc.asn.au/dropbear/dropbear.html">https://matt.ucc.asn.au/dropbear/dropbear.html</a> </p>
<h2>Index</h2>
