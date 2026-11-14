---
title: "systemd-socket(5)"
name: "systemd-socket"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-socket/"
description: "systemd.socket – Socket unit configuration"
---

<p>systemd.socket &#8211; Socket unit configuration</p>
<h2>Synopsis</h2>
<p><i>socket</i>.socket</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.socket&quot; encodes information about an IPC or network socket or a file system FIFO controlled and supervised by systemd, for socket-based activation. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The socket specific configuration options are configured in the [Socket] section. </p>
<p> Additional options are listed in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), which define the execution environment the <code>ExecStartPre=</code>, <code>ExecStartPost=</code>, <code>ExecStopPre=</code> and <code>ExecStopPost=</code> commands are executed in, and in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), which define the way the processes are terminated, and in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), which configure resource control settings for the processes of the socket. </p>
<p> For each socket unit, a matching service unit must exist, describing the service to start on incoming traffic on the socket (see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for more information about .service units). The name of the .service unit is by default the same as the name of the .socket unit, but can be altered with the <code>Service=</code> option described below. Depending on the setting of the <code>Accept=</code> option described below, this .service unit must either be named like the .socket unit, but with the suffix replaced, unless overridden with <code>Service=</code>; or it must be a template unit named the same way. Example: a socket file foo.socket needs a matching service foo.service if <code>Accept=no</code> is set. If <code>Accept=yes</code> is set, a service template foo [at] .service must exist from which services are instantiated for each incoming connection. </p>
<p> No implicit <i>WantedBy=</i> or <i>RequiredBy=</i> dependency from the socket to the service is added. This means that the service may be started without the socket, in which case it must be able to open sockets by itself. To prevent this, an explicit <i>Requires=</i> dependency may be added. </p>
<p> Socket units may be used to implement on-demand starting of services, as well as parallelized starting of services. See the blog stories linked at the end for an introduction. </p>
<p> Note that the daemon software configured for socket activation with socket units needs to be able to accept sockets from systemd, either via systemd&#8217;s native socket passing interface (see <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3) for details about the precise protocol used and the order in which the file descriptors are passed) or via traditional <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8)-style socket passing (i.e. sockets passed in via standard input and output, using <i>StandardInput=socket</i> in the service file). </p>
<p> All network sockets allocated through .socket units are allocated in the host&#8217;s network namespace (see <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7)). This does not mean however that the service activated by a configured socket unit has to be part of the host&#8217;s network namespace as well. It is supported and even good practice to run services in their own network namespace (for example through <i>PrivateNetwork=</i>, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)), receiving only the sockets configured through socket-activation from the host&#8217;s namespace. In such a set-up communication within the host&#8217;s network namespace is only permitted through the activation sockets passed in while all sockets allocated from the service code itself will be associated with the service&#8217;s own namespace, and thus possibly subject to a restrictive configuration.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; Socket units automatically gain a <i>Before=</i> dependency on the service units they activate.</dl>
<dl>
<dd>&bull; Socket units referring to file system paths (such as <code>AF_UNIX</code> sockets or FIFOs) implicitly gain <i>Requires=</i> and <i>After=</i> dependencies on all mount units necessary to access those paths.</dl>
<dl>
<dd>&bull; Socket units using the <i>BindToDevice=</i> setting automatically gain a <i>BindsTo=</i> and <i>After=</i> dependency on the device unit encapsulating the specified network interface.</dl>
<p> Additional implicit dependencies may be added as result of execution and resource control parameters as documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</p>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Socket units automatically gain a <i>Before=</i> dependency on sockets.target.</dl>
<dl>
<dd>&bull; Socket units automatically gain a pair of <i>After=</i> and <i>Requires=</i> dependency on sysinit.target, and a pair of <i>Before=</i> and <i>Conflicts=</i> dependencies on shutdown.target. These dependencies ensure that the socket unit is started before normal services at boot, and is stopped on shutdown. Only sockets involved with early boot or late system shutdown should disable <i>DefaultDependencies=</i> option.</dl>
<h2>Options</h2>
<p>Socket files must include a [Socket] section, which carries information about the socket or FIFO it supervises. A number of options that may be used in this section are shared with other unit types. These options are documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5). The options specific to the [Socket] section of socket units are the following: </p>
<p> <i>ListenStream=</i>, <i>ListenDatagram=</i>, <i>ListenSequentialPacket=</i></p>
<dl>
<dd>Specifies an address to listen on for a stream (<code>SOCK_STREAM</code>), datagram (<code>SOCK_DGRAM</code>), or sequential packet (<code>SOCK_SEQPACKET</code>) socket, respectively. The address can be written in various formats: </p>
<p> If the address starts with a slash (&quot;/&quot;), it is read as file system socket in the <code>AF_UNIX</code> socket family. </p>
<p> If the address starts with an at symbol (&quot;@&quot;), it is read as abstract namespace socket in the <code>AF_UNIX</code> family. The &quot;@&quot; is replaced with a <code>NUL</code> character before binding. For details, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7). </p>
<p> If the address string is a single number, it is read as port number to listen on via IPv6. Depending on the value of <i>BindIPv6Only=</i> (see below) this might result in the service being available via both IPv6 and IPv4 (default) or just via IPv6. </p>
<p> If the address string is a string in the format &quot;<i>v.w.x.y</i>:<i>z</i>&quot;, it is interpreted as IPv4 address <i>v.w.x.y</i> and port <i>z</i>. </p>
<p> If the address string is a string in the format &quot;[<i>x</i>]:<i>y</i>&quot;, it is interpreted as IPv6 address <i>x</i> and port <i>y</i>. An optional interface scope (interface name or number) may be specified after a &quot;%&quot; symbol: &quot;[<i>x</i>]:<i>y</i>%<i>dev</i>&quot;. Interface scopes are only useful with link-local addresses, because the kernel ignores them in other cases. Note that if an address is specified as IPv6, it might still make the service available via IPv4 too, depending on the <i>BindIPv6Only=</i> setting (see below). </p>
<p> If the address string is a string in the format &quot;vsock:<i>x</i>:<i>y</i>&quot;, it is read as CID <i>x</i> on a port <i>y</i> address in the <code>AF_VSOCK</code> family. The CID is a unique 32-bit integer identifier in <code>AF_VSOCK</code> analogous to an IP address. Specifying the CID is optional, and may be set to the empty string. </p>
<p> Note that <code>SOCK_SEQPACKET</code> (i.e. <i>ListenSequentialPacket=</i>) is only available for <code>AF_UNIX</code> sockets. <code>SOCK_STREAM</code> (i.e. <i>ListenStream=</i>) when used for IP sockets refers to TCP sockets, <code>SOCK_DGRAM</code> (i.e. <i>ListenDatagram=</i>) to UDP. </p>
<p> These options may be specified more than once, in which case incoming traffic on any of the sockets will trigger service activation, and all listed sockets will be passed to the service, regardless of whether there is incoming traffic on them or not. If the empty string is assigned to any of these options, the list of addresses to listen on is reset, all prior uses of any of these options will have no effect. </p>
<p> It is also possible to have more than one socket unit for the same service when using <i>Service=</i>, and the service will receive all the sockets configured in all the socket units. Sockets configured in one unit are passed in the order of configuration, but no ordering between socket units is specified. </p>
<p> If an IP address is used here, it is often desirable to listen on it before the interface it is configured on is up and running, and even regardless of whether it will be up and running at any point. To deal with this, it is recommended to set the <i>FreeBind=</i> option described below.</dl>
<p> <i>ListenFIFO=</i></p>
<dl>
<dd>Specifies a file system FIFO (see <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7) for details) to listen on. This expects an absolute file system path as argument. Behavior otherwise is very similar to the <i>ListenDatagram=</i> directive above.</dl>
<p> <i>ListenSpecial=</i></p>
<dl>
<dd>Specifies a special file in the file system to listen on. This expects an absolute file system path as argument. Behavior otherwise is very similar to the <i>ListenFIFO=</i> directive above. Use this to open character device nodes as well as special files in /proc/ and /sys/.</dl>
<p> <i>ListenNetlink=</i></p>
<dl>
<dd>Specifies a Netlink family to create a socket for to listen on. This expects a short string referring to the <code>AF_NETLINK</code> family name (such as <i>audit</i> or <i>kobject-uevent</i>) as argument, optionally suffixed by a whitespace followed by a multicast group integer. Behavior otherwise is very similar to the <i>ListenDatagram=</i> directive above.</dl>
<p> <i>ListenMessageQueue=</i></p>
<dl>
<dd>Specifies a POSIX message queue name to listen on (see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7) for details). This expects a valid message queue name (i.e. beginning with &quot;/&quot;). Behavior otherwise is very similar to the <i>ListenFIFO=</i> directive above. On Linux message queue descriptors are actually file descriptors and can be inherited between processes.</dl>
<p> <i>ListenUSBFunction=</i></p>
<dl>
<dd>Specifies a m[blue]<code>USB FunctionFS</code>m[]<font SIZE="-2">[1]</font> endpoints location to listen on, for implementation of USB gadget functions. This expects an absolute file system path of a FunctionFS mount point as the argument. Behavior otherwise is very similar to the <i>ListenFIFO=</i> directive above. Use this to open the FunctionFS endpoint ep0. When using this option, the activated service has to have the <i>USBFunctionDescriptors=</i> and <i>USBFunctionStrings=</i> options set.</dl>
<p> <i>SocketProtocol=</i></p>
<dl>
<dd>Takes one of <code>udplite</code> or <code>sctp</code>. The socket will use the UDP-Lite (<code>IPPROTO_UDPLITE</code>) or SCTP (<code>IPPROTO_SCTP</code>) protocol, respectively.</dl>
<p> <i>BindIPv6Only=</i></p>
<dl>
<dd>Takes one of <code>default</code>, <code>both</code> or <code>ipv6-only</code>. Controls the IPV6_V6ONLY socket option (see <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7) for details). If <code>both</code>, IPv6 sockets bound will be accessible via both IPv4 and IPv6. If <code>ipv6-only</code>, they will be accessible via IPv6 only. If <code>default</code> (which is the default, surprise!), the system wide default setting is used, as controlled by /proc/sys/net/ipv6/bindv6only, which in turn defaults to the equivalent of <code>both</code>.</dl>
<p> <i>Backlog=</i></p>
<dl>
<dd>Takes an unsigned integer argument. Specifies the number of connections to queue that have not been accepted yet. This setting matters only for stream and sequential packet sockets. See <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) for details. Defaults to SOMAXCONN (128).</dl>
<p> <i>BindToDevice=</i></p>
<dl>
<dd>Specifies a network interface name to bind this socket to. If set, traffic will only be accepted from the specified network interfaces. This controls the <code>SO_BINDTODEVICE</code> socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details). If this option is used, an implicit dependency from this socket unit on the network interface device unit is created (see <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5)). Note that setting this parameter might result in additional dependencies to be added to the unit (see above).</dl>
<p> <i>SocketUser=</i>, <i>SocketGroup=</i></p>
<dl>
<dd>Takes a UNIX user/group name. When specified, all <code>AF_UNIX</code> sockets and FIFO nodes in the file system are owned by the specified user and group. If unset (the default), the nodes are owned by the root user/group (if run in system context) or the invoking user/group (if run in user context). If only a user is specified but no group, then the group is derived from the user&#8217;s default group.</dl>
<p> <i>SocketMode=</i></p>
<dl>
<dd>If listening on a file system socket or FIFO, this option specifies the file system access mode used when creating the file node. Takes an access mode in octal notation. Defaults to 0666.</dl>
<p> <i>DirectoryMode=</i></p>
<dl>
<dd>If listening on a file system socket or FIFO, the parent directories are automatically created if needed. This option specifies the file system access mode used when creating these directories. Takes an access mode in octal notation. Defaults to 0755.</dl>
<p> <i>Accept=</i></p>
<dl>
<dd>Takes a boolean argument. If yes, a service instance is spawned for each incoming connection and only the connection socket is passed to it. If no, all listening sockets themselves are passed to the started service unit, and only one service unit is spawned for all connections (also see above). This value is ignored for datagram sockets and FIFOs where a single service unit unconditionally handles all incoming traffic. Defaults to <code>no</code>. For performance reasons, it is recommended to write new daemons only in a way that is suitable for <code>Accept=no</code>. A daemon listening on an <code>AF_UNIX</code> socket may, but does not need to, call <code><a href="/docs/linux/man/2-close/">close</a></code>(2) on the received socket before exiting. However, it must not unlink the socket from a file system. It should not invoke <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) on sockets it got with <i>Accept=no</i>, but it may do so for sockets it got with <i>Accept=yes</i> set. Setting <i>Accept=yes</i> is mostly useful to allow daemons designed for usage with <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) to work unmodified with systemd socket activation. </p>
<p> For IPv4 and IPv6 connections, the <i>REMOTE_ADDR</i> environment variable will contain the remote IP address, and <i>REMOTE_PORT</i> will contain the remote port. This is the same as the format used by CGI. For <code>SOCK_RAW</code>, the port is the IP protocol.</dl>
<p> <i>Writable=</i></p>
<dl>
<dd>Takes a boolean argument. May only be used in conjunction with <i>ListenSpecial=</i>. If true, the specified special file is opened in read-write mode, if false, in read-only mode. Defaults to false.</dl>
<p> <i>FlushPending=</i></p>
<dl>
<dd>Takes a boolean argument. May only be used when <code>Accept=no</code>. If yes, the socket&#8217;s buffers are cleared after the triggered service exited. This causes any pending data to be flushed and any pending incoming connections to be rejected. If no, the socket&#8217;s buffers won&#8217;t be cleared, permitting the service to handle any pending connections after restart, which is the usually expected behaviour. Defaults to <code>no</code>.</dl>
<p> <i>MaxConnections=</i></p>
<dl>
<dd>The maximum number of connections to simultaneously run services instances for, when <code>Accept=yes</code> is set. If more concurrent connections are coming in, they will be refused until at least one existing connection is terminated. This setting has no effect on sockets configured with <code>Accept=no</code> or datagram sockets. Defaults to 64.</dl>
<p> <i>MaxConnectionsPerSource=</i></p>
<dl>
<dd>The maximum number of connections for a service per source IP address. This is very similar to the <i>MaxConnections=</i> directive above. Disabled by default.</dl>
<p> <i>KeepAlive=</i></p>
<dl>
<dd>Takes a boolean argument. If true, the TCP/IP stack will send a keep alive message after 2h (depending on the configuration of /proc/sys/net/ipv4/tcp_keepalive_time) for all TCP streams accepted on this socket. This controls the <code>SO_KEEPALIVE</code> socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and the m[blue]<code>TCP Keepalive HOWTO</code>m[]<font SIZE="-2">[2]</font> for details.) Defaults to <code>false</code>.</dl>
<p> <i>KeepAliveTimeSec=</i></p>
<dl>
<dd>Takes time (in seconds) as argument. The connection needs to remain idle before TCP starts sending keepalive probes. This controls the TCP_KEEPIDLE socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and the m[blue]<code>TCP Keepalive HOWTO</code>m[]<font SIZE="-2">[2]</font> for details.) Defaults value is 7200 seconds (2 hours).</dl>
<p> <i>KeepAliveIntervalSec=</i></p>
<dl>
<dd>Takes time (in seconds) as argument between individual keepalive probes, if the socket option <code>SO_KEEPALIVE</code> has been set on this socket. This controls the <code>TCP_KEEPINTVL</code> socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and the m[blue]<code>TCP Keepalive HOWTO</code>m[]<font SIZE="-2">[2]</font> for details.) Defaults value is 75 seconds.</dl>
<p> <i>KeepAliveProbes=</i></p>
<dl>
<dd>Takes an integer as argument. It is the number of unacknowledged probes to send before considering the connection dead and notifying the application layer. This controls the TCP_KEEPCNT socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and the m[blue]<code>TCP Keepalive HOWTO</code>m[]<font SIZE="-2">[2]</font> for details.) Defaults value is 9.</dl>
<p> <i>NoDelay=</i></p>
<dl>
<dd>Takes a boolean argument. TCP Nagle&#8217;s algorithm works by combining a number of small outgoing messages, and sending them all at once. This controls the TCP_NODELAY socket option (see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)). Defaults to <code>false</code>.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>Takes an integer argument controlling the priority for all traffic sent from this socket. This controls the <code>SO_PRIORITY</code> socket option (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details.).</dl>
<p> <i>DeferAcceptSec=</i></p>
<dl>
<dd>Takes time (in seconds) as argument. If set, the listening process will be awakened only when data arrives on the socket, and not immediately when connection is established. When this option is set, the <code>TCP_DEFER_ACCEPT</code> socket option will be used (see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)), and the kernel will ignore initial ACK packets without any data. The argument specifies the approximate amount of time the kernel should wait for incoming data before falling back to the normal behavior of honoring empty ACK packets. This option is beneficial for protocols where the client sends the data first (e.g. HTTP, in contrast to SMTP), because the server process will not be woken up unnecessarily before it can take any action. </p>
<p> If the client also uses the <code>TCP_DEFER_ACCEPT</code> option, the latency of the initial connection may be reduced, because the kernel will send data in the final packet establishing the connection (the third packet in the &quot;three-way handshake&quot;). </p>
<p> Disabled by default.</dl>
<p> <i>ReceiveBuffer=</i>, <i>SendBuffer=</i></p>
<dl>
<dd>Takes an integer argument controlling the receive or send buffer sizes of this socket, respectively. This controls the <code>SO_RCVBUF</code> and <code>SO_SNDBUF</code> socket options (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details.). The usual suffixes K, M, G are supported and are understood to the base of 1024.</dl>
<p> <i>IPTOS=</i></p>
<dl>
<dd>Takes an integer argument controlling the IP Type-Of-Service field for packets generated from this socket. This controls the <code>IP_TOS</code> socket option (see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) for details.). Either a numeric string or one of <code>low-delay</code>, <code>throughput</code>, <code>reliability</code> or <code>low-cost</code> may be specified.</dl>
<p> <i>IPTTL=</i></p>
<dl>
<dd>Takes an integer argument controlling the IPv4 Time-To-Live/IPv6 Hop-Count field for packets generated from this socket. This sets the <code>IP_TTL</code>/<code>IPV6_UNICAST_HOPS</code> socket options (see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) and <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7) for details.)</dl>
<p> <i>Mark=</i></p>
<dl>
<dd>Takes an integer value. Controls the firewall mark of packets generated by this socket. This can be used in the firewall logic to filter packets from this socket. This sets the <code>SO_MARK</code> socket option. See <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) for details.</dl>
<p> <i>ReusePort=</i></p>
<dl>
<dd>Takes a boolean value. If true, allows multiple <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)s to this TCP or UDP port. This controls the <code>SO_REUSEPORT</code> socket option. See <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details.</dl>
<p> <i>SmackLabel=</i>, <i>SmackLabelIPIn=</i>, <i>SmackLabelIPOut=</i></p>
<dl>
<dd>Takes a string value. Controls the extended attributes &quot;security.SMACK64&quot;, &quot;security.SMACK64IPIN&quot; and &quot;security.SMACK64IPOUT&quot;, respectively, i.e. the security label of the FIFO, or the security label for the incoming or outgoing connections of the socket, respectively. See m[blue]<code>Smack.txt</code>m[]<font SIZE="-2">[3]</font> for details.</dl>
<p> <i>SELinuxContextFromNet=</i></p>
<dl>
<dd>Takes a boolean argument. When true, systemd will attempt to figure out the SELinux label used for the instantiated service from the information handed by the peer over the network. Note that only the security level is used from the information provided by the peer. Other parts of the resulting SELinux context originate from either the target binary that is effectively triggered by socket unit or from the value of the <i>SELinuxContext=</i> option. This configuration option applies only when activated service is passed in single socket file descriptor, i.e. service instances that have standard input connected to a socket or services triggered by exactly one socket unit. Also note that this option is useful only when MLS/MCS SELinux policy is deployed. Defaults to &quot;false&quot;.</dl>
<p> <i>PipeSize=</i></p>
<dl>
<dd>Takes a size in bytes. Controls the pipe buffer size of FIFOs configured in this socket unit. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for details. The usual suffixes K, M, G are supported and are understood to the base of 1024.</dl>
<p> <i>MessageQueueMaxMessages=</i>, <i>MessageQueueMessageSize=</i></p>
<dl>
<dd>These two settings take integer values and control the mq_maxmsg field or the mq_msgsize field, respectively, when creating the message queue. Note that either none or both of these variables need to be set. See <code><a href="/docs/linux/man/3-mq_setattr/">mq_setattr</a></code>(3) for details.</dl>
<p> <i>FreeBind=</i></p>
<dl>
<dd>Takes a boolean value. Controls whether the socket can be bound to non-local IP addresses. This is useful to configure sockets listening on specific IP addresses before those IP addresses are successfully configured on a network interface. This sets the <code>IP_FREEBIND</code>/<code>IPV6_FREEBIND</code> socket option. For robustness reasons it is recommended to use this option whenever you bind a socket to a specific IP address. Defaults to <code>false</code>.</dl>
<p> <i>Transparent=</i></p>
<dl>
<dd>Takes a boolean value. Controls the <code>IP_TRANSPARENT</code>/<code>IPV6_TRANSPARENT</code> socket option. Defaults to <code>false</code>.</dl>
<p> <i>Broadcast=</i></p>
<dl>
<dd>Takes a boolean value. This controls the <code>SO_BROADCAST</code> socket option, which allows broadcast datagrams to be sent from this socket. Defaults to <code>false</code>.</dl>
<p> <i>PassCredentials=</i></p>
<dl>
<dd>Takes a boolean value. This controls the <code>SO_PASSCRED</code> socket option, which allows <code>AF_UNIX</code> sockets to receive the credentials of the sending process in an ancillary message. Defaults to <code>false</code>.</dl>
<p> <i>PassSecurity=</i></p>
<dl>
<dd>Takes a boolean value. This controls the <code>SO_PASSSEC</code> socket option, which allows <code>AF_UNIX</code> sockets to receive the security context of the sending process in an ancillary message. Defaults to <code>false</code>.</dl>
<p> <i>PassPacketInfo=</i></p>
<dl>
<dd>Takes a boolean value. This controls the <code>IP_PKTINFO</code>, <code>IPV6_RECVPKTINFO</code>, <code>NETLINK_PKTINFO</code> or <code>PACKET_AUXDATA</code> socket options, which enable reception of additional per-packet metadata as ancillary message, on <code>AF_INET</code>, <code>AF_INET6</code>, <code>AF_UNIX</code> and <code>AF_PACKET</code> sockets. Defaults to <code>false</code>.</dl>
<p> <i>Timestamping=</i></p>
<dl>
<dd>Takes one of &quot;off&quot;, &quot;us&quot; (alias: &quot;usec&quot;, &quot;&micro;s&quot;) or &quot;ns&quot; (alias: &quot;nsec&quot;). This controls the <code>SO_TIMESTAMP</code> or <code>SO_TIMESTAMPNS</code> socket options, and enables whether ingress network traffic shall carry timestamping metadata. Defaults to <code>off</code>.</dl>
<p> <i>TCPCongestion=</i></p>
<dl>
<dd>Takes a string value. Controls the TCP congestion algorithm used by this socket. Should be one of &quot;westwood&quot;, &quot;veno&quot;, &quot;cubic&quot;, &quot;lp&quot; or any other available algorithm supported by the IP stack. This setting applies only to stream sockets.</dl>
<p> <i>ExecStartPre=</i>, <i>ExecStartPost=</i></p>
<dl>
<dd>Takes one or more command lines, which are executed before or after the listening sockets/FIFOs are created and bound, respectively. The first token of the command line must be an absolute filename, then followed by arguments for the process. Multiple command lines may be specified following the same scheme as used for <i>ExecStartPre=</i> of service unit files.</dl>
<p> <i>ExecStopPre=</i>, <i>ExecStopPost=</i></p>
<dl>
<dd>Additional commands that are executed before or after the listening sockets/FIFOs are closed and removed, respectively. Multiple command lines may be specified following the same scheme as used for <i>ExecStartPre=</i> of service unit files.</dl>
<p> <i>TimeoutSec=</i></p>
<dl>
<dd>Configures the time to wait for the commands specified in <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecStopPre=</i> and <i>ExecStopPost=</i> to finish. If a command does not exit within the configured time, the socket will be considered failed and be shut down again. All commands still running will be terminated forcibly via <code>SIGTERM</code>, and after another delay of this time with <code>SIGKILL</code>. (See <code>KillMode=</code> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5).) Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass &quot;0&quot; to disable the timeout logic. Defaults to <i>DefaultTimeoutStartSec=</i> from the manager configuration file (see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)).</dl>
<p> <i>Service=</i></p>
<dl>
<dd>Specifies the service unit name to activate on incoming traffic. This setting is only allowed for sockets with <i>Accept=no</i>. It defaults to the service that bears the same name as the socket (with the suffix replaced). In most cases, it should not be necessary to use this option. Note that setting this parameter might result in additional dependencies to be added to the unit (see above).</dl>
<p> <i>RemoveOnStop=</i></p>
<dl>
<dd>Takes a boolean argument. If enabled, any file nodes created by this socket unit are removed when it is stopped. This applies to <code>AF_UNIX</code> sockets in the file system, POSIX message queues, FIFOs, as well as any symlinks to them configured with <i>Symlinks=</i>. Normally, it should not be necessary to use this option, and is not recommended as services might continue to run after the socket unit has been terminated and it should still be possible to communicate with them via their file system node. Defaults to off.</dl>
<p> <i>Symlinks=</i></p>
<dl>
<dd>Takes a list of file system paths. The specified paths will be created as symlinks to the <code>AF_UNIX</code> socket path or FIFO path of this socket unit. If this setting is used, only one <code>AF_UNIX</code> socket in the file system or one FIFO may be configured for the socket unit. Use this option to manage one or more symlinked alias names for a socket, binding their lifecycle together. Note that if creation of a symlink fails this is not considered fatal for the socket unit, and the socket unit may still start. If an empty string is assigned, the list of paths is reset. Defaults to an empty list.</dl>
<p> <i>FileDescriptorName=</i></p>
<dl>
<dd>Assigns a name to all file descriptors this socket unit encapsulates. This is useful to help activated services identify specific file descriptors, if multiple fds are passed. Services may use the <code><a href="/docs/linux/man/3-sd_listen_fds_with_names/">sd_listen_fds_with_names</a></code>(3) call to acquire the names configured for the received file descriptors. Names may contain any ASCII character, but must exclude control characters and &quot;:&quot;, and must be at most 255 characters in length. If this setting is not used, the file descriptor name defaults to the name of the socket unit, including its .socket suffix.</dl>
<p> <i>TriggerLimitIntervalSec=</i>, <i>TriggerLimitBurst=</i></p>
<dl>
<dd>Configures a limit on how often this socket unit my be activated within a specific time interval. The <i>TriggerLimitIntervalSec=</i> may be used to configure the length of the time interval in the usual time units &quot;us&quot;, &quot;ms&quot;, &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &#8230; and defaults to 2s (See <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for details on the various time units understood). The <i>TriggerLimitBurst=</i> setting takes a positive integer value and specifies the number of permitted activations per time interval, and defaults to 200 for <i>Accept=yes</i> sockets (thus by default permitting 200 activations per 2s), and 20 otherwise (20 activations per 2s). Set either to 0 to disable any form of trigger rate limiting. If the limit is hit, the socket unit is placed into a failure mode, and will not be connectible anymore until restarted. Note that this limit is enforced before the service activation is enqueued.</dl>
<p> Check <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for more settings.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_listen_fds_with_names/">sd_listen_fds_with_names</a></code>(3) </p>
<p> For more extensive descriptions see the &quot;systemd for Developers&quot; series: m[blue]<code>Socket Activation</code>m[]<font SIZE="-2">[4]</font>, m[blue]<code>Socket Activation, part II</code>m[]<font SIZE="-2">[5]</font>, m[blue]<code>Converting inetd Services</code>m[]<font SIZE="-2">[6]</font>, m[blue]<code>Socket Activated Internet Services and OS Containers</code>m[]<font SIZE="-2">[7]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>USB FunctionFS</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/usb/functionfs.txt">https://www.kernel.org/doc/Documentation/usb/functionfs.txt</a></dl>
<dt> 2.</p>
<dd>TCP Keepalive HOWTO</p>
<dl>
<dd><a rel="nofollow" href="http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/">http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/</a></dl>
<dt> 3.</p>
<dd>Smack.txt</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/security/Smack.txt">https://www.kernel.org/doc/Documentation/security/Smack.txt</a></dl>
<dt> 4.</p>
<dd>Socket Activation</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/socket-activation.html">http://0pointer.de/blog/projects/socket-activation.html</a></dl>
<dt> 5.</p>
<dd>Socket Activation, part II</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/socket-activation2.html">http://0pointer.de/blog/projects/socket-activation2.html</a></dl>
<dt> 6.</p>
<dd>Converting inetd Services</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/inetd.html">http://0pointer.de/blog/projects/inetd.html</a></dl>
<dt> 7.</p>
<dd>Socket Activated Internet Services and OS Containers</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/socket-activated-containers.html">http://0pointer.de/blog/projects/socket-activated-containers.html</a></dl>
