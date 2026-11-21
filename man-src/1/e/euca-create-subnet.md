---

title: "euca-create-subnet(1)"
name: "euca-create-subnet"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-subnet/"
description: "euca-create-subnet – Create a new VPC subnet"
---

<p> euca-create-subnet &#8211; Create a new VPC subnet</p>
<h2>SYNOPSIS</h2>
<p> euca-create-subnet <code>-c</code> VPCID [-z ZONE] [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] CIDR</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create a new VPC subnet</p>
<h3>positional arguments:</h3>
<dl>
<dt>CIDR</dt>
<dd> CIDR address block for the new subnet (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> VPCID, <code>&#8211;vpc</code> VPCID</dt>
<dd> ID of the VPC to create the new subnet in (required)</dd>
<dt><code>-z</code> ZONE, <code>&#8211;availability-zone</code> ZONE</dt>
<dd> availability zone in which to create the new subnet</dd>
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
