---
title: "tc-vlan(8)"
name: "tc-vlan"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-vlan/"
description: "vlan – vlan manipulation module"
---

<p>vlan &#8211; vlan manipulation module</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action vlan</code> { <code>pop</code> | <code>pop_eth</code> | <i>PUSH</i> | <i>MODIFY</i> | <i>PUSH_ETH</i> } [ <i>CONTROL</i> ] </p>
<pre><code>PUSH :=

push [ protocol

VLANPROTO ]

[ priority

VLANPRIO ]

id VLANID
MODIFY :=

modify [ protocol

VLANPROTO ]

[ priority

VLANPRIO ]

id VLANID
PUSH_ETH :=

push_eth

dst_mac LLADDR src_mac LLADDR
CONTROL := {

    reclassify | pipe | drop | continue | pass | goto chain CHAIN_INDEX }</code></pre>
<h2>Description</h2>
<p>The <code>vlan</code> action allows to perform 802.1Q en- or decapsulation on a packet, reflected by the operation modes <i>POP</i>, <i>PUSH</i> and <i>MODIFY</i>. The <i>POP</i> mode is simple, as no further information is required to just drop the outer-most VLAN encapsulation. The <i>PUSH</i> and <i>MODIFY</i> modes require at least a <i>VLANID</i> and allow to optionally choose the <i>VLANPROTO</i> to use. The <code>vlan</code> action can also be used to add or remove the base Ethernet header. The <code>pop_eth</code> mode, which takes no argument, is used to remove the base Ethernet header. All existing VLANs must have been previously dropped. The opposite operation, adding a base Ethernet header, is done with the <code>push_eth</code> mode. In that case, the packet must have no MAC header (stacking MAC headers is not permitted). This mode is mostly useful when a previous action has encapsulated the whole original frame behind a network header and one needs to prepend an Ethernet header before forwarding the resulting packet. </p>
<h2>Options</h2>
<dl>
<dt><code>pop</code></p>
<dd>Decapsulation mode, no further arguments allowed.</p>
<dt><code>push</code></p>
<dd>Encapsulation mode. Requires at least <code>id</code> option.</p>
<dt><code>modify</code></p>
<dd>Replace mode. Existing 802.1Q tag is replaced. Requires at least <code>id</code> option.</p>
<dt><code>pop_eth</code></p>
<dd>Ethernet header decapsulation mode. Only works on a plain Ethernet header: VLANs, if any, must be removed first.</p>
<dt><code>push_eth</code></p>
<dd>Ethernet header encapsulation mode. The Ethertype is automatically set using the network header type. Chaining Ethernet headers is not allowed: the packet must have no MAC header when using this mode. Requires the <code>dst_mac </code>and<code> src_mac </code>options.</p>
<dt><code>id</code><i> VLANID</i></p>
<dd>Specify the VLAN ID to encapsulate into. <i>VLANID</i> is an unsigned 16bit integer, the format is detected automatically (e.g. prefix with &#8216;<code>0x</code>&#8216; for hexadecimal interpretation, etc.).</p>
<dt><code>protocol</code><i> VLANPROTO</i></p>
<dd>Choose the VLAN protocol to use. At the time of writing, the kernel accepts only <code>802.1Q</code> or <code>802.1ad</code>.</p>
<dt><code>priority</code><i> VLANPRIO</i></p>
<dd>Choose the VLAN priority to use. Decimal number in range of 0-7.</p>
<dt><code>dst_mac</code><i> LLADDR</i></p>
<dd>Choose the destination MAC address to use.</p>
<dt><code>src_mac</code><i> LLADDR</i></p>
<dd>Choose the source MAC address to use.</p>
<dt><i>CONTROL</i></p>
<dd>How to continue after executing this action.</p>
<dl>
<dd>
<dl>
<dt><code>reclassify</code></p>
<dd>Restarts classification by jumping back to the first filter attached to this action&#8217;s parent.</p>
<dt><code>pipe</code></p>
<dd>Continue with the next action, this is the default.</p>
<dt><code>drop</code></p>
<dd>Packet will be dropped without running further actions.</p>
<dt><code>continue</code></p>
<dd>Continue classification with next filter in line.</p>
<dt><code>pass</code></p>
<dd>Return to calling qdisc for packet processing. This ends the classification process.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>The following example encapsulates incoming ICMP packets on eth0 from 10.0.0.2 into VLAN ID 123:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev eth0 parent ffff: pref 11 protocol ip \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> match ip src 10.0.0.2 flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action vlan push id 123
</dl>
<p> Here is an example of the <code>pop</code> function: Incoming VLAN packets on eth0 are decapsulated and the classification process then restarted for the plain packet:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev $ETH parent ffff: pref 1 protocol 802.1Q \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match u32 0 0 flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action vlan pop reclassify
</dl>
<p> For an example of the <code>pop_eth</code> and <code>push_eth</code> modes, see <code><a href="/docs/linux/man/8-tc-mpls/">tc-mpls</a></code>(8). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-mpls/">tc-mpls</a></code>(8) </p>
