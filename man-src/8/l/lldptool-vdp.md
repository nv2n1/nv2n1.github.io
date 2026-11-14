---
title: "lldptool-vdp(8)"
name: "lldptool-vdp"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-vdp/"
description: "vdp – Show / manipulate VDP TLV configuration"
---

<p>vdp &#8211; Show / manipulate VDP TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V vdp -c enableTx</code> <code>lldptool -T -i ethx -V vdp -c enableTx=[yes|no]</code> <code>lldptool -t -i ethx -V vdp -c mode</code> <code>lldptool -T -i ethx -V vdp -c mode=&lt;mode&gt;,&lt;mgrid&gt;,&lt;typeid&gt;,&lt;typeidversion&gt;,&lt;instanceid&gt;,&lt;mac&gt;,&lt;vlan&gt;</code> <code>lldptool -t -i ethx -V vdp -c role</code> <code>lldptool -T -i ethx -V vdp -c role=[station|bridge]</code> </p>
<h2>Description</h2>
<p>The VSI discovery protocol (VDP) is <i>NOT</i> a TLV in the LLDP sense but rather a protocol to manage the association and deassociation of virtual station interfaces (VSIs) between the station and an adjacent switch. VDP uses ECP as transport for VDP TLVs. An ECP frame may contain multiple VDP TLVs. Each VDP TLVs contains a mode, typeid, version, instanceid, mac and vlan for a VSI. </p>
<h2>Arguments</h2>
<dl>
<dt><code>enableTx</code></p>
<dd>Enables or disables VDP</p>
<dt><code>mode</code></p>
<dd>shows or sets modes for VSIs with the following parameters:</p>
<dl>
<dd>
<dl>
<dt>&lt;mode&gt;</p>
<dd>mode (0=preassociate, 1=preassociate with RR, 2=associate, 3=deassociate)</p>
<dt>&lt;mgrid&gt;</p>
<dd>manager (database) id</p>
<dt>&lt;typeid&gt;</p>
<dd>VSI type id</p>
<dt>&lt;version&gt;</p>
<dd>VSI type id version</p>
<dt>&lt;instanceid&gt;</p>
<dd>VSI instance id</p>
<dt>&lt;format&gt;</p>
<dd>VDP filter info format</p>
<dt>&lt;mac&gt;</p>
<dd>VSI mac address</p>
<dt>&lt;vlan&gt;</p>
<dd>VSI vlan id</dl>
</dl>
<dt><code>role</code></p>
<dd>shows or sets the role of the local machine to act as either station (default) or bridge. </p>
</dl>
<h2>Theory of Operation</h2>
<p>The VDP protocol is used to pre-associate, associate or deassociate VSIs to and adjacent switch. Information about the VSIs is formatted into VDP TLVs which are then handed to ECP for lower-level transport. Each ECP frame may contain multiple VDP TLVs. </p>
<p> Two ways to receive VSI information exist in llpdad: via netlink or with lldptool. netlink is used by libvirt to communicate VSIs to lldpad. lldptool can be used to associate/deassociate VSIs from the command line. This is especially helpful for testing purposes.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Display if vdp is enabled on <i>eth8</i></p>
<dd><code>lldptool -t -i eth8 -V vdp -c enableTx</code></p>
<dt>Enable vdp on <i>eth8</i></p>
<dd><code>lldptool -T -i eth8 -V vdp -c enableTx=yes</code></p>
<dt>Display the currently configured VSIs for <i>eth8</i></p>
<dd><code>lldptool -t -i eth8 -V vdp -c mode</code></p>
<dt>Associate a VSI on <i>eth8</i></p>
<dd><code>lldptool -T -i eth8 -V vdp -c mode=2,12,1193046,1,fa9b7fff-b0a0-4893-8e0e-beef4ff18f8f,2,52:54:00:C7:3E:CE,3</code></p>
<dt>Display the locally configured role for VDP on <i>eth8</i></p>
<dd><code>lldptool -t -i eth8 -V vdp -c role</code></p>
<dt>Set the local role for VDP on <i>eth8</i></p>
<dd><code>lldptool -T -i eth8 -V vdp -c role=bridge</code> </p>
</dl>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>IEEE 802.1Qbg (<a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1bg.html)">http://www.ieee802.org/1/pages/802.1bg.html)</a> </p>
</dl>
<h2>Notes</h2>
<p>Currently the code in lldpad reflects draft 0 of the upcoming standard. ECP/VDP TLVs on the wire can be decoded with wireshark &gt; v1.8. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool-evb/">lldptool-evb</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>Jens Osterkamp</p>
