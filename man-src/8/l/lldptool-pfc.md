---
title: "lldptool-pfc(8)"
name: "lldptool-pfc"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-pfc/"
description: "PFC – Show / manipulate PFC TLV configuration"
---

<p>PFC &#8211; Show / manipulate PFC TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V PFC [ -c [ enableTx | willing | enabled | delay ] ]</code> <code>lldptool -T -i ethx -V PFC</code> &lt;<i>CONFIG_ARG=value</i> <i>&#8230;</i>&gt;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>CONFIG_ARG</i>:= <code>enableTx=</code>&lt;<code>yes</code>|<code>no</code>&gt; <code>willing=</code>&lt;<code>yes</code>|<code>no</code>|<code>0</code>|<code>1</code>&gt; <code>enabled=</code>&lt;<code>none</code>|[<code>0</code>..<code>7</code>]<code>,</code>[<code>0</code>..<code>7</code>]<code>,</code>&#8230;&gt; <code>delay=</code>&lt;integer value&gt; </p>
<h2>Description</h2>
<p>The PFC TLV is used to display and set current PFC TLV attributes. </p>
<h2>Arguments</h2>
<dl>
<dt><code>enableTx</code></p>
<dd>Enable the PFC TLV to be transmitted in the LLDP PDU for the specified interface.</p>
<dt><code>willing</code></p>
<dd>Display or set the willing attribute. If set to <code>yes</code> and a peer TLV is received then the peer PFC attributes will be used. If set to <code>no</code> then locally configured attributes are used.</p>
<dt><code>enabled</code></p>
<dd>Display or set the priorities with PFC enabled. The set attribute takes a comma separated list of priorities to enable, or the string <code>none</code> to disable all priorities.</p>
<dt><code>delay </code></p>
<dd>Display or set the delay attribute used to configure PFC thresholds in hardware buffers. If PFC is enabled and frames continue to be dropped due to full hardware buffers then increasing this value may help. </p>
</dl>
<h2>Theory of Operations</h2>
<p>The PFC TLV uses the Symmetric attribute passing state machine defined in IEEE 802.1Qaz. This means the attributes used will depend on the willing bit. If the willing bit is set to 1 and a peer TLV is received then the peers attributes will be used. If the willing bit is set to 0 the local attributes will be used. When both the peer and local configuration are willing a tie breaking scheme is used. For more detailed coverage see the specification.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Enable PFC for priorities 1, 2, and 4 on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V PFC enabled=1,2,4</code></p>
<dt>Disable PFC for all priorities on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V PFC enabled=none</code></p>
<dt>Display configuration of PFC enabled priorities for <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V PFC -c enabled </code></p>
<dt>Display last transmitted PFC TLV on <i>eth2</i></p>
<dd><code>lldptool -t -i eth2 -V PFC </code></dl>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>IEEE 802.1Qaz (<a rel="nofollow" href="http://www.ieee802.org/1/pages/dcbridges.html)">http://www.ieee802.org/1/pages/dcbridges.html)</a> </p>
</dl>
<h2>Notes</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>John Fastabend</p>
