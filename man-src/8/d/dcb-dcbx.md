---
title: "dcb-dcbx(8)"
name: "dcb-dcbx"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-dcbx/"
description: "dcb-dcbx – show / manipulate port DCBX (Data Center Bridging eXchange)"
---

<p>dcb-dcbx &#8211; show / manipulate port DCBX (Data Center Bridging eXchange)</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

dcbx

{ COMMAND | help }
</code></pre>
<p> <code>dcb dcbx show dev</code> DEV<br />
 <code>dcb dcbx set dev</code> DEV [ <code>host</code> ] [ <code>lld-managed</code> ] [ <code>cee</code> ] [ <code>ieee</code> ] [ <code>static</code> ] </p>
<h2>Description</h2>
<p>Data Center Bridging eXchange (DCBX) is a protocol used by DCB devices to exchange configuration information with directly connected peers. The Linux DCBX object is a 1-byte bitfield of flags that configure whether DCBX is implemented in the device or in the host, and which version of the protocol should be used. <code>dcb dcbx</code> is used to access the per-port Linux DCBX object. There are two principal modes of operation: in <code>host</code> mode, DCBX protocol is implemented by the host LLDP agent, and the DCB interfaces are used to propagate the negotiate parameters to capable devices. In <code>lld-managed</code> mode, the configuration is handled by the device, and DCB interfaces are used for inspection of negotiated parameters, and can also be used to set initial parameters. </p>
<h2>Parameters</h2>
<p>When used with <code>dcb dcbx set,</code> the following keywords enable the corresponding configuration. The keywords that are not mentioned on the command line are considered disabled. When used with <code>show,</code> each enabled feature is shown by its corresponding keyword. </p>
<dl>
<dt><code>host</code></p>
<dd><code>lld-managed</code> The device is in the host mode of operation and, respectively, the lld-managed mode of operation, as described above. In principle these two keywords are mutually exclusive, but <code>dcb dcbx</code> allows setting both and lets the driver handle it as appropriate. </p>
<dt><code>cee</code></p>
<dd><code>ieee</code> The device supports CEE (Converged Enhanced Ethernet) and, respecively, IEEE version of the DCB specification. Typically only one of these will be set, but <code>dcb dcbx</code> does not mandate this. </p>
<dt><code>static</code></p>
<dd>indicates the engine supports static configuration. No actual negotiation is performed, negotiated parameters are always the initial configuration. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Put the DCB engine into the &quot;host&quot; mode of operation, and use IEEE-standardized DCB interfaces: </p>
<p> # dcb dcbx set dev eth0 host ieee </p>
<p> Show what was set: </p>
<p> # dcb dcbx show dev eth0<br />
 host ieee</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
