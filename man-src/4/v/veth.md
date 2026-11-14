---
title: "veth(4)"
name: "veth"
section: "4"
letter: "v"
url: "/docs/linux/man/4-veth/"
description: "veth – Virtual Ethernet Device"
---

<p>veth &#8211; Virtual Ethernet Device</p>
<h2>Description</h2>
<p>The <code>veth</code> devices are virtual Ethernet devices. They can act as tunnels between network namespaces to create a bridge to a physical network device in another namespace, but can also be used as standalone network devices. <code>veth</code> devices are always created in interconnected pairs. A pair can be created using the command: # ip link add &lt;p1-name&gt; type veth peer name &lt;p2-name&gt; In the above, <i>p1-name</i> and <i>p2-name</i> are the names assigned to the two connected end points. Packets transmitted on one device in the pair are immediately received on the other device. When either devices is down the link state of the pair is down. <code>veth</code> device pairs are useful for combining the network facilities of the kernel together in interesting ways. A particularly interesting use case is to place one end of a <code>veth</code> pair in one network namespace and the other end in another network namespace, thus allowing communication between network namespaces. To do this, one can provide the <code>netns</code> parameter when creating the interfaces: # ip link add &lt;p1-name&gt; netns &lt;p1-ns&gt; type veth peer &lt;p2-name&gt; netns &lt;p2-ns&gt; or, for an existing <code>veth</code> pair, move one side to the other namespace: # ip link set &lt;p2-name&gt; netns &lt;p2-ns&gt; <code><a href="/docs/linux/man/8-ethtool/">ethtool</a></code>(8) can be used to find the peer of a <code>veth</code> network interface, using commands something like: # <code>ip link add ve_A type veth peer name ve_B</code> # Create veth pair # <code>ethtool -S ve_A</code> # Discover interface index of peer NIC statistics:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;peer_ifindex: 16 # <code>ip link | grep &#8216;ha16:&#8217;</code> # Look up interface 16: ve_B [at] ve_A: &lt;BROADCAST,MULTICAST,M-DOWN&gt; mtu 1500 qdisc &#8230; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ip-link/">ip-link</a></code>(8), <code><a href="/docs/linux/man/8-ip-netns/">ip-netns</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
