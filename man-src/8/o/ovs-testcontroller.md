---
title: "ovs-testcontroller(8)"
name: "ovs-testcontroller"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-testcontroller/"
description: "ovs-testcontroller – simple OpenFlow controller for testing"
---

<p>ovs-testcontroller &#8211; simple OpenFlow controller for testing</p>
<h2>Synopsis</h2>
<p><code>ovs-testcontroller</code> [<i>options</i>] <i>method</i> <code>[</code><i>method</i>]&#8230;</p>
<h2>Description</h2>
<p><code>ovs-testcontroller</code> is a simple OpenFlow controller that manages any number of switches over the OpenFlow protocol, causing them to function as L2 MAC-learning switches or hubs. It is suitable for initial testing of OpenFlow networks. It is not a necessary or desirable part of a production OpenFlow deployment. </p>
<p> <code>ovs-testcontroller</code> controls one or more OpenFlow switches, specified as one or more of the following OpenFlow connection methods:</p>
<dl>
<dd>
<dl>
<dt><code>pssl:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>
<dt><code>ptcp:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for OpenFlow connections on <i>port</i>. The default <i>port</i> is 6653. By default, connections are allowed from any IPv4 address. Specify <i>ip</i> as an IPv4 address or a bracketed IPv6 address (e.g. <code>ptcp:6653:[::1]</code>). DNS names may not be used. For <code>pssl</code>, the <code>&#8211;private-key</code>,<code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory.</p>
<dd>
<dt><code>punix:</code><i>file</i></p>
<dd>Listens for OpenFlow connections on the Unix domain server socket named <i>file</i>.</p>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. Wrap IPv6 addresses in square brackets, e.g. <code>tcp:[::1]:6653</code>. For <code>ssl</code>, the <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory.</p>
<dd>If <i>port</i> is not specified, it defaults to 6653.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, a Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, a localhost TCP port written in <i>file</i>.</dl>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;noflow</code></p>
<dd>By default, <code>ovs-testcontroller</code> sets up a flow in each OpenFlow switch whenever it receives a packet whose destination is known due through MAC learning. This option disables flow setup, so that every packet in the network passes through the controller.</p>
<dd>This option is most useful for debugging. It reduces switching performance, so it should not be used in production.</p>
<dt><code>&#8211;max-idle=</code><i>secs</i>|<code>permanent</code></p>
<dd>Sets <i>secs</i> as the number of seconds that a flow set up by the controller will remain in the switch&#8217;s flow table without any matching packets being seen. If <code>permanent</code> is specified, which is not recommended, flows will never expire. The default is 60 seconds.</p>
<dd>This option has no effect when <code>-n</code> (or <code>&#8211;noflow</code>) is in use (because the controller does not set up flows in that case).</p>
<dt><code>-H</code></p>
<dd>
<dt><code>&#8211;hub</code></p>
<dd>By default, the controller acts as an L2 MAC-learning switch. This option changes its behavior to that of a hub that floods packets on all but the incoming port.</p>
<dd>If <code>-H</code> (or <code>&#8211;hub</code>) and <code>-n</code> (or <code>&#8211;noflow</code>) are used together, then the cumulative effect is that every packet passes through the controller and every packet is flooded.</p>
<dd>This option is most useful for debugging. It reduces switching performance, so it should not be used in production.</p>
<dt><code>-w</code>[<i>wildcard_mask</i>]</p>
<dd>
<dt><code>&#8211;wildcards</code>[<code>=</code><i>wildcard_mask</i>]</p>
<dd>By default, <code>ovs-testcontroller</code> sets up exact-match flows. This option allows it to set up wildcarded flows, which may reduce flow setup latency by causing less traffic to be sent up to the controller.</p>
<dd>The optional <i>wildcard_mask</i> is an OpenFlow wildcard bitmask in hexadecimal that specifies the fields to wildcard. If no <i>wildcard_mask</i> is specified, the default value 0x2820F0 is used which specifies L2-only switching and wildcards L3 and L4 fields. Another interesting value is 0x2000EC, which specifies L3-only switching and wildcards L2 and L4 fields.</p>
<dd>This option has no effect when <code>-n</code> (or <code>&#8211;noflow</code>) is in use (because the controller does not set up flows in that case).</p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;normal</code></p>
<dd>By default, <code>ovs-testcontroller</code> directs packets to a particular port or floods them. This option causes it to direct non-flooded packets to the OpenFlow <code>OFPP_NORMAL</code> port. This allows the switch itself to make decisions about packet destinations. Support for <code>OFPP_NORMAL</code> is optional in OpenFlow, so this option may not well with some non-Open vSwitch switches.</p>
<dt><code>&#8211;mute</code></p>
<dd>Prevents ovs-testcontroller from replying to any OpenFlow messages sent to it by switches.</p>
<dd>This option is only for debugging the Open vSwitch implementation of &#8220;fail open&#8221; mode. It must not be used in production.</p>
<dt><code>-q </code><i>id</i></p>
<dd>
<dt><code>&#8211;queue=</code><i>id</i></p>
<dd>By default, <code>ovs-testcontroller</code> uses the default OpenFlow queue for sending packets and setting up flows. Use one of these options, supplying <i>id</i> as an OpenFlow queue ID as a decimal number, to instead use that specific queue.</p>
<dd>This option is incompatible with <code>-N</code> or <code>&#8211;normal</code> and with <code>-H</code> or <code>&#8211;hub</code>. If more than one is specified then this option takes precedence.</p>
<dd>This option may be useful for testing or debugging quality of service setups.</p>
<dt><code>-Q </code><i>port-name</i><code>:</code><i>queue-id</i></p>
<dd>
<dt><code>&#8211;port-queue </code><i>port-name</i><code>:</code><i>queue-id</i></p>
<dd>Configures packets received on the port named <i>port-name</i> (e.g. <code>eth0</code>) to be output on OpenFlow queue ID <i>queue-id</i> (specified as a decimal number). For the specified port, this option overrides the default specified on <code>-q</code> or <code>&#8211;queue</code>.</p>
<dd>This option may be specified any number of times with different <i>port-name</i> arguments.</p>
<dd>This option is incompatible with <code>-N</code> or <code>&#8211;normal</code> and with <code>-H</code> or <code>&#8211;hub</code>. If more than one is specified then this option takes precedence.</p>
<dd>This option may be useful for testing or debugging quality of service setups.</p>
<dt><code>&#8211;with-flows </code><i>file</i></p>
<dd>When a switch connects, push the flow entries as described in <i>file</i>. Each line in <i>file</i> is a flow entry in the format described for the <code>add-flows</code> command in the <code>Flow Syntax</code> section of the <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8) man page.</p>
<dd>Use this option more than once to add flows from multiple files.</dl>
<h3>Public Key Infrastructure Options</h3>
<dl>
<dt><code>-p</code> <i>privkey.pem</i></p>
<dd>
<dt><code>&#8211;private-key=</code><i>privkey.pem</i></p>
<dd>Specifies a PEM file containing the private key used as <code>ovs-testcontroller</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd>Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd>Specifies a PEM file containing the CA certificate that <code>ovs-testcontroller</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd>Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>&#8211;peer-ca-cert=</code><i>peer-cacert.pem</i></p>
<dd>Specifies a PEM file that contains one or more additional certificates to send to SSL peers. <i>peer-cacert.pem</i> should be the CA certificate used to sign <code>ovs-testcontroller</code>&#8216;s own certificate, that is, the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>. If <code>ovs-testcontroller</code>&#8216;s certificate is self-signed, then <code>&#8211;certificate</code> and <code>&#8211;peer-ca-cert</code> should specify the same file.</p>
<dd>This option is not useful in normal operation, because the SSL peer must already have the CA certificate for the peer to have any confidence in <code>ovs-testcontroller</code>&#8216;s identity. However, this offers a way for a new installation to bootstrap the CA certificate on its first SSL connection. The following options are valid on POSIX based platforms.</p>
<dt><code>&#8211;pidfile</code>[<code>=</code><i>pidfile</i>]</p>
<dd>Causes a file (by default, <code>ovs-testcontroller.pid</code>) to be created indicating the PID of the running process. If the <i>pidfile</i> argument is not specified, or if it does not begin with <code>/</code>, then it is created in <code>/var/run/openvswitch</code>.</p>
<dd>If <code>&#8211;pidfile</code> is not specified, no pidfile is created.</p>
<dt><code>&#8211;overwrite-pidfile</code></p>
<dd>By default, when <code>&#8211;pidfile</code> is specified and the specified pidfile already exists and is locked by a running process, <code>ovs-testcontroller</code> refuses to start. Specify <code>&#8211;overwrite-pidfile</code> to cause it to instead overwrite the pidfile.</p>
<dd>When <code>&#8211;pidfile</code> is not specified, this option has no effect.</p>
<dt><code>&#8211;detach</code></p>
<dd>Runs <code>ovs-testcontroller</code> as a background process. The process forks, and in the child it starts a new session, closes the standard file descriptors (which has the side effect of disabling logging to the console), and changes its current directory to the root (unless <code>&#8211;no-chdir</code> is specified). After the child completes its initialization, the parent exits.</p>
<dt><code>&#8211;monitor</code></p>
<dd>Creates an additional process to monitor the <code>ovs-testcontroller</code> daemon. If the daemon dies due to a signal that indicates a programming error (<code>SIGABRT</code>, <code>SIGALRM</code>, <code>SIGBUS</code>, <code>SIGFPE</code>, <code>SIGILL</code>, <code>SIGPIPE</code>, <code>SIGSEGV</code>, <code>SIGXCPU</code>, or <code>SIGXFSZ</code>) then the monitor process starts a new copy of it. If the daemon dies or exits for another reason, the monitor process exits.</p>
<dd>This option is normally used with <code>&#8211;detach</code>, but it also functions without it.</p>
<dt><code>&#8211;no-chdir</code></p>
<dd>By default, when <code>&#8211;detach</code> is specified, <code>ovs-testcontroller</code> changes its current working directory to the root directory after it detaches. Otherwise, invoking <code>ovs-testcontroller</code> from a carelessly chosen directory would prevent the administrator from unmounting the file system that holds that directory.</p>
<dd>Specifying <code>&#8211;no-chdir</code> suppresses this behavior, preventing <code>ovs-testcontroller</code> from changing its current working directory. This may be useful for collecting core files, since it is common behavior to write core dumps into the current working directory and the root directory is not a good directory to use.</p>
<dd>This option has no effect when <code>&#8211;detach</code> is not specified.</p>
<dt><code>&#8211;user</code></p>
<dd>Causes <code>ovs-testcontroller</code> to run as a different user specified in &quot;user:group&quot;, thus dropping most of the root privileges. Short forms &quot;user&quot; and &quot;:group&quot; are also allowed, with current user or group are assumed respectively. Only daemons started by the root user accepts this argument.</p>
<dd>On Linux, daemons will be granted CAP_IPC_LOCK and CAP_NET_BIND_SERVICES before dropping root privileges. Daemons interact with datapath, such as ovs-vswitchd, will be granted two additional capabilities, namely CAP_NET_ADMIN and CAP_NET_RAW. The capability change will apply even if new user is &quot;root&quot;.</p>
<dd>On Windows, this option is not currently supported. For security reasons, specifying this option will cause the daemon process not to start.</p>
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
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovs-testcontroller</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
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
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovs-testcontroller.log</code>.</p>
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
<dt><code>&#8211;unixctl=</code><i>socket</i></p>
<dd>Sets the name of the control socket on which <code>ovs-testcontroller</code> listens for runtime management commands (see <code>RUNTIME MANAGEMENT COMMANDS</code>, below). If <i>socket</i> does not begin with <code>/</code>, it is interpreted as relative to <code>/var/run/openvswitch</code>. If <code>&#8211;unixctl</code> is not used at all, the default socket is <code>/var/run/openvswitch/ovs-testcontroller.</code><i>pid</i><code>.ctl</code>, where <i>pid</i> is <code>ovs-testcontroller</code>&#8216;s process ID.</p>
<dd>On Windows, uses a kernel chosen TCP port on the localhost to listen for runtime management commands. The kernel chosen TCP port value is written in a file whose absolute path is pointed by <i>socket</i>. If <code>&#8211;unixctl</code> is not used at all, the file is created as <code>ovs-testcontroller.ctl</code> in the configured <i>OVS_RUNDIR</i> directory.</p>
<dd>Specifying <code>none</code> for <i>socket</i> disables the control socket feature.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</p>
<dt><code>-O </code>[<i>version</i>[<code>,</code><i>version</i>]&#8230;]</p>
<dd>
<dt><code>&#8211;protocols=</code>[<i>version</i>[<code>,</code><i>version</i>]&#8230;]</p>
<dd>Sets the OpenFlow protocol versions that are allowed when establishing an OpenFlow session.</p>
<dd>The following versions are considered to be ready for general use. These protocol versions are enabled by default:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>OpenFlow10</code>, for OpenFlow 1.0.</dl>
</dl>
<dd>Support for the following protocol versions is provided for testing and development purposes. They are not enabled by default:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>OpenFlow11</code>, for OpenFlow 1.1.</p>
<dt>&bull;</p>
<dd><code>OpenFlow12</code>, for OpenFlow 1.2.</p>
<dt>&bull;</p>
<dd><code>OpenFlow13</code>, for OpenFlow 1.3.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>To bind locally to port 6653 (the default) and wait for incoming connections from OpenFlow switches:</p>
<dl>
<dd><code>% ovs-testcontroller ptcp:</code></dl>
<h2>Bugs</h2>
<p>Configuring a Citrix XenServer to connect to a particular controller only points the remote OVSDB management connection to that controller. It does not also configure OpenFlow connections, because the manager is expected to do that over the management protocol. <code>ovs-testcontroller</code> is not an Open vSwitch manager and does not know how to do that. </p>
<p> As a stopgap workaround, <code>ovs-vsctl</code> can wait for an OVSDB connection and set the controller, e.g.:</p>
<dl>
<dd><code>% ovs-vsctl -t0 &#8211;db=pssl: &#8211;certificate=cert.pem &#8211;ca-cert=none &#8211;private-key=privkey.pem &#8211;peer-ca-cert=cacert.pem set-controller ssl:</code><i>ip</i></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8), <code><a href="/docs/linux/man/8-ovs-dpctl/">ovs-dpctl</a></code>(8) </p>
