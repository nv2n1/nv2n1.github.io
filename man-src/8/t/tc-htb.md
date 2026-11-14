---
title: "tc-htb(8)"
name: "tc-htb"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-htb/"
description: "HTB – Hierarchy Token Bucket"
---

<p>HTB &#8211; Hierarchy Token Bucket</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> dev <code>( parent</code> classid <code>| root) [ handle</code> major: <code>] htb [ default</code> minor-id <code>] [ r2q</code> divisor <code>] [ offload ]</code> <code>tc class &#8230; dev</code> dev <code>parent</code> major:[minor] <code>[ classid</code> major:minor <code>] htb rate</code> rate <code>[ ceil</code> rate <code>] burst</code> bytes <code>[ cburst</code> bytes <code>] [ prio</code> priority <code>] [ quantum</code> bytes <code>]</code> </p>
<h2>Description</h2>
<p>HTB is meant as a more understandable and intuitive replacement for the CBQ qdisc in Linux. Both CBQ and HTB help you to control the use of the outbound bandwidth on a given link. Both allow you to use one physical link to simulate several slower links and to send different kinds of traffic on different simulated links. In both cases, you have to specify how to divide the physical link into simulated links and how to decide which simulated link to use for a given packet to be sent. Unlike CBQ, HTB shapes traffic based on the Token Bucket Filter algorithm which does not depend on interface characteristics and so does not need to know the underlying bandwidth of the outgoing interface. </p>
<h2>Shaping Algorithm</h2>
<p>Shaping works as documented in <code>tc-tbf (8).</code></p>
<h2>Classification</h2>
<p>Within the one HTB instance many classes may exist. Each of these classes contains another qdisc, by default <code><a href="/docs/linux/man/8-tc-pfifo/">tc-pfifo</a></code>(8). </p>
<p> When enqueueing a packet, HTB starts at the root and uses various methods to determine which class should receive the data. </p>
<p> In the absence of uncommon configuration options, the process is rather easy. At each node we look for an instruction, and then go to the class the instruction refers us to. If the class found is a barren leaf-node (without children), we enqueue the packet there. If it is not yet a leaf node, we do the whole thing over again starting from that node. </p>
<p> The following actions are performed, in order at each node we visit, until one sends us to another node, or terminates the process.</p>
<dl>
<dt>(i)</p>
<dd>Consult filters attached to the class. If sent to a leafnode, we are done. Otherwise, restart.</p>
<dt>(ii)</p>
<dd>If none of the above returned with an instruction, enqueue at this node.</dl>
<p> This algorithm makes sure that a packet always ends up somewhere, even while you are busy building your configuration.</p>
<h2>Link Sharing Algorithm</h2>
<p>FIXME</p>
<h2>Qdisc</h2>
<p>The root of a HTB qdisc class tree has the following parameters: </p>
<dl>
<dt>parent major:minor | root</p>
<dd>This mandatory parameter determines the place of the HTB instance, either at the <code>root</code> of an interface or within an existing class.</p>
<dt>handle major:</p>
<dd>Like all other qdiscs, the HTB can be assigned a handle. Should consist only of a major number, followed by a colon. Optional, but very useful if classes will be generated within this qdisc.</p>
<dt>default minor-id</p>
<dd>Unclassified traffic gets sent to the class with this minor-id.</p>
<dt>r2q divisor</p>
<dd>Divisor used to calculate <code>quantum</code> values for classes. Classes divide <code>rate</code> by this number. Default value is 10.</p>
<dt>offload</p>
<dd>Offload the HTB algorithm to hardware (requires driver and device support). </p>
</dl>
<h2>Classes</h2>
<p>Classes have a host of parameters to configure their operation. </p>
<dl>
<dt>parent major:minor</p>
<dd>Place of this class within the hierarchy. If attached directly to a qdisc and not to another class, minor can be omitted. Mandatory.</p>
<dt>classid major:minor</p>
<dd>Like qdiscs, classes can be named. The major number must be equal to the major number of the qdisc to which it belongs. Optional, but needed if this class is going to have children.</p>
<dt>prio priority</p>
<dd>In the round-robin process, classes with the lowest priority field are tried for packets first. </p>
<dt>rate rate</p>
<dd>Maximum rate this class and all its children are guaranteed. Mandatory. </p>
<dt>ceil rate</p>
<dd>Maximum rate at which a class can send, if its parent has bandwidth to spare. Defaults to the configured rate, which implies no borrowing </p>
<dt>burst bytes</p>
<dd>Amount of bytes that can be burst at <code>ceil</code> speed, in excess of the configured <code>rate.</code> Should be at least as high as the highest burst of all children. </p>
<dt>cburst bytes</p>
<dd>Amount of bytes that can be burst at &#8216;infinite&#8217; speed, in other words, as fast as the interface can transmit them. For perfect evening out, should be equal to at most one average packet. Should be at least as high as the highest cburst of all children. </p>
<dt>quantum bytes</p>
<dd>Number of bytes to serve from this class before the scheduler moves to the next class. Default value is <code>rate</code> divided by the qdisc <code>r2q</code> parameter. If specified, <code>r2q</code> is ignored. </p>
</dl>
<h2>Notes</h2>
<p>Due to Unix timing constraints, the maximum ceil rate is not infinite and may in fact be quite low. On Intel, there are 100 timer events per second, the maximum rate is that rate at which &#8216;burst&#8217; bytes are sent each timer tick. From this, the minimum burst size for a specified rate can be calculated. For i386, a 10mbit rate requires a 12 kilobyte burst as 100*12kb*8 equals 10mbit. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
<p> HTB website: <a rel="nofollow" href="http://luxik.cdi.cz/~devik/qos/htb/">http://luxik.cdi.cz/~devik/qos/htb/</a></p>
<h2>Author</h2>
<p>Martin Devera &lt;devik [at] cdi.cz&gt;. This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
