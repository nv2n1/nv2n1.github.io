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
<h2>SYNOPSIS</h2>
<p> <code>mip6d [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> Mobile IPv6 and NEMO Basic Support implementation </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information and copyright</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Display this help text</p>
<dt><code>-c &lt;file&gt;</code></p>
<dd> Read configuration from &lt;file&gt;. If option is not present, default path (/etc/mip6d.conf) is used.<br />
&nbsp;<wbr></dl>
<p> These options override values read from config file:</p>
<dl>
<dt><code>-d &lt;number&gt;</code></p>
<dd> Set debug level (0-10)</p>
<dt><code>-C, &#8211;correspondent-node</code></p>
<dd> Node is CN</p>
<dt><code>-H, &#8211;home-agent</code></p>
<dd> Node is HA</p>
<dt><code>-M, &#8211;mobile-node</code></p>
<dd> Node is MN </p>
</dl>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the daemon:</p>
<dl>
<dt><code>&nbsp;<wbr>SIGHUP</code></p>
<dd> Reload the configuration. See <code><a href="/docs/linux/man/5-mip6d-conf/">mip6d.conf</a></code>(5) for information on supported option reload.</p>
<dt><code>&nbsp;<wbr>SIGINT, SIGTERM</code></p>
<dd> Terminates the daemon operation. </p>
</dl>
<h2>FILES</h2>
<p> /etc/mip6d.conf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-mip6d-conf/">mip6d.conf</a></code>(5), <code><a href="/docs/linux/man/7-mipv6/">mipv6</a></code>(7), </p>
<p> RFC6275: Mobility Support in IPv6 </p>
<p> RFC3776: Using IPsec to Protect Mobile IPv6 Signaling Between Mobile Nodes and Home Agents </p>
<p> RFC4877: Mobile IPv6 Operation with IKEv2 and the Revised IPsec Architecture </p>
<p> RFC3963: Network Mobility (NEMO) Basic Support Protocol </p>
<h2>Index</h2>
