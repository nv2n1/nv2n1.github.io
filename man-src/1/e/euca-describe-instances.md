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
<p> euca-describe-instances [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [INSTANCE [INSTANCE &#8230;]]</dd></dl>
<p> Show information about instances</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> limit results to specific instances</dd></dl>
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
<dt>architecture</dt>
<dd> CPU architecture</dd>
<dt>association.allocation-id</dt>
<dd> [VPC only] allocation ID bound to a network interface&#8217;s elastic IP address</dd>
<dt>association.association-id</dt>
<dd> [VPC only] association ID returned when an elastic IP was associated with a network interface</dd>
<dt>association.ip-owner-id</dt>
<dd> [VPC only] ID of the owner of the elastic IP address associated with a network interface</dd>
<dt>association.public-ip</dt>
<dd> [VPC only] address of the elastic IP address bound to a network interface availability-zone block-device-mapping.attach-time volume attachment time</dd>
<dt>block-device-mapping.delete-on-termination</dt>
<dd> whether a volume is deleted upon instance termination</dd>
<dt>block-device-mapping.device-name</dt>
<dd> volume device name (e.g. <i>,/dev/sdf/</i>)</dd>
<dt>block-device-mapping.status</dt>
<dd> volume status</dd>
<dt>block-device-mapping.volume-id</dt>
<dd> volume ID</dd>
<dt>client-token</dt>
<dd> idempotency token provided at instance run time</dd>
<dt>dns-name</dt>
<dd> public DNS name</dd>
<dt>group-id</dt>
<dd> security group ID</dd>
<dt>group-name</dt>
<dd> security group name</dd>
<dt>hypervisor</dt>
<dd> hypervisor type</dd>
<dt>iam-instance-profile.arn</dt>
<dd> ARN of the instance&#8217;s instance profile</dd>
<dt>image-id</dt>
<dd> machine image ID</dd>
<dt>instance.group-id</dt>
<dd> security group ID</dd>
<dt>instance.group-name</dt>
<dd> security group name instance-id instance-lifecycle whether this is a spot instance instance-state-code numeric code identifying instance state instance-state-name instance state instance-type ip-address public IP address kernel-id kernel image ID key-name key pair name provided at instance launch time launch-index launch index within a reservation launch-time instance launch time monitoring-state monitoring state (&quot;enabled&quot; or &quot;disabled&quot;) network-interface.addresses.association.ip-owner-id</dd>
<dt>[VPC only] ID of the owner of the private IP</dt>
<dd> address associated with a network interface</dd>
<dt>network-interface.addresses.association.public-ip</dt>
<dd> [VPC only] ID of the association of an elastic IP address with a network interface</dd>
<dt>network-interface.addresses.primary</dt>
<dd> [VPC only] whether the IP address of the VPC network interface is the primary private IP address (&quot;true&quot; or &quot;false&quot;)</dd>
<dt>network-interface.addresses.private-ip-address</dt>
<dd> [VPC only] network interface&#8217;s private IP address</dd>
<dt>network-interface.attachment.device-index</dt>
<dd> [VPC only] device index to which a network interface is attached</dd>
<dt>network-interface.attachment.attach-time</dt>
<dd> [VPC only] time a network interface was attached to an instance</dd>
<dt>network-interface.attachment.attachment-id</dt>
<dd> [VPC only] ID of a network interface&#8217;s attachment</dd>
<dt>network-interface.attachment.delete-on-termination</dt>
<dd> [VPC only] whether a network interface attachment is deleted when an instance is terminated (&quot;true&quot; or &quot;false&quot;)</dd>
<dt>network-interface.attachment.instance-owner-id</dt>
<dd> [VPC only] ID of the instance to which a network interface is attached</dd>
<dt>network-interface.attachment.status</dt>
<dd> [VPC only] network interface&#8217;s attachment status</dd>
<dt>network-interface.availability-zone</dt>
<dd> [VPC only] network interface&#8217;s availability zone</dd>
<dt>network-interface.description</dt>
<dd> [VPC only] description of a network interface</dd>
<dt>network-interface.group-id</dt>
<dd> [VPC only] network interface&#8217;s security group ID</dd>
<dt>network-interface.group-name</dt>
<dd> [VPC only] network interface&#8217;s security group name</dd>
<dt>network-interface.mac-address</dt>
<dd> [VPC only] network interface&#8217;s hardware address</dd>
<dt>network-interface.network-interface.id</dt>
<dd> [VPC only] ID of a network interface</dd>
<dt>network-interface.owner-id</dt>
<dd> [VPC only] ID of a network interface&#8217;s owner</dd>
<dt>network-interface.private-dns-name</dt>
<dd> [VPC only] network interface&#8217;s private DNS name</dd>
<dt>network-interface.requester-id</dt>
<dd> [VPC only] network interface&#8217;s requester ID</dd>
<dt>network-interface.requester-managed</dt>
<dd> [VPC only] whether the network interface is managed by the service</dd>
<dt>network-interface.source-destination-check</dt>
<dd> [VPC only] whether source/destination checking is enabled for a network interface (&quot;true&quot; or &quot;false&quot;)</dd>
<dt>network-interface.status</dt>
<dd> [VPC only] network interface&#8217;s status</dd>
<dt>network-interface.subnet-id</dt>
<dd> [VPC only] ID of a network interface&#8217;s subnet</dd>
<dt>network-interface.vpc-id</dt>
<dd> [VPC only] ID of a network interface&#8217;s VPC</dd>
<dt>owner-id</dt>
<dd> instance owner&#8217;s account ID placement-group-name platform &quot;windows&quot; for Windows instances private-dns-name private-ip-address product-code product-code.type type of product code (&quot;devpay&quot; or &quot;marketplace&quot;)</dd>
<dt>ramdisk-id</dt>
<dd> ramdisk image ID</dd>
<dt>reason</dt>
<dd> reason for the instance&#8217;s current state</dd>
<dt>requester-id</dt>
<dd> ID of the entity that launched an instance</dd>
<dt>reservation-id</dt>
<dd> ID of the instance&#8217;s reservation</dd>
<dt>root-device-name</dt>
<dd> root device name (e.g. <i>,/dev/sda1/</i>)</dd>
<dt>root-device-type</dt>
<dd> root device type (&quot;ebs&quot; or &quot;instance-store&quot;) spot-instance-request-id state-reason-code reason code for the most recent state change state-reason-message message describing the most recent state change</dd>
<dt>subnet-id</dt>
<dd> [VPC only] ID of the subnet the instance is in</dd>
<dt>tag-key</dt>
<dd> name of any tag assigned to the instance</dd>
<dt>tag-value</dt>
<dd> value of any tag assigned to the instance</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination virtualization-type vpc-id [VPC only] ID of the VPC the instance is in </dd>
</dl>
