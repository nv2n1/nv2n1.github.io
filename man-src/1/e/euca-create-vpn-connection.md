---
title: "euca-create-vpn-connection(1)"
name: "euca-create-vpn-connection"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-vpn-connection/"
description: "euca-create-vpn-connection – Create a VPN connection between a virtual private gateway and a customer gateway"
---

<h2>NAME</h2>
<p> euca-create-vpn-connection &#8211; Create a VPN connection between a virtual private gateway and a customer gateway</p>
<h2>SYNOPSIS</h2>
<p> euca-create-vpn-connection <code>-t</code> ipsec.1 <code>&#8211;customer-gateway</code> CGATEWAY</p>
<dl>
<dt><code>&#8211;vpn-gateway</code> VGATEWAY</p>
<dd> [&#8211;static-routes-only] [&#8211;format FORMAT] [&#8211;stylesheet STYLESHEET] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Create a VPN connection between a virtual private gateway and a customer gateway</p>
<h2>DESCRIPTION</h2>
<p> You can optionally format the connection information for specific devices using the <code>&#8211;format</code> or <code>&#8211;stylesheet</code> options. If the <code>&#8211;stylesheet</code> option is an HTTP or HTTPS URL it will be downloaded as needed.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> ipsec.1, <code>&#8211;type</code> ipsec.1</p>
<dd> the type of VPN connection to use (required)</p>
<dt><code>&#8211;customer-gateway</code> CGATEWAY</p>
<dd> ID of the customer gateway to connect (required)</p>
<dt><code>&#8211;vpn-gateway</code> VGATEWAY</p>
<dd> ID of the virtual private gateway to connect (required)</p>
<dt><code>&#8211;static-routes-only</code></p>
<dd> use only static routes instead of BGP</p>
<dt><code>&#8211;format</code> FORMAT</p>
<dd> show connection information in a specific format (cisco-ios-isr, juniper-junos-j, juniper-screenos-6.1, juniper-screenos-6.2, generic, xml, none) (default: xml)</p>
<dt><code>&#8211;stylesheet</code> STYLESHEET</p>
<dd> format the connection information using an XSL stylesheet. If the value contains &quot;{format}&quot; it will be replaced with the format chosen by the <code>&#8211;format</code> option. If the value is an HTTP or HTTPS URL it will be downloaded as needed. (default: value of &quot;vpnstylesheet&quot; region option)</p>
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
