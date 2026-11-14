---
title: "tc-ife(8)"
name: "tc-ife"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-ife/"
description: "IFE – encapsulate/decapsulate metadata"
---

<p>IFE &#8211; encapsulate/decapsulate metadata</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code> action ife</code> <i>DIRECTION</i> [ <i>ACTION</i> ] [ <code>dst</code> <i>DMAC</i> ] [ <code>src</code> <i>SMAC</i> ] [ <code>type</code> <i>TYPE</i> ] [ <i>CONTROL</i> ] [ <code>index</code> <i>INDEX</i> ] </p>
<pre><code>DIRECTION := {

    decode | encode }
ACTION := {

    allow ATTR

    | use

    ATTR value }
ATTR := {

    mark | prio | tcindex }
CONTROL := {

    reclassify | use | pipe | drop | continue | ok | goto chain CHAIN_INDEX }</code></pre>
<h2>Description</h2>
<p>The <code>ife</code> action allows for a sending side to encapsulate arbitrary metadata, which is then decapsulated by the receiving end. The sender runs in encoding mode and the receiver in decode mode. Both sender and receiver must specify the same ethertype. In the future, a registered ethertype may be available as a default.</p>
<h2>Options</h2>
<dl>
<dt><code>decode</code></p>
<dd>For the receiving side; decode the metadata if the packet matches.</p>
<dt><code>encode</code></p>
<dd>For the sending side. Encode the specified metadata if the packet matches.</p>
<dt><code>allow</code></p>
<dd>Encode direction only. Allows encoding specified metadata.</p>
<dt><code>use</code></p>
<dd>Encode direction only. Enforce static encoding of specified metadata.</p>
<dt><code>mark</code> [</p>
<dd><i>u32_value</i> ] The value to set for the skb mark. The u32 value is required only when <code>use</code> is specified. If <code>mark</code> value is zero, it will not be encoded, instead &quot;overlimits&quot; statistics increment and <code>CONTROL</code> action is taken.</p>
<dt><code>prio</code> [</p>
<dd><i>u32_value</i> ] The value to set for priority in the skb structure. The u32 value is required only when <code>use</code> is specified.</p>
<dt><code>tcindex</code> [</p>
<dd><i>u16_value</i> ] Value to set for the traffic control index in the skb structure. The u16 value is required only when <code>use</code> is specified.</p>
<dt><code>dmac</code><i> DMAC</i></p>
<dd><code>smac</code><i> SMAC</i> Optional six byte destination or source MAC address to encode.</p>
<dt><code>type</code><i> TYPE</i></p>
<dd>Optional 16-bit ethertype to encode. If not specified value of 0xED3E will be used.</p>
<dt><code>CONTROL</code></p>
<dd>Action to take following an encode/decode.</p>
<dt><code>index</code><i> INDEX</i></p>
<dd>Assign a unique ID to this action instead of letting the kernel choose one automatically. <i>INDEX</i> is a 32bit unsigned integer greater than zero.</dl>
<h2>Examples</h2>
<p>On the receiving side, match packets with ethertype 0xdead and restart classification so that it will match ICMP on the next rule, at prio 3:</p>
<dl>
<dd># tc qdisc add dev eth0 handle ffff: ingress # tc filter add dev eth0 parent ffff: prio 2 protocol 0xdead \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match u32 0 0 flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action ife decode reclassify<br />
 # tc filter add dev eth0 parent ffff: prio 3 protocol ip \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 0xff flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action continue
</dl>
<p> Match with skb mark of 17:</p>
<dl>
<dd># tc filter add dev eth0 parent ffff: prio 4 protocol ip \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>handle 0x11 fw flowid 1:1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action ok
</dl>
<p> Configure the sending side to encode for the filters above. Use a destination IP address of 192.168.122.237/24, then tag with skb mark of decimal 17. Encode the packaet with ethertype 0xdead, add skb-&gt;mark to whitelist of metadatum to send, and rewrite the destination MAC address to 02:15:15:15:15:15.</p>
<dl>
<dd># tc qdisc add dev eth0 root handle 1: prio # tc filter add dev eth0 parent 1: protocol ip prio 10 u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip dst 192.168.122.237/24 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip protocol 1 0xff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action skbedit mark 17 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action ife encode \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>type 0xDEAD \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>allow mark \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>dst 02:15:15:15:15:15
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8) </p>
