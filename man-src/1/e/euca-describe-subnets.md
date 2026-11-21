---

title: "euca-describe-subnets(1)"
name: "euca-describe-subnets"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-subnets/"
description: "euca-describe-subnets – Show information about one or more VPC subnets"
---

<h2>NAME</h2>
<p> euca-describe-subnets &#8211; Show information about one or more VPC subnets</p>
<p> euca-describe-subnets [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [SUBNET [SUBNET &#8230;]]</dd></dl>
<p> Show information about one or more VPC subnets</p>
<h3>positional arguments:</h3>
<dl>
<dt>SUBNET</dt>
<dd> limit results to specific subnets</dd></dl>
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
<p> availability-zone available-ip-address-count</p>
<dl>
<dt>the number of unused IP addresses in the</dt>
<dd> subnet</dd>
<dt>cidr-block</dt>
<dd> the subnet&#8217;s CIDR address block</dd>
<dt>default-for-az</dt>
<dd> whether this is the default subnet for the availability zone state subnet-id tag-key key of a tag assigned to the subnet tag-value value of a tag assigned to the subnet tag:KEY specific tag key/value combination vpc-id the associated VPC&#8217;s ID </dd>
</dl>
