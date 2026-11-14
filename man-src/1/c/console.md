---
title: "console(1)"
name: "console"
section: "1"
letter: "c"
url: "/docs/linux/man/1-console/"
description: "console – console server client program"
---

<h2>NAME</h2>
<p> console &#8211; console server client program</p>
<h2>SYNOPSIS</h2>
<p> <code>console</code> [<i>generic-args</i>] [<code>-aAfFsS</code>] <code>[</code>-e <i>esc</i>] <i>console</i><br />
 <code>console</code> [<i>generic-args</i>] [<code>-iIuwWx</code>] [<i>console</i>]<br />
 <code>console</code> [<i>generic-args</i>] [<code>-hPqQrRV</code>] [<code>&#8211;</code>[<code>bB</code>] <i>message</i>] [<code>-d</code> [<i>user</i>][<code>@</code><i>console</i>]] [<code>-t</code> [<i>user</i>][<code>@</code><i>console</i>] <i>message</i>] [<code>&#8211;</code>[<code>zZ</code>] <i>cmd</i>] </p>
<p> <i>generic-args</i>: [<code>-7DEnUv</code>] [<code>-c</code> <i>cred</i>] [<code>-C</code> <i>config</i>] <code>[</code>-M <i>master</i>] <code>[</code>-p <i>port</i>] <code>[</code>-l <i>user</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Console</code> is used to manipulate console terminals remotely or to poll running <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8) daemons for status information. </p>
<p> In the first form above, <code>console</code> asks the user&#8217;s password before granting interactive access to a console (on a non-trusted system), since such a session may provide single-user access. If the server&#8217;s autocompletion feature is enabled, only as much of the console name as is required to identify it uniquely to the server is required. </p>
<p> For non-interactive options, <code>console</code> outputs only the requested information and exits. </p>
<p> <code>Console</code> knows only of a primary <code>conserver</code> host (see the <code>-M</code> option below), to which it initially connects. In a multi-server environment, the primary server may refer the client to a different server handling the requested console, or it will provide a list of all servers if required (as when <code>console</code> is invoked with the <code>-r</code> option). <code>Console</code> then opens connections to the appropriate server(s). It is not necessary for the user of <code>console</code> to know which server manages which consoles, as long as <code>console</code> knows a valid primary server and all available consoles are listed in the primary server&#8217;s configuration file.</p>
<h2>OPTIONS</h2>
<p> Options may be given as separate arguments (e.g., <code>-v</code> <code>-w</code>) or clustered (e.g., <code>-vw</code>). Options and their arguments may be separated by optional white space. Option arguments containing spaces or other characters special to the shell must be quoted.</p>
<dl>
<dt><code>-7</code></p>
<dd> Strip the high bit off of all data received, whether from user input or from the server, before any processing occurs. Disallows escape sequence characters with the high bit set.</p>
<dt><code>-a</code></p>
<dd> Access a console with a two-way (read-write) connection (this is the default). The connection is dropped to spy mode if someone else is attached read-write.</p>
<dt><code>-b</code><i>message</i></p>
<dd> Broadcast a <i>message</i> to all users connected to each server.</p>
<dt><code>-B</code><i>message</i></p>
<dd> Same as <code>-b</code> but just send a <i>message</i> to users on the primary server.</p>
<dt><code>-c</code><i>cred</i></p>
<dd> Load an SSL certificate and key from the PEM encoded file <i>cred</i>.</p>
<dt><code>-C</code><i>config</i></p>
<dd> Use the per-user configuration file <i>config</i>.</p>
<dt><code>-d</code></p>
<dd> Disconnect the users specified by <i>user</i>@<i>console</i>. You may specify the target as <i>user</i> (disconnect the <i>user,</i> regardless of what console they are attached to), @<i>console</i> (disconnect all users attached to <i>console</i>), or <i>user</i>@<i>console</i> (disconnect the <i>user</i> attached to <i>console</i>).</p>
<dt><code>-D</code></p>
<dd> Enable debugging output.</p>
<dt><code>-e</code><i>esc</i></p>
<dd> Set the initial two-character escape sequence to those represented by <i>esc</i>. Any of the forms output by <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1)&#8217;s <code>-v</code> option are accepted. The default value is &#8220;<code>^Ec</code>&#8221;.</p>
<dt><code>-E</code></p>
<dd> If encryption has been built into the code (<code>&#8211;with-openssl</code>), encrypted client connections are, by default, a requirement. This option disables any attempt at creating an encrypted connection. If you&#8217;d like to use encrypted connections when your server supports it, but fallback to non-encrypted otherwise, the <code>-U</code> option is what you want.</p>
<dt><code>-f</code></p>
<dd> Same as <code>-a</code> except it will force any existing connection into spy mode.</p>
<dt><code>-h</code></p>
<dd> Display a brief help message.</p>
<dt><code>-i</code></p>
<dd> Display status information in a machine-parseable format (see below for the details).</p>
<dt><code>-I</code></p>
<dd> Same as <code>-i</code> but just acts on the primary server.</p>
<dt><code>-l</code><i>user</i></p>
<dd> Set the login name used for authentication to <i>user</i>. By default, <code>console</code> uses $USER if its uid matches the user&#8217;s real uid, or $LOGNAME if its uid matches the user&#8217;s real uid, or else the name associated with the user&#8217;s real uid.</p>
<dt><code>-M</code><i>master</i></p>
<dd> The <code>console</code> client program polls <i>master</i> as the primary server, rather than the default set at compile time (typically &#8220;<code>console</code>&#8221;). The default <i>master</i> may be changed at compile time using the <code>&#8211;with-master</code> option. If <code>&#8211;with-uds</code> is used to enable Unix domain sockets, however, this option points <code>console</code> to the directory which holds those sockets. The default <i>master</i> directory (&#8220;<code>/tmp/conserver</code>&#8221;) may be changed at compile time using the <code>&#8211;with-uds</code> option.</p>
<dt><code>-n</code></p>
<dd> Do not read the system-wide configuration file.</p>
<dt><code>-p</code><i>port</i></p>
<dd> Set the port to connect to. This may be either a port number or a service name. The default <i>port</i> may be changed at compile time using the <code>&#8211;with-port</code> option. If the <code>&#8211;with-uds</code> option was used, this option is ignored.</p>
<dt><code>-P</code></p>
<dd> Display the pid of the master daemon process on each server.</p>
<dt><code>-q</code></p>
<dd> The <code>console</code> client connects to each server to request that the server daemon quit (shut down). The root password of the host(s) running conserver is required unless the local host is listed as &#8220;trusted&#8221; in the conserver.cf file; in that case, just press &lt;return&gt;.</p>
<dt><code>-Q</code></p>
<dd> Same as <code>-q</code> but just acts on the primary server.</p>
<dt><code>-r</code></p>
<dd> Display daemon versions. The <code>console</code> client connects to each server to request its version information.</p>
<dt><code>-R</code></p>
<dd> Same as <code>-r</code> but just acts on the primary server.</p>
<dt><code>-s</code></p>
<dd> Request a read-only (spy mode) connection. In this mode all the escape sequences (below) work, or report errors, but all other keyboard input is discarded.</p>
<dt><code>-t</code></p>
<dd> Send a text <i>message</i> to <i>user</i>@<i>console</i>. You may specify the target as <i>user</i> (send to <i>user,</i> regardless of what console they are attached to), @<i>console</i> (send to all users attached to <i>console</i>), or <i>user</i>@<i>console</i> (send to <i>user</i> attached to <i>console</i>).</p>
<dt><code>-u</code></p>
<dd> Show a list of all consoles with status (`up&#8217;, `down&#8217;, or `init&#8217;) and attached users (<i>user</i>@<i>host</i> if attached read-write, `&lt;spies&gt;&#8217; if only users in spy mode, or `&lt;none&gt;&#8217;).</p>
<dt><code>-U</code></p>
<dd> If encryption has been built into the code (<code>&#8211;with-openssl</code>), encrypted client connections are, by default, a requirement. This option allows the client to attempt an encrypted connection but fall back to a non-encrypted connection if the server doesn&#8217;t support encryption. If the encryption handshake is failing, disabling encryption on the client with the <code>-E</code> option is probably what you want.</p>
<dt><code>-v</code></p>
<dd> Be more verbose when building the connection(s). Use this option in combination with any of `show&#8217; options (below) for added benefit.</p>
<dt><code>-V</code></p>
<dd> Output the version and settings of the console client program and then exit.</p>
<dt><code>-w</code></p>
<dd> Show a list of all who are currently connected to consoles, including the hostnames where the <code>console</code> connections originate and the idle times. This is useful to see if anybody is actively using the console system if it becomes necessary to shut down <code>conserver</code>.</p>
<dt><code>-W</code></p>
<dd> Same as <code>-w</code> but just acts on the primary server.</p>
<dt><code>-x</code></p>
<dd> Show a list of consoles and devices.</p>
<dt><code>-z</code><i>cmd</i></p>
<dd> Sends a command (<i>cmd</i>) to each server and displays the result. The valid commands are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bringup</code></p>
<dd> Try to connect all consoles marked as down (this is equivalent to sending the server a SIGUSR1)</p>
<dt><code>SIGUSR1</code></p>
<dd> Same as <code>bringup</code></p>
<dt><code>help</code></p>
<dd> Displays the help message</p>
<dt><code>pid</code></p>
<dd> Returns the pid of the server (this is equivalent to <code>-P</code>)</p>
<dt><code>quit</code></p>
<dd> Instructs the server to shut down (this is equivalent to <code>-q</code> or sending the server a SIGTERM)</p>
<dt><code>SIGTERM</code></p>
<dd> Same as <code>quit</code></p>
<dt><code>reconfig</code></p>
<dd> Instructs the server to reload the configuration file, then perform the actions of <code>reopen</code> (this is equivalent to sending the server a SIGHUP)</p>
<dt><code>SIGHUP</code></p>
<dd> Same as <code>reconfig</code></p>
<dt><code>reopen</code></p>
<dd> Instructs the server to reopen all logfiles, then perform the actions of <code>bringup</code> (this is equivalent to sending the server a SIGUSR2)</p>
<dt><code>SIGUSR2</code></p>
<dd> Same as <code>reopen</code></p>
<dt><code>version</code></p>
<dd> Returns the version of the server (this is equivalent to <code>-V</code>)</dl>
</dl>
<dt><code>-Z</code><i>cmd</i></p>
<dd> Same as <code>-z</code> but just sends <i>cmd</i> to the primary server.</dl>
<p> The <code>-A</code>, <code>-F</code>, or <code>-S</code> options have the same effect as their lower-case variants. In addition, they each request the last 20 lines of the console output after making the connection (as if &#8220;<code>^Ecr</code>&#8221; were typed). </p>
<p> The <code>-i</code>, <code>-u</code>, <code>-w</code>, and <code>-x</code> options can be given a console name, which will limit their output to that console. </p>
<p> The <code>-i</code> option outputs status information regarding each console in 15 colon-separated fields.</p>
<dl>
<dt><i>name</i></p>
<dd> The name of the console.</p>
<dt><i>hostname,pid,socket</i></p>
<dd> The hostname, pid, and socket number of the child process managing the console.</p>
<dt><i>type</i></p>
<dd> The type of console. Values will be a `/&#8217; for a local device, `|&#8217; for a command, `!&#8217; for a remote port, `%&#8217; for a Unix domain socket, and `#&#8217; for a noop console.</p>
<dt><i>console-details</i></p>
<dd> The details regarding the console. The values here (all comma-separated) depend on the type of the console. Local devices will have values of the device file, baud rate/parity, and file descriptor for the device. Commands will have values of the command, the command&#8217;s pid, the pseudo-tty, and file descriptor for the pseudo-tty. Remote ports will have values of the remote hostname, remote port number, &#8220;raw&#8221; or &#8220;telnet&#8221; protocol, and file descriptor for the socket connection. Unix domain sockets will have the path to the socket and the file descriptor for the socket connection. Noop consoles will have nothing.</p>
<dt><i>users-list</i></p>
<dd> The details of each user connected to the console. The details for each user are an `@&#8217; separated list of `w&#8217;, `r&#8217;, or `s&#8217; (for read-write, read-only, or suspended), username, hostname the user is on, the user&#8217;s idle time, and (for `r&#8217; and `s&#8217; users only) &#8220;rw&#8221; or &#8220;ro&#8221; (if the user wants read-write mode or not). Each user bundle is separated by commas.</p>
<dt><i>state</i></p>
<dd> The state of the console. Values with either be &#8220;up&#8221;, &#8220;down&#8221;, or &#8220;init&#8221;.</p>
<dt><i>perm</i></p>
<dd> This value will either be &#8220;rw&#8221; or &#8220;ro&#8221;. It will only be &#8220;ro&#8221; if the console is a local device (`/&#8217; type) and the permissions are such that the server can open the file for read, but not write.</p>
<dt><i>logfile-details</i></p>
<dd> The details regarding the logging for the console. The comma-separated values will be the logfile, &#8220;log&#8221; or &#8220;nolog&#8221; (if logging is on or not &#8211; toggled via &#8220;^EcL&#8221;), &#8220;act&#8221; or &#8220;noact&#8221; (if activity logging is enabled or not &#8211; the `a&#8217; timestamp option), the timestamp interval, and the file descriptor of the logfile.</p>
<dt><i>break</i></p>
<dd> The default break sequence used for the console.</p>
<dt><i>reup</i></p>
<dd> If the console is currently down and the automatic reconnection code is at work, it will have the value of &#8220;autoup&#8221;, otherwise it will be &#8220;noautoup&#8221;.</p>
<dt><i>aliases</i></p>
<dd> The console aliases are presented in a comma-separated list.</p>
<dt><i>options</i></p>
<dd> The active options for the console are presented in a comma-separated list.</p>
<dt><i>initcmd</i></p>
<dd> The initcmd configuration option for the console.</p>
<dt><i>idletimeout</i></p>
<dd> The idletimeout configuration option for the console.</p>
<dt><i>idlestring</i></p>
<dd> The idlestring configuration option for the console.</dl>
<h2>CONFIGURATION</h2>
<p> <code>Console</code> reads configuration information from the system-wide configuration file (<code>console.cf</code>), then the per-user configuration file (<code>.consolerc</code>), and then applies command-line arguments. Each configuration location can override the previous. The same happens when parsing an individual file &#8211; the later entries always override the earlier entries. Because of that, you should put &#8220;global&#8221; defaults first and more specific defaults second. </p>
<p> The configuration file is read using the same parser as <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5), and you should check that manpage for parser details. <code>Console</code> recognizes the following configuration blocks.</p>
<dl>
<dt><code>config</code> <i>hostname</i>|<i>ipaddr</i></p>
<dd>
 Define a configuration block for the client host named <i>hostname</i> or using the address <i>ipaddr</i>. If the value of &#8220;*&#8221; is used, the configuration block will be applied to all client hosts.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>escape</code> <i>esc</i></p>
<dd>
 Set the escape sequence (see the <code>-e</code> command-line flag).</p>
<dt><code>master</code> <i>master</i></p>
<dd>
 Set the default master to <i>master</i> (see the <code>-M</code> command-line flag).</p>
<dt><code>playback</code> <i>num</i>|<code>&quot;&quot;</code></p>
<dd>
 Override the playback length for the <code>p</code> escape command to <i>num</i> lines (if the server supports it). Using the special value of &#8220;0&#8221; will cause the client to use the number of lines of the current terminal (if that can be determined). If the null string (&#8220;&quot;&quot;&#8221;) is used, the playback length will not be overridden.</p>
<dt><code>port</code> <i>port</i></p>
<dd>
 Set the default port to <i>port</i> (see the <code>-p</code> command-line flag).</p>
<dt><code>replay</code> <i>num</i>|<code>&quot;&quot;</code></p>
<dd>
 Override the replay length for the <code>r</code> escape command to <i>num</i> lines (if the server supports it). Using the special value of &#8220;0&#8221; will cause the client to use the number of lines of the current terminal (if that can be determined). If the null string (&#8220;&quot;&quot;&#8221;) is used, the replay length will not be overridden.</p>
<dt><code>sslcacertificatefile</code> <i>filename</i></p>
<dd>
 Load the valid CA certificates for the <font SIZE="-1">SSL</font> connection from the PEM encoded file.</p>
<dt><code>sslcacertificatepath</code> <i>directory</i></p>
<dd>
 Load the valid CA certificates for the <font SIZE="-1">SSL</font> connection from the PEM encoded files in the directory.</p>
<dt><code>sslcredentials</code> <i>filename</i></p>
<dd>
 Set the <font SIZE="-1">SSL</font> credentials file location (see the <code>-c</code> command-line flag).</p>
<dt><code>sslenabled</code> <code>yes</code>|<code>true</code>|<code>on</code>|<code>no</code>|<code>false</code>|<code>off</code></p>
<dd>
 Set whether or not encryption is attempted when talking to servers (see the <code>-E</code> command-line flag).</p>
<dt><code>sslrequired</code> <code>yes</code>|<code>true</code>|<code>on</code>|<code>no</code>|<code>false</code>|<code>off</code></p>
<dd>
 Set whether or not encryption is required when talking to servers (see the <code>-U</code> command-line flag).</p>
<dt><code>striphigh</code> <code>yes</code>|<code>true</code>|<code>on</code>|<code>no</code>|<code>false</code>|<code>off</code></p>
<dd>
 Set whether or not to strip the high bit off all data received (see the <code>-7</code> command-line flag).</p>
<dt><code>username</code> <i>user</i></p>
<dd>
 Set the username passed to the server to <i>user</i> (see the <code>-l</code> command-line flag).</dl>
</dl>
<dt><code>terminal</code> <i>type</i></p>
<dd>
 Define a configuration block when using a terminal of type <i>type</i>. If the value of &#8220;*&#8221; is used, the configuration block will be applied to all terminal types.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>attach</code> <i>string</i>|<code>&quot;&quot;</code></p>
<dd>
 Set a <i>string</i> to print when successfully attached to a console. Character substitions will be performed based on the <code>attachsubst</code> value and occur <i>before</i> interpretation of the special characters below. If the null string (&#8220;<code>&quot;&quot;</code>&#8221;) is used, no string will be printed. <i>string</i> is a simple character string with the exception of `\&#8217; and `^&#8217;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code></code></p>
<dd> alert</p>
<dt><code></code></p>
<dd> backspace</p>
<dt><code></code></p>
<dd> form-feed</p>
<dt><code>
</code></p>
<dd> newline</p>
<dt><code></code></p>
<dd> carriage-return</p>
<dt><code>	</code></p>
<dd> tab</p>
<dt><code></code></p>
<dd> vertical-tab</p>
<dt><code>\</code></p>
<dd> backslash</p>
<dt><code>\^</code></p>
<dd> circumflex</p>
<dt><code>\</code><i>ooo</i></p>
<dd> octal representation of a character (where <i>ooo</i> is one to three octal digits)</p>
<dt><code>\</code><i>c</i></p>
<dd> character <i>c</i></p>
<dt><code>^?</code></p>
<dd> delete</p>
<dt><code>^</code><i>c</i></p>
<dd> control character (<i>c</i> is &#8220;and&#8221;ed with 0x1f)</dl>
</dl>
</dl>
<dt>
<dd> An interesting use of <code>attach</code> and <code>attachsubst</code> would be:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
terminal xterm
{
    attach "^[]0;conserver: U@C^G";
    attachsubst U = us, C = cs;
}
</code></pre>
</dl>
</dl>
<dt><code>attachsubst</code> <i>c</i><code>=</code><i>t</i>[<i>n</i>]<i>f</i>[<code>,</code>&#8230;]|<code>&quot;&quot;</code></p>
<dd>
 Perform character substitutions on the <code>attach</code> value. A series of replacements can be defined by specifying a comma-separated list of <i>c</i><code>=</code><i>t</i>[<i>n</i>]<i>f</i> sequences where <i>c</i> is any printable character, <i>t</i> specifies the replacement value, <i>n</i> is a field length (optional), and <i>f</i> is the format string. <i>t</i> can be one of the characters below, catagorized as a string replacement or a numeric replacement, which dictates the use of the <i>n</i> and <i>f</i> fields.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>String Replacement</p>
<dd>
<dt><code>u</code></p>
<dd> username</p>
<dt><code>c</code></p>
<dd> console name </p>
</dl>
<p> Numeric Replacement</p>
<dl>
<dt>none available (yet)</p>
<dd></dl>
</dl>
</dl>
<dt>
<dd> For string replacements, if the replacement isn&#8217;t at least <i>n</i> characters, it will be padded with space characters on the left. <i>f</i> must be `s&#8217;. For numeric replacements, the value will be formatted to at least <i>n</i> characters, padded with 0s if <i>n</i> begins with a 0, and space characters otherwise. <i>f</i> must be either `d&#8217;, `x&#8217; or `X&#8217;, specifying a decimal, lower-case hexadecimal, or an uppercase hexadecimal conversion. If the null string (&#8220;<code>&quot;&quot;</code>&#8221;) is used, no replacements will be done.</p>
<dt><code>detach</code> <i>string</i>|<code>&quot;&quot;</code></p>
<dd>
 Set a <i>string</i> to print once detached from a console. Character substitions will be performed based on the <code>detachsubst</code> value. See the <code>attach</code> option for an explanation of <i>string</i>. If the null string (&#8220;<code>&quot;&quot;</code>&#8221;) is used, no string will be printed.</p>
<dt><code>detachsubst</code> <i>c</i><code>=</code><i>t</i>[<i>n</i>]<i>f</i>[<code>,</code>&#8230;]|<code>&quot;&quot;</code></p>
<dd>
 Perform character substitutions on the <code>detach</code> value. See the <code>attachsubst</code> option for an explanation of the format string.</dl>
</dl>
</dl>
<p> A simple configuration to set a new default escape sequence and override the master location would be:</p>
<dl>
<dt>
<dd>
#override options for all hosts<br />
config *<br />
{<br />
    master localhost;<br />
    escape ^ Ee;<br />
}<br />
#set things more specific to host1<br />
#note : if the entries were reversed, host1<br />
#would also use localhost.<br />
config host1<br />
{<br />
    master console1;<br />
}
</dl>
<h2>ESCAPE SEQUENCES</h2>
<p> The connection can be controlled by a two-character escape sequence, followed by a command. The default escape sequence is &#8220;control-E c&#8221; (octal 005 143). (The escape sequences are actually processed by the server; see the <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8) man page for more information.) Commands are: </p>
<dl>
<dt><code>.</code></p>
<dd> disconnect</p>
<dt><code>;</code></p>
<dd> move to another console</p>
<dt><code>a</code></p>
<dd> attach read-write if nobody already is</p>
<dt><code>b</code></p>
<dd> send broadcast message to all users on this console</p>
<dt><code>c</code></p>
<dd> toggle flow control (don&#8217;t do this)</p>
<dt><code>d</code></p>
<dd> down the current console</p>
<dt><code>e</code><i>cc</i></p>
<dd> change the escape sequence to the next two characters</p>
<dt><code>f</code></p>
<dd> forcibly attach read-write</p>
<dt><code>g</code></p>
<dd> group info</p>
<dt><code>i</code></p>
<dd> information dump</p>
<dt><code>L</code></p>
<dd> toggle logging on/off</p>
<dt><code>l?</code></p>
<dd> list the break sequences available</p>
<dt><code>l0</code></p>
<dd> send the break sequence associated with this console</p>
<dt><code>l1-9a-z</code></p>
<dd> send the specific break sequence</p>
<dt><code>m</code></p>
<dd> display the &quot;message of the day&quot;</p>
<dt><code>o</code></p>
<dd> close (if open) and reopen the line (to clear errors (silo overflows)) and the log file</p>
<dt><code>p</code></p>
<dd> playback the last 60 lines of output</p>
<dt><code>P</code></p>
<dd> set number of playback lines</p>
<dt><code>r</code></p>
<dd> replay the last 20 lines of output</p>
<dt><code>R</code></p>
<dd> set number of replay lines</p>
<dt><code>s</code></p>
<dd> switch to spy mode (read only)</p>
<dt><code>u</code></p>
<dd> show status of hosts/users in this group</p>
<dt><code>v</code></p>
<dd> show the version of the group server</p>
<dt><code>w</code></p>
<dd> who is using this console</p>
<dt><code>x</code></p>
<dd> examine this group&#8217;s devices and modes</p>
<dt><code>z</code></p>
<dd> suspend this connection</p>
<dt><code>!</code></p>
<dd> invoke task</p>
<dt><code>|</code></p>
<dd> attach a local command to the console</p>
<dt><code>?</code></p>
<dd> display list of commands</p>
<dt><code>^M</code> (return)</p>
<dd> continue, ignore the escape sequence</p>
<dt><code>^R</code> (ctrl-R)</p>
<dd> replay the last line only</p>
<dt><code>\</code><i>ooo</i></p>
<dd> send character having octal code <i>ooo</i> (must specify three octal digits)</dl>
<p> If any other character is hit after the escape sequence, all three characters will be discarded. Note that a line break or a down command can only be sent from a read-write connection. To send the escape sequence through the connection one must redefine the outer escape sequence, or use <code>^Ec\</code><i>ooo</i> to send the first escape character before typing the second character directly. </p>
<p> In the <code>-u</code> output, the login &#8220;&lt;none&gt;&#8221; indicates no one is viewing that console, and the login &#8220;&lt;spies&gt;&#8221; indicates that no one has a read-write connection (only read-only). </p>
<p> When running a local command via &#8220;<code>^Ec|</code>&#8221;, you can type `<code>^C</code>&#8216; to send the command a SIGHUP, `<code>^\</code>&#8216; to send the command a SIGKILL, and `<code>o</code>&#8216; to toggle the display of the console data.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>console -u</p>
<dd> Outputs something like:</p>
<dt>
<dd>
<pre>
dumb      up      &lt;none&gt;
expert    up      ksb [at] mentor
tyro      up      &lt;spies&gt;
mentor    up      &lt;none&gt;
sage      up      fine@cis
</pre>
<dt>
<dd> The <code>&lt;none&gt;</code> indicates no one is viewing <i>dumb</i> or <i>mentor</i>, the <code>&lt;spies&gt;</code> indicates only read-only connections exist for <i>tyro</i>, and other <i>login</i>@<i>host</i> entries indicate users attached read-write to <i>sage</i> and <i>expert</i>.</p>
<dt>console -w</p>
<dd> Outputs something like:</p>
<dt>
<dd>
<pre><code>
ksb[at] extra attach 2days expert
    file @cis attach 21 : 46 sage
        dmr[at] alice spy &amp;nbsp;
0 : 04 tyro
</code></pre>
<dt>
<dd> The third column is the idle time of the user. Either <i>hours</i>:<i>minutes</i> or number of days is displayed.</p>
<dt>console -e &quot;^[1&quot; lv426</p>
<dd> Requests a connection to the host &#8220;lv426&#8221; with the escape characters set to &#8220;escape one&#8221;.</dl>
<h2>FILES</h2>
<p> The following default file locations may be overridden at compile time or by the command-line options described above. Run <code>console -V</code> to see the defaults set at compile time. </p>
<dl>
<dt><code>/etc/console.cf</code></p>
<dd> system-wide configuration file</p>
<dt><font SIZE="-1"><code>$HOME</code></font><code>/.consolerc</code></p>
<dd> per-user configuration file</dl>
<h2>BUGS</h2>
<p> It is possible to create a loop of console connections, with ugly results. Never run <code>console</code> from within a console connection (unless you set each escape sequence differently). </p>
<p> The -i output can produce more than the stated number of fields of information if the user-provided information has embedded colons. </p>
<p> I&#8217;m sure there are more, I just don&#8217;t know where they are. Please let me know if you find any.</p>
<h2>AUTHORS</h2>
<p> Thomas A. Fine, Ohio State Computer Science<br />
 Kevin Braunsdorf, Purdue University Computing Center<br />
 Bryan Stansell, conserver.com</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-conserver-cf/">conserver.cf</a></code>(5), <code><a href="/docs/linux/man/5-conserver-passwd/">conserver.passwd</a></code>(5), <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8) </p>
<h2>Index</h2>
