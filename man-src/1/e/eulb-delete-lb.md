---

title: "eulb-delete-lb(1)"
name: "eulb-delete-lb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-delete-lb/"
description: "eulb-delete-lb – Delete a load balancer"
---

<h2>NAME</h2>
<p> eulb-delete-lb &#8211; Delete a load balancer</p>
<p> eulb-delete-lb [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dl>
<dt>[&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger]</dt>
<dd> [&#8211;version] [-h] ELB</dd></dl>
<p> Delete a load balancer</p>
<h2>DESCRIPTION</h2>
<p> If the load balancer does not exist, this command still succeeds.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to delete (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> load balancing service endpoint URL</dd>
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
