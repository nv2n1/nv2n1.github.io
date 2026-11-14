---
title: "euca-describe-instances(1)"
name: "euca-describe-instances"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-instances/"
description: "euca-describe-instances – Show information about instances"
---

<h2>NAME</h2>
<p> euca-describe-instances &#8211; Show information about instances</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-instances [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [INSTANCE [INSTANCE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about instances</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> limit results to specific instances</dl>
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
<dt>architecture</p>
<dd> CPU architecture</p>
<dt>association.allocation-id</p>
<dd> [VPC only] allocation ID bound to a network interface&#8217;s elastic IP address</p>
<dt>association.association-id</p>
<dd> [VPC only] association ID returned when an elastic IP was associated with a network interface</p>
<dt>association.ip-owner-id</p>
<dd> [VPC only] ID of the owner of the elastic IP address associated with a network interface</p>
<dt>association.public-ip</p>
<dd> [VPC only] address of the elastic IP address bound to a network interface availability-zone block-device-mapping.attach-time volume attachment time</p>
<dt>block-device-mapping.delete-on-termination</p>
<dd> whether a volume is deleted upon instance termination</p>
<dt>block-device-mapping.device-name</p>
<dd> volume device name (e.g. <i>,/dev/sdf/</i>)</p>
<dt>block-device-mapping.status</p>
<dd> volume status</p>
<dt>block-device-mapping.volume-id</p>
<dd> volume ID</p>
<dt>client-token</p>
<dd> idempotency token provided at instance run time</p>
<dt>dns-name</p>
<dd> public DNS name</p>
<dt>group-id</p>
<dd> security group ID</p>
<dt>group-name</p>
<dd> security group name</p>
<dt>hypervisor</p>
<dd> hypervisor type</p>
<dt>iam-instance-profile.arn</p>
<dd> ARN of the instance&#8217;s instance profile</p>
<dt>image-id</p>
<dd> machine image ID</p>
<dt>instance.group-id</p>
<dd> security group ID</p>
<dt>instance.group-name</p>
<dd> security group name instance-id instance-lifecycle whether this is a spot instance instance-state-code numeric code identifying instance state instance-state-name instance state instance-type ip-address public IP address kernel-id kernel image ID key-name key pair name provided at instance launch time launch-index launch index within a reservation launch-time instance launch time monitoring-state monitoring state (&quot;enabled&quot; or &quot;disabled&quot;) network-interface.addresses.association.ip-owner-id</p>
<dt>[VPC only] ID of the owner of the private IP</p>
<dd> address associated with a network interface</p>
<dt>network-interface.addresses.association.public-ip</p>
<dd> [VPC only] ID of the association of an elastic IP address with a network interface</p>
<dt>network-interface.addresses.primary</p>
<dd> [VPC only] whether the IP address of the VPC network interface is the primary private IP address (&quot;true&quot; or &quot;false&quot;)</p>
<dt>network-interface.addresses.private-ip-address</p>
<dd> [VPC only] network interface&#8217;s private IP address</p>
<dt>network-interface.attachment.device-index</p>
<dd> [VPC only] device index to which a network interface is attached</p>
<dt>network-interface.attachment.attach-time</p>
<dd> [VPC only] time a network interface was attached to an instance</p>
<dt>network-interface.attachment.attachment-id</p>
<dd> [VPC only] ID of a network interface&#8217;s attachment</p>
<dt>network-interface.attachment.delete-on-termination</p>
<dd> [VPC only] whether a network interface attachment is deleted when an instance is terminated (&quot;true&quot; or &quot;false&quot;)</p>
<dt>network-interface.attachment.instance-owner-id</p>
<dd> [VPC only] ID of the instance to which a network interface is attached</p>
<dt>network-interface.attachment.status</p>
<dd> [VPC only] network interface&#8217;s attachment status</p>
<dt>network-interface.availability-zone</p>
<dd> [VPC only] network interface&#8217;s availability zone</p>
<dt>network-interface.description</p>
<dd> [VPC only] description of a network interface</p>
<dt>network-interface.group-id</p>
<dd> [VPC only] network interface&#8217;s security group ID</p>
<dt>network-interface.group-name</p>
<dd> [VPC only] network interface&#8217;s security group name</p>
<dt>network-interface.mac-address</p>
<dd> [VPC only] network interface&#8217;s hardware address</p>
<dt>network-interface.network-interface.id</p>
<dd> [VPC only] ID of a network interface</p>
<dt>network-interface.owner-id</p>
<dd> [VPC only] ID of a network interface&#8217;s owner</p>
<dt>network-interface.private-dns-name</p>
<dd> [VPC only] network interface&#8217;s private DNS name</p>
<dt>network-interface.requester-id</p>
<dd> [VPC only] network interface&#8217;s requester ID</p>
<dt>network-interface.requester-managed</p>
<dd> [VPC only] whether the network interface is managed by the service</p>
<dt>network-interface.source-destination-check</p>
<dd> [VPC only] whether source/destination checking is enabled for a network interface (&quot;true&quot; or &quot;false&quot;)</p>
<dt>network-interface.status</p>
<dd> [VPC only] network interface&#8217;s status</p>
<dt>network-interface.subnet-id</p>
<dd> [VPC only] ID of a network interface&#8217;s subnet</p>
<dt>network-interface.vpc-id</p>
<dd> [VPC only] ID of a network interface&#8217;s VPC</p>
<dt>owner-id</p>
<dd> instance owner&#8217;s account ID placement-group-name platform &quot;windows&quot; for Windows instances private-dns-name private-ip-address product-code product-code.type type of product code (&quot;devpay&quot; or &quot;marketplace&quot;)</p>
<dt>ramdisk-id</p>
<dd> ramdisk image ID</p>
<dt>reason</p>
<dd> reason for the instance&#8217;s current state</p>
<dt>requester-id</p>
<dd> ID of the entity that launched an instance</p>
<dt>reservation-id</p>
<dd> ID of the instance&#8217;s reservation</p>
<dt>root-device-name</p>
<dd> root device name (e.g. <i>,/dev/sda1/</i>)</p>
<dt>root-device-type</p>
<dd> root device type (&quot;ebs&quot; or &quot;instance-store&quot;) spot-instance-request-id state-reason-code reason code for the most recent state change state-reason-message message describing the most recent state change</p>
<dt>subnet-id</p>
<dd> [VPC only] ID of the subnet the instance is in</p>
<dt>tag-key</p>
<dd> name of any tag assigned to the instance</p>
<dt>tag-value</p>
<dd> value of any tag assigned to the instance</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination virtualization-type vpc-id [VPC only] ID of the VPC the instance is in </p>
</dl>
<h2>Index</h2>
