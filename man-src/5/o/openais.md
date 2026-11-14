---
title: "openais(5)"
name: "openais"
section: "5"
letter: "o"
url: "/docs/linux/man/5-openais/"
description: "openais.conf – openais executive configuration file"
---

<p>openais.conf &#8211; openais executive configuration file </p>
<h2>Synopsis</h2>
<p>/etc/ais/openais.conf </p>
<h2>Description</h2>
<p>The openais.conf instructs the openais executive about various parameters needed to control the openais executive. The configuration file consists of bracketed top level directives. The possible directive choices are <i>totem { } , logging { } , event { } , and amf { }.</i><br />
&nbsp;<wbr>These directives are described below.</p>
<dl>
<dt>totem { }</p>
<dd>This top level directive contains configuration options for the totem protocol.</p>
<dt>logging { }</p>
<dd>This top level directive contains configuration options for logging.</p>
<dt>event { }</p>
<dd>This top level directive contains configuration options for the event service.</p>
<dt>amf { }</p>
<dd>This top level directive contains configuration options for the AMF service.  Within the <code>totem</code> directive, an interface directive is required. There is also one configuration option which is required: Within the <code>interface</code> sub-directive of totem there are four parameters which are required:</p>
<dl>
<dt>ringnumber</p>
<dd>This specifies the ring number for the interface. When using the redundant ring protocol, each interface should specify separate ring numbers to uniquely identify to the membership protocol which interface to use for which redundant ring.</p>
<dt>bindnetaddr</p>
<dd>This specifies the address which the openais executive should bind. This address should always end in zero. If the totem traffic should be routed over 192.168.5.92, set bindnetaddr to 192.168.5.0. This may also be an IPV6 address, in which case IPV6 networking will be used. In this case, the full address must be specified and there is no automatic selection of the network interface within a specific subnet as with IPv4. If IPv6 networking is used, the nodeid field must be specified.</p>
<dt>mcastaddr</p>
<dd>This is the multicast address used by openais executive. The default should work for most networks, but the network administrator should be queried about a multicast address to use. Avoid 224.x.x.x because this is a &quot;config&quot; multicast address. This may also be an IPV6 multicast address, in which case IPV6 networking will be used. If IPv6 networking is used, the nodeid field must be specified.</p>
<dt>mcastport</p>
<dd>This specifies the UDP port number. It is possible to use the same multicast address on a network with the openais services configured for different UDP ports.  Within the <code>totem</code> directive, there are seven configuration options of which one is required, five are optional, and one is required when IPV6 is configured in the interface subdirective. The required directive controls the version of the totem configuration. The optional option unless using IPV6 directive controls identification of the processor. The optional options control secrecy and authentication, the redundant ring mode of operation, maximum network MTU, and number of sending threads, and the nodeid field.</p>
<dl>
<dt>version</p>
<dd>This specifies the version of the configuration file. Currently the only valid version for this directive is 2. </p>
<dl>
<dt>nodeid</p>
<dd>This configuration option is optional when using IPv4 and required when using IPv6. This is a 32 bit value specifying the node identifier delivered to the cluster membership service. If this is not specified with IPv4, the node id will be determined from the 32 bit IP address the system to which the system is bound with ring identifier of 0. The node identifier value of zero is reserved and should not be used.</p>
<dt>secauth</p>
<dd>This specifies that HMAC/SHA1 authentication should be used to authenticate all messages. It further specifies that all data should be encrypted with the sober128 encryption algorithm to protect data from eavesdropping. Enabling this option adds a 36 byte header to every message sent by totem which reduces total throughput. Encryption and authentication consume 75% of CPU cycles in aisexec as measured with gprof when enabled. For 100mbit networks with 1500 MTU frame transmissions: A throughput of 9mb/sec is possible with 100% cpu utilization when this option is enabled on 3ghz cpus. A throughput of 10mb/sec is possible wth 20% cpu utilization when this optin is disabled on 3ghz cpus. For gig-e networks with large frame transmissions: A throughput of 20mb/sec is possible when this option is enabled on 3ghz cpus. A throughput of 60mb/sec is possible when this option is disabled on 3ghz cpus. The default is on.</p>
<dt>rrp_mode</p>
<dd>This specifies the mode of redundant ring, which may be none, active, or passive. Active replication offers slightly lower latency from transmit to delivery in faulty network environments but with less performance. Passive replication may nearly double the speed of the totem protocol if the protocol doesn&#8217;t become cpu bound. The final option is none, in which case only one network interface will be used to operate the totem protocol. If only one interface directive is specified, none is automatically chosen. If multiple interface directives are specified, only active or passive may be chosen.</p>
<dt>netmtu</p>
<dd>This specifies the network maximum transmit unit. To set this value beyond 1500, the regular frame MTU, requires ethernet devices that support large, or also called jumbo, frames. If any device in the network doesn&#8217;t support large frames, the protocol will not operate properly. The hosts must also have their mtu size set from 1500 to whatever frame size is specified here. Please note while some NICs or switches claim large frame support, they support 9000 MTU as the maximum frame size including the IP header. Setting the netmtu and host MTUs to 9000 will cause totem to use the full 9000 bytes of the frame. Then Linux will add a 18 byte header moving the full frame size to 9018. As a result some hardware will not operate properly with this size of data. A netmtu of 8982 seems to work for the few large frame devices that have been tested. Some manufacturers claim large frame support when in fact they support frame sizes of 4500 bytes. Increasing the MTU from 1500 to 8982 doubles throughput performance from 30MB/sec to 60MB/sec as measured with evsbench with 175000 byte messages with the secauth directive set to off. When sending multicast traffic, if the network frequently reconfigures, chances are that some device in the network doesn&#8217;t support large frames. Choose hardware carefully if intending to use large frame support. The default is 1500.</p>
<dt>threads</p>
<dd>This directive controls how many threads are used to encrypt and send multicast messages. If secauth is off, the protocol will never use threaded sending. If secauth is on, this directive allows systems to be configured to use multiple threads to encrypt and send multicast messages. A thread directive of 0 indicates that no threaded send should be used. This mode offers best performance for non-SMP systems. The default is 0.  The default is ykd. The vsftype can also be set to none. Within the <code>totem</code> directive, there are several configuration options which are used to control the operation of the protocol. It is generally not recommended to change any of these values without proper guidance and sufficient testing. Some networks may require larger values if suffering from frequent reconfigurations. Some applications may require faster failure detection times which can be achieved by reducing the token timeout.</p>
<dt>token</p>
<dd>This timeout specifies in milliseconds until a token loss is declared after not receiving a token. This is the time spent detecting a failure of a processor in the current configuration. Reforming a new configuration takes about 50 milliseconds in addition to this timeout. The default is 1000 milliseconds.</p>
<dt>token_retransmit</p>
<dd>This timeout specifies in milliseconds after how long before receiving a token the token is retransmitted. This will be automatically calculated if token is modified. It is not recommended to alter this value without guidance from the openais community. The default is 238 milliseconds.</p>
<dt>hold</p>
<dd>This timeout specifies in milliseconds how long the token should be held by the representative when the protocol is under low utilization. It is not recommended to alter this value without guidance from the openais community. The default is 180 milliseconds.</p>
<dt>retransmits_before_loss</p>
<dd>This value identifies how many token retransmits should be attempted before forming a new configuration. If this value is set, retransmit and hold will be automatically calculated from retransmits_before_loss and token. The default is 4 retransmissions.</p>
<dt>join</p>
<dd>This timeout specifies in milliseconds how long to wait for join messages in the membership protocol. The default is 100 milliseconds.</p>
<dt>send_join</p>
<dd>This timeout specifies in milliseconds an upper range between 0 and send_join to wait before sending a join message. For configurations with less then 32 nodes, this parameter is not necessary. For larger rings, this parameter is necessary to ensure the NIC is not overflowed with join messages on formation of a new ring. A reasonable value for large rings (128 nodes) would be 80msec. Other timer values must also change if this value is changed. Seek advice from the openais mailing list if trying to run larger configurations. The default is 0 milliseconds.</p>
<dt>consensus</p>
<dd>This timeout specifies in milliseconds how long to wait for consensus to be achieved before starting a new round of membership configuration. The default is 200 milliseconds.</p>
<dt>merge</p>
<dd>This timeout specifies in milliseconds how long to wait before checking for a partition when no multicast traffic is being sent. If multicast traffic is being sent, the merge detection happens automatically as a function of the protocol. The default is 200 milliseconds.</p>
<dt>downcheck</p>
<dd>This timeout specifies in milliseconds how long to wait before checking that a network interface is back up after it has been downed. The default is 1000 millseconds.</p>
<dt>fail_to_recv_const</p>
<dd>This constant specifies how many rotations of the token without receiving any of the messages when messages should be received may occur before a new configuration is formed. The default is 50 failures to receive a message.</p>
<dt>seqno_unchanged_const</p>
<dd>This constant specifies how many rotations of the token without any multicast traffic should occur before the merge detection timeout is started. The default is 30 rotations.</p>
<dt>heartbeat_failures_allowed</p>
<dd>[HeartBeating mechanism] Configures the optional HeartBeating mechanism for faster failure detection. Keep in mind that engaging this mechanism in lossy networks could cause faulty loss declaration as the mechanism relies on the network for heartbeating. So as a rule of thumb use this mechanism if you require improved failure in low to medium utilized networks. This constant specifies the number of heartbeat failures the system should tolerate before declaring heartbeat failure e.g 3. Also if this value is not set or is 0 then the heartbeat mechanism is not engaged in the system and token rotation is the method of failure detection The default is 0 (disabled).</p>
<dt>max_network_delay</p>
<dd>[HeartBeating mechanism] This constant specifies in milliseconds the approximate delay that your network takes to transport one packet from one machine to another. This value is to be set by system engineers and please dont change if not sure as this effects the failure detection mechanism using heartbeat. The default is 50 milliseconds.</p>
<dt>window_size</p>
<dd>This constant specifies the maximum number of messages that may be sent on one token rotation. If all processors perform equally well, this value could be large (300), which would introduce higher latency from origination to delivery for very large rings. To reduce latency in large rings(16+), the defaults are a safe compromise. If 1 or more slow processor(s) are present among fast processors, window_size should be no larger then 256000 / netmtu to avoid overflow of the kernel receive buffers. The user is notified of this by the display of a retransmit list in the notification logs. There is no loss of data, but performance is reduced when these errors occur. The default is 50 messages.</p>
<dt>max_messages</p>
<dd>This constant specifies the maximum number of messages that may be sent by one processor on receipt of the token. The max_messages parameter is limited to 256000 / netmtu to prevent overflow of the kernel transmit buffers. The default is 17 messages.</p>
<dt>rrp_problem_count_timeout</p>
<dd>This specifies the time in milliseconds to wait before decrementing the problem count by 1 for a particular ring to ensure a link is not marked faulty for transient network failures. The default is 1000 milliseconds.</p>
<dt>rrp_problem_count_threshold</p>
<dd>This specifies the number of times a problem is detected with a link before setting the link faulty. Once a link is set faulty, no more data is transmitted upon it. Also, the problem counter is no longer decremented when the problem count timeout expires. A problem is detected whenever all tokens from the proceeding processor have not been received within the rrp_token_expired_timeout. The rrp_problem_count_threshold * rrp_token_expired_timeout should be atleast 50 milliseconds less then the token timeout, or a complete reconfiguration may occur. The default is 20 problem counts.</p>
<dt>rrp_token_expired_timeout</p>
<dd>This specifies the time in milliseconds to increment the problem counter for the redundant ring protocol after not having received a token from all rings for a particular processor. This value will automatically be calculated from the token timeout and problem_count_threshold but may be overridden. It is not recommended to override this value without guidance from the openais community. The default is 47 milliseconds.  Within the <code>logging</code> directive, there are seven configuration options which are all optional:</p>
<dl>
<dt>to_stderr</p>
<dd>
<dt>to_file</p>
<dd>
<dt>to_syslog</p>
<dd>These specify the destination of logging output. Any combination of these options may be specified. Valid options are <code>yes</code> and <code>no.</code> The default is syslog and stderr.</p>
<dt>logfile</p>
<dd>If the <code>to_file</code> directive is set to <code>yes</code> , this option specifies the pathname of the log file. No default.</p>
<dt>debug</p>
<dd>This specifies whether debug output is logged for all services. This is generally a bad idea, unless there is some specific bug or problem that must be found in the executive. Set the value to <code>on</code> to debug, <code>off</code> to turn off debugging. If enabled, individual loggers can be disabled using a <code>logger_subsys</code> directive. The default is off.</p>
<dt>timestamp</p>
<dd>This specifies that a timestamp is placed on all log messages. The default is off.</p>
<dt>fileline</p>
<dd>This specifies that file and line should be printed instead of logger name. The default is off.</p>
<dt>syslog_facility</p>
<dd>This specifies the syslog facility type that will be used for any messages sent to syslog. options are daemon, local0, local1, local2, local3, local4, local5, local6 &amp; local7. The default is daemon.  Within the <code>logging</code> directive, logger directives are optional. Within the <code>logger_subsys</code> sub-directive of logging there are three configuration options:</p>
<dl>
<dt>subsys</p>
<dd>This specifies the subsystem identity (name) for which logging is specified. This is the name used by a service in the log_init () call. E.g. &#8216;CKPT&#8217;. This directive is required.</p>
<dt>debug</p>
<dd>This specifies whether debug output is logged for this particular logger. The default is off.</p>
<dt>syslog_level</p>
<dd>This specifies the syslog level for this particular subsystem. Ignored if debug is on. Possible values are: alert, crit, debug (same as debug = on), emerg, err, info, notice, warning. The default is: info.</p>
<dt>tags</p>
<dd>This specifies which tags should be traced for this particular logger. Set debug directive to <code>on</code> in order to enable tracing using tags. Values are specified using a vertical bar as a logical OR separator: enter|leave|trace1|trace2|trace3|&#8230; The default is none.  Within the <code>event</code> directive, there are two configuration options which are all optional:</p>
<dl>
<dt>delivery_queue_size</p>
<dd>This directive describes the full size of the outgoing delivery queue to the application. If applications are slow to process messages, they will be delivered event loss messages. By increasing this value, the applications that are slowly processing messages may have an opportunity to catch up.</p>
<dt>delivery_queue_resume</p>
<dd>This directive describes when new events can be accepted by the event service when the delivery queue count of pending messages has reached this value. Please note this is not cluster wide.  Within the <code>amf</code> directive, there is one configuration option which is optional:</p>
<dl>
<dt>mode</p>
<dd>This can either contain the value enabled or disabled. When enabled, AMF will start the applications specified in the /etc/ais/amf.conf file. The default is disabled. </p>
<h2>Files</h2>
<dl>
<dt>/etc/ais/openais.conf</p>
<dd>The openais executive configuration file.</p>
<dt>/etc/ais/amf.conf</p>
<dd>The openais AMF configuration file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-openais_overview/">openais_overview</a></code>(8),<code>README.amf</code> </p>
