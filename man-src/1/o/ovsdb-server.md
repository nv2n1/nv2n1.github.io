---
title: "ovsdb-server(1)"
name: "ovsdb-server"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ovsdb-server/"
description: "ovsdb-server – Open vSwitch database server"
---

<h2 class="name">NAME</h2>
<p> ovsdb-server &#8211; Open vSwitch database server </p>
<h2>SYNOPSIS</h2>
<p> <code>ovsdb-server</code> [<i>database</i>]&#8230; [<code>&#8211;remote=</code><i>remote</i>]&#8230; [<code>&#8211;run=</code><i>command</i>]</p>
<dl>
<dt>Daemon options:</p>
<dd> [<code>&#8211;pidfile</code>[<code>=</code><i>pidfile</i>]] [<code>&#8211;overwrite-pidfile</code>] [<code>&#8211;detach</code>] [<code>&#8211;no-chdir</code>]</p>
<dt>Service options:</p>
<dd> [<code>&#8211;service</code>] [<code>&#8211;service-monitor</code>]</p>
<dt>Logging options:</p>
<dd> [<code>-v</code>[<i>module</i>[<code>:</code><i>destination</i>[<code>:</code><i>level</i>]]]]&#8230;<br />
 [<code>&#8211;verbose[=</code><i>module</i>[<code>:</code><i>destination</i>[<code>:</code><i>level</i>]]]]&#8230;<br />
 [<code>&#8211;log-file</code>[<code>=</code><i>file</i>]]</p>
<dt>Public key infrastructure options:</p>
<dd> [<code>&#8211;private-key=</code><i>privkey.pem</i>]<br />
 [<code>&#8211;certificate=</code><i>cert.pem</i>]<br />
 [<code>&#8211;ca-cert=</code><i>cacert.pem</i>]<br />
 [<code>&#8211;bootstrap-ca-cert=</code><i>cacert.pem</i>]<br />
 [<code>&#8211;peer-ca-cert=</code><i>peer-cacert.pem</i>]</p>
<dt>Runtime management options:</p>
<dd> <code>&#8211;unixctl=</code><i>socket</i></p>
<dt>Common options:</p>
<dd> [<code>-h</code> | <code>&#8211;help</code>] [<code>-V</code> | <code>&#8211;version</code>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ovsdb-server</code> program provides RPC interfaces to one or more Open vSwitch databases (OVSDBs). It supports JSON-RPC client connections over active or passive TCP/IP or Unix domain sockets. </p>
<p> Each OVSDB file may be specified on the command line as <i>database</i>. If none is specified, the default is <code>/etc/openvswitch/conf.db</code>. The database files must already have been created and initialized using, for example, <code>ovsdb-tool create</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;remote=</code><i>remote</i></p>
<dd> Adds <i>remote</i> as a connection method used by <code>ovsdb-server</code>. <i>remote</i> must take one of the following forms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>pssl:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd> Listen on the given SSL <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but specifying <i>ip</i> limits connections to those from the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>pssl:6640:[::1]</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>ptcp:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd> Listen on the given TCP <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but <i>ip</i> may be specified to listen only for connections to the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ptcp:6640:[::1]</code>.</p>
<dt><code>punix:</code><i>file</i></p>
<dd> On POSIX, listen on the Unix domain server socket named <i>file</i> for a connection.</p>
<dt>
<dd> On Windows, listen on a kernel chosen TCP port on the localhost. The kernel chosen TCP port value is written in <i>file</i>.</p>
<dt><code>ssl:</code><i>ip</i><code>:</code><i>port</i></p>
<dd> The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ssl:[::1]:6640</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>tcp:</code><i>ip</i><code>:</code><i>port</i></p>
<dd> Connect to the given TCP <i>port</i> on <i>ip</i>, where <i>ip</i> can be IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>tcp:[::1]:6640</code>.</p>
<dt><code>unix:</code><i>file</i></p>
<dd> On POSIX, connect to the Unix domain server socket named <i>file</i>.</p>
<dt>
<dd> On Windows, connect to a localhost TCP port whose value is written in <i>file</i>.</p>
<dt><code>db:</code><i>db</i><code>,</code><i>table</i><code>,</code><i>column</i></p>
<dd> Reads additional connection methods from <i>column</i> in all of the rows in <i>table</i> within <i>db</i>. As the contents of <i>column</i> changes, <code>ovsdb-server</code> also adds and drops connection methods accordingly.</p>
<dt>
<dd> If <i>column</i>&#8216;s type is string or set of strings, then the connection methods are taken directly from the column. The connection methods in the column must have one of the forms described above.</p>
<dt>
<dd> If <i>column</i>&#8216;s type is UUID or set of UUIDs and references a table, then each UUID is looked up in the referenced table to obtain a row. The following columns in the row, if present and of the correct type, configure a connection method. Any additional columns are ignored.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>target</code> (string)</p>
<dd> Connection method, in one of the forms described above. This column is mandatory: if it is missing or empty then no connection method can be configured.</p>
<dt><code>max_backoff</code> (integer)</p>
<dd> Maximum number of milliseconds to wait between connection attempts.</p>
<dt><code>inactivity_probe</code> (integer)</p>
<dd> Maximum number of milliseconds of idle time on connection to client before sending an inactivity probe message.</dl>
</dl>
<dt>
<dd> It is an error for <i>column</i> to have another type.</dl>
</dl>
<dt>
<dd> To connect or listen on multiple connection methods, use multiple <code>&#8211;remote</code> options.</p>
<dt><code>&#8211;run=</code><i>command</i>]</p>
<dd> Ordinarily <code>ovsdb-server</code> runs forever, or until it is told to exit (see <code>RUNTIME MANAGEMENT COMMANDS</code> below). With this option, <code>ovsdb-server</code> instead starts a shell subprocess running <i>command</i>. When the subprocess terminates, <code>ovsdb-server</code> also exits gracefully. If the subprocess exits normally with exit code 0, then <code>ovsdb-server</code> exits with exit code 0 also; otherwise, it exits with exit code 1.</p>
<dt>
<dd> This option can be useful where a database server is needed only to run a single command, e.g.: <code>ovsdb-server &#8211;remote=punix:socket &#8211;run=&#8217;ovsdb-client dump unix:socket Open_vSwitch&#8217;</code></p>
<dt>
<dd> This option is not supported on Windows platform.</dl>
<h3>Daemon Options</h3>
<p> The following options are valid on POSIX based platforms.</p>
<dl>
<dt><code>&#8211;pidfile</code>[<code>=</code><i>pidfile</i>]</p>
<dd> Causes a file (by default, <code>ovsdb-server.pid</code>) to be created indicating the PID of the running process. If the <i>pidfile</i> argument is not specified, or if it does not begin with <code>/</code>, then it is created in <code>/var/run/openvswitch</code>.</p>
<dt>
<dd> If <code>&#8211;pidfile</code> is not specified, no pidfile is created.</p>
<dt><code>&#8211;overwrite-pidfile</code></p>
<dd> By default, when <code>&#8211;pidfile</code> is specified and the specified pidfile already exists and is locked by a running process, <code>ovsdb-server</code> refuses to start. Specify <code>&#8211;overwrite-pidfile</code> to cause it to instead overwrite the pidfile.</p>
<dt>
<dd> When <code>&#8211;pidfile</code> is not specified, this option has no effect.</p>
<dt><code>&#8211;detach</code></p>
<dd> Runs <code>ovsdb-server</code> as a background process. The process forks, and in the child it starts a new session, closes the standard file descriptors (which has the side effect of disabling logging to the console), and changes its current directory to the root (unless <code>&#8211;no-chdir</code> is specified). After the child completes its initialization, the parent exits. <code>ovsdb-server</code> detaches only after it starts listening on all configured remotes.</p>
<dt><code>&#8211;monitor</code></p>
<dd> Creates an additional process to monitor the <code>ovsdb-server</code> daemon. If the daemon dies due to a signal that indicates a programming error (<code>SIGABRT</code>, <code>SIGALRM</code>, <code>SIGBUS</code>, <code>SIGFPE</code>, <code>SIGILL</code>, <code>SIGPIPE</code>, <code>SIGSEGV</code>, <code>SIGXCPU</code>, or <code>SIGXFSZ</code>) then the monitor process starts a new copy of it. If the daemon dies or exits for another reason, the monitor process exits.</p>
<dt>
<dd> This option is normally used with <code>&#8211;detach</code>, but it also functions without it.</p>
<dt><code>&#8211;no-chdir</code></p>
<dd> By default, when <code>&#8211;detach</code> is specified, <code>ovsdb-server</code> changes its current working directory to the root directory after it detaches. Otherwise, invoking <code>ovsdb-server</code> from a carelessly chosen directory would prevent the administrator from unmounting the file system that holds that directory.</p>
<dt>
<dd> Specifying <code>&#8211;no-chdir</code> suppresses this behavior, preventing <code>ovsdb-server</code> from changing its current working directory. This may be useful for collecting core files, since it is common behavior to write core dumps into the current working directory and the root directory is not a good directory to use.</p>
<dt>
<dd> This option has no effect when <code>&#8211;detach</code> is not specified.</p>
<dt><code>&#8211;user</code></p>
<dd> Causes <code>ovsdb-server</code> to run as a different user specified in &quot;user:group&quot;, thus dropping most of the root privileges. Short forms &quot;user&quot; and &quot;:group&quot; are also allowed, with current user or group are assumed respectively. Only daemons started by the root user accepts this argument.</p>
<dt>
<dd> On Linux, daemons will be granted CAP_IPC_LOCK and CAP_NET_BIND_SERVICES before dropping root privileges. Daemons interact with datapath, such as ovs-vswitchd, will be granted two additional capabilities, namely CAP_NET_ADMIN and CAP_NET_RAW. The capability change will apply even if new user is &quot;root&quot;.</p>
<dt>
<dd> On Windows, this option is not currently supported. For security reasons, specifying this option will cause the daemon process not to start.</dl>
<h3>Service Options</h3>
<p> The following options are valid only on Windows platform.</p>
<dl>
<dt><code>&#8211;service</code></p>
<dd> Causes <code>ovsdb-server</code> to run as a service in the background. The service should already have been created through external tools like <code>SC.exe</code>.</p>
<dt><code>&#8211;service-monitor</code></p>
<dd> Causes the <code>ovsdb-server</code> service to be automatically restarted by the Windows services manager if the service dies or exits for unexpected reasons.</p>
<dt>
<dd> When <code>&#8211;service</code> is not specified, this option has no effect.</dl>
<h3>Logging Options</h3>
<dl>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd> Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd> <code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovsdb-server</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dt>
<dd> On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd> <code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dt>
<dd> Case is not significant within <i>spec</i>.</p>
<dt>
<dd> Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dt>
<dd> For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd> Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd> Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd> Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovsdb-server.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd> Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd> Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd> <code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd> <code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
</dl>
<h3>Public Key Infrastructure Options</h3>
<p> The options described below for configuring the SSL public key infrastructure accept a special syntax for obtaining their configuration from the database. If any of these options is given <code>db:</code><i>db</i><code>,</code><i>table</i><code>,</code><i>column</i> as its argument, then the actual file name is read from the specified <i>column</i> in <i>table</i> within the <i>db</i> database. The <i>column</i> must have type string or set of strings. The first nonempty string in the table is taken as the file name. (This means that ordinarily there should be at most one row in <i>table</i>.)</p>
<dl>
<dt><code>-p</code> <i>privkey.pem</i></p>
<dd>
<dt><code>&#8211;private-key=</code><i>privkey.pem</i></p>
<dd> Specifies a PEM file containing the private key used as <code>ovsdb-server</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd> Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd> Specifies a PEM file containing the CA certificate that <code>ovsdb-server</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd> Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>&#8211;bootstrap-ca-cert=</code><i>cacert.pem</i></p>
<dd> When <i>cacert.pem</i> exists, this option has the same effect as <code>-C</code> or <code>&#8211;ca-cert</code>. If it does not exist, then <code>ovsdb-server</code> will attempt to obtain the CA certificate from the SSL peer on its first SSL connection and save it to the named PEM file. If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained.</p>
<dt>
<dd> <code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate</code>, but it may be useful for bootstrapping.</p>
<dt>
<dd> This option is only useful if the SSL peer sends its CA certificate as part of the SSL certificate chain. The SSL protocol does not require the server to send the CA certificate.</p>
<dt>
<dd> This option is mutually exclusive with <code>-C</code> and <code>&#8211;ca-cert</code>.</p>
<dt><code>&#8211;peer-ca-cert=</code><i>peer-cacert.pem</i></p>
<dd> Specifies a PEM file that contains one or more additional certificates to send to SSL peers. <i>peer-cacert.pem</i> should be the CA certificate used to sign <code>ovsdb-server</code>&#8216;s own certificate, that is, the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>. If <code>ovsdb-server</code>&#8216;s certificate is self-signed, then <code>&#8211;certificate</code> and <code>&#8211;peer-ca-cert</code> should specify the same file.</p>
<dt>
<dd> This option is not useful in normal operation, because the SSL peer must already have the CA certificate for the peer to have any confidence in <code>ovsdb-server</code>&#8216;s identity. However, this offers a way for a new installation to bootstrap the CA certificate on its first SSL connection.</dl>
<h3>Other Options</h3>
<dl>
<dt><code>&#8211;unixctl=</code><i>socket</i></p>
<dd> Sets the name of the control socket on which <code>ovsdb-server</code> listens for runtime management commands (see <code>RUNTIME MANAGEMENT COMMANDS</code>, below). If <i>socket</i> does not begin with <code>/</code>, it is interpreted as relative to <code>/var/run/openvswitch</code>. If <code>&#8211;unixctl</code> is not used at all, the default socket is <code>/var/run/openvswitch/ovsdb-server.</code><i>pid</i><code>.ctl</code>, where <i>pid</i> is <code>ovsdb-server</code>&#8216;s process ID.</p>
<dt>
<dd> On Windows, uses a kernel chosen TCP port on the localhost to listen for runtime management commands. The kernel chosen TCP port value is written in a file whose absolute path is pointed by <i>socket</i>. If <code>&#8211;unixctl</code> is not used at all, the file is created as <code>ovsdb-server.ctl</code> in the configured <i>OVS_RUNDIR</i> directory.</p>
<dt>
<dd> Specifying <code>none</code> for <i>socket</i> disables the control socket feature.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Prints version information to the console.</dl>
<h2>RUNTIME MANAGEMENT COMMANDS</h2>
<p> <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) can send commands to a running <code>ovsdb-server</code> process. The currently supported commands are described below.</p>
<h3>OVSDB-SERVER COMMANDS</h3>
<p> These commands are specific to <code>ovsdb-server</code>.</p>
<dl>
<dt><code>exit</code></p>
<dd> Causes <code>ovsdb-server</code> to gracefully terminate.</p>
<dt><code>ovsdb-server/compact</code> [<i>db</i>]&#8230;</p>
<dd> Compacts each database <i>db</i> in-place. If no <i>db</i> is specified, compacts every database in-place. Databases are also automatically compacted occasionally.</p>
<dt><code>ovsdb-server/reconnect</code></p>
<dd> Makes <code>ovsdb-server</code> drop all of the JSON-RPC connections to database clients and reconnect.</p>
<dt>
<dd> This command might be useful for debugging issues with database clients.</p>
<dt><code>ovsdb-server/add-remote </code><i>remote</i></p>
<dd> Adds a remote, as if <code>&#8211;remote=</code><i>remote</i> had been specified on the <code>ovsdb-server</code> command line. (If <i>remote</i> is already a remote, this command succeeds without changing the configuration.)</p>
<dt><code>ovsdb-server/remove-remote </code><i>remote</i></p>
<dd> Removes the specified <i>remote</i> from the configuration, failing with an error if <i>remote</i> is not configured as a remote. This command only works with remotes that were named on <code>&#8211;remote</code> or <code>ovsdb-server/add-remote</code>, that is, it will not remove remotes added indirectly because they were read from the database by configuring a <code>db:</code><i>db</i><code>,</code><i>table</i><code>,</code><i>column</i> remote. (You can remove a database source with <code>ovsdb-server/remove-remote db:</code><i>db</i><code>,</code><i>table</i><code>,</code><i>column</i>, but not individual remotes found indirectly through the database.)</p>
<dt><code>ovsdb-server/list-remotes</p>
<dd> Outputs a list of the currently configured remotes named on &#8211;remote</code> or <code>ovsdb-server/add-remote</code>, that is, it does not list remotes added indirectly because they were read from the database by configuring a <code>db:</code><i>db</i><code>,</code><i>table</i><code>,</code><i>column</i> remote.</p>
<dt><code>ovsdb-server/add-db </code><i>database</i></p>
<dd> Adds the <i>database</i> to the running <code>ovsdb-server</code>. The database file must already have been created and initialized using, for example, <code>ovsdb-tool create</code>.</p>
<dt><code>ovsdb-server/remove-db </code><i>database</i></p>
<dd> Removes <i>database</i> from the running <code>ovsdb-server</code>. <i>database</i> must be a database name as listed by <code>ovsdb-server/list-dbs</code>.</p>
<dt>
<dd> If a remote has been configured that points to the specified <i>database</i> (e.g. <code>&#8211;remote=db:</code><i>database</i><code>,</code>&#8230; on the command line), then it will be disabled until another database with the same name is added again (with <code>ovsdb-server/add-db</code>).</p>
<dt>
<dd> Any public key infrastructure options specified through this database (e.g. <code>&#8211;private-key=db:</code><i>database,</i>&#8230; on the command line) will be disabled until another database with the same name is added again (with <code>ovsdb-server/add-db</code>).</p>
<dt><code>ovsdb-server/list-dbs</p>
<dd> Outputs a list of the currently configured databases added either through the command line or through the ovsdb-server/add-db</code> command.</dl>
<h3>VLOG COMMANDS</h3>
<p> These commands manage <code>ovsdb-server</code>&#8216;s logging settings.</p>
<dl>
<dt><code>vlog/set</code> [<i>spec</i>]</p>
<dd> Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd> <code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively.</p>
<dt>
<dd> On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd> <code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dt>
<dd> Case is not significant within <i>spec</i>.</p>
<dt>
<dd> Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>ovsdb-server</code> was invoked with the <code>&#8211;log-file</code> option.</p>
<dt>
<dd> For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>vlog/set PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd> Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>vlog/list</code></p>
<dd> Lists the supported logging modules and their current levels.</p>
<dt><code>vlog/list-pattern</code></p>
<dd> Lists logging patterns used for each destination.</p>
<dt><code>vlog/reopen</code></p>
<dd> Causes <code>ovsdb-server</code> to close and reopen its log file. (This is useful after rotating log files, to cause a new log file to be used.)</p>
<dt>
<dd> This has no effect unless <code>ovsdb-server</code> was invoked with the <code>&#8211;log-file</code> option.</p>
<dt><code>vlog/disable-rate-limit </code>[<i>module</i>]&#8230;</p>
<dd>
<dt><code>vlog/enable-rate-limit </code>[<i>module</i>]&#8230;</p>
<dd> By default, <code>ovsdb-server</code> limits the rate at which certain messages can be logged. When a message would appear more frequently than the limit, it is suppressed. This saves disk space, makes logs easier to read, and speeds up execution, but occasionally troubleshooting requires more detail. Therefore, <code>vlog/disable-rate-limit</code> allows rate limits to be disabled at the level of an individual log module. Specify one or more module names, as displayed by the <code>vlog/list</code> command. Specifying either no module names at all or the keyword <code>any</code> disables rate limits for every log module.</p>
<dt>
<dd> The <code>vlog/enable-rate-limit</code> command, whose syntax is the same as <code>vlog/disable-rate-limit</code>, can be used to re-enable a rate limit that was previously disabled.</dl>
<h3>MEMORY COMMANDS</h3>
<p> These commands report memory usage.</p>
<dl>
<dt><code>memory/show</code></p>
<dd> Displays some basic statistics about <code>ovsdb-server</code>&#8216;s memory usage. <code>ovsdb-server</code> also logs this information soon after startup and periodically as its memory consumption grows.</dl>
<h3>COVERAGE COMMANDS</h3>
<p> These commands manage <code>ovsdb-server</code>&#8216;s &#8220;coverage counters,&#8221; which count the number of times particular events occur during a daemon&#8217;s runtime. In addition to these commands, <code>ovsdb-server</code> automatically logs coverage counter values, at <code>INFO</code> level, when it detects that the daemon&#8217;s main loop takes unusually long to run. </p>
<p> Coverage counters are useful mainly for performance analysis and debugging.</p>
<dl>
<dt><code>coverage/show</code></p>
<dd> Displays the averaged per-second rates for the last few seconds, the last minute and the last hour, and the total counts of all of the coverage counters.</dl>
<h2>SPECIFICATIONS</h2>
<p> <code>ovsdb-server</code> implements the Open vSwitch Database (OVSDB) protocol specified in RFC 7047, with the following clarifications:</p>
<dl>
<dt>3.1. JSON Usage</p>
<dd> RFC 4627 says that names within a JSON object should be unique. The Open vSwitch JSON parser discards all but the last value for a name that is specified more than once.</p>
<dt>
<dd> The definition of &lt;error&gt; allows for implementation extensions. Currently <code>ovsdb-server</code> uses the following additional &quot;error&quot; strings which might change in later releases):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>syntax error</code> or <code>unknown column</code></p>
<dd> The request could not be parsed as an OVSDB request. An additional &quot;syntax&quot; member, whose value is a string that contains JSON, may narrow down the particular syntax that could not be parsed.</p>
<dt><code>internal error</code></p>
<dd> The request triggered a bug in <code>ovsdb-server</code>.</p>
<dt><code>ovsdb error</code></p>
<dd> A map or set contains a duplicate key.</dl>
</dl>
<dt>3.2. Schema Format</p>
<dd> RFC 7047 requires the &quot;version&quot; field in &lt;database-schema&gt;. Current versions of <code>ovsdb-server</code> allow it to be omitted (future versions are likely to require it).</p>
<dt>4. Wire Protocol</p>
<dd> The original OVSDB specifications included the following reason, omitted from RFC 7047, to operate JSON-RPC directly over a stream instead of over HTTP:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> JSON-RPC is a peer-to-peer protocol, but HTTP is a client-server protocol, which is a poor match. Thus, JSON-RPC over HTTP requires the client to periodically poll the server to receive server requests.</p>
<dt>&bull;</p>
<dd> HTTP is more complicated than stream connections and doesn&#8217;t provide any corresponding advantage.</p>
<dt>&bull;</p>
<dd> The JSON-RPC specification for HTTP transport is incomplete.</dl>
</dl>
<dt>4.1.5. Monitor</p>
<dd> For backward compatibility, <code>ovsdb-server</code> currently permits a single &lt;monitor-request&gt; to be used instead of an array; it is treated as a single-element array. Future versions of <code>ovsdb-server</code> might remove this compatibility feature.</p>
<dt>
<dd> Because the &lt;json-value&gt; parameter is used to match subsequent update notifications (see below) to the request, it must be unique among all active monitors. <code>ovsdb-server</code> rejects attempt to create two monitors with the same identifier.</p>
<dt>5.1. Notation</p>
<dd> For &lt;condition&gt;, RFC 7047 only allows the use of <code>!=</code>, <code>==</code>, <code>includes</code>, and <code>excludes</code> operators with set types. Open vSwitch 2.4 and later extend &lt;condition&gt; to allow the use of <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;=</code>, and <code>&gt;</code> operators with columns with type &#8220;set of 0 or 1 integer&#8221; and &#8220;set of 0 or 1 real&#8221;. These conditions evaluate to false when the column is empty, and otherwise as described in RFC 7047 for integer and real types.</dl>
<h2>BUGS</h2>
<p> In Open vSwitch before version 2.4, when <code>ovsdb-server</code> sent JSON-RPC error responses to some requests, it incorrectly formulated them with the <code>result</code> and <code>error</code> swapped, so that the response appeared to indicate success (with a nonsensical result) rather than an error. The requests that suffered from this problem were:</p>
<dl>
<dt><code>transact</code></p>
<dd>
<dt><code>get_schema</code></p>
<dd> Only if the request names a nonexistent database.</p>
<dt><code>monitor</code></p>
<dd>
<dt><code>lock</code></p>
<dd>
<dt><code>unlock</code></p>
<dd> In all error cases.</dl>
<p> Of these cases, the only error that a well-written application is likely to encounter in practice is <code>monitor</code> of tables or columns that do not exist, in an situation where the application has been upgraded but the old database schema is still temporarily in use. To handle this situation gracefully, we recommend that clients should treat a <code>monitor</code> response with a <code>result</code> that contains an <code>error</code> key-value pair as an error (assuming that the database being monitored does not contain a table named <code>error</code>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ovsdb-tool/">ovsdb-tool</a></code>(1). </p>
<h2>Index</h2>
