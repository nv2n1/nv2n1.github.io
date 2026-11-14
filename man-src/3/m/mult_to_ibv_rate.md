---
title: "mult_to_ibv_rate(3)"
name: "mult_to_ibv_rate"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mult_to_ibv_rate/"
---

ibv_rate_to_mult - convert IB rate enumeration to multiplier of 2.5 Gbit/sec 

 mult_to_ibv_rate - convert multiplier of 2.5 Gbit/sec to an IB rate enumeration 

<h2>Synopsis</h2><dl COMPACT><dd><pre>#include &lt;infiniband/verbs.h&gt;
int ibv_rate_to_mult(enum ibv_rate rate);
enum ibv_rate mult_to_ibv_rate(int mult);</pre></dl><h2>Description</h2>ibv_rate_to_mult() converts the IB transmission rate enumeration rate to a multiple of 2.5 Gbit/sec (the base rate). For example, if rate is IBV_RATE_5_GBPS, the value 2 will be returned (5 Gbit/sec = 2 * 2.5 Gbit/sec). 

 mult_to_ibv_rate() converts the multiplier value (of 2.5 Gbit/sec) mult to an IB transmission rate enumeration. For example, if mult is 2, the rate enumeration IBV_RATE_5_GBPS will be returned.
<h2>Return Value</h2>ibv_rate_to_mult() returns the multiplier of the base rate 2.5 Gbit/sec. 

 mult_to_ibv_rate() returns the enumeration representing the IB transmission rate.
<h2>See Also</h2><a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)
<h2>Author</h2>Dotan Barak &lt;dotanba [at] gmail.com&gt;
