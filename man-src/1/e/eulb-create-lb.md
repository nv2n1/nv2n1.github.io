---
title: "eulb-create-lb(1)"
name: "eulb-create-lb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-create-lb/"
description: "eulb-create-lb – Create a load balancer"
---

<h2>NAME</h2>
<p> eulb-create-lb &#8211; Create a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-create-lb (<code>-s</code> SUBNET1,SUBNET2,&#8230; | <code>-z</code> ZONE1,ZONE2,&#8230;) <code>-l</code></p>
<dl>
<dt>&quot;lb-port=PORT, protocol={HTTP,HTTPS,SSL,TCP},</p>
<dd> instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot; [-i internal] [-g GROUP1,GROUP2,&#8230;] [-t KEY=VALUE] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Create a load balancer</p>
<h2>DESCRIPTION</h2>
<p> After the load balancer is created, instances must be registered with it separately.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the new load balancer (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SUBNET1,SUBNET2,&#8230;, <code>&#8211;subnets</code> SUBNET1,SUBNET2,&#8230;</p>
<dd> [VPC only] subnets the load balancer should run in (required)</p>
<dt><code>-z</code> ZONE1,ZONE2,&#8230;, <code>&#8211;availability-zones</code> ZONE1,ZONE2,&#8230;</p>
<dd> [Non-VPC only] availability zones the load balancer should run in (required)</p>
<dt><code>-l</code> &quot;lb-port=PORT, protocol={HTTP,HTTPS,SSL,TCP}, instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot;, <code>&#8211;listener</code> &quot;lb-port=PORT, protocol={HTTP,HTTPS,SSL,TCP}, instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot;</p>
<dd> port/protocol settings for the load balancer, where lb-port is the external port number, protocol is the external protocol, instance-port is the back end server port number, instance-protocol is the protocol to use for routing traffic to back end instances, and cert-id is the ARN of the server certificate to use for encrypted connections. lb-port, protocol, and instance-port are required. This option may be used multiple times. (at least 1 required)</p>
<dt><code>-i</code> internal, <code>&#8211;scheme</code> internal</p>
<dd> [VPC only] &quot;internal&quot; to make the new load balancer private to a VPC</p>
<dt><code>-g</code> GROUP1,GROUP2,&#8230;, <code>&#8211;security-groups</code> GROUP1,GROUP2,&#8230;</p>
<dd> [VPC only] IDs of the security groups to assign to the new load balancer</p>
<dt><code>-t</code> KEY=VALUE, <code>&#8211;tag</code> KEY=VALUE</p>
<dd> key and value of a tag to add to the new load balancer</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> load balancing service endpoint URL</p>
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
