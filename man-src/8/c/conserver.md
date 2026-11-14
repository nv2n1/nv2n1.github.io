---
title: "conserver(8)"
name: "conserver"
section: "8"
letter: "c"
url: "/docs/linux/man/8-conserver/"
description: "conserver – console server daemon"
---

<p>conserver &#8211; console server daemon</p>
<h2>Synopsis</h2>
<p><code>conserver</code> [<code>-7dDEFhinoRSuvV</code>] [<code>-a</code> <i>type</i>] [<code>-m</code> <i>max</i>] [<code>-M</code> <i>master</i>] [<code>-p</code> <i>port</i>] [<code>-b</code> <i>port</i>] [<code>-c</code> <i>cred</i>] [<code>-C</code> <i>config</i>] [<code>-P</code> <i>passwd</i>] [<code>-L</code> <i>logfile</i>] [<code>-O</code> <i>min</i>] [<code>-U</code> <i>logfile</i>]</p>
<h2>Description</h2>
<p><code>Conserver</code> is the daemon that manages remote access to system consoles by multiple users via the <code><a href="/docs/linux/man/1-console/">console</a></code>(1) client program and (optionally) log the console output. It can connect to consoles via local serial ports, Unix domain sockets, TCP sockets (for terminal servers and the like), or any external program. </p>
<p> When started, <code>conserver</code> reads the <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5) file for details of each console. The console type, logging options, serial or network parameters, and user access levels are just a few of the things that can be specified. Command-line options are then applied, possibly overriding <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5) settings. <code>Conserver</code> categorizes consoles into two types: those it should actively manage, and those it should just know about, so it can refer clients to other <code>conserver</code> instances. If the <code>master</code> value of a console matches the hostname or ip address of the local machine, <code>conserver</code> will actively manage the console. Otherwise, it&#8217;s considered a &#8220;remote&#8221; console and managed by a different server. <code>Conserver</code> forks a child for each group of consoles it must manage and assigns each process a port number to listen on. The maximum number of consoles managed by each child process is set using the <code>-m</code> option. The <code><a href="/docs/linux/man/1-console/">console</a></code>(1) client program communicates with the master console server process to find the port (and host, in a multi-server configuration) on which the appropriate child is listening. <code>Conserver</code> restricts connections from clients based on the host access section of its <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5) file, restricts users based on the console access lists of the <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5) file, and authenticates users against its <code><a href="/docs/linux/man/5-conserver-passwd/">conserver.passwd</a></code>(5) file. <code>Conserver</code> can also restrict clients using the tcp-wrappers package (enabled using <code>&#8211;with-libwrap</code>). This authentication is done before consulting the <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5) access list. </p>
<p> When Unix domain sockets are used between the client and server (enabled using <code>&#8211;with-uds</code>), authentication checks are done on the hardcoded address &#8220;127.0.0.1&#8221;. Automatic client redirection is also disabled (as if the <code>-R</code> option was used) since the client cannot communicate with remote servers. The directory used to hold the sockets is checked to make sure it&#8217;s empty when the server starts. The server will <code>not</code> remove any files in the directory itself, just in case the directory is accidentally specified as &#8220;/etc&#8221; or some other critical location. The server will do its best to remove all the sockets when it shuts down, but it could stop ungracefully (crash, &#8220;kill -9&#8221;, etc) and leave files behind. It would then be up to the admin (or a creative startup script) to clean up the directory before the server will start again. </p>
<p> <code>Conserver</code> completely controls any connection to a console. All escape sequences given by the user to <code>console</code> are passed to the server without interpretation. The server recognizes and processes all escape sequences. </p>
<p> The <code>conserver</code> parent process will automatically respawn any child process that dies. The following signals are propagated by the parent process to its children.</p>
<dl>
<dt>SIGTERM</p>
<dd>Close all connections and exit.</p>
<dt>SIGHUP</p>
<dd>Reread the configuration file. New consoles are managed by forking off new children, deleted consoles (and their clients) are dropped, and changes to consoles are done &quot;in place&quot;, resetting the console port (bringing it down and up) only when necessary. The console name is used to determine when consoles have been added/removed/changed. All actions performed by SIGUSR2 are also performed.</p>
<dt>SIGUSR1</p>
<dd>Try to connect to any consoles marked as down. This can come in handy if you had a terminal server (or more) that wasn&#8217;t accepting connections at startup and you want <code>conserver</code> to try to reconnect to all those downed ports.</p>
<dt>SIGUSR2</p>
<dd>Close and reopen all console logfiles and, if in daemon mode (<code>-d</code> option), the error logfile (see the <code>-L</code> option). All actions performed by SIGUSR1 are also performed.</dl>
<p> Consoles which have no current client connection might produce important error messages. With the <code>-u</code> option, these &#8220;unloved&#8221; errors are labeled with a machine name and output on stdout (or, in daemon mode, to the logfile). This allows a live operator or an automated log scanner to find otherwise unseen errors by watching in a single location. </p>
<p> <code>Conserver</code> must be run as root if it is to bind to a port under 1024 or if it must read protected password files (like shadow passwords) for authentication (see <code><a href="/docs/linux/man/5-conserver-passwd/">conserver.passwd</a></code>(5)). Otherwise, it may be run by any user, with <code>-p</code> used to specify a port above 1024. </p>
<p> If encryption has been built into the code (<code>&#8211;with-openssl</code>), encrypted client connections (without certificate exchanges) happen by default. To add certificate exchanges, use the <code>-c</code> option with the client and server. For authentication of the certificates to work, the signing certificate must be properly trusted, which usually means the public portion is in <i>OPENSSL_ROOT</i><code>/ssl/certs</code> (on both the client and server sides). See the sample self-signing certificate making script <code>contrib/maketestcerts</code> for further clues. To allow non-encrypted client connections (in addition to encrypted client connections), use the <code>-E</code> option.</p>
<h2>Options</h2>
<p>Options may be given as separate arguments (e.g., <code>-n</code> <code>-d</code>) or clustered (e.g., <code>-nd</code>). Options and their arguments may be separated by optional white space. Option arguments containing spaces or other characters special to the shell must be quoted.</p>
<dl>
<dt><code>-7</code></p>
<dd>Strip the high bit off of all data received, whether from the <code>console</code> client or from the console device, before any processing occurs.</p>
<dt><code>-a</code><i>type</i></p>
<dd>Set the default access type for incoming connections from <code>console</code> clients: `<code>r</code>&#8216; for refused (the default), `<code>a</code>&#8216; for allowed, or `<code>t</code>&#8216; for trusted. This applies to hosts for which no matching entry is found in the access section of <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5).</p>
<dt><code>-b</code><i>port</i></p>
<dd>Set the base port for children to listen on. Each child starts looking for free ports at <i>port</i> and working upward, trying a maximum number of ports equal to twice the maximum number of groups. If no free ports are available in that range, <code>conserver</code> exits. By default, <code>conserver</code> lets the operating system choose a free port.</p>
<dt><code>-c</code><i>cred</i></p>
<dd>Load an SSL certificate and key from the PEM encoded file <i>cred</i>.</p>
<dt><code>-C</code><i>config</i></p>
<dd>Read configuration information from the file <i>config</i>. The default <i>config</i> may be changed at compile time using the <code>&#8211;with-cffile</code> option.</p>
<dt><code>-d</code></p>
<dd>Become a daemon. Disconnects from the controlling terminal and sends all output (including any debug output) to the logfile (see <code>-L</code>).</p>
<dt><code>-D</code></p>
<dd>Enable debugging output, sent to stderr. Multiple <code>-D</code> options increases debug output.</p>
<dt><code>-E</code></p>
<dd>If encryption has been built into the code (<code>&#8211;with-openssl</code>), encrypted client connections are a requirement. This option allows non-encrypted clients (as well as encrypted clients) to connect to consoles.</p>
<dt><code>-F</code></p>
<dd>Do not automatically reinitialize failed (unexpectedly closed) consoles. If the console is a program (`|&#8217; syntax) and it closes with a zero exit status, the console is reinitialized regardless of this option. Without this option, a console is immediately reopened, and if that fails, retried every minute until successful. This option has no effect on the <code>-o</code> and <code>-O</code> options.</p>
<dt><code>-h</code></p>
<dd>Output a brief help message.</p>
<dt><code>-i</code></p>
<dd>Initiate console connections on demand (and close them when not used).</p>
<dt><code>-L</code><i>logfile</i></p>
<dd>Log errors and informational messages to <i>logfile</i> after startup in daemon mode (<code>-d</code>). This option does not apply when not running in daemon mode. The default <i>logfile</i> may be changed at compile time using the <code>&#8211;with-logfile</code> option.</p>
<dt><code>-m</code><i>max</i></p>
<dd>Set the maximum consoles managed per process. The default <i>max</i> may be changed at compile time using the <code>&#8211;with-maxmemb</code> option.</p>
<dt><code>-M</code><i>master</i></p>
<dd>Normally, this allows conserver to bind to a particular IP address (like `127.0.0.1&#8242;) instead of all interfaces. The default is to bind to all addresses. However, if <code>&#8211;with-uds</code> was used to enable Unix domain sockets for client/server communication, this points conserver to the directory where it should store the sockets. The default <i>master</i> directory (&#8220;<code>/tmp/conserver</code>&#8221;) may be changed at compile time using the <code>&#8211;with-uds</code> option.</p>
<dt><code>-n</code></p>
<dd>Obsolete (now a no-op); see <code>-u</code>.</p>
<dt><code>-o</code></p>
<dd>Normally, a client connecting to a &#8220;downed&#8221; console does just that. Using this option, the server will automatically attempt to open (&#8220;bring up&#8221;) the console when the client connects.</p>
<dt><code>-O</code><i>min</i></p>
<dd>Enable periodic attempts (every <i>min</i> minutes) to open (&#8220;bring up&#8221;) all downed consoles (similar to sending a SIGUSR1). Without this option, or if <i>min</i> is zero, no periodic attempts occur.</p>
<dt><code>-p</code><i>port</i></p>
<dd>Set the TCP port for the master process to listen on. This may be either a port number or a service name. The default <i>port</i>, &#8220;conserver&#8221; (typically 782), may be changed at compile time using the <code>&#8211;with-port</code> option. If the <code>&#8211;with-uds</code> option was used, this option is ignored.</p>
<dt><code>-P</code><i>passwd</i></p>
<dd>Read the table of authorized user data from the file <i>passwd</i>. The default <i>passwd</i> may be changed at compile time using the <code>&#8211;with-pwdfile</code> option.</p>
<dt><code>-R</code></p>
<dd>Disable automatic client redirection to other conserver hosts. This means informational commands like <code>-w</code> and <code>-i</code> will only show the status of the local conserver host and attempts to connect to remote consoles will result in an informative message to the user.</p>
<dt><code>-S</code></p>
<dd>Do not run the server, just perform a syntax check of configuration file and exit with a non-zero value if there is an error. Using more than one <code>-S</code> will cause conserver to output various information about each console in 5 colon-separated fields, enclosed in curly-braces. The philosophy behind the output is to provide information to allow external detection of multiple consoles access the same physical port. Since this is <i>highly</i> environment-specific, conserver cannot do the check internally.</p>
<dl>
<dd>
<dl>
<dt><i>name</i></p>
<dd>The name of the console.</p>
<dt><i>master</i></p>
<dd>The hostname of the master conserver host for the console.</p>
<dt><i>aliases</i></p>
<dd>The console aliases in a comma-separated list.</p>
<dt><i>type</i></p>
<dd>The type of console. Values will be a `/&#8217; for a local device, `|&#8217; for a command, `!&#8217; for a remote port, `%&#8217; for a Unix domain socket, and `#&#8217; for a noop console.</p>
<dt><i>details</i></p>
<dd>Multiple values are comma-separated and depend on the type of the console. Local devices will have the values of the device file and baud rate/parity. Commands will have string to invoke. Remote ports will have the values of the remote hostname and port number. Unix domain sockets will have the path to the socket. Noop consoles will have nothing.</dl>
</dl>
<dt><code>-u</code></p>
<dd>Send unloved console output to <code>conserver</code>&#8216;s stdout (which, in daemon mode, is redirected to the logfile). This applies to all consoles to which no user is attached, independent of whether logging of individual consoles is enabled via <code>conserver.cf</code> entries.</p>
<dt><code>-U</code><i>logfile</i></p>
<dd>Copy all console data to the &#8220;unified&#8221; <i>logfile</i>. The output is the same as the <code>-u</code> output, but all consoles, not just those without a user, are logged. Each line of output is prefixed with the console name. If a user is attached read/write, a `*&#8217; is appended to the console name, to allow log watching utilites to ignore potential user-introduced alarms.</p>
<dt><code>-v</code></p>
<dd>Echo the configuration as it is being read (be verbose).</p>
<dt><code>-V</code></p>
<dd>Output the version number and settings of the <code>conserver</code> program and then exit.</dl>
<h2>Protocol</h2>
<p>The protocol used to interact with the <code>conserver</code> daemon has two basic styles. The first style is the initial line-based mode, which occurs before connecting to a console. The second style is the character-based, escape-sequence mode, while connected to a console. </p>
<p> The initial line-based mode begins the same for both the master process and its children. Upon a successful (non-rejected) client connection, an &#8220;ok&#8221; is sent. The client then issues a command and the server responds to it with a result string (&#8220;ok&#8221; being the sign of success for most commands). The commands available are &#8220;help&#8221;, &#8220;ssl&#8221; (if SSL was built into the code), &#8220;login&#8221;, and &#8220;exit&#8221;. Using the &#8220;login&#8221; command, the client authenticates and gains access to the extended command set. This is where the master process and its children differ. The master process gives the client access to global commands, and the child provides commands for interacting with the consoles it manages. The &#8220;help&#8221; command, in both cases, will provide a complete list of commands and a short description of what they do. </p>
<p> The second, character-based, style of interaction occurs when the client issues the &#8220;call&#8221; command with a child process. This command connects the client to a console and, at that point, relays all traffic between the client and the console. There is no more command-based interaction between the client and the server, any interaction with the server is done with the default escape sequence. </p>
<p> This is, by no means, a complete description of the entire client/server interaction. It is, however, a brief explanation in order to give a idea of what the program does. See the <font SIZE="-1"><code>PROTOCOL</code></font> file in the distribution for further details.</p>
<h2>Files</h2>
<p>The following default file locations may be overridden at compile time or by the command-line options described above. Run <code>conserver -V</code> to see the defaults set at compile time. </p>
<dl>
<dt><code>/etc/conserver.cf</code></p>
<dd>description of console terminal lines and client host access levels; see <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5).</p>
<dt><code>/etc/conserver.passwd</code></p>
<dd>users allowed to access consoles; see <code><a href="/docs/linux/man/5-conserver-passwd/">conserver.passwd</a></code>(5).</p>
<dt><code>/var/run/conserver.pid</code></p>
<dd>the master conserver process ID</p>
<dt><code>/var/log/conserver</code></p>
<dd>log of errors and informational messages</p>
<dt><code>/tmp/conserver</code></p>
<dd>directory to hold Unix domain sockets (if enabled)</dl>
<p> Additionally, output from individual consoles may be logged to separate files specified in <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5).</p>
<h2>Bugs</h2>
<p>I&#8217;m sure there are bugs, I just don&#8217;t know where they are. Please let me know if you find any.</p>
<h2>Authors</h2>
<p>Thomas A. Fine, Ohio State Computer Science<br />
 Kevin S Braunsdorf, Purdue University Computing Center<br />
 Bryan Stansell, conserver.com</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-console/">console</a></code>(1), <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5), <code><a href="/docs/linux/man/5-conserver-passwd/">conserver.passwd</a></code>(5) </p>
