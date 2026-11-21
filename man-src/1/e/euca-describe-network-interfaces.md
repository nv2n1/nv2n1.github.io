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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [INTERFACE [INTERFACE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about VPC network interfaces</p>
<h3>positional arguments:</h3>
<dl>
<dt>INTERFACE</dt>
<dd> limit results to specific network interfaces</dd></dl>
<h3>optional arguments:</h3>
<dl>
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
<dt>addresses.private-ip-addresses</dt>
<dd> the interface&#8217;s private IP addresses</dd>
<dt>addresses.primary</dt>
<dd> whether the private IP address is the network interface&#8217;s primary IP address</dd>
<dt>addresses.association.public-ip</dt>
<dd> association ID for the network interface&#8217;s elastic IP address</dd>
<dt>addresses.association.owner-id</dt>
<dd> owner ID of the addresses associated with the network interface</dd>
<dt>association.association-id</dt>
<dd> association ID of the network interface&#8217;s IP Address</dd>
<dt>association.allocation-id</dt>
<dd> allocation ID of the network interface&#8217;s elastic IP address</dd>
<dt>association.ip-owner-id</dt>
<dd> owner ID of the network interface&#8217;s elastic IP address</dd>
<dt>association.public-ip</dt>
<dd> network interface&#8217;s elastic IP address</dd>
<dt>association.public-dns-name</dt>
<dd> network interface&#8217;s public DNS name</dd>
<dt>attachment.attachment-id</dt>
<dd> ID of the network interface&#8217;s attachment</dd>
<dt>attachment.instance-id</dt>
<dd> ID of the instance the network interface is attached to</dd>
<dt>attachment.instance-owner-id</dt>
<dd> owner ID of the instance the network interface is attached to</dd>
<dt>attachment.device-index</dt>
<dd> device index to which the network interface is attached</dd>
<dt>attachment.status</dt>
<dd> attachment status (attaching, attached, detaching, detached)</dd>
<dt>attachment.attach.time</dt>
<dd> time the network interface was attached</dd>
<dt>attachment.delete-on-termination</dt>
<dd> whether the attachment will be deleted when the associated instance is terminated</dd>
<dt>availability-zone</dt>
<dd> availability zone in which the network interface resides</dd>
<dt>description</dt>
<dd> network interface&#8217;s description</dd>
<dt>group-id</dt>
<dd> ID of a security group associated with the network interface</dd>
<dt>group-name</dt>
<dd> name of a security group associated with the network interface</dd>
<dt>mac-address</dt>
<dd> MAC (hardware) address</dd>
<dt>network-interface-id</dt>
<dd> ID of the network interface</dd>
<dt>owner-id</dt>
<dd> account ID of the network interface&#8217;s owner</dd>
<dt>private-ip-address</dt>
<dd> the network interface&#8217;s private address(es)</dd>
<dt>private-dns-name</dt>
<dd> the network interface&#8217;s private DNS name</dd>
<dt>requester-id</dt>
<dd> ID of the entity that created the network interface</dd>
<dt>requester-managed</dt>
<dd> whether the network interface is being managed by one of the cloud&#8217;s services</dd>
<dt>source-dest-check</dt>
<dd> whether the network interface&#8217;s traffic is subject to source/destination address checking</dd>
<dt>status</dt>
<dd> the interface&#8217;s status (available, in-use)</dd>
<dt>subnet-id</dt>
<dd> ID of the subnet in which the network interface resides</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the network interface</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the network interface</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>vpc-id</dt>
<dd> ID of the VPC in which the network interface resides </dd>
</dl>
