---
title: "ibv_rate_to_mult(3)"
name: "ibv_rate_to_mult"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_rate_to_mult/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_rate_to_mult - convert IB rate enumeration to multiplier of 2.5 Gbit/sec 

 mult_to_ibv_rate - convert multiplier of 2.5 Gbit/sec to an IB rate enumeration 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_rate_to_mult(enum ibv_rate rate);
enum ibv_rate mult_to_ibv_rate(int mult);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_rate_to_mult() converts the IB transmission rate enumeration rate to a multiple of 2.5 Gbit/sec (the base rate). For example, if rate is IBV_RATE_5_GBPS, the value 2 will be returned (5 Gbit/sec = 2 * 2.5 Gbit/sec). 

 mult_to_ibv_rate() converts the multiplier value (of 2.5 Gbit/sec) mult to an IB transmission rate enumeration. For example, if mult is 2, the rate enumeration IBV_RATE_5_GBPS will be returned.

<h2>RETURN VALUE</h2>

 

 ibv_rate_to_mult() returns the multiplier of the base rate 2.5 Gbit/sec. 

 mult_to_ibv_rate() returns the enumeration representing the IB transmission rate.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


