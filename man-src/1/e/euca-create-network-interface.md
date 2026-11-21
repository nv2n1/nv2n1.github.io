---

title: "euca-create-network-interface(1)"
name: "euca-create-network-interface"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-create-network-interface/"
description: "euca-create-network-interface – Create a new VPC network interface"
---

<h2>NAME</h2>
<p> euca-create-network-interface &#8211; Create a new VPC network interface</p>
<p> euca-create-network-interface [-d DESC] [-g GROUP]</p>
<dl>
<dt>[&#8211;private-ip-address ADDRESS]</dt>
<dd> [&#8211;secondary-address ADDRESS | <code>&#8211;secondary-count</code> COUNT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] SUBNET</dd></dl>
<p> Create a new VPC network interface</p>
<h3>positional arguments:</h3>
<dl>
<dt>SUBNET</dt>
<dd> subnet to create the new network interface in (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> DESC, <code>&#8211;description</code> DESC</dt>
<dd> description for the new network interface</dd>
<dt><code>-g</code> GROUP, <code>&#8211;group</code> GROUP</dt>
<dd> ID of a security group to add the new network interface to. This option may be used more than once. Each time adds the network interface to an additional security group.</dd>
<dt><code>&#8211;private-ip-address</code> ADDRESS</dt>
<dd> assign a specific primary private IP address to the new network interface</dd>
<dt><code>&#8211;secondary-address</code> ADDRESS, <code>&#8211;secondary-private-ip-address</code> ADDRESS</dt>
<dd> assign a specific secondary private IP address to the new network interface. Use this option multiple times to add additional addresses.</dd>
<dt><code>&#8211;secondary-count</code> COUNT, <code>&#8211;secondary-private-ip-address-count</code> COUNT</dt>
<dd> automatically assign a specific number of secondary private IP addresses to the new network interface</dd>
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
