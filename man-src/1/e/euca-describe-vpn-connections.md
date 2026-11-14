---
title: "euca-describe-vpn-connections(1)"
name: "euca-describe-vpn-connections"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-vpn-connections/"
description: "euca-describe-vpn-connections – Show information about VPN connections"
---

<h2>NAME</h2>
<p> euca-describe-vpn-connections &#8211; Show information about VPN connections</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-vpn-connections [&#8211;format FORMAT]</p>
<dl>
<dt>[&#8211;stylesheet STYLESHEET]</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [VPNCONN [VPNCONN &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPN connections</p>
<h3>positional arguments:</h3>
<dl>
<dt>VPNCONN</p>
<dd> limit results to specific VPN connections</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;format</code> FORMAT</p>
<dd> show connection information in a specific format (cisco-ios-isr, juniper-junos-j, juniper-screenos-6.1, juniper-screenos-6.2, generic, xml, none) (default: none)</p>
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
<dt><code>&#8211;filter</code> NAME=VALUE</p>
<dd>
<dd>restrict results to those that meet criteria</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</dl>
<h3>allowed filter names:</h3>
<dl>
<dt>bgp-asn</p>
<dd> the BGP AS number advertised by the customer gateway router</p>
<dt>customer-gateway-configuration</p>
<dd> connection information for the customer gateway</p>
<dt>customer-gateway-id</p>
<dd> ID of the connected customer gateway</p>
<dt>state</p>
<dd> the VPN connection&#8217;s state (available, deleting, deleted, pending)</p>
<dt>option.static-routes-only</p>
<dd> whether the VPN connection is restricted to static routes instead of using BGP</p>
<dt>route.destination-cidr-block</p>
<dd> the address block corresponding to the subnet used in the data center behind the customer gateway router</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the VPN connection</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the VPN connection</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>type</p>
<dd> the type of virtual private gateway (ipsec.1)</p>
<dt>vpn-connection-id</p>
<dd> ID of the VPN connection</p>
<dt>vpn-gateway-id</p>
<dd> ID of the connected virtual private gateway </p>
</dl>
<h2>Index</h2>
