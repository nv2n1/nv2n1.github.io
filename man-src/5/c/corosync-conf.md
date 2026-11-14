---
title: "corosync-conf(5)"
name: "corosync-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-corosync-conf/"
description: "corosync.conf – corosync executive configuration file"
---

<p>corosync.conf &#8211; corosync executive configuration file </p>
<h2>Synopsis</h2>
<p>/etc/corosync/corosync.conf </p>
<h2>Description</h2>
<p>The corosync.conf instructs the corosync executive about various parameters needed to control the corosync executive. Empty lines and lines starting with # character are ignored. The configuration file consists of bracketed top level directives. The possible directive choices are:</p>
<dl>
<dt>totem { }</p>
<dd>This top level directive contains configuration options for the totem protocol.</p>
<dt>logging { }</p>
<dd>This top level directive contains configuration options for logging.</p>
<dt>quorum { }</p>
<dd>This top level directive contains configuration options for quorum.</p>
<dt>nodelist { }</p>
<dd>This top level directive contains configuration options for nodes in cluster.</p>
<dt>qb { }</p>
<dd>This top level directive contains configuration options related to libqb.  Within the <code>totem</code> directive, an interface directive is required. There is also one configuration option which is required: Within the <code>interface</code> sub-directive of totem there are four parameters which are required. There is one parameter which is optional.</p>
<dl>
<dt>ringnumber</p>
<dd>This specifies the ring number for the interface. When using the redundant ring protocol, each interface should specify separate ring numbers to uniquely identify to the membership protocol which interface to use for which redundant ring. The ringnumber must start at 0.</p>
<dt>bindnetaddr</p>
<dd>This specifies the network address the corosync executive should bind to. bindnetaddr should be an IP address configured on the system, or a network address. For example, if the local interface is 192.168.5.92 with netmask 255.255.255.0, you should set bindnetaddr to 192.168.5.92 or 192.168.5.0. If the local interface is 192.168.5.92 with netmask 255.255.255.192, set bindnetaddr to 192.168.5.92 or 192.168.5.64, and so forth. This may also be an IPV6 address, in which case IPV6 networking will be used. In this case, the exact address must be specified and there is no automatic selection of the network interface within a specific subnet as with IPv4. If IPv6 networking is used, the nodeid field in nodelist must be specified.</p>
<dt>broadcast</p>
<dd>This is optional and can be set to yes. If it is set to yes, the broadcast address will be used for communication. If this option is set, mcastaddr should not be set.</p>
<dt>mcastaddr</p>
<dd>This is the multicast address used by corosync executive. The default should work for most networks, but the network administrator should be queried about a multicast address to use. Avoid 224.x.x.x because this is a &quot;config&quot; multicast address. This may also be an IPV6 multicast address, in which case IPV6 networking will be used. If IPv6 networking is used, the nodeid field in nodelist must be specified. It&#8217;s not needed to use this option if cluster_name option is used. If both options are used, mcastaddr has higher priority.</p>
<dt>mcastport</p>
<dd>This specifies the UDP port number. It is possible to use the same multicast address on a network with the corosync services configured for different UDP ports. Please note corosync uses two UDP ports mcastport (for mcast receives) and mcastport &#8211; 1 (for mcast sends). If you have multiple clusters on the same network using the same mcastaddr please configure the mcastports with a gap.</p>
<dt>ttl</p>
<dd>This specifies the Time To Live (TTL). If you run your cluster on a routed network then the default of &quot;1&quot; will be too small. This option provides a way to increase this up to 255. The valid range is 0..255. Note that this is only valid on multicast transport types.  Within the <code>totem</code> directive, there are seven configuration options of which one is required, five are optional, and one is required when IPV6 is configured in the interface subdirective. The required directive controls the version of the totem configuration. The optional option unless using IPV6 directive controls identification of the processor. The optional options control secrecy and authentication, the redundant ring mode of operation and maximum network MTU field.</p>
<dl>
<dt>version</p>
<dd>This specifies the version of the configuration file. Currently the only valid version for this directive is 2.  clear_node_high_bit This configuration option is optional and is only relevant when no nodeid is specified. Some corosync clients require a signed 32 bit nodeid that is greater than zero however by default corosync uses all 32 bits of the IPv4 address space when generating a nodeid. Set this option to yes to force the high bit to be zero and therefor ensure the nodeid is a positive signed 32 bit integer. WARNING: The clusters behavior is undefined if this option is enabled on only a subset of the cluster (for example during a rolling upgrade).</p>
<dl>
<dt>crypto_hash</p>
<dd>This specifies which HMAC authentication should be used to authenticate all messages. Valid values are none (no authentication), md5, sha1, sha256, sha384 and sha512. The default is sha1.</p>
<dt>crypto_cipher</p>
<dd>This specifies which cipher should be used to encrypt all messages. Valid values are none (no encryption), aes256, aes192, aes128 and 3des. Enabling crypto_cipher, requires also enabling of crypto_hash. The default is aes256.</p>
<dt>secauth</p>
<dd>This specifies that HMAC/SHA1 authentication should be used to authenticate all messages. It further specifies that all data should be encrypted with the nss library and aes256 encryption algorithm to protect data from eavesdropping. Enabling this option adds a encryption header to every message sent by totem which reduces total throughput. Also encryption and authentication consume extra CPU cycles in corosync. The default is on. WARNING: This parameter is deprecated. It&#8217;s recomended to use combination of crypto_cipher and crypto_hash.</p>
<dt>rrp_mode</p>
<dd>This specifies the mode of redundant ring, which may be none, active, or passive. Currently only &#8216;passive&#8217; is supported or tested (using &#8216;active&#8217; is not recommended). Active replication offers slightly lower latency from transmit to delivery in faulty network environments but with less performance. Passive replication may nearly double the speed of the totem protocol if the protocol doesn&#8217;t become cpu bound. The final option is none, in which case only one network interface will be used to operate the totem protocol. If only one interface directive is specified, none is automatically chosen. If multiple interface directives are specified, only active or passive may be chosen. The maximum number of interface directives that is allowed for either modes (active or passive) is 2. When using multiple interfaces, make sure to use different multicast address/port (port for same address must differ by at least two) pair for each interface (this is checked by parser) to make rrp works.</p>
<dt>netmtu</p>
<dd>This specifies the network maximum transmit unit. To set this value beyond 1500, the regular frame MTU, requires ethernet devices that support large, or also called jumbo, frames. If any device in the network doesn&#8217;t support large frames, the protocol will not operate properly. The hosts must also have their mtu size set from 1500 to whatever frame size is specified here. Please note while some NICs or switches claim large frame support, they support 9000 MTU as the maximum frame size including the IP header. Setting the netmtu and host MTUs to 9000 will cause totem to use the full 9000 bytes of the frame. Then Linux will add a 18 byte header moving the full frame size to 9018. As a result some hardware will not operate properly with this size of data. A netmtu of 8982 seems to work for the few large frame devices that have been tested. Some manufacturers claim large frame support when in fact they support frame sizes of 4500 bytes. When sending multicast traffic, if the network frequently reconfigures, chances are that some device in the network doesn&#8217;t support large frames. Choose hardware carefully if intending to use large frame support. The default is 1500.</p>
<dt>transport</p>
<dd>This directive controls the transport mechanism used. If the interface to which corosync is binding is an RDMA interface such as RoCEE or Infiniband, the &quot;iba&quot; parameter may be specified. To avoid the use of multicast entirely, a unicast transport parameter &quot;udpu&quot; can be specified. This requires specifying the list of members in nodelist directive, that could potentially make up the membership before deployment. The default is udp. The transport type can also be set to udpu or iba.</p>
<dt>cluster_name</p>
<dd>This specifies the name of cluster and it&#8217;s used for automatic generating of multicast address.</p>
<dt>config_version</p>
<dd>This specifies version of config file. This is converted to unsigned 64-bit int. By default it&#8217;s 0. Option is used to prevent joining old nodes with not up-to-date configuration. If value is not 0, and node is going for first time (only for first time, join after split doesn&#8217;t follow this rules) from single-node membership to multiple nodes membership, other nodes config_versions are collected. If current node config_version is not equal to highest of collected versions, corosync is terminated.</p>
<dt>ip_version</p>
<dd>Specifies version of IP to use for communication. Value can be one of ipv4 or ipv6. Default (if unspecified) is ipv4. Within the <code>totem</code> directive, there are several configuration options which are used to control the operation of the protocol. It is generally not recommended to change any of these values without proper guidance and sufficient testing. Some networks may require larger values if suffering from frequent reconfigurations. Some applications may require faster failure detection times which can be achieved by reducing the token timeout.</p>
<dt>token</p>
<dd>This timeout is used directly or as a base for real token timeout calculation (explained in <code>token_coefficient</code> section). Token timeout specifies in milliseconds until a token loss is declared after not receiving a token. This is the time spent detecting a failure of a processor in the current configuration. Reforming a new configuration takes about 50 milliseconds in addition to this timeout. For real token timeout used by totem it&#8217;s possible to read cmap value of <code>runtime.config.token</code> key. The default is 1000 milliseconds.</p>
<dt>token_coefficient</p>
<dd>This value is used only when <code>nodelist</code> section is specified and contains at least 3 nodes. If so, real token timeout is then computed as token + (number_of_nodes &#8211; 2) * token_coefficient. This allows cluster to scale without manually changing token timeout every time new node is added. This value can be set to 0 resulting in effective removal of this feature. The default is 650 milliseconds.</p>
<dt>token_retransmit</p>
<dd>This timeout specifies in milliseconds after how long before receiving a token the token is retransmitted. This will be automatically calculated if token is modified. It is not recommended to alter this value without guidance from the corosync community. The default is 238 milliseconds.</p>
<dt>hold</p>
<dd>This timeout specifies in milliseconds how long the token should be held by the representative when the protocol is under low utilization. It is not recommended to alter this value without guidance from the corosync community. The default is 180 milliseconds.</p>
<dt>token_retransmits_before_loss_const</p>
<dd>This value identifies how many token retransmits should be attempted before forming a new configuration. If this value is set, retransmit and hold will be automatically calculated from retransmits_before_loss and token. The default is 4 retransmissions.</p>
<dt>join</p>
<dd>This timeout specifies in milliseconds how long to wait for join messages in the membership protocol. The default is 50 milliseconds.</p>
<dt>send_join</p>
<dd>This timeout specifies in milliseconds an upper range between 0 and send_join to wait before sending a join message. For configurations with less then 32 nodes, this parameter is not necessary. For larger rings, this parameter is necessary to ensure the NIC is not overflowed with join messages on formation of a new ring. A reasonable value for large rings (128 nodes) would be 80msec. Other timer values must also change if this value is changed. Seek advice from the corosync mailing list if trying to run larger configurations. The default is 0 milliseconds.</p>
<dt>consensus</p>
<dd>This timeout specifies in milliseconds how long to wait for consensus to be achieved before starting a new round of membership configuration. The minimum value for consensus must be 1.2 * token. This value will be automatically calculated at 1.2 * token if the user doesn&#8217;t specify a consensus value. For two node clusters, a consensus larger then the join timeout but less then token is safe. For three node or larger clusters, consensus should be larger then token. There is an increasing risk of odd membership changes, which stil guarantee virtual synchrony, as node count grows if consensus is less than token. The default is 1200 milliseconds.</p>
<dt>merge</p>
<dd>This timeout specifies in milliseconds how long to wait before checking for a partition when no multicast traffic is being sent. If multicast traffic is being sent, the merge detection happens automatically as a function of the protocol. The default is 200 milliseconds.</p>
<dt>downcheck</p>
<dd>This timeout specifies in milliseconds how long to wait before checking that a network interface is back up after it has been downed. The default is 1000 millseconds.</p>
<dt>fail_recv_const</p>
<dd>This constant specifies how many rotations of the token without receiving any of the messages when messages should be received may occur before a new configuration is formed. The default is 2500 failures to receive a message.</p>
<dt>seqno_unchanged_const</p>
<dd>This constant specifies how many rotations of the token without any multicast traffic should occur before the hold timer is started. The default is 30 rotations.</p>
<dt>heartbeat_failures_allowed</p>
<dd>[HeartBeating mechanism] Configures the optional HeartBeating mechanism for faster failure detection. Keep in mind that engaging this mechanism in lossy networks could cause faulty loss declaration as the mechanism relies on the network for heartbeating. So as a rule of thumb use this mechanism if you require improved failure in low to medium utilized networks. This constant specifies the number of heartbeat failures the system should tolerate before declaring heartbeat failure e.g 3. Also if this value is not set or is 0 then the heartbeat mechanism is not engaged in the system and token rotation is the method of failure detection The default is 0 (disabled).</p>
<dt>max_network_delay</p>
<dd>[HeartBeating mechanism] This constant specifies in milliseconds the approximate delay that your network takes to transport one packet from one machine to another. This value is to be set by system engineers and please don&#8217;t change if not sure as this effects the failure detection mechanism using heartbeat. The default is 50 milliseconds.</p>
<dt>window_size</p>
<dd>This constant specifies the maximum number of messages that may be sent on one token rotation. If all processors perform equally well, this value could be large (300), which would introduce higher latency from origination to delivery for very large rings. To reduce latency in large rings(16+), the defaults are a safe compromise. If 1 or more slow processor(s) are present among fast processors, window_size should be no larger then 256000 / netmtu to avoid overflow of the kernel receive buffers. The user is notified of this by the display of a retransmit list in the notification logs. There is no loss of data, but performance is reduced when these errors occur. The default is 50 messages.</p>
<dt>max_messages</p>
<dd>This constant specifies the maximum number of messages that may be sent by one processor on receipt of the token. The max_messages parameter is limited to 256000 / netmtu to prevent overflow of the kernel transmit buffers. The default is 17 messages.</p>
<dt>miss_count_const</p>
<dd>This constant defines the maximum number of times on receipt of a token a message is checked for retransmission before a retransmission occurs. This parameter is useful to modify for switches that delay multicast packets compared to unicast packets. The default setting works well for nearly all modern switches. The default is 5 messages.</p>
<dt>rrp_problem_count_timeout</p>
<dd>This specifies the time in milliseconds to wait before decrementing the problem count by 1 for a particular ring to ensure a link is not marked faulty for transient network failures. The default is 2000 milliseconds.</p>
<dt>rrp_problem_count_threshold</p>
<dd>This specifies the number of times a problem is detected with a link before setting the link faulty. Once a link is set faulty, no more data is transmitted upon it. Also, the problem counter is no longer decremented when the problem count timeout expires. A problem is detected whenever all tokens from the proceeding processor have not been received within the rrp_token_expired_timeout. The rrp_problem_count_threshold * rrp_token_expired_timeout should be atleast 50 milliseconds less then the token timeout, or a complete reconfiguration may occur. The default is 10 problem counts.</p>
<dt>rrp_problem_count_mcast_threshold</p>
<dd>This specifies the number of times a problem is detected with multicast before setting the link faulty for passive rrp mode. This variable is unused in active rrp mode. The default is 10 times rrp_problem_count_threshold.</p>
<dt>rrp_token_expired_timeout</p>
<dd>This specifies the time in milliseconds to increment the problem counter for the redundant ring protocol after not having received a token from all rings for a particular processor. This value will automatically be calculated from the token timeout and problem_count_threshold but may be overridden. It is not recommended to override this value without guidance from the corosync community. The default is 47 milliseconds.</p>
<dt>rrp_autorecovery_check_timeout</p>
<dd>This specifies the time in milliseconds to check if the failed ring can be auto-recovered. The default is 1000 milliseconds.  Within the <code>logging</code> directive, there are several configuration options which are all optional. The following 3 options are valid only for the top level logging directive:</p>
<dl>
<dt>timestamp</p>
<dd>This specifies that a timestamp is placed on all log messages. The default is off.</p>
<dt>fileline</p>
<dd>This specifies that file and line should be printed. The default is off.</p>
<dt>function_name</p>
<dd>This specifies that the code function name should be printed. The default is off.  The following options are valid both for top level logging directive and they can be overridden in logger_subsys entries.</p>
<dl>
<dt>to_stderr</p>
<dd>
<dt>to_logfile</p>
<dd>
<dt>to_syslog</p>
<dd>These specify the destination of logging output. Any combination of these options may be specified. Valid options are <code>yes</code> and <code>no.</code> The default is syslog and stderr. Please note, if you are using to_logfile and want to rotate the file, use <a href="/docs/linux/man/8-logrotate/">logrotate</a>(8) with the option <code>copytruncate.</code> eg.</p>
<dl>
<dd>
<pre>/var/log/corosync.log {
 missingok
 compress
 notifempty
 daily
 rotate 7
 copytruncate
}</pre>
</dl>
<dt>logfile</p>
<dd>If the <code>to_logfile</code> directive is set to <code>yes</code> , this option specifies the pathname of the log file. No default.</p>
<dt>logfile_priority</p>
<dd>This specifies the logfile priority for this particular subsystem. Ignored if debug is on. Possible values are: alert, crit, debug (same as debug = on), emerg, err, info, notice, warning. The default is: info.</p>
<dt>syslog_facility</p>
<dd>This specifies the syslog facility type that will be used for any messages sent to syslog. options are daemon, local0, local1, local2, local3, local4, local5, local6 &amp; local7. The default is daemon.</p>
<dt>syslog_priority</p>
<dd>This specifies the syslog level for this particular subsystem. Ignored if debug is on. Possible values are: alert, crit, debug (same as debug = on), emerg, err, info, notice, warning. The default is: info.</p>
<dt>debug</p>
<dd>This specifies whether debug output is logged for this particular logger. Also can contain value trace, what is highest level of debug information. The default is off.  Within the <code>logging</code> directive, logger_subsys directives are optional. Within the <code>logger_subsys</code> sub-directive, all of the above logging configuration options are valid and can be used to override the default settings. The subsys entry, described below, is mandatory to identify the subsystem.</p>
<dl>
<dt>subsys</p>
<dd>This specifies the subsystem identity (name) for which logging is specified. This is the name used by a service in the log_init () call. E.g. &#8216;CPG&#8217;. This directive is required.  Within the <code>quorum</code> directive it is possible to specify the quorum algorithm to use with the</p>
<dl>
<dt>provider</p>
<dd>directive. At the time of writing only corosync_votequorum is supported. See <a href="/docs/linux/man/5-votequorum/">votequorum</a>(5) for configuration options.  Within the <code>nodelist</code> directive it is possible to specify specific information about nodes in cluster. Directive can contain only <code>node</code> sub-directive, which specifies every node that should be a member of the membership, and where non-default options are needed. Every node must have at least ring0_addr field filled. For UDPU, every node that should be a member of the membership must be specified. Possible options are:</p>
<dl>
<dt>ringX_addr</p>
<dd>This specifies ip address of one of the nodes. X is ring number.</p>
<dt>nodeid</p>
<dd>This configuration option is optional when using IPv4 and required when using IPv6. This is a 32 bit value specifying the node identifier delivered to the cluster membership service. If this is not specified with IPv4, the node id will be determined from the 32 bit IP address the system to which the system is bound with ring identifier of 0. The node identifier value of zero is reserved and should not be used.  Within the <code>qb</code> directive it is possible to specify options for libqb. Possible option is:</p>
<dl>
<dt>ipc_type</p>
<dd>This specifies type of IPC to use. Can be one of native (default), shm and socket. Native means one of shm or socket, depending on what is supported by OS. On systems with support for both, SHM is selected. SHM is generally faster, but need to allocate ring buffer file in /dev/shm. </p>
<h2>Files</h2>
<dl>
<dt>/etc/corosync/corosync.conf</p>
<dd>The corosync executive configuration file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/5-votequorum/">votequorum</a></code>(5), <code><a href="/docs/linux/man/8-logrotate/">logrotate</a></code>(8) </p>
