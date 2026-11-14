---
title: "tc-mpls(8)"
name: "tc-mpls"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-mpls/"
description: "mpls – mpls manipulation module"
---

<p>mpls &#8211; mpls manipulation module</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action mpls</code> { <i>POP</i> | <i>PUSH</i> | <i>MODIFY</i> | <code>dec_ttl</code> } [ <i>CONTROL</i> ] </p>
<pre><code>POP :=

pop protocol

MPLS_PROTO
PUSH :=

{ push | mac_push } [ protocol

MPLS_PROTO ]

[ tc

MPLS_TC ]

[ ttl

MPLS_TTL ]

[ bos

MPLS_BOS ]

label MPLS_LABEL
MODIFY :=

modify [ label

MPLS_LABEL ]

[ tc

MPLS_TC ]

[ ttl

MPLS_TTL ]
CONTROL := {

    reclassify | pipe | drop | continue | pass | goto chain CHAIN_INDEX }</code></pre>
<h2>Description</h2>
<p>The <code>mpls</code> action performs mpls encapsulation or decapsulation on a packet, reflected by the operation modes <i>POP</i>, <i>PUSH</i>, <i>MODIFY</i> and <i>DEC_TTL</i>. The <i>POP</i> mode requires the ethertype of the header that follows the MPLS header (e.g. IPv4 or another MPLS). It will remove the outer MPLS header and replace the ethertype in the MAC header with that passed. The <i>PUSH</i> and <i>MODIFY</i> modes update the current MPLS header information or add a new header. <i>PUSH</i> requires at least an <i>MPLS_LABEL</i>. <i>DEC_TTL</i> requires no arguments and simply subtracts 1 from the MPLS header TTL field. </p>
<h2>Options</h2>
<dl>
<dt><code>pop</code></p>
<dd>Decapsulation mode. Requires the protocol of the next header.</p>
<dt><code>push</code></p>
<dd>Encapsulation mode. Adds the MPLS header between the MAC and the network headers. Requires at least the <code>label</code> option.</p>
<dt><code>mac_push</code></p>
<dd>Encapsulation mode. Adds the MPLS header before the MAC header. Requires at least the <code>label</code> option.</p>
<dt><code>modify</code></p>
<dd>Replace mode. Existing MPLS tag is replaced. <code>label</code>, <code>tc</code>, and <code>ttl</code> are all optional.</p>
<dt><code>dec_ttl</code></p>
<dd>Decrement the TTL field on the outer most MPLS header.</p>
<dt><code>label</code><i> MPLS_LABEL</i></p>
<dd>Specify the MPLS LABEL for the outer MPLS header. <i>MPLS_LABEL</i> is an unsigned 20bit integer, the format is detected automatically (e.g. prefix with &#8216;<code>0x</code>&#8216; for hexadecimal interpretation, etc.).</p>
<dt><code>protocol</code><i> MPLS_PROTO</i></p>
<dd>Choose the protocol to use. For push actions this must be <code>mpls_uc</code> or <code>mpls_mc</code> (<code>mpls_uc</code> is the default). For pop actions it should be the protocol of the next header. This option cannot be used with modify.</p>
<dt><code>tc</code><i> MPLS_TC</i></p>
<dd>Choose the TC value for the outer MPLS header. Decimal number in range of 0-7. Defaults to 0.</p>
<dt><code>ttl</code><i> MPLS_TTL</i></p>
<dd>Choose the TTL value for the outer MPLS header. Number in range of 0-255. A non-zero default value will be selected if this is not explicitly set.</p>
<dt><code>bos</code><i> MPLS_BOS</i></p>
<dd>Manually configure the bottom of stack bit for an MPLS header push. The default is for TC to automatically set (or unset) the bit based on the next header of the packet.</p>
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
<p>The following example encapsulates incoming IP packets on eth0 into MPLS with a label 123 and sends them out eth1:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev eth0 protocol ip parent ffff: flower \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mpls push protocol mpls_uc label 123 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev eth1
</dl>
<p> In this example, incoming MPLS unicast packets on eth0 are decapsulated and redirected to eth1:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev eth0 protocol mpls_uc parent ffff: flower \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mpls pop protocol ipv4 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev eth1
</dl>
<p> Here is another example, where incoming Ethernet frames are encapsulated into MPLS with label 123 and TTL 64. Then, an outer Ethernet header is added and the resulting frame is finally sent on eth1:</p>
<dl>
<dd>#tc qdisc add dev eth0 ingress #tc filter add dev eth0 ingress matchall \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mpls mac_push label 123 ttl 64 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action vlan push_eth \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>dst_mac 02:00:00:00:00:02 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>src_mac 02:00:00:00:00:01 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev eth1
</dl>
<p> The following example assumes that incoming MPLS packets with label 123 transport Ethernet frames. The outer Ethernet and the MPLS headers are stripped, then the inner Ethernet frame is sent on eth1:</p>
<dl>
<dd>#tc qdisc add dev eth0 ingress #tc filter add dev eth0 ingress protocol mpls_uc \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>flower mpls_label 123 mpls_bos 1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action vlan pop_eth \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mpls pop protocol teb \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev eth1
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-mirred/">tc-mirred</a></code>(8), <code><a href="/docs/linux/man/8-tc-vlan/">tc-vlan</a></code>(8) </p>
