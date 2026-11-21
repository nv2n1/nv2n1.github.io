---

title: "euca-delete-network-acl-entry(1)"
name: "euca-delete-network-acl-entry"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-delete-network-acl-entry/"
description: "euca-delete-network-acl-entry – Delete a network acl rule"
---

<h2>NAME</h2>
<p> euca-delete-network-acl-entry &#8211; Delete a network acl rule</p>
<p> euca-delete-network-acl-entry <code>-n</code> RULENUMBER [&#8211;egress]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] NACL</dd></dl>
<p> Delete a network acl rule</p>
<h3>positional arguments:</h3>
<dl>
<dt>NACL</dt>
<dd> ID of the network ACL to delete an entry from (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> RULENUMBER, <code>&#8211;rule-number</code> RULENUMBER</dt>
<dd> number of the entry to delete (required)</dd>
<dt><code>&#8211;egress</code></dt>
<dd> delete an egress entry (default: delete an ingress entry)</dd>
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
