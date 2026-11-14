---
title: "euca-describe-network-interfaces(1)"
name: "euca-describe-network-interfaces"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-network-interfaces/"
description: "euca-describe-network-interfaces – Show information about VPC network interfaces"
---

<h2>NAME</h2>
<p> euca-describe-network-interfaces &#8211; Show information about VPC network interfaces</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-network-interfaces [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [INTERFACE [INTERFACE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPC network interfaces</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</p>
<dd> limit results to specific network interfaces</dl>
<h3>optional arguments:</h3>
<dl>
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
<dt>addresses.private-ip-addresses</p>
<dd> the interface&#8217;s private IP addresses</p>
<dt>addresses.primary</p>
<dd> whether the private IP address is the network interface&#8217;s primary IP address</p>
<dt>addresses.association.public-ip</p>
<dd> association ID for the network interface&#8217;s elastic IP address</p>
<dt>addresses.association.owner-id</p>
<dd> owner ID of the addresses associated with the network interface</p>
<dt>association.association-id</p>
<dd> association ID of the network interface&#8217;s IP Address</p>
<dt>association.allocation-id</p>
<dd> allocation ID of the network interface&#8217;s elastic IP address</p>
<dt>association.ip-owner-id</p>
<dd> owner ID of the network interface&#8217;s elastic IP address</p>
<dt>association.public-ip</p>
<dd> network interface&#8217;s elastic IP address</p>
<dt>association.public-dns-name</p>
<dd> network interface&#8217;s public DNS name</p>
<dt>attachment.attachment-id</p>
<dd> ID of the network interface&#8217;s attachment</p>
<dt>attachment.instance-id</p>
<dd> ID of the instance the network interface is attached to</p>
<dt>attachment.instance-owner-id</p>
<dd> owner ID of the instance the network interface is attached to</p>
<dt>attachment.device-index</p>
<dd> device index to which the network interface is attached</p>
<dt>attachment.status</p>
<dd> attachment status (attaching, attached, detaching, detached)</p>
<dt>attachment.attach.time</p>
<dd> time the network interface was attached</p>
<dt>attachment.delete-on-termination</p>
<dd> whether the attachment will be deleted when the associated instance is terminated</p>
<dt>availability-zone</p>
<dd> availability zone in which the network interface resides</p>
<dt>description</p>
<dd> network interface&#8217;s description</p>
<dt>group-id</p>
<dd> ID of a security group associated with the network interface</p>
<dt>group-name</p>
<dd> name of a security group associated with the network interface</p>
<dt>mac-address</p>
<dd> MAC (hardware) address</p>
<dt>network-interface-id</p>
<dd> ID of the network interface</p>
<dt>owner-id</p>
<dd> account ID of the network interface&#8217;s owner</p>
<dt>private-ip-address</p>
<dd> the network interface&#8217;s private address(es)</p>
<dt>private-dns-name</p>
<dd> the network interface&#8217;s private DNS name</p>
<dt>requester-id</p>
<dd> ID of the entity that created the network interface</p>
<dt>requester-managed</p>
<dd> whether the network interface is being managed by one of the cloud&#8217;s services</p>
<dt>source-dest-check</p>
<dd> whether the network interface&#8217;s traffic is subject to source/destination address checking</p>
<dt>status</p>
<dd> the interface&#8217;s status (available, in-use)</p>
<dt>subnet-id</p>
<dd> ID of the subnet in which the network interface resides</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the network interface</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the network interface</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>vpc-id</p>
<dd> ID of the VPC in which the network interface resides </p>
</dl>
<h2>Index</h2>
