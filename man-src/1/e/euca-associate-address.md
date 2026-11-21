---

title: "euca-associate-address(1)"
name: "euca-associate-address"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-associate-address/"
description: "euca-associate-address – Associate an elastic IP address with a running instance"
---

<h2>NAME</h2>
<p> euca-associate-address &#8211; Associate an elastic IP address with a running instance</p>
<p> euca-associate-address [-a ALLOC] (<code>-i</code> INSTANCE | <code>-n</code> INTERFACE)</p>
<dl>
<dt>[-p ADDRESS]</dt>
<dd> [&#8211;allow-reassociation | <code>&#8211;no-allow-reassociation]</code> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ADDRESS]</dd></dl>
<p> Associate an elastic IP address with a running instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>ADDRESS</dt>
<dd> [Non-VPC only] IP address to associate (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-a</code> ALLOC, <code>&#8211;allocation-id</code> ALLOC</dt>
<dd> [VPC only] VPC allocation ID (required)</dd>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance-id</code> INSTANCE</dt>
<dd> ID of the instance to associate the address with</dd>
<dt><code>-n</code> INTERFACE, <code>&#8211;network-interface</code> INTERFACE</dt>
<dd> [VPC only] network interface to associate the address with</dd>
<dt><code>-p</code> ADDRESS, <code>&#8211;private-ip-address</code> ADDRESS</dt>
<dd> [VPC only] the private address to associate with the address being associated in the VPC (default: primary private IP)</dd>
<dt><code>&#8211;allow-reassociation</code></dt>
<dd> [VPC only] allow the address to be associated even if it is already associated with another interface</dd>
<dt><code>&#8211;no-allow-reassociation</code></dt>
<dd> [VPC only] do not allow the address to be associated if it is already associated with another interface</dd>
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
