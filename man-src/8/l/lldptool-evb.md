---
title: "lldptool-evb(8)"
name: "lldptool-evb"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-evb/"
description: "evb – Show / manipulate EVB TLV configuration"
---

<p>evb &#8211; Show / manipulate EVB TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -g ncb -i ethx -V evbCfg -c enableTx</code> <code>lldptool -T -g ncb -i ethx -V evbCfg -c enableTx=[yes|no]</code> <code>lldptool -t -g ncb -i ethx -V evbCfg -c fmode</code> <code>lldptool -T -g ncb -i ethx -V evbCfg -c fmode=[bridge|reflectiverelay]</code> <code>lldptool -t -g ncb -i ethx -V evbCfg -c capabilities</code> <code>lldptool -T -g ncb -i ethx -V evbCfg -c capabilities=[rte|ecp|vdp|none]</code> <code>lldptool -t -g ncb -i ethx -V evbCfg -c rte</code> <code>lldptool -T -g ncb -i ethx -V evbCfg -c rte=[&lt;rte&gt;]</code> <code>lldptool -t -g ncb -i ethx -V evbCfg -c vsis</code> <code>lldptool -T -g ncb -i ethx -V evbCfg -c vsis=[&lt;number of vsis&gt;]</code> </p>
<h2>Description</h2>
<p>The EVB TLV is a TLV to announce the station and bridge&#8217;s edge virtual bridging (evb) capabilities and request the bridge forwarding mode. If both sides have agree on edge control protocol (ECP), VSI discovery protocol (VDP) capabilities, both sides can exchange VDP TLV using ECP frames. The vsis parameter will set the maximum number of VSIs and show the number of currently configured VSIs. </p>
<h2>Arguments</h2>
<dl>
<dt><code>enableTx</code></dt>
<dd>Enables the EVB TLV to be transmitted</dd>
<dt><code>fmode</code></dt>
<dd>shows or sets the forwarding mode between bridge (default) or reflectiverelay (RR).</dd>
<dt><code>capabilities</code></dt>
<dd>shows or sets the local capabilities that are announced to the adjacent switch in the TLV. This parameter will accept any combination of rte, vdp or ecp, separated by &quot;,&quot;. Use the keyword &quot;none&quot; if you do not want to set any capabilities.</dd>
<dt><code>rte</code></dt>
<dd>shows or set the local run time exponent (RTE). The RTE will be used as the base for the timing of the ECP and VDP protocols.</dd>
<dt><code>vsis</code></dt>
<dd>shows or sets the number of virtual station interfaces (VSIs) that are announced to the adjacent switch in the TLV. This parameter expects a number between 0 and 65535. </dd>
</dl>
<h2>Theory of Operation</h2>
<p>The EVB TLV is used to announce and exchange supported parameters between the station and an adjacent switch. The TLV uses the nearest customer bridge agent. </p>
<p> If &quot;reflectiverelay&quot; is set as forwarding mode, the switch will allow &quot;reflection&quot; of frames coming from different sources at the same port back to the port. This will allow communication between virtual machines on the same host via the switch. </p>
<p> The capabilities parameter is used to set RTE, ECP and VDP support. VDP TLVs in ECP frames can only be exchanged if both sides agree on ECP and VDP as capabilities. RTE will be used as the base timing parameter for ECP and VDP.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Display locally configured values for <i>eth8</i></dt>
<dd><code>lldptool -t -g ncb -i eth8 -V evbCfg</code></dd>
<dt>Display remotely configured values for <i>eth8</i></dt>
<dd><code>lldptool -n -g ncb -t -i eth8 -V evbCfg</code></dd>
<dt>Display wether evb tlv is configured for tx on <i>eth8</i></dt>
<dd><code>lldptool -t -g ncb -i eth8 -V evbCfg -c enableTx</code></dd>
<dt>Display the currently requested forwarding mode for <i>eth8</i></dt>
<dd><code>lldptool -t -g ncb -i eth8 -V evbCfg -c fmode</code></dd>
<dt>Set the forwarding mode to reflective relay</dt>
<dd><code>lldptool -T -g ncb -i eth8 -V evbCfg -c fmode=reflectiverelay</code></dd>
<dt>Display the currently configured capabilities</dt>
<dd><code>lldptool -t -g ncb -i ethx -V evbCfg -c capabilities</code></dd>
<dt>Set the locally possible capabilities to RTE, ECP and VDP</dt>
<dd><code>lldptool -T -g ncb -i ethx -V evbCfg -c capabilities=rte,ecp,vdp</code></dd>
<dt>Resets the locally possible capabilities to &quot;none&quot;</dt>
<dd><code>lldptool -T -g ncb -i ethx -V evbCfg -c capabilities=none</code></dd>
<dt>Display the locally configured value for RTE</dt>
<dd><code>lldptool -t -g ncb -i ethx -V evbCfg -c rte</code></dd>
<dt>Set the value for RTE</dt>
<dd><code>lldptool -T -g ncb -i ethx -V evbCfg -c rte=[&lt;rte&gt;]</code></dd>
<dt>Display the configured maximum number of VSIs</dt>
<dd><code>lldptool -t -g ncb -i ethx -V evbCfg -c vsis</code></dd>
<dt>Set the maximum number of VSIs</dt>
<dd><code>lldptool -T -g ncb -i ethx -V evbCfg -c vsis=[&lt;number of vsis&gt;]</code> </dd>
</dl>
<h2>Source</h2>
<dl>
<dt>o</dt>
<dd>IEEE 802.1Qbg (<a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1bg.html)">http://www.ieee802.org/1/pages/802.1bg.html)</a> </dd>
</dl>
<h2>Notes</h2>
<p>Currently the code in lldpad reflects draft 0 of the upcoming standard. EVB TLVs on the wire can be decoded with wireshark &gt; v1.6. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>Jens Osterkamp</p>
