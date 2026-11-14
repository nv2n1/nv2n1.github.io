---
title: "tc-stab(8)"
name: "tc-stab"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-stab/"
description: "tc-stab – Generic size table manipulations"
---

<p>tc-stab &#8211; Generic size table manipulations</p>
<h2>Synopsis</h2>
<pre>tc qdisc add ... stab
<dl><dt><dd>[ <code>mtu</code> BYTES ] [ <code>tsize</code> SLOTS ]
[ <code>mpu</code> BYTES ] [ <code>overhead</code> BYTES ]
[ <code>linklayer</code> { adsl | atm | ethernet } ] ...
</dl></pre>
<h2>Options</h2>
<p>For the description of BYTES &#8211; please refer to the <code>UNITS</code> section of <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8). </p>
<dl>
<dt><code>mtu</code></p>
<dd>maximum packet size we create size table for, assumed 2048 if not specified explicitly</p>
<dt><code>tsize</code></p>
<dd>required table size, assumed 512 if not specified explicitly</p>
<dt><code>mpu</code></p>
<dd>minimum packet size used in computations</p>
<dt><code>overhead</code></p>
<dd>per-packet size overhead (can be negative) used in computations</p>
<dt><code>linklayer</code></p>
<dd>required linklayer specification.</dl>
<h2>Description</h2>
<p>Size tables allow manipulation of packet sizes, as seen by the whole scheduler framework (of course, the actual packet size remains the same). Adjusted packet size is calculated only once &#8211; when a qdisc enqueues the packet. Initial root enqueue initializes it to the real packet&#8217;s size. Each qdisc can use a different size table, but the adjusted size is stored in an area shared by whole qdisc hierarchy attached to the interface. The effect is that if you have such a setup, the last qdisc with a stab in a chain &quot;wins&quot;. For example, consider HFSC with simple pfifo attached to one of its leaf classes. If that pfifo qdisc has stab defined, it will override lengths calculated during HFSC&#8217;s enqueue; and in turn, whenever HFSC tries to dequeue a packet, it will use a potentially invalid size in its calculations. Normal setups will usually include stab defined only on root qdisc, but further overriding gives extra flexibility for less usual setups. The initial size table is calculated by <code>tc</code> tool using <code>mtu</code> and <code>tsize</code> parameters. The algorithm sets each slot&#8217;s size to the smallest power of 2 value, so the whole <code>mtu</code> is covered by the size table. Neither <code>tsize</code>, nor <code>mtu</code> have to be power of 2 value, so the size table will usually support more than is required by <code>mtu</code>. For example, with <code>mtu</code>~=~1500 and <code>tsize</code>~=~128, a table with 128 slots will be created, where slot 0 will correspond to sizes 0-16, slot 1 to 17~-~32, &#8230;, slot 127 to 2033~-~2048. Sizes assigned to each slot depend on <code>linklayer</code> parameter. Stab calculation is also safe for an unusual case, when a size assigned to a slot would be larger than 2^16-1 (you will lose the accuracy though). During the kernel part of packet size adjustment, <code>overhead</code> will be added to original size, and then slot will be calculated. If the size would cause overflow, more than 1 slot will be used to get the final size. This of course will affect accuracy, but it&#8217;s only a guard against unusual situations. Currently there are two methods of creating values stored in the size table &#8211; ethernet and atm (adsl):</p>
<dl>
<dt>ethernet</p>
<dd>This is basically 1-1 mapping, so following our example from above (disregarding <code>mpu</code> for a moment) slot 0 would have 8, slot 1 would have 16 and so on, up to slot 127 with 2048. Note, that <code>mpu</code>~&gt;~0 must be specified, and slots that would get less than specified by <code>mpu</code> will get <code>mpu</code> instead. If you don&#8217;t specify <code>mpu</code>, the size table will not be created at all (it wouldn&#8217;t make any difference), although any <code>overhead</code> value will be respected during calculations.</p>
<dt>atm, adsl</p>
<dd>ATM linklayer consists of 53 byte cells, where each of them provides 48 bytes for payload. Also all the cells must be fully utilized, thus the last one is padded if/as necessary. When the size table is calculated, adjusted size that fits properly into lowest amount of cells is assigned to a slot. For example, a 100 byte long packet requires three 48-byte payloads, so the final size would require 3 ATM cells &#8211; 159 bytes. For ATM size tables, 16~bytes sized slots are perfectly enough. The default values of <code>mtu</code> and <code>tsize</code> create 4~bytes sized slots.</dl>
<h2>Typical Overheads</h2>
<p>The following values are typical for different adsl scenarios (based on <code>[1]</code> and <code>[2]</code>): </p>
<pre>LLC based:
<dl><dt><dd>PPPoA - 14 (PPP - 2, ATM - 12)
PPPoE - 40+ (PPPoE - 8, ATM - 18, ethernet 14, possibly FCS - 4+padding)
Bridged - 32 (ATM - 18, ethernet 14, possibly FCS - 4+padding)
IPoA - 16 (ATM - 16)
</dl>
VC Mux based:
<dl><dt><dd>PPPoA - 10 (PPP - 2, ATM - 8)
PPPoE - 32+ (PPPoE - 8, ATM - 10, ethernet 14, possibly FCS - 4+padding)
Bridged - 24+ (ATM - 10, ethernet 14, possibly FCS - 4+padding)
IPoA - 8 (ATM - 8)
</dl></pre>
<p>There are a few important things regarding the above overheads:</p>
<dl>
<dt>&bull;</p>
<dd>IPoA in LLC case requires SNAP, instead of LLC-NLPID (see rfc2684) &#8211; this is the reason why it actually takes more space than PPPoA.</p>
<dt>&bull;</p>
<dd>In rare cases, FCS might be preserved on protocols that include Ethernet frames (Bridged and PPPoE). In such situation, any Ethernet specific padding guaranteeing 64 bytes long frame size has to be included as well (see RFC2684). In the other words, it also guarantees that any packet you send will take minimum 2 atm cells. You should set <code>mpu</code> accordingly for that.</p>
<dt>&bull;</p>
<dd>When the size table is consulted, and you&#8217;re shaping traffic for the sake of another modem/router, an Ethernet header (without padding) will already be added to initial packet&#8217;s length. You should compensate for that by subtracting 14 from the above overheads in this case. If you&#8217;re shaping directly on the router (for example, with speedtouch usb modem) using ppp daemon, you&#8217;re using raw ip interface without underlying layer2, so nothing will be added. </p>
<p> For more thorough explanations, please see <code>[1]</code> and <code>[2]</code>.</dl>
<h2>Ethernet Cards Considerations</h2>
<p>It&#8217;s often forgotten that modern network cards (even cheap ones on desktop motherboards) and/or their drivers often support different offloading mechanisms. In the context of traffic shaping, &#8216;tso&#8217; and &#8216;gso&#8217; might cause undesirable effects, due to massive TCP segments being considered during traffic shaping (including stab calculations). For slow uplink interfaces, it&#8217;s good to use <code>ethtool</code> to turn off offloading features.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/7-tc-hfsc/">tc-hfsc</a></code>(7), <code><a href="/docs/linux/man/8-tc-hfsc/">tc-hfsc</a></code>(8),<br />
 <code>[1]</code> <a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/tc-atm/">http://ace-host.stuart.id.au/russell/files/tc/tc-atm/</a><br />
 <code>[2]</code> <a rel="nofollow" href="http://www.faqs.org/rfcs/rfc2684.html">http://www.faqs.org/rfcs/rfc2684.html</a> </p>
<p> Please direct bugreports and patches to: &lt;netdev [at] vger.kernel.org&gt;</p>
<h2>Author</h2>
<p>Manpage created by Michal Soltys (soltys [at] ziu.info)</p>
