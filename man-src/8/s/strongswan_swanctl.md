---
title: "strongswan_swanctl(8)"
name: "strongswan_swanctl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-strongswan_swanctl/"
description: "swanctl – strongSwan configuration, control and monitoring command line interface."
---

<p>swanctl &#8211; strongSwan configuration, control and monitoring command line interface.</p>
<h2>Synopsis</h2>
<p><i>command</i> [<i>option~</i>&#8230;] <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>swanctl is a cross-platform command line utility to configure, control and monitor the strongSwan IKE daemon. It is a replacement for the aging <code>starter</code>, <code>ipsec</code> and <code>stroke</code> tools. swanctl uses a configuration file called <code><a href="/docs/linux/man/5-swanctl-conf/">swanctl.conf</a></code>(5) to parse configurations and credentials. Private keys, certificates and other PKI related credentials are read from specific directories. To communicate with the IKE daemon, swanctl uses the VICI protocol, the Versatile IKE Configuration Interface. This stable interface is usable by other tools and is often preferable than scripting swanctl and parsing its output. </p>
<h2>Commands</h2>
<dl>
<dt><code>-i, &#8211;initiate</code></p>
<dd>initiate a connection</p>
<dt><code>-t, &#8211;terminate</code></p>
<dd>terminate a connection</p>
<dt><code>-R, &#8211;rekey</code></p>
<dd>rekey an SA</p>
<dt><code>-d, &#8211;redirect</code></p>
<dd>redirect an IKE_SA</p>
<dt><code>-p, &#8211;install</code></p>
<dd>install a trap or shunt policy</p>
<dt><code>-u, &#8211;uninstall</code></p>
<dd>uninstall a trap or shunt policy</p>
<dt><code>-l, &#8211;list-sas</code></p>
<dd>list currently active IKE_SAs</p>
<dt><code>-P, &#8211;list-pols</code></p>
<dd>list currently installed policies</p>
<dt><code>-b, &#8211;load-authorities</code></p>
<dd>(re-)load certification authorities information</p>
<dt><code>-L, &#8211;list-conns</code></p>
<dd>list loaded configurations</p>
<dt><code>-B, &#8211;list-authorities</code></p>
<dd>list loaded certification authorities information</p>
<dt><code>-x, &#8211;list-certs</code></p>
<dd>list stored certificates</p>
<dt><code>-A, &#8211;list-pools</code></p>
<dd>list loaded pool configurations</p>
<dt><code>-g, &#8211;list-algs</code></p>
<dd>list loaded algorithms and their implementation</p>
<dt><code>-q, &#8211;load-all</code></p>
<dd>(re-)load credentials, pools, authorities and connections</p>
<dt><code>-c, &#8211;load-conns</code></p>
<dd>(re-)load connection configuration</p>
<dt><code>-s, &#8211;load-creds</code></p>
<dd>(re-)load credentials</p>
<dt><code>-a, &#8211;load-pools</code></p>
<dd>(re-)load pool configuration</p>
<dt><code>-T, &#8211;log</code></p>
<dd>trace logging output</p>
<dt><code>-S, &#8211;stats</code></p>
<dd>show daemon infos and statistics</p>
<dt><code>-f, &#8211;flush-certs</code></p>
<dd>flush cached certificates</p>
<dt><code>-r, &#8211;reload-settings</code></p>
<dd>reload <a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a>(5) configuration</p>
<dt><code>-v, &#8211;version</code></p>
<dd>show daemon version information</p>
<dt><code>-h, &#8211;help</code></p>
<dd>show usage information</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-swanctl-conf/">swanctl.conf</a></code>(5) </p>
