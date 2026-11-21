---

title: "euca-describe-vpn-connections(1)"
name: "euca-describe-vpn-connections"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-vpn-connections/"
description: "euca-describe-vpn-connections – Show information about VPN connections"
---

<p> euca-describe-vpn-connections &#8211; Show information about VPN connections</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-vpn-connections [&#8211;format FORMAT]</p>
<dl>
<dt>[&#8211;stylesheet STYLESHEET]</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [VPNCONN [VPNCONN &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPN connections</p>
<h3>positional arguments:</h3>
<dl>
<dt>VPNCONN</dt>
<dd> limit results to specific VPN connections</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;format</code> FORMAT</dt>
<dd> show connection information in a specific format (cisco-ios-isr, juniper-junos-j, juniper-screenos-6.1, juniper-screenos-6.2, generic, xml, none) (default: none)</dd>
<dt><code>&#8211;stylesheet</code> STYLESHEET</dt>
<dd> format the connection information using an XSL stylesheet. If the value contains &quot;{format}&quot; it will be replaced with the format chosen by the <code>&#8211;format</code> option. If the value is an HTTP or HTTPS URL it will be downloaded as needed. (default: value of &quot;vpnstylesheet&quot; region option)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;filter</code> NAME=VALUE</dt>
<dd>
</dd><dd>restrict results to those that meet criteria</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd></dl>
<h3>allowed filter names:</h3>
<dl>
<dt>bgp-asn</dt>
<dd> the BGP AS number advertised by the customer gateway router</dd>
<dt>customer-gateway-configuration</dt>
<dd> connection information for the customer gateway</dd>
<dt>customer-gateway-id</dt>
<dd> ID of the connected customer gateway</dd>
<dt>state</dt>
<dd> the VPN connection&#8217;s state (available, deleting, deleted, pending)</dd>
<dt>option.static-routes-only</dt>
<dd> whether the VPN connection is restricted to static routes instead of using BGP</dd>
<dt>route.destination-cidr-block</dt>
<dd> the address block corresponding to the subnet used in the data center behind the customer gateway router</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the VPN connection</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the VPN connection</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>type</dt>
<dd> the type of virtual private gateway (ipsec.1)</dd>
<dt>vpn-connection-id</dt>
<dd> ID of the VPN connection</dd>
<dt>vpn-gateway-id</dt>
<dd> ID of the connected virtual private gateway </dd>
</dl>
