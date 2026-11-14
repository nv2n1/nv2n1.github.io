---
title: "brctl(8)"
name: "brctl"
section: "8"
letter: "b"
url: "/docs/linux/man/8-brctl/"
description: "brctl – ethernet bridge administration"
---

<p>brctl &#8211; ethernet bridge administration</p>
<h2>Synopsis</h2>
<p><code>brctl [command]</code></p>
<h2>Description</h2>
<p><code>brctl</code> is used to set up, maintain, and inspect the ethernet bridge configuration in the Linux kernel. An ethernet bridge is a device commonly used to connect different networks of ethernets together, so that these ethernets will appear as one ethernet to the participants. Each of the ethernets being connected corresponds to one physical interface in the bridge. These individual ethernets are bundled into one bigger (&#8216;logical&#8217;) ethernet, this bigger ethernet corresponds to the bridge network interface. </p>
<h2>Instances</h2>
<p>The command <code>brctl addbr &lt;name&gt;</code> creates a new instance of the ethernet bridge. The network interface corresponding to the bridge will be called &lt;name&gt;. </p>
<p> The command <code>brctl delbr &lt;name&gt;</code> deletes the instance &lt;name&gt; of the ethernet bridge. The network interface corresponding to the bridge must be down before it can be deleted! </p>
<p> The command <code>brctl show</code> shows all current instances of the ethernet bridge.</p>
<h2>Ports</h2>
<p>Each bridge has a number of ports attached to it. Network traffic coming in on any of these ports will be forwarded to the other ports transparently, so that the bridge is invisible to the rest of the network (i.e. it will not show up in <i><a href="/docs/linux/man/8-traceroute/">traceroute</a>(8)</i> ). </p>
<p> The command <code>brctl addif &lt;brname&gt; &lt;ifname&gt;</code> will make the interface &lt;ifname&gt; a port of the bridge &lt;brname&gt;. This means that all frames received on &lt;ifname&gt; will be processed as if destined for the bridge. Also, when sending frames on &lt;brname&gt;, &lt;ifname&gt; will be considered as a potential output interface. </p>
<p> The command <code>brctl delif &lt;brname&gt; &lt;ifname&gt;</code> will detach the interface &lt;ifname&gt; from the bridge &lt;brname&gt;. </p>
<p> The command <code>brctl show &lt;brname&gt;</code> will show some information on the bridge and its attached ports.</p>
<h2>Ageing</h2>
<p>The bridge keeps track of ethernet addresses seen on each port. When it needs to forward a frame, and it happens to know on which port the destination ethernet address (specified in the frame) is located, it can &#8216;cheat&#8217; by forwarding the frame to that port only, thus saving a lot of redundant copies and transmits. </p>
<p> However, the ethernet address location data is not static data. Machines can move to other ports, network cards can be replaced (which changes the machine&#8217;s ethernet address), etc. </p>
<p> <code>brctl showmacs &lt;brname&gt;</code> shows a list of learned MAC addresses for this bridge. </p>
<p> <code>brctl setageing &lt;brname&gt; &lt;time&gt;</code> sets the ethernet (MAC) address ageing time, in seconds. After &lt;time&gt; seconds of not having seen a frame coming from a certain address, the bridge will time out (delete) that address from the Forwarding DataBase (fdb). </p>
<p> <code>brctl setgcint &lt;brname&gt; &lt;time&gt;</code> sets the garbage collection interval for the bridge &lt;brname&gt; to &lt;time&gt; seconds. This means that the bridge will check the forwarding database for timed out entries every &lt;time&gt; seconds.</p>
<h2>Spanning Tree Protocol</h2>
<p>Multiple ethernet bridges can work together to create even larger networks of ethernets using the IEEE 802.1d spanning tree protocol. This protocol is used for finding the shortest path between two ethernets, and for eliminating loops from the topology. As this protocol is a standard, Linux bridges will interwork properly with other third party bridge products. Bridges communicate with each other by sending and receiving BPDUs (Bridge Protocol Data Units). These BPDUs can be recognized by an ethernet destination address of 01:80:c2:00:00:00. </p>
<p> The spanning tree protocol can also be turned off (for those situations where it just doesn&#8217;t make sense, for example when this Linux box is the only bridge on the LAN, or when you know that there are no loops in the topology.) </p>
<p> <i><a href="/docs/linux/man/8-brctl/">brctl</a>(8)</i> can be used for configuring certain spanning tree protocol parameters. For an explanation of these parameters, see the IEEE 802.1d specification (or send me an email). The default values should be just fine. If you don&#8217;t know what these parameters mean, you probably won&#8217;t feel the desire to tweak them. </p>
<p> <code>brctl stp &lt;bridge&gt; &lt;state&gt;</code> controls this bridge instance&#8217;s participation in the spanning tree protocol. If &lt;state&gt; is &quot;on&quot; or &quot;yes&quot; the STP will be turned on, otherwise it will be turned off. When turned off, the bridge will not send or receive BPDUs, and will thus not participate in the spanning tree protocol. If your bridge isn&#8217;t the only bridge on the LAN, or if there are loops in the LAN&#8217;s topology, DO NOT turn this option off. If you turn this option off, please know what you are doing. </p>
<p> <code>brctl setbridgeprio &lt;bridge&gt; &lt;priority&gt;</code> sets the bridge&#8217;s priority to &lt;priority&gt;. The priority value is an unsigned 16-bit quantity (a number between 0 and 65535), and has no dimension. Lower priority values are &#8216;better&#8217;. The bridge with the lowest priority will be elected &#8216;root bridge&#8217;. </p>
<p> <code>brctl setfd &lt;bridge&gt; &lt;time&gt;</code> sets the bridge&#8217;s &#8216;bridge forward delay&#8217; to &lt;time&gt; seconds. </p>
<p> <code>brctl sethello &lt;bridge&gt; &lt;time&gt;</code> sets the bridge&#8217;s &#8216;bridge hello time&#8217; to &lt;time&gt; seconds. </p>
<p> <code>brctl setmaxage &lt;bridge&gt; &lt;time&gt;</code> sets the bridge&#8217;s &#8216;maximum message age&#8217; to &lt;time&gt; seconds. </p>
<p> <code>brctl setpathcost &lt;bridge&gt; &lt;port&gt; &lt;cost&gt;</code> sets the port cost of the port &lt;port&gt; to &lt;cost&gt;. This is a dimensionless metric (from 1 to 65535, default is 100). </p>
<p> <code>brctl setportprio &lt;bridge&gt; &lt;port&gt; &lt;priority&gt;</code> sets the port &lt;port&gt;&#8217;s priority to &lt;priority&gt;. The priority value is a number from 0 (min) to 63 (max), default is 32, and has no dimension. This metric is used in the designated port and root port selection algorithms.</p>
<h2>Notes</h2>
<p><code><a href="/docs/linux/man/8-brctl/">brctl</a>(8)</code> is obsolete. Some features such as STP guard, hairpin mode, fast leave and root block are intentionally not implemented in this command. Instead use <code>bridge</code> command from <code>iproute2</code> package for a more full set of features. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code> </p>
<h2>Author</h2>
<p>Lennert Buytenhek &lt;buytenh [at] gnu.org&gt; Stephen Hemminger &lt;stephen [at] networkplumber.org&gt;</p>
