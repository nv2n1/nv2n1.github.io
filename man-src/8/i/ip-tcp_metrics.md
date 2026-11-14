---
title: "ip-tcp_metrics(8)"
name: "ip-tcp_metrics"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-tcp_metrics/"
description: "ip-tcp_metrics – management for TCP Metrics"
---

<p>ip-tcp_metrics &#8211; management for TCP Metrics</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

tcp_metrics

{ COMMAND |

    help }
</code></pre>
<p> <code>ip tcp_metrics</code> { <code>show</code> | <code>flush</code> } <i>SELECTOR</i><br />
 <code>ip tcp_metrics delete </code>[<code> address </code>] <i>ADDRESS</i> </p>
<pre><code>SELECTOR :=

[ [ address ]

PREFIX ]
</code></pre>
<h2>Description</h2>
<p><code>ip tcp_metrics</code> is used to manipulate entries in the kernel that keep TCP information for IPv4 and IPv6 destinations. The entries are created when TCP sockets want to share information for destinations and are stored in a cache keyed by the destination address. The saved information may include values for metrics (initially obtained from routes), recent TSVAL for TIME-WAIT recycling purposes, state for the Fast Open feature, etc. For performance reasons the cache can not grow above configured limit and the older entries are replaced with fresh information, sometimes reclaimed and used for new destinations. The kernel never removes entries, they can be flushed only with this tool.</p>
<h3>ip tcp_metrics show &#8211; show cached entries</h3>
<dl>
<dt><code>address</code><i> PREFIX </i><code>(default)</code></p>
<dd>IPv4/IPv6 prefix or address. If no prefix is provided all entries are shown.  The output may contain the following information: <code>age</code><i> &lt;S.MMM&gt;</i><code>sec</code> &#8211; time after the entry was created, reset or updated with metrics from sockets. The entry is reset and refreshed on use with metrics from route if the metrics are not updated in last hour. Not all cached values reset the age on update. <code>cwnd</code><i> &lt;N&gt;</i> &#8211; CWND metric value <code>fo_cookie</code><i> &lt;HEX-STRING&gt;</i> &#8211; Cookie value received in SYN-ACK to be used by Fast Open for next SYNs <code>fo_mss</code><i> &lt;N&gt;</i> &#8211; MSS value received in SYN-ACK to be used by Fast Open for next SYNs <code>fo_syn_drops</code><i> &lt;N&gt;/&lt;S.MMM&gt;</i><code>sec ago</code> &#8211; Number of drops of initial outgoing Fast Open SYNs with data detected by monitoring the received SYN-ACK after SYN retransmission. The seconds show the time after last SYN drop and together with the drop count can be used to disable Fast Open for some time. <code>reordering</code><i> &lt;N&gt;</i> &#8211; Reordering metric value <code>rtt</code><i> &lt;N&gt;</i><code>us</code> &#8211; RTT metric value <code>rttvar</code><i> &lt;N&gt;</i><code>us</code> &#8211; RTTVAR metric value <code>ssthresh</code><i> &lt;SSTHRESH&gt;</i> &#8211; SSTHRESH metric value <code>tw_ts</code><i> &lt;TSVAL&gt;/&lt;SEC&gt;</i><code>sec ago</code> &#8211; recent TSVAL and the seconds after saving it into TIME-WAIT socket</p>
<h3>ip tcp_metrics delete &#8211; delete single entry</h3>
<dl>
<dt><code>address</code><i> ADDRESS </i><code>(default)</code></p>
<dd>IPv4/IPv6 address. The address is a required argument.</dl>
<h3>ip tcp_metrics flush &#8211; flush entries</h3>
<p>This command flushes the entries selected by some criteria. This command has the same arguments as <code>show.</code> </p>
<h2>Examples</h2>
<p>ip tcp_metrics show address 192.168.0.0/24</p>
<dl>
<dd>Shows the entries for destinations from subnet</dl>
<p> ip tcp_metrics show 192.168.0.0/24</p>
<dl>
<dd>The same but address keyword is optional</dl>
<p> ip tcp_metrics</p>
<dl>
<dd>Show all is the default action</dl>
<p> ip tcp_metrics delete 192.168.0.1</p>
<dl>
<dd>Removes the entry for 192.168.0.1 from cache.</dl>
<p> ip tcp_metrics flush 192.168.0.0/24</p>
<dl>
<dd>Removes entries for destinations from subnet</dl>
<p> ip tcp_metrics flush all</p>
<dl>
<dd>Removes all entries from cache</dl>
<p> ip -6 tcp_metrics flush all</p>
<dl>
<dd>Removes all IPv6 entries from cache keeping the IPv4 entries.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Julian Anastasov &lt;ja [at] ssi.bg&gt;</p>
