---
title: "tc-skbedit(8)"
name: "tc-skbedit"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-skbedit/"
description: "skbedit – SKB editing action"
---

<p>skbedit &#8211; SKB editing action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action skbedit </code>[<code> queue_mapping</code> <i>QUEUE_MAPPING</i> ] [ <code>priority</code> <i>PRIORITY</i> ] [ <code>mark</code><i> MARK</i>[<code>/</code><i>MASK] ] [</i> <code>ptype</code> <i>PTYPE</i> ] [ <code>inheritdsfield</code> ]</p>
<h2>Description</h2>
<p>The <code>skbedit</code> action allows to change a packet&#8217;s associated meta data. It complements the <code>pedit</code> action, which in turn allows to change parts of the packet data itself. </p>
<p> The most unique feature of <code>skbedit</code> is its ability to decide over which queue of an interface with multiple transmit queues the packet is to be sent out. The number of available transmit queues is reflected by sysfs entries within <i>/sys/class/net/&lt;interface&gt;/queues</i> with name <i>tx-N</i> (where <i>N</i> is the actual queue number).</p>
<h2>Options</h2>
<dl>
<dt><code>queue_mapping</code><i> QUEUE_MAPPING</i></p>
<dd>Override the packet&#8217;s transmit queue. Useful when applied to packets transmitted over MQ-capable network interfaces. <i>QUEUE_MAPPING</i> is an unsigned 16bit value in decimal format.</p>
<dt><code>priority</code><i> PRIORITY</i></p>
<dd>Override the packet classification decision. <i>PRIORITY</i> is either <code>root</code>, <code>none</code> or a hexadecimal major class ID optionally followed by a colon (<code>:</code>) and a hexadecimal minor class ID.</p>
<dt><code>mark</code><i> MARK</i>[<code>/</code><i>MASK]</i></p>
<dd>Change the packet&#8217;s firewall mark value. <i>MARK</i> is an unsigned 32bit value in automatically detected format (i.e., prefix with &#8216;<code>0x</code>&#8216; for hexadecimal interpretation, etc.). <i>MASK</i> defines the 32-bit mask selecting bits of mark value. Default is 0xffffffff.</p>
<dt><code>ptype</code><i> PTYPE</i></p>
<dd>Override the packet&#8217;s type. Useful for setting packet type to host when needing to allow ingressing packets with the wrong MAC address but correct IP address. <i>PTYPE</i> is one of: host, otherhost, broadcast, multicast</p>
<dt><code>inheritdsfield</code></p>
<dd>Override the packet classification decision, and any value specified with <code>priority</code>, using the information stored in the Differentiated Services Field of the IPv6/IPv4 header (RFC2474).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-pedit/">tc-pedit</a></code>(8) </p>
