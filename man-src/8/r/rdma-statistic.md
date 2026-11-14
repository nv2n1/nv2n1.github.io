---
title: "rdma-statistic(8)"
name: "rdma-statistic"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-statistic/"
description: "rdma-statistic – RDMA statistic counter configuration"
---

<p>rdma-statistic &#8211; RDMA statistic counter configuration</p>
<h2>Synopsis</h2>
<pre><code>rdma

[ OPTIONS ]

statistic

{ COMMAND |

    help }
</code></pre>
<p> <code>rdma statistic</code> { <i>OBJECT</i> } <code>show</code><br />
 <code>rdma statistic</code> [ <i>OBJECT</i> ] <code>show link</code> [ <i>DEV/PORT_INDX</i> ] [ <i>FILTER_NAME</i> <i>FILTER_VALUE</i> ]<br />
 <code>rdma statistic</code> <i>OBJECT</i> <code>mode</code> rdma statistic</p>
<p>OBJECT</p>
<p>set</p>
<p>COUNTER_SCOPE</p>
<p>[ DEV/PORT_INDEX ]</p>
<p>auto</p>
<p>{ CRITERIA |</p>
<p>    off }<br />
 <code>rdma statistic</code> <i>OBJECT</i> <code>bind</code> <i>COUNTER_SCOPE</i> [ <i>DEV/PORT_INDEX</i> ] [ <i>OBJECT-ID</i> ] [ <i>COUNTER-ID</i> ]<br />
 <code>rdma statistic</code> <i>OBJECT</i> <code>unbind</code> <i>COUNTER_SCOPE</i> [ <i>DEV/PORT_INDEX</i> ] [ <i>COUNTER-ID</i> ] [ <i>OBJECT-ID</i> ] </p>
<pre><code>COUNTER_SCOPE :=

{ link | dev }
OBJECT :=

{ qp | mr }
CRITERIA :=

{ type | pid }
FILTER_NAME :=

{ cntn | lqpn | pid | qp-type }
</code></pre>
<h2>Description</h2>
<h3>rdma statistic [object] show &#8211; Queries the specified RDMA device for RDMA and driver-specific statistics. Show the default hw counters if object is not specified</h3>
<p><i>DEV</i> &#8211; specifies counters on this RDMA device to show. <i>PORT_INDEX</i> &#8211; specifies counters on this RDMA port to show. <i>FILTER_NAME</i> &#8211; specifies a filter to show only the results matching it.</p>
<h3>rdma statistic &lt;object&gt; set &#8211; configure counter statistic auto-mode for a specific device/port</h3>
<p>In auto mode all objects belong to one category are bind automatically to a single counter set. The &quot;off&quot; is global for all auto modes together. Not applicable for MR&#8217;s.</p>
<h3>rdma statistic &lt;object&gt; bind &#8211; manually bind an object (e.g., a qp) with a counter</h3>
<p>When bound the statistics of this object are available in this counter. Not applicable for MR&#8217;s.</p>
<h3>rdma statistic &lt;object&gt; unbind &#8211; manually unbind an object (e.g., a qp) from the counter previously bound</h3>
<p>When unbound the statistics of this object are no longer available in this counter; And if object id is not specified then all objects on this counter will be unbound. Not applicable for MR&#8217;s. <i>COUNTER-ID</i> &#8211; specifies the id of the counter to be bound. If this argument is omitted then a new counter will be allocated. </p>
<h2>Examples</h2>
<p>rdma statistic show</p>
<dl>
<dd>Shows the state of the default counter of all RDMA devices on the system.</dl>
<p> rdma statistic show link mlx5_2/1</p>
<dl>
<dd>Shows the state of the default counter of specified RDMA port</dl>
<p> rdma statistic qp show</p>
<dl>
<dd>Shows the state of all qp counters of all RDMA devices on the system.</dl>
<p> rdma statistic qp show link mlx5_2/1</p>
<dl>
<dd>Shows the state of all qp counters of specified RDMA port.</dl>
<p> rdma statistic qp show link mlx5_2 pid 30489</p>
<dl>
<dd>Shows the state of all qp counters of specified RDMA port and belonging to pid 30489</dl>
<p> rdma statistic qp show link mlx5_2 qp-type UD</p>
<dl>
<dd>Shows the state of all qp counters of specified RDMA port and with QP type UD</dl>
<p> rdma statistic qp mode</p>
<dl>
<dd>List current counter mode on all devices</dl>
<p> rdma statistic qp mode link mlx5_2/1</p>
<dl>
<dd>List current counter mode of device mlx5_2 port 1</dl>
<p> rdma statistic qp set link mlx5_2/1 auto type on</p>
<dl>
<dd>On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same qp type.</dl>
<p> rdma statistic qp set link mlx5_2/1 auto pid on</p>
<dl>
<dd>On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same pid.</dl>
<p> rdma statistic qp set link mlx5_2/1 auto pid,type on</p>
<dl>
<dd>On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same pid and same type.</dl>
<p> rdma statistic qp set link mlx5_2/1 auto off</p>
<dl>
<dd>Turn-off auto mode on device mlx5_2 port 1. The allocated counters can be manually accessed.</dl>
<p> rdma statistic qp bind link mlx5_2/1 lqpn 178</p>
<dl>
<dd>On device mlx5_2 port 1, allocate a counter and bind the specified qp on it</dl>
<p> rdma statistic qp unbind link mlx5_2/1 cntn 4 lqpn 178</p>
<dl>
<dd>On device mlx5_2 port 1, bind the specified qp on the specified counter</dl>
<p> rdma statistic qp unbind link mlx5_2/1 cntn 4</p>
<dl>
<dd>On device mlx5_2 port 1, unbind all QPs on the specified counter. After that this counter will be released automatically by the kernel.</dl>
<p> rdma statistic show mr</p>
<dl>
<dd>List all currently allocated MR&#8217;s and their counters.</dl>
<p> rdma statistic show mr mrn 6</p>
<dl>
<dd>Dump a specific MR statistics with mrn 6. Dumps nothing if does not exists.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rdma/">rdma</a></code>(8), <code><a href="/docs/linux/man/8-rdma-dev/">rdma-dev</a></code>(8), <code><a href="/docs/linux/man/8-rdma-link/">rdma-link</a></code>(8), <code><a href="/docs/linux/man/8-rdma-resource/">rdma-resource</a></code>(8), </p>
<h2>Authors</h2>
<p>Mark Zhang &lt;markz [at] mellanox.com&gt;<br />
 Erez Alfasi &lt;ereza [at] mellanox.com&gt;</p>
