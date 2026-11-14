---
title: "ibv_rate_to_mbps(3)"
name: "ibv_rate_to_mbps"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_rate_to_mbps/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_rate_to_mbps - convert IB rate enumeration to Mbit/sec 

 mbps_to_ibv_rate - convert Mbit/sec to an IB rate enumeration 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_rate_to_mbps(enum ibv_rate rate);
enum ibv_rate mbps_to_ibv_rate(int mbps);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_rate_to_mbps() converts the IB transmission rate enumeration rate to a number of Mbit/sec. For example, if rate is IBV_RATE_5_GBPS, the value 5000 will be returned (5 Gbit/sec = 5000 Mbit/sec). 

 mbps_to_ibv_rate() converts the number of Mbit/sec mult to an IB transmission rate enumeration. For example, if mult is 5000, the rate enumeration IBV_RATE_5_GBPS will be returned.

<h2>RETURN VALUE</h2>

 

 ibv_rate_to_mbps() returns the number of Mbit/sec. 

 mbps_to_ibv_rate() returns the enumeration representing the IB transmission rate.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanb [at] dev.mellanox.co.il&gt; 

<h2>Index</h2>


