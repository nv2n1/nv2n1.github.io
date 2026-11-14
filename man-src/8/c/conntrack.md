---
title: "conntrack(8)"
name: "conntrack"
section: "8"
letter: "c"
url: "/docs/linux/man/8-conntrack/"
description: "conntrack – command line interface for netfilter connection tracking"
---

<p>conntrack &#8211; command line interface for netfilter connection tracking</p>
<h2>Synopsis</h2>
<p><code>conntrack -L [table] [options] [-z]</code><br />
 <code>conntrack -G [table] parameters</code><br />
 <code>conntrack -D [table] parameters</code><br />
 <code>conntrack -I [table] parameters</code><br />
 <code>conntrack -U [table] parameters</code><br />
 <code>conntrack -E [table] [options]</code><br />
 <code>conntrack -F [table]</code><br />
 <code>conntrack -C [table]</code><br />
 <code>conntrack -S </code></p>
<h2>Description</h2>
<p>The <code>conntrack</code> utilty provides a full featured userspace interface to the Netfilter connection tracking system that is intended to replace the old /proc/net/ip_conntrack interface. This tool can be used to search, list, inspect and maintain the connection tracking subsystem of the Linux kernel. Using <code>conntrack</code>, you can dump a list of all (or a filtered selection of) currently tracked connections, delete connections from the state table, and even add new ones. In addition, you can also monitor connection tracking events, e.g. show an event message (one line) per newly established connection. </p>
<h2>Tables</h2>
<p>The connection tracking subsystem maintains several internal tables:</p>
<dl>
<dt><code>conntrack</code>:</p>
<dd>This is the default table. It contains a list of all currently tracked connections through the system. If you don&#8217;t use connection tracking exemptions (NOTRACK iptables target), this means all connections that go through the system.</p>
<dt><code>expect</code>:</p>
<dd>This is the table of expectations. Connection tracking expectations are the mechanism used to &quot;expect&quot; <code>RELATED</code> connections to existing ones. Expectations are generally used by &quot;connection tracking helpers&quot; (sometimes called application level gateways [ALGs]) for more complex protocols such as FTP, SIP or H.323.</p>
<dt><code>dying</code>:</p>
<dd>This table shows the conntrack entries, that have expired and that have been destroyed by the connection tracking system itself, or via the <code>conntrack</code> utility.</p>
<dt><code>unconfirmed</code>:</p>
<dd>This table shows new entries, that are not yet inserted into the conntrack table. These entries are attached to packets that are traversing the stack, but did not reach the confirmation point at the postrouting hook. </p>
<p> The tables &quot;dying&quot; and &quot;unconfirmed&quot; are basically only useful for debugging purposes. Under normal operation, it is hard to see entries in any of them. There are corner cases, where it is valid to see entries in the unconfirmed table, eg. when packets that are enqueued via nfqueue, and the dying table, eg. when <code><a href="/docs/linux/man/8-conntrackd/">conntrackd</a>(8)</code> runs in event reliable mode. </p>
</dl>
<h2>Options</h2>
<p>The options recognized by <code>conntrack</code> can be divided into several different groups.</p>
<h3>Commands</h3>
<p>These options specify the particular operation to perform. Only one of them can be specified at any given time.</p>
<dl>
<dt><code>-L &#8211;dump </code></p>
<dd>List connection tracking or expectation table</p>
<dt><code>-G, &#8211;get </code></p>
<dd>Search for and show a particular (matching) entry in the given table.</p>
<dt><code>-D, &#8211;delete </code></p>
<dd>Delete an entry from the given table.</p>
<dt><code>-I, &#8211;create </code></p>
<dd>Create a new entry from the given table.</p>
<dt><code>-U, &#8211;update </code></p>
<dd>Update an entry from the given table.</p>
<dt><code>-E, &#8211;event </code></p>
<dd>Display a real-time event log.</p>
<dt><code>-F, &#8211;flush </code></p>
<dd>Flush the whole given table</p>
<dt><code>-C, &#8211;count </code></p>
<dd>Show the table counter.</p>
<dt><code>-S, &#8211;stats </code></p>
<dd>Show the in-kernel connection tracking system statistics. </p>
</dl>
<h3>Parameters</h3>
<dl>
<dt><code>-z, &#8211;zero </code></p>
<dd>Atomically zero counters after reading them. This option is only valid in combination with the &quot;-L, &#8211;dump&quot; command options.</p>
<dt><code>-o, &#8211;output [extended,xml,timestamp,id,ktimestamp,labels] </code></p>
<dd>Display output in a certain format. With the extended output option, this tool displays the layer 3 information. With ktimestamp, it displays the in-kernel timestamp available since 2.6.38 (you can enable it via the <code><a href="/docs/linux/man/8-sysctl/">sysctl</a>(8)</code> key <code>net.netfilter.nf_conntrack_timestamp</code>). The labels output option tells <code>conntrack</code> to show the names of connection tracking labels that might be present.</p>
<dt><code>-e, &#8211;event-mask </code><i>[ALL|NEW|UPDATES|DESTROY][,&#8230;]</i></p>
<dd>Set the bitmask of events that are to be generated by the in-kernel ctnetlink event code. Using this parameter, you can reduce the event messages generated by the kernel to those types to those that you are actually interested in. This option can only be used in conjunction with &quot;-E, &#8211;event&quot;.</p>
<dt><code>-b, &#8211;buffer-size </code><i>value</i></p>
<dd>Set the Netlink socket buffer size in bytes. This option is useful if the command line tool reports ENOBUFS errors. If you do not pass this option, the default value available at <code><a href="/docs/linux/man/8-sysctl/">sysctl</a>(8)</code> key <code>net.core.rmem_default</code> is used. The tool reports this problem if your process is too slow to handle all the event messages or, in other words, if the amount of events are big enough to overrun the socket buffer. Note that using a big buffer reduces the chances to hit ENOBUFS, however, this results in more memory consumption. This option can only be used in conjunction with &quot;-E, &#8211;event&quot;. </p>
</dl>
<h3>Filter Parameters</h3>
<dl>
<dt><code>-s, &#8211;src, &#8211;orig-src </code><i>IP_ADDRESS</i></p>
<dd>Match only entries whose source address in the original direction equals the one specified as argument. Implies &quot;&#8211;mask-src&quot; when CIDR notation is used.</p>
<dt><code>-d, &#8211;dst, &#8211;orig-dst </code><i>IP_ADDRESS</i></p>
<dd>Match only entries whose destination address in the original direction equals the one specified as argument. Implies &quot;&#8211;mask-dst&quot; when CIDR notation is used.</p>
<dt><code>-r, &#8211;reply-src </code><i>IP_ADDRESS</i></p>
<dd>Match only entries whose source address in the reply direction equals the one specified as argument.</p>
<dt><code>-q, &#8211;reply-dst </code><i>IP_ADDRESS</i></p>
<dd>Match only entries whose destination address in the reply direction equals the one specified as argument.</p>
<dt><code>-p, &#8211;proto </code><i>PROTO </i></p>
<dd>Specify layer four (TCP, UDP, &#8230;) protocol.</p>
<dt><code>-f, &#8211;family </code><i>PROTO</i></p>
<dd>Specify layer three (ipv4, ipv6) protocol This option is only required in conjunction with &quot;-L, &#8211;dump&quot;. If this option is not passed, the default layer 3 protocol will be IPv4.</p>
<dt><code>-t, &#8211;timeout </code><i>TIMEOUT</i></p>
<dd>Specify the timeout.</p>
<dt><code>-m, &#8211;mark </code><i>MARK[/MASK]</i></p>
<dd>Specify the conntrack mark. Optionally, a mask value can be specified. In &quot;&#8211;update&quot; mode, this mask specifies the bits that should be zeroed before XORing the MARK value into the ctmark. Otherwise, the mask is logically ANDed with the existing mark before the comparision. In &quot;&#8211;create&quot; mode, the mask is ignored.</p>
<dt><code>-l, &#8211;label </code><i>LABEL</i></p>
<dd>Specify a conntrack label. This option is only available in conjunction with &quot;-L, &#8211;dump&quot;, &quot;-E, &#8211;event&quot;, &quot;-U &#8211;update&quot; or &quot;-D &#8211;delete&quot;. Match entries whose labels match at least those specified. Use multiple -l commands to specify multiple labels that need to be set. Match entries whose labels matches at least those specified as arguments.</p>
<dt><code>&#8211;label-add </code><i>LABEL</i></p>
<dd>Specify the conntrack label to add to to the selected conntracks. This option is only available in conjunction with &quot;-I, &#8211;create&quot; or &quot;-U, &#8211;update&quot;.</p>
<dt><code>&#8211;label-del </code><i>[LABEL]</i></p>
<dd>Specify the conntrack label to delete from the selected conntracks. If no label is given, all labels are deleted. This option is only available in conjunction with &quot;-U, &#8211;update&quot;.</p>
<dt><code>-c, &#8211;secmark </code><i>SECMARK</i></p>
<dd>Specify the conntrack selinux security mark.</p>
<dt><code>-u, &#8211;status </code><i>[ASSURED|SEEN_REPLY|FIXED_TIMEOUT|EXPECTED|UNSET][,&#8230;]</i></p>
<dd>Specify the conntrack status.</p>
<dt><code>-n, &#8211;src-nat </code></p>
<dd>Filter source NAT connections.</p>
<dt><code>-g, &#8211;dst-nat </code></p>
<dd>Filter destination NAT connections.</p>
<dt><code>-j, &#8211;any-nat </code></p>
<dd>Filter any NAT connections.</p>
<dt><code>-w, &#8211;zone </code></p>
<dd>Filter by conntrack zone. See iptables CT target for more information.</p>
<dt><code>&#8211;orig-zone </code></p>
<dd>Filter by conntrack zone in original direction. See iptables CT target for more information.</p>
<dt><code>&#8211;reply-zone </code></p>
<dd>Filter by conntrack zone in reply direction. See iptables CT target for more information.</p>
<dt><code>&#8211;tuple-src </code><i>IP_ADDRESS</i></p>
<dd>Specify the tuple source address of an expectation. Implies &quot;&#8211;mask-src&quot; when CIDR notation is used.</p>
<dt><code>&#8211;tuple-dst </code><i>IP_ADDRESS</i></p>
<dd>Specify the tuple destination address of an expectation. Implies &quot;&#8211;mask-dst&quot; when CIDR notation is used.</p>
<dt><code>&#8211;mask-src </code><i>IP_ADDRESS</i></p>
<dd>Specify the source address mask. For conntracks this option is only available in conjunction with &quot;-L, &#8211;dump&quot;, &quot;-E, &#8211;event&quot;, &quot;-U &#8211;update&quot; or &quot;-D &#8211;delete&quot;. For expectations this option is only available in conjunction with &quot;-I, &#8211;create&quot;.</p>
<dt><code>&#8211;mask-dst </code><i>IP_ADDRESS</i></p>
<dd>Specify the destination address mask. Same limitations as for &quot;&#8211;mask-src&quot;. </p>
</dl>
<h3>Protocol Filter Parameters</h3>
<dl>
<dt>TCP-specific fields:</p>
<dd>
<dt><code>&#8211;sport, &#8211;orig-port-src </code><i>PORT</i></p>
<dd>Source port in original direction</p>
<dt><code>&#8211;dport, &#8211;orig-port-dst </code><i>PORT</i></p>
<dd>Destination port in original direction</p>
<dt><code>&#8211;reply-port-src </code><i>PORT</i></p>
<dd>Source port in reply direction</p>
<dt><code>&#8211;reply-port-dst </code><i>PORT</i></p>
<dd>Destination port in reply direction</p>
<dt><code>&#8211;state </code><i>state</i></p>
<dd>TCP state, one of NONE, SYN_SENT, SYN_RECV, ESTABLISHED, FIN_WAIT, CLOSE_WAIT, LAST_ACK, TIME_WAIT, CLOSE or LISTEN. </p>
<dt>UDP-specific fields:</p>
<dd>
<dt><code>&#8211;sport, &#8211;orig-port-src </code><i>PORT</i></p>
<dd>Source port in original direction</p>
<dt><code>&#8211;dport, &#8211;orig-port-dst </code><i>PORT</i></p>
<dd>Destination port in original direction</p>
<dt><code>&#8211;reply-port-src </code><i>PORT</i></p>
<dd>Source port in reply direction</p>
<dt><code>&#8211;reply-port-dst </code><i>PORT</i></p>
<dd>Destination port in reply direction </p>
<dt>ICMP-specific fields:</p>
<dd>
<dt><code>&#8211;icmp-type </code><i>TYPE</i></p>
<dd>ICMP Type. Has to be specified numerically.</p>
<dt><code>&#8211;icmp-code </code><i>CODE</i></p>
<dd>ICMP Code. Has to be specified numerically.</p>
<dt><code>&#8211;icmp-id </code><i>ID</i></p>
<dd>ICMP Id. Has to be specified numerically (non-mandatory) </p>
<dt>UDPlite-specific fields:</p>
<dd>
<dt><code>&#8211;sport, &#8211;orig-port-src </code><i>PORT</i></p>
<dd>Source port in original direction</p>
<dt><code>&#8211;dport, &#8211;orig-port-dst </code><i>PORT</i></p>
<dd>Destination port in original direction</p>
<dt><code>&#8211;reply-port-src </code><i>PORT</i></p>
<dd>Source port in reply direction</p>
<dt><code>&#8211;reply-port-dst </code><i>PORT</i></p>
<dd>Destination port in reply direction </p>
<dt>SCTP-specific fields:</p>
<dd>
<dt><code>&#8211;sport, &#8211;orig-port-src </code><i>PORT</i></p>
<dd>Source port in original direction</p>
<dt><code>&#8211;dport, &#8211;orig-port-dst </code><i>PORT</i></p>
<dd>Destination port in original direction</p>
<dt><code>&#8211;reply-port-src </code><i>PORT</i></p>
<dd>Source port in reply direction</p>
<dt><code>&#8211;reply-port-dst </code><i>PORT</i></p>
<dd>Destination port in reply direction</p>
<dt><code>&#8211;state </code><i>state</i></p>
<dd>SCTP state, one of NONE, CLOSED, COOKIE_WAIT, COOKIE_ECHOED, ESTABLISHED, SHUTDOWN_SENT, SHUTDOWN_RECD, SHUTDOWN_ACK_SENT.</p>
<dt><code>&#8211;orig-vtag </code><i>value</i></p>
<dd>Verification tag (32-bits value) in the original direction</p>
<dt><code>&#8211;reply-vtag </code><i>value</i></p>
<dd>Verification tag (32-bits value) in the reply direction </p>
<dt>DCCP-specific fields (needs Linux &gt;= 2.6.30):</p>
<dd>
<dt><code>&#8211;sport, &#8211;orig-port-src </code><i>PORT</i></p>
<dd>Source port in original direction</p>
<dt><code>&#8211;dport, &#8211;orig-port-dst </code><i>PORT</i></p>
<dd>Destination port in original direction</p>
<dt><code>&#8211;reply-port-src </code><i>PORT</i></p>
<dd>Source port in reply direction</p>
<dt><code>&#8211;reply-port-dst </code><i>PORT</i></p>
<dd>Destination port in reply direction</p>
<dt><code>&#8211;state </code><i>state</i></p>
<dd>DCCP state, one of NONE, REQUEST, RESPOND, PARTOPEN, OPEN, CLOSEREQ, CLOSING, TIMEWAIT.</p>
<dt><code>&#8211;role </code><i>[client|server]</i></p>
<dd>Role that the original conntrack tuple is tracking </p>
<dt>GRE-specific fields:</p>
<dd>
<dt><code>&#8211;srckey, &#8211;orig-key-src </code><i>KEY</i></p>
<dd>Source key in original direction (in hexadecimal or decimal)</p>
<dt><code>&#8211;dstkey, &#8211;orig-key-dst </code><i>KEY</i></p>
<dd>Destination key in original direction (in hexadecimal or decimal)</p>
<dt><code>&#8211;reply-key-src </code><i>KEY</i></p>
<dd>Source key in reply direction (in hexadecimal or decimal)</p>
<dt><code>&#8211;reply-key-dst </code><i>KEY</i></p>
<dd>Destination key in reply direction (in hexadecimal or decimal) </p>
</dl>
<h2>Diagnostics</h2>
<p>The exit code is 0 for correct function. Errors which appear to be caused by invalid command line parameters cause an exit code of 2. Any other errors cause an exit code of 1.</p>
<h2>Examples</h2>
<dl>
<dt><code>conntrack -L</code></p>
<dd>Show the connection tracking table in /proc/net/ip_conntrack format</p>
<dt><code>conntrack -L -o extended</code></p>
<dd>Show the connection tracking table in /proc/net/nf_conntrack format, with additional information.</p>
<dt><code>conntrack -L -o xml</code></p>
<dd>Show the connection tracking table in XML</p>
<dt><code>conntrack -L -f ipv6 -o extended</code></p>
<dd>Only dump IPv6 connections in /proc/net/nf_conntrack format, with additional information.</p>
<dt><code>conntrack -L &#8211;src-nat</code></p>
<dd>Show source NAT connections</p>
<dt><code>conntrack -E -o timestamp</code></p>
<dd>Show connection events together with the timestamp</p>
<dt><code>conntrack -D -s 1.2.3.4</code></p>
<dd>Delete all flow whose source address is 1.2.3.4</p>
<dt><code>conntrack -U -s 1.2.3.4 -m 1</code></p>
<dd>Set connmark to 1 of all the flows whose source address is 1.2.3.4 </p>
<h2>Bugs</h2>
<p>Please, report them to netfilter-devel [at] vger.kernel.org or file a bug in Netfilter&#8217;s bugzilla (<a rel="nofollow" href="https://bugzilla.netfilter.org">https://bugzilla.netfilter.org</a>). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nftables/">nftables</a></code>(8),<code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8),<code><a href="/docs/linux/man/8-conntrackd/">conntrackd</a>(8)</code><br />
 See <code><a rel="nofollow" href="http://conntrack-tools.netfilter.org">http://conntrack-tools.netfilter.org</a></code> </p>
<h2>Authors</h2>
<p>Jay Schulist, Patrick McHardy, Harald Welte and Pablo Neira Ayuso wrote the kernel-level &quot;ctnetlink&quot; interface that is used by the conntrack tool. </p>
<p> Pablo Neira Ayuso wrote and maintain the conntrack tool, Harald Welte added support for conntrack based accounting counters. </p>
<p> Man page written by Harald Welte &lt;laforge [at] netfilter.org&gt; and Pablo Neira Ayuso &lt;pablo [at] netfilter.org&gt;.</p>
