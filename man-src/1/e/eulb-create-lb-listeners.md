---
title: "eulb-create-lb-listeners(1)"
name: "eulb-create-lb-listeners"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-create-lb-listeners/"
description: "eulb-create-lb-listeners – Add one or more listeners to a load balancer"
---

<h2>NAME</h2>
<p> eulb-create-lb-listeners &#8211; Add one or more listeners to a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-create-lb-listeners <code>-l</code> &quot;lb-port=PORT,</p>
<dl>
<dt>protocol={HTTP,HTTPS,SSL,TCP},</p>
<dd> instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot; [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Add one or more listeners to a load balancer</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> &quot;lb-port=PORT, protocol={HTTP,HTTPS,SSL,TCP}, instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot;, <code>&#8211;listener</code> &quot;lb-port=PORT, protocol={HTTP,HTTPS,SSL,TCP}, instance-port=PORT, instance-protocol={HTTP,HTTPS,SSL,TCP}, cert-id=ARN&quot;</p>
<dd> port/protocol settings for the load balancer, where lb-port is the external port number, protocol is the external protocol, instance-port is the back end server port number, instance-protocol is the protocol to use for routing traffic to back end instances, and cert-id is the ARN of the server certificate to use for encrypted connections. lb-port, protocol, and instance-port are required. This option may be used multiple times. (at least 1 required)</p>
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
