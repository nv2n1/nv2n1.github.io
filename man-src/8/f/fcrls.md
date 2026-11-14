---
title: "fcrls(8)"
name: "fcrls"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcrls/"
description: "fcrls – Fibre Channel Read Link Error Status Block (RLS) tool"
---

<p>fcrls &#8211; Fibre Channel Read Link Error Status Block (RLS) tool</p>
<h2>Synopsis</h2>
<p><code>fcrls</code> &#8211;port <i>rport_bsg_name</i> [&#8211;quiet] </p>
<p> <code>fcrls</code> &#8211;fcid <i>rport_port_FC-ID</i> [&#8211;quiet] </p>
<p> <code>fcrls</code> &#8211;help</p>
<h2>Description</h2>
<p>The <code>fcrls</code> command performs Fibre Channel Read Link Error Status Block (RLS) ELS request (see FC-LS-2) via BSG over a given rport bsg name or FC-ID. </p>
<p> <code>fcrls</code> takes either a rport bsg name or a rport port FC-ID as the input. To disable verbose output, use the <code>&#8211;quiet</code> option.</p>
<h2>Options</h2>
<p><code>&#8211;port</code> <i>rport_bsg_name</i></p>
<dl>
<dd>Send RLS to a rport by FC remote port bsg name, e.g., rport-7:0-1.</dl>
<p> <code>&#8211;fcid</code> <i>rport_port_FC-ID</i></p>
<dl>
<dd>Send RLS to a rport by port FC-ID, e.g., 0xce000d.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dd>Disable verbose output.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Display a help message with basic usage instructions.</dl>
<h2>Examples</h2>
<p>Sends RLS to the FC remote port as rport-7:0-1 </p>
<dl>
<dd>
<pre>fcrls --port rport-7:0-1</pre>
</dl>
<p> Sends RLS to the FC remote port with 0xce000d as its port FC-ID </p>
<dl>
<dd>
<pre>fcrls --fcid 0xce000d</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoeadm/">fcoeadm</a></code>(8)</p>
<h2>Support</h2>
<p><code>fcrls</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/.">http://open-fcoe.org/.</a></p>
