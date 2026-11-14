---
title: "ss(8)"
name: "ss"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ss/"
description: "ss – another utility to investigate sockets"
---

<p>ss &#8211; another utility to investigate sockets</p>
<h2>Synopsis</h2>
<p><code>ss</code> [<i>options</i>]<i> [ FILTER ]</i></p>
<h2>Description</h2>
<p><code>ss</code> is used to dump socket statistics. It allows showing information similar to <i>netstat</i>. It can display more TCP and state information than other tools. </p>
<h2>Options</h2>
<p>When no option is used ss displays a list of open non-listening sockets (e.g. TCP/UNIX/UDP) that have established connection.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Output version information.</p>
<dt><code>-H, &#8211;no-header</code></p>
<dd>Suppress header line.</p>
<dt><code>-O, &#8211;oneline</code></p>
<dd>Print each socket&#8217;s data on a single line.</p>
<dt><code>-n, &#8211;numeric</code></p>
<dd>Do not try to resolve service names. Show exact bandwidth values, instead of human-readable.</p>
<dt><code>-r, &#8211;resolve</code></p>
<dd>Try to resolve numeric address/ports.</p>
<dt><code>-a, &#8211;all</code></p>
<dd>Display both listening and non-listening (for TCP this means established connections) sockets.</p>
<dt><code>-l, &#8211;listening</code></p>
<dd>Display only listening sockets (these are omitted by default).</p>
<dt><code>-o, &#8211;options</code></p>
<dd>Show timer information. For TCP protocol, the output format is:</p>
<dl>
<dd>timer:(&lt;timer_name&gt;,&lt;expire_time&gt;,&lt;retrans&gt;) </p>
<dl>
<dt><code>&lt;timer_name&gt;</code></p>
<dd>the name of the timer, there are five kind of timer names:</p>
<dl>
<dd><code>on</code> : means one of these timers: TCP retrans timer, TCP early retrans timer and tail loss probe timer </p>
<p> <code>keepalive</code>: tcp keep alive timer </p>
<p> <code>timewait</code>: timewait stage timer </p>
<p> <code>persist</code>: zero window probe timer </p>
<p> <code>unknown</code>: none of the above timers</dl>
<dt><code>&lt;expire_time&gt;</code></p>
<dd>how long time the timer will expire</dl>
<dl>
<dt><code>&lt;retrans&gt;</code></p>
<dd>how many times the retransmission occurred</dl>
</dl>
<dt><code>-e, &#8211;extended</code></p>
<dd>Show detailed socket information. The output format is:</p>
<dl>
<dd>uid:&lt;uid_number&gt; ino:&lt;inode_number&gt; sk:&lt;cookie&gt; </p>
<dl>
<dt><code>&lt;uid_number&gt;</code></p>
<dd>the user id the socket belongs to</dl>
<dl>
<dt><code>&lt;inode_number&gt;</code></p>
<dd>the socket&#8217;s inode number in VFS</dl>
<dl>
<dt><code>&lt;cookie&gt;</code></p>
<dd>an uuid of the socket</dl>
</dl>
<dt><code>-m, &#8211;memory</code></p>
<dd>Show socket memory usage. The output format is:</p>
<dl>
<dd>skmem:(r&lt;rmem_alloc&gt;,rb&lt;rcv_buf&gt;,t&lt;wmem_alloc&gt;,tb&lt;snd_buf&gt;, </p>
<dl>
<dd>
<dl>
<dd>f&lt;fwd_alloc&gt;,w&lt;wmem_queued&gt;,o&lt;opt_mem&gt;,</dl>
</dl>
<dl>
<dd>
<dl>
<dd>bl&lt;back_log&gt;,d&lt;sock_drop&gt;)</dl>
</dl>
<dl>
<dt><code>&lt;rmem_alloc&gt;</code></p>
<dd>the memory allocated for receiving packet</dl>
<dl>
<dt><code>&lt;rcv_buf&gt;</code></p>
<dd>the total memory can be allocated for receiving packet</dl>
<dl>
<dt><code>&lt;wmem_alloc&gt;</code></p>
<dd>the memory used for sending packet (which has been sent to layer 3)</dl>
<dl>
<dt><code>&lt;snd_buf&gt;</code></p>
<dd>the total memory can be allocated for sending packet</dl>
<dl>
<dt><code>&lt;fwd_alloc&gt;</code></p>
<dd>the memory allocated by the socket as cache, but not used for receiving/sending packet yet. If need memory to send/receive packet, the memory in this cache will be used before allocate additional memory.</dl>
<dl>
<dt><code>&lt;wmem_queued&gt;</code></p>
<dd>The memory allocated for sending packet (which has not been sent to layer 3)</dl>
<dl>
<dt><code>&lt;ropt_mem&gt;</code></p>
<dd>The memory used for storing socket option, e.g., the key for TCP MD5 signature</dl>
<dl>
<dt><code>&lt;back_log&gt;</code></p>
<dd>The memory used for the sk backlog queue. On a process context, if the process is receiving packet, and a new packet is received, it will be put into the sk backlog queue, so it can be received by the process immediately</dl>
<dl>
<dt><code>&lt;sock_drop&gt;</code></p>
<dd>the number of packets dropped before they are de-multiplexed into the socket</dl>
</dl>
<dt><code>-p, &#8211;processes</code></p>
<dd>Show process using socket.</p>
<dt><code>-i, &#8211;info</code></p>
<dd>Show internal TCP information. Below fields may appear:</p>
<dl>
<dd>
<dl>
<dt><code>ts</code></p>
<dd>show string &quot;ts&quot; if the timestamp option is set</dl>
<dl>
<dt><code>sack</code></p>
<dd>show string &quot;sack&quot; if the sack option is set</dl>
<dl>
<dt><code>ecn</code></p>
<dd>show string &quot;ecn&quot; if the explicit congestion notification option is set</dl>
<dl>
<dt><code>ecnseen</code></p>
<dd>show string &quot;ecnseen&quot; if the saw ecn flag is found in received packets</dl>
<dl>
<dt><code>fastopen</code></p>
<dd>show string &quot;fastopen&quot; if the fastopen option is set</dl>
<dl>
<dt><code>cong_alg</code></p>
<dd>the congestion algorithm name, the default congestion algorithm is &quot;cubic&quot;</dl>
<dl>
<dt><code>wscale:&lt;snd_wscale&gt;:&lt;rcv_wscale&gt;</code></p>
<dd>if window scale option is used, this field shows the send scale factor and receive scale factor</dl>
<dl>
<dt><code>rto:&lt;icsk_rto&gt;</code></p>
<dd>tcp re-transmission timeout value, the unit is millisecond</dl>
<dl>
<dt><code>backoff:&lt;icsk_backoff&gt;</code></p>
<dd>used for exponential backoff re-transmission, the actual re-transmission timeout value is icsk_rto &lt;&lt; icsk_backoff</dl>
<dl>
<dt><code>rtt:&lt;rtt&gt;/&lt;rttvar&gt;</code></p>
<dd>rtt is the average round trip time, rttvar is the mean deviation of rtt, their units are millisecond</dl>
<dl>
<dt><code>ato:&lt;ato&gt;</code></p>
<dd>ack timeout, unit is millisecond, used for delay ack mode</dl>
<dl>
<dt><code>mss:&lt;mss&gt;</code></p>
<dd>max segment size</dl>
<dl>
<dt><code>cwnd:&lt;cwnd&gt;</code></p>
<dd>congestion window size</dl>
<dl>
<dt><code>pmtu:&lt;pmtu&gt;</code></p>
<dd>path MTU value</dl>
<dl>
<dt><code>ssthresh:&lt;ssthresh&gt;</code></p>
<dd>tcp congestion window slow start threshold</dl>
<dl>
<dt><code>bytes_acked:&lt;bytes_acked&gt;</code></p>
<dd>bytes acked</dl>
<dl>
<dt><code>bytes_received:&lt;bytes_received&gt;</code></p>
<dd>bytes received</dl>
<dl>
<dt><code>segs_out:&lt;segs_out&gt;</code></p>
<dd>segments sent out</dl>
<dl>
<dt><code>segs_in:&lt;segs_in&gt;</code></p>
<dd>segments received</dl>
<dl>
<dt><code>send &lt;send_bps&gt;bps</code></p>
<dd>egress bps</dl>
<dl>
<dt><code>lastsnd:&lt;lastsnd&gt;</code></p>
<dd>how long time since the last packet sent, the unit is millisecond</dl>
<dl>
<dt><code>lastrcv:&lt;lastrcv&gt;</code></p>
<dd>how long time since the last packet received, the unit is millisecond</dl>
<dl>
<dt><code>lastack:&lt;lastack&gt;</code></p>
<dd>how long time since the last ack received, the unit is millisecond</dl>
<dl>
<dt><code>pacing_rate &lt;pacing_rate&gt;bps/&lt;max_pacing_rate&gt;bps</code></p>
<dd>the pacing rate and max pacing rate</dl>
<dl>
<dt><code>rcv_space:&lt;rcv_space&gt;</code></p>
<dd>a helper variable for TCP internal auto tuning socket receive buffer</dl>
<dl>
<dt><code>tcp-ulp-mptcp flags:[MmBbJjecv] token:&lt;rem_token(rem_id)/loc_token(loc_id)&gt; seq:&lt;sn&gt; sfseq:&lt;ssn&gt; ssnoff:&lt;off&gt; maplen:&lt;maplen&gt;</code></p>
<dd>MPTCP subflow information</dl>
</dl>
<dt><code>&#8211;tos</code></p>
<dd>Show ToS and priority information. Below fields may appear:</p>
<dl>
<dd>
<dl>
<dt><code>tos</code></p>
<dd>IPv4 Type-of-Service byte</dl>
<dl>
<dt><code>tclass</code></p>
<dd>IPv6 Traffic Class byte</dl>
<dl>
<dt><code>class_id</code></p>
<dd>Class id set by net_cls cgroup. If class is zero this shows priority set by SO_PRIORITY.</dl>
</dl>
<dt><code>&#8211;cgroup</code></p>
<dd>Show cgroup information. Below fields may appear:</p>
<dl>
<dd>
<dl>
<dt><code>cgroup</code></p>
<dd>Cgroup v2 pathname. This pathname is relative to the mount point of the hierarchy.</dl>
</dl>
<dt><code>-K, &#8211;kill</code></p>
<dd>Attempts to forcibly close sockets. This option displays sockets that are successfully closed and silently skips sockets that the kernel does not support closing. It supports IPv4 and IPv6 sockets only.</p>
<dt><code>-s, &#8211;summary</code></p>
<dd>Print summary statistics. This option does not parse socket lists obtaining summary from various sources. It is useful when amount of sockets is so huge that parsing /proc/net/tcp is painful.</p>
<dt><code>-E, &#8211;events</code></p>
<dd>Continually display sockets as they are destroyed</p>
<dt><code>-Z, &#8211;context</code></p>
<dd>As the <code>-p</code> option but also shows process security context. </p>
<p> For <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) sockets the initiating process context is displayed as follows:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>If valid pid show the process context.</p>
<dt>2.</p>
<dd>If destination is kernel (pid = 0) show kernel initial context.</p>
<dt>3.</p>
<dd>If a unique identifier has been allocated by the kernel or netlink user, show context as &quot;unavailable&quot;. This will generally indicate that a process has more than one netlink socket active.</dl>
</dl>
</dl>
<dt><code>-z, &#8211;contexts</code></p>
<dd>As the <code>-Z</code> option but also shows the socket context. The socket context is taken from the associated inode and is not the actual socket context held by the kernel. Sockets are typically labeled with the context of the creating process, however the context shown will reflect any policy role, type and/or range transition rules applied, and is therefore a useful reference.</p>
<dt><code>-N NSNAME, &#8211;net=NSNAME</code></p>
<dd>Switch to the specified network namespace name.</p>
<dt><code>-b, &#8211;bpf</code></p>
<dd>Show socket classic BPF filters (only administrators are allowed to get these information).</p>
<dt><code>-4, &#8211;ipv4</code></p>
<dd>Display only IP version 4 sockets (alias for -f inet).</p>
<dt><code>-6, &#8211;ipv6</code></p>
<dd>Display only IP version 6 sockets (alias for -f inet6).</p>
<dt><code>-0, &#8211;packet</code></p>
<dd>Display PACKET sockets (alias for -f link).</p>
<dt><code>-t, &#8211;tcp</code></p>
<dd>Display TCP sockets.</p>
<dt><code>-u, &#8211;udp</code></p>
<dd>Display UDP sockets.</p>
<dt><code>-d, &#8211;dccp</code></p>
<dd>Display DCCP sockets.</p>
<dt><code>-w, &#8211;raw</code></p>
<dd>Display RAW sockets.</p>
<dt><code>-x, &#8211;unix</code></p>
<dd>Display Unix domain sockets (alias for -f unix).</p>
<dt><code>-S, &#8211;sctp</code></p>
<dd>Display SCTP sockets.</p>
<dt><code>&#8211;vsock</code></p>
<dd>Display vsock sockets (alias for -f vsock).</p>
<dt><code>&#8211;xdp</code></p>
<dd>Display XDP sockets (alias for -f xdp).</p>
<dt><code>&#8211;inet-sockopt</code></p>
<dd>Display inet socket options.</p>
<dt><code>-f FAMILY, &#8211;family=FAMILY</code></p>
<dd>Display sockets of type FAMILY. Currently the following families are supported: unix, inet, inet6, link, netlink, vsock, xdp.</p>
<dt><code>-A QUERY, &#8211;query=QUERY, &#8211;socket=QUERY</code></p>
<dd>List of socket tables to dump, separated by commas. The following identifiers are understood: all, inet, tcp, udp, raw, unix, packet, netlink, unix_dgram, unix_stream, unix_seqpacket, packet_raw, packet_dgram, dccp, sctp, vsock_stream, vsock_dgram, xdp Any item in the list may optionally be prefixed by an exclamation mark (<code>!</code>) to exclude that socket table from being dumped.</p>
<dt><code>-D FILE, &#8211;diag=FILE</code></p>
<dd>Do not display anything, just dump raw information about TCP sockets to FILE after applying filters. If FILE is &#8211; stdout is used.</p>
<dt><code>-F FILE, &#8211;filter=FILE</code></p>
<dd>Read filter information from FILE. Each line of FILE is interpreted like single command line option. If FILE is &#8211; stdin is used.</p>
<dt><code>FILTER := [ state STATE-FILTER ] [ EXPRESSION ]</code></p>
<dd>Please take a look at the official documentation for details regarding filters. </p>
</dl>
<h2>State-Filter</h2>
<p><code>STATE-FILTER</code> allows to construct arbitrary set of states to match. Its syntax is sequence of keywords state and exclude followed by identifier of state.</p>
<dl>
<dt>Available identifiers are:</p>
<dd>All standard TCP states: <code>established</code>, <code>syn-sent</code>, <code>syn-recv</code>, <code>fin-wait-1</code>, <code>fin-wait-2</code>, <code>time-wait</code>, <code>closed</code>, <code>close-wait</code>, <code>last-ack</code>, <code>listening</code> and <code>closing.</code> </p>
<p> <code>all</code> &#8211; for all the states </p>
<p> <code>connected</code> &#8211; all the states except for <code>listening</code> and <code>closed</code> </p>
<p> <code>synchronized</code> &#8211; all the <code>connected</code> states except for <code>syn-sent</code> </p>
<p> <code>bucket</code> &#8211; states, which are maintained as minisockets, i.e. <code>time-wait</code> and <code>syn-recv</code> </p>
<p> <code>big</code> &#8211; opposite to <code>bucket</code> </p>
</dl>
<h2>Expression</h2>
<p><code>EXPRESSION</code> allows filtering based on specific criteria. <code>EXPRESSION</code> consists of a series of predicates combined by boolean operators. The possible operators in increasing order of precedence are <code>or</code> (or | or ||), <code>and</code> (or &amp; or &amp;&amp;), and <code>not</code> (or !). If no operator is between consecutive predicates, an implicit <code>and</code> operator is assumed. Subexpressions can be grouped with &quot;(&quot; and &quot;)&quot;. </p>
<p> The following predicates are supported: </p>
<dl>
<dt><code>{dst|src} [=] HOST</code></p>
<dd>Test if the destination or source matches HOST. See HOST SYNTAX for details.</p>
<dt><code>{dport|sport} [OP] [FAMILY:]:PORT</code></p>
<dd>Compare the destination or source port to PORT. OP can be any of &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;=&quot;, &quot;!=&quot;, &quot;&gt;=&quot; and &quot;&gt;&quot;. Following normal arithmetic rules. FAMILY and PORT are as described in HOST SYNTAX below.</p>
<dt><code>dev [=|!=] DEVICE</code></p>
<dd>Match based on the device the connection uses. DEVICE can either be a device name or the index of the interface.</p>
<dt><code>fwmark [=|!=] MASK</code></p>
<dd>Matches based on the fwmark value for the connection. This can either be a specific mark value or a mark value followed by a &quot;/&quot; and a bitmask of which bits to use in the comparison. For example &quot;fwmark = 0x01/0x03&quot; would match if the two least significant bits of the fwmark were 0x01.</p>
<dt><code>cgroup [=|!=] PATH</code></p>
<dd>Match if the connection is part of a cgroup at the given path.</p>
<dt><code>autobound</code></p>
<dd>Match if the port or path of the source address was automatically allocated (rather than explicitly specified).</dl>
<p> Most operators have aliases. If no operator is supplied &quot;=&quot; is assumed. Each of the following groups of operators are all equivalent:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>= == eq</p>
<dt>&bull;</p>
<dd>!= ne neq</p>
<dt>&bull;</p>
<dd>&gt; gt</p>
<dt>&bull;</p>
<dd>&lt; lt</p>
<dt>&bull;</p>
<dd>&gt;= ge geq</p>
<dt>&bull;</p>
<dd>&lt;= le leq</p>
<dt>&bull;</p>
<dd>! not</p>
<dt>&bull;</p>
<dd>| || or</p>
<dt>&bull;</p>
<dd>&amp; &amp;&amp; and</dl>
</dl>
<h2>Host Syntax</h2>
<p>The general host syntax is [FAMILY:]ADDRESS[:PORT]. </p>
<p> FAMILY must be one of the families supported by the -f option. If not given it defaults to the family given with the -f option, and if that is also missing, will assume either inet or inet6. Note that all host conditions in the expression should either all be the same family or be only inet and inet6. If there is some other mixture of families, the results will probably be unexpected. </p>
<p> The form of ADDRESS and PORT depends on the family used. &quot;*&quot; can be used as a wildcard for either the address or port. The details for each family are as follows:</p>
<dl>
<dt><code>unix</code></p>
<dd>ADDRESS is a glob pattern (see <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3)) that will be matched case-insensitively against the unix socket&#8217;s address. Both path and abstract names are supported. Unix addresses do not support a port, and &quot;*&quot; cannot be used as a wildcard.</p>
<dt><code>link</code></p>
<dd>ADDRESS is the case-insensitive name of an Ethernet protocol to match. PORT is either a device name or a device index for the desired link device, as seen in the output of ip link.</p>
<dt><code>netlink</code></p>
<dd>ADDRESS is a descriptor of the netlink family. Possible values come from /etc/iproute2/nl_protos. PORT is the port id of the socket, which is usually the same as the owning process id. The value &quot;kernel&quot; can be used to represent the kernel (port id of 0).</p>
<dt><code>vsock</code></p>
<dd>ADDRESS is an integer representing the CID address, and PORT is the port.</p>
<dt><code>inet</code>&nbsp;and&nbsp;<code>inet6</code></p>
<dd>ADDRESS is an ip address (either v4 or v6 depending on the family) or a DNS hostname that resolves to an ip address of the required version. An ipv6 address must be enclosed in &quot;[&quot; and &quot;]&quot; to disambiguate the port separator. The address may additionally have a prefix length given in CIDR notation (a slash followed by the prefix length in bits). PORT is either the numerical socket port, or the service name for the port to match. </p>
</dl>
<h2>Usage Examples</h2>
<dl>
<dt><code>ss -t -a</code></p>
<dd>Display all TCP sockets.</p>
<dt><code>ss -t -a -Z</code></p>
<dd>Display all TCP sockets with process SELinux security contexts.</p>
<dt><code>ss -u -a</code></p>
<dd>Display all UDP sockets.</p>
<dt><code>ss -o state established &#8216;( dport = :ssh or sport = :ssh )&#8217;</code></p>
<dd>Display all established ssh connections.</p>
<dt><code>ss -x src /tmp/.X11-unix/*</code></p>
<dd>Find all local processes connected to X server.</p>
<dt><code>ss -o state fin-wait-1 &#8216;( sport = :http or sport = :https )&#8217; dst 193.233.7/24</code></p>
<dd>List all the tcp sockets in state FIN-WAIT-1 for our apache to network 193.233.7/24 and look at their timers.</p>
<dt><code>ss -a -A &#8216;all,!tcp&#8217;</code></p>
<dd>List sockets in all states from all socket tables but TCP.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8),<br />
 <code>RFC</code> 793 &#8211; <a rel="nofollow" href="https://tools.ietf.org/rfc/rfc793.txt">https://tools.ietf.org/rfc/rfc793.txt</a> (TCP states) </p>
<h2>Author</h2>
<p><i>ss</i> was written by Alexey Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt;. </p>
<p> This manual page was written by Michael Prokop &lt;mika [at] grml.org&gt; for the Debian project (but may be used by others).</p>
