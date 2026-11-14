---
title: "tcp(7)"
name: "tcp"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tcp/"
description: "tcp – TCP protocol"
---

<p>tcp &#8211; TCP protocol</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;


#include &lt;netinet/in.h&gt;


#include &lt;netinet/tcp.h&gt;
tcp_socket = socket(AF_INET, SOCK_STREAM, 0);</code></pre>
<h2>Description</h2>
<p>This is an implementation of the TCP protocol defined in RFC 793, RFC 1122 and RFC 2001 with the NewReno and SACK extensions. It provides a reliable, stream-oriented, full-duplex connection between two sockets on top of <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), for both v4 and v6 versions. TCP guarantees that the data arrives in order and retransmits lost packets. It generates and checks a per-packet checksum to catch transmission errors. TCP does not preserve record boundaries. A newly created TCP socket has no remote or local address and is not fully specified. To create an outgoing TCP connection use <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) to establish a connection to another TCP socket. To receive new incoming connections, first <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) the socket to a local address and port and then call <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) to put the socket into the listening state. After that a new socket for each incoming connection can be accepted using <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). A socket which has had <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) or <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) successfully called on it is fully specified and may transmit data. Data cannot be transmitted on listening or not yet connected sockets. Linux supports RFC 1323 TCP high performance extensions. These include Protection Against Wrapped Sequence Numbers (PAWS), Window Scaling and Timestamps. Window scaling allows the use of large (&gt; 64 kB) TCP windows in order to support links with high latency or bandwidth. To make use of them, the send and receive buffer sizes must be increased. They can be set globally with the <i>/proc/sys/net/ipv4/tcp_wmem</i> and <i>/proc/sys/net/ipv4/tcp_rmem</i> files, or on individual sockets by using the <code>SO_SNDBUF</code> and <code>SO_RCVBUF</code> socket options with the <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) call. The maximum sizes for socket buffers declared via the <code>SO_SNDBUF</code> and <code>SO_RCVBUF</code> mechanisms are limited by the values in the <i>/proc/sys/net/core/rmem_max</i> and <i>/proc/sys/net/core/wmem_max</i> files. Note that TCP actually allocates twice the size of the buffer requested in the <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) call, and so a succeeding <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) call will not return the same size of buffer as requested in the <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) call. TCP uses the extra space for administrative purposes and internal kernel structures, and the <i>/proc</i> file values reflect the larger sizes compared to the actual TCP windows. On individual connections, the socket buffer size must be set prior to the <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) or <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) calls in order to have it take effect. See <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for more information. TCP supports urgent data. Urgent data is used to signal the receiver that some important message is part of the data stream and that it should be processed as soon as possible. To send urgent data specify the <code>MSG_OOB</code> option to <code><a href="/docs/linux/man/2-send/">send</a></code>(2). When urgent data is received, the kernel sends a <code>SIGURG</code> signal to the process or process group that has been set as the socket &quot;owner&quot; using the <code>SIOCSPGRP</code> or <code>FIOSETOWN</code> ioctls (or the POSIX.1-specified <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETOWN</code> operation). When the <code>SO_OOBINLINE</code> socket option is enabled, urgent data is put into the normal data stream (a program can test for its location using the <code>SIOCATMARK</code> ioctl described below), otherwise it can be received only when the <code>MSG_OOB</code> flag is set for <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) or <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). When out-of-band data is present, <code><a href="/docs/linux/man/2-select/">select</a></code>(2) indicates the file descriptor as having an exceptional condition and <i>poll (2)</i> indicates a <code>POLLPRI</code> event. Linux 2.4 introduced a number of changes for improved throughput and scaling, as well as enhanced functionality. Some of these features include support for zero-copy <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), Explicit Congestion Notification, new management of TIME_WAIT sockets, keep-alive socket options and support for Duplicate SACK extensions.</p>
<h3>Address formats</h3>
<p>TCP is built on top of IP (see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7)). The address formats defined by <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) apply to TCP. TCP supports point-to-point communication only; broadcasting and multicasting are not supported.</p>
<h3>/proc interfaces</h3>
<p>System-wide TCP parameter settings can be accessed by files in the directory <i>/proc/sys/net/ipv4/</i>. In addition, most IP <i>/proc</i> interfaces also apply to TCP; see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). Variables described as <i>Boolean</i> take an integer value, with a nonzero value (&quot;true&quot;) meaning that the corresponding option is enabled, and a zero value (&quot;false&quot;) meaning that the option is disabled.</p>
<dl>
<dt><i>tcp_abc</i> (Integer; default: 0; Linux 2.6.15 to Linux 3.8)</p>
<dd>Control the Appropriate Byte Count (ABC), defined in RFC 3465. ABC is a way of increasing the congestion window (<i>cwnd</i>) more slowly in response to partial acknowledgments. Possible values are:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>increase <i>cwnd</i> once per acknowledgment (no ABC)</p>
<dt>1</p>
<dd>increase <i>cwnd</i> once per acknowledgment of full sized segment</p>
<dt>2</p>
<dd>allow increase <i>cwnd</i> by two if acknowledgment is of two segments to compensate for delayed acknowledgments.</dl>
</dl>
<dt><i>tcp_abort_on_overflow</i> (Boolean; default: disabled; since Linux 2.4)</p>
<dd>Enable resetting connections if the listening service is too slow and unable to keep up and accept them. It means that if overflow occurred due to a burst, the connection will recover. Enable this option <i>only</i> if you are really sure that the listening daemon cannot be tuned to accept connections faster. Enabling this option can harm the clients of your server.</p>
<dt><i>tcp_adv_win_scale</i> (integer; default: 2; since Linux 2.4)</p>
<dd>Count buffering overhead as <i>bytes/2^tcp_adv_win_scale</i>, if <i>tcp_adv_win_scale</i> is greater than 0; or <i>bytes-bytes/2^(-tcp_adv_win_scale)</i>, if <i>tcp_adv_win_scale</i> is less than or equal to zero.</p>
<dd>The socket receive buffer space is shared between the application and kernel. TCP maintains part of the buffer as the TCP window, this is the size of the receive window advertised to the other end. The rest of the space is used as the &quot;application&quot; buffer, used to isolate the network from scheduling and application latencies. The <i>tcp_adv_win_scale</i> default value of 2 implies that the space used for the application buffer is one fourth that of the total.</p>
<dt><i>tcp_allowed_congestion_control</i> (String; default: see text; since Linux 2.4.20)</p>
<dd>Show/set the congestion control algorithm choices available to unprivileged processes (see the description of the <code>TCP_CONGESTION</code> socket option). The items in the list are separated by white space and terminated by a newline character. The list is a subset of those listed in <i>tcp_available_congestion_control</i>. The default value for this list is &quot;reno&quot; plus the default setting of <i>tcp_congestion_control</i>.</p>
<dt><i>tcp_autocorking</i> (Boolean; default: enabled; since Linux 3.14)</p>
<dd>If this option is enabled, the kernel tries to coalesce small writes (from consecutive <code><a href="/docs/linux/man/2-write/">write</a></code>(2) and <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) calls) as much as possible, in order to decrease the total number of sent packets. Coalescing is done if at least one prior packet for the flow is waiting in Qdisc queues or device transmit queue. Applications can still use the <code>TCP_CORK</code> socket option to obtain optimal behavior when they know how/when to uncork their sockets.</p>
<dt><i>tcp_available_congestion_control</i> (String; read-only; since Linux 2.4.20)</p>
<dd>Show a list of the congestion-control algorithms that are registered. The items in the list are separated by white space and terminated by a newline character. This list is a limiting set for the list in <i>tcp_allowed_congestion_control</i>. More congestion-control algorithms may be available as modules, but not loaded.</p>
<dt><i>tcp_app_win</i> (integer; default: 31; since Linux 2.4)</p>
<dd>This variable defines how many bytes of the TCP window are reserved for buffering overhead.</p>
<dd>A maximum of (<i>window/2^tcp_app_win</i>, mss) bytes in the window are reserved for the application buffer. A value of 0 implies that no amount is reserved.</p>
<dt><i>tcp_base_mss</i> (Integer; default: 512; since Linux 2.6.17)</p>
<dd>The initial value of <i>search_low</i> to be used by the packetization layer Path MTU discovery (MTU probing). If MTU probing is enabled, this is the initial MSS used by the connection.</p>
<dt><i>tcp_bic</i> (Boolean; default: disabled; Linux 2.4.27/2.6.6 to 2.6.13)</p>
<dd>Enable BIC TCP congestion control algorithm. BIC-TCP is a sender-side-only change that ensures a linear RTT fairness under large windows while offering both scalability and bounded TCP-friendliness. The protocol combines two schemes called additive increase and binary search increase. When the congestion window is large, additive increase with a large increment ensures linear RTT fairness as well as good scalability. Under small congestion windows, binary search increase provides TCP friendliness.</p>
<dt><i>tcp_bic_low_window</i> (integer; default: 14; Linux 2.4.27/2.6.6 to 2.6.13)</p>
<dd>Set the threshold window (in packets) where BIC TCP starts to adjust the congestion window. Below this threshold BIC TCP behaves the same as the default TCP Reno.</p>
<dt><i>tcp_bic_fast_convergence</i> (Boolean; default: enabled; Linux 2.4.27/2.6.6 to 2.6.13)</p>
<dd>Force BIC TCP to more quickly respond to changes in congestion window. Allows two flows sharing the same connection to converge more rapidly.</p>
<dt><i>tcp_congestion_control</i> (String; default: see text; since Linux 2.4.13)</p>
<dd>Set the default congestion-control algorithm to be used for new connections. The algorithm &quot;reno&quot; is always available, but additional choices may be available depending on kernel configuration. The default value for this file is set as part of kernel configuration.</p>
<dt><i>tcp_dma_copybreak</i> (integer; default: 4096; since Linux 2.6.24)</p>
<dd>Lower limit, in bytes, of the size of socket reads that will be offloaded to a DMA copy engine, if one is present in the system and the kernel was configured with the <code>CONFIG_NET_DMA</code> option.</p>
<dt><i>tcp_dsack</i> (Boolean; default: enabled; since Linux 2.4)</p>
<dd>Enable RFC 2883 TCP Duplicate SACK support.</p>
<dt><i>tcp_ecn</i> (Integer; default: see below; since Linux 2.4)</p>
<dd>Enable RFC 3168 Explicit Congestion Notification.</p>
<dd>This file can have one of the following values:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Disable ECN. Neither initiate nor accept ECN. This was the default up to and including Linux 2.6.30.</p>
<dt>1</p>
<dd>Enable ECN when requested by incoming connections and also request ECN on outgoing connection attempts.</p>
<dt>2</p>
<dd>Enable ECN when requested by incoming connections, but do not request ECN on outgoing connections. This value is supported, and is the default, since Linux 2.6.31.</dl>
</dl>
<dd>When enabled, connectivity to some destinations could be affected due to older, misbehaving middle boxes along the path, causing connections to be dropped. However, to facilitate and encourage deployment with option 1, and to work around such buggy equipment, the <code>tcp_ecn_fallback</code> option has been introduced.</p>
<dt><i>tcp_ecn_fallback</i> (Boolean; default: enabled; since Linux 4.1)</p>
<dd>Enable RFC 3168, Section 6.1.1.1. fallback. When enabled, outgoing ECN-setup SYNs that time out within the normal SYN retransmission timeout will be resent with CWR and ECE cleared.</p>
<dt><i>tcp_fack</i> (Boolean; default: enabled; since Linux 2.2)</p>
<dd>Enable TCP Forward Acknowledgement support.</p>
<dt><i>tcp_fin_timeout</i> (integer; default: 60; since Linux 2.2)</p>
<dd>This specifies how many seconds to wait for a final FIN packet before the socket is forcibly closed. This is strictly a violation of the TCP specification, but required to prevent denial-of-service attacks. In Linux 2.2, the default value was 180.</p>
<dt><i>tcp_frto</i> (integer; default: see below; since Linux 2.4.21/2.6)</p>
<dd>Enable F-RTO, an enhanced recovery algorithm for TCP retransmission timeouts (RTOs). It is particularly beneficial in wireless environments where packet loss is typically due to random radio interference rather than intermediate router congestion. See RFC 4138 for more details.</p>
<dd>This file can have one of the following values:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Disabled. This was the default up to and including Linux 2.6.23.</p>
<dt>1</p>
<dd>The basic version F-RTO algorithm is enabled.</p>
<dt>2</p>
<dd>Enable SACK-enhanced F-RTO if flow uses SACK. The basic version can be used also when SACK is in use though in that case scenario(s) exists where F-RTO interacts badly with the packet counting of the SACK-enabled TCP flow. This value is the default since Linux 2.6.24.</dl>
</dl>
<dd>Before Linux 2.6.22, this parameter was a Boolean value, supporting just values 0 and 1 above.</p>
<dt><i>tcp_frto_response</i> (integer; default: 0; since Linux 2.6.22)</p>
<dd>When F-RTO has detected that a TCP retransmission timeout was spurious (i.e., the timeout would have been avoided had TCP set a longer retransmission timeout), TCP has several options concerning what to do next. Possible values are:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Rate halving based; a smooth and conservative response, results in halved congestion window (<i>cwnd</i>) and slow-start threshold (<i>ssthresh</i>) after one RTT.</p>
<dt>1</p>
<dd>Very conservative response; not recommended because even though being valid, it interacts poorly with the rest of Linux TCP; halves <i>cwnd</i> and <i>ssthresh</i> immediately.</p>
<dt>2</p>
<dd>Aggressive response; undoes congestion-control measures that are now known to be unnecessary (ignoring the possibility of a lost retransmission that would require TCP to be more cautious); <i>cwnd</i> and <i>ssthresh</i> are restored to the values prior to timeout.</dl>
</dl>
<dt><i>tcp_keepalive_intvl</i> (integer; default: 75; since Linux 2.4)</p>
<dd>The number of seconds between TCP keep-alive probes.</p>
<dt><i>tcp_keepalive_probes</i> (integer; default: 9; since Linux 2.2)</p>
<dd>The maximum number of TCP keep-alive probes to send before giving up and killing the connection if no response is obtained from the other end.</p>
<dt><i>tcp_keepalive_time</i> (integer; default: 7200; since Linux 2.2)</p>
<dd>The number of seconds a connection needs to be idle before TCP begins sending out keep-alive probes. Keep-alives are sent only when the <code>SO_KEEPALIVE</code> socket option is enabled. The default value is 7200 seconds (2 hours). An idle connection is terminated after approximately an additional 11 minutes (9 probes an interval of 75 seconds apart) when keep-alive is enabled.</p>
<dd>Note that underlying connection tracking mechanisms and application timeouts may be much shorter.</p>
<dt><i>tcp_low_latency</i> (Boolean; default: disabled; since Linux 2.4.21/2.6; obsolete since Linux 4.14)</p>
<dd>If enabled, the TCP stack makes decisions that prefer lower latency as opposed to higher throughput. It this option is disabled, then higher throughput is preferred. An example of an application where this default should be changed would be a Beowulf compute cluster. Since Linux 4.14, this file still exists, but its value is ignored.</p>
<dt><i>tcp_max_orphans</i> (integer; default: see below; since Linux 2.4)</p>
<dd>The maximum number of orphaned (not attached to any user file handle) TCP sockets allowed in the system. When this number is exceeded, the orphaned connection is reset and a warning is printed. This limit exists only to prevent simple denial-of-service attacks. Lowering this limit is not recommended. Network conditions might require you to increase the number of orphans allowed, but note that each orphan can eat up to ~64 kB of unswappable memory. The default initial value is set equal to the kernel parameter NR_FILE. This initial default is adjusted depending on the memory in the system.</p>
<dt><i>tcp_max_syn_backlog</i> (integer; default: see below; since Linux 2.2)</p>
<dd>The maximum number of queued connection requests which have still not received an acknowledgement from the connecting client. If this number is exceeded, the kernel will begin dropping requests. The default value of 256 is increased to 1024 when the memory present in the system is adequate or greater (&gt;= 128 MB), and reduced to 128 for those systems with very low memory (&lt;= 32 MB).</p>
<dd>Prior to Linux 2.6.20, it was recommended that if this needed to be increased above 1024, the size of the SYNACK hash table (<code>TCP_SYNQ_HSIZE</code>) in <i>include/net/tcp.h</i> should be modified to keep</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;TCP_SYNQ_HSIZE&nbsp;*&nbsp;16&nbsp;&lt;=&nbsp;tcp_max_syn_backlog</p>
<dd>and the kernel should be recompiled. In Linux 2.6.20, the fixed sized <code>TCP_SYNQ_HSIZE</code> was removed in favor of dynamic sizing.</p>
<dt><i>tcp_max_tw_buckets</i> (integer; default: see below; since Linux 2.4)</p>
<dd>The maximum number of sockets in TIME_WAIT state allowed in the system. This limit exists only to prevent simple denial-of-service attacks. The default value of NR_FILE*2 is adjusted depending on the memory in the system. If this number is exceeded, the socket is closed and a warning is printed.</p>
<dt><i>tcp_moderate_rcvbuf</i> (Boolean; default: enabled; since Linux 2.4.17/2.6.7)</p>
<dd>If enabled, TCP performs receive buffer auto-tuning, attempting to automatically size the buffer (no greater than <i>tcp_rmem[2]</i>) to match the size required by the path for full throughput.</p>
<dt><i>tcp_mem</i> (since Linux 2.4)</p>
<dd>This is a vector of 3 integers: [low, pressure, high]. These bounds, measured in units of the system page size, are used by TCP to track its memory usage. The defaults are calculated at boot time from the amount of available memory. (TCP can only use <i>low memory</i> for this, which is limited to around 900 megabytes on 32-bit systems. 64-bit systems do not suffer this limitation.)</p>
<dl>
<dd>
<dl>
<dt><i>low</i></p>
<dd>TCP doesn&#8217;t regulate its memory allocation when the number of pages it has allocated globally is below this number.</p>
<dt><i>pressure</i></p>
<dd>When the amount of memory allocated by TCP exceeds this number of pages, TCP moderates its memory consumption. This memory pressure state is exited once the number of pages allocated falls below the <i>low</i> mark.</p>
<dt><i>high</i></p>
<dd>The maximum number of pages, globally, that TCP will allocate. This value overrides any other limits imposed by the kernel.</dl>
</dl>
<dt><i>tcp_mtu_probing</i> (integer; default: 0; since Linux 2.6.17)</p>
<dd>This parameter controls TCP Packetization-Layer Path MTU Discovery. The following values may be assigned to the file:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Disabled</p>
<dt>1</p>
<dd>Disabled by default, enabled when an ICMP black hole detected</p>
<dt>2</p>
<dd>Always enabled, use initial MSS of <i>tcp_base_mss</i>.</dl>
</dl>
<dt><i>tcp_no_metrics_save</i> (Boolean; default: disabled; since Linux 2.6.6)</p>
<dd>By default, TCP saves various connection metrics in the route cache when the connection closes, so that connections established in the near future can use these to set initial conditions. Usually, this increases overall performance, but it may sometimes cause performance degradation. If <i>tcp_no_metrics_save</i> is enabled, TCP will not cache metrics on closing connections.</p>
<dt><i>tcp_orphan_retries</i> (integer; default: 8; since Linux 2.4)</p>
<dd>The maximum number of attempts made to probe the other end of a connection which has been closed by our end.</p>
<dt><i>tcp_reordering</i> (integer; default: 3; since Linux 2.4)</p>
<dd>The maximum a packet can be reordered in a TCP packet stream without TCP assuming packet loss and going into slow start. It is not advisable to change this number. This is a packet reordering detection metric designed to minimize unnecessary back off and retransmits provoked by reordering of packets on a connection.</p>
<dt><i>tcp_retrans_collapse</i> (Boolean; default: enabled; since Linux 2.2)</p>
<dd>Try to send full-sized packets during retransmit.</p>
<dt><i>tcp_retries1</i> (integer; default: 3; since Linux 2.2)</p>
<dd>The number of times TCP will attempt to retransmit a packet on an established connection normally, without the extra effort of getting the network layers involved. Once we exceed this number of retransmits, we first have the network layer update the route if possible before each new retransmit. The default is the RFC specified minimum of 3.</p>
<dt><i>tcp_retries2</i> (integer; default: 15; since Linux 2.2)</p>
<dd>The maximum number of times a TCP packet is retransmitted in established state before giving up. The default value is 15, which corresponds to a duration of approximately between 13 to 30 minutes, depending on the retransmission timeout. The RFC 1122 specified minimum limit of 100 seconds is typically deemed too short.</p>
<dt><i>tcp_rfc1337</i> (Boolean; default: disabled; since Linux 2.2)</p>
<dd>Enable TCP behavior conformant with RFC 1337. When disabled, if a RST is received in TIME_WAIT state, we close the socket immediately without waiting for the end of the TIME_WAIT period.</p>
<dt><i>tcp_rmem</i> (since Linux 2.4)</p>
<dd>This is a vector of 3 integers: [min, default, max]. These parameters are used by TCP to regulate receive buffer sizes. TCP dynamically adjusts the size of the receive buffer from the defaults listed below, in the range of these values, depending on memory available in the system.</p>
<dl>
<dd>
<dl>
<dt><i>min</i></p>
<dd>minimum size of the receive buffer used by each TCP socket. The default value is the system page size. (On Linux 2.4, the default value is 4 kB, lowered to <code>PAGE_SIZE</code> bytes in low-memory systems.) This value is used to ensure that in memory pressure mode, allocations below this size will still succeed. This is not used to bound the size of the receive buffer declared using <code>SO_RCVBUF</code> on a socket.</p>
<dt><i>default</i></p>
<dd>the default size of the receive buffer for a TCP socket. This value overwrites the initial default buffer size from the generic global <i>net.core.rmem_default</i> defined for all protocols. The default value is 87380 bytes. (On Linux 2.4, this will be lowered to 43689 in low-memory systems.) If larger receive buffer sizes are desired, this value should be increased (to affect all sockets). To employ large TCP windows, the <i>net.ipv4.tcp_window_scaling</i> must be enabled (default).</p>
<dt><i>max</i></p>
<dd>the maximum size of the receive buffer used by each TCP socket. This value does not override the global <i>net.core.rmem_max</i>. This is not used to limit the size of the receive buffer declared using <code>SO_RCVBUF</code> on a socket. The default value is calculated using the formula</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max(87380, min(4 MB,&nbsp;<i>tcp_mem</i>[1]*PAGE_SIZE/128))</p>
<dd>(On Linux 2.4, the default is 87380*2 bytes, lowered to 87380 in low-memory systems).</dl>
</dl>
<dt><i>tcp_sack</i> (Boolean; default: enabled; since Linux 2.2)</p>
<dd>Enable RFC 2018 TCP Selective Acknowledgements.</p>
<dt><i>tcp_slow_start_after_idle</i> (Boolean; default: enabled; since Linux 2.6.18)</p>
<dd>If enabled, provide RFC 2861 behavior and time out the congestion window after an idle period. An idle period is defined as the current RTO (retransmission timeout). If disabled, the congestion window will not be timed out after an idle period.</p>
<dt><i>tcp_stdurg</i> (Boolean; default: disabled; since Linux 2.2)</p>
<dd>If this option is enabled, then use the RFC 1122 interpretation of the TCP urgent-pointer field. According to this interpretation, the urgent pointer points to the last byte of urgent data. If this option is disabled, then use the BSD-compatible interpretation of the urgent pointer: the urgent pointer points to the first byte after the urgent data. Enabling this option may lead to interoperability problems.</p>
<dt><i>tcp_syn_retries</i> (integer; default: 6; since Linux 2.2)</p>
<dd>The maximum number of times initial SYNs for an active TCP connection attempt will be retransmitted. This value should not be higher than 255. The default value is 6, which corresponds to retrying for up to approximately 127 seconds. Before Linux 3.7, the default value was 5, which (in conjunction with calculation based on other kernel parameters) corresponded to approximately 180 seconds.</p>
<dt><i>tcp_synack_retries</i> (integer; default: 5; since Linux 2.2)</p>
<dd>The maximum number of times a SYN/ACK segment for a passive TCP connection will be retransmitted. This number should not be higher than 255.</p>
<dt><i>tcp_syncookies</i> (integer; default: 1; since Linux 2.2)</p>
<dd>Enable TCP syncookies. The kernel must be compiled with <code>CONFIG_SYN_COOKIES</code>. The syncookies feature attempts to protect a socket from a SYN flood attack. This should be used as a last resort, if at all. This is a violation of the TCP protocol, and conflicts with other areas of TCP such as TCP extensions. It can cause problems for clients and relays. It is not recommended as a tuning mechanism for heavily loaded servers to help with overloaded or misconfigured conditions. For recommended alternatives see <i>tcp_max_syn_backlog</i>, <i>tcp_synack_retries</i>, and <i>tcp_abort_on_overflow</i>. Set to one of the following values:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Disable TCP syncookies.</p>
<dt>1</p>
<dd>Send out syncookies when the syn backlog queue of a socket overflows.</p>
<dt>2</p>
<dd>(since Linux 3.12) Send out syncookies unconditionally. This can be useful for network testing.</dl>
</dl>
<dt><i>tcp_timestamps</i> (integer; default: 1; since Linux 2.2)</p>
<dd>Set to one of the following values to enable or disable RFC 1323 TCP timestamps:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Disable timestamps.</p>
<dt>1</p>
<dd>Enable timestamps as defined in RFC1323 and use random offset for each connection rather than only using the current time.</p>
<dt>2</p>
<dd>As for the value 1, but without random offsets. Setting <i>tcp_timestamps</i> to this value is meaningful since Linux 4.10.</dl>
</dl>
<dt><i>tcp_tso_win_divisor</i> (integer; default: 3; since Linux 2.6.9)</p>
<dd>This parameter controls what percentage of the congestion window can be consumed by a single TCP Segmentation Offload (TSO) frame. The setting of this parameter is a tradeoff between burstiness and building larger TSO frames.</p>
<dt><i>tcp_tw_recycle</i> (Boolean; default: disabled; Linux 2.4 to 4.11)</p>
<dd>Enable fast recycling of TIME_WAIT sockets. Enabling this option is not recommended as the remote IP may not use monotonically increasing timestamps (devices behind NAT, devices with per-connection timestamp offsets). See RFC 1323 (PAWS) and RFC 6191.</p>
<dt><i>tcp_tw_reuse</i> (Boolean; default: disabled; since Linux 2.4.19/2.6)</p>
<dd>Allow to reuse TIME_WAIT sockets for new connections when it is safe from protocol viewpoint. It should not be changed without advice/request of technical experts.</p>
<dt><i>tcp_vegas_cong_avoid</i> (Boolean; default: disabled; Linux 2.2 to 2.6.13)</p>
<dd>Enable TCP Vegas congestion avoidance algorithm. TCP Vegas is a sender-side-only change to TCP that anticipates the onset of congestion by estimating the bandwidth. TCP Vegas adjusts the sending rate by modifying the congestion window. TCP Vegas should provide less packet loss, but it is not as aggressive as TCP Reno.</p>
<dt><i>tcp_westwood</i> (Boolean; default: disabled; Linux 2.4.26/2.6.3 to 2.6.13)</p>
<dd>Enable TCP Westwood+ congestion control algorithm. TCP Westwood+ is a sender-side-only modification of the TCP Reno protocol stack that optimizes the performance of TCP congestion control. It is based on end-to-end bandwidth estimation to set congestion window and slow start threshold after a congestion episode. Using this estimation, TCP Westwood+ adaptively sets a slow start threshold and a congestion window which takes into account the bandwidth used at the time congestion is experienced. TCP Westwood+ significantly increases fairness with respect to TCP Reno in wired networks and throughput over wireless links.</p>
<dt><i>tcp_window_scaling</i> (Boolean; default: enabled; since Linux 2.2)</p>
<dd>Enable RFC 1323 TCP window scaling. This feature allows the use of a large window (&gt; 64 kB) on a TCP connection, should the other end support it. Normally, the 16 bit window length field in the TCP header limits the window size to less than 64 kB. If larger windows are desired, applications can increase the size of their socket buffers and the window scaling option will be employed. If <i>tcp_window_scaling</i> is disabled, TCP will not negotiate the use of window scaling with the other end during connection setup.</p>
<dt><i>tcp_wmem</i> (since Linux 2.4)</p>
<dd>This is a vector of 3 integers: [min, default, max]. These parameters are used by TCP to regulate send buffer sizes. TCP dynamically adjusts the size of the send buffer from the default values listed below, in the range of these values, depending on memory available.</p>
<dl>
<dd>
<dl>
<dt><i>min</i></p>
<dd>Minimum size of the send buffer used by each TCP socket. The default value is the system page size. (On Linux 2.4, the default value is 4 kB.) This value is used to ensure that in memory pressure mode, allocations below this size will still succeed. This is not used to bound the size of the send buffer declared using <code>SO_SNDBUF</code> on a socket.</p>
<dt><i>default</i></p>
<dd>The default size of the send buffer for a TCP socket. This value overwrites the initial default buffer size from the generic global <i>/proc/sys/net/core/wmem_default</i> defined for all protocols. The default value is 16 kB. If larger send buffer sizes are desired, this value should be increased (to affect all sockets). To employ large TCP windows, the <i>/proc/sys/net/ipv4/tcp_window_scaling</i> must be set to a nonzero value (default).</p>
<dt><i>max</i></p>
<dd>The maximum size of the send buffer used by each TCP socket. This value does not override the value in <i>/proc/sys/net/core/wmem_max</i>. This is not used to limit the size of the send buffer declared using <code>SO_SNDBUF</code> on a socket. The default value is calculated using the formula</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max(65536, min(4 MB,&nbsp;<i>tcp_mem</i>[1]*PAGE_SIZE/128))</p>
<dd>(On Linux 2.4, the default value is 128 kB, lowered 64 kB depending on low-memory systems.)</dl>
</dl>
<dt><i>tcp_workaround_signed_windows</i> (Boolean; default: disabled; since Linux 2.6.26)</p>
<dd>If enabled, assume that no receipt of a window-scaling option means that the remote TCP is broken and treats the window as a signed quantity. If disabled, assume that the remote TCP is not broken even if we do not receive a window scaling option from it.</dl>
<h3>Socket options</h3>
<p>To set or get a TCP socket option, call <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to write the option with the option level argument set to <code>IPPROTO_TCP</code>. Unless otherwise noted, <i>optval</i> is a pointer to an <i>int</i>. In addition, most <code>IPPROTO_IP</code> socket options are valid on TCP sockets. For more information see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). Following is a list of TCP-specific socket options. For details of some other socket options that are also applicable for TCP sockets, see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7).</p>
<dl>
<dt><code>TCP_CONGESTION</code> (since Linux 2.6.13)</p>
<dd>The argument for this option is a string. This option allows the caller to set the TCP congestion control algorithm to be used, on a per-socket basis. Unprivileged processes are restricted to choosing one of the algorithms in <i>tcp_allowed_congestion_control</i> (described above). Privileged processes (<code>CAP_NET_ADMIN</code>) can choose from any of the available congestion-control algorithms (see the description of <i>tcp_available_congestion_control</i> above).</p>
<dt><code>TCP_CORK</code> (since Linux 2.2)</p>
<dd>If set, don&#8217;t send out partial frames. All queued partial frames are sent when the option is cleared again. This is useful for prepending headers before calling <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), or for throughput optimization. As currently implemented, there is a 200 millisecond ceiling on the time for which output is corked by <code>TCP_CORK</code>. If this ceiling is reached, then queued data is automatically transmitted. This option can be combined with <code>TCP_NODELAY</code> only since Linux 2.5.71. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_DEFER_ACCEPT</code> (since Linux 2.4)</p>
<dd>Allow a listener to be awakened only when data arrives on the socket. Takes an integer value (seconds), this can bound the maximum number of attempts TCP will make to complete the connection. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_INFO</code> (since Linux 2.4)</p>
<dd>Used to collect information about this socket. The kernel returns a <i>struct tcp_info</i> as defined in the file <i>/usr/include/linux/tcp.h</i>. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_KEEPCNT</code> (since Linux 2.4)</p>
<dd>The maximum number of keepalive probes TCP should send before dropping the connection. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_KEEPIDLE</code> (since Linux 2.4)</p>
<dd>The time (in seconds) the connection needs to remain idle before TCP starts sending keepalive probes, if the socket option <code>SO_KEEPALIVE</code> has been set on this socket. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_KEEPINTVL</code> (since Linux 2.4)</p>
<dd>The time (in seconds) between individual keepalive probes. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_LINGER2</code> (since Linux 2.4)</p>
<dd>The lifetime of orphaned FIN_WAIT2 state sockets. This option can be used to override the system-wide setting in the file <i>/proc/sys/net/ipv4/tcp_fin_timeout</i> for this socket. This is not to be confused with the <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) level option <code>SO_LINGER</code>. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_MAXSEG</code></p>
<dd>The maximum segment size for outgoing TCP packets. In Linux 2.2 and earlier, and in Linux 2.6.28 and later, if this option is set before connection establishment, it also changes the MSS value announced to the other end in the initial packet. Values greater than the (eventual) interface MTU have no effect. TCP will also impose its minimum and maximum bounds over the value provided.</p>
<dt><code>TCP_NODELAY</code></p>
<dd>If set, disable the Nagle algorithm. This means that segments are always sent as soon as possible, even if there is only a small amount of data. When not set, data is buffered until there is a sufficient amount to send out, thereby avoiding the frequent sending of small packets, which results in poor utilization of the network. This option is overridden by <code>TCP_CORK</code>; however, setting this option forces an explicit flush of pending output, even if <code>TCP_CORK</code> is currently set.</p>
<dt><code>TCP_QUICKACK</code> (since Linux 2.4.4)</p>
<dd>Enable quickack mode if set or disable quickack mode if cleared. In quickack mode, acks are sent immediately, rather than delayed if needed in accordance to normal TCP operation. This flag is not permanent, it only enables a switch to or from quickack mode. Subsequent operation of the TCP protocol will once again enter/leave quickack mode depending on internal protocol processing and factors such as delayed ack timeouts occurring and data transfer. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_SYNCNT</code> (since Linux 2.4)</p>
<dd>Set the number of SYN retransmits that TCP should send before aborting the attempt to connect. It cannot exceed 255. This option should not be used in code intended to be portable.</p>
<dt><code>TCP_USER_TIMEOUT</code> (since Linux 2.6.37)</p>
<dd>This option takes an <i>unsigned int</i> as an argument. When the value is greater than 0, it specifies the maximum amount of time in milliseconds that transmitted data may remain unacknowledged before TCP will forcibly close the corresponding connection and return <code>ETIMEDOUT</code> to the application. If the option value is specified as 0, TCP will use the system default.</p>
<dd>Increasing user timeouts allows a TCP connection to survive extended periods without end-to-end connectivity. Decreasing user timeouts allows applications to &quot;fail fast&quot;, if so desired. Otherwise, failure may take up to 20 minutes with the current system defaults in a normal WAN environment.</p>
<dd>This option can be set during any state of a TCP connection, but is effective only during the synchronized states of a connection (ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT, CLOSING, and LAST-ACK). Moreover, when used with the TCP keepalive (<code>SO_KEEPALIVE</code>) option, <code>TCP_USER_TIMEOUT</code> will override keepalive to determine when to close a connection due to keepalive failure.</p>
<dd>The option has no effect on when TCP retransmits a packet, nor when a keepalive probe is sent.</p>
<dd>This option, like many others, will be inherited by the socket returned by <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), if it was set on the listening socket.</p>
<dd>Further details on the user timeout feature can be found in RFC 793 and RFC 5482 (&quot;TCP User Timeout Option&quot;).</p>
<dt><code>TCP_WINDOW_CLAMP</code> (since Linux 2.4)</p>
<dd>Bound the size of the advertised window to this value. The kernel imposes a minimum size of SOCK_MIN_RCVBUF/2. This option should not be used in code intended to be portable.</dl>
<h3>Sockets API</h3>
<p>TCP provides limited support for out-of-band data, in the form of (a single byte of) urgent data. In Linux this means if the other end sends newer out-of-band data the older urgent data is inserted as normal data into the stream (even when <code>SO_OOBINLINE</code> is not set). This differs from BSD-based stacks. Linux uses the BSD compatible interpretation of the urgent pointer field by default. This violates RFC 1122, but is required for interoperability with other stacks. It can be changed via <i>/proc/sys/net/ipv4/tcp_stdurg</i>. It is possible to peek at out-of-band data using the <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) <code>MSG_PEEK</code> flag. Since version 2.4, Linux supports the use of <code>MSG_TRUNC</code> in the <i>flags</i> argument of <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) (and <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2)). This flag causes the received bytes of data to be discarded, rather than passed back in a caller-supplied buffer. Since Linux 2.4.4, <code>MSG_TRUNC</code> also has this effect when used in conjunction with <code>MSG_OOB</code> to receive out-of-band data.</p>
<h3>Ioctls</h3>
<p>The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls return information in <i>value</i>. The correct syntax is: </p>
<pre><code>int value;
error = ioctl(tcp_socket, ioctl_type, &amp;value);</code></pre>
<p> <i>ioctl_type</i> is one of the following:</p>
<dl>
<dt><code>SIOCINQ</code></p>
<dd>Returns the amount of queued unread data in the receive buffer. The socket must not be in LISTEN state, otherwise an error (<code>EINVAL</code>) is returned. <code>SIOCINQ</code> is defined in <i>&lt;linux/sockios.h&gt;</i>. Alternatively, you can use the synonymous <code>FIONREAD</code>, defined in <i>&lt;sys/ioctl.h&gt;</i>.</p>
<dt><code>SIOCATMARK</code></p>
<dd>Returns true (i.e., <i>value</i> is nonzero) if the inbound data stream is at the urgent mark.</p>
<dd>If the <code>SO_OOBINLINE</code> socket option is set, and <code>SIOCATMARK</code> returns true, then the next read from the socket will return the urgent data. If the <code>SO_OOBINLINE</code> socket option is not set, and <code>SIOCATMARK</code> returns true, then the next read from the socket will return the bytes following the urgent data (to actually read the urgent data requires the <code>recv(MSG_OOB)</code> flag).</p>
<dd>Note that a read never reads across the urgent mark. If an application is informed of the presence of urgent data via <code><a href="/docs/linux/man/2-select/">select</a></code>(2) (using the <i>exceptfds</i> argument) or through delivery of a <code>SIGURG</code> signal, then it can advance up to the mark using a loop which repeatedly tests <code>SIOCATMARK</code> and performs a read (requesting any number of bytes) as long as <code>SIOCATMARK</code> returns false.</p>
<dt><code>SIOCOUTQ</code></p>
<dd>Returns the amount of unsent data in the socket send queue. The socket must not be in LISTEN state, otherwise an error (<code>EINVAL</code>) is returned. <code>SIOCOUTQ</code> is defined in <i>&lt;linux/sockios.h&gt;</i>. Alternatively, you can use the synonymous <code>TIOCOUTQ</code>, defined in <i>&lt;sys/ioctl.h&gt;</i>.</dl>
<h3>Error handling</h3>
<p>When a network error occurs, TCP tries to resend the packet. If it doesn&#8217;t succeed after some time, either <code>ETIMEDOUT</code> or the last received error on this connection is reported. Some applications require a quicker error notification. This can be enabled with the <code>IPPROTO_IP</code> level <code>IP_RECVERR</code> socket option. When this option is enabled, all incoming errors are immediately passed to the user program. Use this option with care &#8212; it makes TCP less tolerant to routing changes and other normal network conditions.</p>
<h2>Errors</h2>
<dl>
<dt><code>EAFNOTSUPPORT</code></p>
<dd>Passed socket address type in <i>sin_family</i> was not <code>AF_INET</code>.</p>
<dt><code>EPIPE</code></p>
<dd>The other end closed the socket unexpectedly or a read is executed on a shut down socket.</p>
<dt><code>ETIMEDOUT</code></p>
<dd>The other end didn&#8217;t acknowledge retransmitted data after some time.</dl>
<p> Any errors defined for <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) or the generic socket layer may also be returned for TCP.</p>
<h2>Versions</h2>
<p>Support for Explicit Congestion Notification, zero-copy <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), reordering support and some SACK extensions (DSACK) were introduced in 2.4. Support for forward acknowledgement (FACK), TIME_WAIT recycling, and per-connection keepalive socket options were introduced in 2.3.</p>
<h2>Bugs</h2>
<p>Not all errors are documented. </p>
<p> IPv6 is not described.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) </p>
<p> The kernel source file <i>Documentation/networking/ip-sysctl.txt</i>. </p>
<p> RFC 793 for the TCP specification.<br />
 RFC 1122 for the TCP requirements and a description of the Nagle algorithm.<br />
 RFC 1323 for TCP timestamp and window scaling options.<br />
 RFC 1337 for a description of TIME_WAIT assassination hazards.<br />
 RFC 3168 for a description of Explicit Congestion Notification.<br />
 RFC 2581 for TCP congestion control algorithms.<br />
 RFC 2018 and RFC 2883 for SACK and extensions to SACK.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
