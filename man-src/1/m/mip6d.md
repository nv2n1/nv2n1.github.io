---

title: "mip6d(1)"
name: "mip6d"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mip6d/"
description: "mip6d – UMIP Mobile IPv6 and NEMO Basic Support protocol implementation"
---

<h2>NAME</h2>
<p> mip6d &#8211; UMIP Mobile IPv6 and NEMO Basic Support protocol implementation</p>
<p> <code>mip6d [options]</code> </p>
<p> Mobile IPv6 and NEMO Basic Support implementation </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display version information and copyright</dd>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Display this help text</dd>
<dt><code>-c &lt;file&gt;</code></dt>
<dd> Read configuration from &lt;file&gt;. If option is not present, default path (/etc/mip6d.conf) is used.<br />
&nbsp;<wbr></dd></dl>
<p> These options override values read from config file:</p>
<dl>
<dt><code>-d &lt;number&gt;</code></dt>
<dd> Set debug level (0-10)</dd>
<dt><code>-C, &#8211;correspondent-node</code></dt>
<dd> Node is CN</dd>
<dt><code>-H, &#8211;home-agent</code></dt>
<dd> Node is HA</dd>
<dt><code>-M, &#8211;mobile-node</code></dt>
<dd> Node is MN </dd>
</dl>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the daemon:</p>
<dl>
<dt><code>&nbsp;<wbr>SIGHUP</code></dt>
<dd> Reload the configuration. See <code><a href="/docs/linux/man/5-mip6d-conf/">mip6d.conf</a></code>(5) for information on supported option reload.</dd>
<dt><code>&nbsp;<wbr>SIGINT, SIGTERM</code></dt>
<dd> Terminates the daemon operation. </dd>
</dl>
<h2>FILES</h2>
<p> /etc/mip6d.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-mip6d-conf/">mip6d.conf</a></code>(5), <code><a href="/docs/linux/man/7-mipv6/">mipv6</a></code>(7), </p>
<p> RFC6275: Mobility Support in IPv6 </p>
<p> RFC3776: Using IPsec to Protect Mobile IPv6 Signaling Between Mobile Nodes and Home Agents </p>
<p> RFC4877: Mobile IPv6 Operation with IKEv2 and the Revised IPsec Architecture </p>
<p> RFC3963: Network Mobility (NEMO) Basic Support Protocol </p>
