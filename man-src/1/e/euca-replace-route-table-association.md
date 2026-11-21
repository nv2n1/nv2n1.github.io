---

title: "euca-replace-route-table-association(1)"
name: "euca-replace-route-table-association"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-replace-route-table-association/"
description: "euca-replace-route-table-association – Change the route table associated with a VPC subnet"
---

<h2>NAME</h2>
<p> euca-replace-route-table-association &#8211; Change the route table associated with a VPC subnet</p>
<p> euca-replace-route-table-association <code>-r</code> RTABLE [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] RTBASSOC</dd></dl>
<p> Change the route table associated with a VPC subnet</p>
<h3>positional arguments:</h3>
<dl>
<dt>RTBASSOC</dt>
<dd> ID of the route table association to replace (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> RTABLE</dt>
<dd> route table to associate with the subnet (required)</dd>
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
