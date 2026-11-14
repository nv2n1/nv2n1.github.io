---
title: "lldptool-med(8)"
name: "lldptool-med"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-med/"
description: "LLDP-MED – Show / manipulate MED TLV configurations"
---

<p>LLDP-MED &#8211; Show / manipulate MED TLV configurations</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V</code> [ <i>TLV_TYPE</i> ] <code>enableTx</code> </p>
<pre><code>lldptool -T -i ethx -V

[ TLV_TYPE ]

enableTx =

{ yes | no }
lldptool -T -i ethx -V

LLDP-MED
devtype =

{ class1 | class2 | class3 | none }</code></pre>
<p> <code>lldptool -t -i ethx -V</code> LLDP-MED <code>devtype</code> </p>
<pre><code>TLV_TYPE : = {LLDP-MED | medCap | medPolicy | medLoc | medPower | medHwRev | medFwRev | medSwRev | medSerNum | medManuf | medModel | medAssetID }
</code></pre>
<h2>Description</h2>
<p>The <code>LLDP-MED</code> extensions support the Link Layer Discovery Protocol for <code>Media Endpoint Devices</code> defined in the <code>ANSI/TIA-1057-2006</code> document. Each TLV can be configured as a <code>class1</code> , <code>class2</code> or <code>class3</code> device. Class I devices are the most basic class of Endpoint Device, Class II devices support media stream capabilities and Class III devices directly support end users of the IP communication system. See <code>ANS-TIA-1057</code> for clarification of class types. </p>
<h2>Arguments</h2>
<dl>
<dt><code>enableTx</code></p>
<dd>Enables the TLV to be transmitted</p>
<dt><code>devtype</code></p>
<dd>Set or query the class type of the device. </p>
</dl>
<h2>Tlv_Type</h2>
<p>List of supported TLV specifiers applicable to Media Endpoint Devices. </p>
<dl>
<dt><code>LLDP-MED</code></p>
<dd>apply arguments to all supported MED TLVs. </p>
<dt><code>medCAP</code></p>
<dd>LLDP-MED Capabilities TLV </p>
<dt><code>medPolicy</code></p>
<dd>LLDP-MED Network Policy TLV </p>
<dt><code>medLoc</code></p>
<dd>LLDP-MED Location TLV </p>
<dt><code>medPower</code></p>
<dd>LLDP-MED Extended Power-via-MDI TLV </p>
<dt><code>medHwRev</code></p>
<dd>LLDP-MED Hardware Revision TLV </p>
<dt><code>medFwRev</code></p>
<dd>LLDP-MED Firmware Revision TLV </p>
<dt><code>medSwRev</code></p>
<dd>LLDP-MED Software Revision TLV </p>
<dt><code>medSerNum</code></p>
<dd>LLDP-MED Serial Number TLV </p>
<dt><code>medManuf</code></p>
<dd>LLDP-MED Manufacturer Name TL </p>
<dt><code>medModel</code></p>
<dd>LLDP-MED Model Name TLV </p>
<dt><code>medAssetID</code></p>
<dd>LLDP-MED Asset ID TLV </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Enable class1 MED device on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V LLDP-MED enableTx=yes devtype=class1</code></p>
<dt>Query class type of MED on <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V LLDP-MED -c devtype</code></p>
<dt>Query transmit state of medPolicy on device <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V medPolicy -c enableTx</code></p>
<dd></dl>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>Link Layer Discovery Protocol for Media Endpoint Devices (<a rel="nofollow" href="http://www.tiaonline.org/standards/technology/voip/documents/ANSI-TIA-1057_final_for_publication.pdf)">http://www.tiaonline.org/standards/technology/voip/documents/ANSI-TIA-1057_final_for_publication.pdf)</a> </p>
</dl>
<h2>Notes</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>John Fastabend</p>
