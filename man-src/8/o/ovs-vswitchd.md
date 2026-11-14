---
title: "ovs-vswitchd(8)"
name: "ovs-vswitchd"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-vswitchd/"
description: "ovs-vswitchd – Open vSwitch daemon"
---

<p>ovs-vswitchd &#8211; Open vSwitch daemon</p>
<h2>Synopsis</h2>
<p><code>ovs-vswitchd </code>[<i>database</i>]</p>
<h2>Description</h2>
<p>A daemon that manages and controls any number of Open vSwitch switches on the local machine. The <i>database</i> argument specifies how <code>ovs-vswitchd</code> connects to <code>ovsdb-server</code>. The default is <code>unix:/var/run/openvswitch/db.sock</code>. The following forms are accepted:</p>
<dl>
<dt><code>ssl:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ssl:[::1]:6640</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>tcp:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>Connect to the given TCP <i>port</i> on <i>ip</i>, where <i>ip</i> can be IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>tcp:[::1]:6640</code>.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, connect to the Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, connect to a localhost TCP port whose value is written in <i>file</i>.</p>
<dt><code>pssl:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given SSL <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but specifying <i>ip</i> limits connections to those from the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>pssl:6640:[::1]</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>ptcp:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given TCP <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but <i>ip</i> may be specified to listen only for connections to the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ptcp:6640:[::1]</code>.</p>
<dt><code>punix:</code><i>file</i></p>
<dd>On POSIX, listen on the Unix domain server socket named <i>file</i> for a connection.</p>
<dd>On Windows, listen on a kernel chosen TCP port on the localhost. The kernel chosen TCP port value is written in <i>file</i>.</dl>
<p> <code>ovs-vswitchd</code> retrieves its configuration from <i>database</i> at startup. It sets up Open vSwitch datapaths and then operates switching across each bridge described in its configuration files. As the database changes, <code>ovs-vswitchd</code> automatically updates its configuration to match. <code>ovs-vswitchd</code> switches may be configured with any of the following features:</p>
<dl>
<dt>&bull;</p>
<dd>L2 switching with MAC learning.</p>
<dt>&bull;</p>
<dd>NIC bonding with automatic fail-over and source MAC-based TX load balancing (&quot;SLB&quot;).</p>
<dt>&bull;</p>
<dd>802.1Q VLAN support.</p>
<dt>&bull;</p>
<dd>Port mirroring, with optional VLAN tagging.</p>
<dt>&bull;</p>
<dd>NetFlow v5 flow logging.</p>
<dt>&bull;</p>
<dd>sFlow(R) monitoring.</p>
<dt>&bull;</p>
<dd>Connectivity to an external OpenFlow controller, such as NOX.</dl>
<p> Only a single instance of <code>ovs-vswitchd</code> is intended to run at a time. A single <code>ovs-vswitchd</code> can manage any number of switch instances, up to the maximum number of supported Open vSwitch datapaths. <code>ovs-vswitchd</code> does all the necessary management of Open vSwitch datapaths itself. Thus, external tools, such <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8), are not needed for managing datapaths in conjunction with <code>ovs-vswitchd</code>, and their use to modify datapaths when <code>ovs-vswitchd</code> is running can interfere with its operation. (<code>ovs-dpctl</code> may still be useful for diagnostics.) An Open vSwitch datapath kernel module must be loaded for <code>ovs-vswitchd</code> to be useful. Please refer to the <code>INSTALL.Linux</code> file included in the Open vSwitch distribution for instructions on how to build and load the Open vSwitch kernel module. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;mlockall</code></p>
<dd>Causes <code>ovs-vswitchd</code> to call the <code>mlockall()</code> function, to attempt to lock all of its process memory into physical RAM, preventing the kernel from paging any of its memory to disk. This helps to avoid networking interruptions due to system memory pressure.</p>
<dd>Some systems do not support <code>mlockall()</code> at all, and other systems only allow privileged users, such as the superuser, to use it. <code>ovs-vswitchd</code> emits a log message if <code>mlockall()</code> is unavailable or unsuccessful.</dl>
<h3>DPDK Options</h3>
<dl>
<dt><code>&#8211;dpdk</code></p>
<dd>Initialize <code>ovs-vswitchd</code> DPDK datapath. Refer to INSTALL.DPDK for details.</dl>
<h3>Daemon Options</h3>
<p>The following options are valid on POSIX based platforms.</p>
<dl>
<dt><code>&#8211;pidfile</code>[<code>=</code><i>pidfile</i>]</p>
<dd>Causes a file (by default, <code>ovs-vswitchd.pid</code>) to be created indicating the PID of the running process. If the <i>pidfile</i> argument is not specified, or if it does not begin with <code>/</code>, then it is created in <code>/var/run/openvswitch</code>.</p>
<dd>If <code>&#8211;pidfile</code> is not specified, no pidfile is created.</p>
<dt><code>&#8211;overwrite-pidfile</code></p>
<dd>By default, when <code>&#8211;pidfile</code> is specified and the specified pidfile already exists and is locked by a running process, <code>ovs-vswitchd</code> refuses to start. Specify <code>&#8211;overwrite-pidfile</code> to cause it to instead overwrite the pidfile.</p>
<dd>When <code>&#8211;pidfile</code> is not specified, this option has no effect.</p>
<dt><code>&#8211;detach</code></p>
<dd>Runs <code>ovs-vswitchd</code> as a background process. The process forks, and in the child it starts a new session, closes the standard file descriptors (which has the side effect of disabling logging to the console), and changes its current directory to the root (unless <code>&#8211;no-chdir</code> is specified). After the child completes its initialization, the parent exits. <code>ovs-vswitchd</code> detaches only after it has connected to the database, retrieved the initial configuration, and set up that configuration.</p>
<dt><code>&#8211;monitor</code></p>
<dd>Creates an additional process to monitor the <code>ovs-vswitchd</code> daemon. If the daemon dies due to a signal that indicates a programming error (<code>SIGABRT</code>, <code>SIGALRM</code>, <code>SIGBUS</code>, <code>SIGFPE</code>, <code>SIGILL</code>, <code>SIGPIPE</code>, <code>SIGSEGV</code>, <code>SIGXCPU</code>, or <code>SIGXFSZ</code>) then the monitor process starts a new copy of it. If the daemon dies or exits for another reason, the monitor process exits.</p>
<dd>This option is normally used with <code>&#8211;detach</code>, but it also functions without it.</p>
<dt><code>&#8211;no-chdir</code></p>
<dd>By default, when <code>&#8211;detach</code> is specified, <code>ovs-vswitchd</code> changes its current working directory to the root directory after it detaches. Otherwise, invoking <code>ovs-vswitchd</code> from a carelessly chosen directory would prevent the administrator from unmounting the file system that holds that directory.</p>
<dd>Specifying <code>&#8211;no-chdir</code> suppresses this behavior, preventing <code>ovs-vswitchd</code> from changing its current working directory. This may be useful for collecting core files, since it is common behavior to write core dumps into the current working directory and the root directory is not a good directory to use.</p>
<dd>This option has no effect when <code>&#8211;detach</code> is not specified.</p>
<dt><code>&#8211;user</code></p>
<dd>Causes <code>ovs-vswitchd</code> to run as a different user specified in &quot;user:group&quot;, thus dropping most of the root privileges. Short forms &quot;user&quot; and &quot;:group&quot; are also allowed, with current user or group are assumed respectively. Only daemons started by the root user accepts this argument.</p>
<dd>On Linux, daemons will be granted CAP_IPC_LOCK and CAP_NET_BIND_SERVICES before dropping root privileges. Daemons interact with datapath, such as ovs-vswitchd, will be granted two additional capabilities, namely CAP_NET_ADMIN and CAP_NET_RAW. The capability change will apply even if new user is &quot;root&quot;.</p>
<dd>On Windows, this option is not currently supported. For security reasons, specifying this option will cause the daemon process not to start.</dl>
<h3>Service Options</h3>
<p>The following options are valid only on Windows platform.</p>
<dl>
<dt><code>&#8211;service</code></p>
<dd>Causes <code>ovs-vswitchd</code> to run as a service in the background. The service should already have been created through external tools like <code>SC.exe</code>.</p>
<dt><code>&#8211;service-monitor</code></p>
<dd>Causes the <code>ovs-vswitchd</code> service to be automatically restarted by the Windows services manager if the service dies or exits for unexpected reasons.</p>
<dd>When <code>&#8211;service</code> is not specified, this option has no effect.</dl>
<h3>Public Key Infrastructure Options</h3>
<dl>
<dt><code>-p</code> <i>privkey.pem</i></p>
<dd>
<dt><code>&#8211;private-key=</code><i>privkey.pem</i></p>
<dd>Specifies a PEM file containing the private key used as <code>ovs-vswitchd</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd>Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd>Specifies a PEM file containing the CA certificate that <code>ovs-vswitchd</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd>Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>&#8211;bootstrap-ca-cert=</code><i>cacert.pem</i></p>
<dd>When <i>cacert.pem</i> exists, this option has the same effect as <code>-C</code> or <code>&#8211;ca-cert</code>. If it does not exist, then <code>ovs-vswitchd</code> will attempt to obtain the CA certificate from the SSL peer on its first SSL connection and save it to the named PEM file. If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained.</p>
<dd><code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate</code>, but it may be useful for bootstrapping.</p>
<dd>This option is only useful if the SSL peer sends its CA certificate as part of the SSL certificate chain. The SSL protocol does not require the server to send the CA certificate.</p>
<dd>This option is mutually exclusive with <code>-C</code> and <code>&#8211;ca-cert</code>.</dl>
<h3>Logging Options</h3>
<dl>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovs-vswitchd</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd>Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovs-vswitchd.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd>Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd>Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd><code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd><code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
</dl>
<h3>Other Options</h3>
<dl>
<dt><code>&#8211;unixctl=</code><i>socket</i></p>
<dd>Sets the name of the control socket on which <code>ovs-vswitchd</code> listens for runtime management commands (see <code>RUNTIME MANAGEMENT COMMANDS</code>, below). If <i>socket</i> does not begin with <code>/</code>, it is interpreted as relative to <code>/var/run/openvswitch</code>. If <code>&#8211;unixctl</code> is not used at all, the default socket is <code>/var/run/openvswitch/ovs-vswitchd.</code><i>pid</i><code>.ctl</code>, where <i>pid</i> is <code>ovs-vswitchd</code>&#8216;s process ID.</p>
<dd>On Windows, uses a kernel chosen TCP port on the localhost to listen for runtime management commands. The kernel chosen TCP port value is written in a file whose absolute path is pointed by <i>socket</i>. If <code>&#8211;unixctl</code> is not used at all, the file is created as <code>ovs-vswitchd.ctl</code> in the configured <i>OVS_RUNDIR</i> directory.</p>
<dd>Specifying <code>none</code> for <i>socket</i> disables the control socket feature.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</dl>
<h2>Runtime Management Commands</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) can send commands to a running <code>ovs-vswitchd</code> process. The currently supported commands are described below. The command descriptions assume an understanding of how to configure Open vSwitch.</p>
<h3>General Commands</h3>
<dl>
<dt><code>exit</code></p>
<dd>Causes <code>ovs-vswitchd</code> to gracefully terminate.</p>
<dt><code>qos/show</code> <i>interface</i></p>
<dd>Queries the kernel for Quality of Service configuration and statistics associated with the given <i>interface</i>.</p>
<dt><code>bfd/show</code> [<i>interface</i>]</p>
<dd>Displays detailed information about Bidirectional Forwarding Detection configured on <i>interface</i>. If <i>interface</i> is not specified, then displays detailed information about all interfaces with BFD enabled.</p>
<dt><code>bfd/set-forwarding</code> [<i>interface</i>] <i>status</i></p>
<dd>Force the fault status of the BFD module on <i>interface</i> (or all interfaces if none is given) to be <i>status</i>. <i>status</i> can be &quot;true&quot;, &quot;false&quot;, or &quot;normal&quot; which reverts to the standard behavior.</p>
<dt><code>cfm/show</code> [<i>interface</i>]</p>
<dd>Displays detailed information about Connectivity Fault Management configured on <i>interface</i>. If <i>interface</i> is not specified, then displays detailed information about all interfaces with CFM enabled.</p>
<dt><code>cfm/set-fault</code> [<i>interface</i>] <i>status</i></p>
<dd>Force the fault status of the CFM module on <i>interface</i> (or all interfaces if none is given) to be <i>status</i>. <i>status</i> can be &quot;true&quot;, &quot;false&quot;, or &quot;normal&quot; which reverts to the standard behavior.</p>
<dt><code>stp/tcn</code> [<i>bridge</i>]</p>
<dd>Forces a topology change event on <i>bridge</i> if it&#8217;s running STP. This may cause it to send Topology Change Notifications to its peers and flush its MAC table.. If no <i>bridge</i> is given, forces a topology change event on all bridges.</dl>
<h3>Bridge Commands</h3>
<p>These commands manage bridges.</p>
<dl>
<dt><code>fdb/flush</code> [<i>bridge</i>]</p>
<dd>Flushes <i>bridge</i> MAC address learning table, or all learning tables if no <i>bridge</i> is given.</p>
<dt><code>fdb/show</code> <i>bridge</i></p>
<dd>Lists each MAC address/VLAN pair learned by the specified <i>bridge</i>, along with the port on which it was learned and the age of the entry, in seconds.</p>
<dt><code>mdb/flush</code> [<i>bridge</i>]</p>
<dd>Flushes <i>bridge</i> multicast snooping table, or all snooping tables if no <i>bridge</i> is given.</p>
<dt><code>mdb/show</code> <i>bridge</i></p>
<dd>Lists each multicast group/VLAN pair learned by the specified <i>bridge</i>, along with the port on which it was learned and the age of the entry, in seconds.</p>
<dt><code>bridge/reconnect</code> [<i>bridge</i>]</p>
<dd>Makes <i>bridge</i> drop all of its OpenFlow controller connections and reconnect. If <i>bridge</i> is not specified, then all bridges drop their controller connections and reconnect.</p>
<dd>This command might be useful for debugging OpenFlow controller issues.</p>
<dt><code>bridge/dump-flows</code> <i>bridge</i></p>
<dd>Lists all flows in <i>bridge</i>, including those normally hidden to commands such as <code>ovs-ofctl dump-flows</code>. Flows set up by mechanisms such as in-band control and fail-open are hidden from the controller since it is not allowed to modify or override them.</dl>
<h3>Bond Commands</h3>
<p>These commands manage bonded ports on an Open vSwitch&#8217;s bridges. To understand some of these commands, it is important to understand a detail of the bonding implementation called &#8220;source load balancing&#8221; (SLB). Instead of directly assigning Ethernet source addresses to slaves, the bonding implementation computes a function that maps an 48-bit Ethernet source addresses into an 8-bit value (a &#8220;MAC hash&#8221; value). All of the Ethernet addresses that map to a single 8-bit value are then assigned to a single slave.</p>
<dl>
<dt><code>bond/list</code></p>
<dd>Lists all of the bonds, and their slaves, on each bridge.</p>
<dt><code>bond/show</code> [<i>port</i>]</p>
<dd>Lists all of the bond-specific information (updelay, downdelay, time until the next rebalance) about the given bonded <i>port</i>, or all bonded ports if no <i>port</i> is given. Also lists information about each slave: whether it is enabled or disabled, the time to completion of an updelay or downdelay if one is in progress, whether it is the active slave, the hashes assigned to the slave. Any LACP information related to this bond may be found using the <code>lacp/show</code> command.</p>
<dt><code>bond/migrate</code> <i>port</i> <i>hash</i> <i>slave</i></p>
<dd>Only valid for SLB bonds. Assigns a given MAC hash to a new slave. <i>port</i> specifies the bond port, <i>hash</i> the MAC hash to be migrated (as a decimal number between 0 and 255), and <i>slave</i> the new slave to be assigned.</p>
<dd>The reassignment is not permanent: rebalancing or fail-over will cause the MAC hash to be shifted to a new slave in the usual manner.</p>
<dd>A MAC hash cannot be migrated to a disabled slave.</p>
<dt><code>bond/set-active-slave</code> <i>port</i> <i>slave</i></p>
<dd>Sets <i>slave</i> as the active slave on <i>port</i>. <i>slave</i> must currently be enabled.</p>
<dd>The setting is not permanent: a new active slave will be selected if <i>slave</i> becomes disabled.</p>
<dt><code>bond/enable-slave</code> <i>port</i> <i>slave</i></p>
<dd>
<dt><code>bond/disable-slave</code> <i>port</i> <i>slave</i></p>
<dd>Enables (or disables) <i>slave</i> on the given bond <i>port</i>, skipping any updelay (or downdelay).</p>
<dd>This setting is not permanent: it persists only until the carrier status of <i>slave</i> changes.</p>
<dt><code>bond/hash</code> <i>mac</i> [<i>vlan</i>] [<i>basis</i>]</p>
<dd>Returns the hash value which would be used for <i>mac</i> with <i>vlan</i> and <i>basis</i> if specified.</p>
<dt><code>lacp/show</code> [<i>port</i>]</p>
<dd>Lists all of the LACP related information about the given <i>port</i>: active or passive, aggregation key, system id, and system priority. Also lists information about each slave: whether it is enabled or disabled, whether it is attached or detached, port id and priority, actor information, and partner information. If <i>port</i> is not specified, then displays detailed information about all interfaces with CFM enabled.</dl>
<h3>Dpctl Datapath Debugging Commands</h3>
<p>The primary way to configure <code>ovs-vswitchd</code> is through the Open vSwitch database, e.g. using <code><a href="/docs/linux/man/8-ovs-vsctl/">ovs-vsctl</a></code>(8). These commands provide a debugging interface for managing datapaths. They implement the same features (and syntax) as <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8). Unlike <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8), these commands work with datapaths that are integrated into <code>ovs-vswitchd</code> (e.g. the <code>netdev</code> datapath type). </p>
<dl>
<dt><code>dpctl/</code><code>add-dp </code><i>dp</i> [<i>netdev</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dd>Creates datapath <i>dp</i>, with a local port also named <i>dp</i>. This will fail if a network device <i>dp</i> already exists.</p>
<dd>If <i>netdev</i>s are specified, <code>ovs-vswitchd</code> adds them to the new datapath, just as if <code>add-if</code> was specified.</p>
<dt><code>dpctl/</code><code>del-dp </code><i>dp</i></p>
<dd>Deletes datapath <i>dp</i>. If <i>dp</i> is associated with any network devices, they are automatically removed.</p>
<dt><code>dpctl/</code><code>add-if </code><i>dp netdev</i>[<code>,</code><i>option</i>]&#8230;</p>
<dd>Adds each <i>netdev</i> to the set of network devices datapath <i>dp</i> monitors, where <i>dp</i> is the name of an existing datapath, and <i>netdev</i> is the name of one of the host&#8217;s network devices, e.g. <code>eth0</code>. Once a network device has been added to a datapath, the datapath has complete ownership of the network device&#8217;s traffic and the network device appears silent to the rest of the system.</p>
<dd>A <i>netdev</i> may be followed by a comma-separated list of options. The following options are currently supported:</p>
<dl>
<dd>
<dl>
<dt><code>type=</code><i>type</i></p>
<dd>Specifies the type of port to add. The default type is <code>system</code>.</p>
<dt><code>port_no=</code><i>port</i></p>
<dd>Requests a specific port number within the datapath. If this option is not specified then one will be automatically assigned.</p>
<dt><i>key</i><code>=</code><i>value</i></p>
<dd>Adds an arbitrary key-value option to the port&#8217;s configuration.</dl>
</dl>
<dd><code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5) documents the available port types and options.</p>
<dt><code>dpctl/</code><code>set-if </code><i>dp port</i>[<code>,</code><i>option</i>]&#8230;</p>
<dd>Reconfigures each <i>port</i> in <i>dp</i> as specified. An <i>option</i> of the form <i>key</i><code>=</code><i>value</i> adds the specified key-value option to the port or overrides an existing key&#8217;s value. An <i>option</i> of the form <i>key</i><code>=</code>, that is, without a value, deletes the key-value named <i>key</i>. The type and port number of a port cannot be changed, so <code>type</code> and <code>port_no</code> are only allowed if they match the existing configuration.</p>
<dt><code>dpctl/</code><code>del-if </code><i>dp netdev</i>&#8230;</p>
<dd>Removes each <i>netdev</i> from the list of network devices datapath <i>dp</i> monitors.</p>
<dt><code>dpctl/</code><code>dump-dps</code></p>
<dd>Prints the name of each configured datapath on a separate line.</p>
<dt> <code>dpctl/</code><code>show [<code>-s</code> | <code>&#8211;statistics</code>] </code>[<i>dp</i>&#8230;]</p>
<dd>Prints a summary of configured datapaths, including their datapath numbers and a list of ports connected to each datapath. (The local port is identified as port 0.) If <code>-s</code> or <code>&#8211;statistics</code> is specified, then packet and byte counters are also printed for each port.</p>
<dd>The datapath numbers consists of flow stats and mega flow mask stats.</p>
<dd>The &quot;lookups&quot; row displays three stats related to flow lookup triggered by processing incoming packets in the datapath. &quot;hit&quot; displays number of packets matches existing flows. &quot;missed&quot; displays the number of packets not matching any existing flow and require user space processing. &quot;lost&quot; displays number of packets destined for user space process but subsequently dropped before reaching userspace. The sum of &quot;hit&quot; and &quot;miss&quot; equals to the total number of packets datapath processed.</p>
<dd>The &quot;flows&quot; row displays the number of flows in datapath.</p>
<dd>The &quot;masks&quot; row displays the mega flow mask stats. This row is omitted for datapath not implementing mega flow. &quot;hit&quot; displays the total number of masks visited for matching incoming packets. &quot;total&quot; displays number of masks in the datapath. &quot;hit/pkt&quot; displays the average number of masks visited per packet; the ratio between &quot;hit&quot; and total number of packets processed by the datapath&quot;.</p>
<dd>If one or more datapaths are specified, information on only those datapaths are displayed. Otherwise, <code>ovs-vswitchd</code> displays information about all configured datapaths.</dl>
<h3>Datapath Flow Table Debugging Commands</h3>
<p>The following commands are primarily useful for debugging Open vSwitch. The flow table entries (both matches and actions) that they work with are not OpenFlow flow entries. Instead, they are different and considerably simpler flows maintained by the Open vSwitch kernel module. Use <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8), instead, to work with OpenFlow flow entries. </p>
<p> The <i>dp</i> argument to each of these commands is optional when exactly one datapath exists, in which case that datapath is the default. When multiple datapaths exist, then a datapath name is required.</p>
<dl>
<dt> <code>dpctl/</code><code>dump-flows</code> [<code>-m </code>| <code>&#8211;more</code>] [<i>dp</i>] [<code>filter=</code><i>filter</i>]</p>
<dd>Prints to the console all flow entries in datapath <i>dp</i>&#8216;s flow table. Without <code>-m</code> or <code>&#8211;more</code>, output omits match fields that a flow wildcards entirely; with <code>-m</code> or <code>&#8211;more</code>, output includes all wildcarded fields.</p>
<dd>If <code>filter=</code><i>filter</i> is specified, only displays the flows that match the <i>filter</i>. <i>filter</i> is a flow in the form similiar to that accepted by <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8)&#8217;s <code>add-flow</code> command. (This is not an OpenFlow flow: besides other differences, it never contains wildcards.) The <i>filter</i> is also useful to match wildcarded fields in the datapath flow. As an example, <code>filter=&#8217;tcp,tp_src=100&#8242;</code> will match the datapath flow containing &#8216;<code>tcp(src=80/0xff00,dst=8080/0xff)</code>&#8216;.</p>
<dt><code>dpctl/</code><code>add-flow</code> [<i>dp</i>] <i>flow actions</i></p>
<dd>
<dt> <code>dpctl/</code><code>mod-flow</code> [<code>&#8211;clear</code>] [<code>&#8211;may-create</code>] [<code>-s</code> | <code>&#8211;statistics</code>] [<i>dp</i>] <i>flow actions</i></p>
<dd>Adds or modifies a flow in <i>dp</i>&#8216;s flow table that, when a packet matching <i>flow</i> arrives, causes <i>actions</i> to be executed.</p>
<dd>The <code>add-flow</code> command succeeds only if <i>flow</i> does not already exist in <i>dp</i>. Contrariwise, <code>mod-flow</code> without <code>&#8211;may-create</code> only modifies the actions for an existing flow. With <code>&#8211;may-create</code>, <code>mod-flow</code> will add a new flow or modify an existing one.</p>
<dd>If <code>-s</code> or <code>&#8211;statistics</code> is specified, then <code>mod-flow</code> prints the modified flow&#8217;s statistics. A flow&#8217;s statistics are the number of packets and bytes that have passed through the flow, the elapsed time since the flow last processed a packet (if ever), and (for TCP flows) the union of the TCP flags processed through the flow.</p>
<dd>With <code>&#8211;clear</code>, <code>mod-flow</code> zeros out the flow&#8217;s statistics. The statistics printed if <code>-s</code> or <code>&#8211;statistics</code> is also specified are those from just before clearing the statistics.</p>
<dt> <code>dpctl/</code><code>del-flow</code> [<code>-s</code> | <code>&#8211;statistics</code>] [<i>dp</i>] <i>flow</i></p>
<dd>Deletes the flow from <i>dp</i>&#8216;s flow table that matches <i>flow</i>. If <code>-s</code> or <code>&#8211;statistics</code> is specified, then <code>del-flow</code> prints the deleted flow&#8217;s statistics.</p>
<dt><code>dpctl/</code><code>get-flow</code> [<i>dp</i>] ufid:<i>ufid</i></p>
<dd>Fetches the flow from <i>dp</i>&#8216;s flow table with unique identifier <i>ufid</i>. <i>ufid</i> must be specified as a string of 32 hexadecimal characters.</p>
<dt><code>dpctl/</code><code>del-flows</code> [<i>dp</i>]</p>
<dd>Deletes all flow entries from datapath <i>dp</i>&#8216;s flow table.</dl>
<h3>Connection Tracking Table Debugging Commands</h3>
<p>The following commands are primarily useful for debugging the connection tracking entries in the datapath. </p>
<p> The <i>dp</i> argument to each of these commands is optional when exactly one datapath exists, in which case that datapath is the default. When multiple datapaths exist, then a datapath name is required. </p>
<p> <code>N.B.</code>(Linux specific): the <i>system</i> datapaths (i.e. the Linux kernel module Open vSwitch datapaths) share a single connection tracking table (which is also used by other kernel subsystems, such as iptables, nftables and the regular host stack). Therefore, the following commands do not apply specifically to one datapath.</p>
<dl>
<dt> <code>dpctl/</code><code>dump-conntrack</code> [<code>-m</code> | <code>&#8211;more</code>] [<code>-s</code> | <code>&#8211;statistics</code>] [<i>dp</i>] [<code>zone=</code><i>zone</i>]</p>
<dd>Prints to the console all the connection entries in the tracker used by <i>dp</i>. If <code>zone=</code><i>zone</i> is specified, only shows the connections in <code>zone</code>. With <code>&#8211;more</code>, some implementation specific details are included. With <code>&#8211;statistics</code> timeouts and timestamps are added to the output.</p>
<dt><code>dpctl/</code><code>flush-conntrack [</code><i>dp</i>] [<code>zone=</code><i>zone</i>]</p>
<dd>Flushes all the connection entries in the tracker used by <i>dp</i>. If <code>zone=</code><i>zone</i> is specified, only flushes the connections in <code>zone</code>.</dl>
<h3>Dpif-Netdev Commands</h3>
<p>These commands are used to expose internal information (mostly statistics) about the &#8220;dpif-netdev&#8221; userspace datapath. If there is only one datapath (as is often the case, unless <code>dpctl/</code> commands are used), the <i>dp</i> argument can be omitted.</p>
<dl>
<dt><code>dpif-netdev/pmd-stats-show</code> [<i>dp</i>]</p>
<dd>Shows performance statistics for each pmd thread of the datapath <i>dp</i>. The special thread &#8220;main&#8221; sums up the statistics of every non pmd thread. The sum of &#8220;emc hits&#8221;, &#8220;masked hits&#8221; and &#8220;miss&#8221; is the number of packets received by the datapath. Cycles are counted using the TSC or similar facilities (when available on the platform). To reset these counters use <code>dpif-netdev/pmd-stats-clear</code>. The duration of one cycle depends on the measuring infrastructure.</p>
<dt><code>dpif-netdev/pmd-stats-clear</code> [<i>dp</i>]</p>
<dd>Resets to zero the per pmd thread performance numbers shown by the <code>dpif-netdev/pmd-stats-show</code> command. It will NOT reset datapath or bridge statistics, only the values shown by the above command.</dl>
<h3>Datapath Debugging Commands</h3>
<p>These commands query and modify datapaths. They are are similar to <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8) commands. <code>dpif/show</code> has the additional functionality, beyond <code>dpctl/show</code> of printing OpenFlow port numbers. The other commands are redundant and will be removed in a future release.</p>
<dl>
<dt><code>dpif/dump-dps</code></p>
<dd>Prints the name of each configured datapath on a separate line.</p>
<dt><code>dpif/show</code></p>
<dd>Prints a summary of configured datapaths, including statistics and a list of connected ports. The port information includes the OpenFlow port number, datapath port number, and the type. (The local port is identified as OpenFlow port 65534.)</p>
<dt><code>dpif/dump-flows</code> [<code>-m</code>] <i>dp</i></p>
<dd>Prints to the console all flow entries in datapath <i>dp</i>&#8216;s flow table. Without <code>-m</code>, output omits match fields that a flow wildcards entirely; with <code>-m</code> output includes all wildcarded fields.</p>
<dd>This command is primarily useful for debugging Open vSwitch. The flow table entries that it displays are not OpenFlow flow entries. Instead, they are different and considerably simpler flows maintained by the datapath module. If you wish to see the OpenFlow flow entries, use <code>ovs-ofctl dump-flows</code>.</p>
<dt><code>dpif/del-flows </code><i>dp</i></p>
<dd>Deletes all flow entries from datapath <i>dp</i>&#8216;s flow table and underlying datapath implementation (e.g., kernel datapath module).</p>
<dd>This command is primarily useful for debugging Open vSwitch. As discussed in <code>dpif/dump-flows</code>, these entries are not OpenFlow flow entries.</dl>
<h3>Ofproto Commands</h3>
<p>These commands manage the core OpenFlow switch implementation (called <code>ofproto</code>).</p>
<dl>
<dt><code>ofproto/list</code></p>
<dd>Lists the names of the running ofproto instances. These are the names that may be used on <code>ofproto/trace</code>.</p>
<dt><code>ofproto/trace</code> [<i>dpname</i>] <i>odp_flow</i> [<code>-generate </code>| <i>packet</i>]</p>
<dd>
<dt><code>ofproto/trace</code> <i>bridge</i> <i>br_flow</i> [<code>-generate </code>| <i>packet</i>]</p>
<dd>
<dt><code>ofproto/trace-packet-out</code> [<code>-consistent</code>] [<i>dpname</i>] <i>odp_flow</i> [<code>-generate </code>| <i>packet</i>] <i>actions</i></p>
<dd>
<dt><code>ofproto/trace-packet-out</code> [<code>-consistent</code>] <i>bridge</i> <i>br_flow</i> [<code>-generate </code>| <i>packet</i>] <i>actions</i></p>
<dd>Traces the path of an imaginary packet through <i>switch</i> and reports the path that it took. The initial treatment of the packet varies based on the command:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>ofproto/trace</code> looks the packet up in the OpenFlow flow table, as if the packet had arrived on an OpenFlow port.</p>
<dt>&bull;</p>
<dd><code>ofproto/trace-packet-out</code> applies the specified OpenFlow <i>actions</i>, as if the packet, flow, and actions had been specified in an OpenFlow &#8220;packet-out&#8221; request.</dl>
</dl>
<dd>The packet&#8217;s headers (e.g. source and destination) and metadata (e.g. input port), together called its &#8220;flow,&#8221; are usually all that matter for the purpose of tracing a packet. You can specify the flow in the following ways:</p>
<dl>
<dd>
<dl>
<dt><i>dpname</i> <i>odp_flow</i></p>
<dd><i>odp_flow</i> is a flow in the form printed by <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8)&#8217;s <code>dump-flows</code> command. If all of your bridges have the same type, which is the common case, then you can omit <i>dpname</i>, but if you have bridges of different types (say, both <code>ovs-netdev</code> and <code>ovs-system</code>), then you need to specify a <i>dpname</i> to disambiguate.</p>
<dt><i>bridge</i> <i>br_flow</i></p>
<dd><i>br_flow</i> is a flow in the form similar to that accepted by <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8)&#8217;s <code>add-flow</code> command. (This is not an OpenFlow flow: besides other differences, it never contains wildcards.) <i>bridge</i> names of the bridge through which <i>br_flow</i> should be traced.</dl>
</dl>
<dd>Most commonly, one specifies only a flow, using one of the forms above, but sometimes one might need to specify an actual packet instead of just a flow:</p>
<dl>
<dd>
<dl>
<dt>Side effects.</p>
<dd>Some actions have side effects. For example, the <code>normal</code> action can update the MAC learning table, and the <code>learn</code> action can change OpenFlow tables. The trace commands only perform side effects when a packet is specified. If you want side effects to take place, then you must supply a packet.</p>
<dd>(Output actions are obviously side effects too, but the trace commands never execute them, even when one specifies a packet.)</p>
<dt>Incomplete information.</p>
<dd>Most of the time, Open vSwitch can figure out everything about the path of a packet using just the flow, but in some special circumstances it needs to look at parts of the packet that are not included in the flow. When this is the case, and you do not supply a packet, then a trace command will tell you it needs a packet.</dl>
</dl>
<dd>If you wish to include a packet as part of a trace operation, there are two ways to do it:</p>
<dl>
<dd>
<dl>
<dt><code>-generate</code></p>
<dd>This option, added to one of the ways to specify a flow already described, causes Open vSwitch to internally generate a packet with the flow described and then to use that packet. If your goal is to execute side effects, then <code>-generate</code> is the easiest way to do it, but <code>-generate</code> is not a good way to fill in incomplete information, because it generates packets based on only the flow information, which means that the packets really do not have any more information than the flow.</p>
<dt><i>packet</i></p>
<dd>This form supplies an explicit <i>packet</i> as a sequence of hex digits. An Ethernet frame is at least 14 bytes long, so there must be at least 28 hex digits. Obviously, it is inconvenient to type in the hex digits by hand, so the <code><a href="/docs/linux/man/1-ovs-pcap/">ovs-pcap</a></code>(1) and <code><a href="/docs/linux/man/1-ovs-tcpundump/">ovs-tcpundump</a></code>(1) utilities provide easier ways.</p>
<dd>With this form, packet headers are extracted directly from <i>packet</i>, so the <i>odp_flow</i> or <i>br_flow</i> should specify only metadata. The metadata can be:</p>
<dl>
<dd>
<dl>
<dt><i>skb_priority</i></p>
<dd>Packet QoS priority.</p>
<dt><i>pkt_mark</i></p>
<dd>Mark of the packet.</p>
<dt><i>ct_state</i></p>
<dd>Connection state of the packet.</p>
<dt><i>ct_zone</i></p>
<dd>Connection tracking zone for packet.</p>
<dt><i>ct_mark</i></p>
<dd>Connection mark of the packet.</p>
<dt><i>ct_label</i></p>
<dd>Connection label of the packet.</p>
<dt><i>tun_id</i></p>
<dd>The tunnel ID on which the packet arrived.</p>
<dt><i>in_port</i></p>
<dd>The port on which the packet arrived.</dl>
</dl>
</dl>
</dl>
<dd>The in_port value is kernel datapath port number for the first format and OpenFlow port number for the second format. The numbering of these two types of port usually differs and there is no relationship.</p>
<dd><code>ofproto-trace-packet-out</code> accepts an additional <code>-consistent</code> option. With this option specified, the command rejects <i>actions</i> that are inconsistent with the specified packet. (An example of an inconsistency is attempting to strip the VLAN tag from a packet that does not have a VLAN tag.) Open vSwitch ignores most forms of inconsistency in OpenFlow 1.0 and rejects inconsistencies in later versions of OpenFlow. The option is necessary because the command does not ordinarily imply a particular OpenFlow version. One exception is that, when <i>actions</i> includes an action that only OpenFlow 1.1 and later supports (such as <code>push_vlan</code>), <code>-consistent</code> is automatically enabled.</p>
<dt><code>ofproto/self-check</code> [<i>switch</i>]</p>
<dd>Runs an internal consistency check on <i>switch</i>, if specified, otherwise on all ofproto instances, and responds with a brief summary of the results. If the summary reports any errors, then the Open vSwitch logs should contain more detailed information. Please pass along errors reported by this command to the Open vSwitch developers as bugs.</dl>
<h3>Vlog Commands</h3>
<p>These commands manage <code>ovs-vswitchd</code>&#8216;s logging settings.</p>
<dl>
<dt><code>vlog/set</code> [<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively.</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>ovs-vswitchd</code> was invoked with the <code>&#8211;log-file</code> option.</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>vlog/set PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>vlog/list</code></p>
<dd>Lists the supported logging modules and their current levels.</p>
<dt><code>vlog/list-pattern</code></p>
<dd>Lists logging patterns used for each destination.</p>
<dt><code>vlog/reopen</code></p>
<dd>Causes <code>ovs-vswitchd</code> to close and reopen its log file. (This is useful after rotating log files, to cause a new log file to be used.)</p>
<dd>This has no effect unless <code>ovs-vswitchd</code> was invoked with the <code>&#8211;log-file</code> option.</p>
<dt><code>vlog/disable-rate-limit </code>[<i>module</i>]&#8230;</p>
<dd>
<dt><code>vlog/enable-rate-limit </code>[<i>module</i>]&#8230;</p>
<dd>By default, <code>ovs-vswitchd</code> limits the rate at which certain messages can be logged. When a message would appear more frequently than the limit, it is suppressed. This saves disk space, makes logs easier to read, and speeds up execution, but occasionally troubleshooting requires more detail. Therefore, <code>vlog/disable-rate-limit</code> allows rate limits to be disabled at the level of an individual log module. Specify one or more module names, as displayed by the <code>vlog/list</code> command. Specifying either no module names at all or the keyword <code>any</code> disables rate limits for every log module.</p>
<dd>The <code>vlog/enable-rate-limit</code> command, whose syntax is the same as <code>vlog/disable-rate-limit</code>, can be used to re-enable a rate limit that was previously disabled.</dl>
<h3>Memory Commands</h3>
<p>These commands report memory usage.</p>
<dl>
<dt><code>memory/show</code></p>
<dd>Displays some basic statistics about <code>ovs-vswitchd</code>&#8216;s memory usage. <code>ovs-vswitchd</code> also logs this information soon after startup and periodically as its memory consumption grows.</dl>
<h3>Coverage Commands</h3>
<p>These commands manage <code>ovs-vswitchd</code>&#8216;s &#8220;coverage counters,&#8221; which count the number of times particular events occur during a daemon&#8217;s runtime. In addition to these commands, <code>ovs-vswitchd</code> automatically logs coverage counter values, at <code>INFO</code> level, when it detects that the daemon&#8217;s main loop takes unusually long to run. </p>
<p> Coverage counters are useful mainly for performance analysis and debugging.</p>
<dl>
<dt><code>coverage/show</code></p>
<dd>Displays the averaged per-second rates for the last few seconds, the last minute and the last hour, and the total counts of all of the coverage counters.</dl>
<h3>Openvswitch Tunneling Commands</h3>
<p>These commands query and modify OVS tunnel components. Ref to README-native-tunneling.md for more info.</p>
<dl>
<dt><code>ovs/route/add ipv4_address/plen output_bridge [GW]</code></p>
<dd>Adds ipv4_address/plen route to vswitchd routing table. output_bridge needs to be OVS bridge name. This command is useful if OVS cached routes does not look right.</p>
<dt><code>ovs/route/show</code></p>
<dd>Print all routes in OVS routing table, This includes routes cached from system routing table and user configured routes.</p>
<dt><code>ovs/route/del ipv4_address/plen</code></p>
<dd>Delete ipv4_address/plen route from OVS routing table.</p>
<dt><code>tnl/neigh/show</code></p>
<dd>
<dt><code>tnl/arp/show</code></p>
<dd>OVS builds ARP cache by snooping are messages. This command shows ARP cache table.</p>
<dt><code>tnl/neigh/set </code><i>bridge ip mac</i></p>
<dd>
<dt><code>tnl/arp/set </code><i>bridge ip mac</i></p>
<dd>Adds or modifies an ARP cache entry in <i>bridge</i>, mapping <i>ip</i> to <i>mac</i>.</p>
<dt><code>tnl/neigh/flush</code></p>
<dd>
<dt><code>tnl/arp/flush</code></p>
<dd>Flush ARP table.</p>
<dt><code>tnl/egress_port_range [num1] [num2]</code></p>
<dd>Set range for UDP source port used for UDP based Tunnels. For example VxLAN. If case of zero arguments this command prints current range in use.</dl>
<h2>Openflow Implementation</h2>
<p>This section documents aspects of OpenFlow for which the OpenFlow specification requires documentation.</p>
<h3>Packet buffering.</h3>
<p>The OpenFlow specification, version 1.2, says:</p>
<dl>
<dd>Switches that implement buffering are expected to expose, through documentation, both the amount of available buffering, and the length of time before buffers may be reused.</dl>
<p> Open vSwitch maintains a separate set of 256 packet buffers for each OpenFlow connection. Any given packet buffer is preserved until it is referenced by an <code>OFPT_FLOW_MOD</code> or <code>OFPT_PACKET_OUT</code> request or for 5 seconds, whichever comes first.</p>
<h2>Limits</h2>
<p>We believe these limits to be accurate as of this writing. These limits assume the use of the Linux kernel datapath.</p>
<dl>
<dt>&bull;</p>
<dd><code>ovs-vswitchd</code> started through <code><a href="/docs/linux/man/8-ovs-ctl/">ovs-ctl</a></code>(8) provides a limit of 65535 file descriptors. The limits on the number of bridges and ports is decided by the availability of file descriptors. With the Linux kernel datapath, creation of a single bridge consumes three file descriptors and adding a port consumes &quot;n-handler-threads&quot; file descriptors per bridge port. Performance will degrade beyond 1,024 ports per bridge due to fixed hash table sizing. Other platforms may have different limitations.</p>
<dt>&bull;</p>
<dd>2,048 MAC learning entries per bridge, by default. (This is configurable via <code>other-config:mac-table-size</code> in the <code>Bridge</code> table. See <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5) for details.)</p>
<dt>&bull;</p>
<dd>Kernel flows are limited only by memory available to the kernel. Performance will degrade beyond 1,048,576 kernel flows per bridge with a 32-bit kernel, beyond 262,144 with a 64-bit kernel. (<code>ovs-vswitchd</code> should never install anywhere near that many flows.)</p>
<dt>&bull;</p>
<dd>OpenFlow flows are limited only by available memory. Performance is linear in the number of unique wildcard patterns. That is, an OpenFlow table that contains many flows that all match on the same fields in the same way has a constant-time lookup, but a table that contains many flows that match on different fields requires lookup time linear in the number of flows.</p>
<dt>&bull;</p>
<dd>255 ports per bridge participating in 802.1D Spanning Tree Protocol.</p>
<dt>&bull;</p>
<dd>32 mirrors per bridge.</p>
<dt>&bull;</p>
<dd>15 bytes for the name of a port. (This is a Linux kernel limitation.)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), <code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1), <code>INSTALL.Linux</code> in the Open vSwitch distribution. </p>
