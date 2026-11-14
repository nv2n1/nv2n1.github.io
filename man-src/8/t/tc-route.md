---
title: "tc-route(8)"
name: "tc-route"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-route/"
description: "route – route traffic control filter"
---

<p>route &#8211; route traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>route</code> [ <code>from</code> <i>REALM</i> | <code>fromif</code> <i>TAG</i> ] [ <code>to</code> <i>REALM</i> ] [ <code>classid</code> <i>CLASSID</i> ] [ <code>action</code> <i>ACTION_SPEC</i> ]</p>
<h2>Description</h2>
<p>Match packets based on routing table entries. This filter centers around the possibility to assign a <code>realm</code> to routing table entries. For any packet to be classified by this filter, a routing table lookup is performed and the returned <code>realm</code> is used to decide on whether the packet is a match or not.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Push matching packets into the class identified by <i>CLASSID</i>.</p>
<dt><code>from</code><i> REALM</i></p>
<dd><code>fromif</code><i> TAG</i> Perform source route lookups. <i>TAG</i> is the name of an interface which must be present on the system at the time of <code>tc</code> invocation.</p>
<dt><code>to</code><i> REALM</i></p>
<dd>Match if normal (i.e., destination) routing returns the given <i>REALM</i>.</dl>
<h2>Examples</h2>
<p>Consider the subnet 192.168.2.0/24 being attached to eth0: </p>
<dl>
<dd>ip route add 192.168.2.0/24 dev eth0 realm 2</dl>
<p> The following <code>route</code> filter will then match packets from that subnet: </p>
<dl>
<dd>tc filter add &#8230; route from 2 classid 1:2</dl>
<p> and pass packets on to class 1:2.</p>
<h2>Notes</h2>
<p>Due to implementation details, <code>realm</code> values must be in a range from 0 to 255, inclusive. Alternatively, a verbose name defined in /etc/iproute2/rt_realms may be given instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-ip-route/">ip-route</a></code>(8) </p>
