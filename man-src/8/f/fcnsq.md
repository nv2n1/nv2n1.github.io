---
title: "fcnsq(8)"
name: "fcnsq"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcnsq/"
description: "fcnsq – Fibre Channel Name Server Query Tool"
---

<p>fcnsq &#8211; Fibre Channel Name Server Query Tool</p>
<h2>Synopsis</h2>
<p><code>fcnsq</code> <i>host</i> &#8211;gpn <i>port_id</i> [-q | &#8211;quiet] </p>
<p> <code>fcnsq</code> <i>host</i> &#8211;gnn <i>port_id</i> [-q | &#8211;quiet] </p>
<p> <code>fcnsq</code> <i>host</i> &#8211;gspn <i>port_id</i> [-q | &#8211;quiet] </p>
<p> <code>fcnsq</code> <i>host</i> &#8211;gsnn <i>wwpn</i> [-q | &#8211;quiet] </p>
<p> <code>fcnsq</code> ?</p>
<h2>Description</h2>
<p>The <code>fcnsq</code> command performs Fibre Channel Name Server queries for a user-specified FC Host. The supported name server query commands include: Get Port Name (GPN), Get Node Name (GNN), Get Symbolic Node Name (GSNN), and Get Symbolic Port Name (GSPN) as described in FC-GS-3 for the Common Transport (CT) services. </p>
<p> <code>fcnsq</code> takes the host bsg name as the input for the target host. Host bsg name must be a valid bsg device, e.g., &quot;host12&quot; as derived from /dev/bsg/fc_host12. For each name server query command, the argument is either a Port ID or a World Wide Port Name. Port IDs and World Wide Names must be specified in hexadecimal. To disable verbose output, use the <code>&#8211;quiet</code> option.</p>
<h2>Options</h2>
<p><code>host</code> <code>&#8211;gpn</code> <i>port_id</i></p>
<dl>
<dd>Get Port Name by Port ID for <i>host</i>.</dl>
<p> <code>host</code> <code>&#8211;gnn</code> <i>port_id</i></p>
<dl>
<dd>Get Node Name by Port ID for <i>host</i>.</dl>
<p> <code>host</code> <code>&#8211;gspn</code> <i>port_id</i></p>
<dl>
<dd>Get Symbolic Port Name by Port ID for <i>host</i>.</dl>
<p> <code>host</code> <code>&#8211;gsnn</code> <i>wwpn</i></p>
<dl>
<dd>Get Symbolic Node Name by World Wide Port Name for <i>host</i>.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Disable verbose output.</dl>
<p> <code>?</code></p>
<dl>
<dd>Display a help message with basic usage instructions.</dl>
<h2>Examples</h2>
<p>Query Get Port Name (GPN) from host12 for Port ID 0xbf0027 </p>
<dl>
<dd>
<pre>fcnsq host12 --gpn bf0027</pre>
</dl>
<p> Query Get Node Name (GNN) from host12 for Port ID 0xbf0027 </p>
<dl>
<dd>
<pre>fcnsq host12 --gnn bf0027</pre>
</dl>
<p> Query Get Symbolic Port Name (GSPN) from host12 for Port ID 0xbf0027 </p>
<dl>
<dd>
<pre>fcnsq host12 --gspn bf0027</pre>
</dl>
<p> Query Get Symbolic Node Name (GSNN) from host12 for WWWPN 0x1000001B213C9DDA </p>
<dl>
<dd>
<pre>fcnsq host12 --gsnn 0x1000001B213C9DDA</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoeadm/">fcoeadm</a></code>(8)</p>
<h2>Support</h2>
<p><code>fcnsq</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/.">http://open-fcoe.org/.</a></p>
