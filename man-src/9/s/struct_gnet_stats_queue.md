---
title: "struct_gnet_stats_queue(9)"
name: "struct_gnet_stats_queue"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_gnet_stats_queue/"
---

struct_gnet_stats_queue - queuing statistics

<h2>Synopsis</h2>

<pre><code>struct gnet_stats_queue {
    __u32 qlen;
    __u32 backlog;
    __u32 drops;
    __u32 requeues;
    __u32 overlimits;
};</code></pre>

<h2>Members</h2>

qlen
<dl><dd>queue length</dl>
 

 backlog
<dl><dd>backlog size of queue</dl>
 

 drops
<dl><dd>number of dropped packets</dl>
 

 requeues
<dl><dd>number of requeues</dl>
 

 overlimits
<dl><dd>number of enqueues over the limit</dl>

<h2>Copyright</h2>


