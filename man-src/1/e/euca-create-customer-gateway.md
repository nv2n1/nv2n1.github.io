---
title: "euca-create-customer-gateway(1)"
name: "euca-create-customer-gateway"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-customer-gateway/"
description: "euca-create-customer-gateway – Create a VPN customer gateway"
---

<h2>NAME</h2>
<p> euca-create-customer-gateway &#8211; Create a VPN customer gateway</p>
<h2>SYNOPSIS</h2>
<p> euca-create-customer-gateway <code>-t</code> ipsec.1 <code>-i</code> ADDRESS [-b ASN]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Create a VPN customer gateway</p>
<h2>DESCRIPTION</h2>
<p> This is the external side of a VPN connection. You will also need to create a virtual private gateway with <a href="/docs/linux/man/1-euca-create-vpn-gateway/">euca-create-vpn-gateway</a>(1).</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> ipsec.1, <code>&#8211;type</code> ipsec.1</p>
<dd> the type of VPN connection to use (required)</p>
<dt><code>-i</code> ADDRESS, <code>&#8211;ip</code> ADDRESS</p>
<dd> the new customer gateway&#8217;s cloud-facing IP address (required)</p>
<dt><code>-b</code> ASN, <code>&#8211;bgp-asn</code> ASN</p>
<dd> the new customer gateway&#8217;s BGP AS number</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
