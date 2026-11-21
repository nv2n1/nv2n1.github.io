---

title: "euca-create-nat-gateway(1)"
name: "euca-create-nat-gateway"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-nat-gateway/"
description: "euca-create-nat-gateway – Create a new VPC NAT gateway"
---

<p> euca-create-nat-gateway &#8211; Create a new VPC NAT gateway</p>
<h2>SYNOPSIS</h2>
<p> euca-create-nat-gateway <code>-s</code> SUBNET <code>-a</code> ALLOC [&#8211;client-token TOKEN]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create a new VPC NAT gateway</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SUBNET, <code>&#8211;subnet-id</code> SUBNET</dt>
<dd> the subnet in which to create the new NAT gateway (required)</dd>
<dt><code>-a</code> ALLOC, <code>&#8211;allocation-id</code> ALLOC</dt>
<dd> the allocation ID of the Elastic IP address to associate with the NAT gateway (required)</dd>
<dt><code>&#8211;client-token</code> TOKEN</dt>
<dd> unique identifier to ensure request idempotency</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
